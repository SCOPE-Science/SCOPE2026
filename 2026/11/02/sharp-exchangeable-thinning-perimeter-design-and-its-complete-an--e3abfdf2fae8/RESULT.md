# Sharp exchangeable-thinning perimeter design and its complete angular stability spectrum

## Finding
Let \(n\ge3\) distinct vertices lie on a common radius-\(R\) circle. Under any **exchangeable** random deletion rule, conditional on the number retained, the subset is uniform. Provided that at least two vertices survive with positive probability, equally spaced vertices uniquely maximize the **expected perimeter of the surviving convex hull**. Moreover, the complete local angular Hessian at the regular arrangement is explicit and strictly positive on every nonconstant discrete Fourier mode.

Write \(\rho_r=\Pr(K=r)\). The sharp expected-perimeter maximum is
\[
M=2Rn\sum_{k=1}^{n-1}w_k\sin(k\pi/n),\qquad
w_k=\sum_{r=2}^{n-k+1}\rho_r\frac{\binom{n-k-1}{r-2}}{\binom nr}.
\]
For independent Bernoulli retention of probability \(p\in(0,1]\), the sharp bound simplifies to
\[
M_{n,p}=\frac{2Rnp^2\sin(\pi/n)\bigl(1+(1-p)^n\bigr)}{1-2(1-p)\cos(\pi/n)+(1-p)^2}.
\]

## Assumptions and scope
The original vertices are distinct and ordered counterclockwise on one Euclidean circle of radius \(R>0\), with positive consecutive central angles \(\theta_0,\ldots,\theta_{n-1}\) summing to \(2\pi\). The random subset law is invariant under all permutations of the vertex labels. An empty or one-point hull has perimeter zero, while a two-point segment has the conventional doubled-edge perimeter. Define \(S_{i,k}=\sum_{j=0}^{k-1}\theta_{i+j\bmod n}\) for \(1\le k\le n-1\). We require \(\sum_{r\ge2}\rho_r>0\) for strict optimality; with no possible surviving pair every arrangement has expected perimeter zero.

## Proof
**Exact expected-perimeter identity.** For a fixed retained cardinality \(r\ge2\), an oriented chord joining vertices \(i\) and \(i+k\) appears as a consecutive boundary edge precisely when both endpoints are retained and none of the \(k-1\) intermediate vertices is retained. Its conditional probability is \(\binom{n-k-1}{r-2}/\binom nr\), interpreted as zero when impossible. For \(r=2\), both oriented complementary arcs contribute the same chord, consistently producing the doubled-edge perimeter. Since chord length is \(2R\sin(S_{i,k}/2)\), linearity of expectation gives
\[
\mathbb EP=2R\sum_{k=1}^{n-1}w_k\sum_{i=0}^{n-1}\sin(S_{i,k}/2).
\]

**Global uniqueness.** For each fixed \(k\), \(\sum_iS_{i,k}=2\pi k\) and every \(S_{i,k}\in(0,2\pi)\). The function \(t\mapsto\sin(t/2)\) is strictly concave on \((0,2\pi)\). Hence
\[
\sum_i\sin(S_{i,k}/2)\le n\sin(k\pi/n).
\]
All \(w_k\) are nonnegative. Further, \(w_1=\sum_{r\ge2}\rho_r r(r-1)/(n(n-1))>0\). Equality of the weighted sum therefore forces equality for \(k=1\), so all \(\theta_i=2\pi/n\); conversely that regular arrangement attains every equality.

**Complete quadratic curvature.** Fix real \(\delta_j\) with \(\sum_j\delta_j=0\), and put \(\theta_j=2\pi/n+t\delta_j\) for sufficiently small real \(t\). Taylor expansion at each \(S_{i,k}=2\pi k/n\) gives, since all first derivatives sum to zero,
\[
M-\mathbb EP=\frac{Rt^2}{4}\sum_{k=1}^{n-1}w_k\sin(k\pi/n)\sum_{i=0}^{n-1}\left(\sum_{j=0}^{k-1}\delta_{i+j}\right)^2+O(t^3).
\]
Use the normalized discrete transform \(\widehat\delta_m=n^{-1}\sum_{j=0}^{n-1}\delta_je^{-2\pi imj/n}\). Parseval and the finite geometric sum yield
\[
M-\mathbb EP=\frac{Rnt^2}{4}\sum_{m=1}^{n-1}\Lambda_m|\widehat\delta_m|^2+O(t^3),\quad
\Lambda_m=\sum_{k=1}^{n-1}w_k\sin(k\pi/n)\frac{\sin^2(km\pi/n)}{\sin^2(m\pi/n)}.
\]
Here \(m=1,\ldots,n-1\), so the denominator never vanishes; \(w_1>0\) forces \(\Lambda_m\ge w_1\sin(\pi/n)>0\) for all such \(m\). This is a complete diagonal description of local sensitivity to arbitrary angular perturbations, not merely an unspecified positive-definiteness argument.

**Bernoulli simplification.** If each vertex survives independently with probability \(p\), the consecutive-chord event has probability \(w_k=p^2(1-p)^{k-1}\). Set \(q=1-p\), \(\alpha=\pi/n\). The elementary finite complex-geometric-series identity
\[
\sum_{k=1}^{n-1}q^{k-1}\sin(k\alpha)=\frac{\sin\alpha(1+q^n)}{1-2q\cos\alpha+q^2}
\]
gives the sharp closed formula in the finding.

## Verification
Run the standalone `verify.py` with Python 3; it prints `ALL_CHECKS_PASSED` and `FIXED_SIZE_AND_FOURIER_CHECKS_PASSED`. The code independently enumerates every subset for small \(n\), compares with the exact chord-count identity, checks the Bernoulli closed form and optimizer, and compares direct angular quadratic curvature with its Fourier diagonalization. These finite checks corroborate but do not replace the above general proof. No external data files are required.

## Relationship to prior work
Madras and KC (2006) already computed regular-polygon uniform-subset perimeter expectations, including the regular fixed-cardinality case, and those baseline values are not claimed as new. Morin (first public January 29, 2024) studies independent interior sampling in regular polygons; his random model and questions differ from exchangeable deletion of finitely many initially specified cyclic vertices. Reitzner, Schütt and Werner (first public November 14, 2019) study continuous arclength sampling from polytope boundaries, not discrete vertex deletion. The present claim concerns simultaneous **optimization over arbitrary cyclic angular spacings and all exchangeable deletion laws**, and the explicit, mode-resolved Hessian. The regularity inequality can be viewed as a weighted combination of classical concave cyclic chord inequalities; the structural local curvature classification is the refinement that is not supplied by merely knowing an optimizer.

## Limitations
The result assumes cocircular Euclidean vertices, exchangeable subset laws, and the doubled-segment perimeter convention. It does not imply stochastic dominance of full perimeter distributions. The displayed local Hessian is not a sharp global finite-deformation stability coefficient. The result does not apply directly to noncyclic polygons or arbitrary nonexchangeable retention probabilities. Earlier work on diagonal-chord sums could contain an equivalent extremal inequality; exhaustive historical priority verification remains incomplete, particularly for the general second-variation spectrum.

## References
- L. Morin, *Probability that n points are in convex position in a regular κ-gon: Asymptotic results*, arXiv:2401.16207, initial posting January 29, 2024, https://arxiv.org/abs/2401.16207.
- A. Madras and S. KC, *Randomly Generated Triangles whose Vertices are Vertices of Regular Polygons*, Rose-Hulman Undergraduate Mathematics Journal 7(2), Article 12 (2006), https://scholar.rose-hulman.edu/rhumj/vol7/iss2/12/.
- M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (2019), https://arxiv.org/abs/1911.05917.
