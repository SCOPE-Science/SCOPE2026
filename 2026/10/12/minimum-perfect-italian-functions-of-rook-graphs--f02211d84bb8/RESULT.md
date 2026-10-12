# Minimum perfect Italian functions of rook graphs
## Finding
Let
\[
2\le m\le n,
\]
and let
\[
R_{m,n}=K_m\square K_n
\]
be the rook graph. Index its vertices by cells
\[
(i,j),\qquad 1\le i\le m,\quad 1\le j\le n,
\]
with two cells adjacent exactly when they lie in a common row or a common column.

The minimum perfect Italian dominating functions admit the following complete classification.

If \(m=n\), then
\[
\gamma_I^p(R_{n,n})=n,
\]
and every minimum function is a permutation matrix of label \(1\): for a unique permutation \(\pi\in S_n\),
\[
f(i,\pi(i))=1
\]
for every row \(i\), and all other cells receive label \(0\). Hence the number of minimum functions is
\[
n!.
\]

If \(m<n\), then
\[
\gamma_I^p(R_{m,n})=2m.
\]
Every minimum function has exactly one of the following forms.

1. A single column is entirely labeled \(2\), and every other cell is labeled \(0\).
2. Two columns are entirely labeled \(1\), and every other cell is labeled \(0\).
3. Only when \(n=m+1\): one row is entirely labeled \(1\), and in every other row exactly one further cell is labeled \(1\), with all of those further labels lying in one common column.

Thus the number of minimum functions is
\[
N_{m,n}=
\begin{cases}
n!,&m=n,\\
n+\binom n2+mn,&n=m+1,\\
n+\binom n2,&n\ge m+2.
\end{cases}
\]

## Assumptions and scope
A perfect Italian dominating function on a finite simple graph \(G\) is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every vertex \(v\) with \(f(v)=0\) satisfies
\[
\sum_{u\in N(v)}f(u)=2.
\]
Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_I^p(G)\) is the minimum weight.

For an \(m\)-by-\(n\) labeling, write
\[
r_i=\sum_{j=1}^n f(i,j),
\qquad
c_j=\sum_{i=1}^m f(i,j).
\]
For every zero cell \((i,j)\), the perfect Italian condition is exactly
\[
r_i+c_j=2,
\tag{1}
\]
because its neighbors are precisely the other cells in its row and column.

The previously published Cartesian-product theorem already determines the minimum values \(n\) in the square case and \(2m\) in the rectangular case. The new content here is the complete equality classification and exact count of minimum functions; a self-contained proof of the minimum values is included to make the equality analysis independent.

## Proof
A zero row and a zero column cannot occur simultaneously: their intersection would be a zero cell with neighbor-label sum \(0\), contradicting (1). Therefore every feasible labeling has either every row positive or every column positive. In particular,
\[
\omega(f)\ge m.
\tag{2}
\]

### Square case
Suppose \(m=n\). A permutation-matrix labeling of \(1\)'s is feasible because each zero cell sees one unit in its row and one unit in its column. Hence
\[
\gamma_I^p(R_{n,n})\le n.
\]
Together with (2), this gives equality.

Let \(f\) now have weight \(n\). If some column were zero, then every row would meet that column in a zero cell, so (1) would force every row sum to be \(2\), giving total weight \(2n\), impossible. Thus every column is positive. By symmetry every row is positive. Since there are \(n\) rows and \(n\) columns and the total weight is exactly \(n\), every row sum and every column sum equals \(1\). Hence each row and each column contains exactly one label \(1\), and all other entries are zero. These are exactly the permutation matrices, giving \(n!\) minima.

### Rectangular lower bound
Assume \(m<n\). We prove
\[
\omega(f)\ge2m.
\tag{3}
\]
Suppose instead that \(\omega(f)<2m\).

If some column \(j\) is zero, then every cell \((i,j)\) is zero and (1) gives
\[
r_i=2
\]
for every row. Hence \(\omega(f)=2m\), contradiction.

Thus every column is positive. A zero row would then force every column sum to be \(2\), so the total weight would be \(2n>2m\), again impossible. Hence every row is also positive.

If some row has \(r_i\ge2\), that row cannot contain a zero cell, since every column sum is at least \(1\) and (1) would give at least \(3\). Thus the entire row is positive and has weight at least \(n\). Every other row has weight at least \(1\), so
\[
\omega(f)\ge n+(m-1)\ge2m,
\]
because \(n\ge m+1\), a contradiction.

Therefore every row has sum \(1\), so the total weight is \(m\). But all \(n\) columns are positive, requiring total weight at least \(n>m\), impossible. This proves (3).

A full column of label \(2\) is feasible, as are two full columns of label \(1\). Both have weight \(2m\), so
\[
\gamma_I^p(R_{m,n})=2m
\]
when \(m<n\).

### Equality classification in the rectangular case
Let \(m<n\) and let \(f\) have weight \(2m\).

First suppose some column \(j\) is zero. Equation (1) at the cells of that column gives
\[
r_i=2
\]
for every row. If a positive column \(k\) contained a zero entry \((i,k)\), then
\[
r_i+c_k\ge3,
\]
contradicting (1). Hence every positive column is full. Because each row has total weight exactly \(2\), there can be only two possibilities: one full positive column, whose entries must all be \(2\); or two full positive columns, whose entries must all be \(1\). These are types 1 and 2.

Now suppose no column is zero. As above, no row can be zero. Let \(h\) be the number of rows with sum at least \(2\). Every such row is full, hence contributes at least \(n\), while every other row contributes at least \(1\). Therefore
\[
2m=\omega(f)\ge hn+(m-h)=m+h(n-1).
\tag{4}
\]
If \(h=0\), the total weight would be only \(m\), so \(h\ge1\). Since \(n-1\ge m\), (4) forces
\[
h=1,
\qquad
n=m+1,
\]
and equality throughout. Thus the unique heavy row consists entirely of label \(1\), while every other row has exactly one label \(1\).

Let \(t_j\) be the number of those nonheavy rows whose unique \(1\) lies in column \(j\). The full row contributes one unit to every column, so
\[
c_j=1+t_j.
\]
If a nonheavy row has its unique \(1\) in column \(s\), then every other cell \((i,j)\) in that row is zero. Equation (1) gives
\[
1+c_j=2
\]
for every \(j\ne s\), hence \(t_j=0\) for every \(j\ne s\). Therefore all nonheavy rows use the same column. This is exactly type 3.

Conversely, every labeling of type 3 is feasible: a zero cell lies in a nonheavy row and outside the common column, so its row sum and column sum are both \(1\), satisfying (1).

The three families are disjoint. There are \(n\) choices in type 1, \(\binom n2\) choices in type 2, and, when \(n=m+1\), \(m\) choices of the full row and \(n\) choices of the common column in type 3. This yields the stated counts.

## Verification
The included verifier checks the perfect Italian definition directly from the rook graph adjacency relation.

For the cases
\[
(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),
\]
it enumerates every ternary labeling whose weight is at most the claimed optimum, rejects all lower-weight candidates, and compares the complete minimum layer with the structural classification. It checks \(57{,}007\) bounded-weight labelings in this direct phase.

The verifier then constructs all theorem-predicted minimum functions for
\[
2\le m\le8,
\qquad
m\le n\le9,
\]
and checks the defining equality at every zero cell, the weight, and the closed counting formulas. In this construction phase it checks \(47{,}296\) minimum functions.

## Relationship to prior work
Varghese and Lakshmanan proved the exact perfect Italian domination number of \(K_m\square K_n\): their Theorem 4.4 gives the value \(n\) for \(m=n\) and \(2m\) for \(m<n\). Their proof works with row weights and establishes the scalar optimum, but the inspected full text does not classify all equality cases or count minimum functions. Targeted full-text searches for “minimum functions” and “permutation” returned no occurrence.

Lauri and Mitillos study perfect Italian domination on planar and regular graphs. Their regular-graph discussion includes \(K_3\square K_2\) as a small cubic example, but the inspected full text contains no rook-graph treatment and does not imply the rectangular classification above.

The present theorem refines the published product value into an equality-structure theorem. In particular, it reveals a phase not visible in the scalar formula: the rectangular family has only the one-column and two-column minima once \(n\ge m+2\), while the boundary \(n=m+1\) acquires an additional row-column-cross family of \(mn\) minima.

## Limitations
The theorem classifies only minimum perfect Italian functions, not all feasible functions or their full weight enumerator.

The result is specific to the Cartesian product of two complete graphs. It does not claim an analogous classification for Hamming graphs with three or more factors or for arbitrary line graphs.

Finite computation is corroborative only. The all-parameter result follows from the row-sum and column-sum proof.

A differently phrased or non-indexed minimum-function classification may exist; targeted same-object and same-invariant searches did not locate one.

## References
1. J. Lauri, C. Mitillos, “Perfect Italian domination on planar and regular graphs,” arXiv:1905.06293v1, 15 May 2019.
2. J. Varghese, A. Lakshmanan S, “Perfect Italian Domination Number of Graphs,” arXiv:1910.12260v1, 27 October 2019.
