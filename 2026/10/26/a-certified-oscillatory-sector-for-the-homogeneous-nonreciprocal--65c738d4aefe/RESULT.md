# A certified oscillatory sector for the homogeneous nonreciprocal Ising flow

## Finding

Consider the spatially homogeneous, fully antisymmetric two-species mean-field equation
\[
\dot x=-x+\tanh(Jx+Ky),\qquad
\dot y=-y+\tanh(Jy-Kx).
\]
For every \(J>1\) and \(K\ge J-1\), the origin is the **only equilibrium** in the entire plane, is a repelling focus, and **every nonzero solution has a periodic orbit as its complete omega-limit set**. Thus this explicit unbounded coupling sector is necessarily oscillatory; no nonzero static magnetization attractor or nonperiodic omega-limit set is possible within the deterministic planar equation.

In the strong nonreciprocity sub-sector \(K>J\), every nonzero solution rotates strictly clockwise after it enters the physical magnetization square, and every periodic orbit has least period \(T\) satisfying the explicit bounds
\[
\frac{2\pi}{\sqrt{J^2+K^2}}
<T<\frac{2\pi(J+K)}{(K-J)\tanh(J+K)}.
\]
The conclusion is **not** a uniqueness theorem for periodic orbits, a sharp phase boundary, or a theorem about noisy finite-dimensional lattice systems.

## Assumptions and scope

The time variable has been rescaled so that the single-spin relaxation coefficient is one. Both couplings \(J,K\) are real and satisfy \(J>1\) and \(K\ge J-1>0\). The spatially homogeneous two-dimensional ODE is defined on all \(\mathbb R^2\); its physically relevant invariant square is \([-1,1]^2\). Solutions are classical for arbitrary deterministic initial data, and \(\omega(z_0)\) denotes the full forward omega-limit set of the orbit starting at \(z_0=(x_0,y_0)\). A periodic orbit is a nonconstant closed solution curve. The second assertion assumes \(K>J\), with period measured in these rescaled time units.

## Proof

**1. Boundedness and the repelling focus.** For each coordinate, \(-1-x\le\dot x\le1-x\) and \(-1-y\le\dot y\le1-y\). Thus every forward orbit is bounded. On the faces of \([-1,1]^2\), the vector field points strictly inward, and every periodic orbit lies strictly in its interior: a maximum or minimum of either coordinate on a periodic orbit must equal a hyperbolic tangent and hence has absolute value less than one. The Jacobian at the origin equals
\[
\begin{pmatrix}J-1&K\\-K&J-1\end{pmatrix},
\]
with eigenvalues \(J-1\pm iK\). Since \(J>1\), there is a punctured disk in which the radial derivative is strictly positive. Thus the origin cannot be the forward limit of a nonzero orbit; each such orbit is eventually confined to some compact annulus bounded away from zero.

**2. Excluding other fixed points.** Every equilibrium has \(|x|,|y|<1\). If one coordinate vanishes, so does the other. Suppose both are nonzero and define, with the value at zero interpreted continuously,
\[
F_J(u)=\frac{\operatorname{arctanh}u}{u}-J.
\]
The map \(u\mapsto\operatorname{arctanh}(u)/u\) is strictly increasing in \(|u|\in(0,1)\), from \(1\) to infinity. There is consequently a unique \(m_J\in(0,1)\) with \(F_J(m_J)=0\). Furthermore \(F_J(u)<0\) exactly when \(0<|u|<m_J\), and \(|F_J(u)|<J-1\) whenever \(F_J(u)<0\). Applying the inverse hyperbolic tangent to the equilibrium equations gives
\[
xF_J(x)=Ky,\qquad yF_J(y)=-Kx,
\]
so \(F_J(x)F_J(y)=-K^2\). Exactly one factor is negative. If \(F_J(x)<0\), then \(|x|<m_J\) and
\[
|y|=\frac{|x|\,|F_J(x)|}{K}
<\frac{m_J(J-1)}K\le m_J,
\]
contradicting \(F_J(y)>0\). Interchanging coordinates handles the other possible sign. Thus the origin is the only equilibrium, including at \(K=J-1\).

**3. Every nonzero omega-limit is periodic.** Boundedness makes every forward omega-limit nonempty, compact, and connected. Near the repelling hyperbolic focus, choose a sufficiently small circle on which \(d(x^2+y^2)/dt>0\). An orbit outside cannot cross inward; any orbit starting inside except at the origin crosses this circle in finite time, since the radial growth is uniformly positive relative to radius in the punctured disk. Every nonzero orbit therefore has a compact omega-limit set free of equilibria. The planar Poincare--Bendixson theorem implies that this whole omega-limit set is one periodic orbit. This proves the first assertion for every initial condition except the fixed point itself.

**4. Strict clockwise rotation.** Put \(a=Jx+Ky\), \(b=Jy-Kx\), \(D=J^2+K^2\), and \(r^2=x^2+y^2=(a^2+b^2)/D\). For \(r>0\), differentiating the polar angle gives the exact identity
\[
\dot\theta=\frac{J[a\tanh b-b\tanh a]-K[a\tanh a+b\tanh b]}{Dr^2}.
\]
The elementary **strict angular inequality**
\[
|a\tanh b-b\tanh a|<a\tanh a+b\tanh b\qquad((a,b)\ne(0,0))
\]
follows as follows. By absolute values and interchange, write \(A=|a|\ge B=|b|\ge0\), \(U=\tanh A\ge V=\tanh B\ge0\). Since \(s\mapsto\tanh(s)/s\) decreases on positive numbers, \(AV\ge BU\); therefore the left side is \(AV-BU\), whereas the right side is \(AU+BV\). Their difference is \(A(U-V)+B(U+V)>0\) (with the case \(B=0\) also strict). It follows that for \(K\ge J>0\), \(\dot\theta<0\).

**5. Quantitative period bounds.** If \(K>J\), the same inequality implies
\[
-\dot\theta>\frac{K-J}{Dr^2}(a\tanh a+b\tanh b).
\]
On any periodic orbit, \(|x|,|y|<1\), so \(|a|,|b|<J+K\). The decrease of \(\tanh(s)/s\) gives
\[
a\tanh a+b\tanh b\ge
\frac{\tanh(J+K)}{J+K}(a^2+b^2),
\]
and therefore \(-\dot\theta>(K-J)\tanh(J+K)/(J+K)\). Conversely, strict \(|\tanh s|<|s|\) for nonzero \(s\), Cauchy--Schwarz, and \(a^2+b^2=Dr^2\) imply \(|\dot\theta|<\sqrt D\). Every simple planar periodic orbit contains a fixed point in its interior (index one); here that point can only be the origin. Consequently its strictly clockwise angle decreases by exactly \(2\pi\) in one least period. Integrating the two strict angular inequalities yields the displayed bounds on \(T\).

## Verification

The companion `VERIFY.py` independently evaluates the strict scalar angular inequality at 50,000 pseudorandom real pairs, searches equilibria numerically from 175 starts across seven parameter regimes, and checks 7,000 long-time angular speeds against the proven inequalities. It prints three PASS lines when run with NumPy and SciPy. These finite computations corroborate but do not prove equilibrium uniqueness, omega-limit classification, or global period bounds. The analytical proof above supplies the infinite-domain arguments and includes the boundary case \(K=J-1\).

## Relationship to prior work

The nonreciprocal Ising mean-field model and its disorder, swap-cycle, and static-order phases were introduced and studied by Avni and collaborators, first released November 9, 2023, with an extensive follow-up released September 2, 2024 [1,2]. The follow-up's homogeneous mean-field Sec. IV--V derives the equations, plots the fixed points numerically, and analyzes Hopf and SNIC bifurcations. The contribution here is the nonperturbative explicit entire-sector theorem \(J>1, K\ge J-1\), its **every-initial-condition** omega-limit conclusion, and the quantitative strong-coupling period bounds; it neither claims to discover the swap phase nor changes the established mean-field equations.

Seung, Richardson, Lagarias, and Hopfield [3] investigate broader antisymmetric excitatory-inhibitory networks and establish *global fixed-point stability* under sufficient dissipativity assumptions. Their result does not imply universal oscillatory omega-limits in the stated strong-coupling sector; their discussion identifies sufficient conditions for oscillatory behavior as a separate problem. Blom, Thiele, and Godec [4] develop a more detailed correlated-lattice approximation and local-order onset criterion; their results do not provide the stated exact global theorem for this specific spatially homogeneous planar flow.

## Limitations

The inequality \(K\ge J-1\) is a sufficient oscillation region, **not** a claim that its boundary is the exact physical static-to-swap phase transition. Existence and omega-limit periodicity do not imply uniqueness, uniform orbital convergence rates, or structural stability under perturbations. The numerical period bounds are not claimed sharp. All statements concern the deterministic spatially homogeneous mean-field ODE, not spatially extended stochastic lattice dynamics, finite-size Monte Carlo trajectories, or systems with delayed interaction. An unrecognized earlier general theorem for two-neuron antisymmetric sigmoidal systems could have this result as a corollary; publication-priority certainty requires independent review.

## References

[1] Y. Avni, M. Fruchart, D. Martin, D. Seara, V. Vitelli, *Nonreciprocal Ising model*, arXiv:2311.05471, initially public 2023-11-09. https://arxiv.org/abs/2311.05471

[2] Y. Avni et al., *Dynamical phase transitions in the nonreciprocal Ising model*, arXiv:2409.07481, initially public 2024-09-02; inspect especially Secs. IV.3, V.2 and Appendix D. https://arxiv.org/html/2409.07481v2

[3] H. S. Seung, T. J. Richardson, J. C. Lagarias, J. J. Hopfield, *Minimax and Hamiltonian Dynamics of Excitatory-Inhibitory Networks*, NeurIPS 10 (1997), pp. 329--335. https://papers.neurips.cc/paper_files/paper/1997/file/3d779cae2d46cf6a8a99a35ba4167977-Paper.pdf

[4] K. Blom, U. Thiele, A. Godec, *Local order controls the onset of oscillations in the nonreciprocal Ising model*, arXiv:2407.20312, 2024; Phys. Rev. E 111, 024207 (2025). https://arxiv.org/abs/2407.20312
