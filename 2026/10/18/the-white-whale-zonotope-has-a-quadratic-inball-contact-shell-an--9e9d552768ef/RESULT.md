# The White Whale zonotope has a quadratic inball contact shell and a one-dimensional center locus

## Finding

For every integer \(d\geq2\), consider the **centered White Whale zonotope**
\[
 Z_d=\sum_{\substack{b\in\{0,1\}^d\\b\ne0}}[-b/2,b/2]\subset\mathbb R^d.
\]
This is a translation of the standard positive-primitive zonotope \(H^+_\infty(d,1)\). The following assertions hold simultaneously:

1. Its maximal Euclidean inscribed-ball radius and minimal enclosing-ball radius are, respectively,
\[
 r_d=\frac{2^{d-2}}{\sqrt2},\qquad R_d=2^{d-2}\sqrt d,\qquad \frac{R_d}{r_d}=\sqrt{2d}.
\]
2. Exactly \(d(d-1)\) **oriented facets** touch the origin-centered maximal Euclidean ball. Their outward unit normals are precisely
\[
 \pm\frac{e_i-e_j}{\sqrt2}\quad(1\le i<j\le d).
\]
Each such facet is, up to translation, a linearly embedded copy of the \((d-1)\)-dimensional White Whale zonotope, with its merged coordinate stretched by \(\sqrt2\) in the induced Euclidean metric.
3. The set of centers of **all** maximal-radius inscribed Euclidean balls is a nondegenerate closed segment in the diagonal line \(\mathbb R(1,\ldots,1)\). Its affine dimension is exactly one in every dimension \(d\ge2\).
4. The smallest enclosing Euclidean ball is centered at the origin, and its only contacts with \(Z_d\) are the antipodal vertices \(\pm2^{d-2}(1,\ldots,1)\).

These are parts of one metric-and-contact classification for the specified family; the sharp first-moment Khintchine inequality used in the proof is an established external theorem, not a new claim.

## Assumptions and scope

All statements use the standard Euclidean norm of \(\mathbb R^d\), the standard generator normalization \([-b/2,b/2]\), and integers \(d\ge2\). A facet is an exposed face of dimension \(d-1\); each opposite facet is counted separately. The inradius allows arbitrary centers, not merely the origin. The circumradius also allows arbitrary centers. The non-centered convention \(\sum_b[0,b]\) translates \(Z_d\) by \(2^{d-2}(1,\ldots,1)\), leaving radii and contact counts unchanged. The dimension-one case is excluded because its incenter is unique.

## Proof

**1. Support identity and the sharp inequality.** For \(u\in\mathbb R^d\), put \(m=\sum_{i=1}^d u_i\), let \(\varepsilon_i\) be independent uniform signs, and set \(X=\sum_{i=1}^d\varepsilon_i u_i\). The support function is
\[
 h_{Z_d}(u)=\frac12\sum_{b\in\{0,1\}^d}|u\cdot b|
             =2^{d-2}\,\mathbb E|m+X|.
\]
The omitted zero generator contributes nothing. As \(X\) and \(-X\) have the same distribution,
\[
 \mathbb E|m+X|=\mathbb E\frac{|m+X|+|m-X|}{2}
 =\mathbb E\max\{|m|,|X|\}\ge\mathbb E|X|.
\]
Szarek's sharp \(L^1\) Khintchine inequality, including its equality characterization, states
\[
 \mathbb E|X|\ge\frac{\|u\|_2}{\sqrt2},
\]
with equality for nonzero \(u\) exactly when \(u\) is proportional to \(\pm e_i\pm e_j\) for distinct indices and the two nonzero coefficients have equal absolute value. In the same-sign case \(m\ne0\), the preceding expectation strictly increases: then \(X=0\) with probability \(1/2\) and \(|m|>0\). The opposite-sign case has \(m=0\), yielding equality. Consequently,
\[
 h_{Z_d}(u)\ge r_d\|u\|_2,\qquad
 h_{Z_d}(u)=r_d\|u\|_2\ (u\ne0)
 \iff u\parallel e_i-e_j\quad(i\ne j).
\]
For a centrally symmetric convex body, the largest ball centered at zero has radius \(\min_{\|u\|=1}h(u)\). Furthermore, any inscribed radius-\(r\) ball centered at \(c\) has a reflected partner centered at \(-c\), and convexly averaging both proves the same ball of radius \(r\) is inscribed at zero. Thus the **global** inradius is \(r_d\).

**2. Facet contacts and their recursive shape.** Fix \(i\ne j\) and take \(u=e_i-e_j\). The generators parallel to the support face, equivalently the vectors \(b\) satisfying \(u\cdot b=0\), are exactly those with \(b_i=b_j\). They span the \((d-1)\)-dimensional hyperplane \(u^\perp\): among them are \(e_i+e_j\) and all \(e_k\) with \(k\notin\{i,j\}\). Hence the contact support face is a facet. Deleting coordinate \(j\) from each such binary generator gives a bijection onto the \(2^{d-1}-1\) nonzero binary generators in dimension \(d-1\). Reinstating that coordinate equal to coordinate \(i\) gives an injective linear map, with the merged coordinate having Euclidean stretch \(\sqrt2\). The facet is therefore a translate of the indicated embedded smaller zonotope. Conversely, Step 1 rules out every other support normal as a maximal-ball contact normal. There are \(2\binom d2=d(d-1)\) such oriented facets.

**3. All maximum-ball centers.** If \(B_2^d(c,r_d)\subseteq Z_d\), each contacting normal \(\pm(e_i-e_j)/\sqrt2\) forces \(c_i=c_j\), hence \(c=t\mathbf1\) for some real \(t\), where \(\mathbf1=(1,\ldots,1)\). To see that a nonzero \(t\) is feasible, note that a full-dimensional polytope has finitely many facets. Every facet not listed in Step 2 has distance **strictly greater than \(r_d\)** from zero, by the complete support equality characterization. Taking \(|t|\) sufficiently small leaves each of these finitely many facet inequalities valid for the translated ball; the contacting facets remain valid because their normals sum to zero. Thus centers include a nontrivial interval on the diagonal and none outside that line. Convexity and compactness of the set of feasible centers, together with central symmetry, make it exactly a closed nondegenerate symmetric line segment. No closed formula for its endpoints is asserted.

**4. Enclosing sphere and antipodal equality.** In the centered generator description, coordinate \(i\) has absolute value at most half the number of nonzero binary generators whose \(i\)-th coordinate is one, namely \(2^{d-2}\). Thus
\[
 Z_d\subseteq[-2^{d-2},2^{d-2}]^d
 \subseteq B_2^d(0,2^{d-2}\sqrt d).
\]
The all-positive and all-negative choices of every segment endpoint are the vertices \(\pm2^{d-2}\mathbf1\), so this radius is attained. Any enclosing ball must contain both antipodes and has radius at least half their separation, which also forces its center to be zero at equality. Any point on the circum-sphere must attain the absolute coordinate bound in every coordinate. Mixed signs are impossible because the binary generator \(e_i+e_j\), present for every distinct \(i,j\), would be required to take both coefficient endpoints simultaneously. Thus only those two vertices touch. This proves the final assertion and the ratio in Step 1.

## Verification

The accompanying self-contained `checker.py` independently enumerates potential facet normals from independent binary generator subsets in dimensions \(2\) through \(5\). Exact integer support comparisons identify \(2,6,12,20\) contacting oriented facets, respectively, and show positive slack in all remaining facets. It tests the recursive facet-generator identification and positive diagonal-center perturbation thresholds. A separate sampled-direction stress test evaluates \(4,000\) random unit normals per dimension in dimensions \(2\) through \(10\), without discovering a violated support inequality. Run with Python 3 and NumPy: `python checker.py`. Finite experiments are **not** the proof of the all-dimensional theorem, which is given above.

## Relationship to prior work

The White Whale is the all-nonzero-binary-generator positive primitive zonotope introduced in the primitive-zonotope literature. Deza, Manoussakis and Onn developed its polyhedral/combinatorial context, and Deza, Hao and Pournin determined large-dimensional vertex and edge information. Their inspected full texts concern combinatorial enumeration, graph diameter, and optimization properties, not the complete metric contact structure proved here. Szarek's sharp Khintchine constant and equality characterization are classical and are essential **prior results**, explicitly credited rather than presented as new. De, Diakonikolas and Servedio provide a directly inspectable formulation and proof of this sharp inequality. The geometric content here is the support-function reduction for this zonotope together with its complete nearest-facet set, recursive contact faces, and one-dimensional locus of optimal inball centers. A prior equivalent geometric specialization under alternate terminology is possible.

## Limitations

This classification addresses Euclidean balls and the indicated exact centered normalization, not all ellipsoid metrics or arbitrary weighted generators. It determines the optimal-center locus's affine dimension and direction, but does not give a dimension-uniform closed formula for its endpoints. Literature coverage cannot exclude unindexed historical geometric formulations. No independent mathematical audit has been performed; the numerical tests provide finite consistency checks only.

## References

1. A. Deza, M. Hao and L. Pournin, *Sizing the White Whale*, arXiv:2205.13309v1, first publicly submitted 2022-05-26, https://arxiv.org/html/2205.13309v1.
2. A. Deza, G. Manoussakis and S. Onn, *Primitive Zonotopes*, arXiv:1512.08018, first publicly submitted 2015-12-25, https://arxiv.org/html/1512.08018v4.
3. S. Szarek, *On the best constants in the Khintchine inequality*, Studia Mathematica 58 (1976), 197–208, https://doi.org/10.4064/sm-58-2-197-208.
4. A. De, I. Diakonikolas and R. A. Servedio, *A robust Khintchine inequality, and algorithms for computing optimal constants in Fourier analysis and high-dimensional geometry*, arXiv:1207.2229v2, Theorem 7 and Section 3.1, https://arxiv.org/html/1207.2229v2.
