# The sharp second-extremal Fibonacci gap for binary shortest absent subsequences

## Finding
Fix the binary alphabet \(\{0,1\}\). For a finite word \(w\), let \(\operatorname{SAS}(w)\) be the set of shortest words that are **not** subsequences (order-preserving scattered subwords) of \(w\), and put \(s(w)=|\operatorname{SAS}(w)|\). Let \(F_0=0\), \(F_1=1\), and \(F_{r+2}=F_{r+1}+F_r\) for integers \(r\geq0\).

**Theorem.** For every integer \(m\geq5\), among all binary words of length \(2m\), the largest value of \(s\) is \(F_{m+3}\), attained by exactly two words. The **second-largest distinct value** is
\[
\boxed{F_{m+3}-F_{m-2},}
\]
attained by exactly **four** words. Consequently, no word has a shortest-absence count strictly between these two values.

The two maximizers have the form \(B_1\cdots B_m\), where each block \(B_i\) is \(01\) or \(10\), and the blocks alternate between these two possibilities. The four second-place words have the same two-letter blocks, with exactly one adjacent **equal-block** boundary; that boundary is either between blocks \(2\) and \(3\) or between blocks \(m-2\) and \(m-1\), and all other adjacent blocks differ. Either initial block is allowed. These four words are distinct for all \(m\geq5\).

A stronger defect formula holds. If a two-letter-block word has exactly one equal-block boundary after block \(j\), where \(1\leq j\leq m-1\), then
\[
s(w)=F_{m+3}-F_jF_{m-j}.
\]
More generally, correcting any equal-block boundary to a differing-block boundary while preserving all other block-equality relations **strictly increases** \(s(w)\).

For example, at length \(10\) the largest value is \(21\), and the second is \(19\), attained by the four block orientations \(01001\), \(01101\), \(10010\), and \(10110\), with digit \(0\) denoting block \(01\) and digit \(1\) denoting block \(10\). These orientation strings are encodings of words, not the words themselves.

## Assumptions and scope
The alphabet is fixed to two symbols and length is exactly \(2m\). A subsequence need not occupy consecutive positions. Repeated occurrences of the same subsequence count once. For words containing both symbols, the universality index \(\iota(w)\) is the greatest \(k\) for which every binary word of length \(k\) is a subsequence. Hence all shortest absent subsequences have length \(\iota(w)+1\). A unary word has only one missing length-one binary subsequence under the fixed-alphabet convention, so it cannot attain either extremum in the theorem. The four extremizers are classified as literal ordered words, not modulo reversal or symbol complementation.

## Proof
**1. Reduction to minimal two-letter arches.** A binary *arch* is a shortest nonempty prefix of a remaining suffix containing both letters. It consists of one or more copies of a letter followed by the other letter. Greedily stripping arches gives exactly \(\iota(w)\) arches: each arch can supply any one letter, so their concatenation is that many-universal; conversely, choosing at each stage the symbol not yet seen in the current arch forces any missing next arch and shows that a larger universality index is impossible. One can equivalently verify this using greedy subsequence matching.

If \(\iota(w)=k\), select from each arch one copy of its initial letter and its final, opposite letter. The resulting subsequence \(u\) has length \(2k\), is a concatenation of \(k\) mixed pairs \(01\) or \(10\), and is itself \(k\)-universal but not \((k+1)\)-universal (it contains only \(k\) copies of each symbol). Because \(u\) is a subsequence of \(w\), every length-\(k+1\) word absent from \(w\) is absent from \(u\). Thus \(s(w)\leq s(u)\). In particular, any binary word of length \(2m\) with \(\iota(w)\leq m-1\) satisfies \(s(w)\leq\max_{u\in\mathcal P_{m-1}}s(u)\), where \(\mathcal P_t\) consists of the words made from \(t\) mixed pairs.

If \(\iota(w)=m\) and \(|w|=2m\), every arch has the minimum length two and there is no remainder. Thus \(w\in\mathcal P_m\). This is the intrinsic reason that the pair-structured words are not an arbitrary subclass: they are **all** shortest possible binary \(m\)-universal words.

**2. Exact suffix recurrence.** Write \(w=B_1\cdots B_m\in\mathcal P_m\), with \(B_j=a_j(1-a_j)\). Let \(E_j\) denote the number of shortest absent subsequences of the suffix \(B_j\cdots B_m\), for \(1\leq j\leq m\), and put \(E_{m+1}=2\) for the empty suffix. Let \(O_j\) count the shortest absent subsequences of the suffix that starts at the **second** symbol of \(B_j\) and continues through \(B_m\). Each complete mixed pair supplies every single letter as a subsequence. Consequently the shortest absent length for \(E_j\) is \(m-j+2\), and for \(O_j\) it is \(m-j+1\). The second assertion follows by greedy matching: the letter \(a_j\) must next be read in block \(j+1\), while choosing the available second letter \(1-a_j\) immediately leaves an entire mixed-pair suffix and costs one extra position of the target word.

At the last block, \(O_m=1\), \(E_m=3\), and \(E_{m+1}=2\). For \(1\leq j<m\), greedy matching of the first desired letter gives the exact recurrences
\[
E_j=E_{j+1}+O_j,
\qquad
O_j=\begin{cases}
O_{j+1},&a_j=a_{j+1},\\
E_{j+2},&a_j\ne a_{j+1}.
\end{cases}
\]
Indeed, from the first position of a pair, either desired letter can be selected immediately or at its second position, both giving an absent word of optimal length. From the second position, a shortest absent word must start with the *other* letter; its next occurrence is at the first symbol of the next pair in the equal case, and at the second symbol of the next pair in the unequal case. There are no duplications between the branches because their first letters differ.

Eliminating \(O_j\), for \(j<m\) one obtains
\[
E_j=\begin{cases}
2E_{j+1}-E_{j+2},&a_j=a_{j+1},\\
E_{j+1}+E_{j+2},&a_j\ne a_{j+1},
\end{cases}
\qquad E_{m+1}=2,\ E_m=3.
\]
The sought value is \(s(w)=E_1\).

**3. Strict improvement by repairing a defect.** An *equal-block boundary* is an index \(j\in\{1,\ldots,m-1\}\) with \(a_j=a_{j+1}\). Its complement is an alternating boundary. Since the recurrence uses only these boundary types, every prescribed boundary-type vector has exactly two representing words, obtained by choosing the first block. In particular, changing just one boundary type is well-defined even though it may require complementing all later orientation symbols.

At any boundary, the alternative update for \(O_j\) compares \(O_{j+1}\) with \(E_{j+2}\). Always \(E_{j+2}>O_{j+1}\): in the final case this is \(2>1\), and otherwise \(O_{j+1}\) is either \(O_{j+2}\) or \(E_{j+3}\), whereas \(E_{j+2}=O_{j+2}+E_{j+3}\) with both terms positive. Hence changing an equal boundary to an alternating boundary strictly increases \(O_j\) and \(E_j\). The recurrence has nonnegative dependencies in \((E,O)\), and the positive increase in \(E_j\) propagates strictly backwards to \(E_1\). Therefore repairing a defect strictly increases \(s\). It follows that the only global maximizers within \(\mathcal P_m\) are the two fully alternating orientation words.

**4. Fibonacci maximum and one-defect gap.** In a fully alternating word, \(E_j=E_{j+1}+E_{j+2}\) at every boundary, with terminal values \(2,3\). Thus \(E_j=F_{m-j+4}\) and in particular \(E_1=F_{m+3}\).

Suppose exactly one boundary, after block \(j\), is equal rather than alternating. The two suffix values beyond this boundary agree with the alternating case. Replacing the alternating update \(E_j=E_{j+1}+E_{j+2}\) by \(E_j=2E_{j+1}-E_{j+2}\) lowers \(E_j\) by
\[
2E_{j+2}-E_{j+1}=F_{m-j}.
\]
All preceding boundaries are alternating, so the deficit propagates backwards by the Fibonacci recursion, multiplying by \(F_j\) at \(E_1\). Consequently the exact loss is \(F_jF_{m-j}\).

**5. Locating the sharp second value.** If a block word has more than one equal boundary, repairing all but one strictly increases its \(s\)-value. Thus the best nonalternating block word must have exactly one equal boundary and minimize \(F_jF_{m-j}\). If \(j=1\) or \(j=m-1\), this product is \(F_{m-1}>F_{m-2}\) for \(m\geq5\). For \(2\leq j\leq m-2\), the Fibonacci addition identity gives
\[
F_jF_{m-j}=F_{m-2}+F_{j-2}F_{m-j-2}\geq F_{m-2}.
\]
Equality holds exactly when \(j=2\) or \(j=m-2\), since Fibonacci numbers of positive index are positive. Those are distinct boundaries for \(m\geq5\), each having two choices of first block. This proves the exact second-highest value and the four-word classification within \(\mathcal P_m\).

**6. Excluding words with fewer arches.** The same repair argument gives \(\max_{u\in\mathcal P_k}s(u)=F_{k+3}\) for every positive integer \(k\). Therefore a length-\(2m\) word with \(\iota(w)\leq m-1\) has at most \(F_{m+2}\) shortest absent subsequences. For \(m\geq5\),
\[
F_{m+2}<F_{m+3}-F_{m-2}
\]
because \(F_{m+1}>F_{m-2}\). Unary words have at most one shortest absent subsequence under the fixed binary alphabet. Hence no word outside \(\mathcal P_m\) reaches the second-place value. The theorem follows.

## Verification
The accompanying standalone `checker.py` computes shortest absent lengths and counts by a greedy earliest-occurrence subsequence automaton, independently computes the mixed-pair recurrence, and for small cases directly enumerates absent words. It checks **all** pair-orientation strings for \(2\leq m\leq11\), verifies the theorem and the exact four maximizers for \(5\leq m\leq11\), and exhaustively checks **all** binary words of lengths \(10,12,14,16,18\). These tests support the proof but do not replace the infinite induction and Fibonacci inequalities.

## Relationship to prior work
Karandikar, Kufleitner, and Schnoebelen study the global index of Simon's subsequence congruence; their 2013 preprint motivates the importance of which scattered subwords are present but does not address a second-extremal count for a fixed word length. Hofman and Martens study language separability by short subsequences, not this extremal count. Kosche, Koß, Manea, and Siemer establish the combinatorics of shortest absent subsequences and extremality at fixed universality index, but do not specify the first strict gap below the binary length-extremum. Fleischmann and coauthors treat nearly universal words and computable counts of missing scattered subwords, but their section on general missing-count values does not classify the second-highest multiplicity at every even length. A public research record titled *Fibonacci extremals for shortest absent subsequences of binary words* establishes the maximum \(F_{m+3}\) for even lengths; its full mathematical statement and proof contain no theorem determining the second-largest distinct value or exactly four runner-up words. The **new** claim here is the sharp first deficit and complete equality classification, not the previously known Fibonacci maximum or the basic matrix recursion.

## Limitations
The theorem treats a fixed two-letter alphabet and even word lengths of at least ten. It does not determine the second-largest count at odd lengths, the full ranking below second place, or higher-alphabet analogues. Although the cited close results were inspected, an equivalent stability result under another term or an inaccessible earlier source is still a historical-priority risk. The theorem's classification is mathematical and has not received an independent external audit.

## References
1. P. Karandikar, M. Kufleitner, Ph. Schnoebelen, *On the index of Simon's congruence for piecewise testability*, arXiv:1310.1278, first publicly submitted 2013-10-03; *Information Processing Letters* 115 (2015), 515–519. https://arxiv.org/abs/1310.1278
2. P. Hofman, W. Martens, *Separability by Short Subsequences and Subwords*, ICDT 2015, DOI:10.4230/LIPIcs.ICDT.2015.230, published 2015-03-19. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICDT.2015.230
3. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1 (2021-08-31), notably section 3 and Proposition 3.21. https://arxiv.org/abs/2108.13968
4. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, D. Nowotka, *m-Nearly k-Universal Words -- Investigating Simon Congruence*, arXiv:2202.07981v1 (2022-02-16), section 4. https://arxiv.org/abs/2202.07981
5. *Fibonacci extremals for shortest absent subsequences of binary words*, public mathematical result record, 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28
