# Complete \(C_4\)-isolation polynomial and aspect-ratio transition for rook graphs

## Finding

For all integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\), with vertex set \([m]\times[n]\); two distinct cells are adjacent if they have the same row or the same column. A \(C_4\)-isolating set is a subset \(D\) for which \(R_{m,n}-N[D]\) has no *subgraph* isomorphic to a four-cycle (the cycle need not be induced). Write \(I_{m,n}(z)=\sum_{D\ C_4\text{-isolating}}z^{|D|}\).

Let \(Q_{a,b}(z)\), for nonnegative integers \(a,b\), count subsets of an \(a\)-by-\(b\) board meeting every row and every column:
\[
Q_{a,b}(z)=\sum_{i=0}^a\sum_{j=0}^b(-1)^{i+j}\binom ai\binom bj(1+z)^{(a-i)(b-j)}.
\]
Define \(\epsilon(r,c)=1\) exactly when
\[
r=0\quad\text{or}\quad c=0\quad\text{or}\quad(r=1\text{ and }c\le3)\quad\text{or}\quad(c=1\text{ and }r\le3),
\]
and \(\epsilon(r,c)=0\) otherwise. Then the **complete all-cardinality enumerator** is
\[
\boxed{I_{m,n}(z)=\sum_{a=0}^{m}\sum_{b=0}^{n}
\binom ma\binom nb\epsilon(m-a,n-b)Q_{a,b}(z).}
\]
All coefficients are nonnegative integers, as they count specified sets; alternating summands occur only in the inclusion-exclusion representation of \(Q_{a,b}\).

The exact minimum cardinality has an aspect-ratio transition:
\[
\boxed{\iota(R_{m,n},C_4)=\begin{cases}m-1,&m\le n\le m+2,\\m,&n\ge m+3.\end{cases}}
\]
Put \((x)_{\underline{k}}=x(x-1)\cdots(x-k+1)\), with \((x)_{\underline0}=1\), and let \(S(t,b)\) be a Stirling number of the second kind. The number \(T_{m,n}\) of minimum \(C_4\)-isolating sets is given by the following exhaustive five-case formula:
\[
\boxed{T_{m,n}=\begin{cases}
2m\displaystyle\sum_{b=\max\{1,m-3\}}^{m-1}\binom mb b!S(m-1,b)-m^2(m-1)!,&n=m,\\[2mm]
m\left((n)_{\underline{m-1}}+\binom{m-1}{2}(n)_{\underline{m-2}}\right),&n=m+1,\\[2mm]
m(n)_{\underline{m-1}},&n=m+2,\\[2mm]
n^m+m(m-1)\binom n2(n-2)_{\underline{m-2}},&n=m+3,\\[2mm]
n^m,&n\ge m+4.
\end{cases}}
\]
The case \(n=m+3\) has two qualitatively different optimal families, whereas for \(n\ge m+4\) every optimum selects precisely one cell from each row.

## Assumptions and scope

All graphs are finite, simple and undirected. The four-cycle is a **not necessarily induced** subgraph: a clique on four vertices therefore contains a four-cycle. Empty residual graphs contain no four-cycle. The displayed claims concern every integer pair \(2\le m\le n\). The polynomial counts every isolating subset, not only inclusion-minimal ones. The extremal counts refer to labeled board cells.

## Proof

**Residual-rectangle lemma.** Given \(D\subseteq[m]\times[n]\), let \(A\) be its set of occupied rows and \(B\) its set of occupied columns, with \(|A|=a\) and \(|B|=b\). A cell lies in \(N[D]\) if and only if its row belongs to \(A\) or its column belongs to \(B\). Hence the surviving induced graph is exactly \(R_{r,c}\), where \(r=m-a\) and \(c=n-b\), interpreting a zero-sized factor as an empty graph. If \(r,c\ge2\), four cells in two different rows and columns form a four-cycle. If \(r=1\), the surviving graph is the complete graph on \(c\) cells, which contains a non-induced four-cycle exactly when \(c\ge4\); symmetrically for \(c=1\). If either factor is zero, the residual graph is empty. This proves that \(D\) is isolating exactly when \(\epsilon(r,c)=1\), without any assumption on the cardinality of \(D\).

**Full polynomial.** Choose the \(a\) occupied rows and \(b\) occupied columns. Every selected cell lies in their \(a\)-by-\(b\) intersection, and every chosen row and column must actually be occupied. Inclusion-exclusion over empty selected rows and columns counts such choices by \(Q_{a,b}(z)\). The occupied row and column sets are unique for each \(D\); thus multiplying by \(\binom ma\binom nb\epsilon(m-a,n-b)\) and summing proves the formula with no double counting.

**Minimum.** Suppose \(|D|\le m-2\). Since at most \(|D|\) rows and columns can be occupied, at least two rows and at least \(n-(m-2)\ge2\) columns survive; the residual graph contains a four-cycle. Therefore \(\iota\ge m-1\). If \(|D|=m-1\), at least one row and \(n-m+1\) columns survive. For \(n\ge m+3\), at least four columns survive, so this is impossible. One selected cell in each row supplies an isolating set of size \(m\) for every \(n\). Conversely, when \(n\le m+2\), choosing cells in \(m-1\) distinct rows and distinct columns leaves exactly one row and at most three columns; this gives an isolating set of size \(m-1\). The minimum formula follows.

**Exact optimum multiplicities.** The residual-rectangle lemma gives all cases, as follows.

When \(n\ge m+4\), an optimum has \(m\) cells; if any row is unused, at least \(n-m\ge4\) columns also survive, contradicting isolation. Thus exactly one cell lies in each row, with \(n^m\) choices.

When \(n=m+3\), all sets with one cell per row still qualify, giving \(n^m\). The only other optimum has exactly one unused row, exactly one occupied row with two cells and all other occupied rows with one cell, with all \(m\) selected columns distinct. Choose the unused row, doubled row, two columns for the doubled row, and an injective assignment of the other \(m-2\) rows to different remaining columns. This gives \(m(m-1)\binom n2(n-2)_{\underline{m-2}}\) additional sets.

When \(n=m+2\), an optimum of size \(m-1\) must occupy precisely \(m-1\) rows and at least \(n-3=m-1\) columns. Thus all columns used by its cells are distinct, giving \(m(n)_{\underline{m-1}}\) choices.

When \(n=m+1\), an optimum of size \(m-1\) must occupy precisely \(m-1\) rows and at least \(m-2\) columns; the selected cells form a row-function with either all distinct images or exactly one double-preimage. The two numbers of functions are \((n)_{\underline{m-1}}\) and \(\binom{m-1}{2}(n)_{\underline{m-2}}\). Choose the omitted row in \(m\) ways.

When \(n=m\), an optimum of size \(m-1\) is isolating if and only if either it meets exactly \(m-1\) rows and at least \(m-3\) columns, or it meets exactly \(m-1\) columns and at least \(m-3\) rows. Each row-oriented family has size \(m\sum_{b=\max\{1,m-3\}}^{m-1}\binom mb b!S(m-1,b)\): choose the missing row and a surjection from the selected rows to the \(b\) occupied columns. The two orientations overlap exactly on partial permutation matrices with \(m-1\) cells, in number \(m^2(m-1)!\). Inclusion-exclusion of these two families completes the fifth formula. This argument also covers \(m=2,3\), since the lower cutoff in the Stirling sum is at least one.

## Verification

Run `python3 verify.py` with Python 3 standard library only. It reconstructs rook-graph adjacency; enumerates every four-vertex subset containing a (not necessarily induced) four-cycle by graph-edge tests; and exhaustively tests all selected sets for \((m,n)=(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(3,6),(3,7),(4,4),(4,5)\). These independent predicates reproduce every coefficient of the polynomial and every minimum count. The program also compares the closed extremal formula with coefficient extraction for \(2\le m\le8\) and \(m\le n<m+8\). A successful execution ends with `VERIFY_OK`. These finite tests do not establish the theorem beyond the stated ranges; the preceding lemmas prove it for all allowed parameters.

As examples, the minimum counts at \((m,n)=(3,3),(4,4),(3,6),(4,5)\) are respectively \(36,416,576,480\). The value \(\iota(R_{3,6},C_4)=3\) contrasts with \(\iota(R_{3,5},C_4)=2\).

## Relationship to prior work

Bartolo, Borg and Scicluna introduced a sharp universal vertex-order bound and exceptional graphs for \(C_4\)-isolation; Wei, Zhang and Zhao obtained a complementary edge-order bound. Their results concern an optimum upper bound in arbitrary connected graphs, not the exact polynomial or the complete enumeration of optimizers in rectangular rook graphs. Neither of those general bounds implies the present cardinality distribution or the exact five-regime counts. Rook graphs also admit the equivalent description as line graphs of complete bipartite graphs, but the four-cycle-isolation predicate is applied to the *line graph*, rather than to the original bipartite graph's cycles. The proof here uses an explicit residual-rectangle description to avoid ambiguity. The result is also not a parameter substitution in star isolation: the residual rook graphs \(R_{1,3}\) and \(R_{2,2}\) both have maximum degree \(2\), but the first is \(C_4\)-free and the second contains a four-cycle. Therefore any test based only on residual maximum degree, even with every star-size threshold available, cannot recover the exact square-isolation predicate.

## Limitations

The result is restricted to two-dimensional complete-factor Cartesian products, with \(m,n\ge2\); no claim is made for arbitrary Hamming products or induced-four-cycle isolation. Priority is assessed against inspected and discoverable sources, not guaranteed against every unindexed publication. Exact boundary behavior depends on using non-induced four-cycles.

## References

- K. Bartolo, P. Borg, D. Scicluna, *Isolation of squares in graphs*, arXiv:2310.09128, first submitted 2023-10-13, https://arxiv.org/abs/2310.09128 .
- X. Wei, G. Zhang, B. Zhao, *On the \(C_4\)-isolation number of a graph*, arXiv:2310.17337, first submitted 2023-10-26, https://arxiv.org/abs/2310.17337 .
