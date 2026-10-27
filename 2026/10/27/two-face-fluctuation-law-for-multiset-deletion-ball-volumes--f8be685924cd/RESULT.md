# Two-face fluctuation law for multiset deletion-ball volumes

## Finding
Let \(q\ge2\) and \(r\ge1\) be fixed integers. Sample a center \(X_n\) **uniformly among weak compositions** of \(n\) into \(q\) parts, not by sampling a uniformly random ordered word. For the multiset deletion-distance radius-\(r\) ball, put \(V_n=|B_r(X_n)|\) and let \(H_{q,r}\) be its unrestricted interior volume.

Define the nonnegative integers \(\delta_a\) and \(\omega_{ab}\), for \(0\le a,b<r\), as the numbers of unrestricted radius-\(r\) moves that respectively consume more than \(a\) objects from one designated coordinate, or consume more than \(a\) and \(b\) from two designated coordinates. Their exact finite sums are given below. Set \(D_n=H_{q,r}-V_n\), and for each fixed positive integer \(k\), define

\[
L_k=q(q-1)\sum_{a=0}^{r-1}\delta_a^k,
\]
\[
M_k=-q(q-1)\sum_{a=0}^{r-1}[(q-2)a+q-1]\delta_a^k
+\binom q2(q-1)(q-2)\sum_{a,b=0}^{r-1}
\left[(\delta_a+\delta_b-\omega_{ab})^k-\delta_a^k-\delta_b^k\right].
\]
Then the first two orders of **every fixed positive deficit moment** are
\[
\boxed{\mathbb E[D_n^k]=\frac{L_k}{n}+\frac{M_k}{n^2}+O_{q,r,k}(n^{-3}).}
\]
In particular,
\[
\boxed{\operatorname{Var}(V_n)=\frac{L_2}{n}+\frac{M_2-L_1^2}{n^2}+O_{q,r}(n^{-3}).}
\]
There is a discrete rare-defect law: the \(r\) numbers \(\delta_0>\cdots>\delta_{r-1}>0\) are distinct, and
\[
\Pr(V_n=H_{q,r}-\delta_a)=\frac{q(q-1)}n+O_{q,r}(n^{-2}),\quad 0\le a<r,
\]
while \(\Pr(V_n=H_{q,r})=1-q(q-1)r/n+O_{q,r}(n^{-2})\).

An exact finite-block specialization accompanies the general expansion: **for every \(n\ge6\), the ternary radius-two deletion-ball volume has exactly six values**, with respective numbers of centers

| Volume \(v\) | Number of ternary centers with \(V_n=v\) |
| --- | ---: |
| \(19\) | \(\binom{n-4}{2}\) |
| \(16\) | \(3(n-4)\) |
| \(13\) | \(3\) |
| \(12\) | \(3(n-3)\) |
| \(9\) | \(6\) |
| \(6\) | \(3\) |

Therefore the exact ternary radius-two variance is
\[
\boxed{\operatorname{Var}(V_n)=\frac{348n+1332}{(n+1)(n+2)}-\left(\frac{60n+36}{(n+1)(n+2)}\right)^2\quad(n\ge6).}
\]
Its leading and second-order coefficients are \(348\) and \(-3312\), respectively.

## Assumptions and scope
Identify a size-\(n\) multiset over \(q\) symbols with \(x\in\mathbb Z_{\ge0}^q\), \(\sum_i x_i=n\). The deletion metric on equal-size multisets is \(d(x,y)=\frac12\sum_i|x_i-y_i|\). The radius-\(r\) ball contains all \(y\) of size \(n\) with \(d(x,y)\le r\). Both \(q\) and \(r\) are independent of \(n\) in the asymptotic statements. The distribution is uniform on the \(\binom{n+q-1}{q-1}\) multiplicity vectors.

Define
\[
\mathcal Z_{q,r}=\{z\in\mathbb Z^q:\sum_i z_i=0,\ \sum_i z_i^+\le r\},\qquad H_{q,r}=|\mathcal Z_{q,r}|.
\]
The known interior volume also has the exact expression
\[
H_{q,r}=\sum_{j=0}^{\min(r,q-1)}\binom{q-1}{j}^2\binom{r-j+q-1}{q-1}.
\]
For \(d\ge1\), \(s\ge1\), and \(u\ge0\), define \(K_d(s,u)\) to count integral \(d\)-vectors with coordinate sum \(s\) and total negative mass \(u\). All coefficients are explicit:
\[
K_d(s,0)=\binom{s+d-1}{d-1},\qquad
K_d(s,u)=\sum_{j=1}^{\min(d-1,u)}\binom dj\binom{u-1}{j-1}\binom{s+u+d-j-1}{d-j-1}\quad(u\ge1).
\]
Empty sums are zero. Then
\[
\delta_a=\sum_{s=a+1}^r\sum_{u=0}^{r-s}K_{q-1}(s,u),
\]
\[
\omega_{ab}=\sum_{s=a+1}^r\sum_{t=b+1}^{r-s}\sum_{u=0}^{r-s-t}K_{q-2}(s+t,u)\quad(q\ge3),
\]
and set \(\omega_{ab}=0\) for \(q=2\). Binomial coefficients outside their combinatorial ranges are understood to vanish.

## Proof
**1. Difference-vector and boundary characterization.** A target \(x+z\) lies in \(B_r(x)\) precisely when \(z\in\mathcal Z_{q,r}\) and \(x_i+z_i\ge0\) for all coordinates. Thus \(D_n\) is the number of moves forbidden by at least one boundary coordinate. If \(x_i\ge r\), this coordinate forbids no move. If \(x_i=a<r\), exactly \(\delta_a\) moves violate coordinate \(i\). When precisely two coordinates \(i,j\) are below \(r\), inclusion-exclusion gives \(D_n=\delta_{x_i}+\delta_{x_j}-\omega_{x_i x_j}\).

To compute \(\delta_a\), fix the negative consumption \(-z_i=s\ge a+1\), then let the remaining coordinates have negative mass \(u\le r-s\) and sum \(s\). The remaining choices are counted by \(K_{q-1}(s,u)\). Fixing two negative consumptions gives \(\omega_{ab}\). For \(K_d\), choose its \(j\) strictly negative coordinates, compose \(u\) into \(j\) positive parts, and distribute total positive mass \(s+u\) among the remaining \(d-j\) coordinates. The stated sums follow. Since \(\delta_a-\delta_{a+1}\ge K_{q-1}(a+1,0)>0\), the single-facet deficits are strictly decreasing.

**2. Exact face probabilities.** For a specified coordinate and fixed \(a<r\), stars and bars gives
\[
p_1(n,a)=\Pr(X_{n,i}=a)=\frac{\binom{n-a+q-2}{q-2}}{\binom{n+q-1}{q-1}}=\frac{q-1}{n}-\frac{(q-1)[(q-2)a+q-1]}{n^2}+O_{q,r}(n^{-3}).
\]
For two specified distinct coordinates, when \(q\ge3\),
\[
p_2(n,a,b)=\frac{\binom{n-a-b+q-3}{q-3}}{\binom{n+q-1}{q-1}}=\frac{(q-1)(q-2)}{n^2}+O_{q,r}(n^{-3}).
\]
For \(q=2\), two coordinates cannot both lie below \(r\) once \(n>2r\). The probability of at least three below-\(r\) coordinates is \(O_{q,r}(n^{-3})\) (zero eventually if \(q\le3\)). These estimates follow from ratios of fixed-degree polynomials.

**3. Two-face expansion.** For fixed \(k\ge1\), start with the sum of \(\delta_a^k\) over all below-\(r\) single coordinates. At a center with exactly two small coordinates of sizes \(a,b\), correct this sum by
\[
(\delta_a+\delta_b-\omega_{ab})^k-\delta_a^k-\delta_b^k.
\]
The approximation is exact for zero, one, or two small coordinates; on the remaining event the error is bounded uniformly by a constant depending only on \(q,r,k\), so its expectation is \(O(n^{-3})\). Summing the single-coordinate and pair-coordinate probabilities and substituting the expansions in step 2 gives \(L_k\) and \(M_k\). In particular \(\operatorname{Var}(V_n)=\operatorname{Var}(D_n)=\mathbb E D_n^2-(\mathbb E D_n)^2\) yields the displayed variance coefficients. A single boundary coordinate of size \(a\) occurs with probability \(q(q-1)/n+O(n^{-2})\); double-boundary events contribute only \(O(n^{-2})\). This proves the rare-defect probabilities.

**4. Exact ternary radius-two spectrum.** At \(q=3,r=2\), direct enumeration of \(\mathcal Z_{3,2}\) gives \(H=19\), \(\delta_0=7\), \(\delta_1=3\), \(\omega_{00}=1\), and \(\omega_{01}=\omega_{10}=\omega_{11}=0\). When \(n\ge6\), at most two coordinates of \(x\) belong to \(\{0,1\}\). If none do, volume is \(19\). If precisely one coordinate is \(0\) or \(1\), the volume is \(12\) or \(16\). If two coordinates are \((0,0)\), \((0,1)\), or \((1,1)\), the volumes are \(6,9,13\), respectively. Stars and bars gives exactly the six multiplicities stated in the table. Their sum is \(\binom{n+2}{2}\). Summing deficits and squared deficits against these multiplicities gives
\[
\mathbb E[D_n]=\frac{60n+36}{(n+1)(n+2)},\quad
\mathbb E[D_n^2]=\frac{348n+1332}{(n+1)(n+2)},
\]
from which the exact variance and its expansion follow. Every center is covered, including all boundary cases for \(n\ge6\).

## Verification
The standalone `verify.py` performs direct finite enumeration of difference vectors and balls, independently recomputes \(K_d,\delta_a,\omega_{ab}\), and checks the exact six-class ternary spectrum and rational moments. It tests \(2\le q\le5\), \(1\le r\le3\), and finite positive lengths, with additional complete ternary radius-two censuses. The resulting output is recorded in `verification_output.txt`; it is evidence of finite consistency only. Steps 1–4, rather than finite checks, prove the infinite-length and asymptotic claims.

## Relationship to prior work
Kreindel, Essayag and Zabokritskiy (2026, arXiv:2603.18322v1) establish exact individual-center deletion-ball generating functions, maximal/minimal centers, pair-distance counts, and exact mean ball sizes. Their Section 4 and Section 5 provide the geometric setting and the known interior volume formula. The present claim does **not** assert originality of these existing facts. It instead develops the two-face inclusion-exclusion **distributional** expansion for all fixed moments, including an explicit sharp \(n^{-2}\) variance coefficient and rare-defect law, and an exact finite-volume **frequency** spectrum in the first nontrivial ternary radius-two case. In particular, computing individual balls or their mean alone is not the same statement as a second-moment law; the earlier center formula permits computations but does not state these distributional results.

The preceding multiset-code paper arXiv:2601.05636 treats code-size bounds and constructions. The earlier multiset/permutation-channel framework arXiv:1612.08837 studies coding models, constructions and bounds. The mathematical-index comparisons found neighboring variance results for sequence deletion/Levenshtein balls, whose center measure and channel metric differ. A complete publication-wide uniqueness assertion is not made.

## Limitations
The asymptotics hold with fixed alphabet size and radius. Uniform weak compositions differ from multinomial count vectors induced by random ordered words. This work does not establish improved code-size bounds, and the uniform single-center generating function of the cited 2026 source can in principle support alternative derivations. The exact finite-block distribution is proved only for ternary radius two and \(n\ge6\); the general result concerns its fixed-radius asymptotic distribution. Independent external validation has not been performed.

## References
1. A. Kreindel, I. B. Essayag, and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322v1 (first public 2026-03-18), https://arxiv.org/abs/2603.18322 .
2. A. Kreindel, I. B. Essayag, and A. L. Zabokritskiy, *Multiset Deletion-Correcting Codes: Bounds and Constructions*, arXiv:2601.05636v1 (first public 2026-01-09), https://arxiv.org/abs/2601.05636 .
3. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837 (2016), https://arxiv.org/abs/1612.08837 .
