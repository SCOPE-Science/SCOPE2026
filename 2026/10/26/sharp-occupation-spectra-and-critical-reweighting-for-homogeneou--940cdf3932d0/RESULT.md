# Sharp occupation spectra and critical reweighting for homogeneous pantograph dynamics

## Finding

This result determines all weak-star subsequential limits of physical-time empirical measures for two natural homogeneous discrete pantograph clocks whenever their underlying continuous dynamical map has an asymptotically periodic orbit. It also identifies sampling weights that restore the ordinary Birkhoff statistics **for arbitrary underlying orbits**, with a quantitative total-variation comparison.

For a compact metric space \(X\), a continuous map \(f:X\to X\), and \(x_0\in X\), put \(y_m=f^m(x_0)\). Suppose first that there is a cycle of **least period** \(p\ge1\), consisting of distinct points \(z_0,\ldots,z_{p-1}\), with \(f(z_i)=z_{i+1\bmod p}\) and \(d(y_m,z_{m\bmod p})\to0\). Define
\[
\mu_*=\frac1p\sum_{i=0}^{p-1}\delta_{z_i},\qquad
v_r^{(q)}=\frac{q-1}{q^p-1}\sum_{j=0}^{p-1}q^{p-1-j}\delta_{z_{r-j\bmod p}},\quad q>1,
\]
\[
\mathcal P_q=\bigcup_{r=0}^{p-1}[v_r^{(q)},v_{r+1\bmod p}^{(q)}],\qquad
\mathcal P_\infty=\bigcup_{r=0}^{p-1}[\delta_{z_r},\delta_{z_{r+1\bmod p}}].
\]
Segments are entire affine convex segments of probability measures. A limit set below means the set of weak-star limits of subsequences as the physical time horizon tends to infinity.

**Proportional delay.** For each integer \(b\ge2\), the recursion \(x_{n+1}=f(x_{\lfloor n/b\rfloor})\) satisfies: for every \(0\le\gamma<1\), the weighted occupation measures
\[
\frac{\sum_{n=1}^{N}n^{-\gamma}\delta_{x_n}}{\sum_{n=1}^{N}n^{-\gamma}}
\]
have limit set **exactly** \(\mathcal P_{b^{1-\gamma}}\). At \(\gamma=1\), they converge to \(\mu_*\).

**Square-root delay.** For \(x_{n+1}=f(x_{\lfloor\sqrt n/2\rfloor})\), unweighted occupations \(N^{-1}\sum_{n=1}^N\delta_{x_n}\) have limit set **exactly** \(\mathcal P_\infty\). For every \(0\le\gamma<1\), occupations weighted from \(n=3\) by \(1/[n(\log n)^\gamma]\) have limit set **exactly** \(\mathcal P_{2^{1-\gamma}}\); at \(\gamma=1\), they converge to \(\mu_*\).

**Universal critical-weight restoration.** Drop the asymptotic-periodic-orbit hypothesis. For either clock, let \(k(N)\) be the index of the stage containing physical time \(N\). Under the respective critical weights \(1/n\) and \(1/[n\log n]\), there is a finite clock-dependent constant \(C\) such that
\[
\left\|\frac{\sum_{n=n_0}^N w_n\delta_{x_n}}{\sum_{n=n_0}^Nw_n}
-\frac1{k(N)}\sum_{m=0}^{k(N)-1}\delta_{y_m}\right\|_{\rm TV}\le\frac{C}{k(N)},
\]
for every sufficiently large \(N\), where \(n_0=1\) for proportional delay and \(n_0=3\) for square-root delay; total-variation norm is the supremum over Borel sets (an alternative convention introduces a factor two). Thus critically weighted delayed occupations and ordinary undelayed Birkhoff occupations have **identical weak-star limit sets**, without assumptions of periodicity or ergodicity. In particular, they converge if and only if the underlying ordinary occupations converge.

When \(p\ge2\), every subcritical limit polygon has more than one point, so the subcritical occupations do not converge. When \(p\ge3\), \(\mu_*\) lies outside the subcritical limit polygon; for \(p=2\) it lies on the segment. For \(p=1\), all these sets reduce to the unique fixed-point mass.

## Assumptions and scope

The clock is deterministic, the recursion starts at \(x_0\), and \(x_n\) is defined for all integers \(n\ge0\). The weights are positive and use the usual real logarithm. The topology on probability measures is weak-star, i.e. convergence against all continuous real observables. The critical total-variation comparison does not use continuity or compactness except to state its weak-star consequence: it is an identity-based estimate for the measures supported on the orbit. The two delay formulas are treated separately; no claim is made for arbitrary delay functions or inhomogeneous mixing with \(x_n\).

## Proof

**1. Plateau identities.** For proportional delay, put \(T_m=(b^m-1)/(b-1)\), \(m\ge0\); then \(T_{m+1}=bT_m+1\) and \(x_n=y_m\) for \(T_m\le n<T_{m+1}\). To see the induction, if \(T_m\le n+1<T_{m+1}\), then \(bT_{m-1}\le n<bT_m\), so \(\lfloor n/b\rfloor\) belongs to the preceding stage; the exceptional initial index is handled directly. The \(m\)-th stage has length \(b^m\). For square-root delay take \(T_0=0,T_1=1,T_{m+1}=4T_m^2+1\), \(m\ge1\). If \(T_m\le n+1<T_{m+1}\), then \(4T_{m-1}^2\le n<4T_m^2\), and \(\lfloor\sqrt n/2\rfloor\) lies in the preceding stage. Hence again \(x_n=y_m\) for \(T_m\le n<T_{m+1}\), beginning with \(T_2=5,T_3=101,T_4=40805\). These stage formulas are already established in Gade and Bhalekar (2026), Section 3; they are premises rather than a novelty claim.

**2. Exact geometric-block limit lemma.** Let \(W_m\) denote the total nonnegative observation weight in the \(m\)-th *complete* stage. Suppose \(W_m=Cq^m(1+o(1))\) for some \(C>0,q>1\), while the maximum weight of a single observation divided by the total accumulated weight tends to zero. As \(m\to\infty\) through \(m\equiv r\pmod p\), the empirical measure at the end of stage \(m\) converges weak-star to
\[
(q-1)\sum_{j=0}^{\infty}q^{-j-1}\delta_{z_{r-j\bmod p}}=v_r^{(q)}.
\]
Indeed, normalize the complete-stage sum by \(\sum_{i\le m}W_i\sim Cq^{m+1}/(q-1)\), cut the geometric tail after \(L\) stages, use \(y_i\to z_{i\bmod p}\) on finitely many last stages, and let \(L\to\infty\). During stage \(m+1\) every partial horizon has measure an affine combination of the already accumulated measure and \(\delta_{y_{m+1}}\). The share of its cumulative partial weight varies monotonically from zero to its full-stage value, with asymptotically vanishing individual jumps; hence its limit points fill the entire segment \([v_m^{(q)},v_{m+1}^{(q)}]\). Conversely, every horizon lies in one of these stage intervals, and compactness of the finite-dimensional simplex of coefficients forces a subsequential phase and fraction, so no other limit is possible.

If \(W_m/\sum_{j<m}W_j\to\infty\) instead, then stage-end measures converge to the corresponding \(\delta_{z_r}\), and the same continuous-fraction argument gives precisely \(\mathcal P_\infty\).

**3. Proportional clock weights.** For \(0\le\gamma<1\), comparison of \(\sum_{T_m\le n<T_{m+1}}n^{-\gamma}\) with its integral, using \(T_m\sim b^m/(b-1)\), gives
\[
W_m\sim \frac{(b/(b-1))^{1-\gamma}-(1/(b-1))^{1-\gamma}}{1-\gamma}\,b^{(1-\gamma)m}.
\]
For \(\gamma=0\) this is the exact stage size. The geometric-block lemma with \(q=b^{1-\gamma}\) proves the entire subcritical claim. At \(\gamma=1\), the integral comparison yields \(W_m=\log b+O(b^{-m})\); the error series is absolutely summable.

**4. Square-root clock weights.** Write \(u_m=\log T_m\), \(m\ge2\). The endpoint recursion gives
\[
u_{m+1}=2u_m+\log4+O(T_m^{-2}),\qquad u_m=c\,2^m+O(1)
\]
with some \(c>0\), since the summable perturbations in the geometric recurrence have a convergent coefficient series. For \(0\le\gamma<1\), comparison with the integral of \(1/[t(\log t)^\gamma]\) gives
\[
W_m\sim\frac{(2^{1-\gamma}-1)c^{1-\gamma}}{1-\gamma}\,2^{(1-\gamma)m}.
\]
The geometric-block lemma therefore yields \(\mathcal P_{2^{1-\gamma}}\). For \(\gamma=1\), the integral over a stage is \(\log(u_{m+1}/u_m)=\log2+O(2^{-m})\), and the discrete sum differs by at most the first summand of the stage, which is summable in \(m\). The raw stage lengths \(T_{m+1}-T_m\) grow so quickly that each is asymptotically much larger than the sum of all preceding stage lengths; the supergeometric-block lemma gives \(\mathcal P_\infty\).

**5. Critical comparison in total variation.** In each critical case the sum of stage weights has the form \(W_m=c_0+e_m\), \(c_0>0\), with \(\sum_m|e_m|<\infty\) (and any finitely many initial exceptional stages absorbed into this finite sum). At horizon \(N\) in stage \(k=k(N)\), the weighted measure equals the normalized sum of the weights of stages below \(k\), plus at most one partially observed stage whose total weight is bounded uniformly in \(k\). The total unnormalized variation distance from \(c_0\sum_{m<k}\delta_{y_m}\) is at most \(\sum_m|e_m|+O(1)\), while its mass is \(c_0k+O(1)\). Normalization changes variation by another \(O(1/k)\), uniformly in the unknown orbit \(y_m\). This proves the stated bound, hence equality of weak-star accumulation sets. The same inequality holds in the opposite direction with the same pair of empirical measures; no measure invariantness assumption is required.

**6. Sharp geometry.** The vectors \(v_r^{(q)}\) obey \(v_r^{(q)}=q^{-1}v_{r-1}^{(q)}+(1-q^{-1})\delta_{z_r}\), so the circulant linear operator that sends the point masses to the vertices has inverse proportional to \(I-q^{-1}P\), with \(P\) a cyclic permutation. It is invertible for \(q>1\); thus the \(p\) vertices are affinely independent. Their barycenter is \(\mu_*\). For \(p\ge3\) this barycenter is in the relative interior of their simplex, disjoint from its one-dimensional edge union. For \(p=2\), the segment contains the barycenter. Distinct vertices also prove nonconvergence for all \(p\ge2\).

## Verification

The embedded `verify.py` is a dependency-free Python 3 checker; run `python3 verify.py`. It checks the exact plateau identity by direct iteration for four integer proportional bases and the square-root clock; finite-horizon concentration at the stated vertices; the discounted-vector identity and exact rational values for a tent-map three-cycle; and antiderivative-based numerical checks for harmonic, double-logarithmic, and fractional sampling exponents. Successful output begins with `VERIFY_OK`. The proof above, not finite trials, establishes the universal infinite-time claims.

For the tent map \(f(t)=2\min\{t,1-t\}\) on \([0,1]\), the least period-three orbit \((2/9,4/9,8/9)\) gives, for proportional base \(b=4\), the vertex
\[
v_0^{(4)}=\frac{16}{21}\delta_{2/9}+\frac{1}{21}\delta_{4/9}+\frac4{21}\delta_{8/9};
\]
for square-root clock with harmonic weight, it gives
\[
v_0^{(2)}=\frac47\delta_{2/9}+\frac17\delta_{4/9}+\frac27\delta_{8/9}.
\]
The unweighted square-root polygon is the boundary of the triangle with these three point masses as vertices. Critical double-logarithmic weighting collapses that nonconvergence into the uniform orbit measure.

## Relationship to prior work

Gade and Bhalekar, *Pantograph Difference Equations: Stability, Multistability, and Chaos* (arXiv:2610.21635v1, October 15, 2026), Section 3, derive both plateau endpoint recursions and explicitly note that the delayed and undelayed time averages need not agree. Those plateau identities and that qualitative observation are credited, not new. The present result computes **all** occupation-measure limits at every subcritical power, gives a sharp phase transition in two clocks, and proves critical total-variation restoration for every base orbit.

Tong, *Exponential convergence can happen in weighted Birkhoff averages via quasi-periodicity with arbitrary nonresonance and low regularity* (arXiv:2607.21950v1, July 24, 2026), Theorem 1.1 and Sections 2.1–2.3, treats specially designed smooth weights applied directly to quasiperiodic torus orbits. It neither studies these growing stasis clocks nor gives the explicit delayed occupation polygons or universal harmonic reweighting; it supplies the complementary recent dynamical-sampling context.

Standard regular-summation arguments explain the qualitative critical-weight phenomenon once constant asymptotic stage weights are established, but not the complete subcritical polygon spectra and their interior-versus-boundary geometry. Historical priority under other time-change/weighted-empirical-measure terminology is a residual bibliographic risk.

## Limitations

This is a theorem about the fully homogeneous coupling, not mixed instantaneous/delayed recursions. The complete polygon classifications assume convergence to a phase-aligned finite periodic orbit; they do not assert such convergence for arbitrary maps or initial points. The universal critical comparison has no periodicity assumption but asserts identity of weak-star limit sets, not existence of a limit. There is no extrapolation to noninteger proportional bases, general nonlinear delay exponents, stochastic sampling, or every possible weight. Numerical tests are finite checks only. No independent audit has been performed.

## References

1. Prashant M. Gade and Sachin Bhalekar, *Pantograph Difference Equations: Stability, Multistability, and Chaos*, arXiv:2610.21635v1 (first public version October 15, 2026), Section 3. https://arxiv.org/html/2610.21635v1
2. Zhicheng Tong, *Exponential convergence can happen in weighted Birkhoff averages via quasi-periodicity with arbitrary nonresonance and low regularity*, arXiv:2607.21950v1 (first public version July 24, 2026), Theorem 1.1 and Section 2. https://arxiv.org/abs/2607.21950
