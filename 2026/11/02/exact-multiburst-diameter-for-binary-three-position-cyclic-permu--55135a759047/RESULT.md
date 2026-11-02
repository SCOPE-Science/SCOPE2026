# Exact multiburst diameter for binary three-position cyclic permutations

## Finding

Let \(n\ge 3\) and \(1\le k\le n-1\) be integers. On binary length-\(n\) words of Hamming weight \(k\), a step cyclically rotates any *contiguous* triple of symbols left or right. For words \(x,y\) of that weight, write \(d_3(x,y)\) for the least number of such steps taking \(x\) to \(y\). Then all these words are mutually reachable and

\[
\boxed{\max_{\mathrm{wt}(x)=\mathrm{wt}(y)=k} d_3(x,y)=\left\lceil\frac{k(n-k)}2\right\rceil.}
\]

The words \(1^k0^{n-k}\) and \(0^{n-k}1^k\) attain the maximum. In particular, taking the maximum over nonconstant input compositions gives \(\left\lceil\lfloor n^2/4\rfloor/2\right\rceil\). Thus the precise worst-case sequence length for repeated three-position cyclic-permutation bursts is quadratic, even though one burst changes only one length-three window.

## Assumptions and scope

The alphabet is binary, positions are ordered without wraparound, and every operation is one of the two nontrivial cyclic rotations of a consecutive *three*-position window; an operation fixing the word may be omitted. The length, Hamming weight and locations of ones are as stated above. This is a distance/reachability theorem for an arbitrary number of **sequential** such bursts, not an optimal code-size or single-burst correction result. All logarithms are absent from the theorem. The graph \(P_n^2\) has vertices \(1,\ldots,n\), with an edge whenever \(1\le |i-j|\le2\). The \(k\)-token graph \(F_k(G)\) has one vertex for each \(k\)-subset of \(V(G)\), joined by one edge when precisely one token moves to an unoccupied adjacent vertex of \(G\).

## Proof

**1. Identify the exact channel graph.** In any binary triple of weight one or two, its three cyclic rotations exhaust its three distinct permutations. Any nontrivial rotation therefore moves a single exceptional symbol between two of its three positions, swapping unequal bits at positions separated by one or two. Conversely, every swap of unequal symbols at positions \(i,j\) with \(1\le|i-j|\le2\) occurs as a rotation of a triple containing them: for a distance-two swap take the window with those endpoints; for an adjacent swap take one of the adjacent triples, possible since \(n\ge3\). Thus the weight-\(k\) channel graph is *exactly* \(F_k(P_n^2)\).

**2. Establish a transport-distance identity.** Let \(G\) be any finite connected undirected graph and \(S,T\) be equally large occupied vertex sets. Consider nonnegative integer flows \(f_{uv}\) on both directed versions of each edge, with net outflow \(\sum_v(f_{uv}-f_{vu})=\mathbf1_S(u)-\mathbf1_T(u)\). Each unit of arc flow costs one. A feasible minimum-cost integer flow exists by integral network-flow theory; since each arc costs one, any such optimum contains no positive directed cycle (nor antiparallel cancellation). Every token-move path gives a feasible flow, so its length is at least the minimum flow cost.

For the reverse inequality, start from an **acyclic minimum-cost integral flow** and the occupied set \(X=S\). If \(X\ne T\), the occupied set \(X\) has strictly positive total divergence \(\sum_{u\in X}(\mathbf1_X(u)-\mathbf1_T(u))=|X\setminus T|>0\). By flow conservation this is the flow leaving \(X\) minus the flow entering \(X\). Therefore at least one arc of positive flow goes from an occupied vertex to an unoccupied one. Make that legal token move and subtract one unit from the arc. The residual flow still has divergence \(\mathbf1_{X'}-\mathbf1_T\). Repeat. Whenever \(X\ne T\), a legal positive-flow arc exists, and every step decreases the total remaining flow by one. If \(X=T\), the residual flow has zero divergence and (being a subflow of an acyclic flow) must be zero. Hence the process ends after precisely the original total flow cost in moves. Consequently the token distance equals the minimum integral flow cost. The finite connected case is also covered when \(S=T\), with both sides zero.

The integral min-cost flow dual (vertex-edge incidence is totally unimodular and edge costs are integers) gives the equivalent *integer Lipschitz-potential formula*

\[
 d_{F_k(G)}(S,T)=\max_{\phi:V(G)\to\mathbb Z,\;|\phi(u)-\phi(v)|\le1\;(uv\in E(G))}\left(\sum_{u\in S}\phi(u)-\sum_{v\in T}\phi(v)\right).
\]

The finite connected graph permits a potential fixed to zero at one vertex; an integral optimum follows from integral difference constraints. Maximizing over \(S,T\) as well, the diameter is the maximum, over integer edge-\(1\)-Lipschitz potentials \(\phi\), of the sum of their \(k\) largest values minus the sum of their \(k\) smallest values.

**3. Constrain the sorted potentials.** Since \(P_n^2\) remains connected after removal of any one vertex, it is two-vertex-connected. For an integer \(1\)-Lipschitz \(\phi\), write its \(n\) values in nondecreasing order \(a_1\le\cdots\le a_n\). If \(a_{i+2}\ge a_i+2\), the nonempty sets of vertices with values at most \(a_i\), respectively at least \(a_i+2\), have no edges between them, and removing at most one intermediate-value vertex separates them. This contradicts two-vertex-connectivity. Hence \(a_{i+2}-a_i\le1\). In particular, consecutive differences \(\delta_i=a_{i+1}-a_i\) belong to \(\{0,1\}\), and no two adjacent differences are one.

**4. Bound all pairs.** Complementing all bits is a graph isomorphism from weight \(k\) to weight \(n-k\), so assume \(k\le n/2\), and put \(m=n-k\). The sum of the top \(k\) values minus the bottom \(k\) equals

\[
 H=\sum_{i=1}^{k}(a_{m+i}-a_i)
  =\sum_{i=1}^{k}\sum_{j=i}^{i+m-1}\delta_j.
\]

If \(m=2h\), each length-\(m\) block of differences contains at most \(h\) ones, yielding \(H\le kh=km/2\). If \(m=2h+1\), each contains at most \(h+1\) ones. Whenever one has the maximum \(h+1\), it is forced to alternate \(1,0,1,0,\ldots,1\); the immediately following length-\(m\) block has only \(h\) ones. Thus no two consecutive blocks among the \(k\) blocks can both attain \(h+1\). At most \(\lceil k/2\rceil\) blocks do, giving

\[
 H\le kh+\lceil k/2\rceil=\lceil km/2\rceil.
\]

The dual identity proves \(d_3(x,y)\le\lceil k(n-k)/2\rceil\) for all equal-weight \(x,y\).

**5. Prove attainment.** Choose \(S=\{1,\ldots,k\}\) and \(T=\{n-k+1,\ldots,n\}\), the positions of ones in the two stated words. Both \(\phi_0(j)=\lfloor(j-1)/2\rfloor\) and \(\phi_1(j)=\lceil(j-1)/2\rceil\) are integer edge-\(1\)-Lipschitz on \(P_n^2\). Their pointwise sum is \(j-1\), so the sum of their two signed \(T\)-minus-\(S\) differences is exactly \(k(n-k)\). At least one signed difference is at least \(\lceil k(n-k)/2\rceil\); apply the dual identity with the negative of that potential. This matches the upper bound and proves the exact diameter and the extremal pair. \(\square\)

## Verification

Two standalone, dependency-free source programs accompany this result. Compile `verify.cpp` using a C++17 compiler (`c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`). It constructs **actual** length-three cyclic rotations, checks that every neighborhood equals the distance-one-or-two unequal-bit-swap neighborhood, and runs all-pairs breadth-first search for every \(3\le n\le15\), \(1\le k\le\lfloor n/2\rfloor\). It checks the claimed diameter for every parameter and checks connectedness; by complementation this covers all weights. Its run checks 110,998,233 ordered pairs and reports `VERIFY_OK`.

Run `python3 verify_transport.py` for an independent check of all 66,174 ordered pairs for \(3\le n\le9\), using independently coded BFS, brute-force dynamic-programming minimum-cost matchings with ground distance \(\lceil|i-j|/2\rceil\), and the claimed diameter. It reports `TRANSPORT_VERIFY_OK`. These finite tests are not the proof of the all-parameter statement; the graph/flow/dual/sorted-potential argument above is the proof.

## Relationship to prior work

Chen and Milenkovic introduced permutation-burst correction motivated by storage and studied length-three cyclic errors, their four local error patterns, redundancy bounds and single-error correcting codes. Their Proposition 3 (§V) gives the relevant one-move patterns; the present theorem concerns *arbitrarily many sequential moves* and exactly determines the global composition-dependent graph diameter, not a new single-error code. Fabila-Monroy et al. introduced token graphs and gave generic diameter bounds \(k(\delta-k+1)\le\operatorname{diam}F_k(G)\le k\delta\) for connected \(G\) of diameter \(\delta\); these inequalities do not determine the present exact value. Adame, Rivera and Trujillo-Negrete identify \(F_k(P_n^2)\) as the graph of the one-or-two-apart transposition rule in their Gray-code appendix, but their conclusions address Hamiltonicity, not this diameter. The 2025 supertoken-graph paper concerns multiple tokens per vertex and different metric-dimension and diameter questions. The new proof exploits integral transport duality and the sorted-potential consequence of two-connectivity. The exact relation was not identified in the inspected relevant references; an unindexed earlier calculation remains possible.

## Limitations

The statement is exact only for binary words of fixed nontrivial weight, windows of exactly three positions, unbounded *sequential* cyclic rotations, and non-circular positions. It does not determine optimal error-correcting code sizes, the distance distribution, shortest-path multiplicities, or corresponding diameters for longer windows, nonbinary alphabets, or simultaneously applied disjoint bursts. The occurrence of the same graph in earlier Gray-code work makes mathematical publication priority a residual risk. No independent external mathematical audit has been performed.

## References

1. Y.-P. Chen and O. Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, first posted 2026-10-11. https://arxiv.org/html/2610.15701v1 (especially §V, Proposition 3).
2. R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia, and D. R. Wood, *Token Graphs*, arXiv:0910.4774v1, 2009; *Graphs and Combinatorics* 28 (2012), 365–380. https://arxiv.org/html/0910.4774v1 (especially §3, Theorem 1).
3. L. E. Adame, L. M. Rivera, and A. L. Trujillo-Negrete, *Hamiltonicity of Token Graphs of some Join Graphs*, arXiv:2101.01855, first posted 2021-01-06; *Symmetry* 13 (2021), 1076. https://arxiv.org/abs/2101.01855 (especially the Gray-code appendix).
4. *On some metric properties of supertoken graphs*, *Utilitas Mathematica* 123 (2025), published 2025-06-26. https://combinatorialpress.com/um-articles/vol-123/on-some-metric-properties-of-supertoken-graphs/ (especially §3).
