# Two-adic critical groups distinguish the smallest diameter-three Doob and Hamming graphs

## Finding

Let \(S\) be the Shrikhande graph, let \(R=K_4\square K_4\), and let \(K_4\) be the complete four-vertex graph. Set \(D=S\square K_4\) and \(H=R\square K_4=H(3,4)\). The two connected graphs have 64 vertices, the same distance-regular intersection array, and the same Laplacian spectrum, but their critical groups are not isomorphic. Their exact elementary-divisor decompositions are

\[
\begin{aligned}
K(D)&\cong (\mathbb Z/3\mathbb Z)^{27}
\oplus(\mathbb Z/2\mathbb Z)^3
\oplus(\mathbb Z/4\mathbb Z)^4
\oplus(\mathbb Z/8\mathbb Z)^2
\oplus(\mathbb Z/16\mathbb Z)^6
\oplus(\mathbb Z/32\mathbb Z)^{14}
\oplus(\mathbb Z/64\mathbb Z)^6,\\
K(H)&\cong (\mathbb Z/3\mathbb Z)^{27}
\oplus(\mathbb Z/2\mathbb Z)
\oplus(\mathbb Z/4\mathbb Z)^8
\oplus(\mathbb Z/16\mathbb Z)^6
\oplus(\mathbb Z/32\mathbb Z)^{14}
\oplus(\mathbb Z/64\mathbb Z)^6.
\end{aligned}
\]

Both have spanning-tree number \(2^{147}3^{27}\) and the same rank 28 for their reduced Laplacians modulo two. Nevertheless, their subgroups annihilated by four have different sizes:
\[
|K(D)[4]|=2^{67},\qquad |K(H)[4]|=2^{69}.
\]
Here \(K(G)[4]=\{x\in K(G):4x=0\}\). Thus an integral chip-firing invariant distinguishes this canonical cospectral pair even when the ordinary prime-field ranks and tree counts agree.

## Assumptions and scope

All graphs are simple, undirected, unweighted, and finite. Give \(S\) vertex set \((\mathbb Z/4\mathbb Z)^2\), with two vertices adjacent precisely when their coordinate difference belongs to
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}.
\]
Give \(R\) the same vertex set, with distinct pairs adjacent exactly when they agree in one coordinate. For either \(X\in\{S,R\}\), the Cartesian product \(X\square K_4\) has vertex set \((\mathbb Z/4\mathbb Z)^3\), with adjacency in the first two coordinates through \(X\), or adjacency in the third coordinate through \(K_4\), never both simultaneously.

For a connected graph \(G\), its critical (Jacobian/sandpile) group \(K(G)\) is the cokernel of any reduced integer Laplacian \(L_G'\) obtained by deleting one row and the corresponding column from \(L_G=\operatorname{diag}(\deg)-A_G\). The result is a statement about these two explicit 64-vertex graphs, not an assertion about every Doob graph.

## Proof

**1. Shared spectral and tree data.** Both \(S\) and \(R\) are strongly regular with parameters \((16,6,2,2)\). This can be verified directly from the adjacency definitions: \(A_X^2=4I+2J\) for \(X=S,R\). Their adjacency eigenvalues, with multiplicities, are \(6^{(1)},2^{(6)},(-2)^{(9)}\). The eigenvalues of \(K_4\) are \(3^{(1)},(-1)^{(3)}\), so the Cartesian product adjacency spectra are \(9^{(1)},5^{(9)},1^{(27)},(-3)^{(27)}\). Consequently both Laplacian spectra are \(0^{(1)},4^{(9)},8^{(27)},12^{(27)}\). The matrix-tree theorem gives
\[
\det L_G'=\frac{4^9 8^{27}12^{27}}{64}=2^{147}3^{27}
\]
for each graph. The simple zero eigenvalue also confirms connectivity.

**2. Explicit reduced Laplacians.** Order vertices lexicographically as triples \((a,b,c)\in\{0,1,2,3\}^3\), with index \(16a+4b+c\). Form the 64-by-64 adjacency matrices from the rules above. Construct \(L=9I-A\), then remove its final row and column to obtain an integer 63-by-63 matrix \(B\). This recipe uniquely determines every integer entry and is implemented independently in the two verifiers.

**3. Certified prime-power elimination.** Fix \(p\in\{2,3\}\) and an exponent \(m\) (nine for two, five for three). Work exactly over \(\mathbb Z/p^m\mathbb Z\). At each active submatrix, select an entry of minimum \(p\)-adic valuation \(t<m\), transpose rows and columns to place it at the diagonal pivot, and multiply its row by a unit to turn the pivot into \(p^t\). Every remaining entry is divisible by \(p^t\), so elementary row and column subtractions clear that pivot's column and row. Such operations are invertible over the residue ring. Continuing produces a diagonal matrix with entries \(p^{t_1},\dots,p^{t_{63}}\) modulo \(p^m\). Since all computed valuations satisfy \(t_i<m\), these are precisely the local Smith elementary-divisor valuations, not just bounds obtained from an insufficient modulus.

The resulting counts are:

| Graph | Prime | Valuation \(0\) | Valuation \(1\) | Valuation \(2\) | Valuation \(3\) | Valuation \(4\) | Valuation \(5\) | Valuation \(6\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(D\) | 2 | 28 | 3 | 4 | 2 | 6 | 14 | 6 |
| \(H\) | 2 | 28 | 1 | 8 | 0 | 6 | 14 | 6 |
| \(D\) | 3 | 36 | 27 | 0 | 0 | 0 | 0 | 0 |
| \(H\) | 3 | 36 | 27 | 0 | 0 | 0 | 0 | 0 |

Each row has 63 factors; the sums of \(i\) times its count are \(147\) for prime two and \(27\) for prime three. The preceding determinant formula excludes all other primes. The fundamental theorem of finite abelian groups gives the asserted decompositions.

**4. Distinguishing invariant.** The number of nontrivial two-primary cyclic summands is 35 in each group, so each has exactly \(2^{35}\) elements annihilated by two. For a summand of order \(2^e\), the subgroup annihilated by four has order \(2^{\min(e,2)}\). The exponents in the displayed decompositions yield \(2^{67}\) and \(2^{69}\), respectively. This proves nonisomorphism despite equal spectra and equal two-ranks.

## Verification

The standalone file `verify.py` builds both graphs from all ordered coordinate triples, checks degree, symmetry and their 16-vertex strongly regular factors, constructs each reduced Laplacian, and performs exact modular Smith elimination using minimum-valuation pivots. The separate C++ program `verify_alt.cpp` builds the graphs by adding their generating edges, selects pivots in the opposite tie order, independently computes the local elementary-divisor counts, and checks the output. Reproduction commands:

```sh
python3 verify.py
g++ -O2 -std=c++17 -Wall -Wextra verify_alt.cpp -o verify_alt
./verify_alt
```

Successful runs end with `CRITICAL_GROUP_CERTIFICATE_OK` and `INDEPENDENT_CERTIFICATE_OK`. No input data files, numerical spectral approximations, remote services, or external packages are needed. The arithmetic in the modular certificate is exact; all values fit within the integer ranges used.

## Relationship to prior work

Peeters (2002; an earlier 1994 report is catalogued) developed prime-field rank methods for Hamming and Doob graphs. His results give equality of their corresponding relevant \(p\)-ranks; they do **not** specify the higher two-adic Smith factors of the 64-vertex reduced Laplacians used here. Thus this result refines, rather than contradicts, that rank equality. The distance-regular graph survey of Van Dam, Koolen and Tanaka (2016, preprint 2014) identifies the matching intersection arrays and observes that the critical group is not in general determined by distance-regular parameters; it cites the earlier 16-vertex Shrikhande/rook example. That example is expressly prior art and not claimed anew here.

Jacobson, Niedermaier and Reiner (2003) study critical groups of Cartesian products of **complete** graphs. Their general block reductions for multiplying by a complete graph are relevant methods, but a product with a Shrikhande factor is not among the explicit complete-factor families covered by their stated theorem. The distinction for the present 64-vertex pair is not supplied by a tree-count formula, the 16-vertex distinction alone, or prime-field rank equality. The literature comparison found no published exact two-adic classification of this specific pair; this absence is not a proof of priority.

## Limitations

This is a finite computationally certified group classification, with the nonstandard numerical Smith reductions reproduced by two standalone source implementations. It does not claim an all-dimensional theorem for arbitrary Doob graphs, nor a symbolic closed formula for future Cartesian powers. A prior equivalent classification could exist in unindexed computational tables or inaccessible literature. The complete text of Jacobson–Niedermaier–Reiner (2003) was not available for line-by-line inspection; its published abstract and an indexed excerpt of its block-reduction proposition were inspected, and the corresponding novelty comparison retains this access risk. Independent scholarly validation has not been performed.

## References

1. R. Peeters, *On the p-Ranks of the Adjacency Matrices of Distance-Regular Graphs*, Journal of Algebraic Combinatorics 15 (2002), 127–149. DOI: 10.1023/A:1013842904024. Full article: https://www.maths.tcd.ie/EMIS/journals/JACO/Volume15_2/v121065651493101.fulltext.pdf .
2. B. Jacobson, A. Niedermaier, V. Reiner, *Critical Groups for Complete Multipartite Graphs and Cartesian Products of Complete Graphs*, Journal of Graph Theory 44 (2003), 231–250. DOI: 10.1002/jgt.10139.
3. E. R. van Dam, J. H. Koolen, H. Tanaka, *Distance-regular graphs*, Electronic Journal of Combinatorics Dynamic Survey DS22 (2016); arXiv:1410.6294, especially Sections 3, 10.2, and 15.2.2. https://arxiv.org/html/1410.6294v2 .
