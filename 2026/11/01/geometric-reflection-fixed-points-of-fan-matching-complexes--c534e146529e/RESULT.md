# Geometric reflection fixed points of fan matching complexes

## Finding
For each integer \(n\ge3\), let \(F_n=K_1\vee P_n\) denote the path-fan graph with rim vertices \(v_1,\ldots,v_n\), apex \(h\), rim edges \(e_i=\{v_i,v_{i+1}\}\) and spokes \(s_i=\{h,v_i\}\). Its *ordinary matching complex* \(\mathcal M(F_n)\) has one vertex per graph edge and one simplex per set of pairwise disjoint graph edges. Let \(\tau(h)=h\) and \(\tau(v_i)=v_{n+1-i}\). The actual geometric fixed-point spaces admit the following piecewise-linear identifications, where \(\operatorname{Ind}(P_0)=\{\varnothing\}\):

\[
|\mathcal M(F_{2m})|^{\langle\tau\rangle}\cong_{\rm PL}|\operatorname{Ind}(P_m)|\quad (m\ge2),
\qquad
|\mathcal M(F_{2m+1})|^{\langle\tau\rangle}\cong_{\rm PL}|\operatorname{Cone}(\operatorname{Ind}(P_{m-1}))|\quad (m\ge1).
\]

Here the cone for \(m=1\) is one point. Consequently, for all odd \(n\ge3\) the fixed set is contractible. For even \(n\ge4\), writing \(m=n/2\), its homotopy type is \(S^{k-1}\) when \(m=3k\) (\(k\ge1\)), contractible when \(m=3k+1\) (\(k\ge1\)), and \(S^k\) when \(m=3k+2\) (\(k\ge0\)). This is the geometric fixed set, not merely its Euler characteristic or the homology-invariant subspace.

## Assumptions and scope
All graph edges are unoriented; matching means pairwise vertex-disjoint. Realizations use the usual affine simplex coordinates. \(P_j\) is a path on \(j\) vertices, and \(\operatorname{Ind}(P_j)\) is its independence simplicial complex. The empty path convention affects only the one-point cone for \(n=3\). Spheres of dimension zero are two-point spaces, not intervals. No regularity or connectivity hypothesis beyond \(n\ge3\) is imposed.

## Proof
**Fixed-orbit lemma.** Let \(K\) be any simplicial complex equipped with a vertex involution \(\tau\). Form the *admissible-orbit complex* \(Q\): its vertices are vertex-orbits \(O\) for which \(O\) is itself a face of \(K\); a set \(\{O_1,\ldots,O_t\}\) is a face if and only if \(\bigcup_j O_j\) is a face of \(K\). The orbit barycenters \(b_O=|O|^{-1}\sum_{x\in O}e_x\) map \(|Q|\) piecewise-linearly onto \(|K|^\tau\). Indeed, a fixed point has equal barycentric coordinates at members of each orbit and its positive-coordinate support is a face, hence a union of admissible orbits; conversely, all such barycenter combinations are fixed points. Distinct orbits have disjoint supports, so barycenter coordinates are uniquely recoverable. This proves a PL homeomorphism, including for points lying on shared simplex boundaries.

Apply the lemma to \(K=\mathcal M(F_n)\). Under reflection, \(e_i\mapsto e_{n-i}\) and \(s_i\mapsto s_{n+1-i}\). Every two-element spoke orbit is forbidden: both spokes meet at \(h\). If \(n=2m\), there is no fixed spoke; the admissible rim orbits are
\[
O_i=\{e_i,e_{2m-i}\}\ (1\le i<m),\qquad O_m=\{e_m\}.
\]
Each is a matching. For distinct indices \(i,j\in\{1,\ldots,m\}\), their unions have an endpoint in common exactly when \(|i-j|=1\). Thus the admissible-orbit complex is precisely \(\operatorname{Ind}(P_m)\), proving the even formula.

If \(n=2m+1\), the admissible rim orbits are \(O_i=\{e_i,e_{2m+1-i}\}\) for \(1\le i<m\). The middle pair \(\{e_m,e_{m+1}\}\) is forbidden, since it meets at the central path vertex. The only admissible spoke orbit is the singleton \(\{s_{m+1}\}\); every admissible rim orbit avoids \(v_{m+1}\) and \(h\), so it is disjoint from that spoke. Distinct rim orbits conflict precisely at successive indices. Therefore the orbit complex is the cone on \(\operatorname{Ind}(P_{m-1})\), proving the odd formula.

It remains to give the sphere dimensions, without inferring an infinite theorem from finite samples. For \(j\ge4\), the open neighborhoods of vertices \(1\) and \(3\) in \(P_j\) satisfy \(N(1)=\{2\}\subseteq N(3)=\{2,4\}\). Consequently any independent set containing vertex \(3\) but not \(1\) can be paired with the independent set obtained by adding \(1\); this is a simplicial elementary-collapse scheme removing all faces containing \(3\). The surviving complex is \(\operatorname{Ind}(P_j-\{3\})\). The remaining graph is the disjoint union of \(P_2\) and \(P_{j-3}\); independence complexes turn graph disjoint unions into joins. Since \(|\operatorname{Ind}(P_2)|=S^0\), this yields
\[
|\operatorname{Ind}(P_j)|\simeq S^0*|\operatorname{Ind}(P_{j-3})|\simeq \Sigma |\operatorname{Ind}(P_{j-3})|.
\]
The three base cases are \(|\operatorname{Ind}(P_1)|\simeq\mathrm{pt}\), \(|\operatorname{Ind}(P_2)|=S^0\) and \(|\operatorname{Ind}(P_3)|\simeq S^0\) (the latter is one edge and an isolated point). The recurrence proves the displayed exhaustive residue-class classification.

## Verification
A standalone deterministic verifier, `verify_fan_fixed.py`, constructs the original fan graph and involution directly. For each \(3\le n\le24\), it independently enumerates admissible reflected edge orbits, checks the full orbit-conflict graph against the claimed path or cone, and cross-checks the alternating face count against the model. For \(3\le n\le18\), it also computes reduced simplicial homology over \(\mathbb F_2\) using exact bit-matrix elimination and confirms the predicted single-sphere or contractible alternatives. All checks passed. These finite checks supplement but do not replace the proof for all \(n\).

## Relationship to prior work
Bayer, Jelić Milutinović and Vega prove that matching complexes of arbitrary outerplanar graphs are contractible or wedges of spheres (first posted 2024-11-07, arXiv:2411.04601); fan graphs form a natural outerplanar family. Their stated nonequivariant conclusion alone does not determine a symmetry's geometric fixed-point space. The present theorem gives such a fixed-point classification, identifying the full PL orbit complex, not only its Betti numbers, Lefschetz trace, or invariant homology. Related matching-complex character computations for cycles and other graph families concern different graphs and/or only rational homology representations.

## Limitations
The finding concerns a single natural reflection of a path-fan graph, not all automorphisms of arbitrary outerplanar graphs; it does not classify the fan matching complex itself or its integral equivariant chain complex. A directly comparable full-text treatment of fan symmetry, if it exists, could affect originality: the closest outerplanar source was accessible only through its abstract/metadata, and institutional full-text retrieval was unavailable. No independent mathematical audit has been completed.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1 (first posted 2024-11-07), https://arxiv.org/abs/2411.04601.
2. `verify_fan_fixed.py`, standalone exact finite verifier accompanying this result (not a proof for unbounded \(n\)).
