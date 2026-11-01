# A minimal ternary obstruction to simultaneous cyclic equalizability

## Finding

Three words may have identical Parikh vectors without being simultaneously cyclically equalizable. In particular, the length-three ternary words \(u=012\), \(v=021\), and \(w=120\) each contain exactly one occurrence of each symbol, but **no common-position insertion of identical blocks into all three words** can make the resulting words cyclic rotations of one another. This gives a counterexample over every alphabet containing at least three symbols and, by inserting a common block into the three words, at every length \(n\geq3\).

The obstruction follows from a general rotation-rigidity lemma: in the cyclic orbit of any finite word, all pairs of distinct rotations at Hamming distance exactly two exchange the *same unordered pair of symbols*. The three displayed words violate this necessary condition, because \((u,v)\) exchanges symbols \(\{1,2\}\), whereas \((v,w)\) exchanges \(\{0,1\}\).

The length and cardinality boundaries are sharp for a counterexample to Parikh-vector sufficiency over a ternary alphabet: every collection of length-at-most-two words having the same Parikh vector is already a collection of cyclic rotations; for any two words having the same Parikh vector, cyclic equalizability is known to hold over arbitrary finite alphabets [2]. The binary three-word case is not settled here.

## Assumptions and scope

A word of length \(n\) over an alphabet \(\Sigma\) is a sequence in \(\Sigma^n\). Let \(R_s z\) denote rotation by \(s\) positions of a word \(z\) of length \(N\), with all indices modulo \(N\). Its *Parikh vector* records the multiplicities of each alphabet symbol.

A simultaneous insertion into \(k\) length-\(n\) words selects \(n+1\) common insertion blocks \(b_0,\ldots,b_n\in\Sigma^*\) and replaces each \(a_1\cdots a_n\) by \(b_0a_1b_1a_2\cdots a_nb_n\). The words are *cyclically equalizable* if some such insertion makes them all members of one cyclic rotation orbit. The definition agrees with [1,2]; repeated simultaneous insertions combine into one such operation.

For two equal-length words at Hamming distance two with equal Parikh vectors, their *exchange pair* is the unordered pair of distinct letters occurring in the two mismatch columns. It is well-defined: the symbols in those two columns must be interchanged.

## Proof

**Lemma (two-mismatch rotation rigidity).** Fix a word \(z\in\Sigma^N\). There is at most one unordered symbol pair \(\{a,b\}\) that can occur as the exchange pair of two members of its cyclic rotation orbit at Hamming distance two.

*Proof.* Every pair of rotations can be rotated simultaneously so that the first is \(z\); simultaneous rotation preserves mismatch symbols. Thus it is enough to consider all pairs \((z,R_s z)\).

Suppose \(d_H(z,R_s z)=2\), and the exchange pair is \(\{a,b\}\). For any symbol \(c\), set \(f_c(i)=1\) when \(z_i=c\) and \(0\) otherwise, a length-\(N\) binary indicator vector. Since \(z\) and its rotation have the same symbol counts, the two mismatches swap \(a\) and \(b\). In particular, the vector \(D=R_s f_a-f_a\) has **exactly one entry \(+1\)**, exactly one entry \(-1\), and all other entries zero.

Suppose also \(d_H(z,R_t z)=2\), with exchange pair \(\{c,d\}\) different from \(\{a,b\}\). Choose a symbol \(e\) in the first pair but not in the second. By exchanging the names \(a\) and \(b\) if needed, the previous argument applies to \(e\) and gives \(D_e=R_s f_e-f_e\) with exactly one positive entry. Since \(e\) is not involved in the second exchange, \(R_t f_e=f_e\). Rotations commute, so

\[
R_t D_e=R_t R_s f_e-R_t f_e=R_s R_t f_e-f_e=D_e.
\]

However, \(t\not\equiv0\pmod N\), because the two words differ. A nonidentity cyclic coordinate shift cannot fix a vector having exactly one positive coordinate: it would have to fix that coordinate, whereas nonzero translations on \(\mathbb Z/N\mathbb Z\) fix no coordinate. This is a contradiction. Therefore the exchange pair is independent of the distance-two rotation pair. \(\square\)

**Theorem (counterexample).** Consider \(u=012\), \(v=021\), and \(w=120\). They have the common Parikh vector \((1,1,1)\). The two differences \((u,v)\) occur at positions two and three (one-indexed), interchanging \(1\) with \(2\). The two differences \((v,w)\) occur at positions one and three, interchanging \(0\) with \(1\). Hence the exchange pairs \(\{1,2\}\) and \(\{0,1\}\) differ.

Any simultaneous insertion leaves every original column aligned across the three words and adds identical columns. Consequently both original pairs still have Hamming distance exactly two, with their exchange pairs unchanged, regardless of inserted blocks or their length. If the extended words were all rotations of one another, they would belong to a single cyclic orbit and violate the lemma. Thus no such insertion exists. \(\square\)

Finally, every pair of words of length zero, one, or two with the same Parikh vector is cyclically equivalent (at length two, the only nontrivial permutation swaps the two positions). Hence no shorter counterexample exists. For any \(n\ge3\), append the **same** block of \(n-3\) occurrences of symbol \(0\) to all three words; the two mismatched pairs and their exchange symbols persist, yielding a counterexample of length \(n\) over the same ternary alphabet.

## Verification

The accompanying `verify.py` exhaustively enumerates all words over alphabets of cardinalities two, three and four through lengths 12, 10 and 8 respectively, checking the asserted exchange-pair uniqueness among every distance-two cyclic shift. It also checks the explicit triple and common-block extension through length 39. Its recorded output appears in `verification_output.txt` and ends in `ALL_FINITE_CHECKS_PASS`.

These finite checks only corroborate the proof. The lemma's all-length statement follows from the commuting-rotation indicator argument, not from exhaustion.

## Relationship to prior work

Shinagawa and Nuida [1, Section 6] posed the multiple-word equalizability question, including the binary three-word case. Thongjarast, Pasiphol and Ruangwises [2, Theorem 3] proved Parikh-vector sufficiency **for two words** over any finite alphabet, and [2, Section 7] explicitly asks whether sufficiency persists with three or more words. The present example answers that sufficiency question negatively for ternary (and larger) alphabets; it neither contradicts nor strengthens the two-word theorem, because the quantifier over the number of words changes. The present result is a necessary obstruction, not a complete multiple-word classification.

## Limitations

This theorem does **not** characterize every equalizable three-word family, prove impossibility for any binary three-word family, or determine minimum insertion length for families that are equalizable. The obstruction uses Hamming-distance-two exchange pairs and is silent when no such pairs exist. A negative bibliographic search cannot exclude an earlier independently known counterexample or equivalent orbit lemma; independent priority verification has not been performed.

## References

[1] K. Shinagawa and K. Nuida, *Cyclic Equalizability of Words and Its Application to Card-Based Cryptography*, arXiv:2507.04916v1, publicly posted 2025-07-07, https://arxiv.org/abs/2507.04916 ; Section 6, p. 9, on open multiple-word questions.

[2] S. Thongjarast, S. Pasiphol and S. Ruangwises, *Cyclic Equalizability Characterized by Parikh Vectors*, arXiv:2604.19504v1, publicly posted 2026-04-21, https://arxiv.org/abs/2604.19504 ; Sections 2–4 (definitions and two-word theorem) and 7 (explicit multiple-word open problem).
