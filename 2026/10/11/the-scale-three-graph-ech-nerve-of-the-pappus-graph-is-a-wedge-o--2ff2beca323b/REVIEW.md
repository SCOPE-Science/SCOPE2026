# Scientific review: the Pappus graph scale-three Čech nerve

## Correctness — PASS
The statement concerns the unit-edge metric graph Čech nerve at radius \(3/2\), not a vertex-metric clique complex. Lemma 2.2 of Adams–Shukla–Singh gives its 27 generating six-vertex faces. The supplied executable checks all 1107 nonempty faces, each of 422 elementary free-face collapses and the entire two-dimensional residual complex. A spanning-tree certificate has 17 edges; 92 explicit triangular van Kampen reductions successively kill all 92 non-tree edge generators, proving simple connectivity. The residual Euler characteristic is 45, so integral Hurewicz and homological Whitehead give a wedge of exactly 44 two-spheres. The independent mod-two boundary-rank computation agrees but is not used as an integral proof. Risk: the finite certificate and its reconstruction code should be independently rerun and inspected; no external audit has occurred.

## Originality — PASS, with residual bibliographic risk
The closest primary source, Adams–Shukla–Singh (arXiv:2212.05871), supplies the general odd-scale Čech face formula and a strict girth recovery bound, but its homotopy classifications involve hypercube graphs. Previte's distance-neighborhood complexes are vertex-centered; Shukla's Lovász neighborhood complexes use common open neighbors. Neither inspected construction/classification implies the Pappus nerve's 44 two-spheres. Related published computations concern the same graph with different complexes (Vietoris–Rips, matching and independence). Searches for corresponding aliases, facet unions, 44 two-spheres, Pappus incidence graph and broader cubic-graph results found no equivalent covering statement. Risk: search coverage is not exhaustive; priority against unindexed literature is not mathematically certified.

## Value — PASS
The Pappus graph is a distinguished 18-vertex symmetric cubic incidence graph of girth six. The exact parameter \(r=3\) is naturally motivated as the first scale excluded by the general \(r<\mathrm{girth}(P)/2\) graph-recovery theorem. The result determines a complete *integral homotopy type*, detects 44 higher-dimensional classes and provides a concrete non-shellability consequence. It is a natural exact invariant beyond merely recomputing a known homology table. The work does not assert a broad all-cubic-graph classification or a full barcode.

## Closest references and scientific limits
Adams, Shukla, Singh, arXiv:2212.05871, Lemmas 2.2–2.3 and Sections 4–7; Previte, *The D-Neighborhood Complex of a Graph* (2014), Definition 12 and Chapters 3–8; Shukla, arXiv:1802.04526, Introduction and Theorem 2.1; Weisstein, *Pappus Graph*, MathWorld. The finite graph is fixed by its LCF description, and the exact certificate is included. There is no external validation of its novelty or proof.

Same-model review: passed. Independent audit: not yet performed.
