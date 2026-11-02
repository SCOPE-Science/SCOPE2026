# Uniform two-step periodicity for majority dynamics on degree-two leaf coronas

## Finding

Let \(H\) be any finite or infinite simple undirected graph with maximum degree at most two, and let \(W(H)=H\circ K_1\) be the graph formed by attaching one distinct private leaf to every vertex of \(H\). Under synchronous binary open-neighbor majority dynamics, with the current state retained at a tie, the global update map satisfies the **pointwise identity**

\[
F_{W(H)}^{4}=F_{W(H)}^{2}
\]

on every initial configuration. Thus every configuration, including an arbitrary deterministic configuration on an infinite graph, is fixed or in a two-cycle by time two. The uniform bound two is sharp even for the corona of the three-vertex path and for the corona of a bi-infinite path.

The base-degree hypothesis is sharp for this universal two-step guarantee: the corona of the degree-three star \(K_{1,3}\) has an initial configuration whose first periodic time is three. By contrast, on the *unwhiskered* odd cycle \(C_{2m+1}\), \(m\ge1\), the same strict-neighbor majority rule with inertial ties has an explicit configuration whose first periodic time is \(m\). Consequently, adding one private leaf to every vertex changes this unbounded worst-case clock to the universal constant two.

## Assumptions and scope

All graphs are simple, undirected, and locally finite. The vertex set of \(H\) may be infinite. Write \(v^*\) for the private leaf associated with \(v\in V(H)\). At time \(t\), \(x_v(t)\in\{0,1\}\) is the state of the original vertex and \(y_v(t)\in\{0,1\}\) is the state of \(v^*\). The update is simultaneous: every leaf copies its original vertex, while every original vertex takes the strict majority of its neighbors, retaining its preceding bit if the two neighbor votes tie. We use \(M(a,b,c)\) for the median (majority) of three binary inputs.

For a configuration \(z\), its first periodic entry time is the least \(t\ge0\) such that \(F^{t+2}(z)=F^t(z)\). An identity of maps on infinite configuration spaces means equality of every vertex coordinate for every initial configuration; no probabilistic assumption is made.

## Proof

**1. Reduction to a two-level majority recurrence.** A private leaf satisfies \(y_v(t+1)=x_v(t)\). Consider first a connected component of \(H\) with at least one edge. Each vertex \(v\) of that component has one or two base neighbors. Define an ordered pair of *ports* \((p(v),q(v))\): if \(v\) has two base neighbors, use those two vertices; if \(v\) has one base neighbor \(u\), use \((u,v)\). For degree two the core has three neighbors, and for degree one it has two neighbors plus inertial tie-breaking. In both cases the exact update is

\[
x_v(t+1)=M\bigl(x_{p(v)}(t),x_{q(v)}(t),y_v(t)\bigr).
\]

For a degree-one vertex this identity follows by checking that the majority of \(x_u(t),y_v(t),x_v(t)\) agrees with the two-neighbor majority retaining \(x_v(t)\) on a tie. No symmetry or finiteness assumption is used.

**2. Two-round absorption lemma.** For arbitrary initial core word \(X\) and leaf word \(Y\), set \(B=x(1)\) and \(A=x(2)\). The two updates give, at every nonisolated base vertex,

\[
B_v=M(X_{p(v)},X_{q(v)},Y_v),\qquad
A_v=M(B_{p(v)},B_{q(v)},X_v).
\]

We prove the two stability conditions

\[
A_v=M(B_{p(v)},B_{q(v)},A_v),\qquad
B_v=M(A_{p(v)},A_{q(v)},B_v).
\]

The first is immediate: if the two port bits of \(B\) agree, their value is the output \(A_v\) regardless of the third input \(X_v\); if they disagree, the median with \(A_v\) returns \(A_v\).

For the second, suppose it fails at \(v\). The two port bits \(A_{p(v)}\) and \(A_{q(v)}\) must then both equal \(1-B_v\). Consider either port \(u\in\{p(v),q(v)\}\). If \(u\ne v\), it is a base neighbor of \(v\), so one of \(u\)'s two ports is \(v\). If \(u=v\), then \(v\) is itself one of its ports by construction. Hence \(A_u\) is a three-bit median with one input \(B_v\) and the third input \(X_u\). Since \(A_u=1-B_v\), necessarily \(X_u=1-B_v\). Applying this observation to both ports gives

\[
X_{p(v)}=X_{q(v)}=1-B_v,
\]

which contradicts \(B_v=M(X_{p(v)},X_{q(v)},Y_v)\). The lemma follows, including the possibility that \(p(v)=v\) or \(q(v)=v\).

**3. The global identity.** At time two the state on each nonisolated component is the core-leaf pair \((A,B)\). The two stability conditions prove that its next two core words are \(B,A\), while its next two leaf words are \(A,B\). Therefore \(F^2(A,B)=(A,B)\) on every such component. An isolated base vertex and its private leaf merely swap their bits, so the same identity holds there even from time zero. Disjoint components evolve independently. We obtain \(F^4=F^2\) simultaneously at every vertex of any finite or infinite \(W(H)\).

**4. Sharpness of the two-step bound and the degree threshold.** On the corona of the path \(P_3\), label base vertices \(0,1,2\), their leaves \(3,4,5\), and encode a state as \(\sum_{i=0}^{5} z_i2^i\). The orbit from integer code \(1\) is \(1\to8\to0\to0\); first periodic entry occurs at time two. The same single excited core vertex with all other bits zero works on the corona of the bi-infinite path.

For the base star \(K_{1,3}\), label its center \(0\), other base vertices \(1,2,3\), and private leaves \(4,5,6,7\). The orbit from code \(33\) is

\[
33\longrightarrow18\longrightarrow32\longrightarrow0\longrightarrow0.
\]

It first becomes periodic at time three, proving that the degree-two hypothesis cannot be relaxed to a universal bound of two for all degree-three bases.

**5. Contrast with the unwhiskered odd cycle.** On \(C_{2m+1}\), let the initial binary word in cyclic order be \(0(10)^m\). Since a degree-two vertex updates by the majority of its two neighbors and its own old bit, induction shows that at integer time \(t\), \(0\le t<m\), the ones lie precisely at positions

\[
t+1,\ t+3,\ \ldots,\ 2m-t-1.
\]

There are \(m-t\) ones; the alternating block loses its two end sites at each step, and every site outside the block remains zero. At time \(m\) the word becomes all zero. Since the population of ones strictly decreases at every preceding step, no earlier state is periodic. Its first periodic entry time is exactly \(m\), with no uniform bound as the cycle grows.

## Verification

The argument above is a universal local proof; finite enumeration is corroboration, not an extrapolation to infinity. The two executable checkers included with this finding use different update implementations. `verify_all_small.cpp` tests **every labelled simple base graph of maximum degree at most two on one through six vertices**, including disconnected graphs, and every initial state of its one-leaf corona: **7,880,484 configuration–graph pairs** across **2,163 labelled base graphs**. It checks the exact identity at time two. `verify_degree2.py` independently enumerates path and cycle coronas through eight base vertices, partitions initial states by first periodic entry time, checks the degree-three star witness, and checks the unwhiskered odd-cycle witnesses through \(m=12\). Both programs print `VERIFY_OK`; their actual output files are included.

Reproduction: run `python3 verify_degree2.py`, then compile with `g++ -O3 -std=c++17 verify_all_small.cpp -o verify_all_small` and execute `./verify_all_small`. The printed output should match the included `.txt` files.

## Relationship to prior work

Goles and Olivos established that finite symmetric binary threshold networks eventually have period at most two [1]. That result does not specify the first periodic entry time and does not by itself imply a uniform two-round bound. Benjamini et al. study the period-two property on infinite graphs under invariant distributions and other assumptions [2]; the present identity is pointwise for *every* configuration on a specific, nontransitive infinite graph class. Nakar and Ron study majority automata directly on unwhiskered cyclic one-dimensional lattices [3], not the leaf-corona coupling. Earlier work on threshold networks with memory [4,5] supplies related general methods, but its period restrictions and transient estimates do not state this local two-round absorption result. A prior enumeration of recurrent states for the finite cycle corona does not determine how long an arbitrary initial state takes to reach those states. A 2026 exact worst-case stabilization theorem for finite trees [6] has a different domain: the cycle coronas are not trees, the path-corona endpoints have even degree outside its formal odd-degree theorem, and infinite coronas are not finite trees.

## Limitations

The identity does not enumerate individual attraction basins or recurrence classes, and it does not assert the same two-step bound for arbitrary base graphs of maximum degree three. The star example proves only that the **universal two-step guarantee** fails at that next base-degree level, not that every degree-three graph fails. The comparison with unwhiskered cycles is an explicit worst-case family, not a full census of those cycles. Historical equivalences under alternative threshold-network terminology cannot be excluded definitively without broader specialist verification.

## References

[1] E. Goles and J. Olivos, "Periodic behaviour of generalized threshold functions," *Discrete Mathematics* **30** (1980), 187–189, doi:10.1016/0012-365X(80)90121-1.

[2] I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, "Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs," arXiv:1405.2486v1, publicly posted 2014-05-11.

[3] Y. Nakar and D. Ron, "The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity," arXiv:2205.08972v1 (2022).

[4] P. Y. Melatagia, R. Ndoundam, and M. Tchuenté, "Dynamical behaviour of neural networks iterated with memory," ICTP preprint IC/2005/111 (2005).

[5] E. Goles, "Dynamical Behaviour of Neural Networks," *SIAM Journal on Algebraic Discrete Methods* **6** (1985), 749–754, doi:10.1137/0606073.

[6] I. Benjamini, G. Zakharov, and M. Zhukovskii, "Majority Dynamics on Finite Trees," *Random Structures & Algorithms* **69** (2026), e70092, first published 2026-09-07, doi:10.1002/rsa.70092.
