# Multiplicity-free symmetric-group homology of Johnson-graph Rips complexes

## Finding

For integers \(n\ge6\) and \(3\le k\le n-3\), let \(J(n,k)\) be the graph of \(k\)-element subsets of \([n]\), in which two vertices are adjacent if they intersect in \(k-1\) elements. Give the vertices shortest-path distance and set \(K_{n,k}=\operatorname{VR}_{\le1}(J(n,k))\), the **inclusive** scale-one Rips complex (equivalently, the graph clique complex). The symmetric group \(S_n\) acts by relabeling \([n]\). Put \(r=\min(k,n-k)-1\). With \(S^{\lambda}\) denoting the rational Specht representation for partition \(\lambda\vdash n\), there is an isomorphism of \(\mathbb Q[S_n]\)-modules

\[
\boxed{\widetilde H_2(K_{n,k};\mathbb Q)\cong
\bigoplus_{j=1}^{r}S^{(n-j-2,j,1,1)}.}
\]

Every summand occurs exactly once. All other reduced rational homology groups vanish, and the full-symmetry invariant subspace in degree two is zero. The vanishing outside degree two and the underlying two-sphere wedge are **previously established facts**; the new statement is the complete multiplicity-free \(S_n\)-representation. For example, \(n=6,k=3\) gives \(S^{(3,1,1,1)}\oplus S^{(2,2,1,1)}\), of dimension \(19\). The dimensions for \((7,3)\) and \((8,4)\) are \(55\) and \(181\).

## Assumptions and scope

Graphs are simple and finite. The Rips convention includes every pair at distance exactly one. The action is that of **relabeling the ground set**, even when complementation produces an extra graph automorphism in the balanced case. All representation statements are over \(\mathbb Q\); no integral Specht direct-sum splitting, equivariant homotopy splitting, or result at other Rips scales is asserted. For \(k>n/2\), complementation of subsets identifies \(J(n,k)\) \(S_n\)-equivariantly with \(J(n,n-k)\), so it suffices to treat \(k\le n/2\). Each partition in the displayed direct sum is valid in this range because \(n-j-2\ge j\ge1\).

## Proof

**1. Two families of maximal cliques and a two-dimensional core.** A star is the collection of all \(k\)-sets containing a fixed \((k-1)\)-set \(A\), and has \(n-k+1\) vertices. A top is the collection of all \(k\)-sets inside a fixed \((k+1)\)-set \(B\), and has \(k+1\) vertices. The elementary common-neighbor argument, also in Shuldiner–Oldford, shows these are all maximal cliques: given adjacent \(A\cup\{u\}\) and \(A\cup\{v\}\), a common neighbor either contains \(A\) or is contained in \(A\cup\{u,v\}\), and the two types cannot mix in a clique. Two distinct maximal cliques intersect in at most two vertices, so every simplex with three or more vertices lies in exactly one star or top. Choose one apex in each clique and collapse its faces of size at least three not containing the apex against their apex cones, in descending cardinality. This yields a connected simplicial two-complex homotopy equivalent to \(K_{n,k}\).

For completeness, its fundamental group is trivial: the Johnson graph is the one-skeleton of the hypersimplex \(\{x\in[0,1]^n:\sum x_i=k\}\), whose two-dimensional faces are all triangles and therefore occur in \(K_{n,k}\). The hypersimplex boundary is a sphere of dimension \(n-2\ge4\), so its two-skeleton is simply connected. It has the whole Johnson graph as its one-skeleton, and adding simplices cannot introduce \(\pi_1\) generators. Hence \(K_{n,k}\) is simply connected; its reduced rational homology is concentrated in degree two. This concentration and the nonequivariant wedge formula also appear in the cited prior classification.

**2. Equivariant augmented Euler class.** Write \(\operatorname{ch}\) for the Frobenius characteristic of a rational \(S_n\)-module, \(h_a\) for a complete symmetric function, \(e_2\) for the second elementary symmetric function, and \(s_{\lambda}\) for the Schur function. The \(S_n\)-modules of the augmented chain complex of \(K_{n,k}\) are finite-dimensional, and the equivariant Euler–Poincaré principle gives

\[
[\widetilde H_2]=-[\widetilde C_{-1}]+[C_0]-[C_1]+\sum_{d\ge2}(-1)^d[C_d]
\]

in the rational representation ring because only \(\widetilde H_2\) survives. The augmentation is the trivial representation, of characteristic \(h_n\). Vertices form the \(k\)-subset permutation module, of characteristic \(h_kh_{n-k}\). An oriented edge corresponds uniquely to a common \((k-1)\)-set, an unordered pair of exchanged labels and the remaining labels. The edge stabilizer interchanges its endpoints with a minus sign; accordingly \(\operatorname{ch}(C_1)=h_{k-1}e_2h_{n-k-1}\).

For a star or top with \(m\) vertices, let \(W_m=\mathbb Q^m\) be its permutation module and \(V_m=\ker(W_m\to\mathbb Q)\) its augmentation module. Its oriented \((q-1)\)-simplices transform as \(\bigwedge^q W_m\). Since \(W_m\cong\mathbf1\oplus V_m\) and the whole simplex has zero augmented virtual Euler characteristic,

\[
\sum_{q=3}^{m}(-1)^{q-1}[\bigwedge^qW_m]
=[\bigwedge^2V_m].
\]

For \(m\ge4\), this exterior square is the irreducible Specht module of shape \((m-2,1,1)\). Each face of cardinality at least three lies in a unique star or top, so we may induce these local Euler classes. The star stabilizer contributes \(h_{k-1}s_{(n-k-1,1,1)}\); the top stabilizer contributes \(h_{n-k-1}s_{(k-1,1,1)}\). Therefore

\[
\begin{aligned}
\operatorname{ch}\bigl(\widetilde H_2(K_{n,k};\mathbb Q)\bigr)
={}&-h_n+h_kh_{n-k}-h_{k-1}e_2h_{n-k-1}\\
&+h_{k-1}s_{(n-k-1,1,1)}+h_{n-k-1}s_{(k-1,1,1)}.
\end{aligned}
\]

**3. Exact Specht cancellation.** The Pieri identity \(e_2h_b=s_{(b,1,1)}+s_{(b+1,1)}\), with \(b=n-k-1\), reduces the preceding expression to

\[
-h_n+h_kh_{n-k}-h_{k-1}s_{(n-k,1)}+h_{n-k-1}s_{(k-1,1,1)}.
\]

Assume \(k\le n/2\) and put \(a=k-1\), \(b=n-k-1\) (so \(1\le a\le b\), in fact \(a\ge2\)). Horizontal-strip Pieri expansions give the three **exact** identities

\[
\begin{aligned}
h_{a+1}h_{b+1}&=\sum_{j=0}^{a+1}s_{(n-j,j)},\\
h_a s_{(b+1,1)}&=\sum_{j=1}^{a+1}s_{(n-j,j)}
+\sum_{j=1}^{a}s_{(n-j-1,j,1)},\\
h_b s_{(a,1,1)}&=\sum_{j=1}^{a}s_{(n-j-1,j,1)}
+\sum_{j=1}^{a}s_{(n-j-2,j,1,1)}.
\end{aligned}
\]

The two-row and three-row terms cancel and the \(j=0\) summand cancels \(-h_n\). Exactly the four-row terms \(s_{(n-j-2,j,1,1)}\), for \(1\le j\le a\), survive. As rational Specht representations are absolutely irreducible and distinct partitions give nonisomorphic modules, their coefficient-one Schur expansion is the claimed direct sum. None has partition \((n)\), so no trivial representation occurs. Complementation proves the result when \(k>n/2\). \(\square\)

## Verification

The bundled standard-library scripts `verify_johnson_rep.py` and `decompose.py` can be run using Python 3, from the same directory, with `python3 verify_johnson_rep.py` and `python3 decompose.py`. The first independently enumerates clique-complex simplices and calculates signed fixed-simplex traces, then compares them to a separate star/top local-wedge trace. It checks every permutation at \((n,k)=(6,3),(7,3)\), plus one representative of each of the 22 conjugacy classes at \((8,4)\), for 5,782 trace comparisons; mod-two boundary ranks check homology in the first two cases. The second computes character inner products by an explicit Murnaghan–Nakayama recursion and matches the stated Specht list for six cases \((6,3),(7,3),(8,3),(8,4),(9,4),(10,5)\). The checks completed successfully. Finite calculations corroborate, but do not prove, the universal quantifiers; the chain-module/Pieri proof supplies the unbounded result.

## Relationship to prior work

Shuldiner and Oldford, arXiv:2208.12710, classify the two maximal Johnson clique families, but do not determine topological representations. *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes* (public research record listed below) already proves the full nonequivariant wedge-of-two-spheres statement and its Betti-number formula over the exact same parameter range; it explicitly does **not** classify functorial or symmetric-group actions. The present claim is thus the **representation-level refinement**, not a new nonequivariant classification. Goyal, Shukla and Singh, arXiv:2009.12130, examine clique complexes of line graphs, including the Johnson boundary case \(k=2\), excluded here. Spectral decompositions of Johnson graph vertex permutation modules are weaker than a decomposition of second homology after oriented edges and higher-dimensional simplex relations are incorporated.

## Limitations

The decomposition is rational; it does not assert an integral splitting into Specht lattices or a canonical basis of geometric two-spheres. It concerns relabeling symmetries, not arbitrary graph automorphisms beyond this action, and only the inclusive scale-one complex in the indicated range. A differently indexed equivalent character calculation in the literature cannot be categorically ruled out; the originality comparison refers to the inspected sources and searches, not an independent certification. The finite programs do not verify all integers \(n,k\); no stronger computational or human-independent assurance is asserted.

## References

1. P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710, first public version 2022-08-26, especially the classification of star and top cliques. https://arxiv.org/abs/2208.12710
2. *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, publicly available original topology classification (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sphere-wedge-collapse-of-scale-one-johnson-graph-rips-complexes--c10287ed1518
3. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (2020), a distinct boundary case. https://arxiv.org/abs/2009.12130
