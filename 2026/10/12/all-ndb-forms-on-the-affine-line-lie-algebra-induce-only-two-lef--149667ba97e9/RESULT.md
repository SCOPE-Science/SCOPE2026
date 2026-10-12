# All NDB forms on the affine-line Lie algebra induce only two left-symmetric classes

## Finding
Let \(k\) be a field with \(\operatorname{char}k\ne 2\), and let \(\mathfrak g=kt\oplus kx\) with \([t,x]=x\). Call a non-degenerate bilinear form \(\phi\) an NDB form when it satisfies the algebraic criterion
\[
\phi([u,v],w)+\phi(v,[u,w])=\phi(u,[v,w])
\]
for all \(u,v,w\in\mathfrak g\); over \(\mathbb R\) this is exactly the criterion in Kato's Lemma 3.3.

Every NDB form has, and only has, a matrix
\[
\Phi_{a,b}=\begin{pmatrix}a&b\\-b&0\end{pmatrix},\qquad a\in k,\quad b\in k^\times,
\]
in the ordered basis \((t,x)\). Under Lie-algebra automorphisms, every form is equivalent to a unique \(\Phi_{a,1}\), so the NDB-form orbit space is naturally parametrized by \(a\in k\).

In contrast, the induced left-symmetric products have exactly two isomorphism classes. Writing \(r=a/b\), the product \(P_r\) is
\[
t\mathbin{\Delta}t=-t-rx,\qquad t\mathbin{\Delta}x=0,\qquad x\mathbin{\Delta}t=-x,\qquad x\mathbin{\Delta}x=0.
\]
Two products \(P_r\) and \(P_s\) are isomorphic if and only if either \(r=s=0\) or \(r,s\ne0\). Thus all nonzero parameters collapse to one isomorphism class. Over \(\mathbb R\), the zero class is Kato's \(\mathcal A_2\) example and the nonzero class is represented by Kato's \(\mathcal F(-1)\) example.

The two product classes are separated internally: \(P_0\) has the affine line of nonzero idempotents \(-t+\beta x\), with \(\beta\in k\), whereas \(P_r\) has no nonzero idempotents when \(r\ne0\).

## Assumptions and scope
The field is arbitrary except that \(2\ne0\). Kato formulates NDB structures for real Lie algebras; the displayed identity is polynomial, so the result uses that identity as the definition over other fields. Isomorphism of left-symmetric algebras means a \(k\)-linear algebra isomorphism. Form equivalence in the form-moduli statement is by pullback under \(\operatorname{Aut}(\mathfrak g)\), without quotienting by scalar multiples of the form.

## Proof
Write
\[
[\phi]_{(t,x)}=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
Evaluating the NDB identity on basis triples gives exactly \(b+c=0\) and \(2d=0\). Since \(\operatorname{char}k\ne2\), this is \(c=-b\) and \(d=0\). The determinant is then \(b^2\), so non-degeneracy is equivalent to \(b\ne0\). This proves the form classification.

The derived ideal \(k x\) is characteristic. Hence every Lie automorphism has the form
\[
t\longmapsto t+\beta x,\qquad x\longmapsto \lambda x,
\]
with \(\beta\in k\) and \(\lambda\in k^\times\). Pullback transforms
\[
\Phi_{a,b}\longmapsto \Phi_{a,b\lambda}.
\]
Thus \(b\) can be normalized to \(1\), while \(a\) is unchanged; this proves uniqueness of the form parameter \(a\).

The induced product is defined by
\[
\phi(u\mathbin{\Delta}v,w)=-\phi(v,[u,w]).
\]
Solving the two pairing equations against \(w=t\) and \(w=x\) gives the displayed multiplication for \(P_r\), where \(r=a/b\).

Any left-symmetric isomorphism preserves the commutator Lie bracket, so it has the same form as the Lie automorphisms above. For a map with parameters \(\beta\) and \(\lambda\), compatibility with \(t\mathbin{\Delta}t\) is equivalent to
\[
s=r\lambda.
\]
The other three basis products are then automatically respected. Because \(\lambda\ne0\), zero cannot be isomorphic to a nonzero parameter, while any two nonzero parameters are related by a suitable \(\lambda\). Finally, for \(v=\alpha t+\gamma x\), the equation \(v\mathbin{\Delta}v=v\) reduces to
\[
-\alpha^2=\alpha,\qquad -r\alpha^2-\alpha\gamma=\gamma.
\]
The first equation gives \(\alpha=0\) or \(\alpha=-1\). The former forces \(v=0\); the latter forces \(r=0\) and leaves \(\gamma\) arbitrary. This gives the idempotent separator.

## Verification
The accompanying `verify.py` reconstructs all eight basis-triple NDB equations, verifies that their nonzero residuals are exactly the equations forcing \(c=-b\) and \(d=0\), solves the induced product symbolically, checks the left-symmetric representation identity, computes the automorphism pullback, derives the isomorphism defect \(s-r\lambda\), and checks the idempotent equations. The recorded execution ends with `CHECK_OK`.

## Relationship to prior work
Kato's arXiv:2609.33063v1 gives the general NDB criterion and, in Example 3.5, exhibits two particular NDB forms on \(\mathfrak{aff}(\mathbb R)\): a genuinely nonsymmetric form inducing \(\mathcal F(-1)\), and the purely skew form inducing \(\mathcal A_2\). The paper does not classify all NDB forms on this Lie algebra or determine the full fiber from NDB-form orbits to left-symmetric isomorphism classes.

Medina, Saldarriaga, and Giraldo, arXiv:1409.0221v3, classify all real flat left-invariant affine structures on the affine group of the line. That is a broader ambient classification of left-symmetric products, but it does not impose Kato's NDB-origin condition or classify the bilinear forms producing those products. The result here identifies that NDB-induced subfamily completely and explains why a one-parameter family of form orbits collapses to only two product classes.

## Limitations
The result does not classify NDB structures on higher-dimensional Lie algebras. Characteristic \(2\) is excluded because the basis equations only force \(2d=0\), so the displayed form classification changes there. The form-orbit statement uses Lie-algebra automorphisms rather than arbitrary bilinear-form congruence. The literature comparison leaves a residual possibility that the two-class consequence is implicit in an older low-dimensional left-symmetric classification, although no inspected source states the NDB-form classification or its orbit-to-product collapse.

## References
1. Naoki Kato, *Non-degenerate bilinear forms and left-symmetric structures*, arXiv:2609.33063v1, 2026.
2. Alberto Medina, Oscar Saldarriaga, and Hernán Giraldo, *Flat Affine or Projective Geometries on Lie Groups*, arXiv:1409.0221v3.
