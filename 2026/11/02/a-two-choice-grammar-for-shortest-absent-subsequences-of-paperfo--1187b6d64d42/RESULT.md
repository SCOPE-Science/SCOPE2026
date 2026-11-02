# A two-choice grammar for shortest absent subsequences of paperfolding prefixes

## Finding

Let \(p_n\) be the regular paperfolding word specified by the odd-part rule below. Every dyadic prefix of length \(2^k\), for \(k\ge4\), has a completely described *language* of shortest absent binary scattered subsequences, not just a count. Put \(m=2^{k-4}\), \(A=\{\mathtt{000011},\mathtt{001011}\}\) and \(B=\{\mathtt{001011},\mathtt{001111}\}\). For \(0\le j<m\) let \(L_j=A\) for even \(j\) and \(L_j=B\) for odd \(j\). Then

\[
\operatorname{SAS}(P_k)=L_0L_1\cdots L_{m-1}\{\mathtt0,\mathtt1\}.
\]

The products denote all independent concatenation choices. The largest subsequence-universality index is exactly \(6m\), the shortest absent length is \(6m+1=3\cdot 2^{k-3}+1\), and the number of shortest absent words is \(2^{m+1}=2^{2^{k-4}+1}\). For example, at prefix lengths \(16,32,64,128,256\), shortest absent lengths are respectively \(7,13,25,49,97\), and counts are \(4,8,32,512,131072\).

## Assumptions and scope

For positive integer \(n\), let \(\operatorname{odd}(n)=n/2^{\nu_2(n)}\), and let \(p_n=1\) when \(\operatorname{odd}(n)\equiv1\pmod4\), otherwise \(p_n=0\). Thus indexing begins at \(n=1\), and \(P_k=p_1\cdots p_{2^k}\). An occurrence of a binary word \(u=u_1\cdots u_h\) as a scattered subsequence in \(w\) consists of strictly increasing positions \(i_1<\cdots<i_h\) with \(w_{i_j}=u_j\). A shortest absent subsequence means an absent word of minimum length, not a minimal absent *factor* and not a shortest absent word subject to additional constraints.

## Proof

**1. Fixed sixteen-position block structure.** The odd-part rule yields a literal decomposition of \(P_k\) into \(m=2^{k-4}\) blocks of sixteen bits. With block index \(j\) beginning at zero, put \(e_j=1\) when \(j\) is even and \(e_j=0\) otherwise; put \(b_j=p_{j+1}\). Directly applying the odd-part rule at the sixteen offsets gives

\[
W_j=\mathtt{1101100}\ e_j\ \mathtt{1100100}\ b_j.
\]

Since \(m\) is a power of two, the final bit \(b_{m-1}=p_m=1\). This last-bit condition is essential for the terminal argument.

**2. Subsequence rank and next-occurrence dynamics.** Use zero-based suffix positions for the rest of the proof. For any finite binary word \(w\), let \(n=|w|\), let \(N_c(i)\) be the first position at or after \(i\) occupied by symbol \(c\), or \(n\) if none, and define \(r(i)\) to be the largest \(h\) such that every binary word of length \(h\) is a scattered subsequence of \(w[i:]\). Then \(r(n)=0\), and

\[
r(i)=\begin{cases}
0,&\max\{N_0(i),N_1(i)\}=n,\\
1+r(1+\max\{N_0(i),N_1(i)\}),&\text{otherwise}.
\end{cases}
\]

Indeed, a universal first symbol needs both letters and the worst first-symbol choice is the one whose first occurrence is later. This is the standard greedy universal-arch recurrence. At any position \(i\) with \(r(i)>0\), a next-matched symbol \(c\) decreases rank either by one or by zero: \(r(N_c(i)+1)\ge r(i)-1\). If rank does not fall at one of the first \(r(0)\) matched steps, then all remaining symbols of a proposed length-\(r(0)+1\) word can still be matched; therefore absence requires a rank drop at every one of the first \(r(0)\) steps. After exactly \(r(0)\) drops the remaining suffix has rank zero and the final letter is absent precisely when it does not occur there.

**3. A finite local transfer calculation.** Consider any concatenation of blocks \(W_j\) as displayed in Step 1, with alternating \(e_j\), arbitrary \(b_j\in\{0,1\}\), and terminal \(b_{m-1}=1\). Every nonterminal block is followed by a suffix beginning \(\mathtt{110}\), whereas the terminal block has empty continuation. Set \(R_j=r(16(j+1))\). Substitution of all two possible letters into the recurrence from Step 2 gives the *exact* relative ranks \(r(16j+s)-R_j\), in order for \(s=0,1,\ldots,16\):

| \((e_j,b_j)\) | Relative ranks, offsets \(0\) through \(16\) |
|---|---|
| \((1,0)\) | 6,6,6,5,5,4,4,3,3,3,2,2,2,1,1,1,0 |
| \((1,1)\) | 6,6,6,5,5,4,4,3,3,3,2,2,2,1,1,0,0 |
| \((0,0)\) | 6,6,6,5,5,4,4,4,3,3,2,2,2,1,1,1,0 |
| \((0,1)\) | 6,6,6,5,5,4,4,4,3,3,2,2,2,1,1,0,0 |

The rows are a small, finite recurrence calculation using the displayed sixteen-bit blocks, with terminal cases only when \(b=1\); they do not assume periodicity or a special value of later \(b\)'s. In particular \(r(16j)=6+R_j\). Descending induction starting from \(r(16m)=0\) gives \(r(0)=6m\).

For clarity, an independent finite calculation applying the *first-occurrence* transitions \(i\mapsto N_c(i)+1\), retaining exactly those with \(r\) lowered by one, produces the following complete six-transition table. At the beginning of block \(j\), the starting offset may be \(0\) or \(1\); both yield the identical sets. The row lists *all*, not merely selected, six-letter paths causing six rank drops:

| First-block symbol \(e_j\) | Exactly six rank-dropping symbols | Landing position after six transitions |
|---|---|---|
| \(1\) | \(\mathtt{000011},\ \mathtt{001011}\) | \(16(j+1)+1-b_j\) |
| \(0\) | \(\mathtt{001011},\ \mathtt{001111}\) | \(16(j+1)+1-b_j\) |

This calculation is obtained by exhaustively branching over the two possible next letters at each of just six steps, using the four rank rows above; at most \(2^6\) branches are examined in each of the eight cases \((e,b,\text{starting offset})\). Every transition is fixed by the given block and the first two letters of the following block; in the terminal case the endpoint is the word end because \(b=1\). It is independently reproduced and asserted in the bundled `checker.py`, which is not used as a replacement for the finite symbolic reduction.

**4. Concatenating the local paths.** Both local branches land at the same offset \(1-b_j\) in the next block, so the table can be iterated, with no compatibility restrictions among earlier choices. Every sequence of \(6m\) rank-decreasing next matches therefore consists of *exactly one* of the two six-letter words prescribed by \(e_j\) at each of the \(m\) blocks. Conversely every such concatenation gives \(6m\) rank drops. Because the final block has \(b_{m-1}=1\), both choices finish exactly at suffix position \(16m\). Neither \(0\) nor \(1\) then occurs: appending either produces a shortest absent word. All other candidate words of that length have a first prefix that failed to decrease rank and are consequently present. The products and cardinalities claimed in the Finding follow. \(\square\)

## Verification

The standalone Python 3 checker `checker.py` independently constructs the rank recurrence and all rank-dropping paths. It verifies the four seventeen-entry relative-rank rows, both possible starting offsets of each block, the complete six-transition alternatives, the exact absent languages, and the dyadic paperfolding decomposition. It exhaustively tests all \(255\) arbitrary terminal-one bit selections through eight sixteen-bit blocks, validates paperfolding dyadic ranks \(4\) through \(8\), and separately tests direct scattered-subsequence membership for *every* binary candidate word at lengths \(6m\) and \(6m+1\) for \(k=4,5\). The actual replay ended `VERIFY_OK 255 arbitrary-block words; all six-check stages passed`. The theorem for unbounded \(k\) follows from the block transfer proof, not the bounded computational tests. Run `python3 checker.py` with no dependencies.

## Relationship to prior work

Madill and Rampersad (2012, arXiv:1208.2856) investigate Abelian complexity of *contiguous factors* of the paperfolding word; their binary convention is complemented relative to the sequence defined here. Their full preprint concerns factor-count statistics, not the scattered absent language stated here. Kosche, Koß, Manea and Siemer (2021, arXiv:2108.13968) develop general absent-subsequence and arch-factorization theory and algorithms. Their general characterizations furnish a conceptual framework but do not by themselves specify the dyadic paperfolding language or its two-choice transfer law. The latter is supplied by the finite sixteen-position analysis above. Later general absent-subsequence enumeration algorithms (arXiv:2504.21471) may compute finite instances but do not establish this closed form by their abstract alone. These comparisons are scope comparisons, not a claim that every historical paper has been exhaustively examined.

## Limitations

The exact language is asserted only for complete dyadic prefixes of lengths \(2^k\), \(k\ge4\), and for the explicitly defined one-based paperfolding orientation. It does not concern contiguous minimal absent factors, arbitrary prefix lengths, or other orientations without appropriate bit complementation. The finite transfer rows are proven by direct recurrence calculation, supported by a checker, but independent mathematical validation has not been performed; historical priority cannot be guaranteed beyond inspected sources.

## References

- B. Madill and N. Rampersad, *The abelian complexity of the paperfolding word*, arXiv:1208.2856, first publicly posted 2012-08-14. https://arxiv.org/abs/1208.2856
- M. Kosche, T. Koß, F. Manea, and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (2021). https://arxiv.org/abs/2108.13968
- *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (2025). https://arxiv.org/abs/2504.21471
