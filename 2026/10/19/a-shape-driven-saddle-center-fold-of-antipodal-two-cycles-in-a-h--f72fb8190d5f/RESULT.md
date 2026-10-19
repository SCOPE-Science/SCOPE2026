# A shape-driven saddle-center fold of antipodal two-cycles in a hyperbolic double-well map

## Finding

For the variable-barrier, fixed-minima hyperbolic double-well family described below, there is an exact deformation threshold
\[
\mu_* = \sqrt{3/2}.
\]
Below and at this threshold, its positive-radius, centrally symmetric primitive period-two orbit exists exactly above the origin's flip threshold and is unique. Above this threshold, a nondegenerate fold precedes the flip threshold and creates **two distinct antipodal primitive period-two orbits**, one hyperbolic saddle and the other linearly elliptic immediately after the fold. At the threshold the radius emerges by a **fourth-root law**, rather than the ordinary square-root law. The entire result concerns only antipodal cycles, not every two-cycle or all invariant sets of the map.

Precisely, for \(p=\mu^2>0\), put
\[
\beta=\operatorname{arsinh}(\sqrt p),\quad
A_c(p)=4(1+p),\quad
R_p(s)=\frac{\sinh s\cosh s}{s}
\left(1-\frac{\sinh^2s}{p}\right),
\qquad 0<s<\beta.
\]
Set \(R_p(0)=1\) by continuity. For \(p>3/2\) there is a unique \(s_*(p)\in(0,\beta)\) maximizing \(R_p\), and we define
\[
A_{\mathrm{sn}}(p)=\frac{A_c(p)}{R_p(s_*(p))}<A_c(p).
\]
The exact count \(N_{\mathrm{anti}}(p,t)\) of *distinct primitive antipodal period-two orbits* is:
\[
\begin{array}{c|c}
\text{parameter range}&N_{\mathrm{anti}}(p,t)\\ \hline
0<p\le3/2,\quad t\le A_c(p)&0\\
0<p\le3/2,\quad t>A_c(p)&1\\
p>3/2,\quad t<A_{\mathrm{sn}}(p)&0\\
p>3/2,\quad t=A_{\mathrm{sn}}(p)&1\\
p>3/2,\quad A_{\mathrm{sn}}(p)<t<A_c(p)&2\\
p>3/2,\quad t\ge A_c(p)&1
\end{array}
\]
where \(t=a/K>0\). In particular, the two-orbit interval is nonempty for every \(\mu>\sqrt{3/2}\). As \(p\downarrow3/2\) from above,
\[
A_c(p)-A_{\mathrm{sn}}(p)
=\frac{25}{27}(p-3/2)^2+O((p-3/2)^3).
\]
At \(p=3/2\), as \(t\downarrow10\) from above, the positive orbit coordinate obeys
\[
y=\frac1{\operatorname{arsinh}(\sqrt{3/2})}
\left(\frac{3(t-10)}{16}\right)^{1/4}(1+o(1)).
\]

## Assumptions and scope

Let \(a,K,\mu>0\). Define the smooth even potential
\[
V_{a,\mu}(u)=\frac{a\mu^2}{4(1+\mu^2)[\operatorname{arsinh}\mu]^2}
\left(\frac{\sinh^2((\operatorname{arsinh}\mu)u)}{\mu^2}-1\right)^2
\]
and the globally defined planar diffeomorphism
\[
F_{a,K,\mu}(u,v)=\left(2u-v+K^{-1}V_{a,\mu}'(u),\;u\right).
\]
Its Jacobian determinant is one everywhere. A *primitive antipodal two-cycle* means the two-point set
\(\{(y,-y),(-y,y)\}\) with \(y>0\); these are distinct nonfixed points. No assertion is made about other period-two orbits, periodic invariant curves, or chaotic trajectories. ``Linearly elliptic'' means the two multipliers of the two-step derivative lie on the unit circle away from real \(\pm1\), not nonlinear Lyapunov stability.

## Proof

**Reduction to one scalar equation.** Write \(p=\mu^2\), \(\beta=\operatorname{arsinh}\sqrt p\), \(t=a/K\), \(s=\beta y\). Direct differentiation gives
\[
K^{-1}V_{a,\mu}'(y)
=-\frac{t}{(1+p)\beta}\sinh s\cosh s
\left(1-\frac{\sinh^2s}{p}\right).
\]
Substitution of \((y,-y)\) into the stated map gives \(F(y,-y)=(-y,y)\) **if and only if** \(K^{-1}V'(y)=-4y\). For \(y>0\) this forces \(\sinh^2s<p\), hence \(0<s<\beta\). Dividing by \(y>0\) shows that the orbit condition is exactly
\[
\boxed{R_p(s)=A_c(p)/t.}
\]
The converse also holds by direct substitution, and different positive solutions \(s\) produce distinct two-cycles.

**A global unimodality lemma.** Set
\[
A(s)=\sinh s\cosh s,\qquad B(s)=A(s)\sinh^2s,
\]
\[
D(s)=sA'(s)-A(s),\qquad N(s)=sB'(s)-B(s).
\]
The hyperbolic identities \(A(s)=\sinh(2s)/2\), \(B(s)=\sinh(4s)/8-\sinh(2s)/4\) give the absolutely convergent expansions, for \(s>0\),
\[
D(s)=\sum_{n=1}^{\infty}d_ns^{2n+1},
\quad N(s)=\sum_{n=1}^{\infty}d_nr_ns^{2n+1},
\]
\[
d_n=\frac{2n\,2^{2n}}{(2n+1)!}>0,
\qquad r_n=\frac{4^n-1}{2}.
\]
Consequently the quotient \(p_c(s)=N(s)/D(s)\) is strictly increasing on \((0,\infty)\): when differentiated, every paired term indexed by \(m<n\) has the strictly positive factor \((n-m)(r_n-r_m)d_md_ns^{2m+2n+1}\). Moreover \(\lim_{s\downarrow0}p_c(s)=r_1=3/2\). Differentiating \(R_p=A/s-B/(ps)\) yields the exact factorization
\[
s^2R_p'(s)=D(s)\left(1-\frac{p_c(s)}p\right).
\]
Thus \(R_p\) is strictly decreasing for \(0<p\le3/2\). If \(p>3/2\), it first increases and can turn down at most once. It must turn down before \(s=\beta\), because \(R_p(\beta)=0\) and \(R_p'(\beta)<0\). Therefore a unique \(s_*\) exists, with \(R_p(s_*)>R_p(0)=1\); it is a strict nondegenerate maximum because \(p_c'(s_*)>0\) and \(D(s_*)>0\). Counting intersections of this graph with the horizontal line \(A_c/t>0\) proves all six cases of the table, including the equality boundaries. At \(t=A_c\) the zero-radius solution is excluded and the positive outer solution survives only when \(p>3/2\).

**Local orbit type at the fold.** Since the potential is even, the one-step derivative is identical at both points of any antipodal orbit. Differentiating the scalar orbit relation at a solution gives its Jacobian trace as
\[
\tau=2+K^{-1}V''(y)=-2-\frac{4sR_p'(s)}{R_p(s)};
\qquad
J=\begin{pmatrix}\tau&-1\\1&0\end{pmatrix}.
\]
On the increasing branch \(R_p'>0\), so \(\tau<-2\) and the corresponding two-cycle is hyperbolic saddle-type. At the nondegenerate fold, \(\tau=-2\), whence the two-step return derivative has a double unit multiplier. On the decreasing branch near the fold, \(-2<\tau<2\), hence this companion cycle is linearly elliptic. No conclusion about nonlinear elliptic stability is needed.

**Asymptotic degeneracy and fold width.** Taylor expansion at \(s=0\) gives, uniformly for \(p\) in compact positive intervals,
\[
R_p(s)=1+\left(\frac23-\frac1p\right)s^2+
\left(\frac2{15}-\frac1p\right)s^4+
\left(\frac4{315}-\frac2{5p}\right)s^6+O(s^8).
\]
At \(p=3/2\) the quadratic coefficient vanishes and the quartic coefficient is \(-8/15\). Inverting \(R_p(s)=10/t\) yields the stated fourth-root law. For comparison, away from the degeneracy the small-amplitude onset or disappearance is of square-root type, since the quadratic coefficient is nonzero. Let \(\delta=p-3/2\downarrow0\). The critical equation \(R_p'(s_*)=0\), strict uniqueness, and the Taylor expansion imply
\[
s_*^2=\frac5{12}\delta+O(\delta^2),
\qquad R_p(s_*)=1+\frac5{54}\delta^2+O(\delta^3).
\]
Substitution into \(A_{\mathrm{sn}}=4(1+p)/R_p(s_*)\) gives the claimed sharp fold-width coefficient \(25/27\). The implicit-function theorem at the nondegenerate maximum also gives the usual square-root separation of the two positive orbit radii above \(A_{\mathrm{sn}}\).

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic for the singular Taylor coefficients and deterministic numerical checks for the monotone critical ratio, original potential derivative, all count regimes, direct two-step map recurrence, and the near-degeneracy scaling. Run it using `python verify.py`. The script reports 687 passed assertions in the environment used to prepare this result. These are finite consistency tests; the preceding power-series positivity and scalar intersection arguments prove the stated all-parameter conclusions.

## Relationship to prior work

Dikandé's 2021 preprint and the full 2022 journal version introduce the relevant area-preserving map, determine the flip threshold \(t=4(1+\mu^2)\), and investigate period-two branches numerically. The present result concerns the global *number* of centrally symmetric period-two orbits across all \(\mu>0\), the exact shape threshold \(\mu^2=3/2\), the subcritical fold, and the fourth-root transition. Its scalar power-series monotonicity certificate supplies a completeness proof not obtained from numerical continuation. Dikandé's earlier 2000 lattice-map analysis examines a related hyperbolic potential and fixed-point bifurcations. The familiar polynomial Duffing-map two-cycle classifications concern a different function and do not imply this hyperbolic shape-dependent fold.

## Limitations

Only centrally symmetric primitive two-cycles are counted. The results do not rule out nonsymmetric primitive two-cycles or higher-period orbits. The linearly elliptic designation is not a proof of nonlinear stability, and the presence of a fold does not by itself prove chaos. The theorem treats strictly positive \(a,K,\mu\); its polynomial \(\mu\to0\) limit is not included in the count table. A completely exhaustive historical priority determination is not claimed.

## References

1. A. M. Dikandé, *Route to chaos in two-dimensional discrete parametric maps with bistable potentials*, arXiv:2103.07727v1 (first public version, 13 March 2021), https://arxiv.org/abs/2103.07727.
2. A. M. Dikandé, *Route to Chaos in Discrete Two-dimensional Maps with Hyperbolic Double-well Potentials*, Acta Physica Polonica B **53** (2022), 3-A1, https://doi.org/10.5506/APhysPolB.53.3-A1.
3. A. M. Dikandé, *Nonlinear coherent wavetrains and bifurcations in a class of deformable models for one-dimensional nonlinear discrete Klein-Gordon systems*, arXiv:nlin/0008011v1 (9 August 2000), https://arxiv.org/abs/nlin/0008011.
