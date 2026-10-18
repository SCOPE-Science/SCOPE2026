# The primitive Klein Hessian sextic is smooth away from characteristics two and seven

## Finding

Let \(Q=x^3y+y^3z+z^3x\) and let
\[
H=x^5z+xy^5+yz^5-5x^2y^2z^2.
\]
For every algebraically closed field \(k\) of prime characteristic \(p\), the projective plane sextic \(C_p=V(H)\subset\mathbb P^2_k\) has the following complete **geometric singular-point** classification.

- For \(p\ne2,7\), \(C_p\) is smooth, including in characteristic three.
- For \(p=2\), the singular locus comprises precisely seven distinct points \([t^3:t:1]\), indexed by \(t^7=1\). They are all ordinary double points with two distinct tangent directions.
- For \(p=7\), there is precisely one singular point \([2:4:1]\). It has multiplicity three and tangent cone \(-2(v-3u)^3\) in local affine coordinates \(u=x-2\), \(v=y-4\), \(z=1\).

In fact \(\det\operatorname{Hess}(Q)=-54H\) over the integers. Our reduction refers to the *primitive* integral polynomial \(H\), not the raw determinant in small characteristic.

## Assumptions and scope

All singularities are geometric over algebraic closures. Singular means that the homogeneous polynomial and all three homogeneous first derivatives vanish at a projective point. This theorem concerns the specified integral model, which is part of the statement; changing a model by a matrix whose determinant is divisible by the residue characteristic can alter the special fiber. In characteristic seven we assert the exact tangent cone and multiplicity, not the complete analytic type, number of branches or delta-invariant.

## Proof

**Integral Hessian identity.** Direct differentiation of \(Q\) gives \(\det\operatorname{Hess}(Q)=-54H\). The integer factor is essential: the raw Hessian determinant is identically zero after reduction modulo either two or three, but \(H\) remains a nonzero sextic.

**Coordinate boundary.** If any projective coordinate vanishes, the equation \(H=0\) forces the point to be one of the three coordinate vertices. Each vertex is smooth because the derivative in the cyclically next coordinate is one. Therefore every singular point lies on the torus \(xyz\ne0\).

**Torus equations.** Set \(A=x^5z\), \(B=xy^5\), \(C=yz^5\), and \(D=x^2y^2z^2\), and write \(U=A/D\), \(V=B/D\), \(W=C/D\). Then \(UVW=1\), and \(H=0\) says \(U+V+W=5\). The three logarithmic derivatives \(xH_x\), \(yH_y\), \(zH_z\), divided by \(D\), yield
\[
5U+V=10,\qquad 5V+W=10,\qquad U+5W=10.
\]
The coefficient matrix has determinant \(126=2\cdot3^2\cdot7\).

If \(p\notin\{2,3,7\}\), the unique solution is \(U=V=W=5/3\). The multiplicative equation would require \(125=27\) in the field, hence \(98=0\), impossible under this hypothesis. In characteristic three, the linear equations imply \(V=U+1\) and \(W=U+2\), so \(U+V+W=0\), contrary to \(5=2\). Thus these characteristics have no singular points.

In characteristic two, the derivative equations imply \(U=V=W\); their sum equation then gives \(U=V=W=1\). With \(z=1\), \(V=y^3/x=1\) gives \(x=y^3\), while \(U=x^3/y^2=1\) becomes \(y^7=1\). These give exactly seven distinct solutions, as \(7\) is prime to the characteristic. A direct Taylor expansion at \([1:1:1]\) has no linear part and quadratic initial form \(u^2+uv+v^2\). This quadratic is squarefree over an algebraic closure of characteristic two: if it were a square, its mixed coefficient would vanish. The transformations \((x,y,z)\mapsto(t^3x,ty,z)\) for \(t^7=1\) preserve \(V(H)\) and act transitively on the singular points. Thus all seven are ordinary nodes.

In characteristic seven, the derivative equations yield \(V=3+2U\) and \(W=2+4U\), the third equation being dependent. Substitution into \(UVW=1\) gives \((U+3)^3=0\), hence \(U=V=W=4\). Since \(V=y^3/x\), we have \(x=y^3/4\) on \(z=1\). Substitution into \(U=x^3/y^2=4\) yields \(y^7=4\). In characteristic seven, the Frobenius equation has the unique geometric solution \(y=4\), whence \(x=2\). This point satisfies the remaining equation and is singular. Its Taylor expansion in \(u=x-2\), \(v=y-4\) has no terms of total degree below three and degree-three part
\[
5u^3+2u^2v+4uv^2+5v^3=-2(v-3u)^3\quad(\bmod\ 7).
\]
It has multiplicity precisely three and one triple tangent line. Together with the coordinate-boundary argument, the enumeration is exhaustive. \(\square\)

## Verification

The standalone Python standard-library program `verify.py` reconstructs the integral Hessian identity as a polynomial equality; checks the exact characteristic-two and characteristic-seven Taylor initial forms; verifies all seven characteristic-two points in \(\mathbb F_8\); and evaluates the defining equation and gradient for \(3{,}358\) normalized rational affine points across eleven small prime fields. It returns `VERIFY_OK`. These finite tests are corroborative: the all-primes classification is supplied by the algebraic torus derivation above, not by finite extrapolation.

## Relationship to prior work

The Hessian sextic is a classical Klein-quartic invariant: Elkies discusses the Klein quartic and its small-characteristic arithmetic and gives this normalized sextic. Koike's 2015 preprint studies the Klein quartic from a Shimura-curve perspective. Dolgachev's 2024 treatment studies the quartic itself and its automorphisms in odd characteristic, including its unusual characteristic-three behavior. The present statement fixes the primitive integer model and classifies **geometric singular points of its sextic special fibers** simultaneously over all residue characteristics. This is not a claim of discovering the sextic or the exceptional importance of two and seven for Klein geometry.

## Limitations

The original 1999 Elkies chapter was identifiable through catalogues and indexed extracts, but its complete body could not be inspected. It is a material originality risk: its description of small-characteristic invariants may contain related or equivalent information. Its archived publication is dated only to a year in one catalogue; the selected source date \(2015\text{-}05\text{-}11\) is the verifiable first arXiv posting date for Koike’s related algebraic-geometric Klein-quartic source. The earlier 1999 Elkies chapter is acknowledged but has no verified first-publication day; catalogue dates are not treated as initial public-release dates. This work does not analyze scheme-theoretic singularity lengths, all analytic branches in characteristic seven, or preservation under alternative integral coordinate models. Independent mathematical review has not occurred.

## References

1. N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, Cambridge University Press / MSRI Publications 35, 1999, chapter DOI: `10.1017/9781009701730.004`; institutional catalogue (1999): `https://dash.harvard.edu/entities/publication/73120378-7d3e-6bd4-e053-0100007fdf3b`; date-resolved bibliography: `https://portal.mardi4nfdi.de/wiki/The_Klein_quartic_in_number_theory`.
2. K. Koike, *The Fermat septic and the Klein quartic as moduli spaces of hypergeometric Jacobians*, arXiv:1505.02471, first posted 2015-05-11.
3. I. Dolgachev, *Automorphisms of del Pezzo surfaces in odd characteristic*, *Journal of the London Mathematical Society* (2024), DOI: `10.1112/jlms.12905`, especially §4.2.
