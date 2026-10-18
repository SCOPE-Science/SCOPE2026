# A unique symplectic timestep and sharp modal-energy reversal in projected RK4

## Finding

For two independent planar harmonic oscillators of distinct positive angular frequencies \(0<\omega_1<\omega_2\), the classical four-stage, fourth-order Runge–Kutta (RK4) method followed by the **one-invariant quasi-orthogonal projection** of Najafian–Vermeire (2024), preserving only the sum of the two oscillator energies, has one and only one positive step length at which it is symplectic on the fully excited phase space. That step length is
\[
h_*^2=\frac{8(\omega_2^6-\omega_1^6)}{\omega_2^8-\omega_1^8}.
\]
At exactly this step length the projected map is a linear product of planar rotations and preserves **each** modal energy exactly, although RK4 itself dissipates each modal energy. At every other positive step length the projected map is nonsymplectic, and for every initial state with both modes nonzero it transfers its exactly conserved total energy asymptotically to just one mode: to the **slower** mode when \(0<h<h_*\), and to the **faster** mode when \(h>h_*\). The reversal occurs **strictly inside** RK4's two-mode absolute-stability window \(0<h<\sqrt 8/\omega_2\), not only after the underlying RK step has become unstable.

More precisely, with \(E_j^{(n)}=\|z_j^{(n)}\|_2^2\), the exact ratio at every integer step \(n\ge0\) is
\[
\frac{E_2^{(n)}}{E_1^{(n)}}=\frac{E_2^{(0)}}{E_1^{(0)}}\left[\frac{Q(\omega_2 h)}{Q(\omega_1 h)}\right]^n,
\qquad Q(x)=1+\frac{x^6(x^2-8)}{576}>0.
\]
Hence the phase transition is a statement about the entire infinite discrete orbit, not just the first numerical step.

## Assumptions and scope

Work in exact real arithmetic. Let \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), let \(A=\operatorname{diag}(\omega_1J,\omega_2J)\), and solve \(\dot z=Az\) on \(\mathbb R^4\). Both frequencies are fixed, positive, and distinct; the fixed timestep \(h\) is strictly positive. Set \(G(z)=\|z\|_2^2/2\); this is an invariant of the continuous system, as are the *separate* actions \(I_j(z)=\|z_j\|_2^2/2\). The numerical scheme enforces **only** \(G\): obtain the classical RK4 predictor \(y\); project its gradient \(\nabla G(y)=y\) into the linear span of the four RK4 stage derivatives; correct along that projected unit gradient using the real root of \(G(z^+)=G(z)\) with the smallest correction magnitude. Both initial modal amplitudes are assumed nonzero to state strict asymptotic transfers, stage full rank, and the symplecticity criterion on the open subset \(\{z:\|z_1\|\|z_2\|>0\}\). The corrected map has an obvious continuous extension to the coordinate axes and to the origin.

## Proof

**1. Stage-space saturation and the exact projection.** The four classical RK4 stage derivatives for the linear system are
\[
\begin{aligned}
k_1&=Az,\\
k_2&=Az+\tfrac h2A^2z,\\
k_3&=Az+\tfrac h2A^2z+\tfrac{h^2}{4}A^3z,\\
k_4&=Az+hA^2z+\tfrac{h^2}{2}A^3z+\tfrac{h^3}{4}A^4z.
\end{aligned}
\]
Writing \(z=(u,v,p,q)^\mathsf T\), direct expansion yields the exact determinant
\[
\det[k_1,k_2,k_3,k_4]=\frac{h^6}{32}\omega_1^3\omega_2^3(\omega_2^2-\omega_1^2)^2(u^2+v^2)(p^2+q^2)>0.
\]
Thus the stage span is all \(\mathbb R^4\). The quasi-orthogonal projected gradient is exactly \(y\), and the smaller projection root yields
\[
\boxed{\quad z^+=\frac{\|z\|_2}{\|y\|_2}\,y,\qquad y=R(hA)z,\quad R(\xi)=1+\xi+\tfrac{\xi^2}{2}+\tfrac{\xi^3}{6}+\tfrac{\xi^4}{24}.\quad}
\]
The denominator never vanishes for nonzero \(z\). Indeed, the real and imaginary parts of \(R(ix)\) are \(1-x^2/2+x^4/24\) and \(x-x^3/6\), which have no common real root; equivalently \(Q(x)=|R(ix)|^2>0\) for all real \(x\). The two modes thus remain nonzero at every step, so the reduction is valid inductively forever.

**2. Exact action map.** Since every \(R(h\omega_jJ)\) is a planar rotation followed by a positive scalar factor \(\sqrt{Q(\omega_jh)}\), put \(Q_j=Q(\omega_jh)\). The projected energies satisfy
\[
E_j^+=\frac{(E_1+E_2)Q_jE_j}{Q_1E_1+Q_2E_2},\qquad E_1^++E_2^+=E_1+E_2.
\]
Dividing proves the exact ratio formula. Its iteration gives exponential convergence of the normalized energy distribution to mode 1 if \(Q_1>Q_2\), or to mode 2 if \(Q_2>Q_1\). If \(Q_1=Q_2\), each action is constant at every step.

**3. Unique switching threshold and stability window.** An exact factorization is
\[
Q(\omega_2h)-Q(\omega_1h)=\frac{h^6(\omega_2^8-\omega_1^8)}{576}(h^2-h_*^2).
\]
Because \(\omega_2>\omega_1>0\), the sign reverses *once* at the displayed positive \(h_*\). Furthermore,
\[
\frac{\omega_2^2 h_*^2}{8}=\frac{1-(\omega_1/\omega_2)^6}{1-(\omega_1/\omega_2)^8}<1.
\]
The last strict inequality locates the switch below \(\sqrt 8/\omega_2\), where the unprojected classical RK4 multipliers of both modes have modulus below one (their squared moduli are \(Q_j<1\)).

**4. Symplecticity if and only if the modes balance.** On the open set of nonzero modal actions introduce standard action-angle coordinates \((I_1,I_2,\theta_1,\theta_2)\), where the canonical two-form is \(dI_1\wedge d\theta_1+dI_2\wedge d\theta_2\), up to one common fixed orientation convention. The scheme shifts each angle by \(\arg R(i\omega_jh)\), independent of the actions, and maps
\[
(I_1,I_2)\longmapsto\left(\frac{(I_1+I_2)Q_1I_1}{Q_1I_1+Q_2I_2},\frac{(I_1+I_2)Q_2I_2}{Q_1I_1+Q_2I_2}\right).
\]
For symplecticity with action-independent angle shifts, the derivative of this action map must equal the identity. At \(I_1=I_2>0\) its action-Jacobian determinant is
\[
\frac{4Q_1Q_2}{(Q_1+Q_2)^2},
\]
which is strictly below \(1\) whenever \(Q_1\ne Q_2\). Hence every \(h\ne h_*\) violates symplecticity on the fully excited domain (and even fails local volume preservation at equal actions). At \(h=h_*\), write \(Q_1=Q_2=Q\). The projection factor becomes the *constant* \(Q^{-1/2}\), so the entire map is \(Q^{-1/2}R(hA)\), an orthogonal block-diagonal product of planar rotations. It is therefore symplectic and fixes both actions. The factorization in step 3 establishes uniqueness among positive steps.

**5. Exact rational benchmark.** For \((\omega_1,\omega_2)=(1,2)\), the unique squared timestep is \(h_*^2=168/85\), and both unprojected modal squared multipliers equal \(47985841/52200625<1\). The global projection cancels their identical attenuation exactly. On either side of this step, the modal ratio respectively decreases or increases geometrically, while the same total energy is conserved.

## Verification

The standalone `verify.py` reproduces symbolically the RK4 stability polynomial, the determinant of all four stage derivatives, the exact factorization defining the threshold, positivity of the RK4 multiplier, the rational benchmark, and the action-map Jacobian. It additionally compares direct RK4 stages and radial projections against the modal recursion in 150 deterministic scalar comparisons. Execute `python verify.py` from the extracted package and compare with `verify_output.txt`. Analytic factorization and the action-angle argument, not finite sampling, justify the all-step and symplecticity statements.

## Relationship to prior work

Najafian and Vermeire, *Quasi-Orthogonal Runge-Kutta Projection Methods* (arXiv:2409.18328v1, published September 26, 2024), define precisely the stage-space gradient projection used here and establish generic small-step solvability/order results. They already note explicitly that if the stage space fills the state space, quasi-orthogonal projection reduces to ordinary orthogonal projection, and they experiment with a two-dimensional nonlinear oscillator. Their results do **not** give the two-distinct-frequency modal ratio, unique finite positive symplectic timestep, or its internal-RK4-stability-window reversal.

An earlier energy-quadratization/orthogonal-projection Runge–Kutta construction of Jiang, Gong, and Wang (arXiv:2001.00774, first publicly available January 2020) already uses normalized quadratic-energy projection. Therefore neither the radial correction nor conservation of the sum of energies is new. Its general energy-conservation and accuracy assertions, however, do not entail the present exact frequency-dependent crossover or the iff symplecticity classification. This finding supplies those additional assertions for a fully specified four-dimensional model; it does not attribute the projection technique to itself.

## Limitations

Only two distinct, independently excited planar oscillators, classical RK4, fixed positive step lengths, and a *single* Euclidean quadratic-energy invariant are addressed. Multiple-invariant quasi-orthogonal projection, noncommuting systems, nonlinear Hamiltonians, other tableaux, high-dimensional stage spans, and rounding-induced drift are not covered. Even at \(h=h_*\) the numerical rotation angles differ in general from the exact frequencies, so symplecticity and modal-energy preservation do not mean exact trajectories. A similar resonance may have appeared under older orthogonal-projection or postprocessing terminology; the checked literature does not certify absolute priority.

## References

1. M. R. Najafian and B. C. Vermeire, *Quasi-Orthogonal Runge-Kutta Projection Methods*, arXiv:2409.18328v1, September 26, 2024. https://arxiv.org/html/2409.18328v1. See §2, (2.2)–(2.5), Remarks 3–4, and §3.2.
2. C. Jiang, Y. Gong, and Y. Wang, *Explicit high-order energy-preserving methods for general Hamiltonian partial differential equations*, arXiv:2001.00774, January 2020. https://arxiv.org/abs/2001.00774. See quadratic-energy orthogonal-projection construction, Scheme 3.1.
3. E. Hairer, S. Nørsett, and G. Wanner, *Solving Ordinary Differential Equations I*, Springer, chapters on classical RK4 and stability polynomials (standard background).
