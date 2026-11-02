# The critical group of the two-token Petersen graph

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph and let \(T=F_2(P)\) be its graph of two indistinguishable tokens on distinct vertices, one token moving along one edge to an unoccupied vertex per step. The critical group is
\[
K(T)\cong (\mathbb Z/2\mathbb Z)^8\oplus(\mathbb Z/4\mathbb Z)^2\oplus\mathbb Z/28\mathbb Z\oplus\mathbb Z/1596\mathbb Z\oplus\mathbb Z/38304\mathbb Z\oplus(\mathbb Z/191520\mathbb Z)^3.
\]
This is an invariant-factor decomposition: successive nontrivial cyclic orders divide the next. The corresponding exact spanning-tree count is
\[
\tau(T)=2^{36}3^9 5^3 7^6 19^5=49253533675382566432014336000.
\]
In particular the two-token operation introduces \(3\)-, \(7\)-, and \(19\)-primary torsion, none of which occurs in the base Petersen critical group (whose order is \(2000\)).

## Assumptions and scope
The ten vertices of \(P\) are the two-element subsets of \(\{1,2,3,4,5\}\); two such subsets are adjacent precisely when disjoint. The 45 vertices of \(T\) are the two-element subsets of \(V(P)\). Distinct \(\{a,b\}\) and \(\{a,c\}\) are adjacent in \(T\) precisely when \(bc\in E(P)\). The graph is simple and connected, with exactly 120 edges. Let \(L\) be its unnormalized integer Laplacian (diagonal equal to graph degree, off-diagonal \(-1\) for adjacent configurations), and \(L'\) any principal cofactor obtained by deleting one row and the corresponding column. For the connected graph \(T\), \(K(T)=\mathbb Z^{44}/L'\mathbb Z^{44}\). No continuous particle configuration space or diagonal-collision convention is involved.

## Proof
**Exact finite Laplacian.** Fix the lexicographic ordering of ten two-element subsets of \(\{1,\ldots,5\}\) and then the lexicographic ordering of the 45 unordered pairs of these ten vertices. The adjacency rule above determines every integer entry of \(L\) without external graph data. A configuration containing an edge of \(P\) has degree four; one containing a nonedge has degree six. Hence 15 vertices have degree four, 30 have degree six, and \(|E(T)|=(15\cdot4+30\cdot6)/2=120\).

**Tree order.** Exact characteristic-polynomial evaluation gives
\[
\det(xI-L)=x(x-7)^6(x-6)^6(x-5)^4(x-3)^5(x-2)^5(x^2-13x+32)^4(x^2-13x+38)^5.
\]
The provided `verify_primary.py` forms all entries of \(L\) independently of the displayed factors and evaluates the polynomial using exact integer arithmetic. Kirchhoff's matrix-tree theorem then gives
\[
\det L'=\frac{7^6 6^6 5^4 3^5 2^5 32^4 38^5}{45}=2^{36}3^9 5^3 7^6 19^5.
\]
This also proves that the only possible primary factors of the Smith normal form occur at the five primes \(2,3,5,7,19\).

**Integral invariant factors.** For a prime \(p\) with \(e=v_p(\det L')\), compute the Smith valuations of \(L'\) over \(R=\mathbb Z/p^{e+1}\mathbb Z\). Within the remaining submatrix choose an entry of minimum \(p\)-adic valuation \(v\); write it as \(p^v u\) with \(u\) a unit modulo \(p^{e+1-v}\). Swap this entry to the current diagonal. Since every remaining entry is divisible by \(p^v\), subtraction of suitable multiples of the pivot row and pivot column clears its column and row over \(R\). These are invertible elementary operations. Induction leaves a diagonal matrix whose \(p\)-valuations are the Smith valuations, in nondecreasing order. Precision \(e+1\) is sufficient because their total is \(e\).

The exact computed distributions of \(p\)-valuations, including zero valuations and hence all 44 diagonal positions, are:

| Prime \(p\) | \(\#\{v_p=0\}\) | Positive valuation multiplicities | Sum of valuations |
| --- | ---: | --- | ---: |
| \(2\) | 28 | \(v=1:8,\ v=2:4,\ v=5:4\) | 36 |
| \(3\) | 39 | \(v=1:1,\ v=2:4\) | 9 |
| \(5\) | 41 | \(v=1:3\) | 3 |
| \(7\) | 38 | \(v=1:6\) | 6 |
| \(19\) | 39 | \(v=1:5\) | 5 |

The full modular elimination for each prime appears in `verify_primary.py` and, with a different underlying Petersen graph construction, in `verify_independent.cpp`. The programs perform the specified elementary operations rather than merely comparing guessed orders. Aligning the sorted valuation lists gives exactly 28 unit factors and the nontrivial factors
\[
\underbrace{2,\ldots,2}_{8},\quad 4,4,28,1596,38304,191520,191520,191520.
\]
Their product is \(\det L'\). By uniqueness of Smith invariant factors, this proves the asserted group decomposition. The independently constructed exact modular calculation and the determinant-order identity provide consistency checks of the entire finite certificate.

## Verification
Run `python verify_primary.py` with `networkx` and `sympy` installed; it builds the Petersen graph by a ten-vertex standard labeling, checks the exact degree sum and characteristic polynomial, performs five prime-power matrix diagonalizations, and verifies the reconstructed Smith diagonal against the spanning-tree count. Separately compile `g++ -O2 -std=c++17 verify_independent.cpp -o verify_independent` and execute `./verify_independent`; this constructs the Petersen graph directly from disjoint two-subsets of a five-set, constructs its two-token Laplacian, and independently checks the five prime-power profiles. Both checks passed on the included scripts. `certificate.json` gives the expected exact outputs in a machine-readable form. All arithmetic is exact: no floating-point spectral approximation or sampling is needed.

## Relationship to prior work
Audenaert, Godsil, Royle and Rudolph (2005/2007) studied symmetric squares of graphs, especially their ordinary adjacency spectra and cospectrality of strongly regular graphs. Fabila-Monroy and collaborators (2009/2012) defined and studied token graphs, including connectivity, diameter, colorings, cliques and Hamiltonian paths. Abdelmalek and collaborators (2020/2023) studied well-covered token graphs and explicitly considered the Petersen two-token graph in their Example 3.12. Lorenzini (2008) treated critical groups and Smith forms of graph Laplacians in general. None of the materially inspected relevant statements supplies the integral invariant-factor decomposition above. In particular, knowledge of an adjacency spectrum, or even a Laplacian spectrum, does not in general determine integral Smith factors. A related published computation of homology of a continuous two-particle Petersen configuration space concerns a different chain complex and does not yield this sandpile group.

## Limitations
This is an exact result for a fixed natural 45-vertex graph, not an infinite-family classification. The displayed Laplacian factorization is a supporting computation, not an assertion of novelty of spectral methods. The group depends on the discrete, no-collision token graph, not on the topological configuration space. Source searching and full-text comparison cannot exclude every unindexed older computation or differently named database table. Independent external validation has not been performed.

## References
1. K. Audenaert, C. Godsil, G. Royle, T. Rudolph, *Symmetric Squares of Graphs*, publicly posted 2005-07-12, arXiv:math/0507251; *Journal of Combinatorial Theory, Series B* 97 (2007), 74–90. https://arxiv.org/abs/math/0507251
2. R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia, D. R. Wood, *Token Graphs*, publicly posted 2009-10-25, arXiv:0910.4774; *Graphs and Combinatorics* 28 (2012), 365–380. https://arxiv.org/abs/0910.4774
3. F. M. Abdelmalek, E. Vander Meulen, K. N. Vander Meulen, A. Van Tuyl, *Well-Covered Token Graphs*, arXiv:2010.04539 (2020), *Discussiones Mathematicae Graph Theory* 43 (2023), 767–792, especially Example 3.12. https://arxiv.org/abs/2010.04539
4. D. Lorenzini, *Smith Normal Form and Laplacians*, *Journal of Combinatorial Theory, Series B* 98 (2008), 1271–1300, DOI:10.1016/j.jctb.2008.02.002.
