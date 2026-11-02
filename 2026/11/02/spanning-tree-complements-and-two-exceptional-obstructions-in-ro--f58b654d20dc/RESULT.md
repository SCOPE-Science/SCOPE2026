# Spanning-tree complements and two exceptional obstructions in rook-graph actuation

## Finding

For integers \(m,n\ge3\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\), with unit edge weights and graph Laplacian \(L\). Each of its \(mn\) vertices is a cell \((i,j)\), \(1\le i\le m\), \(1\le j\le n\). Give a selected set \(U\) independent coordinate inputs, so that
\[
\dot z=-Lz+B_Uu,\qquad B_U=[e_{(i,j)}:(i,j)\in U].
\]
Then the minimum number of coordinate actuators achieving Kalman controllability is
\[
q_{m,n}=(m-1)(n-1).
\]
For any \(|U|=q_{m,n}\), regard its complement \(T=([m]\times[n])\setminus U\) as the edge set of a bipartite graph on labeled row vertices \(r_1,\ldots,r_m\) and column vertices \(c_1,\ldots,c_n\). All minimum controllable sets are characterized as follows.

**Rectangular case \(m\ne n\).** The set \(U\) is controllable if and only if \(T\) is a spanning tree of \(K_{m,n}\). The number of such labeled sets is
\[
A_{m,n}=m^{\,n-1}n^{\,m-1}.
\]

**Square case \(m=n=s\).** The set \(U\) is controllable if and only if \(T\) is a spanning tree and neither of the following occurs:

1. \(T\) is a *double star*: for some row \(r_i\) and column \(c_j\), all \(2s-1\) edges incident to \(r_i\) or \(c_j\) belong to \(T\).
2. There exist a row \(r_i\), a column \(c_j\), and an edge \((r_k,c_\ell)\), with \(k\ne i\) and \(\ell\ne j\), such that \(T\) consists of every edge joining \(r_i\) to a column other than \(c_j\), every edge joining \(c_j\) to a row other than \(r_i\), and the single additional edge \((r_k,c_\ell)\).

The square-case exact enumeration is
\[
\boxed{A_{s,s}=s^{2s-2}-s^2\bigl((s-1)^2+1\bigr).}
\]
For instance, there are \(36\) minimum controllable placements on \(R_{3,3}\) and \(3936\) on \(R_{4,4}\). In the square case, the two excluded types respectively number \(s^2\) and \(s^2(s-1)^2\); they are disjoint.

An explicit minimum placement follows without searching: for \(m\ne n\), take every cell outside a fixed row and fixed column (the omitted cells form a double-star tree). For \(m=n=s\), begin with that double-star tree, replace one edge \((r_1,c_2)\) by \((r_2,c_2)\), and actuate its complementary cells. This replacement preserves the spanning-tree property but avoids both exceptional types. Thus the familiar rectangular-block actuator placement works for unequal dimensions and fails at equal dimensions, where a one-edge exchange repairs it.

The ordinary zero-forcing number provides a comparison for stronger, weight-robust control guarantees:
\[
Z(R_{m,n})=(m-1)(n-1)+1.
\]
Thus this fixed unit-weight Laplacian has a strict one-actuator advantage over zero forcing. The zero-forcing count is included as a checkable comparison, not an independent originality claim.

## Assumptions and scope

Only the undirected, unweighted rook graph with both dimensions at least three is covered. Actuation is by **independent coordinate inputs**: every selected vertex receives a distinct input channel. The dynamic matrix is the full negative graph Laplacian, not a grounded follower submatrix, a random weighted realization, or an arbitrary sign pattern. Controllability means full-state Kalman controllability over \(\mathbb R\), equivalently the Popov–Belevitch–Hautus (PBH) test for each Laplacian eigenspace.

A spanning tree of \(K_{m,n}\) includes all \(m+n\) labeled vertices. In the second excluded square type, the central pair \((r_i,c_j)\) is **not** an edge of \(T\); this distinguishes it from the double-star type.

## Proof

### 1. The four eigenspaces and the lower bound

Identify a state vector with an \(m\)-by-\(n\) matrix \(X=(X_{ij})\). The Laplacian is the Kronecker sum of \(mI_m-J_m\) and \(nI_n-J_n\). Consequently its eigenspaces are:

* eigenvalue \(0\): constant matrices, dimension \(1\);
* eigenvalue \(m\): \(X_{ij}=x_i\), with \(\sum_i x_i=0\), dimension \(m-1\);
* eigenvalue \(n\): \(X_{ij}=y_j\), with \(\sum_j y_j=0\), dimension \(n-1\);
* eigenvalue \(m+n\): matrices with every row sum and every column sum zero, dimension \((m-1)(n-1)\).

For \(m=n\), the middle two spaces combine into a single eigenspace of dimension \(2(m-1)\). Since \((m-1)(n-1)\ge m-1,n-1\) and \((s-1)^2\ge2(s-1)\) for \(s\ge3\), the largest eigenspace has dimension \(q_{m,n}\). The PBH test forces \(|U|\ge q_{m,n}\) for coordinate inputs. The constructions below attain equality, so this is the sharp minimum.

### 2. The tree criterion from the largest eigenspace

Let \(|U|=q_{m,n}\), so \(|T|=m+n-1\). A vector in the eigenspace of eigenvalue \(m+n\) vanishes on every selected vertex precisely when it is a matrix supported on the cells of \(T\) and with zero row and column sums. These equations form the unsigned incidence kernel of the bipartite graph \(T\). Because this graph is bipartite, multiplying the column-vertex incidence equations by \(-1\) transforms them into oriented flow conservation. A nonzero such flow exists exactly when \(T\) has a cycle. Thus PBH holds for the largest eigenspace exactly when \(T\) is a forest. A forest on \(m+n\) vertices with \(m+n-1\) edges is a spanning tree.

In particular, **all** minimum controllable placements must have spanning-tree complements. Conversely, a spanning tree passes the high-eigenvalue PBH test.

### 3. Why unequal dimensions have no further obstructions

Suppose \(m\ne n\) and \(T\) is a spanning tree. If a nonzero eigenvector from the \(m\)-eigenspace vanished on \(U\), then every row with \(x_i\ne0\) would have all \(n\) corresponding edges in \(T\). The sum-zero condition on the \(x_i\) requires at least two such rows. Two fully present rows make a four-cycle in \(T\), contrary to the tree assumption. The identical argument with columns applies to the \(n\)-eigenspace. The constant eigenspace is observed at every nonempty \(U\). Hence every spanning-tree complement is controllable for unequal dimensions.

The classical complete-bipartite spanning-tree count, obtainable from the matrix-tree theorem, is \(m^{n-1}n^{m-1}\). This proves the rectangular enumeration.

### 4. The additional square-case PBH test

Now put \(m=n=s\). The eigenvalue \(s\) has all matrices of the form \(X_{ij}=x_i+y_j\), where \(\sum_i x_i=\sum_j y_j=0\). Let \(H\) be the bipartite graph whose edges are the **selected** cells \(U\), and suppose it has connected components \(C_1,\ldots,C_h\). Let \(a_t\) be the number of row vertices and \(b_t\) the number of column vertices in component \(C_t\); isolated vertices are included as singleton components.

The equations \(x_i+y_j=0\) on every edge of \(H\) say that on each component the row variables have a common value \(c_t\) and the column variables have the opposite value \(-c_t\). This remains valid for a component consisting of an isolated vertex. The two zero-sum conditions become
\[
\sum_{t=1}^{h}a_t c_t=0,\qquad \sum_{t=1}^{h}b_t c_t=0.
\]
There is a nonzero obstructing eigenvector exactly when this \(2\)-by-\(h\) coefficient matrix has a nonzero kernel. Hence a tree complement passes the remaining PBH test if and only if \(h=1\), or \(h=2\) with \(a_1b_2\ne a_2b_1\). For two components, since both bipartition classes have total size \(s\), failure is equivalent to \(a_1=b_1\).

### 5. Exhausting the square-case exceptions

The graph \(H\) has exactly \((s-1)^2\) edges. If \(h\ge3\), write \(d_t=a_t+b_t\) for the component orders. Then
\[
|E(H)|\le\sum_t a_tb_t\le\tfrac14\sum_t d_t^2,
\qquad \sum_t d_t=2s.
\]
If the largest \(d_t\) is at most \(2s-3\), then with at least three positive integer component orders, convexity bounds the sum of squares by \((2s-3)^2+2^2+1^2\). For every \(s\ge3\), one-quarter of this bound is strictly less than \((s-1)^2\), a contradiction. Thus the largest component has order \(2s-2\), with two other singleton components. To have \((s-1)^2\) edges, the large component must be all of \(K_{s-1,s-1}\), and the two singleton components must be one row vertex and one column vertex. Its complement is exactly an excluded double star. There are \(s^2\) choices.

If \(h=2\) and the coefficient matrix has deficient rank, both components are balanced: one has \(t\) rows and \(t\) columns, and the other has \(s-t\) of each, for some \(1\le t\le s-1\). Therefore
\[
(s-1)^2=|E(H)|\le t^2+(s-t)^2=s^2-2t(s-t),
\]
so \(t(s-t)\le s-1\). This is possible only for \(t=1\) or \(t=s-1\). The smaller component must contain its one possible edge or it would split into two isolated components; the larger component has all but one of its \((s-1)^2\) possible edges. Taking complements yields exactly the second excluded type. There are \(s^2(s-1)^2\) choices, and its complement is indeed a spanning tree: the two cross stars are joined by the one edge internal to the large block.

No other tree complement fails PBH. The two excluded families are disjoint because their selected graphs have respectively three and two components. Subtracting them from the \(s^{2s-2}\) spanning trees of \(K_{s,s}\) proves the square formula and establishes existence of minimum placements for all \(s\ge3\).

### 6. The zero-forcing comparison

A zero-forcing set controls the fixed graph Laplacian, by the standard zero-forcing propagation/PBH argument. Therefore a zero-forcing set of size \(q_{m,n}\) would have to be a minimum controllable set, whose complementary white cells form a spanning tree. For any black cell not in that tree, its row vertex and column vertex in the tree both have positive degree; the black cell therefore has **at least two distinct white rook-neighbors**. No force can start. Thus \(Z(R_{m,n})\ge q_{m,n}+1\).

For the reverse inequality, choose a row \(r_0\) and a distinct row \(r_1\), and choose a column \(c_0\). Declare white exactly the cells in row \(r_1\) and those cells \((r_i,c_0)\) with \(r_i\notin\{r_0,r_1\}\). There are \(n+m-2\) white cells, giving \(mn-(m+n-2)=q_{m,n}+1\) black cells. Every white cell \((r_1,c_j)\) for \(j\ne0\) is forced from \((r_0,c_j)\); then the cells \((r_i,c_0)\) for \(i\notin\{0,1\}\) are forced from any \((r_i,c_j)\) with \(j\ne0\); finally \((r_1,c_0)\) is forced. This proves \(Z(R_{m,n})\le q_{m,n}+1\), establishing the exact comparison.

## Verification

The companion file `verify_rook.py` uses only the Python standard library and exact modular arithmetic over the prime \(1000003\). Running `python verify_rook.py` checks every minimum-size control selection for \((m,n)\in\{(3,3),(3,4),(4,4),(3,5)\}\): \(18{,}925\) candidate sets in total. It compares the stated combinatorial criterion with independently assembled eigenspace restriction matrices, checks every \(3\)-by-\(3\) candidate through the full Kalman matrix, and tests selected larger full Kalman matrices. It also exhaustively checks the zero-forcing minimum for the \(3\)-by-\(3\) and \(3\)-by-\(4\) cases. The script prints `PASS` when all assertions hold; it has been executed successfully.

These finite tests cannot establish the universal statements; the proof above covers all integers in the stated range. No floating-point spectral degeneracy tolerance is used in the reported checks.

## Relationship to prior work

Rahmani, Ji, Mesbahi and Egerstedt (2009) study symmetry and equitable partitions as general obstructions to multi-agent controllability. Chapman, Nabi-Abdolyousefi and Mesbahi (2012) develop control-product and layered-input constructions for Cartesian networks; their distinct-eigenvalue product argument is not an all-minimum-placement classification for the repeated-spectrum product here. Yuan and collaborators (2013) establish the general maximum-eigenvalue-multiplicity approach; the lower bound \(q_{m,n}\) is an instance of that known principle, but it does not give the enumerated coordinate-input locations or the two square-specific exclusions. Monshizadeh, Zhang and Camlibel (2014) establish the general zero-forcing/strong structural controllability relationship; the resulting comparison is not claimed as an original zero-forcing theorem. Dai (first online 2022) studies minimum leader selection for other undirected graph families using critical sets; the inspected text does not contain this rook-graph enumeration.

The assessed contribution is the **exact characterization and count of every minimum coordinate-actuation placement** on all rectangular rook graphs, including the two spectrally exceptional balanced families. These are graph-specific conclusions proved here, not claims that the PBH criterion, spectral product decomposition, tree enumeration, or zero forcing is new.

## Limitations

The theorem is limited to unit-weight Laplacian dynamics and independent coordinate channels. It need not hold if edge weights vary or one input broadcasts to several selected vertices. The argument proves exact algebraic controllability, not uniform numerical conditioning, actuator reliability or robustness to changes in weights. Exhaustive checks cover only the stated small dimensions. A directed search of accessible specialist literature and a semantic overlap search did not find an equivalent all-placement theorem, but unavailable or unindexed historical work could still subsume it. No independent mathematical audit has been performed.

## References

1. A. Rahmani, M. Ji, M. Mesbahi and M. Egerstedt, *Controllability of Multi-Agent Systems from a Graph-Theoretic Perspective*, SIAM J. Control Optim. **48** (2009), 162–186. https://doi.org/10.1137/060674909 (published online 11 February 2009).
2. A. Chapman, M. Nabi-Abdolyousefi and M. Mesbahi, *On the Controllability and Observability of Cartesian Product Networks*, IEEE CDC (2012). https://depts.washington.edu/uwrainlab/wordpress/wp-content/uploads/2019/02/On_the_controllability_and_observability_of_cartesian_product_networks.pdf
3. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, *Exact Controllability of Complex Networks*, Nature Communications **4** (2013), article 2447. https://doi.org/10.1038/ncomms3447 (published 12 September 2013).
4. N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero Forcing Sets and Controllability of Dynamical Systems Defined on Graphs*, IEEE Trans. Automat. Control **59** (2014), 2562–2567. https://arxiv.org/abs/1403.4868 (first arXiv submission 19 March 2014).
5. L. Dai, *Minimum Leader Selection for Controllability of Undirected Graphs with Leader–Follower Framework*, IET Control Theory Appl. **17** (2023), 505–515. https://doi.org/10.1049/cth2.12385 (first online 29 October 2022).
