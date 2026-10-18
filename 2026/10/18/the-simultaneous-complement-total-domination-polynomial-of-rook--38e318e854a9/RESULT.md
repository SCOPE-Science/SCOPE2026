# The simultaneous complement-total domination polynomial of rook graphs

## Finding

Let \(R_{m,n}=K_m\square K_n\) be the rook graph on an \(m\)-by-\(n\) board, with \(m,n\ge 2\). A set \(D\) is **simultaneous complement-total dominating** (abbreviated SDCTD) if it dominates \(R_{m,n}\) in the ordinary closed-neighborhood sense and totally dominates the complementary graph \(\overline{R_{m,n}}\) in the open-neighborhood sense. Define the cardinality polynomial
\[
F_{m,n}(z)=\sum_{D:\,D\text{ is SDCTD}}z^{|D|}.
\]
For every \(b\ge2\) put \(U_b(z)=(1+z)^b-1\). For integers \(a,b\ge2\), define
\[
R_{a,b}^{\star}(z)=\begin{cases}
\big(U_b(z)-bz\big)^2,&a=2,\\
U_b(z)^a-bz^a-abz^{a-1}\big(U_b(z)-z\big),&a\ge3.
\end{cases}
\]
Define the row-and-column coverage polynomial
\[
E_{m,n}(z)=\sum_{i=0}^m\sum_{j=0}^n(-1)^{i+j}\binom mi\binom nj
(1+z)^{(m-i)(n-j)}.
\]
**Theorem (all-size classification).** For \((m,n)\ne(2,2)\),
\[
\boxed{F_{m,n}(z)=R_{m,n}^{\star}(z)+R_{n,m}^{\star}(z)-E_{m,n}(z)+mnz^{m+n-2}(1+z).}
\]
For \((m,n)=(2,2)\), \(F_{2,2}(z)=z^4\).

**Theorem (sharp minima and all minimizers).** By symmetry, suppose \(2\le m\le n\). The minimum cardinality is
\[
\boxed{\bar\gamma(R_{m,n})=\begin{cases}4,&m=2,\\m,&m\ge3.\end{cases}}
\]
The number \(N_{m,n}\) of minimum sets equals
\[
\boxed{N_{m,n}=\begin{cases}
\binom n2^2,&m=2,\\
n^m-n-mn(n-1),&3\le m<n,\\
2\big(m^m-m-m^2(m-1)\big)-m!,&3\le m=n.
\end{cases}}
\]
For \(m=2\), every minimizer comprises exactly two selected squares in each row. For \(3\le m<n\), each minimizer selects exactly one square per row and no column contains more than \(m-2\) selected squares. For \(3\le m=n\), take the union of this family and its row-column transpose; their overlap consists exactly of the \(m!\) permutation matrices.

## Assumptions and scope

The graphs are simple finite undirected graphs. Coordinates are ordered pairs \((i,j)\) with \(1\le i\le m\) and \(1\le j\le n\). Two distinct squares are adjacent in the rook graph exactly when they share a row or column. Its complement connects exactly squares differing in both coordinates. Ordinary domination allows a selected vertex to cover itself, while total domination requires every vertex (including a selected one) to have a *different* selected neighbor in the graph in question. All conclusions hold for every pair of integers \(m,n\ge2\) without asymptotic qualification. The symbol \(\bar\gamma\) uses the simultaneous ordinary/complement-total convention, **not** total domination of the rook graph itself.

## Proof

**Step 1: reduce ordinary domination to occupancy.** A square \((i,j)\) is not dominated by \(D\) precisely when no selected square lies in row \(i\) or column \(j\). Thus \(D\) dominates the rook graph if and only if every row is occupied or every column is occupied. Otherwise an empty row intersects an empty column in an undominated square.

**Step 2: characterize the complement-total obstruction.** Since \((i,j)\) is adjacent in \(\overline{R_{m,n}}\) to exactly the squares outside both its row and its column, \(D\) fails complement-total domination precisely when for some \((i,j)\) all selected squares lie in the cross consisting of row \(i\) and column \(j\). This statement applies even if \((i,j)\in D\), as required for total domination.

**Step 3: count SDCTD sets occupying every row.** Select a nonempty subset of each of the \(a\) rows independently. This gives \(U_b(z)^a\). Suppose first \(a\ge3\) and this selection violates complement-total domination. By Step 2 all selected squares outside a distinguished row \(i\) must lie in the same column \(j\), with exactly one selected square in each of those rows. There are two disjoint possibilities. Either every row selects exactly \(\{j\}\), yielding \(b z^a\) sets over all columns, or the distinguished row selects a nonempty subset other than \(\{j\}\), yielding \(abz^{a-1}(U_b(z)-z)\). No configuration of the second type has two different distinguished rows because then all \(a\ge3\) rows would be the same singleton column; and its distinguished column is forced by every other occupied row. Therefore subtraction counts failures exactly once and gives \(R_{a,b}^{\star}\) for \(a\ge3\). If \(a=2\), complement-total domination demands that each of the two rows have at least two selected squares: a row singleton \(\{j\}\) would leave the square in the opposite row and column \(j\) without a complement-neighbor, and if both rows contain at least two selected columns then every vertex finds such a selected square in its opposite row. This gives \((U_b-bz)^2\).

**Step 4: impose the row/column union without double counting.** The polynomial for all sets occupying every row and every column is the displayed \(E_{m,n}\), by ordinary inclusion-exclusion on empty rows and columns. We must subtract only the intersection of the two *successful* coverage families. An intersection set that fails complement-total domination occupies all rows and columns but lies within a single cross. Necessarily it contains the entire cross *except possibly its central square*; conversely, each of these two choices meets every row and column and fails complement-total domination. For \((m,n)\ne(2,2)\), their central crosses are distinct: the full cross is determined by its unique row of \(n\) cells and unique column of \(m\) cells, with the apparent length-two degeneracy excluded. Hence the deficient intersection polynomial is exactly \(mn z^{m+n-2}(1+z)\). Inclusion-exclusion of the successful row and column families gives the formula. On the \(2\)-by-\(2\) board, Step 3 forces all four squares, and \(F_{2,2}=z^4\).

**Step 5: characterize the minimum size.** Ordinary domination forces at least \(\min(m,n)=m\) selected squares: if fewer were selected, at least one row and at least one column would remain empty, contradicting Step 1. For \(m=2\), complement-total domination alone forces at least two selected squares in each row. Indeed, if a row contains no selected square, every vertex in the opposite row has no complement-neighbor. If a row contains only \((i,j)\), then the vertex in the opposite row at column \(j\) has no complement-neighbor. Thus at least four are required, and selecting exactly two squares in each row realizes four. For \(m\ge3\), choosing one square in every row with pairwise different column indices gives \(m\) squares. Every row is occupied, and every cross misses at least one of these squares because at most one square occupies any row and at most one square any column and \(m\ge3\). Hence the size is \(m\).

**Step 6: enumerate every optimum.** Suppose \(m=2\). An optimum has four squares and, by Step 3, must select exactly two in each row. The number is \(\binom n2^2\); when \(n=2\) this is the single all-four configuration. Suppose \(m\ge3\). At size \(m\), an occupied-row set has one selected square in each row. Complement-total domination excludes exactly those assignments in which some column receives \(m-1\) or \(m\) of these squares: the corresponding cross would contain them all. There are \(n\) constant-column assignments and \(mn(n-1)\) assignments with exactly one outlier row (choose the majority column, outlier row and distinct outlier column). These possibilities are disjoint for \(m\ge3\), so the number of successful row assignments is \(n^m-n-mn(n-1)\). If \(m<n\), a set of \(m\) squares cannot occupy all \(n\) columns; therefore no other minima exist. If \(m=n\), the transposed successful-column assignments contribute equally; their intersection consists of sets with one selected square in every row and in every column, precisely the \(m!\) permutation matrices. Each is successful for \(m\ge3\). This proves the formulas and structural assertions. \(\square\)

## Verification

Two standard-library Python programs independently check the claims using direct adjacency masks rather than the occupancy proof. Running `python3 verify.py` checks all vertex subsets of sizes at most the proposed minimum for sixteen boards, including every board of size \(2\)-by-\(n\) for \(2\le n\le8\), \(3\)-by-\(n\) for \(3\le n\le6\), \(4\)-by-\(n\) for \(4\le n\le6\), and \(5\)-by-\(n\) for \(5\le n\le6\). A total of 271,904 selected subsets were examined, with every minimum set compared to the predicted structural classification and count. Running `python3 verify_polynomial.py` checks the *entire cardinality polynomial* against direct evaluation of every subset for twelve boards (\(2\)-by-\(n\) for \(2\le n\le7\), \(3\)-by-\(n\) for \(3\le n\le6\), \(4\)-by-\(n\) for \(4\le n\le5\)), totaling 1,435,472 examined subsets. Both programs passed. These finite checks supplement rather than replace the preceding general proof.

## Relationship to prior work

Bermudo, Peterin, Sedlar, and Škrekovski introduced the simultaneous parameter \(\bar\gamma(G)\), ordinary domination of a graph together with total domination of its complement, in their 2024 work on modular graph products [1]; their concluding discussion highlights it as a parameter of independent interest. The present theorem treats the canonical Cartesian product of two cliques, not a modular graph product, and determines both the all-size polynomial and its minimum configurations. Mertens [2] previously determined the ordinary domination polynomial of rook graphs. Because ordinary rook domination imposes only the row-or-column coverage condition from Step 1, that polynomial neither imposes the complement-total cross obstruction nor directly gives the stricter enumerations here. The classical notion of simultaneous domination of graph families [3] is related but does not alone imply this mixed ordinary/total result. Published formulas for total domination in the rook graph itself also differ: total domination of \(R_{m,n}\) is not total domination of its complement.

## Limitations

The theorem applies to finite rook graphs with both clique factors of order at least two; it makes no claim for higher-dimensional Hamming graphs, other graph products, or factors of arbitrary graphs. It is a mathematical proof independently of the finite checks, but the work has not undergone external independent review. Searches and full-text comparisons do not exclude an unindexed prior equivalent, and accessible abstracts of broad simultaneous-parameter papers may conceal more specialized results. No minimality claim is made for the algebraic *complexity* of the polynomial formula.

## References

[1] S. Bermudo, I. Peterin, J. Sedlar, R. Škrekovski, *Domination number of modular product graphs*, arXiv:2404.02853, first public 2024-04-03. https://arxiv.org/abs/2404.02853.

[2] S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716, first public 2024-01-01; Journal of Integer Sequences 27 (2024), Article 24.3.7. https://arxiv.org/abs/2401.00716.

[3] P. Dankelmann, M. A. Henning, W. Goddard, R. Laskar, *Simultaneous graph parameters: Factor domination and factor total domination*, Discrete Mathematics 306 (2006), 2229–2233. DOI:10.1016/j.disc.2006.04.017.
