# Folding a Skellam law: protected log-concavity and arbitrarily long curvature reversals

## Finding

Let \(X\sim\operatorname{Pois}(a)\) and \(Y\sim\operatorname{Pois}(b)\) be independent, with \(a,b>0\). Put \(D=|X-Y|\) and \(p_k=\Pr(D=k)\), \(k\ge0\). Then:

1. **Protected regime.** The strict inequality \(p_1^2>p_0p_2\) always holds. Moreover, if \(a=b\) **or** \(ab\le1\), then \(p_k^2>p_{k-1}p_{k+1}\) for every integer \(k\ge1\).
2. **Unbounded reversals.** Fix any real \(\theta\ne0\) and any integer \(K\ge2\). For some \(s_0>0\), every \(s\ge s_0\) and rates \(a=s e^{\theta}\), \(b=s e^{-\theta}\) give \(p_k^2<p_{k-1}p_{k+1}\) simultaneously for every \(k=2,\ldots,K\). Nevertheless, for each fixed positive pair \((a,b)\), all sufficiently large indices satisfy the strict log-concavity inequality.

Thus the absolute difference of two independent Poisson counts can have **arbitrarily many consecutive internal log-convex indices** although its first curvature is positive and its far-tail curvature eventually returns to positive. A concrete exact example is \((a,b)=(3,12)\), which fails strict log-concavity at index \(k=2\).

## Assumptions and scope

The Poisson counts are independent, their intensities are positive and finite, and log-concavity means \(p_k^2\ge p_{k-1}p_{k+1}\) for all integers \(k\ge1\). Define \(z=2\sqrt{ab}>0\), \(t=ab=z^2/4\), and \(\theta=\frac12\log(a/b)\). For each integer \(k\ge0\), define the modified Bessel function by its absolutely convergent series
\[
I_k(z)=\sum_{j=0}^{\infty}\frac{(z/2)^{2j+k}}{j!(j+k)!}.
\]
The Skellam formula gives
\[
p_0=e^{-(a+b)}I_0(z),\qquad
p_k=2e^{-(a+b)}\cosh(k\theta)I_k(z)\quad(k\ge1).
\]
The folded distribution is not an order statistic of identically distributed nonnegative counts; it is a different transformation of a signed count difference.

## Proof

**1. Exact curvature comparison.** For every integer \(k\ge2\), positivity of all terms reduces the inequality \(p_k^2\ge p_{k-1}p_{k+1}\) to \(R_k(z)\ge Q_k(\theta)\), where
\[
R_k(z)=\frac{I_k(z)^2}{I_{k-1}(z)I_{k+1}(z)},\qquad
Q_k(\theta)=\frac{\cosh((k-1)\theta)\cosh((k+1)\theta)}{\cosh^2(k\theta)}
=1+\frac{\sinh^2\theta}{\cosh^2(k\theta)}.
\]
For \(k=1\), the exceptional folding factor at zero gives
\[
\frac{p_1^2}{p_0p_2}=\frac{2\cosh^2\theta}{\cosh(2\theta)}R_1(z)>1.
\]
Indeed the classical strict modified-Bessel Turán inequality \(I_k(z)^2>I_{k-1}(z)I_{k+1}(z)\) holds for every \(k\ge1,z>0\). One direct justification is Neumann's product identity, yielding
\[
I_k(z)^2-I_{k-1}(z)I_{k+1}(z)
=\frac4\pi\int_0^{\pi/2} I_{2k}(2z\cos u)\sin^2 u\,du>0.
\]
The displayed integral identity follows from the standard Neumann product formula (or by expanding its two sides into positive, absolutely convergent Bessel series); its integrand is positive for \(0<u<\pi/2\). The other factor exceeds one since \(2\cosh^2\theta=\cosh(2\theta)+1\). When \(\theta=0\), \(Q_k(0)=1<R_k(z)\), proving the entire equal-rate case.

**2. Uniform small-product bound.** Put
\[
A_k(t)=\sum_{j=0}^{\infty}\frac{t^j}{j!(k+1)_j},\qquad
(k+1)_j=(k+1)(k+2)\cdots(k+j),\quad (k+1)_0=1.
\]
Then \(I_k(z)=(z/2)^kA_k(t)/k!\), and \(0<A_{k+1}(t)\le A_k(t)\). With the probability weights proportional to the positive summands defining \(A_k\), let \(J\) be the summation index. Termwise algebra gives
\[
\frac{A_{k-1}}{A_k}=1+\frac{\mathbb EJ}{k},\qquad
\mathbb EJ=\frac{t A_{k+1}}{(k+1)A_k}\le\frac{t}{k+1}.
\]
Consequently, for all integers \(k\ge1\),
\[
R_k(z)=\frac{k+1}{k}\frac{A_k^2}{A_{k-1}A_{k+1}}
\ge\frac{(k+1)^2}{k(k+1)+t}.
\]
For any nonzero real \(\theta\) and integer \(k\ge2\), convexity of hyperbolic sine gives \(\sinh(k|\theta|)\ge k\sinh|\theta|\), and \(\cosh(k|\theta|)>\sinh(k|\theta|)\). Therefore
\[
0<Q_k(\theta)-1<\frac1{k^2}.
\]
If \(t=ab\le1\), the lower bound above yields
\[
R_k(z)-1\ge\frac{k}{k(k+1)+1}>\frac1{k^2},\qquad k\ge2,
\]
since \(k^3>k^2+k+1\) for every integer \(k\ge2\) (true at two, and the difference increases strictly thereafter). Thus every internal curvature is strictly log-concave, as claimed.

**3. Arbitrarily long violation intervals at fixed imbalance.** For fixed nonnegative integer \(j\), the integral representation
\[
I_j(z)=\frac1\pi\int_0^\pi e^{z\cos u}\cos(ju)\,du
\]
shows \(I_j(z)/I_0(z)\to1\) as \(z\to\infty\): the normalized positive weight \(e^{z\cos u}\) concentrates at \(u=0\), where \(\cos(ju)=1\). Thus for each fixed \(k\), \(R_k(z)\to1\). If \(\theta\ne0\), then \(Q_k(\theta)>1\) for every fixed integer \(k\ge2\). For any given finite \(K\), all inequalities \(R_k(z)<Q_k(\theta)\), \(2\le k\le K\), therefore hold simultaneously once \(z\) is sufficiently large. Taking \(a=s e^{\theta}\), \(b=s e^{-\theta}\) makes \(z=2s\), proving the asserted high-intensity conclusion.

**4. Eventual recovery of log-concavity.** Fix \(t>0\) and \(\theta\ne0\). For sufficiently large \(k\), in particular \(k\ge\max(3,2t+2)\), the same elementary bound implies
\[
R_k(z)-1\ge\frac{k+1-t}{k(k+1)+t}\ge\frac1{2(k+2)}.
\]
But \(\cosh(k|\theta|)\ge\tfrac12e^{k|\theta|}\), so
\[
Q_k(\theta)-1\le4\sinh^2\theta\,e^{-2k|\theta|}=o(1/k).
\]
Thus \(R_k(z)>Q_k(\theta)\) eventually. The case \(\theta=0\) was proved globally in Step 1. This completes every infinite-domain assertion.

**5. An exact finite counterexample.** For \((a,b)=(3,12)\), \(z=12\) and \(|\theta|=\log2\); the threshold at \(k=2\) is
\[
Q_2=1+\frac{36}{289}=\frac{325}{289}.
\]
Put \(B_n=\sum_{j\ge0}36^j/[j!(j+n)!]\); then \(I_n(12)=6^nB_n\). The exact-arithmetic certificate described below bounds the three series by rational intervals \([L_n,U_n]\) and verifies
\[
289U_2^2<325L_1L_3.
\]
Hence \(R_2(12)<325/289=Q_2\), proving \(p_2^2<p_1p_3\) without floating-point assumptions.

## Verification

The included standard-library script `verify.py` checks the explicit example with rational interval arithmetic. For each \(n=1,2,3\), it sums terms \(j=0,\ldots,19\) of \(B_n\) exactly; from the next term onward the successive ratio is bounded by \(36/[(21)(21+n)]<1\), giving a rigorously valid geometric tail bound. It then checks the displayed rational strict inequality. Additional exact-integer and exact-rational checks exercise the elementary curvature comparisons at finite indices. Run `python verify.py` with Python 3; no third-party package is needed. The infinite conclusions are proved in Steps 1–4, not inferred from finite code checks.

## Relationship to prior work

Badiella, del Castillo and Puig (first available online 26 June 2023) establish log-concavity preservation for discrete *order statistics*. That operation differs from absolute-value folding of a signed difference, and their proof gives no uniform product regime or unbounded violation window for folded Skellam laws. Gupta, Kumar and Leonenko give the standard Skellam-Bessel probability formula while investigating generalized and time-changed processes, not the folded probability-mass curvature. Tomy and Veena review Skellam distributions and their applications without a folded-curvature classification. The Bessel Turán inequality is classical and used here as prior input, not presented as new. Earlier equivalent folded-count results under other terminology have not been ruled out independently.

## Limitations

At high intensity, the fixed-index violation window can occupy very small probability mass; no practical central-mass distortion is claimed. The bound \(ab\le1\) is sufficient but is **not asserted sharp**; no full two-rate log-concavity phase diagram is claimed. The theorem proves arbitrarily long *consecutive* violations at fixed imbalance and eventual recovery, not uniqueness or connectedness of the complete violating set for arbitrary parameters. The high-scale existence threshold \(s_0\) is not quantified uniformly in \(K\) or \(\theta\). Independence is essential to the Bessel formula. The analysis does not cover general multivariate folded Poisson contrasts or nonlinear functionals of several counts.

## References

1. L. Badiella, J. del Castillo and P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters 201 (2023), 109900, doi:10.1016/j.spl.2023.109900; available online 2023-06-26. https://doi.org/10.1016/j.spl.2023.109900
2. N. Gupta, A. Kumar and N. Leonenko, *Skellam Type Processes of Order K and Beyond*, arXiv:2003.09471 (first posted 2020). https://arxiv.org/abs/2003.09471
3. L. Tomy and G. Veena, *A Retrospective Study on Skellam and Related Distributions*, Austrian Journal of Statistics 51 (2022), 102–111, doi:10.17713/ajs.v51i1.1224. https://ajs.or.at/index.php/ajs/article/view/1224/748
4. Á. Baricz, S. Ponnusamy and M. Vuorinen, *Functional inequalities for modified Bessel functions*, arXiv:1009.4814 (2010), for the classical Bessel Turán context. https://arxiv.org/abs/1009.4814
