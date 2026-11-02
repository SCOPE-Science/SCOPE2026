# Exact finite-field counts and orthogonal orbits of invertible-value spin-factor derivations

## Finding

Let \(q\) be any odd prime power, \(k=\mathbb F_q\), and let \((V,B)\) be a nondegenerate symmetric bilinear space of dimension \(n\ge2\). Set \(J=k1\oplus V\), with Jordan multiplication
\[
(a1+u)\circ(b1+v)=(ab+B(u,v))1+av+bu.
\]
A nonzero derivation \(D\colon J\to J\) has **invertible values** when, for every \(x\in J\), either \(D(x)=0\) or \(D(x)\) is invertible in \(J\). Let \(\mathcal I(J)\) be the set of such derivations, explicitly excluding the zero map. Write \(\chi\) for the quadratic character of \(k^\times\).

Every \(D\in\mathcal I(J)\) has image an anisotropic two-plane \(W\subseteq V\), acts as a nonzero skew-adjoint transformation on \(W\), and vanishes on \(W^\perp\). Each anisotropic two-plane supports exactly \(q-1\) derivations in \(\mathcal I(J)\). Consequently, letting \(N=N(V,B)\) count anisotropic two-planes, the number of these derivations is \((q-1)N\), where
\[
N=\begin{cases}
\displaystyle\frac{q^{2m-1}(q^{2m}-1)}{2(q+1)},&n=2m+1\ (m\ge1),\\[6pt]
\displaystyle\frac{q^{2m-2}(q^m-\epsilon)(q^{m-1}-\epsilon)}{2(q+1)},&n=2m\ (m\ge1),\quad\epsilon=\chi((-1)^m\det B).
\end{cases}
\]
The character \(\epsilon\) is independent of basis because \(\det B\) changes by a square under congruence. The first formula is independent of the discriminant; the second distinguishes split and nonsplit even-dimensional forms.

Under conjugation by \(\operatorname{Aut}(J)=O(V,B)\), if \(N>0\) there are exactly \((q-1)/2\) orbits of \(\mathcal I(J)\), each of cardinality \(2N\). They are indexed by the nonsquare elements \(\eta\in k^\times\), where
\[
\eta=\tfrac12\operatorname{tr}(D^2),\qquad
\operatorname{charpoly}(D|_V)=t^{n-2}(t^2-\eta).
\]
For \(N=0\) there are no such derivations and no orbits. The formula includes dimension two, where the split form has none and the anisotropic form has \(q-1\).

**A boundary consequence.** The accessible April 2020 version of Kaygorodov–Lopatin–Popov, Corollary 8, excludes these derivations over perfect fields. Finite fields are perfect, and the explicit example \(k=\mathbb F_3\), \(n=2\), \(B=\operatorname{diag}(1,1)\), \(D|_V=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\) has invertible values, so that stated perfect-field exclusion cannot hold without an extra hypothesis. Their nearby Lemmas 7 and 9 already contain the ingredients for this example; this observation is not presented as an independent classification of admissible images.

## Assumptions and scope

The field is finite of odd characteristic, all vector spaces are finite-dimensional, and \(B\) is nondegenerate. “Anisotropic” means \(B(w,w)\ne0\) for every nonzero \(w\) of a subspace. “Invertible” means Jordan-invertible: there exists \(y\) with \(x\circ y=1\) and \(x^2\circ y=x\). We count distinct derivation maps, not tuples of generators or their scalar-normalized classes; \(D=0\) is excluded. The eigenvalue variable \(t\) in the characteristic polynomial is formal. The orthogonal group is the full isometry group, not just the special orthogonal subgroup. No characteristic-two claim is made.

## Proof

**Step 1 — derivations and units.** A derivation kills \(1\). For \(v\in V\), use \(v^2=B(v,v)1\) and derivation to obtain \(v\circ D(v)=0\). Writing \(D(v)=a1+w\), the \(V\)-component is \(av\); as \(v\ne0\) it forces \(a=0\). Polarizing yields \(B(Du,v)+B(u,Dv)=0\), and conversely any skew-adjoint endomorphism of \(V\), extended by \(D(1)=0\), is a derivation. For pure \(w\in V\), the element is Jordan-invertible exactly when \(B(w,w)\ne0\): if the latter is nonzero, the inverse is \(B(w,w)^{-1}w\), and if it vanishes, \(w^2=0\) rules out invertibility. Therefore \(D\) has invertible values precisely when its nonzero image vectors are anisotropic.

**Step 2 — permitted images.** For any skew-adjoint \(D\), \(\ker D=(\operatorname{im}D)^\perp\), and the matrix of \(BD\) is alternating; hence \(\operatorname{rank}D\) is even. Every quadratic form in at least three variables over a finite field has a nonzero isotropic vector (Chevalley–Warning, or the classical finite-field quadratic-form theorem). Thus an anisotropic, nonzero image has dimension exactly two. Such a plane \(W\) is nondegenerate; its complement gives \(V=W\perp W^\perp\), and \(D\) vanishes on \(W^\perp\), so \(D|_W\) is an invertible skew-adjoint operator. In a \(B\)-orthogonal basis of \(W\) with diagonal entries \(a,b\in k^\times\), all these operators have the form
\[
D(e_1)=c e_2,\qquad D(e_2)=-(b/a)c e_1,\qquad c\in k^\times.
\]
There are exactly \(q-1\) choices. Because \(W\) is anisotropic, \(-b/a\) is nonsquare, and \(D^2|_W=\eta I_W\) with \(\eta=-(b/a)c^2\), also nonsquare. Conversely, all such operators extended by zero are valid, and two different image planes give disjoint sets of derivations.

**Step 3 — count the planes.** Witt's extension theorem makes \(O(V,B)\) transitive on the anisotropic two-planes. The stabilizer of a plane is \(O^-_2(q)\times O(W^\perp)\) and \(|O^-_2(q)|=2(q+1)\). Standard finite-orthogonal-group orders are
\[
|O_{2m+1}(q)|=2q^{m^2}\prod_{i=1}^{m}(q^{2i}-1),\quad
|O^\epsilon_{2m}(q)|=2q^{m(m-1)}(q^m-\epsilon)\prod_{i=1}^{m-1}(q^{2i}-1).
\]
Here \(\epsilon=\chi((-1)^m\det B)\) for even dimension; removing an anisotropic plane reverses the even-dimensional type because its type is minus. Taking the stabilizer ratio gives the stated formulas for \(N\). For odd dimension, quotienting the orders in dimensions \(2m+1\), \(2\) and \(2m-1\) yields \(q^{2m-1}(q^{2m}-1)/(2(q+1))\). For even dimension \(2m\ge4\), quotienting by type \(-\epsilon\) in dimension \(2m-2\) gives \(q^{2m-2}(q^m-\epsilon)(q^{m-1}-\epsilon)/(2(q+1))\). In dimension \(2\), the same expression gives \(1\) in minus type and \(0\) in plus type, as needed.

**Step 4 — conjugacy.** Every Jordan automorphism fixes \(1\); since the square of each \(v\in V\) is scalar and the characteristic is odd, its image has zero scalar component. It therefore restricts to a linear isometry of \((V,B)\); conversely every isometry extends to a Jordan automorphism. Thus \(\operatorname{Aut}(J)=O(V,B)\). The scalar \(\eta=\tfrac12\operatorname{tr}(D^2)\) is preserved under conjugation. For each nonsquare \(\eta\) and each anisotropic plane \(W\), exactly two nonzero elements of \(\mathfrak{so}(W)\) square to \(\eta I_W\). An isometry of \(W\) with determinant \(-1\) swaps these two elements, and Witt extension moves \(W\) to any other anisotropic two-plane. Hence there is precisely one orbit for each nonsquare \(\eta\), of size \(2N\), accounting for all \((q-1)N\) maps. The characteristic polynomial is immediate from the decomposition \(V=W\perp W^\perp\).

**Step 5 — the explicit boundary instance.** Over \(\mathbb F_3\), \(u^2+v^2\) is nonzero for every nonzero pair \((u,v)\), because squares are \(0\) or \(1\) and \(1+1\ne0\). The displayed \(D\) has image all of \(V\), is skew-adjoint, and takes every nonzero input from \(V\) to an invertible pure element. The form is nondegenerate and \(J\) is the standard simple spin factor. Thus the perfect-field exclusion in the specified preprint version cannot apply literally to all perfect fields.

## Verification

A standalone standard-library Python checker independently enumerates all skew-adjoint operators in dimensions \(2\) through \(5\) for representative forms over \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_9\). It computes their image spaces by finite-field row reduction, explicitly tests anisotropy of every nonzero image vector, and compares the surviving counts and nonsquare-\(\eta\) multiplicities to both formulas. All twelve configurations passed. The attached checker also includes a degree-two extension-field implementation, rather than substituting the prime field. See `verify_spin_factor_invertible.py` and `verification_output.txt` for reproducibility. These finite checks corroborate but do not prove the unrestricted theorem.

## Relationship to prior work

Kaygorodov–Lopatin–Popov (arXiv:1511.00742, first public version November 2, 2015; inspected 2020 version) proves the skew-adjoint and anisotropic-image conditions in Lemmas 6–9. In particular, *the permitted-image criterion and existence of rank-two examples are prior work*. The present result isolates an arithmetic question not answered by those lemmas: the exact count for every finite field, every nondegenerate quadratic space, and both even-dimensional types; it additionally determines the full orthogonal conjugacy profile. The apparent perfect-field contradiction concerns **Corollary 8 of the accessible 2020 preprint**, not necessarily the later journal version. The orthogonal group orders, Witt extension, and finite-field anisotropic-dimension bound are classical inputs; none is claimed as new.

## Limitations

The theorem counts derivations on spin-factor Jordan algebras, not all finite-dimensional Jordan algebras. It excludes even characteristic, degeneracies in \(B\), and automorphism-group scheme structures. The raw existence criterion is already known; the claimed contribution is quantitative and orbit-theoretic. No assertion is made that the journal version retains the quoted perfect-field wording. The closest historical text has been inspected, but an unlocated enumeration or an implication from a broader theorem remains a publication-priority risk. Independent mathematical review has not been performed.

## References

1. I. Kaygorodov, A. Lopatin, Y. Popov, *Jordan algebras admitting derivations with invertible values*, arXiv:1511.00742, first submitted November 2, 2015, version 2 dated April 1, 2020. https://arxiv.org/abs/1511.00742 . Relevant material: Section 4.3, Lemmas 6, 7, 9, and Corollary 8.
2. Classical finite orthogonal-group structure, Witt extension, and order formulas; see the summary “Orthogonal group”, https://handwiki.org/wiki/Orthogonal_group , section “Over finite fields”.
3. E. C. Paige and standard structure theory of Jordan spin factors, as cited in reference 1, Section 2.
