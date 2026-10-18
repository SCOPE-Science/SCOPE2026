# Dimension-independent orbit recovery in directed powers of finite chains

## Finding
For all integers \(m,d\ge1\), let \(L_{m,d}=\{0,1,\ldots,m\}^{d}\) with upward-directed arcs \(x\to y\) precisely when \(y\) is obtained from \(x\) by increasing one coordinate by one. Start all vertices with the same colour and perform synchronous one-dimensional directed counting colour refinement, using the preceding colour and the multisets of colours of incoming and outgoing neighbours. **After at most \(\lceil m/2\rceil\) rounds, two vertices have the same colour if and only if they have the same unordered multiset of coordinate values.** These colour classes are exactly the automorphism orbits of the directed cover graph. Their number is \(\binom{m+d}{d}\), and a class with multiplicities \(N_j=|\{i:x_i=j\}|\) has cardinality \(d!/\prod_{j=0}^{m}N_j!\). This dimension-independent upper bound is sharp uniformly in \(m,d\): already the one-dimensional chain requires \(\lceil m/2\rceil\) rounds.

## Assumptions and scope
The poset has the full vertex set \(\{0,\ldots,m\}^{d}\); all coordinates have the *same* length \(m+1\); edges are immediate upward covers, not the transitive closure. Refinement counts incoming and outgoing neighbours separately. The starting colouring is uniform and colour names are arbitrary, with canonical equality determined by the full signatures. Both \(m\) and \(d\) are arbitrary positive integers. The assertion concerns automorphism orbits *within this directed graph*, not comparisons between different graphs or unbounded-variable logical equivalence.

## Proof
**1. Directed paths are visible after bounded refinement.** Let \(D_t(x)\) and \(U_t(x)\) be the numbers of directed length-\(t\) walks ending at \(x\) and beginning at \(x\), respectively. Set \(D_0(x)=U_0(x)=1\). For \(t\ge1\), \(D_t(x)=\sum_{y\to x}D_{t-1}(y)\) and \(U_t(x)=\sum_{x\to y}U_{t-1}(y)\). By induction on \(r\), equality of the round-\(r\) counting-refinement colours implies equality of all \(D_t,U_t\) with \(0\le t\le r\): signatures retain the old colour and the multiplicity of every neighbouring old colour, and the previous counts are functions of those colours.

**2. Exact walk polynomials.** Define \(E_s(z)=\sum_{k=0}^{s}z^k/k!\). Any descending walk from \(x=(x_1,\ldots,x_d)\) chooses an ordered sequence of coordinate decrements, with coordinate \(i\) used at most \(x_i\) times. Therefore
\[
D_t(x)=t!\,[z^t]\prod_{i=1}^{d}E_{x_i}(z),\qquad
U_t(x)=t!\,[z^t]\prod_{i=1}^{d}E_{m-x_i}(z).
\]
This is an identity over rational formal power series, and only coefficients through \(t=r\) are used.

**3. Recover low and high coordinate multiplicities.** Put \(N_j=|\{i:x_i=j\}|\). Knowledge of \(D_0,\ldots,D_r\) determines the truncated formal logarithm
\[
G(z)=\log\bigl(\prod_iE_{x_i}(z)\bigr)\pmod {z^{r+1}}.
\]
Its linear coefficient is \(d-N_0\), because \(E_0=1\) and \(E_s=1+z+O(z^2)\) for every \(s\ge1\). Thus \(N_0\) is determined. For each \(1\le j<r\), the identity
\[
\log E_j(z)=z-\frac{z^{j+1}}{(j+1)!}+O(z^{j+2}),
\qquad \log E_s(z)=z+O(z^{j+2})\quad(s>j)
\]
shows that the coefficient of \(z^{j+1}\) in \(G\), after subtracting the contributions of already determined \(N_0,\ldots,N_{j-1}\), equals \(-N_j/(j+1)!\). Hence induction determines \(N_0,\ldots,N_{r-1}\). The same argument with \(U_t\) determines \(N_m,N_{m-1},\ldots,N_{m-r+1}\). For \(r=\lceil m/2\rceil\), these ranges cover every value \(0,\ldots,m\), except possibly the single central value \(j=r\) if \(m=2r\). In that case its multiplicity is \(d\) minus all known multiplicities. Therefore equal round-\(r\) colours force identical coordinate multisets.

**4. Converse, orbit sizes, and counts.** Every coordinate permutation preserves upward covers. Consequently, vertices with the same multiset of coordinates lie in a common automorphism orbit; a colour-refinement round never separates vertices in an automorphism orbit, by induction from uniform initial colours. Step 3 proves the reverse inclusion. The total number of weak multiplicity vectors \((N_0,\ldots,N_m)\) summing to \(d\) is \(\binom{m+d}{d}\), and their coordinate-permutation orbit cardinalities are the stated multinomial coefficients. We do not need any additional classification of all automorphisms: orbit refinement equality already proves these are the full orbits.

**5. Optimality uniformly in dimension.** For \(d=1\), an induction on refinement rounds in the directed chain \(0\to1\to\cdots\to m\) gives: the round-\(s\) colour of a vertex \(j\) is completely determined by the pair of clipped endpoint distances \((\min\{j,s\},\min\{m-j,s\})\), and different pairs have different colours. This is true initially, and in each successive round the incoming and outgoing neighbour signatures extend the visible endpoint distance by at most one. For each \(s<\lceil m/2\rceil\), at least two vertices have both distances at least \(s\), so they are indistinguishable. Because the upward-directed chain is rigid, orbit recovery has not yet occurred. Thus the uniform bound cannot be improved.

## Verification
Two standalone exact-integer Python programs accompany this document. `verify_grid.py` explicitly constructs every directed cover graph in 41 tested parameter configurations, performs synchronous refinement on 21,546 vertices, and checks orbit equality and class cardinalities; it prints `EXPLICIT_GRID_REFINEMENT_PASS`. `verify_walks.py` separately implements the walk-generating-function identity by integer binomial convolution, tests 45,731 coordinate-orbit profiles across 88 parameter configurations, and checks one-dimensional sharpness through \(m=29\); it prints `WALK_POLYNOMIAL_INJECTIVITY_PASS`. Run `python3 verify_grid.py` and `python3 verify_walks.py` from this package directory; their exact output records are `verify_grid.out.txt` and `verify_walks.out.txt`. These finite tests are supporting evidence only; the five-step argument proves the all-parameter theorem.

## Relationship to prior work
Cartesian powers and their automorphism groups have a classical structural literature. Albertson (2005), particularly its Section 2, cites the prime-factor automorphism theorem and proves distinguishing-number results for undirected Cartesian powers; this is not a counting-colour-refinement orbit theorem or a depth bound for upward-directed chain products. Arvind, Köbler, Rattan and Verbitsky (2015), Sections 1 and 8, treat general undirected graph colour refinement and the notion of *refinable* graphs, but do not give the specified family-wide directed-product theorem. Bachman and collaborators (2011), Sections on quotient graphs, discuss equitable partitions of Cartesian products in undirected quantum-walk settings rather than the stated refinement depth. The present argument supplies the explicit directed lattice orbit-recovery statement and its dimension-independent sharp round count. Related literature may contain specialized prior formulations; no publication-priority claim is made.

## Limitations
Uniform chain length and separate directed in/out counts are essential hypotheses. The statements do not extend here to heterogeneous factors, undirected cover graphs, ordinary graph isomorphism on arbitrary posets, or marked vertices. The optimality assertion is uniform and is witnessed by \(d=1\); no claim is made that every higher dimension individually needs the same number of rounds. The literature comparison is finite and cannot establish uniqueness of an earlier result, and no independent external mathematical audit has occurred.

## References
1. M. O. Albertson, *Distinguishing Cartesian Powers of Graphs*, Electronic Journal of Combinatorics **12** (2005), N17, published 2005-09-19. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v12i1n17/pdf/
2. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (2015). https://arxiv.org/pdf/1502.01255
3. R. Bachman et al., *Perfect State Transfer on Quotient Graphs*, arXiv:1108.0339 (2011). https://arxiv.org/pdf/1108.0339
