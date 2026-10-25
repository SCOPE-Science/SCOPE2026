# Exact two-rainbow pushability and optimizer rigidity for affine-regular hexagons

## Finding

Let \(P\) be any centered affine-regular hexagon in \(\mathbb R^2\): specifically, \(P=T(H)\) for an invertible linear map \(T\), where \(H\) is a regular hexagon centered at the origin. For independent random vertices \(V\) and \(W\) of \(P\), suppose that \(\mathbb E V+\mathbb E W=0\). The probability that \(V\) and \(W\) belong to one common edge of \(P\) is at most \(2/3\), and this bound is attained. In the notation of Martínez-Sandoval and Olvera-Sampieri,

\[
\boxed{\pi_2(P)=\frac23.}
\]

Furthermore, the *only* maximizing ordered pairs of vertex distributions are the uniform laws on the two complementary triples of alternating hexagon vertices, taken in either order.

The proof gives a quantitative exact deficit identity, not merely an upper bound. Label the vertices of the canonical affine-regular hexagon, cyclically, by

\[
(z_0,z_1,z_2,z_3,z_4,z_5)=
((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)).
\]

Let \(p_j=\Pr(V=z_j)\), \(q_j=\Pr(W=z_j)\), \(X=\sum_{j=0}^5 p_j(z_j)_1\), \(Y=\sum_{j=0}^5 p_j(z_j)_2\), and \(a=\sum_{j=0}^5(-1)^jp_j\), \(b=\sum_{j=0}^5(-1)^jq_j\). Under collective balancing \(\sum_j(p_j+q_j)z_j=0\), the success probability \(S\) satisfies

\[
\boxed{\frac23-S=\frac{X^2+3Y^2+1+ab}{6}.}
\]

In particular, this expresses the whole gap as the sum of two squares and a nonnegative parity-coupling term. The formula transfers to every centered affine-regular hexagon by pulling the probability distributions back along \(T\).

## Assumptions and scope

There are exactly two **independent** vertex-valued random variables. Each law may have arbitrary nonnegative weights summing to one; neither law is required to be individually centered. Only their expectations together must sum to the origin. The affine-regularity assumption is essential to the specific proof and is not claimed for arbitrary centrally symmetric hexagons. Facets of a genuine two-dimensional hexagon are its six edges, and a pair of vertices lies in one edge exactly when the two cyclic labels coincide or differ by one modulo six.

The family \(P=T(H)\) uses invertible *linear*, not arbitrary translated affine, maps, so the distinguished balancing origin is preserved. Equivalently the origin is the center of the affine-regular hexagon. The conclusion concerns \(r=2\) and does not assert a formula for higher rainbow numbers.

## Proof

It suffices to consider the displayed integer-coordinate affine-regular hexagon, because invertible linear transformations preserve vertices, facets, independence, the event of occupying a common facet, and the vanishing of the sum of expectations.

Write \(z_j=(x_j,y_j)\) with

\[
(x_0,\ldots,x_5)=(2,1,-1,-2,-1,1),\qquad
(y_0,\ldots,y_5)=(0,1,1,0,-1,-1).
\]

For \(j,k\in\{0,\ldots,5\}\), set \(A_{jk}=1\) when \(j-k\equiv0,1,-1\pmod6\), and \(A_{jk}=0\) otherwise. The following is an *exact pointwise identity* on all 36 ordered pairs:

\[
6A_{jk}=3+x_jx_k+3y_jy_k-(-1)^{j+k}. \tag{1}
\]

Indeed, \(x_jx_k+3y_jy_k=4\cos(\pi(j-k)/3)\). For cyclic differences \(0,\pm1,\pm2,3\), these products equal \(4,2,-2,-4\), respectively, while \((-1)^{j+k}=(-1)^{j-k}\). The right side of (1) therefore equals \(6,6,0,0\), exactly as the left side does.

Because \(V,W\) are independent, their success probability is \(S=\sum_{j,k}p_jq_kA_{jk}\). Multiplying (1) by \(p_jq_k\), summing, and using \(\sum_jp_j=\sum_kq_k=1\) gives

\[
6S=3+X_pX_q+3Y_pY_q-ab,
\]

where \((X_p,Y_p)=\sum_jp_jz_j\) and \((X_q,Y_q)=\sum_kq_kz_k\). Collective balancing implies \(X_q=-X_p\) and \(Y_q=-Y_p\). Thus

\[
6S=3-X^2-3Y^2-ab
\]

and the boxed deficit identity follows.

Since \(p,q\) are probability weights, their alternating-sign expectations obey \(-1\le a,b\le1\), so \(1+ab\ge0\). Hence \(S\le2/3\). Equality requires \(X=Y=0\) and \(ab=-1\). The last condition forces either \((a,b)=(1,-1)\) or \((a,b)=(-1,1)\). In the first case \(p\) is supported entirely on \(\{z_0,z_2,z_4\}\), while \(q\) is supported on \(\{z_1,z_3,z_5\}\); the other case exchanges them.

For the even triple, the equations \(\sum_jp_j=1\), \(X=0\), \(Y=0\) become

\[
p_0+p_2+p_4=1,\qquad2p_0-p_2-p_4=0,\qquad p_2-p_4=0.
\]

They have the unique solution \(p_0=p_2=p_4=1/3\). By the same calculation the odd triple has unique centered law \(q_1=q_3=q_5=1/3\). These measures satisfy collective balancing, and six of their nine ordered pairs are adjacent, hence \(S=6/9=2/3\). The swapped pair also attains equality. This proves both sharpness and complete optimizer rigidity.

## Verification

The self-contained standard-library script `verify.py` checks the 36 integer identities in (1) with exact arithmetic, the two explicit maximizing distributions and their exact success probability, and the nonzero normalization-plus-centroid determinants on both alternating triples. Run it using `python3 verify.py` from the extracted package directory. The checks have been executed successfully.

The script does **not** enumerate all possible real probability laws. Their universal upper bound and equality classification follow instead from the exact algebraic identity (1), the balancing equations, nonnegativity, and the stated full-rank three-variable systems.

## Relationship to prior work

Martínez-Sandoval and Olvera-Sampieri (arXiv:2610.17157v1, October 12, 2026) introduce rainbow pushability in Section 3, prove a general facet-depth inequality in Section 4.1, compute the cube in Section 4.2, and explicitly ask for exact values for additional centered polytopes in Section 7. Their general centrally symmetric facet bound for the six-edge hexagon is only \(\pi_2\le\min\{1,6/2^2\}=1\), which does not imply the sharp \(2/3\). The cube calculation concerns parallelotopes, not an affine-regular hexagon with six extreme points. No exact hexagonal value or unique pair of alternating-triangle maximizers appears in the inspected relevant full-text sections.

The new result is the nontrivial six-vertex planar case: both the strict bound below one and the equality classification rest on the alternating-parity term in (1). Combining \(\pi_2(P)<1\) with the cited pushed colorful Carathéodory theorem gives a two-color interior-penetration conclusion for this specific polygon, even though that general implication itself is previously known.

## Limitations

No formula is claimed for arbitrary centrally symmetric hexagons, regular polygons with other numbers of vertices, or three or more vertex-valued variables. The coefficient \(2/3\) requires independent variables, two collectively balanced probability laws, and the six-vertex affine-regular incidence pattern. The argument is an exact finite-kernel identity and a proof for an infinite continuum of probability measures; computational checks only replay the finite algebra. Novelty is assessed against accessible publications and mathematical records, so unindexed equivalent earlier calculations cannot be excluded. No independent mathematical audit has been performed.

## References

1. L. Martínez-Sandoval and A. Olvera-Sampieri, *Pushed Colorful Polytopal KKMS Theorem and Orthogonal Star Transversals*, arXiv:2610.17157v1, first submitted October 12, 2026. https://arxiv.org/html/2610.17157v1 (especially Sections 3.1, 4.1–4.2, and 7).
