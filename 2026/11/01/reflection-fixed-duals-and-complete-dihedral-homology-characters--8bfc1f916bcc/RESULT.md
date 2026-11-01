# Reflection-fixed duals and complete dihedral homology characters of cycle-power three-cut complexes

## Finding
For every integer \(p\ge2\) and \(n\ge6p-3\), put \(G=C_n^p\), with vertices \(\mathbb Z/n\mathbb Z\) and edges at circular distance at most \(p\). Let \(K=\Delta_3(G)\) be the **ordinary** three-cut complex (facets complement disconnected induced triples). Let \(r(i)=i+1\), \(s(i)=-i\), and let \(D_n=\langle r,s\rangle\). Its reduced rational homology is concentrated in degree \(n-4\), with dimension
\[
\beta=1+\frac{n(n-4p-1)}2.
\]
The following **reflection character**, previously absent from the known cyclic character, completes the dihedral character on \(H=\widetilde H_{n-4}(K;\mathbb Q)\). Set \(m=\lfloor n/2\rfloor\):
\[
\operatorname{tr}(r^a s\mid H)=
\begin{cases}
(-1)^m(2p-1-m),&n=2m+1,\\
(-1)^{m-1}(2p+1-m),&n=2m,\ a\text{ even},\\
(-1)^m(2p-1-m),&n=2m,\ a\text{ odd}.
\end{cases}
\]
For completeness, the rotation character, already established in [2], is \(\beta\) at the identity, \((-1)^m(1-m)\) at the half-turn \(r^m\) when \(n=2m\), and \((-1)^{n-\gcd(n,a)}\) at every other nonidentity \(r^a\). Thus these formulas determine the full rational \(D_n\)-character. Its invariant dimension is
\[
\dim H^{D_n}=
\begin{cases}
0,&n=2m+1,\ m\text{ even},\\
m-2p+1,&n=2m+1,\ m\text{ odd},\\
(m-2p-2)/2,&n=2m,\ m\text{ even},\\
(m-2p+1)/2,&n=2m,\ m\text{ odd}.
\end{cases}
\]
All displayed multiplicities are nonnegative integers in the stated parameter range.

Stronger geometric input: the actual fixed space of the **Alexander-dual complex** \(L=K^\vee\) under any reflection is a disjoint union of contractible components. The number of components is \(m-2p+2\) for odd \(n=2m+1\), \(m-2p\) for even \(n=2m\) and a vertex-axis reflection \(r^{2a}s\), and \(m-2p+2\) for even \(n=2m\) and an edge-axis reflection \(r^{2a+1}s\). No assertion that the *cut complex* fixed spaces have these types is made.

## Assumptions and scope
A *face* of the simplicial Alexander dual \(L\) is a subset \(T\) of vertices in which every induced three-vertex subgraph of \(G\) is connected. Equivalently, every vertex of \(T\) has at most one nonneighbor inside \(T\). Every singleton and pair belongs to \(L\), and \(L\) is connected. For \(p\ge2\) and \(n\ge6p-3\), the published shelling theorem [1] gives \(K\simeq\bigvee^\beta S^{n-4}\), and Alexander duality gives reduced cohomology of \(L\) concentrated in degree one, of rank \(\beta\). Our character statements use rational coefficients; the decomposition into contractible components is integral/geometric.

## Proof
**1. The geometric orbit triangulation.** For an involution \(g\) acting on vertices of any finite simplicial complex, a point in the realization is fixed exactly when its barycentric coordinates are constant along every \(g\)-orbit. Such a fixed point is a convex combination of normalized uniform orbit barycenters. The orbit barycenters span a simplex precisely when the union of their underlying orbits is a face. Thus \(|L|^{\langle g\rangle}\) is PL homeomorphic to the orbit complex of admissible orbit unions. We analyze this simplicial complex for reflections.

**2. Pair confinement lemma.** Write \(d(u,v)=\min((u-v)\bmod n,(v-u)\bmod n)\). First consider \(g(i)=-i\) and nontrivial reflection orbits \(O_i=\{i,n-i\}\), where \(0<i<n/2\). For \(0<i<j<n/2\), the four cross-orbit distances fall into two repeated values
\[
D_1=j-i,\qquad D_2=\min(i+j,n-i-j),
\]
and the within-orbit distances are \(E_i=\min(2i,n-2i)\) and \(E_j=\min(2j,n-2j)\). If both \(D_1\) and \(D_2\) exceed \(p\), any vertex has two nonneighbors, so the union is forbidden. If \(D_2\le p\), then either \(i+j\le p\), or \(n-i-j\le p\): both orbits lie near the same reflection axis. Otherwise \(D_2>p\), hence \(D_1\le p\). The cross nonneighbor is already present at every vertex, forcing \(E_i,E_j\le p\). These inequalities put both indices in the narrow neighborhoods of the axes, namely \(i\le p/2\) or \(i\ge(n-p)/2\), likewise for \(j\). The two neighborhoods are separated by more than \(p\), since \(n\ge6p-3\) and \(p\ge2\); because \(D_1=j-i\le p\), both indices are near the same axis. In particular any compatible pair of nontrivial orbits lies wholly in a block of width at most \(p\) around one axis. For a fixed singleton vertex, a pair orbit outside its radius-\(p\) block makes that singleton have two nonneighbors, so it cannot be adjacent in the orbit complex. Distinct fixed singletons themselves form an admissible two-element face.

For a reflection through two edges (possible only when \(n\) is even), relabel its orbits \(O_i=\{-i,1+i\}\), \(0\le i<n/2\). The identical argument uses the cross distances \(j-i\), \(\min(i+j+1,n-i-j-1)\), and internal distances \(\min(2i+1,n-2i-1)\). It places every compatible orbit pair wholly within the first \(p\) or last \(p\) orbits. No pair joins the two end blocks.

**3. Contractible components and their count.** If \(n=2m+1\), for the representative reflection \(s\) label the orbits \(O_0=\{0\}\) and \(O_i=\{i,n-i\}\) for \(1\le i\le m\). By step 2, all edges, hence every nontrivial simplex, are contained in the index blocks \(A=\{0,\ldots,p\}\) or \(B=\{m-p+1,\ldots,m\}\). The induced subcomplex on \(A\) is a cone with apex \(O_0\): its unique vertex is adjacent in \(G\) to every other underlying vertex in \(A\). The subcomplex on \(B\) is a cone with apex \(O_m\), the orbit of the two vertices bordering its reflection axis, likewise adjacent to all underlying vertices in \(B\). Every intermediate orbit indexed \(p+1,\ldots,m-p\) is isolated. Therefore there are \(2+(m-2p)\) contractible components.

If \(n=2m\) and the reflection fixes the opposite vertices \(0,m\), its orbit blocks are \(A=\{0,\ldots,p\}\) and \(B=\{m-p,\ldots,m\}\). Each block is conical with respective apex \(O_0=\{0\}\) and \(O_m=\{m\}\). The only cross-block edge is the edge between those two fixed singleton orbits; no higher simplex can contain that bridge. Thus the two cones and the bridge form one contractible component. The intermediate indices \(p+1,\ldots,m-p-1\) are isolated, giving \(1+(m-2p-1)=m-2p\) components.

If \(n=2m\) and the axis runs through opposite edges, the orbits \(O_i=\{-i,1+i\}\), \(0\le i<m\), split into two conical blocks indexed \(0,\ldots,p-1\) and \(m-p,\ldots,m-1\), with apices \(O_0\) and \(O_{m-1}\). The \(m-2p\) intermediate vertices are isolated, giving \(m-2p+2\) contractible components. These blocks are disjoint in the full stated range. Conicality remains valid for faces of arbitrarily high dimension: adding an apex introduces *no new nonedge*, not just pairwise compatibility. Rotating the axis covers all \(r^as\).

**4. Reflection trace.** For a finite simplicial automorphism the Lefschetz number equals the Euler characteristic of its geometric fixed set. Since \(L\) is connected and \(H^j(L;\mathbb Q)=0\) for \(j\ne0,1\), it follows that \(\operatorname{tr}(g\mid H^1(L;\mathbb Q))=1-\#\pi_0(|L|^g)\). The complementary-simplex equivariant Alexander-duality map contributes the permutation orientation sign on all \(n\) vertices. A reflection with \(t\) exchanged vertex pairs has sign \((-1)^t\). For odd \(n=2m+1\), \(t=m\); for even \(n=2m\), \(t=m-1\) on vertex axes and \(t=m\) on edge axes. Multiplying \(1-\#\pi_0\) by these signs gives exactly the three displayed reflection formulas.

**5. Dihedral invariants.** The published complete rotation character [2] has trace \(\beta\) at identity, \((-1)^m(1-m)\) at the half-turn if present, and the permutation sign at remaining rotations. Average this known rotation character and the newly established reflection character over \(2n\) dihedral elements. For \(n=2m+1\) this gives \((m-2p+1)(1-(-1)^m)/2\). For \(n=2m\) the sum gives \((2m-4p-1-3(-1)^m)/4\), equivalent to the displayed parity cases. By the Reynolds averaging projection these are precisely the dimensions of \(D_n\)-fixed homology.

## Verification
Run `python3 verify.py` with standard Python 3. It independently constructs reflection orbits from the labeled cycle, enumerates admissible orbit-union faces, verifies the exact character and component counts for \(126\) parameter/axis cases with \(2\le p\le8\) and \(6p-3\le n\le6p+5\), checks local conical structure on all enumerated orbit faces, and separately reconstructs the **original three-cut complex** for \(21\) smaller cases to compute reflection traces directly using signed fixed simplicial chains. The run returned `VERIFY_OK orbit_cases=126 orbit_faces=6447 direct_cut_cases=21`. These are finite cross-checks, not the proof of the unbounded theorem.

## Relationship to prior work
Chauhan and Shukla [1] prove shellability and the rank \(\beta\) for this exact graph family and parameter range, but give no reflection character in the accessible description. The published published-finding corpus result [2] supplies the **complete cyclic rotation** character and the equivariant Alexander-duality identification, but explicitly limits its result to the cyclic subgroup and does not give a reflection character. Both facts are used, not claimed here as new. Bayer and collaborators [3,4] cover dihedral and cyclic representations for **unpowered** cycles and exceptional squared-cycle parameters; their cited results do not imply the general reflection character for arbitrary \(p\ge2\). A squared-cycle shellability theorem [5] is nonequivariant. The contribution here is the explicit reflection-fixed dual geometry, every reflection trace, and the resulting full dihedral invariant dimension, with exact implication comparisons in the accompanying review.

## Limitations
The theorem requires \(p\ge2\), \(n\ge6p-3\), the ordinary (not total) three-cut complex, and the standard dihedral action. It does not claim an integral dihedral module decomposition, an equivariant splitting as a wedge of spheres, or a homotopy classification for the geometric fixed locus of the original cut complex. The full original text of [1] was inaccessible during the comparison; an accessible abstract, an independent detailed technical summary, and the complete published cyclic proof [2] were examined. A hidden equivalent result in [1] or unindexed work remains an originality risk; there is no independent audit.

## References
1. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1, first published 2026-03-24; Theorem 1.4 (per [2] and available technical overview). https://arxiv.org/abs/2603.23155
2. *Rational cyclic homology representations of three-cut complexes of cycle powers*, published research record, 2026-10-11; RESULT.md gives the full cyclic character and proof. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-rational-cyclic-homology-representations-of-three-cut-complexes--dc0f17aad16d
3. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, especially Theorem 7.15 and Proposition 7.29. https://arxiv.org/abs/2304.13675
4. M. Bayer et al., *Topology of Cut Complexes II*, arXiv:2407.08158, especially Theorem 6.6. https://arxiv.org/abs/2407.08158
5. P. Chauhan, S. Shukla and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979 (originally 2024-06-04). https://arxiv.org/abs/2406.01979
