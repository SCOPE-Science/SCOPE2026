# An explicit boundary martingale for orthogonal products of Euclidean balls

## Finding

**Theorem (uniform interior-to-surface martingale for ball products).** Fix an integer \(m\ge2\), positive integers \(d_1,\ldots,d_m\), and radii \(a_1,\ldots,a_m>0\). Let \(D=\sum_{i=1}^m d_i\), and let
\[
K=\prod_{i=1}^{m}a_i B_2^{d_i}\subset\mathbb R^D,
\qquad H=\sum_{i=1}^m\frac{d_i}{a_i}.
\]
Write \(U\) for the normalized \(D\)-dimensional volume law of \(K\), and \(Y\) for normalized Euclidean \((D-1)\)-dimensional Hausdorff measure on its boundary. Then there is an **explicit coupling** with the indicated marginal laws satisfying \(\mathbb E[Y\mid U]=U\). Consequently, for every continuous convex \(f:K\to\mathbb R\),
\[
\mathbb E f(U)\le\mathbb E f(Y).
\]
For any positive integer \(s\) and any continuous real function \(F:K^s\to\mathbb R\) that is separately convex in each argument, independent samples obey
\[
\mathbb E F(U^{(1)},\ldots,U^{(s)})
\le \mathbb E F(Y^{(1)},\ldots,Y^{(s)}).
\]
For any norm \(\|\cdot\|\) on \(\mathbb R^D\) and any real \(p\ge1\), this gives
\[
\mathbb E\|U^{(1)}-U^{(2)}\|^p\le
\mathbb E\|Y^{(1)}-Y^{(2)}\|^p.
\]
If at least one \(d_i\ge2\), the Euclidean-norm inequality is **strict** for every \(p\ge1\). The exact ambient covariance excess is
\[
\operatorname{Cov}(Y)-\operatorname{Cov}(U)
=\bigoplus_{i=1}^m\frac{2a_i}{H(d_i+2)}I_{d_i},
\]
and hence
\[
\mathbb E\|Y^{(1)}-Y^{(2)}\|_2^2
-\mathbb E\|U^{(1)}-U^{(2)}\|_2^2
=\frac4H\sum_{i=1}^m\frac{d_i a_i}{d_i+2}.
\]
In particular, every nonpolyhedral product in this family with \(D\ge3\) satisfies a convex-order statement stronger than the proposed mean-distance inequality, even though that inequality is false for general centrally symmetric bodies in dimensions three and higher.

## Assumptions and scope

The factors occupy mutually orthogonal Euclidean coordinate blocks. \(B_2^{d}\) denotes the closed Euclidean unit ball in dimension \(d\). A one-dimensional ball is a segment, and its boundary sphere \(S^0\) is the equiprobable pair of endpoints. All radii are strictly positive. A random boundary point is sampled according to **normalized Euclidean surface area**, not cone measure, Gaussian perimeter, or a pushforward under an arbitrary affine transformation. The product boundary has corners, but intersections of its distinct codimension-one faces have zero \((D-1)\)-dimensional Hausdorff measure.

The theorem itself remains valid for one factor, and for all-segment products, but the geometrically new class singled out is \(m\ge2\), \(D\ge3\), with at least one \(d_i\ge2\). Those bodies have curved boundary strata in dimensions where unrestricted interior–boundary convex domination fails.

## Proof

**1. Boundary-face weights.** For each \(i\), define the relatively open face stratum \(F_i\) where the \(i\)-th block lies on its sphere and every other block lies in its ball's interior. Let \(V=\operatorname{vol}_D(K)\). The identity \(\operatorname{area}(a_iS^{d_i-1})=(d_i/a_i)\operatorname{vol}_{d_i}(a_iB_2^{d_i})\), also valid for \(d_i=1\), gives
\[
\mathcal H^{D-1}(F_i)=V\frac{d_i}{a_i},\qquad
\mathcal H^{D-1}(\partial K)=VH.
\]
It follows that the normalized boundary law first chooses an index \(J=i\) with probability
\[
q_i=\frac{d_i/a_i}{H},
\]
then samples the selected block uniformly from \(a_iS^{d_i-1}\) and every other block independently, uniformly from its ball.

**2. Explicit conditional-mean-preserving transfer.** Sample \(U=(U_1,\ldots,U_m)\) with the uniform volume law. For each block, write \(U_i=R_i\Theta_i\), with independent uniform direction \(\Theta_i\in S^{d_i-1}\), radial variable \(0<R_i<a_i\), and density
\[
\frac{d_i r^{d_i-1}}{a_i^{d_i}},\qquad 0<r<a_i.
\]
The independence holds also in dimension one, with the radial variable the absolute coordinate. Independently choose \(J\) with law \((q_1,\ldots,q_m)\). Keep \(Y_j=U_j\) for all \(j\ne J\). Conditionally on \(J=i\) and on \(U_i=R_i\Theta_i\), let
\[
Y_i=\varepsilon_i a_i\Theta_i,\qquad
\Pr(\varepsilon_i=+1\mid U,J=i)=\frac{1+R_i/a_i}{2},\quad
\Pr(\varepsilon_i=-1\mid U,J=i)=\frac{1-R_i/a_i}{2}.
\]
The sign probabilities both belong to \((0,1)\) almost surely. By direct subtraction, \(\mathbb E[\varepsilon_i a_i\Theta_i\mid U,J=i]=R_i\Theta_i=U_i\), and the other blocks are unchanged. Thus \(\mathbb E[Y\mid U,J]=U\), yielding \(\mathbb E[Y\mid U]=U\).

For the marginal of \(Y\), note that \(\Theta_i\) is uniform on its sphere and independent of \(R_i\); multiplying by either sign, even with a radial-dependent sign probability, preserves the uniform sphere law. This sphere variable is independent of all other blocks. Consequently the law of \(Y\) conditional on \(J=i\) is exactly the product law on \(F_i\) in Step 1. Mixing with weights \(q_i\) proves the required Euclidean surface-area marginal, not merely an abstract outward coupling.

**3. Convex observables.** Conditional Jensen now gives
\[
f(U)=f(\mathbb E[Y\mid U])\le\mathbb E[f(Y)\mid U].
\]
Integrating establishes convex-order domination. For independent pairs \((U^{(j)},Y^{(j)})\), apply the one-coordinate inequality successively, keeping the other arguments fixed; independence and separate convexity justify every step. Taking \(F(x,z)=\|x-z\|^p\) proves the norm-moment inequalities because a norm raised to a power \(p\ge1\) is convex.

For strict Euclidean distance inequalities when some \(d_i\ge2\), consider the positive-probability event that both independent couplings select that block \(i\). Almost surely the two radial factors lie strictly between zero and their radii, and the two independent directions in this block are linearly independent. Conditional on the interior samples, the four possible sign pairs yield four positive-probability outputs whose differences have a nondegenerate parallelogram as their projection onto that block. They therefore cannot all lie on one nonnegative Euclidean ray. The equality condition in the triangle inequality gives a strict conditional Jensen inequality for \(\|\cdot\|_2\), and therefore for every \(\|\cdot\|_2^p\), \(p\ge1\). Integration gives strictness.

**4. Exact quadratic excess.** All block means vanish by central symmetry. Uniform points in a radius-\(a_i\), dimension-\(d_i\) ball and sphere have covariance matrices \(a_i^2I_{d_i}/(d_i+2)\) and \(a_i^2I_{d_i}/d_i\), respectively. By Step 1, only a proportion \(q_i\) of the boundary law's \(i\)-th block is drawn from the sphere. Its covariance increment is therefore
\[
q_i\left(\frac{a_i^2}{d_i}-\frac{a_i^2}{d_i+2}\right)I_{d_i}
=\frac{2a_i}{H(d_i+2)}I_{d_i}.
\]
Cross-block covariances vanish by sign symmetry. Finally, for any centered independent and identically distributed pair, \(\mathbb E\|Z_1-Z_2\|_2^2=2\operatorname{tr}\operatorname{Cov}(Z)\). Taking the covariance trace establishes the asserted identity with coefficient \(4/H\).

## Verification

A standalone standard-library Python checker is included as `verify.py`. It performs exact rational identities for \(128\) parameter combinations, checks the block-covariance identity and the trace-derived pair-distance identity, and runs a seeded \(60{,}000\)-pair simulation for one nonspherical solid-cylinder example with block dimensions \((1,2)\) and radii \((1.3,0.7)\). Its successful recorded output is:

`VERIFY_OK exact_fraction_cases=128 sampled_pairs=60000 expected_distance2_gap=0.864040404 observed_distance2_gap=0.859806539`

These numerical samples check the implementation and normalizations; the proof in Steps 1–4, rather than finite simulation, establishes the infinite family and convexity statements. Reproduce by running `python verify.py` from a directory containing the embedded script.

## Relationship to prior work

Tokmachev (2026, arXiv:2607.08869) established convex-order domination for planar bodies with coincident area/surface centroids and for the indicated class of centered circumscribed polytopes. The curved, higher-dimensional Cartesian products addressed here are outside those stated classes. Shen (2026, arXiv:2608.06470) proved the planar distance inequality and constructed three-dimensional counterexamples that propagate under Cartesian multiplication by segments; his full available text does not give this positive higher-dimensional product-ball class. Lotnikov (2026, arXiv:2608.14848) independently described centrally symmetric counterexamples in every dimension at least three. These negative results preclude inferring the present theorem from central symmetry alone.

The result here is the explicit Euclidean **surface-law** martingale, its resulting simultaneous separately convex comparisons, and its exact covariance excess for arbitrary orthogonal ball factors and radii; neither the general conjecture nor the ball's radial convexity alone specifies the correct mixture weights for the nonsmooth product boundary. A title-level or abstract-only literature comparison cannot establish historical uniqueness; the full Tokmachev text was inaccessible during this review and remains an identified priority risk.

## Limitations

No claim is made for arbitrary centrally symmetric bodies, nonorthogonal affine images of ball products, alternative boundary measures, or general convex factors. An arbitrary affine transformation changes Euclidean boundary-area weights and need not preserve this coupling. The strictness assertion concerns the Euclidean norm and at least one factor dimension at least two; arbitrary norms have only the non-strict general inequality. Published-data searches do not certify historical originality, and no independent audit or external proof certification has been performed.

## References

1. A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869, first posted 2026-07-09, https://arxiv.org/abs/2607.08869.
2. Eric Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances*, arXiv:2608.06470, first posted 2026-08-06, https://arxiv.org/abs/2608.06470. Author-posted open text: https://www.researchgate.net/publication/411851456_The_Zaporozhets-Tarasov_Conjecture_on_Mean_Distances.
3. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848, first posted 2026-08-14, https://arxiv.org/abs/2608.14848.
