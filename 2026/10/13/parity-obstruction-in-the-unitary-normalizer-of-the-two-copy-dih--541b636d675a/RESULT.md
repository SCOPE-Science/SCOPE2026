# Parity obstruction in the unitary normalizer of the two-copy dihedral permutation code
## Finding
Let \(D_n=\langle r,f\mid r^n=f^2=1,\;frf=r^{-1}\rangle\), with \(n\ge3\), act on the \(n\) vertices of a regular polygon through its natural permutation representation \(V\). Consider the two-copy representation \(W=V\oplus V\), which is the dihedral code representation studied in Bradshaw, LaBorde, and Montero.

Every abstract automorphism has the form
\[
\phi_{a,b}:\quad r\mapsto r^a,\qquad f\mapsto r^b f,
\]
where \(a\in(\mathbb Z/n\mathbb Z)^\times\) and \(b\in\mathbb Z/n\mathbb Z\). Define
\[
\operatorname{Aut}_W(D_n)=\{\phi\in\operatorname{Aut}(D_n):W\simeq W\circ\phi\}.
\]
Then
\[
N_{U(2n)}(W(D_n))/C_{U(2n)}(W(D_n))\cong\operatorname{Aut}_W(D_n),
\]
and the subgroup on the right is exactly
\[
\operatorname{Aut}_W(D_n)=
\begin{cases}
\operatorname{Aut}(D_n),& n\text{ odd},\\
\{\phi_{a,b}:a\in(\mathbb Z/n\mathbb Z)^\times,\ b\equiv0\pmod2\},& n\text{ even}.
\end{cases}
\]
Thus, when \(n\) is even, the normalizer quotient has order \(n\varphi(n)/2\) and is an index-two subgroup of the full abstract automorphism group. In particular, for the dyadic family \(n=2^m\) with \(m\ge2\), only the reflection-class-preserving automorphisms occur by unitary conjugation.

## Assumptions and scope
The statement concerns the full unitary normalizer of the represented subgroup \(W(D_n)\subset U(2n)\), modulo its unitary centralizer, for the specific representation \(W=V\oplus V\). It does not alter the construction of the code space, the syndrome count, or the continuous \(U(2)\) multiplicity-space operations coming from the centralizer. It also does not claim that the same index-two restriction holds for other faithful representations of \(D_n\).

The parameter \(a\) must be a unit modulo \(n\), not merely a nonzero residue, because \(r\mapsto r^a\) must preserve the order \(n\) of the rotation generator.

## Proof
Conjugation by a unitary normalizing \(W(D_n)\) induces an automorphism \(\phi\) of \(D_n\), because \(W\) is faithful. Its kernel is the centralizer. The image consists precisely of automorphisms for which \(W\) and \(W\circ\phi\) are unitarily equivalent. For finite groups, unitary representations are equivalent exactly when their characters agree, so the quotient is \(\operatorname{Aut}_W(D_n)\).

The character of the natural permutation representation is the number of fixed vertices. For a nonidentity rotation it is zero. A reflection \(r^j f\) acts on vertex labels \(i\in\mathbb Z/n\mathbb Z\) by
\[
i\longmapsto j-i,
\]
so its fixed points solve
\[
2i\equiv j\pmod n.
\]
If \(n\) is odd, this congruence has exactly one solution for every \(j\), so all reflections have the same character value. Every automorphism therefore preserves the character of \(V\), and hence of \(W\).

If \(n\) is even, a reflection \(r^j f\) has two fixed vertices when \(j\) is even and none when \(j\) is odd. Since every unit \(a\) modulo an even \(n\) is odd, \(\phi_{a,b}\) sends \(r^j f\) to \(r^{aj+b}f\), which preserves the parity of \(j\) exactly when \(b\) is even. Therefore odd \(b\) changes the permutation character. In particular,
\[
\chi_V(f)=2,\qquad \chi_V(rf)=0,
\]
so no unitary can conjugate \(W(f)\) to \(W(rf)\), because trace is invariant under unitary conjugation.

The obstruction is also sufficient. For any unit \(a\) and any \(c\in\mathbb Z/n\mathbb Z\), define the basis permutation
\[
P_{a,c}|i\rangle=|ai+c\rangle.
\]
A direct computation gives
\[
P_{a,c}V(r)P_{a,c}^{\dagger}=V(r^a),\qquad
P_{a,c}V(f)P_{a,c}^{\dagger}=V(r^{2c}f).
\]
For odd \(n\), every \(b\) has a solution of \(2c\equiv b\pmod n\). For even \(n\), such a solution exists exactly when \(b\) is even. Taking two copies of \(P_{a,c}\) therefore realizes every and only the character-preserving automorphisms.

## Verification
An exact integer checker enumerates all automorphisms for \(3\le n<25\), computes the natural permutation character on every rotation and reflection, confirms the odd/even criterion above, constructs a solution of \(2c\equiv b\pmod n\) whenever allowed, and verifies the two conjugation identities directly on every basis vector. The checker prints `VERIFY_OK`. These finite tests corroborate the proof; they are not used as evidence for the all-\(n\) statement.

## Relationship to prior work
Bradshaw, LaBorde, and Montero identify \(W\) as two copies of the natural permutation representation and classify its centralizer. Their published normalizer discussion states that the quotient by the centralizer is the full automorphism group and proposes a Fourier-basis implementer involving \(2^{-1}\). The same article later specializes operationally to \(n=2^m\), where \(2\) is not invertible modulo \(n\). The character calculation above shows the precise representation-theoretic restriction: for even \(n\), automorphisms interchanging the two reflection classes cannot be implemented by unitary conjugation in this representation.

The underlying facts that even dihedral permutation actions have two reflection types, with one type fixing two vertices and the other fixing none, are standard. The new point here is the exact consequence for the normalizer quotient of this specific recent quantum-code representation, together with a constructive implementation of every surviving automorphism.

## Limitations
This result corrects the discrete quotient of the full unitary normalizer for the stated representation. It does not imply a failure of the code construction, syndrome extraction, the centralizer computation, or the later choice of a smaller physical error group. It does not classify normalizers for arbitrary representations or for altered physical embeddings of the same abstract dihedral group. No claim is made that the abstract parity facts about dihedral groups are new.

## References
1. Z. P. Bradshaw, M. L. LaBorde, and D. Montero, “Symmetry-Based Quantum Codes Beyond the Pauli Group,” arXiv:2512.07908; Phys. Rev. A 113, 042431 (2026), DOI 10.1103/47pv-zzxb. Earliest public version: 2025-12-08.
2. M. Grech and A. Kisielewicz, “Cyclic Permutation Groups that are Automorphism Groups of Graphs,” Graphs and Combinatorics 35, 1405–1432 (2019). The preliminaries record the fixed-point dichotomy for reflections in the natural dihedral action.
