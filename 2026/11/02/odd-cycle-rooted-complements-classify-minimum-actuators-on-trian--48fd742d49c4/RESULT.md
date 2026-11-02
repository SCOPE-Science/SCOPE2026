# Odd-cycle-rooted complements classify minimum actuators on triangular graphs

## Finding

For each integer \(n\ge5\), let \(J(n,2)=L(K_n)\) be the triangular graph: its \(\binom n2\) vertices are the unordered pairs of \(\{1,\ldots,n\}\), with two pairs adjacent exactly when they intersect. Let \(\mathcal L\) be the unit-edge graph Laplacian. Attach an independent scalar control to every graph vertex in a set \(U\), giving the full-state linear system \(\dot x=-\mathcal Lx+E_Uu\), where \(E_U\) has the corresponding coordinate columns.

The minimum possible size of such a controllable set is
\[
q_n=\binom n2-n.
\]
For any set \(U\) of this size, form a graph \(F\) on the *original* \(n\) labels with edge set \(E(K_n)\setminus U\). Then \((\mathcal L,E_U)\) is controllable **if and only if** every connected component of \(F\) is an odd-unicyclic graph (exactly one cycle, of odd length), **except** that for \(n=6\) the graph consisting of two disjoint triangles fails. Equivalently, the sole exceptional candidate is \(U=K_{3,3}\) as an edge subset of \(K_6\).

For every \(n\ge5\), one explicit minimum set is
\[
U_*=\bigl\{\{i,j\}:2\le i<j\le n\bigr\}\setminus\bigl\{\{2,3\}\bigr\}.
\]
Thus control every pair entirely within \(\{2,\ldots,n\}\), except one pair; no pair incident with label \(1\) is controlled. Despite achieving the minimum, \(U_*\) is **not** a zero-forcing set of the triangular graph: every controlled vertex has at least two uncontrolled neighbors at the outset.

The number of distinct minimum controllable sets is also exact. Define \(T(z)\) as the formal power series with \(T(0)=0\) satisfying \(T(z)=z\exp(T(z))\). Then, for \(n\ge5\),
\[
A_n=n!\,[z^n]\exp\!\left(\frac{\operatorname{artanh}(T(z))-T(z)}2\right)-10\,\mathbf1_{\{n=6\}}.
\]
In particular, \(A_5=162\), \(A_6=2520\), and \(A_7=45615\). For the small boundary cases, the minimum controller counts are \(q_3=2\) and \(q_4=3\); the stated odd-unicyclic classification is only for \(n\ge5\).

## Assumptions and scope

All graphs are simple and undirected. Each edge of \(J(n,2)\) has conductance one. Each control in \(u\) is independent and applied directly to exactly one state coordinate. Controllability refers to the complete \(\binom n2\)-dimensional state space, with no grounded or removed state coordinates. A connected odd-unicyclic graph consists of one odd cycle and arbitrary (possibly empty) trees attached to its cycle vertices. The formal coefficient \([z^n]\) is the coefficient of \(z^n\) in a power series over rational numbers.

The classification is for this fixed, unweighted Laplacian and coordinate-selecting control matrices; it does not assert controllability uniformly over arbitrary changes to graph weights or arbitrary matrices with the same nonzero pattern.

## Proof

**1. Spectral reduction.** Let \(N=\binom n2\). Let \(C\) be the \(n\)-by-\(N\) unsigned vertex-edge incidence matrix of \(K_n\); the column indexed by \(\{i,j\}\) has ones in rows \(i,j\). Direct multiplication gives
\[
C C^{\mathsf T}=(n-2)I_n+\mathbf1_n\mathbf1_n^{\mathsf T},\qquad
\mathcal L=(2n-2)I_N-C^{\mathsf T}C.
\]
The first matrix has eigenvalues \(2n-2\) once and \(n-2\) with multiplicity \(n-1\). Therefore the Laplacian eigenspaces are
\[
\begin{array}{c|c|c}
\text{eigenvalue}&\text{eigenspace}&\text{dimension}\\\hline
0&\operatorname{span}\{\mathbf1_N\}&1\\
n&\{C^{\mathsf T}a:\mathbf1_n^{\mathsf T}a=0\}&n-1\\
2n-2&\ker C&N-n.
\end{array}
\]
For \(n\ge5\), the largest multiplicity is \(N-n\); the symmetric-matrix PBH test forces \(|U|\ge N-n\) for independent coordinate actuators.

**2. Largest eigenspace and odd cycles.** Now suppose \(|U|=N-n\) and put \(F=E(K_n)\setminus U\), so \(|F|=n\). A vector in \(\ker C\) that vanishes on all controlled coordinates is precisely a vector supported on \(F\) in \(\ker C_F\). Hence this eigenspace is observable from \(U\) precisely when the square matrix \(C_F\) is nonsingular.

The equation \(C_F^{\mathsf T}a=0\) says \(a_i+a_j=0\) along every edge of \(F\). On a connected component, this admits a nonzero solution precisely if the component is bipartite: alternate signs across its bipartition. An odd cycle forces the amplitude to vanish on its entire component. Therefore \(C_F\) is nonsingular exactly when every component contains an odd cycle. Because \(F\) has exactly as many edges as vertices, each component must then have exactly one cycle, necessarily odd. This establishes the odd-unicyclic criterion for the eigenspace of eigenvalue \(2n-2\).

**3. The second eigenspace and its unique exception.** A vector of eigenvalue \(n\) has the form \(C^{\mathsf T}a\), where \(\mathbf1_n^{\mathsf T}a=0\). It vanishes on \(U\) exactly when
\[
a_i+a_j=0\quad(\{i,j\}\in U),\qquad \sum_{i=1}^n a_i=0.
\]
View \(U\) as a graph on the original \(n\) labels. Since \(|U|=\binom{n-1}{2}-1\), if \(U\) is disconnected then it must be one isolated vertex together with \(K_{n-1}\) minus one edge. Indeed a disconnection with no isolated vertex has at most \(\binom{n-2}{2}+1<\binom{n-1}{2}-1\) edges for \(n\ge5\). The nonisolated component contains a triangle; the displayed equations make \(a\) zero there, then the zero-sum equation makes it zero at the isolate.

If \(U\) is connected and nonbipartite, the odd cycle again forces \(a=0\). If it is connected and bipartite, the solutions are \(+t\) on one bipartition class and \(-t\) on the other. For odd \(n=5\), the zero-sum constraint forces \(t=0\). For \(n\ge7\), the edge count \(\binom{n-1}{2}-1=n(n-3)/2\) exceeds the bipartite maximum \(\lfloor n^2/4\rfloor\), so this case cannot arise. For \(n=6\), nine edges achieve the bipartite maximum only for \(U=K_{3,3}\), whose two equal-size classes give an unobservable nonzero zero-sum vector. Its complement is exactly two disjoint triangles, which pass the odd-unicyclic test from Step 2. This is the only additional failure.

The zero-eigenvalue vector \(\mathbf1_N\) is nonzero on every nonempty \(U\). The PBH test, applied to all three eigenspaces, now proves the equivalence.

**4. Attainment and boundary dimensions.** For \(U_*\), the complement \(F\) is the star of \(1\) plus the edge \(\{2,3\}\). It is connected with precisely one triangle, and its complement graph \(U_*\) is an isolated vertex together with \(K_{n-1}\) minus one edge. It therefore passes both eigenspace tests for every \(n\ge5\), proving the claimed minimum. In \(J(n,2)\), every vertex \(\{i,j\}\in U_*\) is adjacent to the two white vertices \(\{1,i\}\) and \(\{1,j\}\). Hence no initially controlled vertex can perform even one zero-forcing move.

For \(n=4\), the eigenvalue multiplicities are \(1,3,2\). Control the three pair-vertices \(\{2,3\},\{2,4\},\{3,4\}\). Their restrictions detect the zero-sum incidence eigenspace, and the three complementary star columns are independent, proving three controls suffice. For \(n=3\), \(J(3,2)\) is a triangle and any two controls suffice. Eigenvalue multiplicities prove both small-size lower bounds.

**5. Exact number of minimum sets.** A connected odd-unicyclic labeled graph is an undirected odd cycle of length \(\ell\ge3\), with a rooted labeled tree attached to each cycle vertex. The exponential generating function for rooted labeled trees is \(T(z)=z\exp T(z)\). Thus the exponential generating function for one connected odd-unicyclic component is
\[
\sum_{\substack{\ell\ge3\\\ell\ \mathrm{odd}}}\frac{T(z)^\ell}{2\ell}
=\frac{\operatorname{artanh}(T(z))-T(z)}2.
\]
The labeled exponential formula gives the exponential of this series for a set of such components. Every resulting complement of order \(n\ge5\) is valid, except for the \(\tfrac12\binom63=10\) two-triangle complements when \(n=6\). This proves the coefficient formula and its stated values.

## Verification

Run `python verify.py` from the same directory as this file. The standalone standard-library script produces `VERIFY_OK 6600` and independently assembles line-graph Laplacians to check the three PBH ranks and selected full Kalman matrices modulo the prime `1000003`. It exhaustively checks all \(\binom{10}{5}=252\) complementary edge subsets for \(n=5\) and all \(\binom{15}{6}=5005\) for \(n=6\), finding respectively \(162\) and \(2520\) controllable minimum sets. It also checks deterministic sampled cases for \(n=7,8\), the explicit construction through \(n=11\), and the formal-series counts through \(n=8\). The all-dimensional assertions are proved in Steps 1–5; the finite computations are stress tests, not extrapolated proofs.

## Relationship to prior work

The maximum-eigenvalue-multiplicity lower bound and a general independent-input controllability framework are established by Yuan et al. (2013). Combined with the known triangular-graph spectrum, this already implies the *numerical minimum controller count*; that count is not presented as an independent novelty claim. The specific new statement assessed here is the **if-and-only-if classification of every minimum coordinate-actuator placement, with the isolated six-label exception**, together with its enumeration and constructive non-zero-forcing example.

Monshizadeh, Zhang and Camlibel (2014) characterize zero forcing as a criterion for controllability across an entire qualitative matrix class. Here the explicit optimal set is not zero forcing, so that robust, all-matrices theorem does not imply this fixed-Laplacian result. The unsigned-incidence determinant characterization of odd-unicyclic graphs is a classical ingredient also treated by Monfared and Mallik (2018); the incidence lemma itself is not claimed to be new. Dai (2022) addresses minimal leader sets for other graph families in a leader–follower setup, not this full-state triangular-graph selection classification.

## Limitations

No assertion is made for nonuniform edge conductances, non-coordinate controllers, strong structural controllability, or arbitrary Johnson graphs \(J(n,k)\) with \(k\ne2\). The novelty assessment is based on inspected published sources and semantic searches, not an exhaustive proof that no equivalent literature exists. Independent external mathematical validation has not been carried out. The auxiliary exact-rational and finite-field checks cannot replace the infinite-family proof.

## References

1. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang, Y.-C. Lai, “Exact controllability of complex networks,” *Nature Communications* **4**, 2447 (first published 2013-09-12). https://doi.org/10.1038/ncomms3447
2. N. Monshizadeh, S. Zhang, M. K. Camlibel, “Zero forcing sets and controllability of dynamical systems defined on graphs,” arXiv:1403.4868 (first version 2014-03-19). https://arxiv.org/abs/1403.4868
3. K. Hassani Monfared, S. Mallik, “An Analog of Matrix Tree Theorem for Signless Laplacians,” arXiv:1805.04759 (2018-05-12). https://arxiv.org/abs/1805.04759
4. L. Dai, “Minimum leader selection for controllability of undirected graphs with leader–follower framework,” *IET Control Theory & Applications* **17**, 505–515 (first published 2022-10-29). https://doi.org/10.1049/cth2.12385
