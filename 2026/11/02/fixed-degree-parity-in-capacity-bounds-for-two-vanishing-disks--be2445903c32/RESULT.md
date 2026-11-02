# Fixed-degree parity in capacity bounds for two vanishing disks

## Finding

Write \(K_{a,r}=\overline{D(-a,r)}\cup\overline{D(a,r)}\) for \(a>0\) and \(0<r<a\), and denote its logarithmic capacity by \(C_{a,r}\). For each integer \(n\geq1\), define the least-squares quantity of Ransford [1] by
\[
b_n(K)=\frac{1}{\sqrt{n\pi}}\inf_{p\ \mathrm{monic},\ \deg p=n}\left(\int_K|p'(z)|^2\,dA(z)\right)^{1/2}.
\]
As \(r/a\to0\), with the integer index fixed, there is a sharp parity dichotomy:
\[
C_{a,r}\sim\sqrt{2ar},\qquad
b_{2k}(K_{a,r})\sim(2ar)^k\quad(k\geq1),
\]
whereas
\[
b_{2k+1}(K_{a,r})\sim2^k a^k r^{k+1}\sqrt{\frac{2(2k+1)}{k+1}}\quad(k\geq0).
\]
Consequently,
\[
\lim_{r/a\to0}\frac{b_{2k}(K_{a,r})}{C_{a,r}^{2k}}=1,
\qquad
\frac{b_{2k+1}(K_{a,r})}{C_{a,r}^{2k+1}}
\sim\sqrt{\frac{2k+1}{k+1}}\sqrt{\frac ra}.
\]
Thus every fixed even index becomes asymptotically sharp in Ransford's lower bound as two disks shrink, while every fixed odd index loses a factor of order \(\sqrt{r/a}\) before taking the root. The assertion is not uniform as the index tends to infinity.

## Assumptions and scope

Area measure is unnormalized \(dA=dx\,dy\); all polynomials are complex and monic; the minimizing polynomial is monic of the specified degree. The disks have the same radius and antipodal centers and are disjoint. Logarithmic capacity is the reciprocal exponential of minimal logarithmic energy, with the standard normalization \(\operatorname{cap}\overline{D(0,R)}=R\). Both \(a>0\) and each fixed integer \(k\) are arbitrary. Homogeneity reduces the asymptotic calculation to fixed \(a\) and \(r\downarrow0\); all little-oh statements concern this limit.

## Proof

**Step 1 (capacity).** The equilibrium measures \(\sigma_-\) and \(\sigma_+\) of the circles \(\partial D(-a,r)\) and \(\partial D(a,r)\) have self-energies \(\log(1/r)\). Their mutual energy is exactly \(\log(1/(2a))\), by two applications of the harmonic mean-value property, since \(r<a\). The probability measure \((\sigma_-+\sigma_+)/2\) therefore has energy \(\frac12\log(1/r)+\frac12\log(1/(2a))\), proving \(C_{a,r}\geq\sqrt{2ar}\).

For the reverse estimate, let an arbitrary probability measure of finite logarithmic energy on the union have masses \(t\) and \(1-t\) on the two components. Each normalized component measure has energy at least \(\log(1/r)\), and pairs of points from different disks have distance at most \(2(a+r)\), so their cross-energy is at least \(\log(1/[2(a+r)])\). Thus the full energy is at least
\[
[t^2+(1-t)^2]\log(1/r)+2t(1-t)\log\frac1{2(a+r)}.
\]
Since the difference between the two logarithms is positive, the minimum for \(0\le t\le1\) occurs at \(t=1/2\). Hence \(C_{a,r}\leq\sqrt{2r(a+r)}\). The two bounds prove the asserted capacity equivalence.

**Step 2 (exact norm and parity).** Differentiating monic polynomials establishes
\[
b_n(K)^2=\frac n\pi\min_{q\ \mathrm{monic},\ \deg q=n-1}\int_K|q(z)|^2\,dA(z).
\]
Taylor expansion and orthogonality of monomials on a disk give, for any polynomial \(q\) of degree \(d\) and any center \(c\), the exact identity
\[
\int_{D(c,r)}|q(z)|^2dA(z)
=\pi\sum_{j=0}^{d}\frac{r^{2j+2}}{j+1}\left|\frac{q^{(j)}(c)}{j!}\right|^2.
\tag{1}
\]
The area inner product on the union is strictly positive definite on polynomials, so there is one monic least-norm polynomial \(q_{d,r}\). Invariance under \(z\mapsto-z\), followed by uniqueness, gives \(q_{d,r}(-z)=(-1)^d q_{d,r}(z)\).

**Step 3 (even index).** Fix \(k\ge1\) and take \(d=2k-1\). The monic odd competitor \(Q(z)=z(z^2-a^2)^{k-1}\) vanishes to order \(k-1\) at each center. Its first nonzero Taylor coefficient at \(a\) is \(2^{k-1}a^k\). Applying (1) at both centers yields
\[
\min_{\deg q=2k-1\ \mathrm{monic}}\|q\|_{L^2(K_{a,r})}^2
\le\frac{2\pi}{k}(2^{k-1}a^k)^2r^{2k}(1+O_{a,k}(r^2)).
\tag{2}
\]
By minimality and (1), the Taylor coefficients of \(q_{2k-1,r}\) at \(a\) of orders \(0,\ldots,k-1\) are bounded respectively by \(O(r^{k-1-j})\). The map from odd polynomials of degree at most \(2k-1\) to those \(k\) Taylor coefficients is invertible: an odd polynomial in its kernel would have zeros of multiplicity at least \(k\) at both \(a\) and \(-a\), impossible unless it is zero. Consequently, coefficient vectors of the minimizing polynomials are bounded as \(r\downarrow0\). Every convergent subsequence has a monic odd limit with zero multiplicity at least \(k-1\) at both centers; this limit is necessarily \(Q\). Thus the order-\(k-1\) Taylor coefficient of the minimizer converges to \(2^{k-1}a^k\), and (1) gives the matching lower bound in (2). Therefore
\[
\min\|q\|_{L^2(K_{a,r})}^2
\sim\frac{2\pi}{k}(2^{k-1}a^k)^2r^{2k}
\]
and, multiplying by \(2k/\pi\), \(b_{2k}(K_{a,r})\sim(2ar)^k\).

**Step 4 (odd index).** Fix \(k\ge0\) and take \(d=2k\). The monic even competitor \(Q(z)=(z^2-a^2)^k\) vanishes to order \(k\) at both centers and has order-\(k\) Taylor coefficient \((2a)^k\) at \(a\). The exact disk-norm formula gives
\[
\min_{\deg q=2k\ \mathrm{monic}}\|q\|_{L^2(K_{a,r})}^2
\le\frac{2\pi}{k+1}(2a)^{2k}r^{2k+2}(1+O_{a,k}(r^2)).
\tag{3}
\]
The even-polynomial map to the first \(k+1\) jets at \(a\) is invertible: a kernel element would vanish to order at least \(k+1\) at each of \(a,-a\), exceeding degree \(2k\). From (1) and (3) the first \(k\) jets of the minimizer tend to zero, and the last is bounded. Every coefficient subsequential limit is the unique monic even polynomial with those zeros, \(Q\). Keeping only the order-\(k\) terms in (1) gives the matching lower bound and hence
\[
\min\|q\|_{L^2(K_{a,r})}^2
\sim\frac{2\pi}{k+1}(2a)^{2k}r^{2k+2}.
\]
Multiplication by \((2k+1)/\pi\), and extraction of a square root, proves the stated formula for \(b_{2k+1}\). For \(k=0\), the minimizer is the constant polynomial \(q=1\) and (3) is exact. The capacity equivalence from Step 1 gives both normalized ratios. \(\square\)

## Verification

Identity (1) is exact, with no asymptotic approximation. The proof's finite-dimensional coefficient compactness supplies the lower bounds for **every** fixed integer degree, not merely checked examples. Independent exact moment-matrix elimination gives, when \(a=1\), the identities
\[
b_1^2=2r^2,\quad b_2^2=4r^2+2r^4,\quad b_3^2=12r^4+2r^6,
\]
consistent with the theorem. The accompanying no-dependency checker evaluates moments as rational numbers, solves the exact Gram systems for indices \(1\) to \(6\), verifies the low-degree identities, and confirms convergence of their normalized coefficients for two rational radii. Such finite calculations corroborate, but do not replace, the analytical all-degree argument.

## Relationship to prior work

Ransford [1, Theorems 1.1–1.2] proves a universal least-squares lower bound and asymptotic sharpness in the limit of increasing degree on a fixed set; the fixed-degree degeneration of two separated disks and the even/odd asymptotic constants are separate limits not asserted there. Gustafsson–Putinar–Saff–Stylianopoulos [2] study large-degree Bergman polynomials on disconnected regions, including polynomial lemniscates, but their inspected results do not provide the two-shrinking-disk fixed-degree parity formula. Saff–Stahl–Stylianopoulos–Totik [3] also develop area-orthogonal-polynomial theory primarily in the large-degree regime. The present limits fix the polynomial degree first and then shrink the islands, so they cannot be inferred merely by interchanging asymptotic regimes.

## Limitations

The result requires two **equal** disks with antipodal centers. It gives fixed-degree leading terms only: no rate uniform in \(k\), no claim for arbitrary archipelagos, and no strict inequality for any prescribed finite \(r/a\) beyond the displayed asymptotics. Its priority relative to uninspected classical small-island asymptotics remains uncertain; independent literature verification and mathematical audit are not asserted.

## References

[1] Thomas Ransford, *A least-squares lower bound for capacity* (first public 17 October 2026), arXiv:2610.24702v1, https://arxiv.org/abs/2610.24702.

[2] Björn Gustafsson, Mihai Putinar, Edward B. Saff, and Nikos Stylianopoulos, *Bergman polynomials on an archipelago: Estimates, zeros and shape reconstruction*, Advances in Mathematics **222** (2009), 1405–1460, DOI:10.1016/j.aim.2009.06.010. Author-hosted text: https://mas.ucy.ac.cy/~nikos/AdvMath09.pdf.

[3] Edward B. Saff, Herbert Stahl, Nikos Stylianopoulos, and Vilmos Totik, *Orthogonal polynomials for area-type measures and image recovery*, arXiv:1403.6456v1, https://arxiv.org/abs/1403.6456.
