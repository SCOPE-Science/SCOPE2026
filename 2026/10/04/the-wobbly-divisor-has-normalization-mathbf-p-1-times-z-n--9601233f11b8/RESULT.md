# The wobbly divisor has normalization \(\mathbf P^1\times Z_n\)
## Finding
Let \(X\subset \mathbf P^{n+2}_\mathbf C\), \(n\ge 3\), be a smooth intersection of two diagonal quadrics with pairwise distinct parameters \(\lambda_0,\ldots,\lambda_{n+2}\), in the notation of Bhattacharya--Matsubara. Let \(W\subset X\) be their reduced wobbly divisor, and let \(Z_n\subset\mathbf P^{n+2}\) be the smooth complete intersection of the four diagonal quadrics
\[
\sum_j \lambda_j^k x_j^2=0,\qquad k=0,1,2,3.
\]
For the morphism
\[
\nu_n:\mathbf P^1\times Z_n\longrightarrow W,\qquad
([a:b],[x_j])\longmapsto[(b\lambda_j-a)x_j],
\]
constructed in the source, \(\nu_n\) is the normalization morphism.

In particular \(W\) is non-normal for every \(n\ge3\). Since \(W\) is a reduced Cartier divisor in the smooth variety \(X\), it is \(S_2\); hence non-normality forces failure of \(R_1\), so the singular locus of \(W\) has a codimension-one component.

For \(n=3\), \(Z_3\) is a smooth complete-intersection curve of type \((2,2,2,2)\) in \(\mathbf P^5\), of degree \(16\) and genus \(17\). Thus the degree-\(32\) genus-two wobbly surface has normalization \(\mathbf P^1\times Z_3\).

## Assumptions and scope
The base field is \(\mathbf C\). The parameters \(\lambda_j\) are pairwise distinct, and \(X\) is the smooth complete intersection used in arXiv:2609.31421. The statement concerns the reduced divisor \(W\) and the explicit \(Z_n\) and \(\nu_n\) defined there. It makes no claim that the codimension-one singular locus is irreducible, reduced, or equal to any particular named stratum.

## Proof
Bhattacharya--Matsubara prove that \(Z_n\) is smooth and irreducible for \(n\ge3\), that \(\nu_n\) is projective and surjective onto \(W\), and that
\[
P_{\nu_n([a:b],x)}^{[n]}(Z,T)
=(bZ-aT)^2P_x^{[n-2]}(Z,T).
\]
Thus \(\mathbf P^1\times Z_n\) is normal, and every point of a fiber of \(\nu_n\) determines a multiple root \([a:b]\) of the nonzero binary form \(P_w^{[n]}\).

Fix \(w\in W\). There are only finitely many possible multiple roots \([a:b]\). For a fixed one, if \(b\lambda_j-a\ne0\) for all \(j\), the coordinates of \(x\) are uniquely determined projectively by \(w_j=(b\lambda_j-a)x_j\). If \(b\lambda_m-a=0\), pairwise distinctness of the \(\lambda_j\) makes \(m\) unique. The remaining coordinates are again fixed projectively, and the equation \(\sum_jx_j^2=0\) determines \(x_m^2\), leaving at most two choices for \(x_m\). Hence every fiber is finite. Because \(\nu_n\) is projective, it is finite.

The required degree-one locus is nonempty. Write
\[
q(z)=\prod_j(z-\lambda_j),\qquad
p_x(z)=\sum_jx_j^2\frac{q(z)}{z-\lambda_j}.
\]
The four equations defining \(Z_n\) are exactly the vanishing of the top four coefficients of \(p_x\), so \(p_x\) has degree at most \(n-2\). Conversely, for every polynomial \(R\) of degree at most \(n-2\), Lagrange interpolation gives
\[
y_j=\frac{R(\lambda_j)}{q'(\lambda_j)}
\]
(up to the harmless common normalization in the definition of \(p_x\)); these \(y_j\) satisfy the four moment equations, and choosing \(x_j^2=y_j\) produces \(x\in Z_n\) with \(p_x=R\) up to a nonzero scalar. Choose \(R\) squarefree and choose \([a:b]\) so that its root is distinct from the roots of \(R\) and from all \(\lambda_j\). Then
\[
P_{\nu_n([a:b],x)}^{[n]}=(bZ-aT)^2R
\]
has exactly one double root. Thus this condition defines a nonempty open subset, hence a dense open subset because \(W\) is irreducible.

On that dense open subset, the factorization determines \([a:b]\) uniquely and then determines \(x\) uniquely. Hence \(\nu_n\) is generically one-to-one. In characteristic zero, a finite dominant generically one-to-one morphism between irreducible varieties is birational. Therefore the finite birational morphism from the normal variety \(\mathbf P^1\times Z_n\) is the normalization of \(W\).

It remains to show that this normalization is not an isomorphism. Fix \(m\). Put \(y_j=x_j^2\). The equations of \(Z_n\) become the four linear moment equations
\[
\sum_j\lambda_j^k y_j=0,\qquad 0\le k\le3.
\]
There exists a kernel vector with \(y_m\ne0\): otherwise the coordinate functional \(y\mapsto y_m\) would lie in the row span of the four Vandermonde rows, so a polynomial of degree at most \(3\) would be \(1\) at \(\lambda_m\) and \(0\) at all \(n+2\ge5\) other distinct \(\lambda_j\), which is impossible. Choose square roots \(x_j\). The equation with \(k=0\) ensures that some \(x_j\) with \(j\ne m\) is nonzero. Replacing \(x_m\) by \(-x_m\) gives a projectively distinct point \(x'\in Z_n\), but at \([a:b]=[\lambda_m:1]\) the \(m\)-th output coordinate of \(\nu_n\) vanishes, so
\[
\nu_n([\lambda_m:1],x)=\nu_n([\lambda_m:1],x').
\]
Thus \(\nu_n\) is not injective and \(W\) is not normal.

Finally, for \(n=3\), \(Z_3\subset\mathbf P^5\) is a smooth \((2,2,2,2)\) complete-intersection curve. Its degree is \(2^4=16\), while adjunction gives
\[
K_{Z_3}\cong\mathcal O_{Z_3}(8-6)=\mathcal O_{Z_3}(2).
\]
Hence \(\deg K_{Z_3}=32=2g-2\), so \(g=17\).

## Verification
The accompanying `verify.py` checks exact rational Vandermonde kernels for the boundary case \(n=3\), verifies for every coordinate \(m\) that a moment-kernel vector with \(y_m\ne0\) exists, and checks the complete-intersection degree and genus arithmetic. Its output is stored in `verification_output.txt`. These finite checks illustrate and regression-test the algebra; the proof for arbitrary \(n\ge3\) is the polynomial root-count argument above, not an extrapolation from computation.

## Relationship to prior work
Bhattacharya--Matsubara construct \(Z_n\) and \(\nu_n\), prove smoothness of \(Z_n\), derive the factorization of \(P_w\), prove surjectivity onto \(W\), and use this to prove that \(W\) is irreducible. Their stated result gives \([W]=4(n-1)H\) and \(\deg W=16(n-1)\), but does not identify \(\nu_n\) as birational or as the normalization morphism.

For genus two, Pal--Pauly identify the wobbly locus in the smooth intersection of two quadrics in \(\mathbf P^5\) as an irreducible surface of degree \(32\) and class \(8\Theta\). The statement here adds the normalization \(\mathbf P^1\times Z_3\) and the resulting non-normality.

A closely related 2026 doctoral thesis by Bhattacharya predates the arXiv posting by one day and explicitly studies the same genus-two divisor. Its abstract and metadata were inspectable, but the full thesis PDF was not accessible during this check. It therefore remains a specific residual originality risk rather than being treated as evidence of novelty.

## Limitations
The argument identifies the normalization and proves non-normality, but it does not compute the conductor, scheme structure of the singular locus, or its irreducible components. The thesis just mentioned could contain overlapping genus-two geometry that could not be compared at full-text level. No claim of exhaustive literature coverage is made.

## References
1. S. Bhattacharya and Y. Matsubara, *Fundamental groups of complements of wobbly divisors in intersections of two quadrics*, arXiv:2609.31421v1, submitted 25 September 2026.
2. S. Bhattacharya, *Fundamental Group of the Complement of the Wobbly Divisor in the Intersection of Two Quadrics*, PhD thesis, University of Southern Denmark, public record dated 24 September 2026.
3. S. Pal and C. Pauly, *The wobbly divisors of the moduli space of rank-2 vector bundles*, Advances in Geometry 21 (2021), 473--482, DOI 10.1515/advgeom-2021-0020.
