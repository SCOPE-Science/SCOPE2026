# The surviving Euclidean two-sphere in the truncated tetrahedron's Rips filtration

## Finding

Let \(V\) be the twelve vertices of the regular truncated tetrahedron with unit edge length, equipped with *ambient Euclidean chord distance*. Write \(K_r=\operatorname{VR}_{\le r}(V)\) for the inclusive Vietoris–Rips complex. For every real \(r\ge0\),
\[
K_r\simeq
\begin{cases}
\bigvee^{11} S^0,&0\le r<1,\\
\bigvee^{3} S^1,&1\le r<\sqrt3,\\
\bigvee^{5} S^2,&\sqrt3\le r<2,\\
S^2,&2\le r<\sqrt5,\\
\ast,&r\ge\sqrt5.
\end{cases}
\]
All integral homology groups are free abelian. More strongly, the map
\[
H_2(K_{\sqrt3};\mathbb Z)\longrightarrow H_2(K_2;\mathbb Z)
\]
induced by inclusion is **surjective**, with a primitive geometric generator supplied by an oriented triangulation of the boundary of the original convex truncated tetrahedron. Thus its full reduced integral persistence barcode consists of eleven degree-zero intervals \([0,1)\), three degree-one intervals \([1,\sqrt3)\), four degree-two intervals \([\sqrt3,2)\), and one degree-two interval \([\sqrt3,\sqrt5)\). The surviving sphere is an actual persistent integral class, not merely two equal Betti numbers at consecutive thresholds.

## Assumptions and scope

Take \(p_0=(1,1,1)\), \(p_1=(1,-1,-1)\), \(p_2=(-1,1,-1)\), and \(p_3=(-1,-1,1)\). Index the twelve points by ordered distinct labels \((a,b)\), and set
\[
v_{a,b}=\frac{2p_a+p_b}{2\sqrt2},\qquad a,b\in\{0,1,2,3\},\ a\ne b.
\]
These are precisely the vertices obtained by uniform one-third truncation followed by scaling to unit edge length. Distances are Euclidean chords, **not** shortest-path distances along the edge graph. Simplices enter at equality to their diameter; half-open persistence intervals use this inclusive convention. There are no assertions for other truncation ratios, other metrics, or points on the entire polyhedral surface.

## Proof

**Exact critical distances.** Without the common factor \(1/\sqrt8\), the twelve integer coordinate vectors are \(2p_a+p_b\). Their 66 unordered squared pair distances consist of 18 copies of \(8\), 24 of \(24\), 12 of \(32\), and 12 of \(40\). Therefore, after unit-edge normalization, distinct distances are exactly \(1,\sqrt3,2,\sqrt5\); the complex is constant between these values.

**The three noncontractible positive stages.** Exhaustive combinatorial clique enumeration yields face vectors (indexed from dimension zero)
\[
\begin{array}{c|c}
 r& (f_0,f_1,f_2,\ldots)\\\hline
 1&(12,18,4)\\
 \sqrt3&(12,42,48,12)\\
 2&(12,54,112,108,48,8).
\end{array}
\]
The attached explicit acyclic discrete-Morse matchings, checked in the accompanying verifier, respectively have the critical-cell vectors
\[
(c_0,c_1,c_2,c_3,\ldots)=(1,3,0,0,\ldots),\quad
(1,0,5,0,\ldots),\quad
(1,0,1,0,\ldots).
\]
Each matching is an exhaustive pairing of *all* the face-poset elements other than the displayed critical cells. Each lower face is a codimension-one face of its matched upper face, no face participates twice, and the directed Hasse graph obtained by reversing matched incidences is acyclic; the verifier reconstructs all these assertions from the actual certificates. Forman's discrete Morse theorem therefore yields CW models with one zero-cell and, respectively, three one-cells, five two-cells, or one two-cell. Since there are no other critical cells, their homotopy types are the displayed wedges of circles or spheres. At \(r<1\) the twelve vertices are disconnected, and at \(r\ge\sqrt5\) all twelve vertices span an eleven-simplex.

**Primitive persistence map.** The oriented convex boundary \(\partial\operatorname{conv}(V)\) is a two-sphere with four triangular and four regular hexagonal facets. Triangulate each hexagon into its three short-ear triangles and one central alternating triangle. Every edge in this triangulation has Euclidean length \(1\) or \(\sqrt3\). Its oriented fundamental two-cycle \(Z\) consequently belongs to the chain complex of \(K_{\sqrt3}\). It has 20 signed triangles, and its integral simplicial boundary is zero.

There is an explicit sequence of 146 elementary free-face collapses of \(K_2\) onto a subcomplex with face vector \((10,24,16)\). Each edge of that subcomplex belongs to exactly two triangles, every vertex link is one cycle, and the subcomplex is connected with Euler characteristic two. Hence it is a triangulated two-sphere. For each collapsed free triangle \(\sigma\) belonging to a unique tetrahedron \(\tau\), replace an integral two-chain \(W\) by
\[
W-\frac{[W:\sigma]}{[\partial\tau:\sigma]}\partial\tau.
\]
The incidence coefficient in the denominator is \(\pm1\), so this is an exact integral chain-level elementary-collapse retraction. Other-dimensional elementary collapses act identically on the remaining two-cycle. Applying all 146 substitutions to \(Z\) yields the fundamental cycle of the remaining triangulated sphere: every one of its sixteen triangles has coefficient \(\pm1\), with compatible orientations. These facts are recomputed and checked with integer arithmetic in `verify.py`. Thus the inclusion sends \([Z]\) to a **primitive generator** of \(H_2(K_2;\mathbb Z)\cong\mathbb Z\). In particular, \(\mathbb Z^5\to\mathbb Z\) is split-surjective. Together with the other stage homology groups and the final contractible stage, this proves the stated integral interval decomposition.

## Verification

Run `python3 verify.py` using only the Python standard library. It reads `certificates/tt8_certificate.json`, `certificates/tt24_certificate.json`, and `certificates/tt32_certificate.json`. The program enumerates every nonempty simplex at each critical stage, independently reconstructs each oriented Hasse diagram and tests its acyclicity, builds the outward-oriented geometric boundary cycle without floating-point calculations, replays all 146 elementary sphere collapses, checks the final two-manifold links and connectedness, and verifies that the surviving two-cycle has primitive coefficient one. The supplied `verification_output.txt` records an execution ending in `VERIFY_OK`. The finite checks are exhaustive for this exact twelve-point configuration; no extrapolation to another graph or an infinite family is asserted.

## Relationship to prior work

The pre-2016 truncated-tetrahedral twelve-state model of Krčmár, Gendiar, and Nishino supplies a natural finite geometric configuration but does not study Rips topology. The existing **graph-metric** truncated-tetrahedral Rips classification establishes three circles at graph radius one and five two-spheres at graph radius two. Those two complexes agree with the *first two nontrivial Euclidean stages here*. This overlap is acknowledged. However, graph-distance three inserts all remaining graph edges simultaneously and makes its final complex a simplex, whereas Euclidean distance separates twelve distance-two pairs from twelve distance-\(\sqrt5\) pairs. The surviving two-sphere at Euclidean radius \(2\) and, especially, its *primitive persistence map* are therefore not implied by that graph-metric classification.

Saleh, Titz Mite, and Witzel classify Rips complexes of the **Platonic** solids. Saleh's dissertation develops those theorems and includes a short numerical discussion of other polyhedra, but not the truncated-tetrahedral Euclidean classification here. The closest published geometric and combinatorial sources were inspected for equivalent parameterizations, stronger general results, and tabulated computations; absence from a search is not proof of universal novelty.

## Limitations

The claim covers one canonical twelve-point geometric object with the exact regular truncation ratio and ambient Euclidean distance. It does not apply to arbitrary truncations, intrinsic metric Rips complexes, persistent cohomology ring structures, or equivariant actions. The recorded mathematical checks are reproducible but not independently audited. Prior-publication comparisons remain limited by document accessibility and indexing, especially any unindexed polyhedral point-cloud computation.

## References

1. R. Krčmár, A. Gendiar, and T. Nishino, “Phase diagram of truncated tetrahedral model,” arXiv:1512.09059, first publicly posted **2015-12-30**, Sections I–II (twelve vertex orientations).
2. N. Saleh, T. Titz Mite, and S. Witzel, “Vietoris–Rips complexes of Platonic solids,” arXiv:2302.14388, first posted 2023-02-28.
3. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, dissertation, Justus-Liebig-Universität Gießen (2023), especially Chapters 2–3.
4. “The graph-metric Rips filtration of the truncated tetrahedron,” published mathematical research record `2026/10/4/SCOPE-the-graph-metric-rips-filtration-of-the-truncated-tetrahedron--51e8cc219376` in the published-finding corpus/2026 public archive (2026-10-04).
5. R. Forman, “Morse theory for cell complexes,” *Advances in Mathematics* **134** (1998), 90–145 (the acyclic-matching theorem).
