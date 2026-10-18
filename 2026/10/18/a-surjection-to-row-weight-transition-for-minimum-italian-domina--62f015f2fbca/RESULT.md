# A surjection-to-row-weight transition for minimum Italian domination on \(K_m\square K_n\)

## Finding
Let \(2\le m\le n\) be integers, and let \(R_{m,n}=K_m\square K_n\) be the labeled rook graph with vertex set \(\{(i,j):1\le i\le m,\ 1\le j\le n\}\). An Italian dominating function is a labeling \(f:V(R_{m,n})\to\{0,1,2\}\) such that every zero-labeled vertex has total neighbor-label weight at least two. Write \(\gamma_I\) for the least total label weight and \(N_I(m,n)\) for the number of distinct minimum-weight labelings on the named vertices.

**Theorem.** For every \(2\le m\le n\),
\[
\gamma_I(R_{m,n})=\min\{n,2m\}.
\]
Define the surjection number
\[
U_m(n)=\sum_{j=0}^{m}(-1)^j\binom{m}{j}(m-j)^n
=m!\left\{\!\!\begin{matrix}n\\m\end{matrix}\!\!\right\},
\]
where the braced expression is a Stirling number of the second kind, and put \(B_m(n)=\bigl(n+\binom{n}{2}\bigr)^m\). Then
\[
N_I(m,n)=
\begin{cases}
U_m(n),&n<2m,\\[2pt]
B_m(n)+U_m(n)-(2m)!/2^m,&n=2m,\\[2pt]
B_m(n),&n>2m.
\end{cases}
\]
All minimum-weight functions are classified as follows: for \(n<2m\), each column has exactly one entry labeled \(1\), every row has at least one such entry, and all others are \(0\); for \(n>2m\), every row has total label weight two, realized independently as one \(2\) or two \(1\)'s, with all other entries \(0\). At \(n=2m\), the complete minimum family is the union of these two types, whose intersection consists exactly of the \(0\)-\(1\) matrices with two ones in each row and one in each column.

## Assumptions and scope
The factors are ordinary finite simple complete graphs and \(\square\) denotes their Cartesian graph product, not their tensor product. Vertices and both coordinate directions are labeled, and optimizer counts are not divided by graph automorphisms. A zero entry has neighbors in its own row and its own column, excluding itself. There is no restriction on the neighborhood of a positive entry. The formulas are valid for all integers \(2\le m\le n\), including \(n=2m\) and \(m=n\); interchange the factors for the remaining rectangular orientations.

## Proof
Let \(R_i=\sum_{j=1}^{n}f(i,j)\), \(C_j=\sum_{i=1}^{m}f(i,j)\), and \(W=\sum_i R_i=\sum_j C_j\). For any entry labeled zero at position \((i,j)\), the total label weight of its neighbors is **exactly** \(R_i+C_j\). Thus \(f\) is Italian dominating if and only if \(R_i+C_j\ge2\) at every zero entry.

If some column is identically zero, then every one of its entries is zero, so the preceding characterization forces \(R_i\ge2\) for each row and therefore \(W\ge2m\). If no column is identically zero, then \(C_j\ge1\) for all \(j\), giving \(W\ge n\). Consequently every feasible labeling has \(W\ge\min\{n,2m\}\).

Both bounds are achievable. Because \(n\ge m\), put a single label \(1\) in each column, distributing their locations so that every row is occupied. At a zero entry its row and its column each contribute at least one, so this gives an Italian function of weight \(n\). Alternatively, put one label \(2\) in an arbitrarily chosen column of each row and zero elsewhere. At a zero entry its row alone contributes two, so this gives weight \(2m\). Hence the lower bound is sharp.

Suppose first that \(n<2m\) and \(W=\gamma_I=n\). An empty column would force \(W\ge2m>n\), which is impossible. Since all \(n\) columns are nonempty and their combined weight is exactly \(n\), each column contains precisely one unit of label weight, necessarily an entry labeled \(1\). If a row were empty, the condition on its zero entries would require \(C_j\ge2\) for every column, contradicting \(C_j=1\). Thus every row is occupied. Conversely every labeling described in the theorem is feasible. Choosing for each of the \(n\) named columns its unique occupied row is therefore a surjection onto the \(m\) named rows. Inclusion-exclusion gives \(U_m(n)\).

Next suppose \(n>2m\) and \(W=\gamma_I=2m\). Because \(W<n\), at least one column is empty. Each row therefore has \(R_i\ge2\), and summing forces \(R_i=2\) for all \(i\). Conversely any such labeling is feasible, since every zero entry sees row-weight two. In a particular row, the only realizations of total weight two are a single \(2\), which has \(n\) choices of position, or a pair of \(1\)'s, which has \(\binom{n}{2}\) choices. The rows can be chosen independently, giving \(B_m(n)\).

Finally suppose \(n=2m\) and \(W=\gamma_I=n=2m\). If some column is empty, then exactly the row-weight-two family occurs; if all columns are nonempty, their weights all equal one and every row must be occupied as in the preceding surjection argument. These two families are exhaustive. A labeling in both has exactly one label \(1\) per column and two such labels per row. To count the overlap, assign the \(2m\) distinguishable columns to the \(m\) distinguishable rows in fibers of size exactly two, giving \((2m)!/(2!)^m\). Inclusion-exclusion for the union yields \(B_m(2m)+U_m(2m)-(2m)!/2^m\). This completes every claimed classification and count.

## Verification
The standalone file `verify_italian_rook.py` constructs row-column adjacency directly, enumerates all labelings of weight at most the claimed optimum, and tests each zero entry against the actual sum of adjacent labels. It confirms zero feasible functions of lower weight and the exact optimizer count for nineteen profiles: \(m=2,\ 2\le n\le10\); \(m=3,\ 3\le n\le9\); and \(m=4,\ 4\le n\le6\). The package contains its captured output as `verification_output.txt`. Examples include \(N_I(2,4)=108\), \(N_I(3,6)=9711\), and \(N_I(3,7)=21952\). These finite tests corroborate, but do not establish, the theorem for arbitrary parameters; the preceding proof establishes the infinite family.

## Relationship to prior work
Italian domination is also called Roman \(\{2\}\)-domination. Alizadeh et al. (arXiv:1701.01416, publicly posted on 5 January 2017) study the invariant, graph operations, and Cartesian grid bounds; their general Cartesian-product upper bound does not determine the optimizer counts here. Klostermeyer and MacGillivray (2019) explicitly establish the **previously known** scalar equality \(\gamma_I(K_t\square K_t)=t\) for square rook graphs. Thus the square-case scalar equality above is not presented as novel; the counting, classification, and rectangular three-regime transition are the present claims. Varghese and Lakshmanan (2023, Theorem 2.4) determine the *perfect* Italian domination number for the same rook graphs, imposing equality, rather than inequality, of defending-neighborhood weight at each zero vertex; that result does not count or classify all ordinary Italian minima. Shao and Zhao (2026, arXiv:2610.00108) count Italian dominating functions on paths, trees, and cycles rather than rook graphs. Complete multipartite results for Roman \(\{2\}\)-domination concern a different graph family: a nontrivial rook graph with both factors at least three is not complete multipartite. The complete 2019 publisher PDF could not be retrieved within the available access path; its accessible indexed portions include the square-case scalar result, and possible additional coverage is a residual bibliographic risk.

## Limitations
This is an exact minimum-weight and optimizer-enumeration theorem, not a formula for every coefficient of the Italian domination polynomial. An indexed excerpt, rather than the full publisher PDF, was available for the particularly relevant 2019 paper; this limits the bibliographic comparison. Equivalent earlier counting results in undiscovered or inaccessible sources remain possible. No independent scientific review has been performed.

## References
1. F. Alizadeh, H. R. Maimani, L. Parsaei Majd, and M. Rajabi Parsa, *Roman \(\{2\}\)-domination in graphs and graph products*, arXiv:1701.01416, first version 5 January 2017; later published in the *Iranian Journal of Mathematical Sciences and Informatics*. https://arxiv.org/abs/1701.01416
2. W. F. Klostermeyer and G. MacGillivray, *Roman, Italian, and 2-Domination*, *Journal of Combinatorial Mathematics and Combinatorial Computing* **108** (2019), 125–146. https://combinatorialpress.com/jcmcc-articles/volume-108/roman-italian-and-2-domination/
3. J. Varghese and A. Lakshmanan S., *Perfect Italian Domination Number of Graphs*, *Palestine Journal of Mathematics* **12** (2023), 158–168. https://pjm.ppu.edu/sites/default/files/papers/PJM_Feb_2023_158_to_168.pdf
4. P. Shao and C. Zhao, *Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108, 2026. https://arxiv.org/html/2610.00108v1
