# Full cubic symmetry on two-particle configuration homology of the three-cube

## Finding

Let \(Q_3\) be the one-skeleton of the ordinary three-dimensional cube, with vertices \(\mathbb F_2^3\) and edges joining bit strings differing in one position. Set \(X=\operatorname{UConf}_2(|Q_3|)\), the space of unordered pairs of distinct points of its geometric realization. Its full automorphism group is \(G=(\mathbb Z/2)^3\rtimes S_3\), of order \(48\).

Let \(V\) be the three-dimensional signed-coordinate representation of \(G\): if \(g=(t,p)\) acts on bit strings by \(x\mapsto t\oplus p(x)\), then on the basis of \(V\) it sends \(e_i\mapsto(-1)^{t_{p(i)}}e_{p(i)}\). Let \(\eta(t,p)=(-1)^{t_1+t_2+t_3}\), let \(W\) be the two-dimensional standard representation of \(S_3\) inflated to \(G\), and put \(\varepsilon=\det V=\eta\operatorname{sgn}(p)\). Then the **complete nonzero rational homology representations** are

\[
H_0(X;\mathbb Q)\cong\mathbb Q,\qquad
H_1(X;\mathbb Q)\cong\bigwedge^2 V\oplus(\eta\otimes W)\oplus\varepsilon,\qquad
H_2(X;\mathbb Q)\cong V.
\]

All higher rational homology vanishes. The degree-one decomposition has constituent dimensions \(3+2+1=6\); the natural degree-two representation is irreducible of dimension \(3\). The full quotient has trivial positive-degree rational homology,

\[
\widetilde H_j(X/G;\mathbb Q)=0\quad\text{for all }j\geq0.
\]

For the rotation subgroup \(G^+=\ker(\varepsilon)\) of order \(24\), however, \(\dim_{\mathbb Q}H_1(X/G^+;\mathbb Q)=1\) and \(H_2(X/G^+;\mathbb Q)=0\). Thus the orientation-sensitive extra first-homology class survives rotational identification but not reflection identification.

## Assumptions and scope

The graph has eight vertices, twelve edges, girth four, and each vertex has degree three. The standard subdivision criterion for two particles applies: paths between distinct essential vertices contain at least one edge, and every essential closed path has at least three edges [1]. Its discretized unordered configuration complex \(D\) is therefore a deformation retract of \(X\). The inclusion \(D\hookrightarrow X\) is \(G\)-equivariant; since its induced homology maps are isomorphisms, the computed \(G\)-representations are the representations on \(X\), regardless of whether the retraction itself is equivariant.

The calculation is over \(\mathbb Q\). No claim is made about torsion in integral first homology, the fundamental group, or an integral \(G\)-lattice decomposition.

## Proof

Orient each cube edge \(e=(a,b)\) from smaller to larger binary integer. The compact two-particle cubical complex has \(28\) zero-cells \(\{u,v\}\) with \(u\ne v\), \(72\) one-cells \((e,v)\) for vertices \(v\) outside the endpoints of \(e\), and \(42\) two-cells \((e,f)\) for pairs of edges with disjoint closed supports. Orient two-cells by increasing lexicographic edge order. The boundaries, for \(e=(a,b)\) and \(f=(c,d)\), are

\[
\partial_1(e,v)=(b,v)-(a,v),\qquad
\partial_2(e,f)=(f,b)-(f,a)-(e,d)+(e,c).
\]

Thus the integer cellular chain complex is

\[
0\longrightarrow \mathbb Z^{42}\overset{\partial_2}{\longrightarrow}
\mathbb Z^{72}\overset{\partial_1}{\longrightarrow}
\mathbb Z^{28}\longrightarrow0.
\]

Exact row reduction gives \(\operatorname{rank}(\partial_1)=27\), \(\operatorname{rank}(\partial_2)=39\), and the matrix identity \(\partial_1\partial_2=0\). The rational Betti numbers are therefore \((1,6,3)\). Independent bit-vector reduction over \(\mathbb F_2\) gives the same two boundary ranks, a check on the cell signs and enumeration but not a complete integral torsion calculation.

Every \(g=(t,p)\in G\) maps cells to cells. Its action on an oriented edge acquires the sign of its endpoint order, and its action on a square also acquires the sign of any exchange of the two edge factors. The checker verifies compatibility with both cellular boundary maps for every one of the \(48\) elements. Since \(D\) has no three-cells, \(H_2(D;\mathbb Q)=\ker(\partial_2\otimes\mathbb Q)\) has dimension \(3\). An exact rational kernel basis is transformed under each group element; the resulting image is checked in all \(42\) chain coordinates. Its character coincides with \(\chi_V\) on every element, proving \(H_2\cong V\).

For degree one, apply the equivariant Euler--Poincaré identity to the same chain maps:

\[
\chi_{H_1}(g)=1+\chi_{H_2}(g)-\chi_{C_0}(g)+\chi_{C_1}(g)-\chi_{C_2}(g).
\]

For any signed coordinate permutation the right-hand side equals

\[
\chi_{\wedge^2 V}(g)+\eta(g)\chi_W(p)+\varepsilon(g).
\]

Exact equality was checked on all \(48\) elements, including the ten signed-cycle conjugacy classes below. Complete reducibility in characteristic zero then gives the stated degree-one isomorphism. The three terms are mutually inequivalent irreducibles: the restriction of \(\wedge^2 V\) to translations has three distinct weight-two characters, \(\eta\otimes W\) has translation character \(\eta\) and an irreducible two-dimensional \(S_3\)-part, and \(\varepsilon\) is one-dimensional.

In the table, \(\lambda^+\) and \(\lambda^-\) are partitions of the positive- and negative-signed cycle lengths of the signed permutation. Every element in a class has the displayed homology traces.

| \((\lambda^+,\lambda^-)\) | Class size | \(\chi_{H_1}\) | \(\chi_{H_2}\) |
|---|---:|---:|---:|
| \((\varnothing,(1,1,1))\) | 1 | 0 | -3 |
| \((\varnothing,(2,1))\) | 6 | 0 | -1 |
| \((\varnothing,(3))\) | 8 | 0 | 0 |
| \(((1),(1,1))\) | 3 | 2 | -1 |
| \(((1),(2))\) | 6 | 2 | 1 |
| \(((1,1),(1))\) | 3 | -4 | 1 |
| \(((1,1,1),\varnothing)\) | 1 | 6 | 3 |
| \(((2),(1))\) | 6 | 0 | -1 |
| \(((2,1),\varnothing)\) | 6 | -2 | 1 |
| \(((3),\varnothing)\) | 8 | 0 | 0 |

Averaging either character over all \(48\) elements gives zero. Averaging over the \(24\) elements with \(\varepsilon(g)=1\) gives dimensions \(1\) and \(0\) for degree one and degree two respectively. For any finite group acting cellularly on a finite CW complex, rational homology of its topological quotient agrees with the invariant rational homology of the original space (one can pass to a cellular subdivision and use the transfer/coinvariant argument). This gives both quotient statements.

## Verification

Run `python3 check_cube.py` in an environment with SymPy. The standalone script regenerates the graph, the complete cubical cell sets and integer boundary matrices, verifies \(\partial_1\partial_2=0\), computes exact rational ranks and a separate mod-two rank calculation, constructs an exact basis of degree-two cycles, verifies all \(48\) cellular symmetry actions commute with the boundaries, reconstructs every transformed cycle, checks the two character identities and computes both group averages. The expected final line is `CUBE_TWO_PARTICLE_FULL_B3_EQUIVARIANT_HOMOLOGY_OK`.

## Relationship to prior work

Prue and Scrimshaw's stable-equivalence theorem [1] supplies the bridge from the continuous configuration space to the finite cubical model. An and Maciazek [2] construct graph-braid presentations and prove a structural theorem for three-connected planar graphs, including the existence of one-particle and exchange moves. An, Drummond-Cole and Knudsen [3] develop general homology-computing chain methods for graph configurations. These works provide foundations and general tools but do not furnish the displayed \(48\)-element cube-specific character or its signed-coordinate irreducible decomposition.

Other recorded equivariant calculations concern two particles on the cuboctahedral and dodecahedral graphs; neither graph is \(Q_3\), and their stated modules cannot imply the present cube result by graph isomorphism or subgroup restriction. A 2026 study by Ramos and Yun [4] addresses stable representations for specified nested graph families including complete, complete-bipartite, crown and complete-tripartite graphs, not the three-cube automorphism action here. Those comparisons do not prove absolute bibliographic uniqueness.

## Limitations

The theorem specifies rational representations and quotient rational homology only, not integral homology torsion or quotient homotopy type. The group-invariant rational quotient calculation cannot detect finite torsion. Source searches and the inspected primary works cannot exclude mathematically equivalent unpublished or unindexed computations. The checker establishes a finite exact calculation; no claim about higher-dimensional cubes or configurations of more particles follows from it.

## References

[1] P. Prue and T. Scrimshaw, *Abrams's Stable Equivalence for Graph Braid Groups*, Topology and its Applications 178 (2014), 136–145; arXiv:0909.5511, especially Theorem 3.2. https://arxiv.org/abs/0909.5511

[2] B. H. An and T. Maciazek, *Geometric Presentations of Braid Groups for Particles on a Graph*, Communications in Mathematical Physics 384 (2021), 1109–1140; first arXiv version 27 June 2020, arXiv:2006.15256. https://arxiv.org/abs/2006.15256

[3] B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional Spaces and Graph Braid Groups*, Documenta Mathematica 24 (2019), 1513–1583; arXiv:1708.02351. https://arxiv.org/abs/1708.02351

[4] E. Ramos and C. H. Yun, *Computing Stable Homology Representations of Graph Configuration Spaces*, arXiv:2606.13813 (2026). https://arxiv.org/abs/2606.13813
