# A sharp circular-gap sampling barrier for non-affine control-rate constraints

## Finding

For the sinusoidal time dilation used in pseudospectral optimal control, nodal enforcement of a physical-time control-rate bound can miss its maximum even when the pseudotime control is **affine** and its derivative is represented exactly. The complete, worst-case rate inflation over affine controls and an unknown dilation phase is governed solely by the **largest cyclic gap** between collocation nodes. Equispaced phases uniquely minimize this worst-case inflation for a prescribed node count.

Let \(S\subset[0,1)\) consist of \(N\ge1\) distinct normalized collocation phases, with \(0\) identified with \(1\). Write \(g(S)\in(0,1]\) for the maximum of the \(N\) successive circular gaps, counting the wrap-around gap. For a time-map amplitude \(0<a<1\), define

\[
F_S(a,c)=\frac{1-a\max_{s\in S}\cos(2\pi(s-c))}{1-a}.
\]

Then the exact continuous-to-nodal control-rate amplification on affine pseudotime controls, maximized over the mapping phase, is

\[
\boxed{\sup_{0\le c\le1}F_S(a,c)=\frac{1-a\cos(\pi g(S))}{1-a}.}
\]

Moreover,

\[
\boxed{\inf_{|S|=N}\sup_{0\le c\le1} F_S(a,c)=\frac{1-a\cos(\pi/N)}{1-a}.}
\]

Equality in the infimum holds if and only if the phases are equally spaced, up to a common rotation. For the two-node flipped Legendre–Gauss–Radau (fLGR) mesh \(\tau\in\{-1/3,1\}\), the gap is \(2/3\), and the exact amplification is \((1+a/2)/(1-a)\). At \(a=9/10\) it is \(29/2=14.5\).

## Assumptions and scope

Consider a pseudotime interval \(-1\le\tau\le1\), normalized coordinate \(\sigma=(1+\tau)/2\), and an increasing physical-time transformation \(t=t_0+Ts(\tau;a,c)\), where \(T>0\) and

\[
s(\tau;a,c)=\sigma-\frac{a}{2\pi}\left[\sin(2\pi(\sigma-c))+\sin(2\pi c)\right],
\]

\[
\rho(\tau)=\frac{dt}{d\tau}=\frac T2\left[1-a\cos(2\pi(\sigma-c))\right]>0.
\]

The control \(u(\tau)=u_0+K\tau\), with \(u_0,K\in\mathbb R\), is interpreted as the continuous interpolant in pseudotime. For a physical slew-rate limit \(R>0\), enforce \(|du/dt|\le R\) at exactly the \(N\) collocation nodes, and nowhere else. The theorem concerns this affine-control subspace; no claim is made for general high-degree controls, arbitrary nonlinear time maps, or overall optimality of a discretized control problem. The strict positivity of \(\rho\) guarantees that the physical-time control is continuously differentiable.

## Proof

**1. Exact rate ratio and saturation.** By the chain rule, \(|du/dt|=|K|/\rho(\tau)\). The nodal inequalities are therefore equivalent to

\[
|K|\le R\min_{s\in S}\frac T2[1-a\cos(2\pi(s-c))].
\]

The global minimum of the dilation over the full interval is \((T/2)(1-a)\), attained at \(\sigma=c\) (and at equivalent endpoints). Consequently, every nodally admissible affine control obeys

\[
\frac{\sup_{t\in[t_0,t_0+T]}|du/dt|}{R}\le F_S(a,c).
\]

Equality is attained by either sign of \(K=R\min_{s\in S}\rho(2s-1)\). The freedom in \(u_0\) does not affect the conclusion. In particular, this is the **exact norm of the nodal-to-continuous rate bound** on the affine subspace, not merely an existence example.

**2. Circular gap law.** Let \(\delta_S(c)=\min_{s\in S}\operatorname{dist}_{\mathbb T}(s,c)\) be the closest circular distance, with \(0\le\delta_S(c)\le1/2\). Since the cosine is decreasing on \([0,\pi]\),

\[
\max_{s\in S}\cos(2\pi(s-c))=\cos(2\pi\delta_S(c)).
\]

For any interval between neighboring phases with length \(g\), the farthest point from the set in that interval is its midpoint, at distance \(g/2\). Hence \(\max_c\delta_S(c)=g(S)/2\). The function \(1-a\cos(2\pi\delta)\) increases for \(0\le\delta\le1/2\), yielding the first boxed equality and its attaining phase.

**3. Minimax sampling and uniqueness.** The nonnegative cyclic gaps add to one, so \(g(S)\ge1/N\). Equality holds exactly when all gaps equal \(1/N\), i.e. the sampling phases form a rotated equispaced grid. Because \(a>0\) and \(\cos(\pi g)\) strictly decreases for \(0<g<1\), the minimax value and uniqueness follow.

**4. Exact flipped-Radau instance.** The two-point right-endpoint Radau nodes are \(\tau=-1/3,1\) (equivalently the roots of \(P_2-P_1\)). Their normalized phases are \(1/3,0\), leaving gaps \(1/3\) and \(2/3\). The worst mapping center is \(c=2/3\), where both sampled cosines equal \(-1/2\). Set \(K=R(T/2)(1+a/2)\). Both nodal rate bounds are saturated, while at \(\sigma=2/3\) the continuous slew rate equals \(R(1+a/2)/(1-a)\). This proves sharpness and the stated value \(29/2\).

**5. A design corollary.** When \(1<C<(1+a)/(1-a)\), an equispaced grid guarantees the continuous rate is at most \(CR\) for every phase and affine control satisfying the nodal bound if and only if

\[
N\ge\frac{\pi}{\arccos\!\left(1-\frac{(C-1)(1-a)}{a}\right)}.
\]

The smallest integer grid size is the ceiling of the right side. When \(C\ge(1+a)/(1-a)\), one node suffices. In particular, for fixed \(a\in(0,1)\), \(F_N^*(a)-1=\frac{a\pi^2}{2(1-a)N^2}+O(N^{-4})\) as \(N\to\infty\); at fixed finite \(N\), the worst-phase factor becomes unbounded as \(a\uparrow1\). Enforcing the nodal rate bound tightened from \(R\) to \(R/F_S(a,c)\) is necessary and sufficient for a uniform continuous rate guarantee for affine controls at a given phase; the phase-uniform factor is given by the first boxed result.

## Verification

The accompanying standard-library program `checker.py` reconstructs cyclic gaps, evaluates exact saturation phases, checks the minimizing property of equispaced meshes, and compares direct time-dilation ratios with the analytical formulas for seeded random finite meshes. It also verifies the two-node Radau ratio \(29/2\) in exact rational arithmetic. Run `python checker.py` to reproduce its recorded finite assertions. These computations support the identities but are **not** the proof of the universal or minimax statements; those are proved above.

## Relationship to prior work

Minnozzi and Sagliano (2026), Section 3, Eqs. (38), (40), and (42), impose time-derivative and control-rate bounds **at collocation nodes**; Section 5.1.1, Eqs. (74)–(75), specifies precisely the sinusoidal time mapping analyzed here. Their displayed experiments treat non-affine mapping without a finite thrust-rate constraint and test finite thrust-rate constraints separately with an affine map (Section 5.1.2). The present result makes no claim to discovering direct rate constraints or time mapping: it derives an exact continuous-feasibility sampling factor when these published ingredients are combined on the affine-control subspace.

Hager et al. (2016) study collocation convergence under control constraints, not the sharp worst-phase rate factor for this time map. Elgindy and Refat (2022) study parametric mapping and collocation convergence for infinite-horizon controls, but not this finite-interval harmonic slew-rate minimax factor. The general circular-covering argument is elementary and is used as a tool; no claim is made to have invented circle covering.

## Limitations

No assertion is made about optimizer outputs, high-degree polynomial controls, continuous-time feasibility of all state/path constraints, or control amplitudes. The sharpness witness controls only the slew-rate inequalities; other constraints of a particular optimal control problem may rule it out. The optimal mesh refers to arbitrary phases on a circle, not the optimally weighted Radau quadrature mesh, and is a benchmark rather than a prescription for replacing Radau nodes. Historical priority for an equivalent specialized harmonic-warp bound is not exhaustively established. Independently reproduced mathematical assessment remains outstanding.

## References

1. R. Minnozzi and M. Sagliano, *Theoretical and Computational Advances in Birkhoff Pseudospectral Transcription for Aerospace Optimal Control*, arXiv:2610.17842, first public October 13, 2026. https://arxiv.org/abs/2610.17842
2. W. W. Hager, J. Liu, S. Mohapatra, A. V. Rao, X.-S. Wang, *Convergence rate for a Gauss collocation method applied to constrained optimal control*, arXiv:1607.02798 (2016). https://arxiv.org/abs/1607.02798
3. K. T. Elgindy and H. M. Refat, *A Direct Integral Pseudospectral Method for Solving a Class of Infinite-Horizon Optimal Control Problems Using Gegenbauer Polynomials and Certain Parametric Maps*, arXiv:2207.05467 (2022). https://arxiv.org/abs/2207.05467
4. Y. Nie and E. C. Kerrigan, *Efficient Implementation of Rate Constraints for Nonlinear Optimal Control*, IEEE Trans. Automatic Control 66 (2021), 329–334, DOI:10.1109/TAC.2020.2976051. The full primary text was not available for direct comparison.
