# Scientific review: identifying open codes of subdivided complete graphs

## Correctness — PASS

The proof computes open code signatures separately for original and subdivision vertices. Two unselected original vertices create an undominated subdivision vertex; choosing all but at most one gives distinct nonempty signatures. On the opposite side, equal nonempty incidence signatures mean precisely an isolated selected edge, while empty signatures mean isolated selected vertices. This is an exact equivalence, not a sufficient-only construction. The connected-component bound \(|F|\ge n-c\ge n-\lfloor n/3\rfloor\) yields the minimum, and equality forces every component to be a tree. Cayley's formula counts all labelled equality forests. The labelled exponential formula independently yields every polynomial coefficient. The attached verifier exhaustively checks actual open-neighborhood signatures through \(n=5\), selected-edge graphs through \(n=6\), and the generating function independently over these finite cases.

## Originality — PASS, with bounded bibliographic risk

Chakraborty–Wagler (arXiv:2412.17469v1, section 2.2 and conclusions) characterize the graphs saturating *logarithmic* cardinality bounds for several identification parameters; they do not calculate the one-subdivision-clique code polynomial or minimum count. Chakraborty–Foucaud–Henning (arXiv:2407.09692, introduction and main result) analyze maximum-degree upper bounds for 4-cycle-free graphs and subdivided stars, not this exact two-part signature classification. Argiroffo–Bianchi–Lucarini–Wagler (2019, sections 2–4) study universal-vertex, corona and graph-square operations, not full edge subdivision of cliques. Existing graph-subdivision results about *closed* identifying codes do not imply open total domination and separation. A published central-graph total-domination result gives \(n-1+\lceil n/2\rceil\) for the same underlying graph but lacks separation; here the sharp minimum is \(n-1+\lceil2n/3\rceil\). Related published mathematical claims about double subdivision with pendant arms, total domination of central graphs, or other properties of one-subdivisions likewise do not give the current assertion. Search and text-inspection coverage was substantive but cannot certify exhaustive global novelty; not all potentially adjacent specialist literature was available in full.

## Value — PASS

This is an exact structural description of **every** code in an infinite, natural incidence-graph family. It determines all coefficients of a graph invariant and, separately, a sharp three-periodic extremal formula and exact labelled minimizer multiplicities with distinct residue-class tree profiles. Those statements refine broad bounds into checkable combinatorial data and expose the selected-edge spanning-forest mechanism that controls optimality; they are not mere restatements of a standard domination number.

## Remaining limitations

No independent audit or comprehensive bibliographic-priority certification has been performed. The displayed argument concerns \(n\ge3\) and the full one-subdivision of complete graphs only. Tests for finitely many \(n\) are corroboration, not the source of the infinite theorem. Direct full-text checking of every potentially related older paper is not claimed.

Self-review: passed. Independent audit: not yet performed.
