# Reciprocal-girth gnarledness for multi-cycle cactus graphs
## Finding
Let \(X\) be a finite connected simple cactus graph with \(b_1(X)\ge 2\), viewed as a one-dimensional simplicial complex and marked by its oriented edges. Write \(g(X)\) for the girth. For every subfield \(F\subset \mathbb R\),
\[
G_1^F(C_*^\Delta(X))=\frac{1}{g(X)}.
\]
In particular, multi-cycle cactus graphs retain the reciprocal-cycle-length formula even though the definition permits arbitrary cointegral changes of basis in the higher-rank homology group. Combining this with the dimension-one geometric gnarledness \(G_1(X)=1\) gives
\[
\frac{G_1(X)}{G_1^F(C_*^\Delta(X))}=g(X).
\]
Hence the discrepancy between geometric and algebraic gnarledness is unbounded already on cactus graphs.

## Assumptions and scope
A cactus graph here is a finite connected simple graph in which every edge belongs to at most one simple cycle. The hypothesis \(b_1(X)\ge 2\) isolates the genuinely higher-rank case: the rank-one case is already controlled by the one-dimensional-homology formula in Hofmann--Löh. The simplicial chain complex has no chains in degree \(2\). All edge orientations are arbitrary and fixed once and for all. The statement concerns the marked simplicial chain complex; it does not assert invariance under changing the marking.

## Proof
Let the simple cycle blocks of \(X\) be \(C_1,\ldots,C_r\), with lengths \(\ell_1,\ldots,\ell_r\). Choose an orientation of each \(C_i\), and let \(z_i\) be its signed oriented-edge sum. Because \(X\) is a cactus, the cycle blocks are edge-disjoint. Deleting one edge from every cycle block leaves a spanning tree, so \(r=b_1(X)\). The edge-disjoint cycles \(z_1,\ldots,z_r\) therefore form an integral basis of \(H_1(X;\mathbb Z)\). Since there are no \(2\)-simplices, every simplicial \(1\)-cycle is uniquely a linear combination of these \(z_i\).

For the upper bound, define an \(F\)-linear map
\[
s:C_1^\Delta(X;F)\longrightarrow H_1(X;F)
\]
edgewise as follows. If an oriented edge \(e\) lies on \(C_i\), put \(s(e)=\varepsilon_e z_i/\ell_i\), where \(\varepsilon_e\in\{1,-1\}\) records agreement with the chosen cycle orientation; if \(e\) is a bridge, put \(s(e)=0\). Then \(s(z_i)=z_i\) for every \(i\), so \(s\) is a chain extension. With the cointegral basis \(B=(z_1,\ldots,z_r)\),
\[
\|s\|^B=\max_i\frac{1}{\ell_i}=\frac{1}{g(X)}.
\]
Thus \(G_1^F(C_*^\Delta(X))\le 1/g(X)\).

For the lower bound, let \(s\) be any degree-one chain extension and let \(B\) be any cointegral \(F\)-basis of \(H_1(X;F)\). Cointegrality implies that every integral cycle class \(z_i\) lies in \(\mathbb ZB\). Since \(z_i\ne0\), its \(B\)-coordinate vector is a nonzero integral vector, and hence \(\|z_i\|_1^B\ge1\). Using \(s(z_i)=z_i\) and the triangle inequality,
\[
1\le \|z_i\|_1^B=\|s(z_i)\|_1^B\le \sum_{e\in C_i}\|s(e)\|_1^B\le \ell_i\|s\|^B.
\]
Choose a shortest cycle, so \(\ell_i=g(X)\). Then \(\|s\|^B\ge1/g(X)\). Taking the infimum over all chain extensions and cointegral bases proves the equality.

For the stated comparison with geometric gnarledness, let \(T\) be any ordinary spanning tree of a connected graph with a cycle. In the relative complex \(C_*^\Delta(X,T;\mathbb Q)\), the non-tree edges form a basis of \(H_1(X,T;\mathbb Q)\), every tree edge represents \(0\), and every non-tree edge represents a unit basis vector. Hence the geometric degree-one gnarledness is at most \(1\); it is at least \(1\) because the relative homology is nonzero and the admissible basis condition forces every nonzero edge class to have a nonzero integral coordinate vector. Therefore \(G_1(X)=1\).

## Verification
The proof is symbolic and uses no finite experiment. The critical points were checked directly against the definitions of chain extension, cointegral basis, algebraic gnarledness, and geometric gnarledness in Hofmann--Löh. The lower bound is uniform over all chain extensions and all cointegral bases; it is not a computation in the displayed cycle basis alone. The cactus hypothesis is used exactly to obtain edge-disjoint integral cycle generators and the edgewise upper-bound extension.

## Relationship to prior work
Hofmann--Löh introduce algebraic gnarledness and in their Example 7.13 treat a single simplicial cycle, producing the reciprocal-length upper bound. Their Proposition 7.16 gives an exact formula when the relevant homology is one-dimensional, and their coefficient-independence result applies to all subfields of \(\mathbb R\). Those statements cover the unicyclic case but do not apply directly when \(b_1(X)\ge2\), where cointegral bases may mix several integral cycle classes. The present argument shows that edge-disjoint cycle support prevents such mixing from beating the reciprocal girth bound.

The earlier geometric notion of gnarledness is due to Chambers, Dotterrer, Manin, and Weinberger. In dimension \(1\), their spanning-tree description already makes \(G_1(X)=1\) immediate for connected cyclic graphs; that geometric fact is used only for the comparison above, not claimed as new.

## Limitations
The result is restricted to cactus graphs. For graphs with overlapping cycles, the edge-disjoint support argument fails, and the exact algebraic gnarledness may depend on finer relations among cycle classes. No claim is made about a general graph formula, efficient computation of algebraic gnarledness, or behavior under arbitrary changes of marking.

## References
1. Franziska Hofmann and Clara Löh, *Quantitative chain extensions and integral cohomological fillings*, arXiv:2610.02987v1, 2 October 2026. Relevant material: Definition 2.1; Section 7, especially Definition 7.1, Example 7.13, Proposition 7.16; Section 8.3.
2. Gregory R. Chambers, Dominic Dotterrer, Fedor Manin, and Shmuel Weinberger, *Quantitative null-cobordism*, Journal of the American Mathematical Society 31 (2018), 1165--1203, DOI:10.1090/jams/903. Relevant material: the spanning-tree definition of geometric gnarledness in Section 3.
3. Clara Löh, *Cohomological fillings and gnarledness of chain complexes*, seminar slides, 28 April 2026.
