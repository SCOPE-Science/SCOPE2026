# Tetrahedral symmetry modules of the truncated-tetrahedron Rips filtration

## Finding
Let \(T\) be the twelve-vertex truncated-tetrahedral graph with its graph shortest-path metric, and let \(K_r=\operatorname{VR}_{\le r}(V(T))\) be the inclusive Vietoris–Rips complex. Permuting the four parent-tetrahedron labels gives a natural action of \(S_4\) on the entire filtration. Write \(V\) for the three-dimensional standard rational representation of \(S_4\) and \(\varepsilon\) for its sign character. Then the **complete positive-degree rational equivariant persistence** is
\[
\widetilde H_1(K_r;\mathbb Q)\cong
\begin{cases}\varepsilon\otimes V,&1\le r<2,\\0,&\text{otherwise},\end{cases}
\qquad
\widetilde H_2(K_r;\mathbb Q)\cong
\begin{cases}\mathbf 1\oplus\varepsilon\oplus V,&2\le r<3,\\0,&\text{otherwise}.\end{cases}
\]
All other positive-degree rational homology groups vanish. The corresponding homology characters on the five conjugacy classes, ordered as identity, transposition, double transposition, three-cycle, and four-cycle, are
\[
\chi_{H_1}=(3,-1,-1,0,1),\qquad
\chi_{H_2}=(5,1,1,2,-1).
\]
Consequently, for \(K_2\) at integer threshold two, the rational reduced second homology of the quotient by the full tetrahedral symmetry group has rank one, whereas the quotient by the rotational subgroup has rank two:
\[
\dim_{\mathbb Q}\widetilde H_2(|K_2|/S_4;\mathbb Q)=1,
\qquad
\dim_{\mathbb Q}\widetilde H_2(|K_2|/A_4;\mathbb Q)=2.
\]

## Assumptions and scope
Put \(V(T)=\{(a,b):a,b\in\{0,1,2,3\},\ a\ne b\}\). Distinct ordered pairs \((a,b)\), \((c,d)\) are adjacent when either \(a=c\) or \((c,d)=(b,a)\). All edges have length one. The graph is connected, cubic, has eighteen edges and diameter three. A simplex belongs to \(K_r\) precisely when the graph distance between every pair of its vertices is at most \(r\); this convention includes the integer threshold. A permutation \(g\in S_4\) acts through \((a,b)\mapsto(g(a),g(b))\). The subgroup \(A_4\) consists of even label permutations. The conclusion concerns rational homology representations and rational homology of orbit spaces, not integral representation lattices or equivariant homotopy equivalences.

## Proof
**Exhaustive cellular ranks.** For each of the twelve vertex labels, breadth-first search using the displayed adjacency rule determines all graph distances. Among the sixty-six unordered vertex pairs, eighteen have distance one, twenty-four have distance two and twenty-four have distance three. Enumerating all nonempty subsets of the twelve vertices and retaining exactly those of diameter at most the threshold gives the following complete face vectors, indexed by face cardinality:
\[
K_1:(12,18,4),\qquad K_2:(12,42,48,12).
\]
In particular, \(K_2\) contains no faces of dimension greater than three. Form the simplicial boundary matrices, and compute their ranks by exact bitwise Gaussian elimination over \(\mathbb F_2\). The ranks for \(K_1\), in degrees one and two, are \((11,4)\); for \(K_2\), in degrees one through three, they are \((11,31,12)\). The included standalone verifier performs every subset and every bit-matrix reduction explicitly.

These mod-two ranks also fix the rational ranks without assuming a universal-coefficient conclusion. Indeed, a matrix with entries \(0,\pm1\) has rank over \(\mathbb Q\) at least its rank modulo two. Connectivity makes the rational degree-one boundary rank exactly eleven. For \(K_1\), the degree-two boundary rank is at most its four columns and so is four. For \(K_2\), the chain relation \(\partial_1\partial_2=0\) bounds the degree-two rank by \(42-11=31\), and the degree-three rank cannot exceed its twelve columns. Thus the displayed ranks hold over \(\mathbb Q\) as well. Consequently, \(K_1\) has \(H_0\cong\mathbb Q\), \(H_1\cong\mathbb Q^3\) and no other rational homology, while \(K_2\) has \(H_0\cong\mathbb Q\), \(H_2\cong\mathbb Q^5\) and no other rational homology. For \(r\ge3\), the graph diameter implies that \(K_r\) is the full eleven-simplex.

**Lefschetz characters.** For a label permutation \(g\), its trace on the degree-\(j\) oriented simplicial chain group is the signed number of \(j\)-faces preserved setwise. Thus its simplicial Lefschetz number is exactly
\[
L_r(g)=\sum_{\substack{\varnothing\ne\sigma\in K_r\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma),
\]
where \(\operatorname{sgn}(g|_\sigma)\) is the parity of the induced permutation on the vertices of the face, ordered lexicographically. Exhaustive evaluation for all twenty-four label permutations, grouped into conjugacy classes, gives:

| Cycle class of \(g\) | Identity | Transposition | Double transposition | Three-cycle | Four-cycle |
| --- | ---: | ---: | ---: | ---: | ---: |
| Class cardinality | 1 | 6 | 3 | 8 | 6 |
| \(L_1(g)\) | -2 | 2 | 2 | 1 | 0 |
| \(L_2(g)\) | 6 | 2 | 2 | 3 | 0 |

The Hopf trace identity and the rational homology concentrations just proved yield \(\chi_{H_1}(g)=1-L_1(g)\) and \(\chi_{H_2}(g)=L_2(g)-1\). The characters of \(\mathbf1\), \(\varepsilon\), \(V\), and \(\varepsilon\otimes V\), in the same class order, are respectively
\[
(1,1,1,1,1),\quad(1,-1,1,1,-1),\quad
(3,1,-1,0,-1),\quad(3,-1,-1,0,1).
\]
Character orthogonality, with class sizes \((1,6,3,8,6)\), gives exactly the stated irreducible decompositions. Since nonzero positive rational homology exists only in degree one at scale one and only in degree two at scale two, no nonzero same-degree persistence map connects the two stages. Each displayed representation is therefore an equivariant interval summand with interval \([1,2)\) or \([2,3)\), respectively.

**Orbit-space corollary.** Barycentric subdivision makes the finite simplicial action without inversions. Over \(\mathbb Q\), averaging identifies the homology of the quotient with the invariant subspace of the original homology. The \(S_4\)-fixed subspace of \(\mathbf1\oplus\varepsilon\oplus V\) is its unique trivial line. On restriction to \(A_4\), both \(\mathbf1\) and \(\varepsilon\) become trivial, while \(V\) retains no invariant vectors. The two quotient ranks follow.

## Verification
Run `python3 verify_tetrahedral_equivariance.py` in the same directory as this document; no third-party packages or external data are needed. The checker independently enumerates all graph distances, all candidate faces at scales one and two, all three relevant mod-two boundary matrices, all twenty-four signed simplicial actions, the character inner products, and both quotient invariant dimensions. Its required final status is `TETRAHEDRAL_EQUIVARIANT_CHARACTER_OK`. This is an exact, finite exhaustive certificate, not an extrapolation from a small sample of a larger family.

## Relationship to prior work
Saleh, Titz Mite, and Witzel (first public version 2023) studied Vietoris–Rips complexes of the five Platonic solids and identified Archimedean solids as a natural extension. Their theorems do not concern the truncated tetrahedron's graph-metric complex. A subsequently published calculation entitled *The graph-metric Rips filtration of the truncated tetrahedron* determines the nonequivariant filtration of this **same twelve-vertex graph**, including \(K_1\simeq\bigvee^3S^1\) and \(K_2\simeq\bigvee^5S^2\); those homotopy types are credited rather than claimed as new. That calculation gives neither the \(S_4\)-characters nor the inequivalent full-symmetry and rotation-only quotient ranks. A five-dimensional vector-space rank alone does not determine its five-component character or distinguish the two quotient ranks. Published intrinsic Čech results for the truncated tetrahedron concern a distinct ball-nerve filtration, and matching-complex results concern matchings of the graph's **edges**, not these Rips simplices.

## Limitations
The theorem determines rational equivariant homology and the resulting rational orbit-space homology, not the integral \(\mathbb Z[S_4]\)-module structure, quotient fundamental groups, or equivariant homotopy types. It is confined to one Archimedean graph and its shortest-path metric; nothing here asserts the same character for its Euclidean metric. Existing nonequivariant sphere-wedge classifications are not new. Exhaustive verification proves these finite calculations but does not prove publication priority; equivalent unindexed work remains a bibliographic risk.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, first public version 2023-02-28, primary MSC 55N31.
2. *The graph-metric Rips filtration of the truncated tetrahedron*, previously published published-finding corpus research result, identifier `51e8cc21-9376-42ca-ac38-e1aa653506e1` (nonequivariant homotopy calculation).
3. *Complete intrinsic Čech persistence of the truncated tetrahedral graph*, published research result, identifier `addb7821a6a6` (different filtration).
4. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, published research result, identifier `f5ae4a359c83` (different simplicial object).
