# Exact minimum Italian-domination counts and a three-tile classification on ladders

## Finding
For each integer \(n\ge 2\), let \(L_n=P_2\square P_n\) be the two-row ladder with \(n\) columns. An Italian dominating function (IDF) labels each vertex in \(\{0,1,2\}\), with every zero-labeled vertex having neighbor-label sum at least \(2\). Denote the minimum labeling weight by \(\gamma_I\) and the number of IDFs attaining it by \(a_n\). Then
\[\gamma_I(L_n)=n,\qquad \sum_{n\ge2}a_nz^n=\frac{2z^2}{1-z-z^2-z^5}.\]
Consequently \(a_2,a_3,a_4,a_5,a_6=(2,2,4,6,10)\) and
\[ a_n=a_{n-1}+a_{n-2}+a_{n-5}\quad(n\ge7).\]
Every optimum has an explicit unique representation by an initial choice of one of the two rows and an ordered composition of \(n-2\) into parts from \(\{1,2,5\}\).

## Assumptions and scope
Graphs are finite, undirected, simple. The rows and columns of \(L_n\) are distinguishable; functions on the same graph related by a symmetry count separately unless identical. At a column, use the ordered pair of top and bottom labels \(s=(s_1,s_2)\in\{0,1,2\}^2\). For the left and right sentinel columns put \(s_0=s_{n+1}=(0,0)\). The requirement on a middle column \(s=(a,b)\) between columns \(p,t\) is exactly
\[F(p,s,t):=(a\ne0\ \lor\ b+p_1+t_1\ge2)\land(b\ne0\ \lor\ a+p_2+t_2\ge2).\]
It applies to all columns, including the two ends, because the missing horizontal neighbors there are zero sentinels.

## Proof
**Step 1: a finite local lower-bound certificate.** Write \(00,01,\ldots,22\) for the nine possible columns, and let \(\delta(s)=s_1+s_2-1\). For a pair of columns define the integer potential \(d(p,s)\) by
\[
 d(p,s)=\begin{cases}
 -2,&p=00,\ s\in\{12,21,22\},\\
 -1,&p=00,\ s\notin\{12,21,22\},\\
 -1,&p\in\{01,10\},\\
 0,&p\in\{02,11,12,20,21,22\}.
 \end{cases}
\]
The following finite lemma holds for all \(p,s,t\in\{0,1,2\}^2\):
\[ F(p,s,t)\Longrightarrow \delta(s)+d(p,s)-d(s,t)\ge0.\tag{1}\]
This is a complete \(9^3=729\)-case integer check, not an extrapolation: testing the displayed Boolean condition gives \(666\) admissible triples, and the displayed left-hand side is nonnegative on each. All operations and the exact exhaustive loops are provided in `verification/verify.py`.

A full IDF corresponds bijectively to a path of \(n\) allowed transitions
\[(s_0,s_1)\to(s_1,s_2)\to\cdots\to(s_n,s_{n+1}),\]
with \(s_0=s_{n+1}=00\). Put \(r_j=\delta(s_j)+d(s_{j-1},s_j)-d(s_j,s_{j+1})\ge0\). Telescoping gives
\[\operatorname{wt}(f)-n=\sum_{j=1}^n r_j+d(s_n,00)-d(00,s_1)\ge0,\]
since \(d(s_n,00)\ge-1\) and \(d(00,s_1)\le-1\). Thus \(\gamma_I(L_n)\ge n\).

**Step 2: all equality paths.** Equality holds exactly when every \(r_j=0\) and both endpoint potentials equal \(-1\). To reproduce the zero-cost transition classification, enumerate the same \(729\) triples, retaining those satisfying \(F\) and equality in (1), and trim states that are neither reachable from a permitted start \((00,s)\) nor able to reach a permitted end \((s,00)\). The full remaining transition table, written `previous/current -> permitted next-state(s)`, is:

```
00/00 -> (none)
00/01 -> 01/10
00/10 -> 10/01
00/12 -> 12/00
00/21 -> 21/00
01/00 -> 00/21
01/01 -> 01/10
01/10 -> 10/00, 10/01, 10/10
10/00 -> 00/12
10/01 -> 01/00, 01/01, 01/10
10/10 -> 10/01
12/00 -> 00/10
21/00 -> 00/01
```
The isolated state `00/00` contributes only an empty path and cannot represent an IDF with \(n\ge2\). The two nontrivial starts are `00/01` and `00/10`. Their next states are respectively \(A=(01,10)\) and \(B=(10,01)\). From \(A\) to \(B\), with no internal visit to \(A\) or \(B\), there are precisely three paths, of lengths \(1,2,5\), emitting the respective ordered column blocks
\[(10),\qquad(10,10),\qquad(10,00,12,00,10).\]
From \(B\) to \(A\) the same blocks occur with the two entries of each column exchanged. From \(A\), the terminal step emits `10`; from \(B\), it emits `01`. Conversely, the displayed transitions prove that these are all possible excursions and all endings.

Therefore an optimum is obtained uniquely by first choosing `01` or `10`, taking zero or more alternating excursion blocks of lengths in \(\{1,2,5\}\), and finally appending the terminal opposite one-unit column. The total number of columns is two plus the sum of excursion lengths. The construction always yields a valid IDF of weight \(n\), since every traversed edge has zero reduced cost and the endpoint potentials equal \(-1\). This also attains the lower bound, giving \(\gamma_I(L_n)=n\).

**Step 3: enumerate compositions.** If \(c_m\) is the number of ordered compositions of the nonnegative integer \(m\) into parts of sizes \(1,2,5\), including one empty composition of \(0\), then \(a_n=2c_{n-2}\). The first-part decomposition yields
\[\sum_{m\ge0}c_mz^m=\frac1{1-z-z^2-z^5},\]
which gives the claimed rational generating function, initial counts and recurrence.

## Verification
Run `python3 verification/verify.py` in a directory containing this result's two `verification` files. This independent, Python-standard-library checker exhaustively verifies all \(729\) local triples, their \(666\) feasible instances, all \(161\) zero-reduced-cost transitions, and the entire \(13\)-state trimmed graph (including the irrelevant isolated state). It then enumerates every actual vertex labeling for ladders \(2\le n\le6\), checks the minimum and its count, and independently uses an exact transfer count to verify the composition formula for all \(2\le n\le27\). See `verification/output.txt` for the recorded run. The universal proof rests on the complete finite local lemma and resulting symbolic path decomposition, not on a finite sample of ladder orders.

## Relationship to prior work
Gardner's 2018 thesis treats Italian domination on ladder graphs and establishes the scalar minimum \(\gamma_I(L_n)=n\) for \(n\ge3\) (Theorem 3.4). That value is credited here, and is also established independently by the present potential proof. The four-vertex ladder \(L_2=C_4\) already has the two minimum colorings counted by the cycle table of Shao and Zhao; no novelty is claimed for that individual base case. The substantive new statement is an all-orders enumeration and explicit bijective description of **every** minimizer on the ladder family. Shao and Zhao (public September 9, 2026) study Italian-domination weight enumerators for paths, trees, and cycles; their full text presents no ladder enumeration or this three-tile recurrence. Other published Roman \(\{2\}\)-domination enumerators for complete multipartite graphs concern structurally different graph families and do not yield this ladder coefficient. These are comparisons of stated mathematical results; lack of indexed matches is not a proof of worldwide uniqueness.

## Limitations
This is an exact result for ordinary two-row Cartesian ladders only; it does not determine the entire Italian domination polynomial, the corresponding problem for wider grids, or the number of perfect Italian dominating functions. The relevant ladder thesis was publicly indexed and its Theorem 3.4 excerpt examined, but its complete PDF could not be retrieved for whole-document comparison. Consequently an equivalent count concealed in that thesis or other unindexed literature remains a specific originality risk. No independent external validation has been performed.

## References
1. P. Shao and C. Zhao, *Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1, first public 2026-09-09. https://arxiv.org/html/2610.00108v1
2. B. Gardner, *Italian Domination on Ladders and Related Products*, East Tennessee State University M.S. thesis, 2018, Theorem 3.4. https://dc.etsu.edu/etd/3509/
