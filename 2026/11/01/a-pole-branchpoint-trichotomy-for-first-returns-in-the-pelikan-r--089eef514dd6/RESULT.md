# A pole–branchpoint trichotomy for first returns in the Pelikan random map

## Finding

Independently at every integer time, apply the doubling map \(x\mapsto2x\pmod 1\) with probability \(p\), or the halving map \(x\mapsto x/2\) with probability \(q=1-p\). Start from Lebesgue measure conditioned to \(A=[1/2,1)\) and let \(\tau=\inf\{n\geq1:X_n\in A\}\), with \(\tau=\infty\) if no return occurs. For \(0<p<1\), put
\[
 r_p(z)=\frac{1-\sqrt{1-4pqz^2}}{2qz},\qquad
 R_p(z)=z\left(qr_p(z)+\frac{p}{2-r_p(z)}\right).
\]
The square-root branch has value \(1\) at \(z=0\), and removable values are taken by continuity. For \(|z|<1\),
\[
 R_p(z)=\sum_{n\geq1}\mathbb P(\tau=n)z^n.
\]
The following precise coefficient asymptotics show a **three-regime sharp threshold at \(p=4/5\)**, distinct from the classical recurrence threshold at \(p=1/2\).

For \(0<p<4/5\), define \(\rho=(2\sqrt{pq})^{-1}\), \(a=\sqrt{p/q}\), and
\[
 c_\pm=\frac{\rho a}{\sqrt{2\pi}}\left(q+\frac{p}{(2\mp a)^2}\right).
\]
Then, as \(n\to\infty\) through arbitrary integers,
\[
 \boxed{\mathbb P(\tau=n)=\rho^{-n}n^{-3/2}\left[c_++(-1)^nc_-+o(1)\right].}
\]
The two constants are strictly positive. The alternating term is essential: the two parity subsequences have different leading coefficients.

At \(p=4/5\), a pole meets the positive square-root branchpoint; the return law instead obeys
\[
 \boxed{\mathbb P(\tau=n)\sim\frac{(4/5)^n}{2\sqrt{2\pi n}}.}
\]
For \(4/5<p<1\), the pole lies strictly inside the two branchpoints, and
\[
 \boxed{\mathbb P(\tau=n)\sim
 \frac{p(p-4q)}{(p+4q)^2}\left(\frac{p+4q}{2}\right)^n.}
\]
At \(p=1\), the law is exactly \(\mathbb P(\tau=n)=2^{-n}\), so the last formula remains valid at that endpoint.

For \(p>1/2\), the return is almost surely finite and \(\mathbb E\tau=2p/(2p-1)\); starting uniformly from \(A\) is then also the conditional stationary initialization. At \(p=1/2\), the return is almost surely finite with infinite mean; the tail satisfies \(\mathbb P(\tau>n)\sim\sqrt{2/(\pi n)}\). For \(0<p<1/2\), the return probability equals \(p(3-4p)/(2-3p)<1\). These recurrence facts are contextual, not the novelty claim.

## Assumptions and scope

All random map choices are mutually independent and independent of the uniform initial point. The interval uses its half-open convention; dyadic ambiguities form a null set. Return probabilities average both the initial point and the map choices. The three tail regimes are for each **fixed** \(p\) in the stated open interval; the formulas are not uniform as \(p\to4/5\). No claim is made about arbitrary nonuniform initial densities, quenched return laws, or higher-dimensional random maps.

## Proof

**1. Exact reduction.** Let \(L(x)\) count the initial binary zeros of \(x\), so \(L(x)=j\) for \(x\in[2^{-j-1},2^{-j})\). Thus \(A=\{L=0\}\). Until the first return, halving increments \(L\) and doubling decrements it. At the first step from a uniform point of \(A\), halving puts \(L\) at \(1\), while doubling makes the point uniform on \([0,1)\). In the latter case its new \(L\) has the geometric law \(\mathbb P(L=j)=2^{-j-1}\) for \(j\geq0\).

Let \(h_j(z)\) be the defective generating function of the hitting time of \(0\) for the walk started at \(j\geq0\). For \(0<|z|<1\) it solves \(h_0=1\) and \(h_j=z(ph_{j-1}+qh_{j+1})\) for \(j\geq1\). Boundedness at infinity and the condition \(h_j(0)=0\) for \(j\geq1\) select the smaller characteristic root \(r_p(z)\) with \(r_p=z(p+qr_p^2)\), hence \(h_j(z)=r_p(z)^j\). The geometric sum is \(\sum_{j\geq0}2^{-j-1}r_p(z)^j=1/(2-r_p(z))\). Conditioning on the first random choice yields exactly \(R_p(z)\).

**2. Below the tail threshold.** For \(0<p<4/5\) the positive and negative branchpoints \(z=\pm\rho\) are the only singularities of minimum modulus on the principal algebraic sheet. At \(z=\rho\), the root tends to \(a<2\) and has the local expansion \(r_p(z)=a-a\sqrt{2(1-z/\rho)}+O(1-z/\rho)\). The singular coefficient of \(R_p\) is therefore \(-\rho a\sqrt2\,(q+p/(2-a)^2)\). At \(z=-\rho\), the corresponding square-root coefficient is \(-\rho a\sqrt2\,(q+p/(2+a)^2)\). The transfer rule \([z^n](1-z/\rho)^{1/2}\sim-\rho^{-n}/(2\sqrt\pi n^{3/2})\), together with the factor \((-1)^n\) from the negative singularity, gives the stated two-parity law.

**3. Collision and pole.** At \(p=4/5\), \(\rho=5/4\) and \(a=2\). Consequently \(2-r_p(z)=2\sqrt{2(1-z/\rho)}+O(1-z/\rho)\), which makes \(R_p(z)\sim(2\sqrt2)^{-1}(1-z/\rho)^{-1/2}\). The positive inverse-square-root singularity dominates the negative square-root singularity, proving the critical \(n^{-1/2}\) law.

For \(p>4/5\), the equation \(r_p(z)=2\) has the positive principal-sheet solution \(z_0=2/(p+4q)<\rho\). Implicit differentiation of \(r_p=z(p+qr_p^2)\) gives \(r_p'(z_0)=(p+4q)^2/(p-4q)\). Thus
\[
 R_p(z)=\frac{p(p-4q)}{(p+4q)^2}\frac1{1-z/z_0}+O(1)
\]
near the simple pole. The branchpoints are farther from the origin; the residue gives the geometric law. At \(p=1\), the direct formula is \(R_1(z)=z/(2-z)\).

**4. Recurrence and moments.** The root at \(z=1\) is \(r_p(1)=1\) when \(p\geq1/2\) and \(r_p(1)=p/q\) otherwise; substituting gives the return probabilities. For \(p>1/2\), differentiation at \(z=1\) gives \(r_p'(1)=1/(2p-1)\) and \(R_p'(1)=1+1/(2p-1)=2p/(2p-1)\). At \(p=1/2\), the positive square-root expansion yields \(1-R_{1/2}(z)\sim\sqrt{2(1-z)}\), and the standard nonnegative-coefficient Tauberian transfer gives \(\mathbb P(\tau>n)\sim\sqrt{2/(\pi n)}\).

## Verification

The included standalone program `verify.py` checks the generating-function coefficients against an entirely separate finite-state walk evolution, using exact fractions. For five choices of \(p\), all 26 coefficients match; it also tests the deterministic doubling endpoint, checks the rational pole residue at \(p=9/10\), and performs illustrative large-time coefficient comparisons in the three regimes. These finite computations do not prove the asymptotics: the preceding analytic singularity argument does.

## Relationship to prior work

Yan et al. (2023) analyze invariant densities and temporal correlations for this switching map. Monthus (2024) establishes the binary-cell walk with geometric resetting and gives explicit transforms for first-passage and geometrically mixed absorbing excursions (especially her equations (71), (292) and Appendix B.3). **The existence of a geometric reset and the transform themselves are prior results**. Monthus also identifies \(p=4/5\) as a spectral crossover for a *different observable*, the position correlation (equations (203), (210)–(211)); the crossover parameter is therefore not claimed new in general.

The present distinct result is the **full first-return coefficient asymptotic, including parity and the inverse-square-root pole collision**. Monthus's Appendix B.3 asymptotic formula (296), stated for \(1/2<p\leq1\), asserts an \(n^{-3/2}\) factor and the branchpoint exponential rate throughout. Its displayed geometric-weight sum (291) converges only for \(p<4/5\); the first-return calculation makes the corresponding exceptional regime explicit and shows why the fixed-parameter asymptotic changes. This comparison does not invalidate her exact first-passage transform or the independently derived position-correlation crossover.

Brevitt and Klages (2026) study quasi-stationary distributions under an additional hole; the accessible relevant material does not provide the closed-map first-return coefficient trichotomy here. A theorem already explicitly giving these same asymptotics, if found, would supersede the novelty claim.

## Limitations

The pointwise formulas are not a uniform crossover theorem in a window where \(p-4/5\) depends on \(n\). They do not settle quenched return-time fluctuations or nonuniform starting laws. The earlier geometrically mixed absorption transform makes the new coefficient asymptotics accessible by singularity analysis, so priority depends on whether the three-regime return-law statement has appeared elsewhere. All literature comparisons are best-knowledge, not an independent publication-priority certification.

## References

1. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269, first public 2023-08-18. https://arxiv.org/abs/2308.09269
2. C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, arXiv:2409.19999, first public 2024-09-30, particularly Sections III–IV, VI.5, Appendix B.3. https://arxiv.org/abs/2409.19999
3. S. Brevitt and R. Klages, *Quasi-stationary and quasi-ergodic distributions in the Pelikan random map*, arXiv:2607.19084, 2026. https://arxiv.org/abs/2607.19084
4. S. Pelikan, original random-map construction, *Transactions of the American Mathematical Society* 281 (1984), 813–825, DOI: 10.1090/S0002-9947-1984-0722776-1. This historical original was not inspected in full.
