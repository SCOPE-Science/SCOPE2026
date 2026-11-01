# An exact vertex-source geodesic law for cross-polytopes in all dimensions

## Finding

Let \(n\ge2\), let \(C_n=\{x\in\mathbb R^n:\sum_{i=1}^n|x_i|\le1\}\), and equip its boundary \(S_n=\partial C_n\) with the intrinsic length metric \(d_{S_n}\) induced by ordinary Euclidean arclength. Write \(v=e_1\). **For every** \(p=(p_1,\ldots,p_n)\in S_n\), the squared intrinsic distance obeys the pointwise identity

\[
\boxed{d_{S_n}(v,p)^2=\|v-p\|_2^2+\frac4{n-1}\max\{0,-p_1\}.}
\]

In particular, among all target points \(p\in S_n\setminus\{v\}\), the sharp intrinsic-to-chord stretch is

\[
\boxed{\max_{p\ne v}\frac{d_{S_n}(v,p)}{\|v-p\|_2}=\sqrt{\frac n{n-1}},}
\]

with equality **only** at the opposite vertex \(p=-v\).

A statistical consequence is equally explicit. Let \(P\) be distributed uniformly according to \((n-1)\)-dimensional Hausdorff area on \(S_n\), and define the nonnegative squared-geodesic excess \(Z=d_{S_n}(v,P)^2-\|v-P\|_2^2\). Then \(\Pr(Z=0)=1/2\), and for \(0\le z\le4/(n-1)\),

\[
\boxed{\Pr(Z>z)=\tfrac12\bigl(1-\tfrac{n-1}{4}z\bigr)^{n-1}.}
\]

Consequently,

\[
\boxed{\mathbb E\,d_{S_n}(v,P)^2=\frac{n+3}{n+1}+\frac2{n(n-1)}.}
\]

The excess distribution has an atom at zero and a polynomial tail of exact degree \(n-1\). This formula is for the standard cross-polytope with vertices \(\pm e_i\) and edges of Euclidean length \(\sqrt2\); for a homothetic copy, squared distances and the excess scale by the square of the homothety factor, while stretch does not change.

## Assumptions and scope

Here the *intrinsic* metric means the infimum of Euclidean lengths of rectifiable curves constrained to the full boundary, **not** the ambient chord metric or the edge-skeleton graph distance. Dimension \(n\) is an arbitrary integer \(n\ge2\), the source is any fixed vertex by regular-polytope symmetry, and the target can be a vertex, a ridge point, or a point in any facet. The random variable \(P\) is sampled from surface area (not ambient-volume measure), and boundary faces of lower dimension have area zero.

## Proof

**1. A distance-preserving folding reduction.** Apply the coordinatewise absolute-value map

\[
F(x_1,x_2,\ldots,x_n)=(x_1,|x_2|,\ldots,|x_n|).
\]

The map sends \(S_n\) into the two-simplex complex \(\Sigma\subset S_n\) defined by \(x_2,\ldots,x_n\ge0\). It fixes \(v\), is Euclidean 1-Lipschitz, and cannot increase the length of any rectifiable path. Conversely, after mapping any target to \(F(p)\), applying the coordinate sign reflection taking \(F(p)\) back to \(p\) preserves lengths and fixes \(v\). Thus the minimum path length from \(v\) to \(p\) on the full surface equals that from \(v\) to \(F(p)\) within \(\Sigma\). This argument also covers points where one or more coordinates vanish.

**2. Two regular simplices unfold into a flat double cone.** The complex \(\Sigma\) consists precisely of \(\Delta_+=\operatorname{conv}(e_1,e_2,\ldots,e_n)\) and \(\Delta_-=\operatorname{conv}(-e_1,e_2,\ldots,e_n)\), joined along their common \((n-2)\)-simplex \(Q=\operatorname{conv}(e_2,\ldots,e_n)\). Develop the two \((n-1)\)-simplices isometrically into one \(\mathbb R^{n-1}\), with their interiors on opposite sides of the affine span of \(Q\). If \(c=(e_2+\cdots+e_n)/(n-1)\), both developed apices project orthogonally to \(c\), at signed heights \(h\) and \(-h\), where

\[
h^2=\|e_1-c\|_2^2=\frac n{n-1}.
\]

When \(p_1\ge0\), \(v\) and the folded target are in the same simplex, and the Euclidean chord is a boundary path, hence \(d_{S_n}(v,p)=\|v-p\|_2\).

When \(p_1=-t<0\), write \(t\in(0,1]\), and let \(u=\sum_{j=2}^n u_j e_j\in Q\) with \(u_j=|p_j|/(1-t)\) if \(t<1\), choosing arbitrary \(u\in Q\) when \(t=1\). The folded target is \(t(-e_1)+(1-t)u\). In the development its horizontal component is \(c+(1-t)(u-c)\), and its signed height is \(-th\). The straight segment from the developed \(v\) to this target crosses the equatorial hyperplane precisely at

\[
q=c+\frac{1-t}{1+t}(u-c)\in Q.
\]

Thus the straight segment lies in the developed union of the two simplices and gives a valid path. Every other path develops to a Euclidean curve joining the same endpoints, so its length cannot be smaller. The exact squared intrinsic distance is therefore

\[
d_{S_n}(v,p)^2=h^2(1+t)^2+(1-t)^2\|u-c\|_2^2.
\]

Because \(\|u-c\|_2^2=\|u\|_2^2-1/(n-1)\), while \(\|v-p\|_2^2=(1+t)^2+(1-t)^2\|u\|_2^2\), their difference simplifies to

\[
\frac{(1+t)^2-(1-t)^2}{n-1}=\frac{4t}{n-1}.
\]

This proves the pointwise formula, including \(p=-v\), and handles \(n=2\) since the equator simplex can be a single point.

**3. Sharp stretch.** For \(p_1=-t<0\), the proved formula gives

\[
\frac{d_{S_n}(v,p)^2}{\|v-p\|_2^2}=1+\frac{4t}{(n-1)\|v-p\|_2^2}.
\]

Since \(\|v-p\|_2^2\ge(1+t)^2\ge4t\), the squared ratio is at most \(n/(n-1)\). Equality in \((1+t)^2\ge4t\) requires \(t=1\), hence \(p=-v\), where the bound is attained. For \(p_1\ge0\), the ratio equals one.

**4. Exact area law and moment.** There are \(2^n\) congruent facets. Sampling one uniformly and then a uniform point on it makes the coordinate signs equiprobable and the nonnegative coordinate magnitudes Dirichlet\((1,\ldots,1)\). In particular \(|P_1|\) has beta law \(\mathrm{Beta}(1,n-1)\), giving \(\Pr(|P_1|>t)=(1-t)^{n-1}\) for \(0\le t\le1\). From the pointwise identity, \(Z=4(-P_1)_+/(n-1)\), so the atom and upper-tail law follow immediately. Moreover \(\mathbb E\|P\|_2^2=2/(n+1)\), \(\mathbb E P_1=0\), and \(\mathbb E(-P_1)_+=1/(2n)\). Taking expectations establishes the stated mean squared intrinsic distance.

## Verification

The independent reproducibility script `check_crosspolytope.py` checks the proposed equatorial crossing point and the exact path-length identity in rational arithmetic. In a seeded run it passed **4,002** configurations across dimensions **2 through 24**, including the equator, opposite vertex, uniform barycentric target and boundary targets; it also checked the exact mean-square identity in all 23 dimensions. An independent surface-area Monte Carlo check used **180,000** points and observed maximum absolute excess-tail error **0.00195556** at 16 specified thresholds. Maximum floating squared-distance discrepancy was **8.88e-16**. These are corroborative checks; the proof above establishes the assertion for all dimensions and surface points.

Reproduce with `python3 check_crosspolytope.py`, using only the Python standard library.

## Relationship to prior work

Miller and Pak (first arXiv version 2003-12-12) give the general higher-dimensional polyhedral source-unfolding and Voronoi framework, not the displayed pointwise cross-polytope identity or excess law. Demaine and O'Rourke describe the general geodesic/unfolding method for polyhedral surfaces. Saso, Schuerger and Shi (2024) obtain explicit shortest-path formulas for the regular **three-dimensional** octahedron between arbitrary pairs of surface points; their work subsumes the \(n=3\) distance specialization in principle. The novel scope considered here is the uniform \(n\)-dimensional identity, in particular \(n\ge4\), together with its sharp stretch and full area-uniform squared-excess law. A previously derived three-dimensional vertex-distance distribution and a separate regular-simplex dilation result are not claimed anew.

## Limitations

The statement is for a vertex source and the Euclidean regular cross-polytope. It gives neither all-pairs geodesics from arbitrary sources nor the full marginal distribution of \(d_{S_n}(v,P)\) in general dimension. The squared-excess distribution is a different observable from that full distance distribution. The novelty assessment is literature-based and not a guarantee that an earlier unindexed or differently phrased result does not exist. Independent scientific validation has not been carried out.

## References

1. E. Miller and I. Pak, *Metric combinatorics of convex polyhedra: Cut loci and nonoverlapping unfoldings*, arXiv:math/0312253, first posted 2003-12-12; https://arxiv.org/abs/math/0312253 . Full text: https://www.math.ucla.edu/~pak/papers/FoldLI.pdf .
2. E. D. Demaine and J. O'Rourke, *Geometric Folding Algorithms*, Chapter 24, *Shortest Paths and Geodesics*, Cambridge University Press, DOI 10.1017/CBO9780511735172.026, chapter online 2010-09-07; https://doi.org/10.1017/CBO9780511735172.026 .
3. E. Saso, H. Schuerger and X. Shi, *Landscapes of the Octahedron*, arXiv:2405.20344, first posted 2024-04-11; https://arxiv.org/abs/2405.20344 .
