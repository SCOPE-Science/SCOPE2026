# Derived-conjugacy medialization of conjugation quandles: symmetric and dihedral normal forms

## Finding
Let \(G\) be any group, and let \(Q=\operatorname{Conj}(G)\) denote its conjugation quandle, with \(x\triangleright y=y^{-1}xy\). Write \(G'=[G,G]\) for the derived subgroup. Then the universal medial quotient of \(Q\) is **exactly** the quandle of \(G'\)-conjugacy orbits of elements of \(G\):
\[
\operatorname{Conj}(G)^{\mathrm{med}}\cong G/G'_{\mathrm{conj}},\qquad
x\sim y\iff y=h^{-1}xh\text{ for some }h\in G'.
\]
Here \(G/G'_{\mathrm{conj}}\) means the set of conjugacy orbits for the conjugation action of \(G'\), **not** the quotient group \(G/G'\). Its operation is \([x]\triangleright[y]=[y^{-1}xy]\). When \(G\) is finite, its cardinality is
\[
\left|\operatorname{Conj}(G)^{\mathrm{med}}\right|=
\frac{1}{|G'|}\sum_{h\in G'}|C_G(h)|.
\]

For the symmetric group \(S_n\), \(n\ge3\), let \(p(n)\) be the number of partitions of \(n\), and let \(q(n)\) be the number of partitions into pairwise distinct odd parts. Let \(o(n)\) count partitions \(\lambda\vdash n\) with \(n-\ell(\lambda)\) odd, and set \(e(n)=p(n)-q(n)-o(n)\). The full medialized quandle has exactly \(p(n)+q(n)\) elements. It consists of \(q(n)\) distinguished two-element blocks, \(o(n)\) distinguished singleton elements, and \(e(n)\) other singleton elements. If \(\sigma\) swaps the elements of every two-element block and fixes the singletons, its complete operation is
\[
 a\triangleright b=\begin{cases}\sigma(a),&b\text{ is in the distinguished set of }o(n)\text{ singletons},\\ a,&\text{otherwise}.\end{cases}
\]
Consequently, its full quandle automorphism group is
\[
\operatorname{Aut}\!\left(\operatorname{Conj}(S_n)^{\mathrm{med}}\right)
\cong (C_2\wr S_{q(n)})\times S_{o(n)}\times S_{e(n)},
\]
with exact order \(2^{q(n)}q(n)!\,o(n)!\,e(n)!\). For the exceptional \(n=2\), the medialization is the trivial two-element quandle, whose automorphism group is \(S_2\). Its cardinality is \(p(2)+q(2)=2\). For \(n=1\), both groups and quandles are one-element.

For the dihedral group \(D_{2m}=\langle r,s\mid r^m=s^2=1,\ srs=r^{-1}\rangle\), \(m\ge3\), put \(g=\gcd(m,4)\). The medialization has \(m\) distinct rotation elements \(R_i\) (indices \(i\) modulo \(m\)) and \(g\) reflection elements \(T_j\) (indices \(j\) modulo \(g\)), with **complete operation table**
\[
\begin{aligned}
R_i\triangleright R_b&=R_i,&R_i\triangleright T_j&=R_{-i},\\
T_j\triangleright R_b&=T_{j-2b},&T_j\triangleright T_k&=T_{2k-j}.
\end{aligned}
\]
In particular, its cardinality is \(m+\gcd(m,4)\).

## Assumptions and scope
All statements concern groups with no finiteness assumption unless finite cardinalities are explicitly invoked. Quandles use **right** conjugation; the group convention is \(x^h=h^{-1}xh\), so \((x^a)^b=x^{ab}\). A medial quandle satisfies \((a\triangleright b)\triangleright(c\triangleright d)=(a\triangleright c)\triangleright(b\triangleright d)\). The medialization is the universal quotient imposing this identity. In the symmetric part, \(S_k\) is the usual symmetric group and \(C_2\wr S_k\) is the wreath product \((C_2)^k\rtimes S_k\); all factorials and partition counts are ordinary integers.

## Proof
**1. Derived-orbit congruence.** Let \(N=G'\), a normal subgroup of \(G\). Its conjugacy-orbit equivalence is stable under right conjugation: if \(x'\) is conjugate to \(x\) by \(n\in N\), then for each \(y\in G\), \((x')^y\) is conjugate to \(x^y\) by \(y^{-1}ny\in N\). Moreover, if \(y'=y^h\) for \(h\in N\), the conjugators \(y'\) and \(y\) have the same image in the abelian group \(G/N\); therefore the results of conjugating any \(x\) by them lie in the same \(N\)-orbit. This proves that both arguments of the operation respect the equivalence. The same argument applies to conjugation by \(y^{-1}\), so the quotient is a quandle.

**2. Mediality and minimality.** In the four-variable medial identity, the two outputs before quotienting are \(x^{y z^t}\) and \(x^{z y^t}\). Both conjugators map to the same product in the abelianization \(G/N\), so the outputs are in the same \(N\)-orbit. Thus the orbit congruence yields a medial quotient. Conversely, in *any* medial quotient, substituting \(t=1_G\) into the medial identity forces \(x^{yz}\sim x^{zy}\) for all \(x,y,z\in G\). Replacing \(x\) by a suitable conjugate shows \(u\sim u^{(yz)^{-1}zy}\) for every \(u\). These commutators generate \(N\); the equivalence is transitive, symmetric, and a quandle congruence, hence it also identifies \(u\) with \(u^h\) for every \(h\in N\). Therefore every medial congruence contains the \(N\)-orbit relation. The orbit congruence is exactly the universal medial congruence. For finite \(G\), Burnside's orbit-counting lemma applied to the action of \(N\) by conjugation gives the centralizer sum.

**3. Symmetric-group classes and operation.** For \(n\ge3\), \(S_n'=A_n\). The \(S_n\)-conjugacy classes correspond to partitions \(\lambda\vdash n\). Under \(A_n\)-conjugation, a class is either one orbit or two equal-size orbits, with splitting precisely when the centralizer of a representative contains no odd permutation. An even-length cycle supplies an odd centralizer element; swapping two cycles of the same odd length supplies another. Conversely, if all cycle lengths are odd and distinct, the centralizer is a product of cyclic groups generated by even permutations. Thus precisely the \(q(n)\) partitions into distinct odd parts split. They contribute \(2q(n)\) points; all other partitions contribute one, proving \(p(n)+q(n)\) total points.

Conjugation by any even permutation acts trivially on the \(A_n\)-orbit set. Conjugation by any odd permutation induces a common involution \(\sigma\), which swaps the two orbits above each split \(S_n\)-class and fixes every nonsplit class. A split class contains only even permutations (every odd-length cycle has even sign). An unsplit \(S_n\)-class is odd exactly when \(n-\ell(\lambda)\) is odd; these \(o(n)\) orbit elements have right translation \(\sigma\), and all other right translations are identity. This proves the stated complete operation.

For \(n\ge3\), \(q(n)>0\) (use the single part \(n\) when \(n\) is odd and the distinct odd parts \(n-1,1\) when \(n\) is even), and \(o(n)>0\) (use the partition corresponding to a transposition). Consequently, \(\sigma\neq 1\) and there exist right translations realizing it. A quandle automorphism must preserve the elements whose right translation is \(\sigma\) (the \(o(n)\) odd singletons), preserve the support of \(\sigma\) (the \(2q(n)\) paired points), and preserve the remaining \(e(n)\) singletons; on paired points it must commute with \(\sigma\). Conversely every such permutation respects all products. The centralizer of \(q(n)\) disjoint transpositions on their support is \(C_2\wr S_{q(n)}\), giving the full automorphism group and its order.

**4. Dihedral-group normal form.** The derived group of \(D_{2m}\) is \(\langle r^2\rangle\). It fixes each rotation under conjugation, while conjugating a reflection \(r^js\) by \(r^{2h}\) changes its index to \(j-4h\) modulo \(m\). Hence the reflection orbits are exactly the residues modulo \(g=\gcd(m,4)\). Direct evaluation of \((r^b)^{-1}(r^js)r^b\), \((r^ks)^{-1}(r^js)(r^ks)\), and the corresponding conjugations of rotations gives the four displayed operation rules. The orbit-count and all boundaries follow.

## Verification
The supplied standalone Python program `verify.py` constructs actual finite groups and their derived-orbit quotients, checks that the operation is representative-independent, and exhaustively checks the medial identity on these quotients. It verifies the partition and automorphism formulas for symmetric groups up to degree six; for degrees three through five it brute-force enumerates all automorphisms of the quotient operation table. It verifies dihedral groups for every \(m\) from three through sixteen, including all four operation rules. Executing `python3 verify.py` prints `VERIFY_OK`. The general proof does not rely on the finite enumeration.

## Relationship to prior work
Bardakov and Sangare (2026, Theorem 5.4) establish the mediality criterion for group conjugation quandles, two lower bounds for their medialized cardinalities, and the specific four-element medialization of \(\operatorname{Conj}(S_3)\). Their paper does not state the general derived-orbit identification or give the symmetric-group automorphism-group family and complete dihedral operation tables presented here. Bonatto and Stanovský (2020) provide the displacement-group/congruence framework for racks and quandles, including mediality in terms of abelian displacement groups and normal-subgroup orbit congruences; the general derived-orbit construction is closely related to that known framework and is not claimed as an independent foundational invention. The new contribution targeted here is the **complete concrete structure and automorphism count for the recent symmetric-group medialization problem, together with the dihedral normal form**; the group-theoretic orbit formula supplies their uniform explanation. Standard symmetric/alternating conjugacy-class splitting and Burnside's lemma are acknowledged ingredients, not claimed as new.

## Limitations
The general orbit statement may also be obtainable as a specialization of existing abstract displacement-group theory. The exact finite-family formulas have not been independently peer-audited, and literature search cannot exclude equivalent tabulations under alternative terminology. The symmetric-group operation and automorphism formula requires \(n\ge3\), with \(n=1,2\) treated separately. The dihedral presentation requires \(m\ge3\) to avoid degenerate conventions. No results about core quandles, nonconjugation rack families, link invariants, or higher universal quotient properties are asserted.

## References
1. V. G. Bardakov and B. Sangare, *Constructions and automorphisms of quandles*, arXiv:2610.18676v1 (first posted October 13, 2026), especially Theorem 5.4 and its proof, https://arxiv.org/abs/2610.18676.
2. M. Bonatto and D. Stanovský, *Commutator theory for racks and quandles*, arXiv:1902.08980v3 (2020), especially Sections 2–3 and displacement-group orbit congruences, https://arxiv.org/abs/1902.08980.
3. A. M. Aader, *Derivations on quandle algebras* (Master’s thesis, University of Tartu, 2023), especially Chapters 4–5. Earlier work on the same symmetric and dihedral conjugation quandles, but studying their quandle-algebra derivations rather than medialization.
4. Standard finite-group facts: conjugacy classes of symmetric groups correspond to cycle-type partitions; an \(S_n\)-class splits in \(A_n\) exactly for distinct odd cycle lengths. Burnside's orbit-counting lemma is used solely for the general finite cardinality formula.
