# Independent mathematical audit

## correctness

PASS

Normalize w=sqrt(d) and write x=sqrt(a)(1+u), y=sqrt(b)(1+v), z=sqrt(c)(1+t). The involution sends the three coordinates to their inverses, so in characteristic two its fixed equations are precisely u²=v²=t²=0, giving I with basis 1,u,v,t,uv,ut,vt,uvt. A fresh independent symbolic expansion of the stated actual 4×4 determinant over F2[A,B,C,D,u,v,t] verified all squarefree local coefficients vanish: f∈I and partial derivatives ∈I. The exact three-by-three minor of the quadratic coefficient rows of (f,f_v,f_t) equals (ABCD)^4(A+B)(A+C)(A+D)^2(B+C)^2(B+D)(C+D), nonzero on the pairwise-distinct nonzero locus. Thus J→I/mI surjects, and Nakayama yields J=I in the completed local ring. The independent computer-algebra derivation matched the entire claimed universal minor polynomial, rather than checking only a finite sample. Distinguishing the local Jacobian scheme from the reduced singular locus and restricting to the torus are essential.

## originality

PASS

Qualified novelty is the equality of the characteristic-two infinitesimal Hutchinson fixed scheme with the Weddle quartic Tjurina/Jacobian scheme, including its explicit length-eight algebra. The surface, parameter determinant, D4-type extra point, and geometric fixed-point support are prior; these alone do not determine a nonreduced scheme equality. Primary 1905 coverage remains a historical risk.

## value

PASS

For a natural Weddle quartic and its classical Hutchinson involution in wild characteristic two, reduced fixed-point support loses the entire infinitesimal geometry. An explicit uniform equality between its fixed-point functor and Jacobian singular scheme yields an exact local algebra, multiplicity eight and Hilbert function (1,3,3,1) on a four-parameter locus. This connects two independently motivated geometric structures and can inform deformation and quotient analysis; it is more than merely naming a known D4 singularity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
