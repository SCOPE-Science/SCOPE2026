# Alternating-symmetry exceptions in two-point complete-graph configuration quotients

## Finding

Let \(K_m\) be the complete simple graph on \(m\ge 2\) vertices, with each edge realized as a closed unit interval, and let \(X_m=\operatorname{UConf}_2(|K_m|)\) be its ordinary collision-free **unordered** two-point configuration space. The vertex relabeling actions of the full symmetric group \(\mathfrak S_m\) and its alternating subgroup \(\mathfrak A_m\) induce actions on \(X_m\).

The complete homotopy classifications of their ordinary orbit spaces are
\[
X_m/\mathfrak S_m\simeq *,\qquad
X_m/\mathfrak A_m\simeq
\begin{cases}
S^1,&m=3\text{ or }m=4,\\
*,&m=2\text{ or }m\ge 5.
\end{cases}
\]
The stronger finite-model assertion is that both quotients strongly deformation retract to the corresponding barycentrically triangulated, two-particle discrete-cell orbit spaces. For \(\mathfrak S_m\), the models are respectively a point (\(m=2\)), a closed interval (\(m=3\)), and one closed triangle (\(m\ge4\)). For \(\mathfrak A_m\), they are respectively a point, a circle made of two edges, a closed disk with two distinct boundary vertices identified (\(m=4\)), a closed disk (\(m=5\)), and a closed triangle (\(m\ge6\)). In particular, the exceptional \(m=4\) quotient has fundamental group \(\mathbb Z\), not merely nonzero rational first homology.

## Assumptions and scope

The graphs are geometric realizations of **simple** complete graphs with unit-length edges, not Euclidean point configurations or graph embeddings in a plane. Particles are indistinguishable; equality of their graph positions is excluded. The quotients are ordinary topological orbit spaces by vertex permutations, not homotopy/Borel quotients. \(\mathfrak A_2\) is trivial. No claim is made about three or more particles or arbitrary graph automorphism subgroups.

Let \(D_m\subset X_m\) consist of unordered pairs whose **minimal closed supporting cells** (a vertex for a particle at a vertex, or the closed edge for a particle in the interior of an edge) are disjoint. This is the unordered two-point discretized cubical complex. Its zero-cells are unordered pairs of distinct graph vertices; its one-cells are a vertex together with a nonincident edge; and its square two-cells are unordered pairs of vertex-disjoint edges. It is preserved by all vertex permutations.

## Proof

**Step 1: explicit equivariant strong deformation retraction.** The following argument works for any finite simple graph having unit edges. For a collision-free pair on one common closed edge with coordinates \(0\le x<y\le1\) in either chosen orientation, set
\[
H_t(\{x,y\})=\{(1-t)x,(1-t)y+t\},\qquad0\le t\le1.
\]
This is independent of reversing the edge orientation after the two positions are regarded as unordered. If the positions are on the interiors of *distinct* edges meeting at a vertex \(v\), write \(s,u\in(0,1)\) for their respective distances from \(v\) along these edges and put
\[
H_t(s,u)=\left((1-t)+\frac{t}{\max(s,u)}\right)(s,u).
\]
If their minimal closed supporting cells are disjoint, keep the pair fixed. At a boundary where one position lies at a common endpoint, the first formula gives \((0,(1-t)u+t)\), exactly the second formula with \(s=0\). When a position reaches a *remote* endpoint, the second formula has \(\max(s,u)=1\) and is the identity. The analogous endpoint limits agree on either edge, and all other overlaps are already fixed. The formulas thus glue to one continuous homotopy of \(X_m\), with no need to extend across the excluded collision locus.

No collision occurs: the first formula strictly increases the gap between the ordered positions; in the second, the common endpoint is never simultaneously occupied by both particles. At \(t=1\), a same-edge pair occupies opposite endpoints, while an incident-edge pair has at least one particle at an endpoint remote from the common vertex. Both configurations lie in \(D_m\). All points of \(D_m\) remain fixed for every \(t\): they correspond to distinct vertices, a nonincident vertex and edge, disjoint edges, or incident edges with at least one occupied remote endpoint. Only distances from shared vertices and unoriented edge coordinates enter, so \(H_t\) commutes with every graph automorphism. Consequently the homotopy descends to a **strong deformation retraction** \(X_m/G\searrow D_m/G\) for both \(G=\mathfrak S_m\) and \(G=\mathfrak A_m\).

**Step 2: flag triangulations and orbit counts.** Barycentrically triangulate each square of \(D_m\). Vertices of the resulting simplicial complex are barycenters of cubical cells of dimensions zero, one, or two. Every triangle is a strict chain \(v<e<q\) of a corner, incident side, and square. Every quotient simplex has vertices of different dimension types, so no group element acts by an inversion of that simplex. The ordinary group quotient is therefore the finite \(\Delta\)-complex formed by orbits of flags (allowing parallel edges and distinct triangles with the same vertices).

For \(m\ge4\), the \(\mathfrak S_m\)-action is transitive on the individual cells and on each flag type, because any four distinct vertex labels can be mapped to any other four. Thus there are exactly three vertex orbits, three edge orbits, and one triangle orbit: the quotient is a single triangle. For \(m=3\), there is no square and the symmetric quotient is an interval; for \(m=2\), only one zero-cell survives.

For alternating permutations, every orbit of a symmetric action either remains one orbit or splits into two, according to whether its stabilizer contains an odd permutation. A \(0<1\) flag uses three labels and has stabilizer \(\mathfrak S_{m-3}\): it splits precisely at \(m=3,4\). A \(0<2\) flag uses four labels and has an even involution swapping its two square coordinates (plus arbitrary permutations of unused labels): it splits precisely at \(m=4,5\). A \(1<2\) flag has a transposition of the two endpoints of its moving edge in its stabilizer, so it never splits. Finally, a full \(0<1<2\) flag uses four distinct labels and has stabilizer \(\mathfrak S_{m-4}\), so its orbit splits precisely for \(m=4,5\). For \(m\ge6\), every flag orbit is unsplit. These observations give the following exact numbers of quotient cells:

| Group and range | Zero-cells | One-cells | Two-cells |
|---|---:|---:|---:|
| \(\mathfrak S_2\), \(\mathfrak A_2\) | 1 | 0 | 0 |
| \(\mathfrak S_3\) | 2 | 1 | 0 |
| \(\mathfrak A_3\) | 2 | 2 | 0 |
| \(\mathfrak S_m\), \(m\ge4\) | 3 | 3 | 1 |
| \(\mathfrak A_4\) | 3 | 5 | 2 |
| \(\mathfrak A_5\) | 3 | 4 | 2 |
| \(\mathfrak A_m\), \(m\ge6\) | 3 | 3 | 1 |

**Step 3: exceptional attaching data.** Label the three quotient vertices by \(v_0,v_1,v_2\). For \(\mathfrak A_4\), the five edges are \(e_0,e_1:v_0\to v_1\), \(e_2,e_3:v_0\to v_2\), and \(e_4:v_1\to v_2\). The two triangles have boundary-edge sets \(\{e_0,e_3,e_4\}\) and \(\{e_1,e_2,e_4\}\). They share the one edge \(e_4\); their opposite vertices are identified to \(v_0\), yielding a disk with two boundary vertices identified. Collapse the first triangle along \(e_0\), the second along \(e_1\), and then \(e_4\) with the free vertex \(v_1\). What remains is exactly the pair of parallel edges \(e_2,e_3\) connecting \(v_0\) and \(v_2\), a circle.

For \(\mathfrak A_5\), edges are \(e_0:v_0\to v_1\), \(e_1,e_2:v_0\to v_2\), and \(e_3:v_1\to v_2\). The two triangles have edge sets \(\{e_0,e_2,e_3\}\) and \(\{e_0,e_1,e_3\}\). They are joined along the two-edge boundary path \(e_0\cup e_3\), making a closed disk. They collapse, first along \(e_2\), then along \(e_0\), leaving the tree \(e_1\cup e_3\), which collapses to a vertex. For \(\mathfrak A_3\), the quotient is simply two vertices connected by two parallel edges and hence is a circle. All the remaining complexes are points, intervals, or single triangles and are contractible. Combined with Step 1, this completes the asserted homotopy classification and the stronger orbit-model description.

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies in the same directory as the accompanying files. The program generates the complete cubical cells, their barycentric flags, and all permutations for \(2\le m\le6\), computes the flag orbit models for both symmetry groups, checks the quotient boundary-square identity, independently reduces their cellular chain matrices over \(\mathbb Q\), and performs explicit valid free-face collapses. It writes `orbit_certificate.json` and terminates with `RATIONAL_SAMPLE_EQUIVARIANCE_OK` and `VERIFY_OK` when successful. Finite checks demonstrate the small exceptional orbit incidences and the first \(m=6\) stabilized case; **the group-stabilizer argument, not finite extrapolation, proves all larger sizes**. Exact rational sample checks of the deformation also test collision avoidance, identity at \(t=0\), the time-one target, and permutation equivariance for \(m=3,4,5\). Continuity for every graph configuration is established mathematically in Step 1, not by finite sampling.

## Relationship to prior work

Abrams and Ghrist's 2000 exposition establishes the substantial underlying topology of the *ordered* two-point configuration space of \(K_5\), including its genus-six surface model. Prue and Scrimshaw (2009, revised 2014) prove a general non-equivariant discretized-configuration equivalence. Neither of those facts alone specifies the quotient by **vertex relabeling**, especially the alternating subgroup. Barnett and Farber (2009) study ordered graph-configuration (co)homology, not the present alternating quotient models.

Ramos and Yun (2026), Table 2, determine rational symmetric-group representations for the *unordered* two-point configuration spaces of complete graphs, including a sign constituent for \(m=4\). Thus **the rational first-Betti-number exception for the \(\mathfrak A_4\) quotient follows from that published representation calculation by transfer and is not claimed as new**. The claim here is the precise integral homotopy classification, explicit quotient \(\Delta\)-complexes, and actual collision-preserving group-equivariant deformation from the continuous spaces to the finite models. Rational character data by itself does not determine their fundamental groups or these attaching maps.

## Limitations

The retraction presumes the standard unit-edge topological realization of a finite simple graph and acts only on configurations of two distinct unordered points. The theorem compares ordinary orbit spaces, not Borel quotients and not subgroups other than the full symmetric and alternating groups. The topological quotient classifications use a non-equivariant simplicial collapse only **after** passing to the orbit space. The finite checker does not prove the uniform theorem independently of the arguments given above. The result is not independently audited. An equivalent treatment of the orbit spaces outside the searchable indexed literature remains a publication-priority risk.

## References

1. A. Abrams and R. Ghrist, *Finding topology in a factory: configuration spaces*, arXiv:math/0009118, first submitted 2000-09-12, especially Sections 5–6 and the \(K_5\) example.
2. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180, first submitted 2009-03-12.
3. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511, first submitted 2009-09-30, Theorem 3.2.
4. E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813, first submitted 2026-06-11, Section 3 and Table 2.
