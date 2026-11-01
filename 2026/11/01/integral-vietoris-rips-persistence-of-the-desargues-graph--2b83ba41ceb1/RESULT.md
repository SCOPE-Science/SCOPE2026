# Integral Vietoris–Rips persistence of the Desargues graph

## Finding

Let \(G=\operatorname{GP}(10,3)\) be the twenty-vertex Desargues graph, and let \(K_r=\operatorname{VR}_{\leq r}(V(G),d_G)\) be its **inclusive**, vertex-set Vietoris–Rips complex with intrinsic shortest-path metric. Its **complete homotopy filtration** is

\[
K_r\simeq
\begin{cases}
\bigvee^{19} S^0,&0\le r<1,\\
\bigvee^{11} S^1,&1\le r<2,\\
\bigvee^{19} S^2,&2\le r<3,\\
S^3,&3\le r<4,\\
S^9,&4\le r<5,\\
\ast,&r\ge5.
\end{cases}
\]

In particular, the **entire reduced integral persistence barcode**, including its endpoint convention, is: nineteen degree-zero intervals \([0,1)\); eleven degree-one intervals \([1,2)\); nineteen degree-two intervals \([2,3)\); one degree-three interval \([3,4)\); and one degree-nine interval \([4,5)\). There are no other bars and no torsion. Each displayed homotopy equivalence is nonequivariant and applies to every real \(r\) in its stated range.

The distinctive phenomenon is the progression of noncontractible stages \(\bigvee^{19}S^2\), \(S^3\), and \(S^9\) at three consecutive integer thresholds. The claim is not a classification of arbitrary generalized Petersen graphs or of the continuously realized metric graph.

## Assumptions and scope

Write \(u_i=i\) and \(v_i=10+i\) for \(0\le i<10\). Indices in the edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\) are reduced modulo ten, and these thirty undirected edges define \(G\), also known as the Desargues–Levi graph or bipartite Kneser graph \(H(5,2)\). The metric \(d_G\) is the integer-valued shortest-path distance between the **twenty graph vertices only**. A finite set of these vertices is a simplex of \(K_r\) if and only if all its pairwise distances are at most \(r\). This is the graph-power flag complex \(\operatorname{Cl}(G^{\lfloor r\rfloor})\) for \(r\ge0\), including equality at each integer threshold.

The complete unordered-pair distance distribution is \(30,60,60,30,10\) for distances \(1,2,3,4,5\), respectively, and the graph has diameter five. This fixes all critical filtration thresholds. For clarity, a wedge of zero-spheres is the disjoint union of twenty points with a common chosen basepoint, and \(\ast\) denotes a contractible complex.

## Proof

**(1) Distance and face reconstruction.** Apply breadth-first search from each of the twenty explicitly enumerated vertices. The distance distribution is as stated above. For each integer scale \(t\), form the flag complex on the pairs at distance at most \(t\). Exhaustive recursion over increasing vertex labels creates every nonempty clique exactly once. At threshold two the full face vector in dimensions zero through three is
\[
(20,90,120,30),\qquad\#\{\text{nonempty faces}\}=260.
\]
At threshold three the full face vector in dimensions zero through six is
\[
(20,150,540,1000,960,450,80),\qquad\#\{\text{nonempty faces}\}=3200.
\]
The source code `verify.py` independently regenerates both sets. These are finite exhaustive counts, not sampled computations.

**(2) Integral homotopy at threshold two.** The file `certificates/r2_steps.json` contains an explicit sequence of operations on the actual set of 260 nonempty simplices. A step encoded by `[0,f,g]` deletes the face \(f\) and its unique larger coface \(g\), where the two vertex sets are represented by 20-bit masks and \(|g|=|f|+1\). This is an elementary free-face collapse in the then-current complex. A step `[1,g]` removes a maximal simplex \(g\), recording it as a critical cell. The certificate contains exactly **120 matched free-face pairs**, one critical vertex, and nineteen critical two-simplices; all 260 faces occur exactly once. The checker tests the unique coface condition against the **entire active face set at each step**, not just immediate incidences. It also constructs the full original face-poset Hasse diagram, reverses its matched incidences, and verifies by complete topological sorting that all 260 faces are processed with no directed cycle. Thus it gives an acyclic Forman matching with precisely these critical cells. Forman's discrete Morse theorem provides a CW complex with one zero-cell, no one-cells, and nineteen two-cells. Every two-cell attaches to a point, so
\[
K_2\simeq\bigvee^{19}S^2.
\]
This is an integral homotopy conclusion, not an inference from finite-field Betti numbers.

**(3) Integral homotopy at threshold three.** The analogous `certificates/r3_steps.json` is independently verified against all 3,200 faces. It contains exactly **1,599 matched free-face pairs**, one critical vertex, and one critical three-simplex. A full directed-Hasse-graph topological sort likewise proves acyclicity. The resulting Morse CW model has one zero-cell and one three-cell and no cells of positive dimensions one or two. Therefore
\[
K_3\simeq S^3.
\]
In particular no hidden attaching map or integral torsion can occur.

**(4) Earlier and later stages.** For \(0\le r<1\), the twenty isolated vertices have reduced homotopy type \(\bigvee^{19}S^0\). At scale one, the triangle-free connected cubic graph has twenty vertices and thirty edges, hence cycle rank \(30-20+1=11\), giving \(K_1\simeq\bigvee^{11}S^1\). At scale four, the only missing edges in the distance-power graph are ten disjoint antipodal pairs \(\{u_i,u_{i+5}\}\) for \(0\le i<5\) and \(\{v_i,v_{i+5}\}\) for \(0\le i<5\). Every clique chooses at most one vertex from each opposite pair, and all such choices are allowed. The clique complex is therefore **literally** the join of ten two-point discrete spaces, which is the boundary of the ten-dimensional crosspolytope, homeomorphic to \(S^9\). At scale five, every distance is at most five, so \(K_5\) is the full nineteen-simplex and is contractible.

**(5) Integral persistence.** All the complexes are constant between consecutive integer thresholds. The homotopy types above imply that each nonzero reduced integral homology group occurs in a single filtration stage and in a dimension not represented by either adjacent stage. Consequently every connecting inclusion map between consecutive stages vanishes in every reduced homological degree. Every cyclic integral summand appears at the left endpoint and vanishes exactly at the right endpoint listed in the finding. There are no extension questions between degree-preserving nonzero groups, and all homology groups are free abelian. This proves the integral barcode over the indexing real parameter.

## Verification

Run the following command from the directory containing the extracted files, with Python 3.9 or later and only its standard library:

```text
python3 verify.py
```

The checker reconstructs every vertex, graph edge, shortest-path distance, and Rips face; checks the complete face counts and each supplied free-face certificate; verifies no acyclic-gradient directed cycle exists by topologically sorting every incidence in the complete Hasse diagram; and independently calculates all mod-two boundary ranks as a cross-check. It tests the ten forbidden pairs at distance five and the graph diameter. Successful execution ends in `VERIFY_OK`. A contemporaneous run is preserved in `verification_output.txt`, but the proof rests on the self-contained checker and certificates, not that log alone. Any modification of a certificate invalidating a freeness, coverage, or acyclicity condition is rejected.

## Relationship to prior work

Adamaszek's *Clique complexes and graph powers* [1] explicitly identifies graph-power clique complexes with intrinsic graph Vietoris–Rips complexes, gives the classic one-hexagon and high-girth results, and classifies cyclic graph powers. In particular, its collapse statements requiring girth at least seven, or absence of six-cycles, do not apply here: the Desargues graph has girth six and contains twenty six-cycles, each graph edge belonging to four. Its graph-square homotopy is therefore not determined by the high-girth theorem. The graph-power persistence study by Parks and Marchette [2] directly defines the same Rips graph-power filtration and develops general persistence and girth bounds, but Theorem 5.3 requires girth at least ten and no theorem in its inspected text determines the Desargues graph phases. The 2021 hypercube-graph Vietoris–Rips study [3] addresses full hypercubes, not this twenty-vertex cubic graph.

Two nearby published computations must be distinguished precisely. The *Scale-three Čech nerve of the Desargues graph* [4] computes a wedge of forty-nine two-spheres for a ball-intersection Čech nerve, not the clique complex of distance-bounded graph-vertex pairs; its full proof and face construction were inspected. The *hexagon-packing classification of scale-two graph Rips complexes* [5] assumes that distinct six-cycles share no graph edge; the present graph violates that hypothesis, since every edge lies on four hexagons. Thus neither theorem implies the claimed Rips stages. Other available Desargues independence, matching and cut complex results concern different simplex families. A published calculation of the separate Möbius–Kantor graph concerns a different graph and does not give this filtration. Searches included the alternative Desargues–Levi, bipartite Kneser, and \(H(5,2)\) names, as well as direct graph-power and barcode formulations. They identified no result covering all of the present homotopy stages and integral persistence maps.

## Limitations

This is a specific, finite, nonequivariant homotopy classification of the twenty vertices in the intrinsic graph metric. It does not describe the Rips complexes of the geometric realization with edge-interior points, Euclidean embeddings, subgroup-equivariant homotopy, or any general family of \(\operatorname{GP}(n,k)\). Integer-homology persistence is established, but no preferred geometric cycle bases or equivariant lattice representations are asserted. The exhaustive computation is fully reproducible with the embedded certificate and checker; independent mathematical review has not been performed. An equivalent calculation absent from searched catalogues and literature remains a priority risk.

## References

1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first posted 2011-04-03 (v1). Full-text comparison used the open arXiv HTML version: https://arxiv.org/html/1104.0433v3 ; dated source: https://arxiv.org/abs/1104.0433 .
2. A. D. Parks and D. J. Marchette, *Persistent homology in graph power filtrations*, Royal Society Open Science 3 (2016), 160228, DOI:10.1098/rsos.160228. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC5098965/ .
3. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (2021). https://arxiv.org/abs/2103.01040 .
4. *Scale-three Čech nerve of the Desargues graph is a wedge of 49 two-spheres*, public mathematical research record: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-scale-three-ech-nerve-of-the-desargues-graph-is-a-wedge-of-49-tw--eac77c714390 .
5. *A hexagon-packing classification of scale-two graph Rips complexes*, public mathematical research record: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-hexagon-packing-classification-of-scale-two-graph-rips-complex--70b9bc9b3abb .
