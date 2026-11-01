# Coordinate-fixed homotopy and residual integral symmetry of Hamming total two-cut complexes

## Finding
For all integers \(n,q\ge2\), let \(H(n,q)=K_q^{\square n}\) be the graph of words \([q]^n\) adjacent when they differ in exactly one coordinate. Let \(X_{n,q}=\Delta^t_2(H(n,q))\) be the simplicial complex of subsets of words whose complements contain two nonadjacent words. The coordinate-permutation group \(S_n\) acts on \(X_{n,q}\). Write \(F_{n,q}=|X_{n,q}|^{S_n}\) for its **geometric** fixed-point space, and \(T=\binom{n+q-1}{q-1}\).

**Theorem.** There is a canonical orbit-simplex triangulation and an integral homotopy classification
\[
\boxed{F_{n,q}\simeq\bigvee^{q-1}S^{T-3}.}
\]
Moreover, the commuting diagonal alphabet-relabeling group \(S_q\) acts on its sole nonzero reduced integral homology by the **coaugmentation lattice with an explicit orientation twist**:
\[
\boxed{\widetilde H_{T-3}(F_{n,q};\mathbb Z)\cong
\operatorname{sgn}_{\mathcal H}\otimes
\bigl(\mathbb Z^{[q]}/\mathbb Z(1,\ldots,1)\bigr),}
\]
where \(\mathcal H\) is the \(S_q\)-set of all weak compositions of \(n\) into \(q\) parts, and \(\operatorname{sgn}_{\mathcal H}\) is the sign of its induced permutation action. All other reduced integral homology groups vanish. These are assertions about the actual fixed set, not the invariant submodule of ambient homology.

In particular the twist has the closed parity description \(\operatorname{sgn}_{\mathcal H}(\sigma)=\operatorname{sgn}(\sigma)^{\epsilon_{n,q}}\), where
\[
\epsilon_{n,q}\equiv\frac{T-f_{n,q}}2\pmod2,\qquad
f_{n,q}=\begin{cases}
\mathbf1_{2\mid n},&q=2,\\
\displaystyle\sum_{j=0}^{\lfloor n/2\rfloor}\binom{n-2j+q-3}{q-3},&q\ge3.
\end{cases}
\]
The numerator is even, and this formula specifies the residual integral representation for every \(n,q\ge2\).

## Assumptions and scope
A face of the total two-cut complex is any set \(\sigma\subseteq[q]^n\) for which there exist words \(u,v\notin\sigma\) at Hamming distance at least two. The action on geometric realization is simplicial and affine on barycentric coordinates. The diagonal \(S_q\)-action relabels alphabet symbols consistently in every coordinate, commuting with \(S_n\). The wedge statement is an ordinary homotopy equivalence, and the residual-module statement is an actual integral \(S_q\)-lattice isomorphism. The theorem does not assert a residual-group-equivariant wedge decomposition. Reduced homology conventions include \(\widetilde H_0\) for the disconnected \((n,q)=(2,2)\) case.

## Proof
**1. Canonical fixed-point triangulation.** The \(S_n\)-orbits of the word set \([q]^n\) are indexed by histograms \(h=(h_1,\ldots,h_q)\in\mathbb Z_{\ge0}^{q}\) with \(\sum h_i=n\); their number is \(T\). Every fixed point of a simplex has equal barycentric coefficients on vertices in each word orbit. Hence each admissible union of complete word orbits gives a simplex on the corresponding uniformly averaged orbit barycenters, and these simplices form a simplicial complex PL-homeomorphic to \(F_{n,q}\). This construction commutes with alphabet relabelings.

Denote by \(C\) the \(q\) **constant** histogram orbits \((n,0,\ldots,0)\) and its permutations; denote by \(U\) the remaining \(a=T-q\ge1\) histogram orbits. In the orbit complex a subset of histograms is a face exactly when its omitted word orbits contain two nonadjacent words. Every orbit in \(U\) contains words differing at exactly two positions: choose two unequal symbols in a word and swap their positions. Two words from distinct constant orbits differ at all \(n\ge2\) positions. A single constant orbit, however, contains one word only. Therefore the face condition is exactly: either at least one orbit in \(U\) is omitted, or at least two orbits in \(C\) are omitted.

**2. Exact simplicial model and homotopy.** On the disjoint vertex sets \(U,C\), the orbit complex is
\[
\boxed{Y=(\partial\Delta_U*\Delta_C)\ \cup\ (\Delta_U*\operatorname{sk}_{q-3}\Delta_C),}
\]
where \(\operatorname{sk}_{-1}\Delta_C=\{\emptyset\}\) and \(\partial\Delta_{\{u\}}=\{\emptyset\}\). Both pieces have contractible realizations, because the first is a join with the nonempty simplex \(\Delta_C\), and the second is a join with the nonempty simplex \(\Delta_U\). Their intersection is \(\partial\Delta_U*\operatorname{sk}_{q-3}\Delta_C\). For \(q\ge3\), the latter skeleton is a wedge of \(q-1\) spheres of dimension \(q-3\), by the standard simplex-skeleton collapse, while the boundary on \(a\) vertices is the sphere of dimension \(a-2\) (with the conventional empty-sphere case when \(a=1\)). The join is thus a wedge of \(q-1\) spheres of dimension \(a+q-4=T-4\). Gluing two contractible simplicial complexes along their common subcomplex gives its suspension up to homotopy, hence the formula with dimension \(T-3\). For \(q=2\), the model becomes \((\partial\Delta_U*\Delta_C)\cup\Delta_U\) with intersection \(\partial\Delta_U\), a sphere \(S^{a-1}=S^{T-3}\); for \(a=1\), it is an edge disjoint from one vertex and hence has the homotopy type \(S^0\). All assertions apply uniformly to \(n,q\ge2\).

**3. Integral residual module, not merely its rank.** Take the simplicial Alexander dual inside the full simplex on all \(T\) histogram vertices. The face condition above says precisely that the **dual** is the zero-dimensional complex \(D\) consisting of the \(q\) isolated vertices \(C\); the vertices \(U\) are ghosts. Equivariant combinatorial Alexander duality with integral coefficients, including the orientation sign of the full histogram permutation module, gives
\[
\widetilde H_{T-3}(Y;\mathbb Z)
\cong\operatorname{sgn}_{\mathcal H}\otimes\widetilde H^{0}(D;\mathbb Z)
\cong\operatorname{sgn}_{\mathcal H}\otimes
\bigl(\mathbb Z^{[q]}/\mathbb Z(1,\ldots,1)\bigr).
\]
The complex \(D\) has no reduced cohomology in other degrees. The quotient, **not** the kernel-of-sum lattice, is the natural integral cohomology model; those lattices are rationally isomorphic but need not be integrally isomorphic with their group actions. For a symbol transposition, a histogram is fixed precisely when its two associated counts agree. With \(f_{n,q}\) fixed histograms among \(T\), the remaining histograms form \((T-f_{n,q})/2\) interchanged pairs, proving the parity formula. Every alphabet transposition is conjugate and transpositions generate \(S_q\), so this determines \(\operatorname{sgn}_{\mathcal H}\) on all of \(S_q\).

## Verification
The accompanying standard-library script `verify_hamming_fixed.py` enumerates actual Hamming word pairs and orbit types, independently tests every orbit-subset face against the proposed formula, and checks that the Alexander dual contains **exactly** the \(q\) isolated constant histograms. Eleven cases with parameters \((n,q)\) from \((2,2)\) through \((3,4)\) and \((2,5)\) were checked, totaling **1,116,429** orbit-subset tests. For cases small enough to construct boundary matrices, it separately computes mod-two homology. For all tested alphabet symmetries on small examples, **46** signed Lefschetz-character comparisons agree with the predicted top-module trace. It reports `ALL_OK`. Reproduce with `python3 verify_hamming_fixed.py` from the packaged file. These finite checks corroborate but do not replace the infinite-parameter orbit argument and integral Alexander-dual proof.

## Relationship to prior work
Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first posted February 24, 2026), Theorem 52 of the accessible version, identifies the **ordinary nonequivariant** homotopy type of the total two-cut complex for any Cartesian product of complete graphs. A published published-finding corpus result, *Complete coordinate-symmetry homology of Hamming-graph total two-cut complexes* (2026), strengthens it to the complete rational homology character on the **ambient complex** for natural coordinate relabelings and axis swaps. Neither of these statements describes the geometric \(S_n\)-fixed-point locus or its residual **integral** \(S_q\)-module. In general the homology of a geometric fixed set is not determined by the invariant submodule of ambient homology. Bayer and collaborators establish general total-cut constructions and a nonequivariant two-factor case; Chauhan–Shukla–Vinayak study other Cartesian graph products. The present claim refines this literature in a mathematically distinct direction: exact PL fixed-space model, complete integral homotopy ranks, and integral residual symmetry.

## Limitations
The subgroup fixed point theorem concerns **all** coordinate permutations \(S_n\), not arbitrary proper subgroups. The residual integral representation is computed, but an equivariant wedge-of-spheres homotopy equivalence is **not** claimed. No conclusion about the homology of quotient spaces is asserted. The computational checks are finite, and no exhaustive literature search or independent mathematical audit has been performed. A previously unindexed theorem proving the same fixed-space classification would affect the originality claim.

## References
1. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427v1 (first public 2026-02-24), Theorem 52 in the accessible updated PDF, https://arxiv.org/pdf/2602.21427.
2. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, https://arxiv.org/pdf/2209.13503.
3. P. Chauhan, S. Shukla, K. Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486, https://arxiv.org/pdf/2512.04486.
4. *Complete coordinate-symmetry homology of Hamming-graph total two-cut complexes*, published-finding corpus, published 2026, identifier `2026/10/11/SCOPE-complete-coordinate-symmetry-homology-of-hamming-graph-total-two--719066eb9684`.
