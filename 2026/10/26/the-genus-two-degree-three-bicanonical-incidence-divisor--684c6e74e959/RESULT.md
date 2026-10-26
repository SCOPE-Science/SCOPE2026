# The genus-two degree-three bicanonical incidence divisor

## Finding

Let \(C\) be a smooth projective curve of genus \(2\) over an algebraically closed field of characteristic zero, and let \(K_C\) be its canonical line bundle. Define
\[
Q_3(C)=\{D\in\operatorname{Sym}^3(C):D\leq\operatorname{div}(q)\text{ for some }0\ne q\in H^0(C,K_C^{\otimes2})\}.
\]
Then \(Q_3(C)\) is a smooth divisor in \(\operatorname{Sym}^3(C)\), isomorphic to \(C\times\mathbf P^1\). If \(p_C:C\times\mathbf P^1\to C\) is the projection, its normal bundle is
\[
N_{Q_3(C)/\operatorname{Sym}^3(C)}\cong p_C^*K_C.
\]
In particular, the normal line bundle has degree \(2\) on each curve \(C\times\{t\}\) and degree \(0\) on each fiber \(\{P\}\times\mathbf P^1\).

## Assumptions and scope

The curve is smooth, projective, and of genus exactly \(2\); the ground field is algebraically closed of characteristic zero. The divisor inequality means coefficientwise effectiveness. The claim concerns the locus of degree-three effective divisors on the base curve, not the Brill–Noether locus in the Picard variety of a spectral double cover. No statement is made for singular curves, positive characteristic, higher genus, or higher divisor degree.

The motivation is the use of quadratic-differential-special divisors in the study of rank-two wobbly bundles. The initial public version of Dinh's work on that topic assumed genus at least three, leaving this low-genus incidence geometry outside its stated scope.

## Proof

Let \(h:C\to\mathbf P^1\) be the canonical hyperelliptic double cover, and write \(F_t=h^*(t)\) for its degree-two fiber over \(t\in\mathbf P^1\), with multiplicities retained at branch points. For genus two, \(K_C\cong h^*\mathcal O_{\mathbf P^1}(1)\). Consequently every divisor in \(|2K_C|\) has the form \(F_s+F_t\), allowing \(s=t\).

Every effective degree-three sub-divisor of \(F_s+F_t\) contains one full degree-two fiber and one residual point. This remains true when \(s=t\) or one of the fibers is ramified, because the fiber multiplicities are then doubled in \(2F_s\). Thus every \(D\in Q_3(C)\) can be written as \(D=P+F_t\). Conversely, for any \(P\in C\) and \(t\in\mathbf P^1\),
\[
P+F_t\leq F_{h(P)}+F_t=\operatorname{div}(q)
\]
for a suitable nonzero \(q\in H^0(C,K_C^{\otimes2})\). Hence the underlying set of \(Q_3(C)\) is exactly the family \(\{P+F_t\}\).

Consider the Abel–Jacobi morphism
\[
\alpha_3:\operatorname{Sym}^3(C)\longrightarrow\operatorname{Pic}^3(C),\qquad D\longmapsto\mathcal O_C(D).
\]
For every line bundle \(L\) of degree three, Riemann–Roch gives \(h^0(C,L)=2\) and \(h^1(C,L)=0\). Therefore \(\alpha_3\) is a \(\mathbf P^1\)-bundle. Set
\[
T=\{K_C(P):P\in C\}\subset\operatorname{Pic}^3(C).
\]
The map \(P\mapsto K_C(P)\) is a translate of the Abel embedding, so \(T\) is a smooth curve isomorphic to \(C\). Moreover, the complete linear system \(|K_C(P)|\) is precisely \(P+|K_C|\): multiplication by the canonical section of \(\mathcal O_C(P)\) gives an isomorphism \(H^0(C,K_C)\to H^0(C,K_C(P))\), since both spaces have dimension two. It follows that
\[
Q_3(C)=\alpha_3^{-1}(T).
\]
This identifies \(Q_3(C)\) with a \(\mathbf P^1\)-bundle over \(C\). The same multiplication maps vary algebraically with \(P\) and trivialize the rank-two bundle of sections along \(T\); projectivizing gives \(Q_3(C)\cong C\times\mathbf P^1\). In particular, the locus is smooth and has codimension one in the smooth threefold \(\operatorname{Sym}^3(C)\).

For the normal bundle, the equality \(Q_3(C)=\alpha_3^{-1}(T)\) and smoothness of the projective-bundle morphism give
\[
N_{Q_3(C)/\operatorname{Sym}^3(C)}\cong\alpha_3|_{Q_3(C)}^*N_{T/\operatorname{Pic}^3(C)}.
\]
The variety \(\operatorname{Pic}^3(C)\) is a translate of the Jacobian, hence an abelian surface with trivial canonical bundle. Adjunction for the smooth curve \(T\) therefore gives \(N_{T/\operatorname{Pic}^3(C)}\cong K_T\). Under \(T\cong C\), this is \(K_C\), and the displayed normal bundle is \(p_C^*K_C\), as claimed.

## Verification

The proof uses only the genus-two canonical double cover, the Riemann–Roch theorem, the Abel–Jacobi projective-bundle description in degree three, and adjunction on an abelian surface. The degree-three condition is essential to the stated incidence locus. The result does not assert that a corresponding locus on the spectral curve is itself a product, nor does it determine singularities of the associated wobbly divisor in a moduli space.

## Relationship to prior work

Dinh's initial public version introduces quadratic-differential-special divisors in the rank-two wobbly-bundle setting and assumes genus at least three. Its later revision treats genus two as well and gives a general criterion for wobbliness, but the exact smooth product model and normal bundle of \(Q_3(C)\subset\operatorname{Sym}^3(C)\) are not stated there. Pal and Pauly classify components of the wobbly divisor in the moduli space of rank-two bundles; that is a different ambient space and does not identify this base-curve incidence divisor. published-finding corpus searches returned related normalization results for wobbly divisors and hyperelliptic branch constructions, but none compares the same locus or its normal bundle.

The proof is a genus-two geometric refinement of the quadratic-differential incidence condition, not a new classification of wobbly bundles. A residual priority risk remains because the calculation is short and may be implicit in standard treatments of symmetric products and hyperelliptic curves.

## Limitations

The claim is confined to smooth genus-two curves in characteristic zero. It is an explicit description of the divisor incidence locus only. It does not by itself imply a normality or singularity statement for any image in a moduli space of bundles, and it does not resolve any higher-genus case.

## References

[1] D. Dinh, “Rank-2 wobbly bundles from special divisors on spectral curves,” arXiv:2406.04224v1, first public 2024-06-06, especially the introduction and definition of quadratic-differential-special divisors.

[2] D. Dinh, “Rank-2 wobbly bundles from special divisors on spectral curves,” arXiv:2406.04224v3, revised 2025-11-24, especially Theorem 1.2 and Section 4; consulted for later coverage and overlap only.

[3] S. Pal and C. Pauly, “The wobbly divisors of the moduli space of rank-2 vector bundles,” Advances in Geometry 21 (2021), 473–482; arXiv:1803.11315. This concerns components in the bundle moduli space, rather than the incidence locus defined here.
