# A sphere-wedge homotopy classification for the nine-rung higher-independence complex

## Finding

The two-independence complex of the nine-rung ladder has the integral homotopy type
\[
\operatorname{Ind}_2(P_9\square K_2)\simeq S^5\vee\bigvee^4 S^7.
\]
This is strictly stronger than the previously published integral homology calculation for this complex: it determines all attaching maps that could carry nontrivial order-two Hopf classes.

## Assumptions and scope

Let the ladder have vertices \(\{0,\dots,17\}\). The first rail is \(0,\dots,8\); the second is \(9,\dots,17\). Edges join consecutive vertices along a rail and join \(i\) to \(i+9\) for \(0\le i\le8\). A face is a vertex subset for which the induced subgraph has maximum degree at most one (equivalently, all connected components have size at most two). The empty face is understood conventionally but not counted among nonempty simplices.

## Proof

**Step 1: finite acyclic Morse model.** Represent a nonempty face by its eighteen-bit vertex mask. Independently applying (a) the induced-degree condition and (b) a three-consecutive-column constraint gives exactly \(22,692\) nonempty faces. Process the vertices in order `10,14,9,5,17,2,4,11,6,16,12,13,3,0,1,15,8,7`. At each pivot, among as-yet-unmatched faces match \(\sigma\) with \(\sigma\cup\{v\}\) whenever both remain. The resulting \(11,343\) disjoint face/coface pairs leave exactly five critical cells: one vertex, the degree-five simplex with mask `74386`, and degree-seven simplices with masks `37291`, `37801`, `69995`, `70505`. An exhaustive directed face-incidence check verifies acyclicity on all \(132,988\) covering incidences. Equivalently, a sequential element matching is acyclic by the matching theorem. Discrete Morse theory thus gives a CW model containing exactly one 0-cell, one 5-cell and four 7-cells. Its five-skeleton is \(S^5\), and each of the four top attaching maps belongs to \(\pi_6(S^5)\cong\mathbb Z/2\).

**Step 2: a nonzero fifth cohomology class with sparse support.** Dualize the mod-two Morse chain projection to a fifth cochain \(\alpha\). For a critical degree-five face its value is one; on a matched upper degree-five face it is zero; on a matched lower degree-five face \(\sigma\), paired to \(\tau\), its value is the mod-two sum of the values on the other degree-five facets of \(\tau\). Exhaustive evaluation finds precisely four nonzero faces, with masks `73875`, `73878`, `74386`, `75922`. Every degree-six face has an even number of supporting degree-five facets, so \(\delta\alpha=0\). A 27-simplex degree-five mod-two cycle obtained by the corresponding gradient correction has boundary zero and pairs with \(\alpha\) to one. Thus \([\alpha]\ne0\) and generates \(H^5(X;\mathbb F_2)\).

**Step 3: the Hopf obstruction vanishes.** The four supporting degree-five simplices all contain the same five vertices, encoded by mask `73874`; every pair has a union of at most seven vertices. In the explicit simplicial cup-\(i\) formula for \(Sq^2[\alpha]=[\alpha\smile_3\alpha]\), each tensor term on a degree-seven simplex uses two degree-five faces whose union contains all eight vertices of the original simplex. No pair of supporting faces of \(\alpha\) satisfies this condition. Therefore \(\alpha\smile_3\alpha\) is **identically zero as a cochain**, not just zero in cohomology. The verifier also directly evaluates all eighteen degree-compatible parity-partition terms on every degree-seven face, obtaining zero.

**Step 4: pass from cohomology to integral homotopy.** A CW complex with a single 0-cell, a single 5-cell, and four 7-cells is obtained by attaching four 7-cells to \(S^5\) via elements of \(\pi_6(S^5)\cong\mathbb Z/2\). The nonzero element is the suspended Hopf map, whose mapping cone has a nonzero \(Sq^2\) from fifth to seventh mod-two cohomology. Hence vanishing of \(Sq^2\) on the fifth generator forces *each* of the four attaching classes to be zero. All four top cells attach trivially and the asserted wedge homotopy equivalence follows.

## Verification

Run `python3 verify_ladder_homotopy.py` from the package. The standalone checker exhausts all \(2^{18}-1=262,143\) nonempty subsets against an independent constraint generator, constructs and topologically sorts the entire directed matching, validates the four-term cocycle and nonzero pairing with an explicit closed 5-cycle, evaluates the cup-three square on every degree-seven face, and checks closed independent 7-cycles. The recorded result is `ALL_CHECKS_PASS`. No finite computation is used to extrapolate to other ladder sizes: the theorem concerns exactly this one eighteen-vertex complex.

## Relationship to prior work

Taylan (2015) introduced matching-tree methods for graph devoid complexes, an archive-era source for the path-free-complex approach. Deshpande and Singh (2020 preprint; revised 2021), Section 6.4 and Table 1, explicitly calculated \(\widetilde H_5\cong\mathbb Z\) and \(\widetilde H_7\cong\mathbb Z^4\) for the same nine-rung, parameter-two complex and asked for homotopy types of grid higher-independence complexes (Question 4). Those preexisting homology calculations are **not** novel here: they do not distinguish attaching maps in \(\pi_6(S^5)\). The new contribution is the vanishing Hopf obstruction, proved using a sparse cocycle and the explicit cup-\(i\) formula of Medina-Mardones. This does not imply any result about all grids.

## Limitations

The classification is confined to \(P_9\square K_2\) at higher-independence parameter two. It gives no general recurrence, symmetry representation, or classification of other grid sizes. Computational exactness depends on the fully supplied program and on the standard discrete-Morse and Steenrod-square theorems cited. The scientific review reported here is not an independent external audit. An unindexed equivalent homotopy computation remains possible.

## References

- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754, first public 2015-01-27, https://arxiv.org/html/1501.06754v1.
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first public 2020-01-15, particularly Section 6.4, Table 1 and Question 4, https://arxiv.org/html/2001.05448v2.
- A. M. Medina-Mardones, *New formulas for cup-\(i\) products and fast computation of Steenrod squares*, arXiv:2105.08025, first public 2021-05-17, especially Definition 7 and Theorem 10, https://arxiv.org/html/2105.08025v3.
- Standard integral homotopy fact: \(\pi_6(S^5)\cong\mathbb Z/2\); the nonzero suspended Hopf attaching map is detected by \(Sq^2\).
