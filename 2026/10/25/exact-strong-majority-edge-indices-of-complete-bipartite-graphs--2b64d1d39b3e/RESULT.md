# Exact strong-majority edge indices of complete bipartite graphs

## Finding
For every pair of integers \(m,n\ge 2\), let \(\operatorname{Maj}'(K_{m,n})\) denote the minimum number of edge colours such that, at each edge, no colour occurs on more than half of its adjacent edges. Then
\[
\operatorname{Maj}'(K_{m,n})=\begin{cases}
2,&\min(m,n)=2\text{ and }\max(m,n)\text{ is even},\\
4,&\{m,n\}\in\{\{3,4\},\{4,5\}\},\\
3,&\text{otherwise.}
\end{cases}
\]
In particular, the two four-colour cases are the only obstructions to three colours when both bipartition sides have at least three vertices.

## Assumptions and scope
All graphs are finite and simple. The colouring of the edges need not be proper. Two edges are adjacent if they share an endpoint; the edge itself is not among its adjacent edges. In \(K_{m,n}\), identify its \(mn\) edges with an \(m\)-by-\(n\) matrix of colours. At each cell there are \(m+n-2\) adjacent cells, so no colour may occur more than \(t=\lfloor(m+n-2)/2\rfloor\) times among the other cells in the same row or column. Permuting rows, columns and global colour names preserves feasibility.

## Proof
**Lower bounds and two colours.** One colour is impossible because \(m+n-2>0\). If a two-colouring exists, every edge has precisely half its adjacent edges in each colour, so \(m+n-2\) is even. Write the two colours as \(x_{ij}\in\{-1,1\}\), with row sums \(R_i=\sum_jx_{ij}\) and column sums \(C_j=\sum_ix_{ij}\). The equal-half condition is
\[R_i+C_j-2x_{ij}=0\qquad\text{for every }i,j.\]
Sum over the columns, subtract the resulting equations for any two rows, and obtain \((n-2)(R_i-R_{i'})=0\). Likewise \((m-2)(C_j-C_{j'})=0\). When \(m,n\ge3\), all row sums coincide and all column sums coincide. Thus \(x_{ij}=(R_i+C_j)/2\) is constant across all cells, contradicting the equal-half condition. Hence two colours are impossible for \(m,n\ge3\).

If \(m=2\), every column can have its two cells the same colour. For even \(n\), colour half the columns zero and half one; each cell sees exactly \(n/2\) adjacent cells of either colour, giving a two-colouring. When \(n\) is odd, there are \(n\) adjacent cells at each edge, so two colours are impossible; choose a column-colour word with multiplicities \((n-1)/2,(n-1)/2,1\), and repeat this word in both rows. Each cell sees exactly the full multiplicity of each colour among its neighbours, never exceeding \(\lfloor n/2\rfloor\). This gives three colours for every odd \(n\ge3\). Transposition covers \(n=2\).

**Periodic construction.** Suppose \(m,n\ge3\). Colour cell \((i,j)\) by \(i+j\pmod3\), using zero-based indices. Each colour occurs in any one row at most \(\lceil n/3\rceil\) times and in any one column at most \(\lceil m/3\rceil\) times. Therefore each colour occurs among the neighbours of any cell at most \(\lceil m/3\rceil+\lceil n/3\rceil\) times (actually two fewer for its own colour). This is a valid three-colouring whenever
\[\lceil m/3\rceil+\lceil n/3\rceil\le\lfloor(m+n-2)/2\rfloor.\tag{1}\]
Write \(s=m+n\). Since the left side is at most \((s+4)/3\), inequality (1) holds for \(s\ge17\), as then \((s+4)/3\le(s-3)/2\le\lfloor(s-2)/2\rfloor\). A direct check of the finite domain \(3\le m\le n\), \(m+n\le16\), leaves precisely the four exceptions \((3,4),(4,4),(4,5),(4,7)\). This finite arithmetic step is independently reproducible in `verify.py`.

**Two exceptional three-colour constructions.** For \((m,n)=(4,4)\), the rows of a valid three-colour matrix are
```
0 1 0 0
2 2 0 1
0 1 1 2
2 2 1 0
```
For \((m,n)=(4,7)\), the rows are
```
2 1 1 2 2 0 0
0 1 2 0 2 1 1
1 0 0 1 0 2 2
2 0 0 2 0 1 1
```
The checker in `verify.py` verifies every cell and each colour against the original definition.

**The two four-colour upper bounds.** For \((m,n)=(3,4)\) and \((4,5)\), colour cell \((i,j)\) by \(i+j\pmod4\). In each case the maximum count of any colour among an edge's neighbours is respectively \(2\) and \(3\), which equals \(t\). Hence four colours suffice.

**The two four-colour lower bounds.** The standalone exhaustive program `exception_checker.cpp` verifies that neither \(K_{3,4}\) nor \(K_{4,5}\) has a three-colouring. Its finite exhaustive argument exploits only graph automorphisms: every possible first row can, by permuting columns and globally relabelling three colours, be placed in a canonical order of three contiguous blocks with nonincreasing block sizes. Remaining rows can be placed in nondecreasing lexicographic order because row permutations preserve the property. The program enumerates all three-colour row words at each stage, pruning only a partial assignment for which some already placed cell already has more than \(t\) same-colour neighbouring cells. Such a violation cannot be removed by adding rows, so the pruning is sound. The search enumerates all equivalence classes under these permutations and finds no complete assignment for either parameter pair. The program is a complete finite proof for precisely these two exceptional instances; it makes no inference from a sample or a timeout. Combining these bounds with the explicit four-colourings establishes the theorem.

## Verification
Run `python3 verify.py` to check all special matrices, all two-row constructions through \(n=100\), the periodic construction in 101 ordered parameter pairs, and the finite arithmetic exceptions. Run `g++ -std=c++17 -O2 exception_checker.cpp -o exception_checker && ./exception_checker` to reproduce the exhaustive three-colour nonexistence certificates. It reports 931 and 59,228 attempted partial row extensions, respectively, with no complete valid assignment. These experiments supplement the analytic infinite-family arguments. The only computer-exhaustive steps essential to the theorem are the two explicitly finite exception exclusions; their source code, search domain, symmetry normalisation and pruning justification are provided in full.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak and Woźniak (2026, arXiv:2605.23828v1, publicly posted 22 May 2026) introduce strong-majority edge colourings and establish general bounds, including four colours under substantial minimum-degree assumptions; their article does not state this exact complete-bipartite classification. Pękała and Przybyło (2026, arXiv:2608.04122v1, publicly posted 4 August 2026) prove that all graphs of minimum degree at least five have a three-colouring. Therefore the three-colour upper bound here for \(\min(m,n)\ge5\) is already implied by their stronger general theorem and is not independently novel. What remains family-specific is the sharp two-versus-three-versus-four classification, including the complete low-minimum-degree ranges \(m=2,3,4\) and the two exceptional obstacles. Their full document was not accessible for detailed comparison in this review; potential earlier treatment of individual obstructions is a residual priority risk. Independently, related published-finding corpus records treat complete graphs, not the complete-bipartite phase diagram, and a generalized majority threshold rather than this exact \(k=2\) classification.

## Limitations
The formula applies only to complete bipartite graphs with both parts at least two. Its two exceptional nonexistence arguments are exhaustive finite searches with provided complete source and symmetry justification; independent formal or human checking of those finite programs has not been performed. Other authors may have established individual exceptional examples or an equivalent family classification. No general statement about arbitrary bipartite graphs follows from this theorem.

## References
1. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1 (22 May 2026), https://arxiv.org/html/2605.23828v1.
2. P. Pękała and J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122v1 (4 August 2026), https://arxiv.org/abs/2608.04122.
