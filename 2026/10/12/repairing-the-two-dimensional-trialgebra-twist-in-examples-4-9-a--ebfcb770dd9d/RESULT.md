# Repairing the two-dimensional trialgebra twist in Examples 4.9 and 4.22

## Finding

Consider the two-dimensional associative trialgebra cited in Example 4.9 of Braiek, Chtioui, Elhamdadi, and Mabrouk. The cited low-dimensional classification of Mainellis identifies the intended class as
\[
\operatorname{Trias}^{33}_2.
\]
With basis \(\{e_1,e_2\}\), its nonzero products are
\[
e_1\vdash e_1=e_1,\qquad e_1\vdash e_2=e_2,
\]
\[
e_1\dashv e_1=e_1,\qquad e_2\dashv e_1=e_2,
\]
and
\[
e_1\perp e_1=e_1,\qquad e_1\perp e_2=e_2.
\]
All unspecified products are zero.

The display in Example 4.9 repeats \(e_1\perp e_1\) in the position where the cited class has \(e_1\dashv e_1\). Read literally, that displayed multiplication is not an associative trialgebra. For instance,
\[
(e_1\dashv e_1)\vdash e_1=0
\]
while
\[
e_1\vdash(e_1\vdash e_1)=e_1,
\]
contradicting one of the dialgebra identities.

Now let
\[
\alpha(e_1)=a e_1,\qquad \alpha(e_2)=b e_2.
\]
Corollary 4.8 of the source requires \(\alpha\) to be an algebra endomorphism of all three products. This happens if and only if
\[
\boxed{
a(a-1)=0,\qquad b(a-1)=0.
}
\]
Since the coefficient ring is a field, the exact parameter locus is
\[
\boxed{
(a,b)=(0,0)
\quad\text{or}\quad
a=1\ \text{with}\ b\in K\ \text{arbitrary}.
}
\]
Thus the arbitrary-parameter assertion in Example 4.9 is too broad.

For these and only these diagonal parameters, the Yau-twisted products
\[
\vdash_\alpha=\alpha\circ\vdash,\qquad
\dashv_\alpha=\alpha\circ\dashv,\qquad
\perp_\alpha=\alpha\circ\perp
\]
give the claimed multiplicative Hom-associative trialgebra.

The correction propagates to Example 4.22. Theorem 4.21 defines
\[
\{x,y\}=x\vdash_\alpha y-y\dashv_\alpha x,
\qquad
[x,y]=x\perp_\alpha y-y\perp_\alpha x.
\]
For the corrected trialgebra,
\[
\boxed{\{x,y\}=0\quad\text{for all }x,y\in A,}
\]
and the only nonzero basic Lie bracket is
\[
\boxed{
[e_1,e_2]=b e_2,\qquad [e_2,e_1]=-b e_2.
}
\]
In particular, the relation
\[
\{e_1,e_1\}=a e_1
\]
printed in Example 4.22 is not the Hom-Leibniz-trialgebra structure obtained from the intended associative trialgebra by Theorem 4.21.

Over every finite field \(\mathbf F_q\), the diagonal endomorphism-twist locus has exactly
\[
\boxed{q+1}
\]
points: the isolated zero map and the affine line
\[
\alpha(e_1)=e_1,\qquad \alpha(e_2)=b e_2.
\]

## Assumptions and scope

The primary source works over a field of characteristic zero and states that all Hom-algebras in the paper are multiplicative. Its Corollary 4.8 explicitly assumes that the twisting map is an algebra endomorphism before applying the Yau-type twist.

The repair of the multiplication table uses the exact class cited by the source. Mainellis lists \(\operatorname{Trias}^{33}_2\) with precisely the six nonzero products displayed above. This resolves the repeated-\(\perp\) typographical error without guessing a new algebra.

The endomorphism computation itself is characteristic-free. The finite-field count is therefore an algebraic consequence of the corrected table, not an assumption made by the primary source.

## Proof

The two products
\[
e_1\vdash e_1=e_1
\qquad\text{and}\qquad
e_1\vdash e_2=e_2
\]
already force all restrictions on a diagonal endomorphism.

Preservation of the first product gives
\[
\alpha(e_1)
=
\alpha(e_1\vdash e_1)
=
\alpha(e_1)\vdash\alpha(e_1)
=
a^2e_1.
\]
Since \(\alpha(e_1)=ae_1\),
\[
a(a-1)=0.
\]

Preservation of the second product gives
\[
\alpha(e_2)
=
\alpha(e_1\vdash e_2)
=
\alpha(e_1)\vdash\alpha(e_2)
=
ab\,e_2,
\]
hence
\[
b(a-1)=0.
\]

The four remaining nonzero products impose exactly the same two equations. Every zero product is automatically preserved by a diagonal map. Therefore the displayed equations are both necessary and sufficient.

Over a field, \(a(a-1)=0\) gives \(a=0\) or \(a=1\). If \(a=0\), then \(b(a-1)=0\) forces \(b=0\). If \(a=1\), the second equation is automatic. This proves the exact parameter locus.

For the downstream admissible operations, substitute the corrected twisted products into Theorem 4.21. One obtains
\[
\{e_1,e_1\}
=
e_1\vdash_\alpha e_1-e_1\dashv_\alpha e_1
=
ae_1-ae_1
=
0,
\]
and
\[
\{e_1,e_2\}
=
e_1\vdash_\alpha e_2-e_2\dashv_\alpha e_1
=
be_2-be_2
=
0.
\]
The other basic dicommutators vanish termwise. Thus the Hom-Leibniz operation is identically zero.

For the middle-product commutator,
\[
[e_1,e_2]
=
e_1\perp_\alpha e_2-e_2\perp_\alpha e_1
=
be_2,
\]
and skew-symmetry gives the reversed bracket.

Finally, over \(\mathbf F_q\), the solution set consists of one point with \(a=0\) and \(q\) points with \(a=1\), for a total of \(q+1\).

## Verification

The included program `artifacts/verify.py` reconstructs the six nonzero products of \(\operatorname{Trias}^{33}_2\) and verifies all eleven classical triassociative identities.

It also reads the primary source's repeated-\(\perp\) table literally and exhibits the failed dialgebra identity at \((e_1,e_1,e_1)\).

For a symbolic diagonal map, the program reconstructs every endomorphism defect and obtains exactly the two factors
\[
a(a-1)
\qquad\text{and}\qquad
b(a-1).
\]
It then verifies all Hom-associative trialgebra identities and multiplicativity on both solution branches, and confirms that the advertised sample choice
\[
(a,b)=(2,1)
\]
fails endomorphism preservation.

The program independently reconstructs the Theorem 4.21 descendant operations and obtains zero dicommutator together with
\[
[e_1,e_2]=b e_2.
\]

As a finite-field replay, it enumerates the diagonal twist locus over
\[
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7,\quad
\mathbf F_{11},
\]
finding respectively
\[
4,\quad6,\quad8,\quad12
\]
valid twists. The checker returns `VERIFY_OK`.

## Relationship to prior work

Braiek, Chtioui, Elhamdadi, and Mabrouk state Corollary 4.8 with the correct endomorphism hypothesis, but Example 4.9 then introduces a diagonal map with unrestricted parameters and invokes that corollary without checking the hypothesis. The same example also repeats the middle product where the cited associative-trialgebra class has a left product.

Mainellis's complete two-dimensional complex classification identifies the cited multiplication unambiguously as \(\operatorname{Trias}^{33}_2\). Its table supplies the missing relation
\[
e_1\dashv e_1=e_1.
\]

The downstream Example 4.22 invokes Theorem 4.21 on Example 4.9. Once the cited base trialgebra is restored, the theorem makes the Leibniz operation vanish identically, so the printed nonzero value \(\{e_1,e_1\}=ae_1\) is not implied by the source theorem.

Focused searches for the exact example number, the diagonal endomorphism constraint, \(\operatorname{Trias}^{33}_2\), the downstream Example 4.22 relation, and a correction or erratum did not locate a covering repair. A later journal version of the same work is indexed in 2025, but its full text was not publicly retrievable for direct comparison.

## Limitations

The result repairs the two connected examples and does not alter the general statements of Corollary 4.8 or Theorem 4.21.

The exact journal typesetting of the 2025 publication could not be inspected, so a journal-only correction absent from the public preprint remains a residual access risk.

The finite-field count concerns the same polynomial multiplication table outside the primary source's characteristic-zero convention.

Failed literature searches do not establish absolute historical novelty.

## References

1. S. Braiek, T. Chtioui, M. Elhamdadi, and S. Mabrouk, “Hom-associative algebras, Admissibility and Relative averaging operators,” arXiv:2311.08407v1, first public 20 August 2023; later published in *Journal of Geometry and Physics* 218 (2025), 105677, DOI `10.1016/j.geomphys.2025.105677`.
2. E. Mainellis, “Classification of Low-dimensional Complex Triassociative Algebras,” arXiv:2209.04351v1, first public 9 September 2022.
