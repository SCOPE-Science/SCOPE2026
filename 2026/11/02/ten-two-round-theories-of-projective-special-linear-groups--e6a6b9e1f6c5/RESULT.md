# Ten two-round theories of projective special linear groups

## Finding
Let \(q\ge2\) run over prime powers, and let \(G_q=\operatorname{PSL}_2(\mathbb F_q)\). Interpret \(G_q\) as a relational first-order structure with equality, a constant \(e\) for the identity, and a ternary relation \(M(a,b,c)\) meaning \(ab=c\). For \(q\ge4\), define the four-bit fingerprint
\[
F(q)=(I_4(q),I_6(q),I_8(q),U(q)),
\]
where \(I_k(q)=1\) exactly when \(G_q\) has an element of order \(k\), and \(U(q)=1\) exactly when some element of order at least five has **no** square root in \(G_q\). These bits have explicit arithmetic expressions:
\[
\begin{aligned}
I_4(q)&=[q\text{ odd and }q\equiv\pm1\pmod 8],\\
I_6(q)&=[q\text{ odd and }q\equiv\pm1\pmod{12}],\\
I_8(q)&=[q\text{ odd and }q\equiv\pm1\pmod{16}],\\
U(q)&=[q\text{ odd and }q\ge11].
\end{aligned}
\]
Then, for all prime powers \(q,r\ge2\), the groups \(G_q,G_r\) agree on every sentence of quantifier rank at most two if and only if either \(q=r=2\), or \(q=r=3\), or \(q,r\ge4\) and \(F(q)=F(r)\). Consequently there are exactly **ten** two-round equivalence classes, with least field-size representatives
\[
\boxed{2,3,4,7,11,17,19,23,41,47}.
\]
Every \(G_q\) is two-round equivalent to a group in this family of order at most \(\lvert G_{47}\rvert=51\,888\), and this representative bound is sharp within the family.

## Assumptions and scope
The result concerns finite fields of all prime-power orders, the **relational** multiplication signature above (not a binary multiplication function symbol), ordinary unrestricted first-order sentences, and quantifier **rank** two (not two-variable logic at unbounded rank). The least representatives are chosen by field order; they are not asserted minimal among arbitrary finite groups.

## Proof
**Step 1: a general two-point diagram lemma.** Suppose \(G\) is a group with identity \(e\). For selected \(x,y\), the atomic diagram of the named triple \(e,x,y\) is completely determined by which of \(e,x,y\) coincide, together with the predicates
\[
x^2=e,\quad y^2=e,\quad y=x^2,\quad x=y^2,\quad xy=e.
\]
Indeed, for nonidentity distinct \(x,y\), multiplication among \(e,x,y\) can land in the named triple only via those equations: \(xy=x\) forces \(y=e\), \(xy=y\) forces \(x=e\), and \(yx=e\) is equivalent to \(xy=e\). The same elementary cancellation handles coincidences. With one selected element, its atomic data record whether it is the identity or an involution. The two-round Ehrenfeucht–Fraïssé criterion says that the group theory to rank two is completely determined by the **set of one-move extension diagrams** over each possible first choice, and the set of these rooted diagram sets. This criterion follows directly by allowing the first player to choose either structure and the second player to choose a response in either structure.

**Step 2: rooted diagram profiles under mild abundance.** Assume \(G\) has at least four elements of order three, at least two involutions, and at least one element of order at least five. For any first chosen \(x\), the rooted diagram set has the following forms:

1. \(x=e\): a fixed identity profile (nontrivial elements include involutions and non-involutions).
2. \(x\) an involution: a fixed profile indexed by whether \(x\) has a square root (equivalently, whether an element of order four squares to \(x\)).
3. \(x\) of order three: a fixed profile indexed by whether it has a square root other than \(x^{-1}\), equivalently a root of order six.
4. \(x\) of order four: a fixed profile indexed by whether it has a square root, equivalently a root of order eight.
5. \(x\) of order at least five: two possible profiles, according as \(x\) has a square root or not.

This is an exhaustive examination of the equations in Step 1. The responses \(y=e,x,x^{-1},x^2\), an involution, and (where available) a square root realize all exceptional cases. A remaining non-involutory generic response can always be taken among the at least four order-three elements, avoiding \(x\) and \(x^{-1}\), and in the exceptional order-three case avoiding those two; such a response is never a square root of a first element of order at least five. If necessary for \(x\) of order three, a different order-three element avoids both prescribed elements. The available involutions likewise supply an involutory generic response when \(x\) is itself an involution. No further atomic patterns can occur. Distinct profiles on this list are distinct as sets of **complete** atomic diagrams (e.g. witness square, inverse-square, an involutory square, a square root, or failure of a square root). Hence the entire two-round theory is determined by the occurrence of these rooted profiles, rather than by their multiplicities.

**Step 3: element orders and roots in \(\operatorname{PSL}_2\).** Standard Jordan form gives the elements of \(G_q\) as the identity, unipotent elements of characteristic order \(p\), and semisimple elements lying in cyclic split or nonsplit maximal tori, whose respective orders are
\[
L_-=(q-1)/d,\qquad L_+=(q+1)/d,\qquad d=\gcd(2,q-1).
\]
Every divisor of either torus order occurs, and the centralizer of a semisimple element of order greater than two is its torus. Thus if \(x\) is semisimple of order greater than two, every square root of \(x\) belongs to that cyclic torus. Every odd-order element has a square root in its own cyclic subgroup. A unipotent element of odd characteristic also has a square root in its cyclic subgroup. In characteristic two, all semisimple orders are odd and unipotents have order two.

For \(q\ge4\), the group has at least four elements of order three and two involutions. It also has an element of odd order at least five: in even characteristic use the torus of order \(q+1\); for odd \(q\ge9\) use the odd member of the two consecutive torus orders; at \(q=5,7\) use unipotent elements. The elementary size estimates from the conjugacy classes (or direct inspection of \(G_4\cong A_5\)) give the stated abundance. All involutions are conjugate in \(G_q\), so their common square-root status is precisely existence of order four. All order-three elements have the same extra-square-root status: if \(p=3\) they are unipotent with no roots of order six; otherwise they occupy the unique torus type divisible by three and have a root of order six exactly when that torus order is divisible by six. All order-four elements have the same square-root status, determined by divisibility of the unique even torus by eight.

For odd \(q\), exactly one of \(L_-\) and \(L_+\) is even. That even order is at most four for \(q=5,7,9\), and is at least six for odd prime powers \(q\ge11\). An even torus of order at least six contains an element \(x\) of order at least five that is not a square in its torus (take a generator). By the centralizer statement it is not a square in \(G_q\). Conversely, if every torus's even order is at most four, no element of order at least five fails to be a square. The same conclusion follows in even characteristic. This proves the formula for \(U(q)\). Divisibility of the even torus by four, six, and eight gives the congruence formulas for \(I_4,I_6,I_8\). Combining Step 2 proves the claimed fingerprint criterion for \(q,r\ge4\).

**Step 4: the two exceptional smallest fields.** \(G_2\cong S_3\) has only two nonidentity non-involutions; for a chosen order-three element its sole other non-involution is its inverse. In \(G_3\cong A_4\), a chosen order-three element has another order-three response outside its inverse pair. This distinguishes their two-round rooted diagrams. Neither has elements of order at least five, distinguishing both from every \(G_q\) with \(q\ge4\). Each has its own two-round class.

**Step 5: exact number and sharp bound.** Among \(q\ge4\), precisely two fingerprints have \(U=0\), realized by \(q=4,7\). For \(U=1\), the constraint \(I_8\le I_4\) leaves six logically possible triples \((I_4,I_6,I_8)\), realized in order by \(q=19,11,41,23,17,47\). These statements follow by evaluating the displayed congruences on the listed prime powers. The six fingerprints are distinct, and no other pattern is possible. Adding \(q=2,3\) gives ten classes. Explicit inspection of prime powers below each representative (or the congruence restrictions) establishes minimality. In particular the joint conditions \(I_6=I_8=1\) first hold at \(q=47\), so any set of representatives **within this family** must contain a group of order at least \(\lvert G_{47}\rvert=47(47^2-1)/2=51\,888\). This is attained.

## Verification
The included source `verify.cpp` enumerates the determinant-one matrices over the indicated prime and small extension fields and quotients by their scalar center. For every ordered group-element pair, it computes the complete equality and ternary-multiplication atomic diagram; for every first element, it forms the exact set of possible second-round diagrams. It then compares the complete sets of rooted diagram strings, **not just digest values**. `verify.py` compiles and invokes this exhaustive test for seventeen field sizes from two through thirty-one, including nonprime powers four, eight, nine, sixteen, twenty-five, and twenty-seven. It verifies all pairwise predicted equivalences/inequivalences **among the tested structures**. Reproduce with `python3 verify.py` in a directory containing the two source files; the recorded output is `verification_output.txt`.

The tests do not cover every finite field or the larger least representatives \(41\) and \(47\). Those cases and the infinite classification are established by the symbolic proof, not by computational extrapolation. The C++ finite-field implementation is intended as an additional consistency check rather than a machine-checked proof of the uniform Jordan-form and logical lemmas.

## Relationship to prior work
Garion's work on \(\operatorname{PSL}_2(q)\) develops the exact split, nonsplit, and unipotent element-order data needed in Step 3 in pursuit of Beauville structures, not quantifier-rank-two equivalence classes. Gomaa studies first-order descriptive complexity for finite **abelian** groups. Grochow and Levet study semisimple-group identification using **generalized binary quantifiers**, a different and stronger logical game, and do not provide this ordinary two-round classification. The new claim is a finite-model-theoretic classification derived from classical group structure, not a claim that the component order formulas are new.

## Limitations
The conclusions do not apply to functional group signatures, higher quantifier rank, or unrelated finite simple groups. The literature comparison is not a proof of priority: a logically equivalent formulation in historical or unindexed work could exist. This work has not undergone independent scientific validation.

## References
- S. Garion, *On Beauville Structures for PSL(2,q)*, arXiv:1003.2792 (first version 14 March 2010), especially Sections 3.2–3.3. Open preprint: https://archive.mpim-bonn.mpg.de/2141/1/preprint_2010_30.pdf.
- W. Gomaa, *Descriptive Complexity of Finite Abelian Groups*, International Journal of Algebra and Computation 20 (2010), 1087–1116, DOI:10.1142/S0218196710006047.
- J. A. Grochow and M. Levet, *On the Descriptive Complexity of Groups without Abelian Normal Subgroups*, arXiv:2209.13725, subsequently Logical Methods in Computer Science 21 (2025), 20:1–29.
