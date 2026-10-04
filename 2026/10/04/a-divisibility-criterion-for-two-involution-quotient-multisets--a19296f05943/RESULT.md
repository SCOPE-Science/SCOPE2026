# A divisibility criterion for two-involution quotient multisets
## Finding
Let \(G\) be a finite group and let \(s,t\in G\) be distinct involutions. Put \(n=\operatorname{ord}(st)\ge 3\), \(H=\langle s,t\rangle\), and \(m=[G:H]\). For \(0\le q\le |G|=2nm\), let \(A_q\) be the multiset containing \(q\) copies of \(s\) and \(2nm-q\) copies of \(t\). Then
\[
A_q	ext{ is quotient-realizable in }G \quad\Longleftrightarrow\quad n\mid q.
\]
In particular, for the dihedral subgroup \(H\cong D_{2n}\), the only quotient-realizable two-letter multisets of cardinality \(2n\) have \(0\), \(n\), or \(2n\) copies of \(s\).

## Assumptions and scope
A multiset \(A\) of cardinality \(|G|\) is quotient-realizable if there is a permutation \(\varphi\in\operatorname{Sym}(G)\) such that
\[
A=\{\varphi(x)x^{-1}:x\in G\}
\]
with multiplicity. The theorem assumes only that \(G\) is finite, \(s\ne t\), \(s^2=t^2=1\), and \(n=\operatorname{ord}(st)\ge3\). The conclusion concerns exactly the multisets supported on \(\{s,t\}\); it does not classify arbitrary quotient-realizable multisets in dihedral groups.

## Proof
Write \(r=st\). Since \(srs=r^{-1}\), the subgroup \(H=\langle s,t\rangle=\langle r,s\rangle\) is dihedral. Because \(r\) has order \(n\ge3\), the elements \(1,r,\ldots,r^{n-1},s,rs,\ldots,r^{n-1}s\) are distinct, so \(|H|=2n\).

First consider quotient-realizability inside \(H\). Aliabadi's cycle-tiling criterion says that a quotient-realizable multiset decomposes into simple product-one words whose partial-product sets tile the group by right translates. A simple product-one word over the alphabet \(\{s,t\}\) has only three possible forms. If two adjacent letters are equal, simplicity forces the whole word to be \((s,s)\) or \((t,t)\). Otherwise the word is cyclically alternating. An alternating word has even length \(2a\) and full product \((st)^a\) or \((ts)^a\), so product one forces \(n\mid a\). Simplicity gives length at most \(|H|=2n\), hence the only nontrivial alternating possibility has length exactly \(2n\), with \(n\) copies of each involution.

Thus a cycle-tiling of a two-letter multiset in \(H\) either contains one alternating word of length \(2n\), in which case the multiplicity of \(s\) is \(n\), or consists entirely of the two-letter words \((s,s)\) and \((t,t)\). In the latter case the tiles are sets \(\{x,sx\}\) or \(\{x,tx\}\). The left Cayley graph of \(H\) with generators \(s,t\) is a connected \(2\)-regular graph on \(2n\) vertices, hence the cycle \(C_{2n}\), with edge colors alternating between \(s\) and \(t\). A tiling by two-point tiles is therefore a perfect matching of \(C_{2n}\). An even cycle has exactly two perfect matchings, namely its two alternating edge classes, so all tiles have the same label. Hence the multiplicity of \(s\) is \(0\) or \(2n\). Conversely, these two cases are realized by the corresponding edge matching, while the alternating Hamiltonian word realizes multiplicity \(n\). Therefore a two-letter multiset of cardinality \(2n\) in \(H\) is quotient-realizable exactly for multiplicities \(0,n,2n\).

Now return to \(G\). Aliabadi's subgroup-support theorem states that a multiset of cardinality \(|G|\) supported in \(H\) is quotient-realizable in \(G\) if and only if it can be partitioned into \(m=[G:H]\) blocks of cardinality \(|H|=2n\), each quotient-realizable in \(H\). By the preceding paragraph, the number of copies of \(s\) in each block is \(0\), \(n\), or \(2n\). Therefore quotient-realizability implies \(n\mid q\).

Conversely, if \(n\mid q\), write \(q=nk\) with \(0\le k\le2m\). Every such \(k\) is a sum of \(m\) digits from \(\{0,1,2\}\): take as many \(2\)'s as possible, then one \(1\) if needed, and fill the remaining places with \(0\)'s. Choose the corresponding \(m\) quotient-realizable \(H\)-blocks with \(0\), \(n\), or \(2n\) copies of \(s\). Their disjoint multiset union is \(A_q\), and the subgroup-support theorem gives a quotient realization in \(G\). This proves the equivalence.

## Verification
The general argument above is symbolic; the finite computation is a stress-test, not an extrapolation. The standalone script `verify_dihedral.py` models \(D_{2n}\) exactly and, for each \(3\le n\le10\), enumerates all \(2^{2n}\) assignments of the labels \(s\) and \(t\) to the vertices. For each assignment it checks directly whether \(x\mapsto g_xx\) is a permutation, which is equivalent to quotient-realizability for a multiset supported on \(\{s,t\}\). In every tested case the only realized multiplicities are \(0,n,2n\). The script also checks, for \(1\le m\le6\), that sums of \(m\) block contributions \(\{0,n,2n\}\) are exactly the multiples of \(n\) between \(0\) and \(2nm\). The captured output ends with `VERIFY_OK`.

## Relationship to prior work
Aliabadi introduced quotient-realizability and proved the cycle-tiling criterion and the subgroup-support theorem. His Lemma 6.1 proves the base statement only for \(S_3\), where \(n=3\), obtaining multiplicities \(\{0,3,6\}\), and his Theorem 6.2 uses that case to construct an infinite family of obstructions. His Problem 7.7 asks for explicit tests for familiar families including dihedral groups.

A later paper on quotient-realizable multisets proves the \(D_8\) analogue, obtaining \(\{0,4,8\}\), and explicitly states that it does not treat groups of order larger than \(8\) and makes no claim on Problem 7.7. The theorem here gives the all-\(n\) two-involution pattern and, through subgroup support, the ambient-group divisibility criterion \(n\mid q\). It contains the \(S_3\) and \(D_8\) two-letter results as the cases \(n=3\) and \(n=4\), respectively.

## Limitations
The result treats only multisets supported on two distinct involutions and assumes \(\operatorname{ord}(st)\ge3\). It is not a classification of all quotient-realizable multisets in \(D_{2n}\), nor does it settle the full dihedral portion of Aliabadi's Problem 7.7. The novelty search found no broader statement with the same all-\(n\) divisibility criterion, but literature searches cannot prove absolute uniqueness; unindexed or unpublished work remains a residual risk.

## References
1. M. Aliabadi, *A nonabelian twist on differences of bijections*, arXiv:2605.16478v1, first submitted 15 May 2026; revised v2, 26 June 2026; *Utilitas Mathematica* 128 (2026), 375–397.
2. *Quotient-realizable multisets in a finite group: the classification in \(S_3\), counterexamples in \(D_8\) and \(Q_8\), and the abelianization obstruction in every finite nonabelian group*, Version 1, source snapshot 7 September 2026, https://ideosphere.ai/papers/quotient-realizable.
