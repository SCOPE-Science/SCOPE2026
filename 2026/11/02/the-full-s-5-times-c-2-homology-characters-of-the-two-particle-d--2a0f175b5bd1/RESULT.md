# The full \(S_5\times C_2\) homology characters of the two-particle Desargues configuration space

## Finding
Let \(D\) be the twenty-vertex Desargues graph, realized as the inclusion graph between the two-element and three-element subsets of \(\{0,1,2,3,4\}\). Let \(X=\operatorname{UConf}_2(|D|)\) be the space of unordered pairs of distinct points on its geometric realization. The full automorphism group is \(G=S_5\times C_2\): the first factor permutes the five labels, and the central involution sends each subset to its complement. For a partition \(\lambda\vdash5\), write \(S^\lambda\) for the corresponding rational Specht representation, with subscript \(+\) or \(-\) indicating the central involution's eigenvalue.

The complete positive-degree rational homology representation is
\[
H_1(X;\mathbb Q)\cong S^{(3,1,1)}_+\oplus S^{(2,2,1)}_-,
\]
\[
\begin{aligned}
H_2(X;\mathbb Q)\cong{}&\bigl(S^{(3,1,1)}\oplus S^{(2,2,1)}\oplus S^{(2,1,1,1)}\bigr)_+\\
&\oplus\bigl(S^{(4,1)}\oplus S^{(3,2)}\oplus S^{(3,1,1)}\oplus S^{(2,2,1)}\bigr)_-.
\end{aligned}
\]
All higher homology vanishes. In particular, the Betti vector is \((1,11,35)\), and the integral second homology is free of rank \(35\). The central involution fixes \(6\) dimensions in degree one and \(15\) dimensions in degree two. Consequently the rational Betti vectors of the quotient spaces are \((1,6,15)\) for \(X/C_2\), and \((1,0,0)\) for both \(X/S_5\) and \(X/G\).

## Assumptions and scope
The graph has vertices \(A\subset\{0,1,2,3,4\}\) with \(|A|=2\) or \(3\), and one edge for every strict inclusion between such vertices. It has \(20\) vertices, \(30\) edges, girth \(6\), and no loops. The group acts by graph homeomorphisms; homology coefficients are rational unless explicitly stated otherwise. Unordered configurations exclude collisions everywhere, including vertices and open edges. The assertion concerns ordinary singular homology, not Borel–Moore homology or the one-point compactification. The central complement involution on the graph is not particle-label exchange.

## Proof
**Finite model.** For two particles the Abrams deleted-product cubical model has the homotopy type of \(X\): every essential-vertex-to-essential-vertex path has at least one edge, and every noncontractible embedded cycle has at least three edges. These conditions hold because \(D\) is simple and has girth \(6\). Its unordered cells are vertex pairs, disjoint vertex-edge pairs and unordered pairs of disjoint edges. The numbers of cells in dimensions zero, one and two are
\[
\left(\binom{20}{2},\;30(20-2),\;\binom{30}{2}-20\binom{3}{2}\right)=(190,540,375).
\]
Order vertices lexicographically by subset cardinality and then lexicographic labels, orient each edge from its smaller to its larger indexed endpoint, and orient each square by increasing ordered edge indices. For disjoint oriented edges \(e=[a,b]\) and \(f=[c,d]\), with \(e<f\), the integral cubical differential is
\[
\partial_2[e,f]=[b,f]-[a,f]-[d,e]+[c,e].
\]
The degree-one boundary sends \([v,e]\) to \([v,b]-[v,a]\). These formulas define integer matrices \(\partial_1\) of size \(190\times540\) and \(\partial_2\) of size \(540\times375\).

**Ranks and natural degree-one action.** The cubical one-skeleton is connected, so \(\operatorname{rank}\partial_1=189\). The sum-of-particle-positions cellular map to graph chains sends \([\{a,b\}]\) to \([a]+[b]\), \([v,e]\) to \([e]\), and every square to zero; it is equivariant and induces \(\pi_*:H_1(X;\mathbb Q)\to H_1(D;\mathbb Q)\). A breadth-first tree of \(D\) has eleven non-tree edges; their fundamental cycles have lengths ten or six (ten of length six and one of length ten), and each omits a graph vertex. Keeping a second particle at an omitted vertex while moving the first around each cycle gives eleven classes whose images are a fundamental cycle basis of the graph. Therefore \(\pi_*\) is onto, and \(\operatorname{rank}\partial_2\le 540-189-11=340\). Exact elimination over \(\mathbb F_3\) of the specified complete \(540\times375\) matrix has rank \(340\). An integer minor nonzero modulo three is nonzero over \(\mathbb Q\), so the rational rank is at least \(340\), and hence exactly \(340\). Thus \(\dim H_1(X;\mathbb Q)=11\) and \(\dim H_2(X;\mathbb Q)=35\). The map \(\pi_*\) is an equivariant isomorphism over \(\mathbb Q\). Since \(C_3=0\), \(H_2(X;\mathbb Z)=\ker\partial_2\) is a free subgroup of \(\mathbb Z^{375}\), of rank \(35\).

**Characters.** On graph homology the natural action has character
\[
\chi_{H_1(D)}(g)=1-\operatorname{tr}(g\mid C_0(D))+\operatorname{tr}(g\mid C_1(D)).
\]
The first-homology character of \(X\) is the same. Signed cell permutations determine the character of the second homology via
\[
\chi_{H_2(X)}(g)=\operatorname{tr}(g\mid C_0(X))-\operatorname{tr}(g\mid C_1(X))+\operatorname{tr}(g\mid C_2(X))-1+\chi_{H_1(D)}(g).
\]
For \(g=(\sigma,\delta)\in S_5\times C_2\), the complete computed pairs \((\chi_{H_1},\chi_{H_2})\), with the usual cycle-type notation for \(\sigma\), are:

| Cycle type | Central \(+\) | Central \(-\) |
|---|---|---|
| \((1^5)\) | \((11,35)\) | \((1,-5)\) |
| \((2,1^3)\) | \((-1,-1)\) | \((1,-5)\) |
| \((2^2,1)\) | \((-1,-1)\) | \((-3,-1)\) |
| \((3,1^2)\) | \((-1,-1)\) | \((1,1)\) |
| \((3,2)\) | \((-1,-1)\) | \((1,1)\) |
| \((4,1)\) | \((1,1)\) | \((-1,1)\) |
| \((5)\) | \((1,0)\) | \((1,0)\) |

In this table “central \(+\)” means \(\delta\) is the identity and “central \(-\)” means \(\delta\) is the complement involution, not the eigenvalue labels on irreducible summands. Each of the \(240\) cellular actions preserves the cubical differential, including the orientation sign of any swapped pair of edges. The \(S_5\) character table, obtained by the Murnaghan–Nakayama rim-hook rule, and the orthogonality formula give exactly the displayed Specht decompositions, with multiplicity one for each listed constituent in each central eigenspace.

**Quotients.** For a finite cellular group action and rational coefficients, the homology of the orbit space is the invariant part of homology. The identity and central involution have characters \((11,35)\) and \((1,-5)\), giving central invariant dimensions \((6,15)\). Character averages over \(S_5\) give zero in both positive degrees; hence so does the full group. The indicated quotient Betti vectors follow.

## Verification
Run `python3 CHECK.py` from the directory containing the supplied checker. It reconstructs all cellular bases and boundary formulas from subset incidence, confirms one-skeleton connectivity and the eleven parked-particle cycle generators, obtains the exact rank certificate modulo three, checks cubical boundary equivariance under all \(240\) group elements, computes the fourteen conjugacy-class traces, calculates the rational Specht multiplicities by the rim-hook rule, and verifies the three quotient Betti vectors. Its final success line is `DESARGUES_B2_FULL_S5_C2_SPECHT_CHECKS_OK`. The calculation over \(\mathbb F_3\) proves the required rational rank only in combination with the separate upper bound supplied above; it is not an integral Smith-normal-form classification.

## Relationship to prior work
An, Drummond-Cole and Knudsen (arXiv:1708.02351, especially their first-homology appendix) develop a general graph-configuration chain model and review the triconnected-graph first-homology calculation. An and Knudsen (arXiv:2008.10371) treat second-homology generators for planar graph braid groups and explicitly identify limitations for nonplanar graphs. Farber and Hanbury (arXiv:1005.2300) analyze **ordered** two-particle configurations and mature graph formulas, not the full rational automorphism character of the **unordered** Desargues space. Bibby, Chan, Gadish and Yun (arXiv:2109.03302) treat one-point-compactified ordered configurations in a different moduli-space setting. None of these inspected sources states or implies the seven displayed Desargues Specht constituents with their central parity. The conclusion is an exact equivariant refinement for a canonical nonplanar cubic incidence graph, not a new general formula for every graph.

## Limitations
The result does not classify the full integral first-homology lattice or its torsion, integral equivariant extension classes, the homotopy type of the space, or higher-particle configurations. It concerns the explicitly defined graph and finite group. An equivalent unpublished or unindexed representation computation cannot be ruled out. Finite computations have been supplied in full as an executable certificate, but no independent external audit is asserted.

## References
1. B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351 (first public 2017-08-08), https://arxiv.org/abs/1708.02351.
2. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (2020), https://arxiv.org/abs/2008.10371.
3. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (2010), https://arxiv.org/abs/1005.2300.
4. C. Bibby, M. Chan, N. Gadish and C. H. Yun, *Homology representations of compactified configurations on graphs applied to \(\mathcal M_{2,n}\)*, arXiv:2109.03302 (2021), https://arxiv.org/abs/2109.03302.
5. S. Schmidt, *On the quantum symmetry of distance-transitive graphs*, *Advances in Mathematics* **368** (2020), 107150, https://doi.org/10.1016/j.aim.2020.107150 (automorphism-group table).
