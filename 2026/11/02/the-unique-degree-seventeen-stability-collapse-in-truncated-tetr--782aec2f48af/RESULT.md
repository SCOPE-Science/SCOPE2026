# The unique degree-seventeen stability collapse in truncated-tetrahedron harmonic sampling

## Finding

Let \(X\) be the twelve unit-normalized vertices of a regular truncated tetrahedron. For each integer \(k\ge0\), let \(E_k\) evaluate all real spherical harmonics of *exact* degree \(k\) at these twelve nodes. With \(P_k(1)=1\) denoting the Legendre polynomial, define the symmetric, unit-diagonal sampling Gram matrix
\[
 K_k=(P_k(x\cdot y))_{x,y\in X}.
\]
The exact ranks are
\[
 (\operatorname{rank}E_0,\ldots,\operatorname{rank}E_6)=(1,3,5,7,9,11,9),
 \qquad \operatorname{rank}E_k=12\quad(k\ge7).
\]
Thus unrestricted interpolation of twelve prescribed values by a *single* spherical-harmonic degree begins at degree seven and holds permanently thereafter, although degree six loses two directions compared with degree five.

There is a uniquely severe later loss of stability despite continuing full rank. At degree seventeen,
\[
 \lambda_{\min}(K_{17})=\frac{462143232}{4177248169415651}
 =1.1063341541056885\ldots\times10^{-7}.
\]
This is the eigenvalue of the all-ones vector. For all other full-rank degrees,
\[
 \lambda_{\min}(K_k)>\frac1{10000}\quad(k\ge7,\ k\ne17).
\]
Therefore degree seventeen is the **unique global maximizer** of the spectral condition number:
\[
 \kappa_2(K_{17})>10^6,
 \qquad \kappa_2(K_k)<120000\quad(k\ge7,\ k\ne17).
\]
The condition number here belongs to the **Gram** matrix, not to the unsquared evaluation operator; the latter has condition number \(\sqrt{\kappa_2(K_k)}\).

## Assumptions and scope

Construct the nodes by taking every choice of a coordinate position \(i\in\{1,2,3\}\) and signs \(a,b\in\{-1,1\}\), placing \(3ab\) in coordinate \(i\) and \(a,b\) in the remaining coordinates in increasing order, and dividing the vector by \(\sqrt{11}\). This gives twelve distinct points, the usual regular truncated-tetrahedron orbit. There are no antipodal identifications. The degree \(k\) is any nonnegative integer; sampling values are unrestricted real numbers when the evaluation map is surjective.

Equip \(\mathcal H_k(S^2)\) with the \(L^2\) inner product for probability-normalized surface measure. For an orthonormal real basis \(\{Y_{km}\}_{m=-k}^{k}\), the addition theorem gives
\[
 (E_kE_k^{\mathsf T})_{x,y}=
 \sum_{m=-k}^{k}Y_{km}(x)Y_{km}(y)=(2k+1)P_k(x\cdot y).
\]
Thus \(\operatorname{rank}E_k=\operatorname{rank}K_k\), and the positive eigenvalues of \(K_k\) control exact-degree interpolation stability.

## Proof

**1. A four-distance Gram matrix.** The pairwise numerators \(11x\cdot y\) belong to \(\{11,7,-1,-5,-9\}\). Every row has exactly one \(11\), three \(7\), four \(-1\), two \(-5\), and two \(-9\). The explicit construction above supplies the complete ordered \(12\)-by-\(12\) table, which is reconstructed without geometric tolerances in `CHECKER.py`.

**2. Exact rational values.** Put \(F_k(t)=22^kP_k(t/11)\) for the five integer numerators. The Legendre recurrence becomes the integer recurrence
\[
 F_0(t)=1,\quad F_1(t)=2t,\quad
 (k+1)F_{k+1}(t)=2t(2k+1)F_k(t)-484kF_{k-1}(t).
\]
The checker verifies every division is exact, so all Gram entries are rational without floating-point rounding. Fraction-exact Gaussian elimination gives ranks \(1,3,5,7,9,11,9\) for degrees zero through six.

**3. Degree seventeen.** The equal row sums show that the constant vector is an eigenvector, with eigenvalue
\[
 s_{17}=1+3P_{17}(7/11)+4P_{17}(-1/11)
 +2P_{17}(-5/11)+2P_{17}(-9/11)
 =\frac{462143232}{4177248169415651}.
\]
Direct rational comparison proves \(0<s_{17}<10^{-6}\). To prove this is the *least* eigenvalue, let \(J\) be the twelve-by-twelve all-ones matrix. Exact fraction-free Sylvester elimination proves
\[
 K_{17}-\frac1{10000}\left(I-\frac J{12}\right)+\frac J{12}\succ0.
\]
On the constants this matrix has eigenvalue \(s_{17}+1\), while on their orthogonal complement its eigenvalues are those of \(K_{17}\) decreased by \(10^{-4}\). Hence every other eigenvalue exceeds \(10^{-4}\), and \(s_{17}\) is uniquely minimal (simple).

**4. All other finite degrees.** For every integer \(7\le k\le100\), \(k\ne17\), exact fraction-free Sylvester elimination proves
\[
 K_k-\frac1{10000}I\succ0.
\]
There are 93 separate positive-definiteness checks. Each is a certificate based on the *whole* Gram matrix: the integer matrix \(10000(22^kK_k)-22^kI\) is tested by all twelve leading principal minors, using division-exact Bareiss elimination, not by approximate eigenvalues. The complete executable certificate is `CHECKER.py`.

**5. Infinite tail.** For any \(-1<t<1\), Bernstein's Legendre bound says
\[
 |P_k(t)|<\sqrt{\frac{2}{\pi(k+1/2)\sqrt{1-t^2}}}.
\]
Using \(\pi>3\), for \(|t|\in\{9/11,5/11,1/11,7/11\}\), respectively, the four coefficients multiplying \(1/\sqrt{k+1/2}\) are bounded by \(1079/1000,866/1000,820/1000,932/1000\). The checker proves these radical estimates by rational comparisons. The row multiplicities give
\[
 \sum_{y\ne x}|P_k(x\cdot y)|
 <\frac{2(1079)+2(866)+4(820)+3(932)}{1000\sqrt{k+1/2}}
 =\frac{4983}{500\sqrt{k+1/2}}<\frac{10}{\sqrt{k+1/2}}.
\]
For \(k\ge101\), this is less than \(1-10^{-4}\), by the exact rational inequality \(100<(203/2)(1-10^{-4})^2\). Gershgorin's theorem now proves \(\lambda_{\min}(K_k)>10^{-4}\) for *every* such degree. This proves all-degree positive definiteness and the permanent interpolation threshold.

**6. Unique worst-conditioned degree.** Every Gram matrix is positive semidefinite with trace twelve. Therefore any full-rank degree other than seventeen has
\(\kappa_2(K_k)<12\cdot10000=120000\). At degree seventeen, its smallest eigenvalue is smaller than \(10^{-6}\), while its largest eigenvalue is at least the average eigenvalue one. Thus \(\kappa_2(K_{17})>10^6\), strictly separating it from every competing degree. No untested intermediate or asymptotic degrees remain.

## Verification

Run `python3 CHECKER.py` with a standard Python 3 interpreter. It uses only the standard library. The script reconstructs all twelve coordinates and their pairwise inner-product multiplicities; checks the seven low-degree ranks with exact rational elimination; computes the exact constant eigenvalue at degree seventeen; confirms the strict positive-definite complement bound; checks 93 separate finite degrees using exact integer elimination; and verifies every rational inequality used in the all-degree tail argument. Its final message is `TRUNCATED_TETRAHEDRON_HARMONIC_CERTIFICATE_OK`.

The proof of the infinite tail uses the published Bernstein inequality and Gershgorin's theorem. Finite arithmetic alone does not imply the all-degree assertion. The certificate tests positivity by all leading minors, and exact integer divisibility is enforced at every elimination step.

## Relationship to prior work

Marzo studies interpolation and sampling density for growing spherical-harmonic spaces and changing node families; the present question is about one fixed twelve-node configuration and **exact** individual harmonic degrees. Bannai–Okuda–Tagami study zero-sum harmonic-index designs and corresponding cardinality bounds, not the complete positive Gram spectrum of this non-antipodal configuration. Wang records the Bernstein-type Legendre estimate used here for the infinite tail. No novelty is claimed for the spherical addition theorem, Legendre recurrence, Bernstein inequality, or the regular truncated tetrahedron itself.

The contribution is the complete rank sequence together with the unique global spectral-conditioning collapse at degree seventeen, including an exact extremal eigenvalue and a certified separation from *all* other full-rank degrees.

## Limitations

The theorem concerns the twelve stated vertices, the exact-degree real spherical harmonics on \(S^2\), the unit-diagonal Legendre Gram normalization, and integer degrees. It does not classify conditioning of cumulative-degree polynomial spaces, perturbed node sets, or other Archimedean solids. The strict bounds separate the unique worst condition number but do not give its exact largest eigenvalue or exact condition-number value. An analogous historical computation could exist in polyhedral cubature or tetrahedral representation theory; independent mathematical validation is not claimed.

## References

1. Jordi Marzo, *Marcinkiewicz–Zygmund inequalities and interpolation by spherical harmonics*, arXiv:math/0611503v1, first posted 2006-11-16. https://arxiv.org/abs/math/0611503
2. Eiichi Bannai, Takayuki Okuda, and Makoto Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1, first posted 2013-08-23. https://arxiv.org/abs/1308.5101
3. Haiyong Wang, *A new and sharper bound for Legendre expansion of differentiable functions*, arXiv:1803.00336v1, posted 2018-03-01, Lemma 2.1 (the Bernstein estimate). https://arxiv.org/abs/1803.00336
4. *Truncated Tetrahedron*, Wolfram MathWorld, https://mathworld.wolfram.com/TruncatedTetrahedron.html (geometric reference; no dated priority inferred).
