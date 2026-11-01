# Sharp squared-distance dispersion and stability for uniform points in Euclidean simplices

## Finding
Let \(S\subset\mathbb R^d\) be any nondegenerate Euclidean simplex, \(d\ge2\), and let \(X,Y\) be independent volume-uniform random points of \(S\). The dimensionless squared-distance dispersion, equivalently the normalized fourth distance moment,
\[
Q(S)=\frac{\mathbb E\|X-Y\|^4}{(\mathbb E\|X-Y\|^2)^2}
=1+\frac{\operatorname{Var}(\|X-Y\|^2)}{(\mathbb E\|X-Y\|^2)^2},
\]
has the following **sharp complete range**:
\[
\boxed{\frac{(d+1)(d+2)(d+7)}{d(d+3)(d+4)}\ \le\ Q(S)\ <\ \frac{6(d+1)^3}{d(d+3)(d+4)}.}
\]
The lower equality holds if and only if \(S\) is regular (up to similarity). The strict upper bound is the supremum, approached by nondegenerate simplices degenerating to one separated vertex and \(d\) coincident vertices. Every intermediate value occurs for a nondegenerate simplex. For \(d=2\), the interval is \([9/5,27/10)\); for \(d=3\), it is \([100/63,64/21)\).

There is an **exact shape-stability identity**. Write \(n=d+1\), let the vertices be \(v_1,\ldots,v_n\), set \(\bar v=n^{-1}\sum_i v_i\), \(w_i=v_i-\bar v\), \(C=\sum_iw_iw_i^{\mathsf T}\), \(T=\operatorname{tr}C>0\), and \(c=n(n+1)/[(n+2)(n+3)]\). Then
\[
\boxed{Q(S)-\frac{(d+1)(d+2)(d+7)}{d(d+3)(d+4)}
=\frac{1+c}{T^2}\left\|C-\frac Td I_d\right\|_F^2
+\frac{3c}{T^2}\sum_{i=1}^n\left(\|w_i\|^2-\frac Tn\right)^2.}
\]
The remainder is a quantitative combination of covariance anisotropy and unequal squared vertex radii.

## Assumptions and scope
All simplices have \(d+1\) affinely independent vertices in Euclidean dimension \(d\ge2\). Uniform means normalized \(d\)-dimensional Lebesgue measure on the simplex interior, not surface or vertex sampling. The two samples are independent. The estimate is similarity-invariant; no volume, diameter, or conditioning restriction is needed. The upper endpoint belongs only to the closure of the nondegenerate family and is never attained by a positive-volume simplex. All displayed expectations are finite.

## Proof
**1. Dirichlet moments.** Center the simplex at its vertex centroid, so \(\sum_iw_i=0\), and write \(Z=X-\bar v=\sum_i P_iw_i\), where \((P_1,\ldots,P_n)\) has the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. For any real scalars \(a_i\), the integer moment formula is \(\mathbb E(\sum_iP_ia_i)^k=k!h_k(a_1,\ldots,a_n)/(n)_k\), where \(h_k\) is the complete homogeneous symmetric polynomial. Since \(\sum_i a_i=0\) for \(a_i=\langle u,w_i\rangle\), Newton's identities give \(2!h_2=\sum_i a_i^2\) and \(4!h_4=3(\sum_i a_i^2)^2+6\sum_i a_i^4\). Polarizing and contracting therefore yields, with \(H=\operatorname{tr}(C^2)\) and \(W=\sum_i\|w_i\|^4\),
\[
\mathbb E\|Z\|^2=\frac{T}{n(n+1)},\qquad
\mathbb E\|Z\|^4=\frac{T^2+2H+6W}{n(n+1)(n+2)(n+3)},\qquad
\operatorname{Cov}(Z)=\frac{C}{n(n+1)}.
\]
For independent centered copies \(Z,Z'\), direct expansion and independence give
\[
\mathbb E\|Z-Z'\|^2=2\mathbb E\|Z\|^2,\qquad
\mathbb E\|Z-Z'\|^4=2\mathbb E\|Z\|^4+2(\mathbb E\|Z\|^2)^2+4\operatorname{tr}(\operatorname{Cov}(Z)^2).
\]
Consequently,
\[
\boxed{Q(S)=\frac{1+c}{2}+(1+c)\frac{H}{T^2}+3c\frac{W}{T^2}.}\tag{1}
\]

**2. Lower bound and rigidity.** The \(d\) positive eigenvalues of \(C\) imply \(H\ge T^2/d\), with equality only at \(C=(T/d)I_d\). Cauchy--Schwarz also gives \(W\ge T^2/n\), with equality only when all vertex radii are equal. Substitution into (1) simplifies to the claimed lower constant. Subtracting the lower value gives precisely the displayed sum of squares, because
\(H-T^2/d=\|C-(T/d)I_d\|_F^2\) and \(W-T^2/n=\sum_i(\|w_i\|^2-T/n)^2\).
To establish equality rigidity, let \(A\) be the \(d\times n\) matrix with columns \(w_i\). If \(C=AA^{\mathsf T}=\lambda I_d\), \(\lambda>0\), then \(A\mathbf 1=0\) and \(\operatorname{rank}A=d\) force \(A^{\mathsf T}A=\lambda(I_n-\mathbf1\mathbf1^{\mathsf T}/n)\), so all squared edge lengths equal \(2\lambda\). Conversely the centered vertices of a regular simplex have this Gram matrix, giving lower equality.

**3. Scalar zero-sum quartic lemma.** For any \(n\ge3\) real numbers \(a_i\) with \(\sum_i a_i=0\),
\[
\sum_i a_i^4\le k_n\Big(\sum_i a_i^2\Big)^2,
\qquad k_n=\frac{n^2-3n+3}{n(n-1)}.
\tag{2}
\]
For \(n=3\), \(\sum_i a_i^4=(\sum_i a_i^2)^2/2\), so equality is universal. For \(n\ge4\), normalize \(\sum_i a_i^2=1\) and maximize on the compact sphere in the zero-sum hyperplane. Lagrange multipliers show every coordinate is a root of a single cubic \(4z^3-2\lambda z-\mu=0\); thus there are at most three distinct coordinate values. If there were three values \(a<b<c\), their sum would be zero by Vieta's identity. Replace one coordinate of each value by any nearby triple with the same sum zero and same sum of squares. Its fourth-power sum is fixed, because every zero-sum real triple satisfies \(\sum z_i^4=(\sum z_i^2)^2/2\). The resulting vector remains maximizing, but a generic such perturbation yields three altered values all distinct from an untouched coordinate, hence four distinct values, contradicting the cubic condition. Thus a maximizer has exactly two values, occurring \(j\) and \(n-j\) times. Their normalized fourth-power sum is \(n/[j(n-j)]-3/n\), maximized at \(j=1\) or \(j=n-1\), giving (2). This proves the lemma without reliance on finite enumeration.

**4. Upper bound.** Choose orthonormal Euclidean coordinates and put \(a_i^{(r)}=w_i^{(r)}\). Each \((a_i^{(r)})_i\) has zero sum. By (2) and Cauchy--Schwarz, for any coordinate indices \(r,s\),
\[
\sum_i(a_i^{(r)})^2(a_i^{(s)})^2
\le \sqrt{\sum_i(a_i^{(r)})^4\sum_i(a_i^{(s)})^4}
\le k_n\Big(\sum_i(a_i^{(r)})^2\Big)\Big(\sum_i(a_i^{(s)})^2\Big).
\]
Summing over \(r,s\) gives \(W\le k_nT^2\). Also \(H<T^2\), strictly because \(C\) has rank \(d\ge2\). Formula (1) gives
\[
Q(S)<\frac32(1+c)+3ck_n=\frac{6(d+1)^3}{d(d+3)(d+4)}.
\]

**5. Sharpness and full interval.** Fix \(0<\varepsilon<1\) and take vertices \(e_1,\varepsilon e_1,\varepsilon e_2,\ldots,\varepsilon e_d\) in \(\mathbb R^d\). They are affinely independent. As \(\varepsilon\downarrow0\), their centered Gram matrix tends to a rank-one Gram matrix whose underlying zero-sum coordinate has one exceptional value and \(d\) equal values. Both \(H/T^2\to1\) and \(W/T^2\to k_n\), giving the sharp upper supremum. For the full image, start from a regular simplex and apply to its direction space the linear maps that act by identity on the line through one vertex and its centroid and by \(\varepsilon I\) on the perpendicular subspace. At \(\varepsilon=1\) the lower endpoint holds; as \(\varepsilon\downarrow0\) the same one-versus-\(d\) rank-one limit holds. Continuity of (1) and the intermediate value theorem imply every value below the upper endpoint is attained.

## Verification
Run the complete standalone standard-library checker with `python3 verify_simplex_kurtosis.py`. It independently integrates all fourth-degree barycentric monomials, verifies (1) against exact rational direct integration for integer-coordinate examples in dimensions two, three, and four, checks the nonnegative decomposition, and tests the scalar lemma on a finite integer grid. The checker reported **90,001 exact rational diagnostics passed**. Symmetric rational algebra separately reduces the constants in (1) to the two displayed dimension-dependent endpoints. These finite computations are diagnostics only; Steps 1--5 are the universal proof.

## Relationship to prior work
Sinan Wang's work [1] studies normalized distributions of pairwise distances in general convex bodies, particularly Brunn--Minkowski inequalities and Wulff variations; its main theorems do not compare normalized fourth moments across arbitrary simplex shapes. Bäsel [2] gives second and fourth distance moments for regular polygons, including the equilateral triangle, but not the sharp shape interval over all simplices in all dimensions. Pure--Durrani--Tong--Pan [3] give a general planar polygon distance-density computation; an individual triangle's moments can in principle be recovered, but their formulas do not imply the all-dimensional extremality and stability theorem. Standard Dirichlet integration and zero-sum \(\ell_4\) extremal estimates are acknowledged tools, not separate novelty claims. The new claim is their exact geometric synthesis into a sharp full-dimensional shape optimization and a quantitative rigidity identity.

## Limitations
This is a self-review, **not independent verification or a certified publication priority claim**. The theorem applies only to volume-uniform points in nondegenerate Euclidean simplices of dimension at least two, not arbitrary convex bodies or boundary samples. The strict upper value cannot be realized by a nondegenerate simplex. The dimension-specific values for regular polygons are partially known; older uncatalogued shape inequalities and specialized higher-dimensional moment computations remain a historical-priority risk. The exact checker is finite and does not replace the proof.

## References
1. Sinan Wang, *A Brunn--Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916, first public version 2026-10-01. https://arxiv.org/abs/2610.01916
2. Uwe Bäsel, *The moments of the distance between two random points in a regular polygon*, arXiv:2101.03815, 2021, especially Section 9. https://arxiv.org/abs/2101.03815
3. Ross Pure, Salman Durrani, Fei Tong, Jianping Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757, 2019, Theorem 3 and Proposition 1. https://arxiv.org/abs/1903.07757
4. Joseph Anderson, Navin Goyal, Luis Rademacher, *Efficient learning of simplices*, arXiv:1211.2227, 2012. https://arxiv.org/abs/1211.2227
5. Anastas Baci, Zakhar Kabluchko, Joscha Prochno, Mathias Sonnleitner, Christoph Thäle, *Limit theorems for random points in a simplex*, arXiv:2005.04911, 2020. https://arxiv.org/abs/2005.04911
