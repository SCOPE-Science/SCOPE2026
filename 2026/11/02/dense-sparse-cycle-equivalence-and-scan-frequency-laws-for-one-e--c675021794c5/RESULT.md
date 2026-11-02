# Dense–sparse cycle equivalence and scan-frequency laws for one-edge-deleted cliques

## Finding
Fix an integer \(n\ge4\), two distinct labelled vertices \(u,v\), and the graph \(G_n=K_n-uv\). On the binary state space \(\mathbb F_2^n\), let each local update at vertex \(w\) replace its current coordinate by the XOR of itself and all its *current* neighbors. Let \(F_\pi\) be a complete sweep in any vertex permutation \(\pi\), repeated at every time step. Write \(k=(\operatorname{pos}_\pi(v)-\operatorname{pos}_\pi(u))\bmod n\) with \(1\le k\le n-1\), and put \(m=n-k\).

**Theorem.** For every integer \(t\ge1\), set \(g=\gcd(k,t)\), \(h=\gcd(m,t)\), and \(\varepsilon_t=(nt/(gh))\bmod2\), interpreting the last expression as either zero or one. Then
\[
\#\operatorname{Fix}(F_\pi^t)=2^{g+h-\varepsilon_t}.
\]
Every state lies on a periodic orbit without a transient. The permutation order of \(F_\pi\) is precisely
\[
L(k,m)=\begin{cases}\operatorname{lcm}(k,m),&\nu_2(k)=\nu_2(m),\\2\operatorname{lcm}(k,m),&\nu_2(k)\ne\nu_2(m),\end{cases}
\]
and at least one state has primitive period \(L(k,m)\). For every divisor \(d\) of \(L(k,m)\), the number of primitive period-\(d\) states and orbits is, respectively,
\[
P_d=\sum_{e\mid d}\mu(d/e)2^{\gcd(k,e)+\gcd(m,e)-\varepsilon_e},\qquad P_d/d.
\]
For other \(d\), the number is zero.

For **each** \(k\in\{1,\ldots,n-1\}\), precisely \(n(n-2)!\) of the \(n!\) labelled scanning permutations realize that oriented gap. Thus the schedule-dependent recurrence classes of the dense graphs are distributed by a *uniform* cyclic-gap law. In contrast, for the ordinary nearest-neighbor Rule 150 sweep on the sparse cycle \(C_n\), the corresponding class indexed by the cyclic ascent count \(k\) occurs \(n A(n-1,k-1)\) times, where \(A\) denotes the Eulerian number. Despite these different frequencies, every dense-graph scan has exactly the periodic-orbit population of a cycle-graph scan with the matching index \(k\). Their induced finite permutations are therefore conjugate as set maps, without claiming a linear similarity.

For example, on the six-vertex graph \(K_6-uv\), the three possible orders \(3,5,8\) occur for exactly \(144,288,288\) scan permutations respectively; on \(C_6\), the same orders have scan frequencies \(396,12,312\) respectively. For even \(n\) there are exactly four fixed states for every scan, and for odd \(n\) exactly two.

## Assumptions and scope
All graphs are finite labelled simple graphs, \(n\ge4\), and the field is exactly \(\mathbb F_2\). The local rule is self-inclusive neighbor XOR, and a sweep is sequential, not simultaneous. Both marked vertices \(u,v\) are distinct and not adjacent in \(G_n\); all other pairs are adjacent. Every sweep uses the same ordering. The gap is oriented modulo \(n\), and the symmetric expressions depend only on the unordered pair \(\{k,m\}\). Fixed-point counts count states, while primitive orbit counts divide by the actual orbit length. These statements do not extend without proof to other alphabets, simultaneous updates, or additional deleted edges.

## Proof
**1. Scan matrix.** In scan order \(1,\ldots,n\), let \(A\) be the adjacency matrix over \(\mathbb F_2\), split as its strictly lower and upper triangular parts \(L,U\). The sequential update equations, with later-coordinate input from the old state and earlier-coordinate input from the new state, give
\[
F=(I+L)^{-1}(I+U).
\]
Both triangular factors are invertible. Consequently \(\lambda I-F\) and the polynomial matrix \(M(\lambda)=\lambda(I+L)+(I+U)\) have the same Smith invariant factors over \(\mathbb F_2[\lambda]\). Moreover, each local update is an involution, because the neighbors are unchanged by updating that vertex, so \(F\) is invertible.

Conjugating a product of invertible local updates by its leading local factor cyclically rotates the scan. Renaming \(u,v\) interchanges \(k,m\), and permuting the ordinary clique vertices conjugates the dynamics. We may therefore arrange that the missing edge joins positions \(1\) and \(j=k+1\), where \(1\le k\le n-2\), and \(m=n-k\ge2\). This covers the remaining case by exchanging \(k,m\).

**2. Polynomial elimination.** For a polynomial column vector \(z\), write \(P_i=\sum_{r=1}^i z_r\), \(P_0=0\), \(S=P_n\). The \(i\)-th row \(R_i\) of \(M(\lambda)z\) is
\[
R_i=\lambda P_i+P_{i-1}+S+\mathbf1_{i=1}z_j+\mathbf1_{i=j}\lambda z_1.
\]
Perform the unimodular row change replacing the first \(n-1\) equations by \(D_i=R_i+R_{i+1}\) and keeping \(R_n\). Except at the missing-edge positions, \(D_i=z_i+\lambda z_{i+1}\). Explicitly, for \(j\ge3\),
\[
D_1=z_1+\lambda z_2+z_j,\quad D_{j-1}=z_{j-1}+\lambda z_j+\lambda z_1,\quad D_j=z_j+\lambda z_{j+1}+\lambda z_1.
\]
For \(j=2\), the two exceptional contributions combine into \(D_1=(\lambda+1)(z_1+z_2)\) and \(D_2=z_2+\lambda z_3+\lambda z_1\). Every \(D_2,\ldots,D_{n-1}\) contains a unit coefficient on its own variable; polynomial elementary eliminations leave two free variables \(a=z_1\), \(c=z_n\). In both cases, the solved variables satisfy
\[
z_j=\lambda a+\lambda^{m-1}c,\qquad
z_r=\lambda^{j-r}(z_j+a)\ (2\le r<j),\qquad
z_r=\lambda^{n-r}c\ (j<r\le n).
\]
Write \(B_s=1+\lambda+\cdots+\lambda^{s-1}\). Substitution into \(D_1\) and \(R_n\) reduces the complete polynomial presentation by unimodular operations to \(n-2\) unit entries and the following \(2\times2\) block:
\[
H_{k,m}(\lambda)=\begin{pmatrix}
(\lambda+1)^2B_k&\lambda^{m-1}(\lambda+1)B_k\\
\lambda(\lambda+1)B_k&B_n
\end{pmatrix}.
\]
Indeed, \(D_1=(\lambda^k+1)((\lambda+1)a+\lambda^{m-1}c)\) and \(R_n=\lambda(\lambda+1)B_k a+B_nc\). The same equalities hold at the boundary \(k=1\), as shown by the explicit \(j=2\) equations.

**3. Smith invariants and recurrent counts.** Direct multiplication gives
\[
\det H_{k,m}=(\lambda^k+1)(\lambda^m+1).
\]
The gcd of the four entries of \(H\), using the three non-bottom-right entries and \(B_n=(\lambda^n+1)/(\lambda+1)\), equals \(\gcd(\lambda^k+1,B_n)\). Thus the only potentially nonunit invariant factors are
\[
d_1=\gcd\!\left(\lambda^k+1,\frac{\lambda^n+1}{\lambda+1}\right),\qquad
d_2=\frac{(\lambda^k+1)(\lambda^m+1)}{d_1}.
\]
Let \(q=\gcd(k,m)\) and \(\delta=\mathbf1_{\nu_2(k)\ne\nu_2(m)}\). Comparison of multiplicities of the root \(\lambda=1\) (and the ordinary polynomial gcd identity) yields
\[
d_1=\frac{\lambda^q+1}{(\lambda+1)^\delta},\qquad
d_2=\operatorname{lcm}(\lambda^k+1,\lambda^m+1)(\lambda+1)^\delta.
\]
For a linear map over \(\mathbb F_2\) with these invariant factors, the fixed space of its \(t\)-th power has dimension
\[
\deg\gcd(d_1,\lambda^t+1)+\deg\gcd(d_2,\lambda^t+1).
\]
The two summands agree with those for \(\lambda^k+1\) and \(\lambda^m+1\) apart from moving one \(\lambda+1\) factor from the smaller to the larger invariant factor when \(\delta=1\). The resulting one-dimensional deficit occurs exactly when
\[
\min(\nu_2(k),\nu_2(m))\le\nu_2(t)\le\max(\nu_2(k),\nu_2(m)),
\]
which is precisely when \(nt/(\gcd(k,t)\gcd(m,t))\) is odd. The stated fixed-point count follows from \(\deg\gcd(\lambda^r+1,\lambda^t+1)=\gcd(r,t)\). The displayed invariant factors also give the exact order of \(F\) from its largest invariant factor: the additional factor \(\lambda+1\) in the unequal-valuation case doubles the order. A vector generating the cyclic module for \(d_2\) has orbit of this maximal order. Möbius inversion proves the primitive-state and primitive-orbit formulas.

**4. Scan frequencies and dense–sparse comparison.** For a fixed oriented gap \(k\), choose the position of \(u\) in \(n\) ways, place \(v\) at position \(k\) steps later cyclically, and permute the \(n-2\) remaining vertices freely. Hence the exact multiplicity is \(n(n-2)!\). The nearest-neighbor Rule 150 cycle census has the same expression for its fixed-point counts, indexed instead by the number of cyclic ascents in the scan; the latter index has distribution \(nA(n-1,k-1)\). Equality of fixed-point counts for every iterate implies equality of the number of cycles of every length by Möbius inversion. As both full maps are finite permutations, a bijection matching corresponding cycles and their phases gives set-theoretic dynamical conjugacy. It does not yield or require linear similarity of update matrices.

## Verification
The standalone Python 3 standard-library program `verify.py` reconstructs every local update matrix over \(\mathbb F_2\), all scan maps for \(3\le n\le7\), and their entire state orbits. It independently checks the cycle-graph Rule 150 orbit census for every scan on \(3\le n\le7\), separately from the dense graph calculations. It also checks polynomial gcd invariant factors against binary-matrix ranks for all \(3\le n\le24\), every nonzero cyclic gap, and a range of iterate times. Its recorded successful execution output is in `verification_output.txt`. In total the run checked 5,910 dense scans with 695,472 dense scan–state pairs, independently checked 5,910 cycle scans with 695,472 cycle scan–state pairs, and checked 15,438 pairs of fixed-space and polynomial computations. These tests corroborate the explicit all-\(n\) algebraic proof; they are not an exhaustive enumeration of infinitely many dimensions.

## Relationship to prior work
Macauley and Mortveit (2008, first public February 29, 2008) established general cycle equivalences for graph dynamical systems under update-order transformations **on a fixed graph**. Chen and Reidys (2015) derived general sequential linear-system matrix formulas. Defant (2015) treated Rule 150/105 on **cycle graphs**, including the identity-order periodic point problem. A prior cycle-specific all-scan census provides the sparse-side fixed-point formula used for comparison here. None of these results, as inspected, asserts the deleted-edge complete-graph Smith decomposition, its all-scan formula, or the contrasting uniform gap distribution. The present classification is the derivation of those dense-graph results and their explicit comparison with cycle dynamics, not a claim to have discovered general scan matrices or the existing cycle formula.

## Limitations
The graph must have exactly one deleted edge, the local update must be self-inclusive binary XOR, and the scans must be repeated. The cross-graph conjugacy is a conjugacy of permutations, not a demonstrated linear conjugacy. The audit establishes no comprehensive absence of historical equivalent work: differently formulated Coxeter-transformation results or nonindexed literature might imply this classification. Independent mathematical validation has not been performed.

## References
1. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412, first version February 29, 2008. https://arxiv.org/abs/0802.4412
2. R. X. F. Chen and C. M. Reidys, *Linear Sequential Dynamical Systems, Incidence Algebras, and Möbius Functions*, arXiv:1510.04930, first version October 16, 2015. https://arxiv.org/abs/1510.04930
3. C. Defant, *Flexible Toggles and Symmetric Invertible Asynchronous Elementary Cellular Automata*, arXiv:1511.06966, first version November 22, 2015. https://arxiv.org/abs/1511.06966
