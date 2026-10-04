# The H3 unexpected sextic is a rational curve with one ordinary quintuple point
## Finding
Let \\(Z(H_3)\\subset\\mathbb P^2_{\\mathbb C}\\) be the 15-point configuration attached to the non-crystallographic root system \\(H_3\\) in Harbourne--Migliore--Nagel--Teitler. Their computation, later written explicitly by Di Gennaro--Ilardi--Miró-Roig--Szemberg--Szpond, gives for a general point \\(P\\) a unique sextic \\(C_P\\) through \\(Z(H_3)\\) with multiplicity \\(5\\) at \\(P\\).

The additional geometric conclusion is:

\\[
C_P\text{{ is irreducible, }}\quad P\text{{ is an ordinary quintuple point, }}\quad g(\\widetilde C_P)=0,
\\]

and \\(C_P\\) is smooth away from \\(P\\).

## Assumptions and scope
The ground field is \\(\\mathbb C\\). The statement concerns the unique member for \\(P\\) in a nonempty Zariski-open subset of \\(\\mathbb P^2\\). For the exact witness computation we use the coordinates printed in the original source, with \\(s^2=5\\), and take \\(P_0=[3:5:1]\\).

The 15 points are
\\[
[0:0:1],[1:0:1],[1:0:-1],[0:1:1],[0:1:-1],
\\]
\\[
[0:1:2+s],[0:1:-2-s],[1:0:-2-s],[1:0:2+s],[1:-1:0],[1:1:0],
\\]
\\[
[s+3:-2s-4:3s+7],[2s+4:-s-3:-3s-7],
[2s+4:-s-3:3s+7],[s+3:-2s-4:-3s-7].
\\]

## Proof
Write a degree-six form in the 28 monomials \\(x^iy^jz^k\\) with \\(i+j+k=6\\). Vanishing at the 15 configuration points and vanishing to order at least \\(5\\) at \\(P_0\\) gives a \\(30\\times28\\) matrix over \\(\\mathbb Q(\\sqrt5)\\). Exact row reduction has rank \\(27\\), so the witness sextic is unique up to scale.

After setting \\(x=3+u\\), \\(y=5+v\\), \\(z=1\\), the normalized witness has no terms of total degree below \\(5\\) and takes the form
\\[
F(3+u,5+v,1)=A_5(u,v)+B_6(u,v),
\\]
where
\\[
\\begin{{aligned}}
A_5={}&(6975-1920\\sqrt5)u^5+(-29100+5475\\sqrt5)u^4v\\\\
&+(45600-6300\\sqrt5)u^3v^2+(-33600+3300\\sqrt5)u^2v^3\\\\
&+(11700-645\\sqrt5)uv^4-1545v^5,
\\end{{aligned}}
\\]
and
\\[
\\begin{{aligned}}
B_6={}&3125u^6+(-7980+241\\sqrt5)u^5v+(4180-280\\sqrt5)u^4v^2\\\\
&+(5120-160\\sqrt5)u^3v^3+(-6900+280\\sqrt5)u^2v^4\\\\
&+(2860-81\\sqrt5)uv^5-405v^6.
\\end{{aligned}}
\\]
Exact Euclidean algorithms in \\(\\mathbb Q(\\sqrt5)[u]\\), after setting \\(v=1\\), give
\\[
\\gcd(A_5(u,1),B_6(u,1))=1,
\\qquad
\\gcd(A_5(u,1),\\partial_uA_5(u,1))=1.
\\]
The coefficient of \\(u^5\\) in \\(A_5\\) is nonzero, so the second equality says that the binary tangent form \\(A_5\\) is squarefree. Hence \\(P_0\\) is an ordinary quintuple point.

To prove irreducibility, suppose a degree-six plane curve of multiplicity \\(5\\) at a point factors. The sum, over its positive-degree factors, of \\(\\deg(G)-\\operatorname{{mult}}_P(G)\\) is \\(1\\). Thus at least one nonconstant factor \\(G\\) has \\(\\deg(G)=\\operatorname{{mult}}_P(G)\\); in local coordinates \\(G\\) is homogeneous. Since the whole local equation has only degrees \\(5\\) and \\(6\\), this homogeneous factor divides both \\(A_5\\) and \\(B_6\\), contradicting their coprimality. Therefore the witness sextic is irreducible.

Reducible sextics form a Zariski-closed subset of the projective space of sextic forms, and vanishing of the discriminant of the tangent quintic is also closed. On the open set where the interpolation kernel is one-dimensional, its coefficient vector varies rationally with \\(P\\). The exact witness therefore implies that for general \\(P\\), \\(C_P\\) is irreducible and has an ordinary quintuple point at \\(P\\).

Finally, a plane sextic has arithmetic genus \\(10\\), while an ordinary quintuple point has delta invariant \\(\\binom52=10\\). For an irreducible plane curve,
\\[
g(\\widetilde C_P)=10-\\sum_Q\\delta_Q\\ge0.
\\]
The contribution at \\(P\\) already equals \\(10\\), so \\(g(\\widetilde C_P)=0\\) and no other singular point can occur.

## Verification
The standalone verifier `artifacts/verify.py` uses only Python's standard library. It reconstructs \\(\\mathbb Q(\\sqrt5)\\) exactly, rebuilds the 30 interpolation equations, checks rank \\(27\\), reconstructs the unique kernel vector, checks all 15 incidences and all order-\\(<5\\) jet conditions, reconstructs \\(A_5\\) and \\(B_6\\), and runs exact polynomial gcd computations proving coprimality and squarefreeness.

## Relationship to prior work
Harbourne--Migliore--Nagel--Teitler list the \\(H_3\\) case \\((d,m)=(6,5)\\) with actual dimension \\(1\\) and give the 15 coordinates. Di Gennaro--Ilardi--Miró-Roig--Szemberg--Szpond later write an explicit equation for the unique unexpected sextic and study the associated and companion surfaces. In the inspected full texts, the \\(H_3\\) discussion does not state that the unexpected sextic is irreducible, rational, ordinary at the imposed point, or smooth elsewhere. The present calculation supplies exactly that geometry.

## Limitations
The claim is generic in the assigned point \\(P\\), not a statement about every special point. It does not classify degenerations when \\(P\\) lies on the closed exceptional locus, nor does it determine the full automorphism group of the sextic or the detailed geometry of the companion surface.

## References
B. Harbourne, J. Migliore, U. Nagel, Z. Teitler, *Unexpected hypersurfaces and where to find them*, arXiv:1805.10626; Michigan Math. J. 70 (2021), 301--339, DOI 10.1307/mmj/1593741748.

R. Di Gennaro, G. Ilardi, R. M. Miró-Roig, T. Szemberg, J. Szpond, *Companion varieties for root systems and Fermat arrangements*, arXiv:2101.07346; J. Pure Appl. Algebra 226 (2022), 107055, DOI 10.1016/j.jpaa.2022.107055.
