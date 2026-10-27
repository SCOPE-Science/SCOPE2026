# Eight vertices are the sharp onset of transmissibility-dependent single-node vaccination on trees

## Finding

**Theorem (sharp eight-vertex threshold and complete first-exception classification).** Consider an independent-edge Reed–Frost outbreak on an undirected finite tree. Before the outbreak, exactly one vertex is completely vaccinated and removed; the one initial infective is chosen uniformly from the remaining vertices. Every remaining edge transmits independently with the same probability \(p\in(0,1)\). Let an *optimal vaccination vertex* minimize the expected total final number of infected vertices, including the initial infective.

For every tree on at most seven vertices, a single fixed vaccination vertex is optimal **for all** \(p\in(0,1)\). This property fails at eight vertices, where precisely two of the 23 unlabelled trees have transmissibility-dependent optimal vertices. Explicit representatives, whose vertices are numbered \(0,\ldots,7\), are:

- **Broom:** edges \((1,0),(1,2),(0,5),(2,3),(2,4),(5,6),(6,7)\). Let \(\rho\) be the unique root in \((0,1)\) of \(\rho^3+\rho^2=1\). The unique optimum is vertex \(2\) when \(p<\rho\), vertex \(1\) when \(p>\rho\), and the two vertices tie exactly at \(p=\rho\). Numerically \(\rho\approx0.7548776662\).
- **Double-broom:** edges \((1,0),(1,2),(2,3),(2,4),(0,5),(5,6),(5,7)\). The optimum is exactly \(\{2,5\}\) when \(p<1/\sqrt2\), exactly \(\{0,1\}\) when \(p>1/\sqrt2\), and all four vertices \(\{0,1,2,5\}\) tie at equality.

There are no other eight-vertex exception types, up to graph isomorphism. Thus eight is the smallest population size at which the optimal single-site immunization location on a tree can change when only the pathogen's edge transmissibility changes.

## Assumptions and scope

A *tree* is a finite, simple, connected, undirected acyclic graph \(T=(V,E)\) with \(n=|V|\ge2\). Vaccinating \(v\in V\) deletes the vertex and every incident edge before introduction. The seed \(S\) is uniform on \(V\setminus\{v\}\), independent of Bernoulli-open edges of common probability \(p\in(0,1)\). Infection reaches precisely the open connected component of \(S\) in \(T-v\). No reinfection or pathogen-induced dynamic response is included.

Let \(d_T(x,y)\) denote the number of edges of the unique original path. Write \(x\sim_v y\) when the path from \(x\) to \(y\) avoids \(v\); this is equivalent to their lying in the same component of \(T-v\). Define the ordered-pair distance polynomial
\[
W_v(p)=\sum_{\substack{x,y\in V\setminus\{v\}\\x\ne y,\ x\sim_v y}}p^{d_T(x,y)}.
\]
If \(Z_v\) is final outbreak size, define \(J_v(p)=\mathbb E[Z_v]\). An optimum minimizes \(J_v(p)\) at fixed \(p\). A *universal* optimum minimizes it simultaneously for every \(p\in(0,1)\). The phrase ``all trees through size seven'' means every isomorphism type at each integer order \(2\le n\le7\); the eight-vertex statement considers all 23 unlabelled isomorphism types.

## Proof

**1. Exact expectation identity.** Conditional on seed \(x\ne v\), a distinct \(y\ne v\) is reached if and only if the unique \(x\)-to-\(y\) path avoids \(v\) and every edge of that path is open. Independence and uniqueness of the path give probability \(p^{d_T(x,y)}\) for pairs in the same component and zero otherwise. Summing the indicators of infected vertices, averaging the seed over \(n-1\) possibilities, and including the certain infected seed yields the identity
\[
\boxed{J_v(p)=1+\frac{W_v(p)}{n-1}}.\tag{1}
\]
Write \(W_v(p)=\sum_{k=1}^{n-2}a_{v,k}p^k\), where \(a_{v,k}\) is the **integer number of ordered pairs** in \(T-v\) at original-tree distance \(k\). Equation (1) reduces the full stochastic problem to exact comparison of finite integer polynomials.

**2. Exact finite comparison certificate.** For vertices \(v,w\), set \(F_{w,v}(p)=W_w(p)-W_v(p)=\sum_{k=1}^{d}c_kp^k\) with \(d=n-2\). Under \(p=t/(1+t)\), \(t>0\),
\[
(1+t)^dF_{w,v}\!\left(\frac{t}{1+t}\right)
=\sum_{j=0}^{d}\left(\sum_{k=1}^{j}c_k\binom{d-k}{j-k}\right)t^j.\tag{2}
\]
If every parenthesized integer in (2) is nonnegative, then \(F_{w,v}(p)\ge0\) for every \(0<p<1\). This is a sufficient *all-real-parameters* certificate: it does not rely on sampling values of \(p\).

**3. Exhaustive classification up to order eight.** Every labelled tree on \(n\) vertices occurs exactly once among Prüfer words of length \(n-2\) over \(\{0,\ldots,n-1\}\). The accompanying standalone `verify.py` enumerates those words for each \(2\le n\le8\). It collapses labelled representatives to unlabelled types by the canonical center-rooted recursive encoding: remove leaves until one center or two adjacent centers remain, recursively encode each rooted subtree with lexicographically sorted child encodings, and for a bicentered tree sort the two rooted halves. This encoding is a complete tree-isomorphism invariant by induction on rooted-subtree order.

For every unlabelled representative and every vertex, the program obtains all \(a_{v,k}\) by exact breadth-first search after vertex deletion. It then tests each possible universal optimum \(v\) by applying the nonnegative-coefficient certificate (2) against **every** \(w\). The resulting complete tree-class counts are
\[
\begin{array}{c|rrrrrrr}
n&2&3&4&5&6&7&8\\\hline
\text{unlabelled trees}&1&1&2&3&6&11&23
\end{array}.
\]
At orders \(2\) through \(7\), every class has a certified universal optimum. At order \(8\), exactly 21 classes have such a certificate. The only two classes without it are exactly the two representative trees stated above. For each of these two classes, the program additionally calculates the exact optimal sets at \(p=1/2\) and \(p=9/10\), finds them disjoint, and thereby proves that **no** universal optimum exists there. This last step is essential: failure to obtain a sufficient coefficient certificate alone would not establish nonexistence.

**4. Analytic optimum in the broom.** Direct ordered-pair counting gives
\[
W_2(p)=8p+6p^2+4p^3+2p^4,\qquad
W_1(p)=10p+6p^2+2p^3.
\]
For every other vertex \(w\), the exact coefficient certificate (2) proves \(W_w(p)\ge W_1(p)\) throughout \((0,1)\); in fact the differences are strictly positive in the interior. Finally,
\[
W_1(p)-W_2(p)=2p(1-p^2-p^3).\tag{3}
\]
Since \(p^2+p^3\) increases strictly from zero to two on \([0,1]\), equation (3) has exactly one interior sign change, at \(\rho\). The stated optimizers and unique tie follow.

**5. Analytic optimum in the double-broom.** The two trivalent centers are symmetric and the two bridge vertices are symmetric:
\[
W_2(p)=W_5(p)=8p+8p^2+4p^3,\qquad
W_1(p)=W_0(p)=10p+8p^2.
\]
Each of the four leaves is strictly dominated by bridge vertices, as the certificate (2) confirms. Therefore
\[
W_1(p)-W_2(p)=2p(1-2p^2).\tag{4}
\]
Its unique sign change on \((0,1)\) is \(p=1/\sqrt2\). Symmetry gives the full optimal sets, including the exact four-way tie at the boundary.

Combining steps 1–5 proves all statements. The finite classification is a reproducible exhaustive computer-assisted proof with exact integer arithmetic; the formulas (3)–(4) give the independent analytic threshold explanations.

## Verification

Run `python3 verify.py` using Python 3's standard library. The checker independently generates all Prüfer words through order eight, computes isomorphism representatives and exact ordered-pair polynomials, executes the coefficient certificates (2), identifies the two exceptional canonical tree types, checks disjoint optimal sets at two exact rational transmissibilities, and asserts both displayed witness polynomials and domination of all competitors. Expected type counts are exactly \(1,1,2,3,6,11,23\). A successful run ends with `PASS: no crossover through 7 vertices; precisely two 8-vertex cases; rational comparisons checked`. No floating-point enumeration or stochastic simulation is used in the mathematical certificate; the final reported execution time is not part of the proof.

## Relationship to prior work

Holme [1] compares exact SIR influence, vaccination and sentinel importance for small connected networks of up to seven vertices under **continuous-time Markovian** infection/recovery. Its full outbreak law differs from independent-bond Reed–Frost because transmissions from the same person can be correlated. **However, for the mean final outbreak size on a tree, the two models have the same unique-path marginal probabilities** after setting \(p=\beta/(\beta+\gamma)\) for common Markov infection and recovery rates \(\beta,\gamma>0\): every path traverses different transmitting persons, whose infectious lifetimes are independent. Thus the mean vaccination objective coincides on trees. Our claim does not assert novelty of this objective or low-order tree ranking; it identifies the sharp first crossover at eight vertices and its two complete exceptional shapes, beyond Holme's through-seven graph enumeration.

Hall and Siebert [2] derive exact node-state probabilities for Markov SIR/SEIR on rooted trees; their analysis does not classify which one-vertex deletion minimizes the seed-averaged final size as independent-edge transmissibility changes. The Hosoya–Wiener polynomial literature [3] gives general distance-polynomial constructions on weighted trees and suggests an equivalent graph-polynomial description of our objective. It does not, from the material examined, supply the sharp first switching order or the complete exception classification. The site–bond epidemic-vaccination literature [4] studies expected outbreak sizes and vaccination but under different aggregate models, without the asserted finite-tree vertex-ranking theorem. The novelty claim here is **the exact size-eight optimal-location onset and complete exception classification**, not the distance-polynomial or percolation identities themselves.

## Limitations

The theorem applies only to one perfectly removed vertex on a tree, one uniformly chosen postvaccination seed, identical independent edge-open events and final **mean** outbreak size. Although the same mean objective applies to continuous-time Markov SIR on trees after matching each edge transmission probability, the theorem does not characterize the joint outbreak distribution or higher moments of such models. It also does not cover heterogeneous edge probabilities, multiple vaccinated vertices, cyclic contact graphs, adaptive intervention, nonuniform sources, or population-level epidemic thresholds. The exhaustive computation establishes nothing beyond eight vertices. Publication priority has been compared with the cited primary literature and mathematical records but not independently certified; the complete original literature cannot be proven absent.

## References

[1] P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456, first publicly posted 22 August 2017; Phys. Rev. E **96** (2017), 062305. https://arxiv.org/abs/1708.06456 ; https://doi.org/10.1103/PhysRevE.96.062305 .

[2] C. L. Hall and B. A. Siebert, *Exact solutions and bounds for network SIR and SEIR models using a rooted-tree approximation*, J. Math. Biol. **86** (2023), article 22. https://doi.org/10.1007/s00285-022-01854-9 .

[3] B. Zmazek and J. Žerovnik, *The Hosoya-Wiener Polynomial of Weighted Trees*, Croatica Chemica Acta **80** (2007), 75–80. https://hrcak.srce.hr/12827 .

[4] *Site-bond percolation model of epidemic spreading with vaccination in complex networks*, J. Math. Biol. (2022), https://doi.org/10.1007/s00285-022-01816-1 .
