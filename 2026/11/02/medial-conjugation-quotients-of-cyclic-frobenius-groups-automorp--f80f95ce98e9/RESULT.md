# Medial conjugation quotients of cyclic Frobenius groups: automorphisms and an infinite collision family

## Finding
Let \(K\) be a nonzero finite abelian group of order \(n\), and let \(\alpha\in\operatorname{Aut}(K)\) have order \(m\ge 3\). Assume that \(\alpha^j-I\) is bijective for every \(1\le j<m\). Write \(G=K\rtimes_\alpha C_m\) and \(k=(n-1)/m\). The universal medial quotient of the conjugation quandle of \(G\) has precisely \(n+m-1\) points and is isomorphic to the quandle \(Q_{n,m}=K\sqcup\{s_1,\ldots,s_{m-1}\}\) with multiplication
\[
 a\triangleright b=a,\quad a\triangleright s_j=\alpha^{-j}(a),\quad s_i\triangleright x=s_i
\]
for every \(a,b\in K\), every \(x\in Q_{n,m}\), and \(1\le i,j<m\). Its isomorphism type depends only on \((n,m)\), not on \(K\) or the specific fixed-point-free action. The number \(k\) is a positive integer, and
\[
\operatorname{Aut}(Q_{n,m})\cong\bigl(C_m\wr S_k\bigr)\rtimes (\mathbb Z/m\mathbb Z)^\times,
\quad |\operatorname{Aut}(Q_{n,m})|=m^k k!\varphi(m).
\]
The unit group acts by applying the same power automorphism to each cyclic factor, and commutes with permutations of those factors. The inner group is the diagonal copy of \(C_m\); hence \(\operatorname{Out}(Q_{n,m})\) has order \(m^{k-1}k!\varphi(m)\).

For every \(r\ge1\), the nonisomorphic groups
\[
G_{1,r}=(C_4)^{2r}\rtimes C_3,\qquad G_{2,r}=(C_2)^{4r}\rtimes C_3
\]
with the fixed-point-free actions defined below have identical universal medial conjugation quotients \(Q_{16^r,3}\). For \(r=1\) this is an eighteen-element quandle with automorphism group of order \(58\,320\).

## Assumptions and scope
A quandle is a set with an idempotent, right-invertible, right-self-distributive operation \(\triangleright\). It is *medial* when \((x\triangleright y)\triangleright(z\triangleright w)=(x\triangleright z)\triangleright(y\triangleright w)\). The conjugation operation is \(x\triangleright y=y^{-1}xy\). The universal medial quotient is the quotient by the smallest quandle congruence making the induced quandle medial, with its usual universal mapping property. All groups in the theorem are finite; the action hypothesis is essential, and the result on automorphisms is asserted only for \(m\ge3\).

## Proof
**Derived-orbit quotient and its multiplication.** Since \(K\) is abelian and \(\alpha-I\) is bijective, \([G,G]=K\). The known derived-orbit description of the universal medial quotient of a group conjugation quandle identifies two elements exactly when they lie in the same orbit under conjugation by \([G,G]\). To see directly why this applies, the orbits form a quandle congruence; conjugations induced by the abelianization of \(G\) commute on the quotient, so the quotient is medial. Conversely, in any medial image of the conjugation quandle the image of the group identity gives an element whose right translation is the identity. Substituting it into the medial law shows that all right translations on the image commute. The conjugation action of every group commutator must then be trivial in the image, so the quotient is universal.

Conjugation by \(K\) fixes each element of \(K\). For \(1\le j<m\), conjugation by \(K\) acts transitively on the full coset \(Kt^j\): the change in the \(K\)-coordinate is an image of \(\alpha^j-I\), which is surjective. There are therefore \(n\) singleton classes and one class for each nonidentity complement coset. Conjugation by \(t^j\) acts on \(K\) as \(\alpha^{-j}\), whereas any representative of \(Kt^i\) stays in its class after conjugation by any element. These observations give the stated multiplication table. Its right translations are the identity on the \(s_i\) and, on \(K\), powers of \(\alpha\).

**Intrinsic structure and normalizer.** The elements with trivial right translation are exactly the \(n\) elements of \(K\), since \(\alpha^j\ne I\) for \(1\le j<m\). Thus every quandle automorphism preserves \(K\), and restricts to a permutation \(f\) of \(K\) normalizing the cyclic permutation group \(\langle\alpha\rangle\). Conversely, any such normalizer element sends \(\alpha\) to \(\alpha^u\) for some unit \(u\in(\mathbb Z/m\mathbb Z)^\times\), and extends to exactly one quandle automorphism by sending \(s_j\) to \(s_{uj}\). Hence \(\operatorname{Aut}(Q_{n,m})\cong N_{S(K)}(\langle\alpha\rangle)\).

Every nonzero element of \(K\) has an \(\alpha\)-orbit of length \(m\), while zero is the sole fixed point. There are exactly \(k=(n-1)/m\) nontrivial cycles. A permutation normalizing \(\langle\alpha\rangle\) fixes zero; it may rotate the \(k\) cycles independently, permute the cycles, and uniformly replace the common generator by any generator \(\alpha^u\). Labeling each cycle by \(\mathbb Z/m\mathbb Z\) realizes all these choices and proves the semidirect-product description and order formula. The right translations generate exactly \(\langle\alpha\rangle\), embedded diagonally across the cycles; dividing its order gives the claimed outer-group order. The cycle structure also proves that any two admissible data sets with the same \((n,m)\) yield isomorphic quandles.

**Infinite collision.** On \((\mathbb Z/4\mathbb Z)^2\) and \((\mathbb Z/2\mathbb Z)^2\), use the order-three matrix
\[
A=\begin{pmatrix}0&-1\\1&-1\end{pmatrix}.
\]
It satisfies \(A^3=I\); both \(A-I\) and \(A^2-I\) have determinant \(3\), a unit modulo \(2\) and modulo \(4\). Put \(r\) copies of \(A\) on \((C_4)^{2r}\), and \(2r\) copies on \((C_2)^{4r}\). Both kernels have order \(16^r\), both actions are fixed-point-free away from zero, and both semidirect products satisfy the theorem. The groups are nonisomorphic because their characteristic derived subgroups, which equal their respective kernels, have different exponents: \(4\) and \(2\). Their medial quotients are nonetheless isomorphic. When \(r=1\), \(k=5\), and the automorphism order is \(3^5\cdot5!\cdot 2=58\,320\).

## Verification
The companion standalone Python script `verify.py` constructs the original semidirect groups for six small prime-field cases, computes the smallest medial congruence by saturating the four-variable identities and the quandle congruence rules, compares the resulting multiplication tables with the theorem, and exhaustively counts the automorphisms of the first four small quotients. It additionally checks the isomorphism of the two distinct-kernel examples of order \(16\) on the nose at the multiplication-table level. Running `python3 verify.py` returned `VERIFY_OK`. These finite tests are consistency checks; the all-parameter theorem is proved by the arguments above.

## Relationship to prior work
Bardakov and Sangare (2026), Section 5, study universal medial quotients of conjugation quandles and derive general bounds. The derived-subgroup-orbit mechanism, including its previously recorded application to general groups, is not claimed as novel here. Cazet (2024), Theorem 3.4, computes automorphisms for quandles having one nontrivial column; it covers the closely related two-element-complement situation, which is excluded from the claimed new range. Salix and Wood (2025) give structural facts about inner groups for quandles with trivial columns and computational catalogues through order ten. None of those inspected sources provides the full \(m\ge3\) semidirect normalizer formula or the explicit infinite pair of nonisomorphic Frobenius-group families sharing a medialization. The full automorphism computation uses the standard normalizer of a regular-cycle permutation; no novelty is asserted for that standalone permutation-group lemma.

## Limitations
The result requires a finite abelian kernel and a cyclic complement whose nonidentity powers are all fixed-point-free. The universal medial quotient forgets much group structure and cannot be used to reconstruct the kernel. The formula is not a classification of all conjugation-quandle quotients of arbitrary finite groups, nor of arbitrary medial quandles. The claim of priority is restricted to the combined explicit quotient, group structure and infinite collision phenomenon; older formulations through permutation quandles may implicitly entail some of these facts.

## References
- V. G. Bardakov and B. Sangare, *Constructions and automorphisms of quandles*, arXiv:2610.18676v1 (publicly submitted 13 October 2026), especially Section 5.
- N. Cazet, *Quandles with one non-trivial column*, arXiv:2303.15815v3 (2024), especially Section 3 and Theorem 3.4.
- Q. J. M. Salix and P. P. Wood, *More Automorphism Groups of Quandles*, arXiv:2510.26673v1 (2025).
