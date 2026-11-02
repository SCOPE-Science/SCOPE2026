# Six rank-two theories of finite symmetric groups

## Finding

Let \(S_n\) be the group of permutations on \(n\) letters, for every integer \(n\ge1\). Regard it as a first-order relational structure with a named identity \(e\), equality and a ternary predicate \(R(a,b,c)\) interpreted as \(ab=c\). Then

\[
S_m\equiv_2 S_n\quad\Longleftrightarrow\quad
\begin{cases}
m=n\in\{1,2,3,4\},\quad\text{or}\\
5\le m,n\le7,\quad\text{or}\\
m,n\ge8.
\end{cases}
\]

Thus the family has exactly six quantifier-rank-two theories, with smallest representative degrees \(1,2,3,4,5,8\). In particular, rank-two equivalence stabilizes sharply at degree \(8\), while the three degrees \(5,6,7\) form one exceptional class.

## Assumptions and scope

Quantifier rank is the maximum nesting depth of quantifiers, not the number of quantifiers in the whole sentence. Both groups have the *same* relational signature \(\{e,R\}\), and \(R\) is ternary multiplication. The theorem does not apply to the language with a binary **function** symbol for multiplication: that language can express arbitrarily long fixed powers in quantifier-free formulas. The empty-letter symmetric group \(S_0\) is excluded; it is isomorphic to \(S_1\) if included.

## Proof

**1. Complete atomic reduction.** In a two-round Ehrenfeucht–Fraïssé game, after the two selections the only elements available in atomic formulas are the constant \(e\) and the selected pair \(x,y\). Every equality or multiplication atom involving these terms is determined, using cancellation and the group axioms, by the eight truth values

\[
 x=e,\quad y=e,\quad x=y,\quad x^2=e,\quad y^2=e,
 \quad x^2=y,\quad y^2=x,\quad xy=e.
\]

For example, \(yx=e\) is equivalent to \(xy=e\), and \(xy=x\) is equivalent to \(y=e\). For a fixed first selection \(x\), define its *extension profile* to be the set of eight-bit atomic signatures realized as \(y\) varies over the group. The two-round back-and-forth criterion says that two structures are equivalent exactly when the sets of extension profiles realized by first selections coincide. The criterion is bidirectional: after Spoiler chooses \(x\), Duplicator matches a first selection with the same profile, then matches any second selection's atomic signature in the opposite structure.

**2. Universal profiles for degrees at least five.** Encode the eight conditions above from left to right as bits \(0,\ldots,7\), and write the signature as the sum of their powers of two. For any \(n\ge5\), the possible profiles of \(x\in S_n\) are *exactly* the following table, retaining only rows actually represented in the group:

| Type of \(x\) | Extension signatures |
| --- | --- |
| identity | 9, 89, 255 |
| involution, not a square | 8, 24, 58, 156 |
| involution, a square | 8, 24, 58, 72, 156 |
| order three | 0, 4, 16, 18, 64, 224 |
| order four, not a square | 0, 4, 16, 18, 48, 128 |
| order four, a square | 0, 4, 16, 18, 48, 64, 128 |
| other order at least five, not a square | 0, 4, 16, 18, 32, 128 |
| other order at least five, a square | 0, 4, 16, 18, 32, 64, 128 |

Here a square means an element of the form \(y^2\), not the square \(x^2\) of the element in question. In the row labelled “other”, the element's order is at least five; the order-three and order-four rows are treated separately. The table is a complete atomic calculation, not a table of experimental probabilities.

To verify each row, note that \(y=e\), \(y=x\), \(y=x^{-1}\), and \(y=x^2\) give the mandatory special signatures; repeated selections are allowed. A transposition distinct from these special values gives the generic involution signature, and a three-cycle distinct from the special values gives the generic non-involution signature. In degree at least five there are sufficiently many transpositions and three-cycles to make both choices. A further signature with bit 6 appears precisely when \(x\) has a square root other than the already counted special possibilities. For an element of order three, such an additional root always exists in degree at least five: with two fixed letters multiply \(x^{-1}\) by their transposition; otherwise \(x\) has at least two three-cycles, which can be interlaced into a six-cycle square root. For an element of order at least four, a root, if one exists, cannot equal \(x\), \(x^{-1}\), or \(x^2\). The order-four case is singled out because its square \(x^2\) is a nonidentity involution. These observations yield every signature in the table, and the eight atomic comparisons show there are no others.

**3. Cycle arithmetic and the sharp threshold.** A permutation has a square root in its symmetric group if and only if it has an even number of cycles of *each even length*. Necessity follows because the square of an even cycle splits into a pair of equal cycles. For sufficiency, pair all even-length cycles and interlace each pair into a cycle of twice that length; each odd cycle is squared by taking the appropriate power.

For every \(n\ge5\), all seven types other than “order four, a square” are realized: use respectively the identity, a single transposition, a pair of disjoint transpositions, a three-cycle, a four-cycle, a disjoint three-cycle and transposition, and a five-cycle (with fixed points where necessary). An order-four permutation must contain a four-cycle; if it is a square, the number of four-cycles is even, so it needs at least eight letters. Conversely, the product of two disjoint four-cycles is a square, namely the square of their interlaced eight-cycle. Thus precisely seven profiles occur at each degree \(5,6,7\), and all eight profiles occur at each degree \(n\ge8\). By Step 1 this proves both infinite equivalence classes without any finite extrapolation.

**4. Small degrees and separation.** Direct conjugacy-class calculations give respectively \(1,2,3,5\) distinct extension profiles in degrees \(1,2,3,4\). They are pairwise different and different from the larger-degree profile sets. The following nested rank-at-most-two existential properties independently distinguish consecutive classes (in each case the property first holds at the stated degree):

- Degree \(2\): existence of a nonidentity element.
- Degree \(3\): existence of a non-involution.
- Degree \(4\): existence of a nonidentity involution which has a square root.
- Degree \(5\): existence of a non-involution \(x\) with a square root \(y\) satisfying \(xy\ne e\).
- Degree \(8\): existence of an order-four element with a square root. Order four is expressible with outer \(x\) and a branch-quantified \(y\) satisfying \(R(x,x,y)\), \(y\ne e\), \(R(y,y,e)\); a separate branch-quantified \(z\) asserts \(R(z,z,x)\). Both branches sit inside one outer existential quantifier, so the sentence has rank two.

The last condition is not a single existential two-variable conjunction; separate inner quantifiers are essential. Combining the separations with the universal-profile argument proves the classification.

## Verification

The independent `check_atomic_reduction.py` directly computes all thirty-six equality and multiplication atoms for each ordered pair of permutations through degree six and confirms that the eight-bit reduction retains the complete atomic diagram. The standalone `check_exact.py` enumerates all permutations of degree at most nine and every second-round response for a representative of each conjugacy class. Its exact signature sets agree with the eight profile rows, give \(S_5\equiv_2S_6\equiv_2S_7\), and independently confirm \(S_8\equiv_2S_9\). The script checks all group elements as second moves, rather than sampling them. Its proof-independent finite computation is supplementary to Steps 1–3. The separate `check_cycle_types.py` uses integer partitions and the square-root parity theorem, not pair enumeration, to check the set of category realizations through degree fifty. Full executed outputs are included as `atomic.log`, `exact.log`, and `cycle.log`. Reproduce with `python check_atomic_reduction.py`, `python check_exact.py`, and `python check_cycle_types.py`, using Python 3.9 or newer and no third-party dependencies.

## Relationship to prior work

Nies and Tent, *Describing finite groups by short first-order sentences* (arXiv:1409.8390; first posted 2014-09-30), study lengths of first-order descriptions of finite groups and prove logarithmic/polylogarithmic compressibility results. Their paper's Introduction, Section 2 on group-power formulas, and the final results on permutation groups do not provide this fixed-rank classification. Bova and Martin, *First-Order Queries on Finite Abelian Groups* (CSL 2015, DOI 10.4230/LIPIcs.CSL.2015.41), prove a model-checking tractability theorem for finite **abelian** groups in a functional language; their group class, language, and conclusion differ. The present result instead asks for the complete rank-two equivalence partition of nonabelian symmetric groups with relational multiplication. Relevant low-rank permutation and finite-group terms were compared at the level of logical implications, not just titles; no covering classification was identified in the inspected sources.

## Limitations

The theorem concerns the family of symmetric groups, not arbitrary finite groups or the alternating subgroups, and rank two only. Low-rank statements in obscure or unindexed publications remain a residual historical-priority risk; no exhaustive search of the historical literature is claimed. The finite checks do not alone prove the infinite assertion; the cycle and game arguments do.

## References

1. A. Nies and K. Tent, *Describing finite groups by short first-order sentences*, arXiv:1409.8390 (first posted 2014-09-30), https://arxiv.org/abs/1409.8390.
2. S. Bova and B. Martin, *First-Order Queries on Finite Abelian Groups*, CSL 2015, LIPIcs 41, pp. 41–59 (2015-09-07), DOI:10.4230/LIPIcs.CSL.2015.41, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2015.41.
3. Standard Ehrenfeucht–Fraïssé two-round back-and-forth theorem and elementary permutation cycle-square decomposition; proofs of their specializations are supplied above.
