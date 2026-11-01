# Complete integral graph-metric Rips persistence of the truncated cube

## Finding
Let \(T\) be the graph of the truncated cube, with the explicit vertex and edge description below. Equip its 24 vertices with their shortest-path distance and use **inclusive** Vietoris–Rips complexes \(K_r=\operatorname{VR}_{\le r}(V(T))\) at real thresholds \(r\geq0\). The complete **reduced integral persistent homology**, as an interval-decomposable persistence module over \(\mathbb Z\), has exactly these nonzero intervals:

| Degree | Interval | Multiplicity |
| --- | --- | ---: |
| \(0\) | \([0,1)\) | 23 |
| \(1\) | \([1,3)\) | 5 |
| \(2\) | \([3,4)\) | 1 |
| \(3\) | \([3,4)\) | 6 |
| \(3\) | \([4,5)\) | 1 |
| \(5\) | \([4,5)\) | 2 |
| \(11\) | \([5,6)\) | 1 |

All reduced integral homology groups at every scale are free abelian. In particular, the **new scale-four result** is
\[
\widetilde H_k(K_4;\mathbb Z)\cong
\begin{cases}\mathbb Z,&k=3,\\\mathbb Z^2,&k=5,\\0,&\text{otherwise},\end{cases}
\]
and the inclusion \(K_3\hookrightarrow K_4\) induces the **zero homomorphism in every positive degree**. Thus the third-dimensional generator at scale four is born there; none of the six third-dimensional generators at scale three survives. The scale-three homotopy type and the general antipodal last-stage mechanism were previously known; they are not claimed as discoveries here.

## Assumptions and scope
Represent a vertex of \(T\) as \((x,i)\), where \(x\in\{0,1\}^3\) and \(i\in\{0,1,2\}\). Join \((x,i)\) to \((x,j)\) for \(i\ne j\), and join \((x,i)\) to \((x\oplus e_i,i)\), where \(e_i\) is the unit bit vector. Thus the three half-edges at each vertex of the ordinary cube form one triangle; the remaining 12 edges join corresponding half-edges of original cube edges. This yields the 24-vertex, 36-edge, 3-regular truncated-cube graph, also known as the order-three cube-connected-cycle graph. Each graph edge has length one. No Euclidean intervertex distances are used.

For \(r\in[k,k+1)\), with integer \(k\geq0\), \(K_r=K_k\). The graph diameter is exactly six. All assertions concern unreduced simplicial chains for computing the reduced homology, and standard integral incidence signs obtained by sorting vertices \(3x+i\).

## Proof
**1. Finite simplicial models.** For every integer \(r\), form the distance-power graph joining exactly the pairs whose graph distance is at most \(r\). Its clique complex is \(K_r\). The breadth-first distance matrix and exhaustive maximal-clique/subface enumeration in the accompanying standalone verifier give these exact face vectors (dimensions increase from left to right):

| Scale | Face vector |
| --- | --- |
| \(1\) | \((24,36,8)\) |
| \(2\) | \((24,84,80,24)\) |
| \(3\) | \((24,156,376,372,144,20)\) |
| \(4\) | \((24,228,1112,3060,5016,5108,3288,1302,280,24)\) |

These lists include every face, not just maximal ones. At scale zero there are 24 isolated vertices.

**2. Exact integral chain contractions.** Give the simplex represented by a nonzero 24-bit mask \(f\) the orientation specified by increasing vertex index; its boundary is the alternating sum of masks obtained by deleting one bit. A free face \(s\) with its unique immediate coface \(t\) gives an elementary simplicial collapse; the executable verifier deterministically takes all available such pairs, preferring larger face dimension. On the residual integral cellular chain complex, it repeatedly cancels an incident unit coefficient \(a=[\partial t:s]=\pm1\). Specifically, for any other column \(u\) containing \(s\) with coefficient \(b\), replace \(\partial u\) by \(\partial u-ba^{-1}\partial t\), then delete \(s,t\) and their incident rows/columns. Choosing a unit minimizes the product of the remaining row and column degrees. This is elementary integral chain contraction: it uses only unimodular basis changes and preserves integral homology. The procedure checks the zero composition of successive boundary maps afterwards.

| Scale | Elementary collapses | Further unit chain cancellations | Final cellular generators |
| --- | ---: | ---: | --- |
| \(1\) | 8 | 23 | one in degree 0, five in degree 1 |
| \(2\) | 89 | 14 | one in degree 0, five in degree 1 |
| \(3\) | 266 | 276 | one in degree 0, one in degree 2, six in degree 3 |
| \(4\) | 8881 | 838 | one in degree 0, one in degree 3, two in degree 5 |

All surviving differentials are identically zero, in exact integer arithmetic. The number of original faces equals twice the total canceled pairs plus the number of final generators in each row. Since every cancellation is over \(\mathbb Z\), this proves the displayed **integral**, not merely characteristic-two, homology groups. This chain argument does not assert homotopy equivalences or null-homotopy of attaching maps.

**3. Integral persistence maps.** For a canceled unit pair \((s,t)\), let \(a=[\partial t:s]=\pm1\). The chain projection sends \(t\) to zero, sends \(s\) to \(-a^{-1}(\partial t-a s)\), and fixes other basis elements. Its chain-homotopy inverse inclusion fixes the unaffected lower basis elements and sends another same-degree column \(u\) to \(u-a^{-1}[\partial u:s]t\). The verifier records every such step, lifts each final critical cycle to the original chains, applies the ordinary filtration inclusion, and projects onto the target's critical integral chains. Every lifted chain has zero original simplicial boundary.

In the displayed deterministic critical bases, the nontrivial degree-one inclusion matrix from \(K_1\) to \(K_2\) is
\[
\begin{pmatrix}
0&0&1&0&0\\-1&0&0&0&0\\1&0&0&-1&1\\0&0&0&0&1\\-1&-1&0&0&-1
\end{pmatrix},
\]
whose determinant is \(-1\). Hence it is an isomorphism over \(\mathbb Z\). The degree-three inclusion matrix from \(K_3\) to \(K_4\) is the zero \(1\)-by-\(6\) matrix, **over \(\mathbb Z\)**. All other positive-degree maps between consecutive stages vanish because either the source or target group is zero. This establishes the interval splitting of all stages up to scale four, including the distinction between a dying six-dimensional class space and a newly born one-dimensional class at scale four.

**4. Last two stages.** A distance calculation shows that the unique vertex at graph distance six from \((x,i)\) is \((x\oplus(1,1,1),i)\). Thus precisely twelve disjoint vertex pairs are excluded as edges at scale five, while all other pairs are edges. Therefore
\[
K_5\cong\underbrace{S^0*\cdots*S^0}_{12\text{ factors}}\cong S^{11}.
\]
At scale six, every vertex subset is a simplex, so \(K_6\) is contractible. Inclusions \(K_4\to K_5\to K_6\) therefore induce zero maps on reduced homology. Together with the standard connectivity map \(K_0\to K_1\), the earlier chain contractions and inclusion computations prove all the intervals in the Finding.

## Verification
Run `python3 verify_truncated_cube_persistence.py` using Python 3.10 or later; no third-party library is required. It constructs the graph from its bit-index definition, checks all 24 breadth-first distance rows, enumerates every face at scales one through four, executes all free-face collapses and signed integral unit cancellations, checks the remaining boundary compositions, constructs representative integral cycles and both consecutive nontrivial inclusion maps, and confirms the degree-one determinant \(-1\). An algorithmically separate binary persistent-boundary reduction over \(\mathbb F_2\) independently reproduces the intervals through scale four; this cross-check is supplementary and is **not** substituted for the integral proof. The terminal output is `TRUNCATED_CUBE_INTEGRAL_PERSISTENCE_VERIFIED`. `verification_output.txt` records the actual run.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* (arXiv:1104.0433, first public 2011-04-03) identifies graph-distance Vietoris–Rips complexes with clique complexes of graph powers and studies general behavior, but does not determine the truncated cube's scale-four homology or persistence maps. Saleh, Titz Mite, and Witzel, *Vietoris–Rips complexes of Platonic solids* (arXiv:2302.14388, first public 2023-02-28), classify Platonic rather than Archimedean solids. Their general antipodal terminal-stage lemma is consistent with—and substantially anticipates—the scale-five sphere here. The previously published *A mixed-dimensional Rips wedge for the truncated cube* identifies \(K_3\simeq S^2\vee\bigvee^6 S^3\); it explicitly does **not** establish the full filtration or its inclusion homomorphisms. The present contribution is therefore the integral scale-four calculation and complete **integral persistence maps**, not the known scale-three wedge or an uncredited rederivation of the antipodal argument.

## Limitations
This is an exact finite result for the vertex graph of the truncated cube in the shortest-path metric. No classification of homotopy types for \(K_4\), integral cohomology rings, or equivariant symmetry representations is asserted. The chain reductions alone do not determine higher attaching maps. Nothing is claimed for Euclidean distances or higher-dimensional cube-connected-cycle graphs. Although source searches checked the same graph, all scales, graph powers, and the closely related truncated-octahedral graph, an unindexed equivalent computation remains possible. Independently audited mathematical validation has not been performed.

## References
1. Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first public 2011-04-03), *Israel Journal of Mathematics* **196** (2013), 295–319.
2. Nada Saleh, Thomas Titz Mite, Stefan Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (first public 2023-02-28), *Innovations in Incidence Geometry* **21** (2024), 17–34.
3. *A mixed-dimensional Rips wedge for the truncated cube*, publicly released mathematical record (2026), identifier `4fae71a21a80`.
