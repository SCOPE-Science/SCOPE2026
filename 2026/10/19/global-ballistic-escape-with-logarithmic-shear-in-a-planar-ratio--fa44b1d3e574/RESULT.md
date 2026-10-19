# Global ballistic escape with logarithmic shear in a planar rational map

## Finding
For the two-dimensional rational map introduced by Zhang, Liu, Wei, Jiang and Bi [1], consider its fixed-line subfamily
\[
 F_{a,c}(x,y)=\left(x\left(1+\frac{a}{1+y^2}\right),\;y+cx\right),\qquad a>0,\quad c\in\mathbb R\setminus\{0\}.
\]
For every initial condition \((x_0,y_0)\in\mathbb R^2\), precisely one of the following holds:

1. If \(x_0=0\), the orbit is the constant fixed point \((0,y_0)\).
2. If \(x_0\ne0\), there is a finite, nonzero, initial-condition-dependent \(X\) with \(\operatorname{sgn}X=\operatorname{sgn}x_0\) and \(|X|>|x_0|\), and a finite real constant \(C\), such that as \(n\to\infty\),
\[
 x_n=X-\frac{a}{c^2X}\frac1n+O\!\left(\frac{\log n}{n^2}\right),\qquad
 y_n=cXn-\frac{a}{cX}\log n+C+O\!\left(\frac{\log n}{n}\right).
\]
All constants implicit in the asymptotic notation may depend on \(a,c,x_0,y_0\). In particular, every nonfixed orbit escapes in its second coordinate, despite its first coordinate converging to a finite limit. All bounded forward trajectories and all periodic trajectories are fixed points on the line \(x=0\).

A finite-difference consequence, requiring no knowledge of \(C\), is
\[
 \lim_{N\to\infty}\left(y_{4N}-3y_{2N}+2y_N\right)=\frac{a\log 2}{cX}.
\]
The logarithmic correction is nonzero for every \(a>0\) and \(x_0\ne0\).

## Assumptions and scope
The phase space is the full real plane; \(a>0\), \(c\ne0\) are arbitrary fixed real parameters and there is no restriction on \(y_0\), the sign of \(x_0\), or the size of the initial state. The coefficients corresponding to constant forcing in [1] are fixed to zero. The estimates concern forward discrete time \(n\in\mathbb N\); they make no claim about backward trajectories or other parameter regimes.

## Proof
**Step 1: Fixed and escaping alternatives.** If \(x_0=0\), both coordinates remain unchanged. Otherwise, the multiplier \(1+a/(1+y_n^2)\) is strictly greater than one. Therefore \(x_n\) retains its sign and \(|x_{n+1}|>|x_n|\ge |x_0|\) for all \(n\). The increment \(y_{n+1}-y_n=cx_n\) has a constant nonzero sign, with magnitude at least \(|cx_0|\). Consequently
\[
 |y_n|\ge |cx_0|n-|y_0|,
\]
so \(|y_n|\to\infty\), and for all sufficiently large \(n\) one has \(1+y_n^2\ge K n^2\) for some \(K>0\).

**Step 2: Existence of a finite transverse limit.** The exact product is
\[
 |x_n|=|x_0|\prod_{k=0}^{n-1}\left(1+\frac{a}{1+y_k^2}\right).
\]
The logarithm of this product is bounded above by \(a\sum_{k\ge0}(1+y_k^2)^{-1}<\infty\), because of the quadratic lower bound in Step 1. Its logarithm is also strictly positive. Hence \(x_n\to X\), with \(0<|x_0|<|X|<\infty\) and matching signs. By Cesàro averaging the identity \(y_n=y_0+c\sum_{k<n}x_k\),
\[
 \frac{y_n}{n}\longrightarrow cX\ne0.
\]

**Step 3: Leading transverse tail.** From the recurrence,
\[
 X-x_n=\sum_{k=n}^{\infty}\frac{a x_k}{1+y_k^2}.
\]
Since \(x_k\to X\) and \(y_k/k\to cX\), the summand is \(a/(c^2Xk^2)+o(k^{-2})\). The comparison \(\sum_{k\ge n}k^{-2}=n^{-1}+O(n^{-2})\) gives
\[
 X-x_n=\frac{a}{c^2Xn}+o(n^{-1}).
\]
In particular, \(x_n=X+O(n^{-1})\), and summing the second coordinate recurrence again shows
\[
 y_n=cXn+O(\log n).
\]

**Step 4: Quantitative bootstrap.** For large positive integers \(k\), the bounds just proved give
\[
 x_k=X+O(k^{-1}),\quad y_k=cXk+O(\log k),
\]
so direct expansion of the exact rational summand gives
\[
 \frac{a x_k}{1+y_k^2}=\frac{a}{c^2Xk^2}+O\!\left(\frac{\log k}{k^3}\right).
\]
Since \(\sum_{k\ge n}\log k/k^3=O(\log n/n^2)\), inserting the latter into the exact tail yields
\[
 X-x_n=\frac{a}{c^2Xn}+O\!\left(\frac{\log n}{n^2}\right).
\]

**Step 5: Existence of the phase constant and sharp logarithmic term.** For \(n\ge1\) set
\[
 z_n=y_n-cXn+\frac{a}{cX}\log n.
\]
Then
\[
 z_{n+1}-z_n=c(x_n-X)+\frac{a}{cX}\log\left(1+\frac1n\right)
 =O\!\left(\frac{\log n}{n^2}\right),
\]
because the order-\(n^{-1}\) terms cancel exactly. This absolutely summable difference proves that \(z_n\to C\in\mathbb R\), with remainder \(z_n-C=O(\log n/n)\). The asserted expansion for \(y_n\) follows, valid for both signs of \(cX\).

**Step 6: Consequences.** Since \(|y_n|\to\infty\) whenever \(x_0\ne0\), no such orbit is bounded or periodic. The fixed line is therefore the entire periodic set, and the global bounded-forward-orbit set. Substitution of the asymptotic formula for \(y_n\) at \(N,2N,4N\) cancels its linear and constant terms; the logarithm contributes \(a\log2/(cX)\), while all remainders tend to zero. This proves the finite-difference assertion.

## Verification
The standalone standard-library program `verify.py` checks the recurrence exactly for several rational initial steps, verifies sign monotonicity on four distinct parameter cases (including both signs of \(x_0\) and \(c\)), and compares finite differences to the analytical tail and logarithmic coefficients. All **384,018** finite consistency assertions pass in the packaged program. These checks are not an exhaustive search of initial conditions and are not substitutes for the proof of the universal or asymptotic assertions.

## Relationship to prior work
Zhang et al. [1] introduce the full rational map, enumerate the fixed-line case and compute its local eigenvalues. Their reported examples of complex or bounded dynamics in that case use negative rational coefficients, whereas the entire positive-coefficient half-space here has escape from every point outside the fixed line. Their published analysis does not give the present global positive-coefficient orbit classification, finite limiting first coordinate, logarithmic correction, or dyadic finite-difference law. A known restricted negative-coefficient escape calculation has an analogous logarithmic structure but does not imply the globally escaping positive-coefficient result: its parameter sign is opposite and its escaping points form only part of its phase space. The shared algebraic mechanism is acknowledged rather than claimed anew.

## Limitations
The exact finite limit \(X\) and phase constant \(C\) are determined by each orbit, not represented here by closed elementary expressions in initial data. No claim concerns the forced subfamilies, negative rational coefficients, all backward orbits, convergence uniform over the entire initial-condition plane, or any global compact attractor outside the fixed line. The prior-work comparison cannot eliminate every possible equivalent formulation in unindexed literature; independent examination is warranted before a priority claim.

## References
[1] Li-Ping Zhang, Yang Liu, Zhou-Chao Wei, Hai-Bo Jiang and Qin-Sheng Bi, “A class of two-dimensional rational maps with self-excited and hidden attractors,” *Chinese Physics B* **31** (2022), article 030503, DOI: 10.1088/1674-1056/ac4025. Full original paper: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_3_030503.shtml .
