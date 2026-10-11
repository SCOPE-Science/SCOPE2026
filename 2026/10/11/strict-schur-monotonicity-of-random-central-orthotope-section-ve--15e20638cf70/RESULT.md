# Strict Schur monotonicity of random central orthotope-section vertex counts

## Finding

Fix an integer \(d\ge4\), and let
\[
B(a)=\prod_{i=1}^{d}[-a_i,a_i]\subset\mathbb R^d,
\qquad a_i>0.
\]
Choose \(u\) uniformly from \(S^{d-1}\) and let \(V_a(u)\) be the number of vertices of the central hyperplane section \(B(a)\cap u^\perp\). Define the normalized squared half-widths \(p_i=a_i^2/\sum_j a_j^2\). Then
\[
\boxed{\mathbb E[V_a]=\frac{2^d}{\pi}\sum_{i=1}^d\arcsin\sqrt{p_i}.}
\]
If the vector \(q\) is obtained from \(p\) by a nontrivial transfer from a larger coordinate to a smaller coordinate without reversing their order, then \(\mathbb E[V_q]>\mathbb E[V_p]\). Consequently the expectation is strictly Schur-concave in the normalized squared half-widths. Among all positive orthotopes with a fixed squared space-diagonal, the cube is the unique maximizer up to coordinate permutation:
\[
\boxed{2^{d-1}<\mathbb E[V_a]\le\frac{d\,2^d}{\pi}\arcsin\frac1{\sqrt d}.}
\]
The upper equality is attained precisely when \(a_1=\cdots=a_d\). The strict lower bound is sharp as an infimum: it is approached by orthotopes in which all but two half-widths tend to zero while the squared space-diagonal stays fixed. For the four-dimensional cube the exact expectation is \(32/3\). In fixed dimension, writing \(\bar p=(1/d,\ldots,1/d)\) and letting \(p\to\bar p\), the quantitative local deficit is
\[
\mathbb E[V_{\bar p}]-\mathbb E[V_p]
=\frac{2^d}{\pi}\frac{(d-2)d^2}{8(d-1)^{3/2}}
\sum_{i=1}^d(p_i-1/d)^2+O_d(\|p-\bar p\|_2^3).
\]
Here \(V_{\bar p}\) denotes the section-vertex count for any cube of that diagonal length. The exact formula also holds in dimensions two and three, but strict Schur monotonicity fails in dimension two, where the mean equals two.

## Assumptions and scope

Only positive side lengths and a uniformly oriented *central hyperplane* are considered. The normal is Haar-uniform, not selected by first choosing a random translation or a random interior point. Rescaling all half-widths changes no combinatorial section count. The degenerate directions in which the hyperplane contains a box vertex form a finite union of great subspheres and have probability zero. All exact vertex statements are almost-sure statements; no assertion is made about exceptional degenerate directions or noncentral affine slices.

## Proof

**Step 1: Vertex–edge correspondence.** For almost every normal \(u\), the section contains no box vertices and meets box edges transversally. A section vertex is precisely the intersection with an edge: at an interior point of a box edge, the \(d-1\) active coordinate facet equations together with the independent hyperplane equation uniquely determine a zero-dimensional face; conversely a generic section vertex needs \(d-1\) independent active box facet equations, hence lies in the relative interior of an edge. Distinct box edges give distinct section vertices outside the excluded measure-zero directions.

For a fixed coordinate index \(i\), exactly \(2^{d-1}\) box edges are parallel to that axis. Writing \(\varepsilon_j\in\{-1,1\}\) for the signs of the remaining fixed coordinates, the edge is crossed exactly when
\[
\left|\sum_{j\ne i}\varepsilon_j a_j u_j\right|<a_i|u_i|.
\]
The equality event has probability zero.

**Step 2: Exact random-direction crossing probability.** Generate the normal by \(u=G/\|G\|_2\), with \(G_1,\ldots,G_d\) independent standard normal variables. The common radial denominator cancels. For each fixed sign vector, \(X=\sum_{j\ne i}\varepsilon_j a_jG_j\) and \(Y=a_iG_i\) are independent centered normals with variances \(\sum_{j\ne i}a_j^2\) and \(a_i^2\). Since the ratio of independent standard normals is standard Cauchy,
\[
\mathbb P(|X|<|Y|)
=\frac2\pi\arctan\left(\frac{a_i}{\sqrt{\sum_{j\ne i}a_j^2}}\right)
=\frac2\pi\arcsin\sqrt{p_i}.
\]
Summing indicators over every axis and every sign choice gives the boxed exact expectation, with no assumption that the edge-crossing indicators are independent.

**Step 3: Strict transfer monotonicity.** Set \(f(t)=\arcsin\sqrt t\), so
\[
f'(t)=\frac1{2\sqrt{t(1-t)}}\qquad(0<t<1).
\]
For \(x>y>0\) satisfying \(x+y<1\), the identity
\[
x(1-x)-y(1-y)=(x-y)(1-x-y)>0
\]
shows \(f'(x)<f'(y)\). Fix the sum of the two coordinates and move a positive amount from the larger toward the smaller without passing equality. Along that path the derivative of \(f(x)+f(y)\) is \(f'(y)-f'(x)>0\). Every pair of coordinates of a strictly positive probability vector in dimension at least three has sum strictly below one. Therefore all nontrivial balancing transfers increase \(\sum_i f(p_i)\). The finite-transfer characterization of majorization gives strict Schur-concavity, and every nonuniform positive vector strictly majorizes the uniform vector, establishing the unique maximum.

**Step 4: Sharp lower infimum.** For \(0<x,y\) and \(x+y<1\), the derivative argument just proved, applied to the two coordinates with fixed sum, shows
\[
f(x)+f(y)>f(x+y)+f(0)=f(x+y).
\]
One may merge two positive coordinates at a time. Starting from at least three positive coordinates, the first merge strictly decreases the sum and subsequent merges cannot increase it. On a two-coordinate probability vector, \(f(t)+f(1-t)=\pi/2\) for \(0\le t\le1\). Consequently \(\sum_i f(p_i)>\pi/2\) for every strictly positive vector with at least three coordinates. Conversely as the last \(d-2\) coordinates vanish with two positive coordinates remaining, continuity gives \(\sum_i f(p_i)\to\pi/2\). Multiplying by \(2^d/\pi\) proves the sharp strict infimum.

**Step 5: Four-dimensional example and stability.** For the four-dimensional cube each \(p_i=1/4\), hence \(\sum_i f(p_i)=4\arcsin(1/2)=2\pi/3\) and \(\mathbb E[V_a]=32/3\). Moreover
\[
f''(t)=\frac{2t-1}{4[t(1-t)]^{3/2}},\qquad
f''(1/d)=-\frac{(d-2)d^2}{4(d-1)^{3/2}}.
\]
Taylor expansion around the uniform vector has no first-order term because \(\sum_i(p_i-1/d)=0\). Its second-order term gives the stated local deficit with remainder of order three for fixed dimension.

## Verification

The standalone, dependency-free `verify.py` evaluates the closed formula independently of a direct geometric enumeration of all transversal box-edge intersections. Six explicit orthotopes in dimensions three, four, and five were tested with 9,000 Gaussian normals each, together with 72,000 positive-simplex balancing transfers in dimensions three through eleven and three local-Hessian diagnostics. Replaying `python3 verify.py` prints `VERIFY_OK`. These are finite computational diagnostics; the proof of the theorem for all dimensions and all strictly positive half-widths is Steps 1–5, not the sampled tests.

## Relationship to prior work

Marichal and Mossinghoff's 2008 treatment of hypercube slices, slabs, and sections derives explicit **volume** formulas for central cube sections, but its section theorems do not give an expected **vertex count** or an orthotope shape-ordering theorem. Ball and Prodromou's 2009 combinatorial Vaaler theorem concerns the existence of an isotropic probability measure on every cube section, not the mean number of its vertices. A May 2015 mathematical discussion distinguished random translation from fixed-center slicing and noted that the central-case expressions involve unevaluated integrals. Swan's 2018 paper proves the constant expectation \(2^k\) for \(k\)-flats whose **translation is uniform among intersecting positions**; it explicitly distinguishes this from center-fixed slicing. Its conclusion does not imply the present formula or majorization rigidity. Earlier results about random cones and three-dimensional dual shadow counts are related context rather than claims to the higher-dimensional central-orthotope theorem.

The strict lower bound here has the same numerical value \(2^{d-1}\) as Swan's translated-section expectation with \(k=d-1\), but the probability spaces are different: here it is a nonattained central-section infimum, not a constant over nondegenerate boxes. Likewise the four-dimensional exact mean \(32/3\) is not obtained from any three-dimensional axial-octahedron shadow probability.

## Limitations

The contribution concerns a single codimension, namely hyperplane sections, and the first moment of vertex count. It does not determine the full face-vector distribution, variance of the count, random noncentral slice laws, nor the same optimization for arbitrary parallelotopes. The lower bound is an infimum rather than a positive-orthotope minimizer. The displayed expansion is local for each fixed dimension. Literature comparisons cannot exclude an earlier unindexed derivation of this elementary-looking Cauchy–majorization identity.

## References

1. J.-L. Marichal and M. J. Mossinghoff, *Slices, Slabs, and Sections of the Unit Hypercube*, Online Journal of Analytic Combinatorics 3 (2008), published 29 January 2008. https://combinatorialpress.com/article/ojac/vol3/Marichal_2008.pdf
2. K. M. Ball and M. Prodromou, *A Sharp Combinatorial Version of Vaaler's Theorem*, Bulletin of the London Mathematical Society 41 (2009), 853–858, first published online 13 August 2009. https://doi.org/10.1112/blms/bdp062 ; open manuscript https://warwick.ac.uk/fac/sci/maths/people/staff/keith_ball/vaalm2.pdf
3. *Expected number of vertices of a hypercube slice—is this new/interesting?*, public mathematical discussion dated 12 May 2015. https://mathoverflow.net/questions/206414/expected-number-of-vertices-of-a-hypercube-slice-is-this-new-interesting
4. H. Swan, *Expected Number of Vertices of a Hypercube Slice*, American Mathematical Monthly 123 (2016), 600–604; open full text arXiv:1808.09482v1, submitted 28 August 2018. https://arxiv.org/html/1808.09482v1
5. T. M. Cover and B. Efron, *Geometrical Probability and Random Points on a Hypersphere*, Annals of Mathematical Statistics 38 (1967), 213–220, on face numbers of random cones rather than a single central orthotope section. https://www-isl.stanford.edu/~cover/papers/paper6.pdf
