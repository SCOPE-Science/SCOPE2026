# Exact endpoint cut–cycle norms on adjacent Boolean-lattice ranks

## Finding

For integers \(n\ge3\) and \(1\le k\le n-2\), let \(G_{n,k}\) be the unweighted bipartite graph whose vertices are all \(k\)-subsets and all \((k+1)\)-subsets of \([n]\); join \(S\) to \(T\) exactly when \(S\subset T\). Orient every edge from its lower-rank endpoint to its upper-rank endpoint. Let \(D\) be the vertex–edge incidence matrix with \(+1\) at the lower endpoint and \(-1\) at the upper endpoint. Let \(Q=D^{\mathsf T}(DD^{\mathsf T})^{+}D\) be the Euclidean-orthogonal projection onto the edge cut space and \(P=I-Q\) the complementary cycle-space projection.

The exact induced real endpoint operator norms are
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=2k+1-\frac{2k(k+1)}n}
\]
and
\[
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=2k+2-\frac{2k(k+1)}n-\frac2{k+1}-\frac{2}{n-k}\left(1-\binom nk^{-1}\right).}
\]
Every edge column has the same absolute column sum. Its cut-projector diagonal entry is
\[
\boxed{Q_{ee}=\frac1{k+1}+\frac{1-\binom nk^{-1}}{n-k}.}
\]

For fixed \(k\) and \(n\to\infty\), the two norms tend to \(2k+1\) and \(2k+2-2/(k+1)\), respectively. If \(k/n\to\alpha\in(0,1)\), both norms divided by \(n\) tend to \(2\alpha(1-\alpha)\). In particular, middle-level incidence graphs have endpoint norms of order \(n/2\), whereas graphs of any fixed adjacent ranks have bounded endpoint norms.

## Assumptions and scope

All spaces, matrices and induced norms are real. The graph is finite, simple, connected and unweighted. The projection is canonical orthogonal projection in the Euclidean inner product on edge coefficients; no optimality is asserted among all nonorthogonal projections. Edge orientation does not change the induced norms. The initial calculation assumes \(1\le k\le(n-1)/2\). Complementing every subset identifies \(G_{n,k}\) with \(G_{n,n-k-1}\), and both displayed formulas are invariant under this substitution, yielding the stated full range.

## Proof

**1. Reduction to a Johnson-graph Green function.** Fix the edge \(e=(A,B)\), where \(|A|=k\), \(B=A\cup\{z\}\), and write its cut-projection column as the electrical current from \(A\) to \(B\). Let \(C\) be the lower-to-upper inclusion matrix. If the vertex potential is \((x,y)\), with \(x\) on \(k\)-subsets and \(y\) on \((k+1)\)-subsets, the Laplacian equation is
\[
(n-k)x-Cy=\delta_A,\qquad (k+1)y-C^{\mathsf T}x=-\delta_B.
\]
Because \(CC^{\mathsf T}=(n-k)I+A_J\), where \(A_J\) is the adjacency matrix of the Johnson graph \(J(n,k)\), elimination gives
\[
L_Jx=k\delta_A-\sum_{i\in A}\delta_{(A\setminus\{i\})\cup\{z\}},\qquad
 y=\frac{C^{\mathsf T}x-\delta_B}{k+1}.
\]
Here \(L_J=k(n-k)I-A_J\). The right-hand side has total sum zero, so the equations are soluble up to a common additive constant.

Let \(N=\binom nk\) and let \(g_r\) be the radial Green potential on \(J(n,k)\) with \(L_Jg=\delta_A-N^{-1}{\bf1}\), where \(r\) is the Johnson distance from \(A\). Define \(\Delta_r=g_r-g_{r+1}\) for \(0\le r<k\). The sphere sizes and their outward edge degrees are
\[
N_r=\binom kr\binom{n-k}r,\qquad b_r=(k-r)(n-k-r).
\]
Summing the Green equation over the distance ball of radius \(r\), and using \(N_rb_r=N_{r+1}(r+1)^2\), yields the strictly positive differences
\[
\Delta_r=\frac{\sum_{j=r+1}^{k}N_j}{N N_{r+1}(r+1)^2}.
\]
The solution of the eliminated equation is the sum of the corresponding Green dipoles. Put \(a=|S\cap A|\), \(b={\bf1}_{\{z\in S\}}\), and \(r=k-a\) for a lower-rank vertex \(S\). Counting the distances to the \(k\) sets obtained from \(A\) by replacing one of its elements by \(z\) gives
\[
x(S)=\begin{cases}a\Delta_r,&b=0,\\-r\Delta_{r-1},&b=1.\end{cases}
\]
The cases with a zero multiplier are understood directly and require no out-of-range Green difference.

**2. Exact signs of all edge currents.** Put \(T_r=(\sum_{j=r}^kN_j)/N_r\) for \(1\le r\le k\), and \(u_r=N_{r+1}/N_r=(k-r)(n-k-r)/(r+1)^2\), including \(u_k=0\). Then \(T_r=1+u_rT_{r+1}\) and \(\Delta_{r-1}=T_r/(Nr^2)\). The nonnegative ratios \(u_r\) strictly decrease with \(r\). Consequently \(x(a,0)=(k-r)T_{r+1}/(N(r+1)^2)\) increases with \(a\), and \(x(a,1)=-T_r/(Nr)\) decreases with \(a\); the first is nonnegative, the second strictly negative.

For an upper-rank vertex \(T\ne B\), its potential is the arithmetic mean of its \(k+1\) lower neighbors. These monotonicities give the signs of the currents \(x(S)-y(S\cup\{i\})\) in all but one class: the current is negative if \(z\notin S\) and \(i\in A\), or if \(z\in S\) and \(i\notin A\cup\{z\}\); it is nonnegative in every other class. The only potentially zero class is \(z\notin S\), \(a=0\) and \(i\notin A\cup\{z\}\).

For completeness, when \(z\in S\), \(i\in A\), and \(S\cup\{i\}\ne B\), put \(r=k-a\ge2\). Multiplying this edge current by the positive factor \(N(k+1)\) gives
\[
1+(\beta-1)T_r,\qquad \beta=\frac{(k-r+1)(n-k-r)}{r^2}>0.
\]
If \(\beta\ge1\) this is positive. Otherwise \(u_r<\beta<1\), all later \(u_j\le u_r\), and the geometric bound \(T_r\le(1-u_r)^{-1}<(1-\beta)^{-1}\) makes it positive as well. At the distinguished upper vertex \(B\), the strict minimum principle for the connected graph Laplacian makes every incident current positive; thus the same sign rule holds there.

Define a sign vector \(\sigma\) on oriented edges by setting \(\sigma(S,i)=-1\) in exactly the two negative classes above and \(+1\) otherwise. The possible zero currents cause no ambiguity: \(\langle\sigma,Qe\rangle=\|Qe\|_1\).

**3. A degree-two dual potential evaluates the absolute current sum.** For either vertex rank, let \(a\) and \(b\) denote the same membership statistics. The incidence divergence of the sign vector is
\[
(D\sigma)(S)=(1-2b)(n-3k+2a)\quad(|S|=k),
\]
\[
(D\sigma)(T)=-\big((1-2b)(k+1-2a)+2b\big)\quad(|T|=k+1).
\]
Set, on the two ranks respectively,
\[
w_k(a,b)=1+\frac{2(n-k-1)}n a+\frac{2(k^2+k-n)}n b-2ab,
\]
\[
w_{k+1}(a,b)=\frac{2(n-k)}n a+\frac{2k^2}n b-2ab.
\]
Direct substitution into the graph Laplacian (using \(b^2=b\)) verifies \(Lw=D\sigma\) at every vertex. Hence \(Q\sigma=D^{\mathsf T}w\). Since \(Q\) is symmetric and \(e=(A,B)\),
\[
\|Qe\|_1=\langle\sigma,Qe\rangle
=\langle Q\sigma,e\rangle=w_k(k,0)-w_{k+1}(k,1)
=2k+1-\frac{2k(k+1)}n.
\]
The full symmetric group on \([n]\) is transitive on inclusion edges, so all columns have this norm. Symmetry of \(Q\) also equates its induced \(\ell_1\) and \(\ell_\infty\) norms.

**4. Diagonal and complementary projection.** Among the \(k+1\) lower neighbors of \(B\), the potential is \(k\Delta_0\) at \(A\) and \(-\Delta_0\) at each of the other \(k\) neighbors. Their sum is zero, so \(y(B)=-1/(k+1)\). Also \(\Delta_0=(1-N^{-1})/[k(n-k)]\). Thus
\[
Q_{ee}=x(A)-y(B)=\frac1{k+1}+\frac{1-N^{-1}}{n-k}.
\]
As \(0<Q_{ee}<1\) for the stated nontrivial graphs, the absolute sum in the \(e\)-column of \(I-Q\) is \(\|Qe\|_1+1-2Q_{ee}\), proving the formula for \(P\). Complementation gives the other half of the rank range. The limits follow directly from the exact formulas.

## Verification

The accompanying `verify_boolean_layer_hodge.py` reconstructs exact-rational edge-source potentials independently on stabilizer orbits and by grounded Laplacian inversion of entire graphs, and checks both projection norms and diagonal entries. Its checked test run reported `orbit_cases=54`, `orbit_edge_types=872`, `full_cases=9`, `full_edges=445`, and `symbolic_identities=PASS`. The last check independently expands the degree-two dual-potential identity. Finite cases validate the computations but do not establish the theorem for infinitely many parameters; that relies on the preceding proof.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (2023) develop invariant cycle-space projections and calculate the orthogonal cut-projection norm of the **entire** binary Hamming cube. Their graph and projector differ from the restriction to two adjacent rank levels; induced-subgraph restrictions do not commute with orthogonal edge projection. Dilworth, Kutzarova and Ostrovskii (2018) develop the transportation-cost quotient and projection framework, particularly for diamond and Laakso graphs, but do not give this exact adjacent-rank norm classification in the inspected relevant sections. The eliminated lower-rank equation here is a Johnson-graph equation; that relation by itself does not determine the absolute currents on the bipartite incidence graph, whose endpoint norm is the object computed above.

## Limitations

The result is for real, unweighted inclusion graphs of two neighboring Boolean levels and the **canonical orthogonal** projections only. It does not determine the least norm among arbitrary projections onto the same subspaces, higher-dimensional Boolean rank-selection bands, weighted variants or intermediate \(\ell_p\) norms. Prior literature beyond the inspected sources could contain an equivalent formulation; novelty is not independently certified.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first posted 2023-05-21), https://arxiv.org/abs/2305.12582 .
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first posted 2018-07-10), https://arxiv.org/abs/1807.03814 .
