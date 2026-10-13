# A sharp sparse-link NODF bound forces incomparable specialists
## Finding
For every integer
\[
n\ge4,
\]
consider binary ecological incidence matrices with three species in one guild and \(n\) species in the other, with exactly
\[
E=n+2
\]
interactions and with no species isolated.

Write \(d(u)>0\) for the degree of a row or column species and \(N(u)\) for its set of interaction partners. Define the classical NODF numerator
\[
P(A)=
\sum_{\substack{\{u,v\}\text{ row pair}\\ d(u)\ne d(v)}}
\frac{|N(u)\cap N(v)|}{\min\{d(u),d(v)\}}
+
\sum_{\substack{\{u,v\}\text{ column pair}\\ d(u)\ne d(v)}}
\frac{|N(u)\cap N(v)|}{\min\{d(u),d(v)\}}.
\]
Pairs with equal fill contribute exactly zero; normalization is
\[
\mathrm{NODF}(A)=\frac{P(A)}{K},\qquad
K=\binom n2+\binom32=\binom n2+3.
\]
This is the \(0\)-to-\(1\) convention rather than its common percentage rescaling.

The sharp fixed-link maximum is
\[
\boxed{\max_A\mathrm{NODF}(A)=\frac{2n-2}{\binom n2+3}}.
\]
Equality is attained precisely by matrices equivalent through row and column permutations to
\[
A_n=
\begin{pmatrix}
1&1&1&\cdots&1\\
1&0&0&\cdots&0\\
0&1&0&\cdots&0
\end{pmatrix}.
\]
Thus, up to species relabeling, there is **exactly one** optimal network. It is a connected bipartite tree, with one universal generalist and two specialists attached to **different** partners. There are exactly
\[
3n(n-1)
\]
labeled optimum matrices.

A Ferrers matrix, meaning every pair of row neighborhoods is comparable by inclusion, has the unique admissible type
\[
F_n=
\begin{pmatrix}
1&1&1&\cdots&1\\
1&0&0&\cdots&0\\
1&0&0&\cdots&0
\end{pmatrix},
\]
and scores only
\[
\mathrm{NODF}(F_n)=\frac{n+1}{K}.
\]
The exact advantage of the optimal non-Ferrers network is therefore
\[
\frac{n-3}{K}>0.
\]
For example, at \(n=4\), the maximum is \(2/3\), whereas the Ferrers value is \(5/9\).

## Assumptions and scope
The matrix entries are exactly \(0\) or \(1\), and every row and column contains at least one \(1\).

The number of rows is exactly three; the number of columns is an arbitrary integer \(n\ge4\). The total number of links \(n+2\) is fixed; with \(n+3\) species, this is the smallest possible edge count for a connected graph. We do **not** assume that every admissible network is connected, but every maximizer is.

NODF treats every unequal-degree pair within each guild by overlap divided by the less-filled member's degree. Equal-degree pairs contribute zero even when neighborhoods are identical. The row and column contributions receive equal pair weighting and the denominator is the count of all possible within-guild unordered pairs.

No degree sequence beyond positivity is prescribed. No stochastic null model or species abundance weighting is imposed. The theorem does not address other nestedness metrics, weighted networks, or fixed higher connectance.

## Proof
Because every column has positive degree, the number of links in excess of the minimum one per column is
\[
\sum_{j=1}^{n}(d(c_j)-1)
=(n+2)-n=2.
\]
Every column has degree at most three. Consequently **exactly two cases** are possible.

**Case I: one column has degree three.** Every other column has degree one. The degree-three column overlaps with every singleton column in exactly one neighbor, and each of these unequal-degree pairs contributes one. All pairs of singleton columns have equal degrees and contribute zero. Therefore the column contribution to \(P(A)\) equals \(n-1\).

All three rows share exactly the degree-three column; singleton columns cannot contribute to a row-pair overlap. Thus for unequal-degree rows the normalized overlap is \(1/\min\{d_i,d_j\}\), and tied-degree rows contribute zero. If all three row degrees are distinct, order them as
\[
a<b<c.
\]
The row contribution is
\[
\frac2a+\frac1b\le2+\frac12=\frac52,
\]
since positive distinct integers satisfy \(a\ge1\), \(b\ge2\). If any two degrees agree, at most two unequal-degree pairs contribute, each by at most one; the row contribution is then at most two. In every instance,
\[
P(A)\le n-1+\frac52=n+\frac32<2n-2
\]
for every \(n\ge4\).

**Case II: two columns have degree two.** All other \(n-2\) columns have degree one. The two degree-two columns have either one or two common row neighbors, since the matrix has only three rows.

Suppose first they share **one** row \(r_0\). Each degree-one column contributes at most one to its pair with each of the two degree-two columns; its total column-pair contribution is therefore at most two. Pairs of equal-degree columns contribute zero, hence the full column contribution is at most
\[
2(n-2).
\]
Only the row pairs joining \(r_0\) to one of the other two rows overlap: each contains one of the two degree-two columns in common. The two other rows are disjoint. Each of these at most two contributing row pairs scores at most one, so the row contribution is at most two. Therefore
\[
P(A)\le2(n-2)+2=2n-2.
\]

Equality requires every degree-one column to contribute two, so every such column must be adjacent to \(r_0\), the **only common neighbor** of both degree-two columns. This forces \(r_0\) to have degree \(n\) and the other two rows to have degree one, attached to **different** degree-two columns. Conversely, this configuration gives every degree-one column two full-overlap comparisons and the two specialist–generalist row pairs one each, so its score is exactly \(2n-2\). It is precisely \(A_n\) up to row/column permutations.

Finally, suppose the two degree-two columns share **both** row neighbors. There is a third row, and by the no-isolate requirement at least one degree-one column must be adjacent to it. Such a degree-one column has no overlap with either degree-two column. At most \(n-3\) of the degree-one columns can therefore score two in column comparisons, yielding total column score at most \(2(n-3)\). Only the two common rows can overlap. Their score is at most one, so
\[
P(A)\le2(n-3)+1=2n-5<2n-2.
\]
The exhaustive structural dichotomy proves the sharp bound, uniqueness up to permutations, and the stated maximizing matrix.

The optimizer contains all \(n+3\) vertices in one connected component and exactly \(n+2\) edges, hence is a tree. Its three rows can be labeled by choosing the universal row in three ways; the two distinct singleton columns can be ordered in \(n(n-1)\) ways. This proves the exact labeled count \(3n(n-1)\).

For the Ferrers comparison, nested row neighborhoods and no zero column force the largest row to meet all columns; no zero row and nested column neighborhoods force a column to meet all three rows. With exactly \(n+2\) links, the two other rows must each contain just that full column, proving the displayed Ferrers type. Its sole degree-three column compares with \(n-1\) singleton columns, contributing \(n-1\); its largest row compares with two singleton rows, contributing two. All remaining pairs are degree ties. Therefore
\[
P(F_n)=n+1,
\]
and the strict gap follows.

## Verification
The embedded file `verify_sparse_nodf.py` is an exact-arithmetic independent finite check. It exhaustively generates **all** \(3\)-by-\(n\) binary incidence matrices with exactly \(n+2\) interactions and no isolated rows or columns for \(2\le n\le7\), a total of \(63{,}906\) admissible matrices.

Two independently written scorers—one using bitmasks, the other using set intersections—must agree on every individual NODF score as rational numbers. The verifier confirms the maximum, unique optimal shape and labeled optimizer counts for every \(4\le n\le7\), plus the expected boundary behavior at sizes two and three. It also checks the symbolic case inequalities through \(n=100\).

Execute with standard Python:

`python3 verify_sparse_nodf.py`

The first output line is `VERIFY_OK`. These finite checks support but do not replace the universal case proof.

## Relationship to prior work
Almeida-Neto and coauthors introduced NODF in 2008 to encode decreasing fill together with paired overlap in ecological incidence matrices. Britton, Almeida Neto, and Corso analytically characterized perfect and zero NODF networks; their work does not give the present fixed-link optimum or its equality case. Song, Rohr, and Saavedra motivated normalizing nestedness relative to the maximum attainable at fixed species and link counts but used a greedy search for that maximum. Hoeppke and Simmons provided further computational algorithms for this same constrained maximum and emphasize that these methods generally do not guarantee global optimality.

A related unrestricted-link extremal formula gives Ferrers maximizers when only the two guild sizes are prescribed. It cannot imply the present fixed-link maximum: the link count is an essential restriction, and **none of the new maximizers is Ferrers**. The fixed-link result therefore identifies a distinct behavior not recovered by the unrestricted calculation.

The present theorem provides the exact optimum, all equality cases, and labeled count for the ecologically natural minimal-connected-link regime in the three-species guild. The existence of a non-Ferrers maximizer quantifies why optimizing NODF under sparse fixed connectance need not coincide with enforcing global nested-neighborhood structure.

## Limitations
The formula relies on three rows, exactly \(n+2\) links, and classical unequal-degree-pair NODF. More rows, extra links, fixed degree sequences, weights, or alternate definitions need separate investigation.

The theorem is a combinatorial extremum of an ecological index; it does not predict the assembly of real-world pollination networks. Even a high NODF value does not establish a causal ecological mechanism.

The literature comparison includes an open-access analytic study and full online treatments of the original metric and numerical fixed-link optimization, but an unindexed small-case table or software fixture could have contained the same sparse optimizer without proving its general uniqueness. No claim of independently certified novelty is made.

## References
1. M. Almeida-Neto, P. Guimarães, P. R. Guimarães Jr., R. D. Loyola, and W. Ulrich, “A consistent metric for nestedness analysis in ecological systems: reconciling concept and measurement,” *Oikos* 117 (2008), 1227–1239; first published 7 August 2008; DOI: 10.1111/j.0030-1299.2008.16644.x.
2. N. F. Britton, M. Almeida Neto, and G. Corso, “Which Matrices Show Perfect Nestedness or the Absence of Nestedness? An Analytical Study on the Performance of NODF and WNODF,” *Biomath* 4 (2015), article 1512171; DOI: 10.11145/j.biomath.2015.12.171.
3. C. Song, R. P. Rohr, and S. Saavedra, “Why are some plant–pollinator networks more nested than others?”, *Journal of Animal Ecology* 86 (2017), 1417–1424; DOI: 10.1111/1365-2656.12749.
4. C. Hoeppke and B. I. Simmons, “maxnodf: An R package for fair and fast comparisons of nestedness between networks,” *Methods in Ecology and Evolution* 12 (2021), 580–585; DOI: 10.1111/2041-210X.13545.
5. *Mathematics Subject Classification 2020*, code 92D40: Ecology.
