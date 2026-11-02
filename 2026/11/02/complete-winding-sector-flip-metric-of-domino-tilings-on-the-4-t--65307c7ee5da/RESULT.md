# Complete winding-sector flip metric of domino tilings on the \(4\times6\) torus

## Finding

Let \(G=C_4\square C_6\) be the 24-vertex, 48-edge graph with cell labels \((r,c)\in\mathbb Z/4\mathbb Z\times\mathbb Z/6\mathbb Z\) and the standard cellular embedding in the torus. A configuration is a perfect matching of \(G\): twelve unordered adjacent-cell pairs covering every cell exactly once. A move exchanges two parallel dominoes covering the corners of one **elementary embedded square** with the other parallel pair. All 24 faces, including seam-crossing faces, are allowed, and no nonfacial cycle exchanges are allowed.

For this specifically defined graph \(\mathcal F\), exhaustive exact finite enumeration proves there are **3,108 configurations, 9,048 edges, and 15 connected components**. Each component consists of precisely the matchings with one fixed integral signed seam-flux vector, and every nonempty flux class is connected. The multiset of component orders is
\[
(1456,576,576,152,152,48,48,24,24,24,24,1,1,1,1).
\]
The four order-24 components are cycles, and four configurations are isolated. The largest component is the zero-flux sector: its radius is \(12\), its diameter is \(20\), and its Wiener index (sum over unordered pairs) is \(8{,}146{,}752\). For each of the two sectors of flux \((0,\pm1)\), the radius is \(12\), the diameter is \(16\), and the Wiener index is \(1{,}238{,}340\). Summing Wiener indices of all components gives \(10{,}795{,}608\); pairs in distinct components are deliberately not assigned finite distances.

The exact size/edge/radius/diameter/Wiener profile, in increasing lexicographic order of signed flux, is:

| Flux \((h,v)\) | Tilings | Flip edges | Radius | Diameter | Wiener index |
|---|---:|---:|---:|---:|---:|
| \((-2,0)\) | 1 | 0 | 0 | 0 | 0 |
| \((-1,-1)\) | 24 | 24 | 12 | 12 | 1,728 |
| \((-1,0)\) | 152 | 312 | 12 | 12 | 75,600 |
| \((-1,1)\) | 24 | 24 | 12 | 12 | 1,728 |
| \((0,-3)\) | 1 | 0 | 0 | 0 | 0 |
| \((0,-2)\) | 48 | 72 | 12 | 12 | 7,032 |
| \((0,-1)\) | 576 | 1,608 | 12 | 16 | 1,238,340 |
| \((0,0)\) | 1,456 | 4,968 | 12 | 20 | 8,146,752 |
| \((0,1)\) | 576 | 1,608 | 12 | 16 | 1,238,340 |
| \((0,2)\) | 48 | 72 | 12 | 12 | 7,032 |
| \((0,3)\) | 1 | 0 | 0 | 0 | 0 |
| \((1,-1)\) | 24 | 24 | 12 | 12 | 1,728 |
| \((1,0)\) | 152 | 312 | 12 | 12 | 75,600 |
| \((1,1)\) | 24 | 24 | 12 | 12 | 1,728 |
| \((2,0)\) | 1 | 0 | 0 | 0 | 0 |

The accompanying `sector_metrics.json` gives, for each flux, complete exact degree, eccentricity and ordered-pair shortest-path distance histograms, not only the displayed extremes.

## Assumptions and scope

Every cell has its four distinct coordinate neighbors modulo \(4\) and modulo \(6\), so there are 48 undirected possible dominoes. The face indexed by \((r,c)\) has corners \((r,c),(r,c+1),(r+1,c),(r+1,c+1)\), where coordinates are reduced cyclically. A legal flip uses that face alone; it replaces the pair of horizontal occupied edges with the pair of vertical edges, or conversely.

Signed flux is specified unambiguously as follows. Let \(M\) be a matching, \(M_H(r)\) the indicator that \(M\) contains the horizontal seam domino joining \((r,5)\) to \((r,0)\), and \(M_V(c)\) the indicator for the vertical seam domino joining \((3,c)\) to \((0,c)\). Define
\[
h(M)=\sum_{r=0}^3(-1)^{r+5}M_H(r),\qquad
v(M)=\sum_{c=0}^5(-1)^{3+c}M_V(c).
\]
These fluxes are relative to the fixed horizontal matching \((r,0)(r,1),(r,2)(r,3),(r,4)(r,5)\) in each row; that reference has flux \((0,0)\). A flip changes two opposite seam contributions with opposite signs or changes neither, so flux is invariant under every move. The enumeration shows, specifically for this small torus, the converse: two tilings have the same flux if and only if a sequence of flips connects them. There is no assertion that this equivalence holds for all toroidal grids.

## Proof

The assertion is finite and admits a complete exhaustive proof with two stand-alone constructive enumeration certificates, `verify_primary.py` and `verify_alt.cpp`. The main critical steps are explicit and independently implemented, rather than inferred from sampled cases.

**Exhaustive domain.** The Python program builds the graph's 48 edges from the cyclic-neighbor rule, then recursively chooses the least-index uncovered vertex \(u\) and branches over every uncovered neighbor \(v\), adding the edge \(uv\). Every perfect matching has exactly one partner for \(u\); hence induction on the number of uncovered vertices proves the recursion covers every perfect matching once. This yields precisely 3,108 distinct 12-edge masks. The C++17 program independently bipartitions the 24 cells into 12 black and 12 white cells, recursively chooses a distinct white neighbor for each black cell, and obtains the same 3,108 perfect matchings. This second scheme does not reuse the first recursion or matching encoding.

**Exactly the permitted moves.** The Python program constructs all 24 labeled faces and the horizontal and vertical edge-pair masks on each. It inspects every state-face pair, replacing one occupied pair with the other if possible, and checks that the output is another enumerated matching. It removes duplicate neighbors and checks edge reversibility. The C++17 implementation instead computes the two black and two white corners of each face and swaps their matched white partners precisely when both matching edges lie in the face. These conditions are necessary and sufficient for the defined face flip; thus no legal adjacency is omitted or spurious adjacency added. Both produce 9,048 undirected flip edges.

**Every component, shortest path and flux.** On the resulting finite graph, each program finds all components by graph traversal. For each vertex of each component it performs a separate breadth-first search. In an unweighted graph breadth-first search returns the shortest-path distance exactly, and the traversal explicitly checks that each search reaches the whole component. For each component the scripts tabulate the distance multiset, eccentricities, radius, diameter, vertex degrees, and \(\frac12\sum_{x,y}d(x,y)\) over all ordered pairs in the component, obtaining the table above. The checks verify that each connected component has one flux, that the 15 flux pairs are distinct, and that the two independently generated distance histograms agree in **all 163 sector-distance bins**. Consequently one component occurs for each of the 15 nonempty flux classes, with no extra component of the same flux.

**Accounting identities.** The component orders sum to \(3108\); the component edge counts sum to \(9048\); and each sector's ordered-distance histogram sums to its order squared. The aggregate ordered reachable-pair count is \(2{,}836{,}612\), so unreachable pairs are excluded from the componentwise Wiener sum. The exact Wiener sum is \(10{,}795{,}608\). Each size-24 component is connected and has vertex degree two throughout, as confirmed by the full degree distributions; hence each is a single 24-cycle.

## Verification

Run `python3 verify_primary.py` and compile/run `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt`. No external Python packages or network access are required. Both programs reconstruct the entire graph from cell adjacency and faces; they do not read cached adjacency or shortest-path data. The Python program prints complete JSON statistics followed by `PRIMARY_CERTIFICATE_OK`. The compiled program prints full component distance statistics followed by `ALTERNATIVE_CERTIFICATE_OK`. Their per-sector values have also been compared independently field-by-field with the included `sector_metrics.json`; all 15 sectors and all 163 nonzero ordered-distance bins agreed. The JSON file is an output reference, **not** an input to either verifier.

This verification is a finite exhaustive proof: it does not establish analogous numerical statements on a \(4\times8\) or larger torus. Source-code correctness and reproducibility remain subject to independent review.

## Relationship to prior work

The domino-flip graph on a quadriculated surface, component criteria, general height-based distance formulas and construction of geodesics are classical; see Saldanha–Tomei–Casarin–Romualdo (1995). In particular, the invariant and the general existence of distance methods are **not** claimed as new. Kiwi–Loebl (first public version 2014) study toroidal-grid matching types and their mod-two homology rather than this complete face-flip metric. Liu–Zhang–Zhang (first public version 2023) study connected-component bounds and structure for quadriculated tori, including specific results for the \(4\times4\) case and general bipartite-torus bounds. Their \(4\times4\) numerical analysis is not part of this claim.

The present narrowly scoped contribution is the **full explicit flux-resolved degree, eccentricity and all-pairs distance census for the 24-cell \(4\times6\) torus**. The classical structural theorems do not themselves list these 15 complete numerical metric profiles. A general distance theorem may permit deriving any particular pairwise distance once the two tilings are supplied, but the full component-by-component distribution requires additional exact finite enumeration or a new counting argument. No assertion of a new general distance formula is made.

## Limitations

This is an exact finite computation for one natural anisotropic torus. It does not prove a general family theorem, a first-occurrence threshold, an asymptotic law or mixing-time bounds. A complete independent audit has not occurred; residual originality risk includes an unnoticed equivalent table in older or unindexed toroidal-dimer literature. A general theoretical formula for distances exists in prior work, so the claim is limited to the explicit complete quantitative census, not discovery of the reconfiguration metric itself. The graph is disconnected; the reported sum of Wiener indices intentionally omits pairs in different components.

## References

1. N. C. Saldanha, C. Tomei, M. A. Casarin Jr., D. Romualdo, "Spaces of domino tilings," *Discrete & Computational Geometry* **14** (1995), 207–233. DOI: 10.1007/BF02570703. Original journal appearance: 1995-09-01. `https://doi.org/10.1007/BF02570703`.
2. M. Kiwi and M. Loebl, "Types of perfect matchings in toroidal square grids," arXiv:1406.3317, first public 2014-06-12. `https://arxiv.org/abs/1406.3317`.
3. Q. Liu, Y. Zhang, H. Zhang, "Components of domino tilings under flips in quadriculated tori," arXiv:2307.08332, first public 2023-07-17; *Discrete Mathematics* **348** (2025), article 114396. `https://arxiv.org/abs/2307.08332`.
