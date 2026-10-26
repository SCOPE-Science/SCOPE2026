# Six two-round theories of finite symmetric groups and the sharp eight-letter threshold

## Finding

Let \(S_n\) be the full symmetric group on \(n\ge1\) letters, in the first-order **relational** group language \(\{e,R\}\), with the identity constant \(e\), equality, and ternary relation \(R(a,b,c)\) interpreted as \(ab=c\). Write \(G\equiv_2 H\) when the structures satisfy exactly the same first-order sentences of quantifier rank at most two. The complete classification is

\[
S_m\equiv_2 S_n\quad\Longleftrightarrow\quad
\tau(m)=\tau(n),\qquad
\tau(n)=\begin{cases}n,&1\le n\le4,\\5,&5\le n\le7,\\8,&n\ge8.\end{cases}
\]

Thus this infinite family has exactly **six** rank-two theories, represented by \(S_1,S_2,S_3,S_4,S_5,S_8\). A representative has at most \(8!=40{,}320\) elements, and that is the sharp bound among members of the family. In particular, \(S_5\equiv_2S_7\), yet \(S_7\not\equiv_2S_8\).

The last separation is witnessed by the two-quantifier-rank sentence

\[
\varphi_8:=\exists x\,\Bigl[
 \exists y\,\bigl(R(x,x,y)\land y\ne e\land R(y,y,e)\bigr)
 \ \land\ \exists z\,R(z,z,x)\Bigr].
\]

The first conjunct says that \(x\) has order four; the second says that \(x\) is a square. If \(z^2=x\) has order four, then \(z\) has order eight, impossible in \(S_7\); an eight-cycle in \(S_8\) provides the witness.

## Assumptions and scope

The language contains **no binary multiplication function**, no inverse function, and no named generators. Quantifier rank, not total number of quantifiers or prenex-prefix length, is measured: a conjunction of separate existential subformulas has rank the maximum of their ranks. Consequently \(\varphi_8\) has rank two, while its equivalent prenex form need not. All quantifiers range over **group elements** (permutations). The classification ranges over every positive integer degree, including the trivial group \(S_1\). It does not concern unrestricted elementary equivalence, the functional group language, or pebble counting logic.

## Proof

**1. Atomic two-variable diagrams.** For fixed elements \(x,y\) in an arbitrary group, every atomic formula in variables \(x,y\), the constant \(e\), and \(R\) is determined by these eight truth values:

\[
\begin{gathered}
x=e,\qquad y=e,\qquad x=y,\qquad x^2=e,\qquad y^2=e,\\
x^2=y,\qquad y^2=x,\qquad y=x^{-1}.
\end{gathered}
\]

Indeed, a product containing \(e\) reduces to equality; a mixed product equal to \(e\) asserts that \(y=x^{-1}\); mixed products equal to one of their factors force the other factor to equal \(e\); a product equal to the same factor reduces similarly. The remaining cases are the displayed squares. All equality atoms reduce to the first three values.

In the two-round Ehrenfeucht–Fraïssé game, after the first choice \(x\), the second player must match precisely the **set** of obtainable eight-bit atomic diagrams as \(y\) varies. Hence two groups have the same rank-two theory precisely when the sets of these pointed extension profiles, as \(x\) varies, coincide. Both directions follow by back-and-forth (or by the finite disjunction of atomic diagrams describing each possible second move).

**2. A universal eight-type list above degree four.** For any \(n\ge5\), the pointed extension profile of \(x\in S_n\) is determined by one of the following eight mutually distinct categories:

| Type | Characterization |
| --- | --- |
| \(E\) | \(x=e\) |
| \(I_-\) | \(x\) has order two, is not a square |
| \(I_+\) | \(x\) has order two, is a square |
| \(C_3\) | \(x\) has order three |
| \(C_{4,-}\) | \(x\) has order four, is not a square |
| \(C_{4,+}\) | \(x\) has order four, is a square |
| \(H_-\) | \(x\) has order at least five, is not a square |
| \(H_+\) | \(x\) has order at least five, is a square |

To establish sufficiency and distinctness directly, enumerate the potentially exceptional second choices \(y=e\), \(y=x\), \(y=x^2\), \(y=x^{-1}\), and square roots satisfying \(y^2=x\). These determine all non-generic eight-bit diagrams. The relations among the first four choices depend only on whether \(x=e\), its order is two, three, four, or at least five; the existence of the extra square-root diagram depends on whether \(x\) is a square. For \(x\) of order three, \(x^{-1}\) itself is a square root, so one must additionally establish a square root **different** from \(x^{-1}\). Such a root always exists at degree at least five: if \(x\) has just one three-cycle, multiply its inverse by a transposition of two fixed letters; if it has at least two three-cycles, merge two such cycles into a six-cycle square root and invert the remaining three-cycles.

A genuinely generic involution \(y\) is obtained by a transposition distinct from \(x\) when \(x\) itself is a transposition; the square \(x^2\) is always even, so cannot equal a transposition. A genuinely generic noninvolution \(y\) is obtained from a three-cycle different from the finitely many special three-cycles (there are at least twenty three-cycles in \(S_n\)). These realize the remaining diagrams. Reading off \(x=e\), \(x^2=e\), the diagrams for \(y=x^2\) and \(y=x^{-1}\), and the root diagram proves the eight profiles mutually distinct.

The square-root criterion for permutations states that a permutation is a square if and only if, for **each even cycle length**, the number of cycles having that length is even (Wilf, Theorem 4.8.1). For completeness: squaring an even-length cycle produces two equal-length cycles, so even cycles of the square occur in pairs. Conversely, pair all even cycles and interleave each pair to form the longer root cycle; invert the exponent of two modulo the lengths of individual odd cycles.

**3. Exactly which types occur.** For every \(n\ge5\), representatives for seven types are, respectively, the identity; a single transposition; two disjoint transpositions; a three-cycle; a four-cycle; a three-cycle multiplied by a disjoint transposition; and a five-cycle. Additional letters are fixed. The square-root criterion yields the required signs. A square element of order four requires an even number of four-cycles (at least two), hence at least eight moved letters, and conversely the product of two disjoint four-cycles is such an element. Thus

\[
\{\operatorname{type}(x):x\in S_n\}=
\begin{cases}
\{E,I_-,I_+,C_3,C_{4,-},H_-,H_+\},&5\le n\le7,\\
\{E,I_-,I_+,C_3,C_{4,-},C_{4,+},H_-,H_+\},&n\ge8.
\end{cases}
\]

The game characterization proves equivalence throughout each indicated degree range.

**4. All six classes are different.** A separating sequence of rank-at-most-two sentences, true first at degrees \(2,3,4,5,8\), is:

\[
\begin{aligned}
\psi_2&:=\exists x\,(x\ne e),\\
\psi_3&:=\exists x\,(x\ne e\land\neg R(x,x,e)),\\
\psi_4&:=\exists x\,[x\ne e\land R(x,x,e)\land\exists y\,R(y,y,x)],\\
\psi_5&:=\exists x\exists y\,[R(x,x,y)\land y\ne e\land y\ne x
 \land\neg R(y,y,x)\land\neg R(y,y,e)],\\
\psi_8&:=\varphi_8.
\end{aligned}
\]

The third sentence detects an involution that is a square (equivalently, an element of order four). In the fourth, \(y=x^2\) and the four inequalities exclude element orders one through four; a five-cycle witnesses it in \(S_5\). The last detects a square of order four, equivalent to existence of an element of order eight. The five threshold truth patterns are successively \(00000\), \(10000\), \(11000\), \(11100\), \(11110\), and \(11111\). This separates the six listed classes and proves optimality of the largest class's smallest representative: degree eight and order \(8!=40{,}320\).

## Verification

The standalone programs `exact_symmetric.py`, `verify_symbolic.py`, and `verify_sentences.py` use Python's standard library. Run `python exact_symmetric.py --n9`, then `python verify_symbolic.py`, then `python verify_sentences.py`. `exact_symmetric.py` writes `exact_output.json` beside the script; its output and all other observed output are recorded in `verification.log`.

The first program explicitly enumerates all permutations for degrees one through nine (including \(S_9\) only for comparison), chooses each conjugacy-class representative as first move, and enumerates **all** possible second moves. It computes complete atomic diagrams, not only selected formulas. The second independently analyzes cycle partitions up to degree forty using square-root parity and the eight categories. The third independently evaluates all five displayed threshold formulas for degrees one through eight. All recorded checks passed. Their finite ranges corroborate, but do not replace, Steps 1–4's all-degree proof.

## Relationship to prior work

Gomaa's 2007 dissertation, *Model Theory and Complexity Theory*, Definition 3.1 and Chapter 3, uses precisely the relational group vocabulary \(\{e,R\}\) and measures quantifier depth through group Ehrenfeucht–Fraïssé games. Its substantive classifications and bounds focus on cyclic and other abelian groups, rather than the exact rank-two theories of the symmetric groups. Wilf's earlier square-root criterion supplies a **known** group-theoretic ingredient; the classification of pointed two-round logical profiles and sharp eight-letter collapse are the claims here. He's 2014 article studies strict quantifier-structure hierarchies for different finite structures, rather than the symmetric-group spectrum. Later work on group identification via other pebble games addresses different logical resources and need not imply this ordinary two-round classification.

## Limitations

The result applies only to the precise ternary relational signature, pure rank-two first-order logic, and finite symmetric groups. In the **functional** language with multiplication as a term-forming operation, a single quantifier can test arbitrarily long word identities, so no cross-signature inference is made. A search of accessible related literature and previous related claims found no implication covering the six-class statement, but inaccessible or unindexed earlier work could overlap. All verification is mathematical argument plus same-author computation; no independent external scientific audit has been performed.

## References

1. Walid Gomaa, *Model Theory and Complexity Theory*, PhD thesis, University of Maryland (2007), repository record dated 2007-07-06, handle `hdl:1903/7227`, https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440 ; full text https://drum.lib.umd.edu/bitstreams/5a564fe0-5c19-4da2-8ce0-2cc76964e427/download (Chapter 3, especially Definition 3.1 and Section 3.9).
2. Herbert S. Wilf, *generatingfunctionology*, second edition, Section 4.8, Theorem 4.8.1, https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/wilf.pdf .
3. Yuguo He, *On the Strictness of the Quantifier Structure Hierarchy in First-Order Logic*, Logical Methods in Computer Science 10(4:3) (2014), arXiv:1409.7488, https://arxiv.org/abs/1409.7488 .
4. Joshua Grochow and Michael Levet, *On the Descriptive Complexity of Groups without Abelian Normal Subgroups*, arXiv:2209.13725 (2022; later revisions), https://arxiv.org/abs/2209.13725 .
