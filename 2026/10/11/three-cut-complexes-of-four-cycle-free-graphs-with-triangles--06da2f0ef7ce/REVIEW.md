# Scientific review

**Correctness — PASS.** The Alexander dual contains precisely connected triples as two-faces and no higher faces under the no-four-cycle condition. Each induced path triangle has a uniquely owned nonedge; after its collapse, each remaining graph triangle has an edge not shared with another graph triangle. The resulting connected one-complex determines integral cohomology; Alexander duality plus full-skeleton connectivity and the Hurewicz–Whitehead argument determine the stated wedge homotopy type. The standalone checker reconstructs the dual and its collapses for triangle necklaces and the truncated tetrahedral graph, and directly computes the latter's reduced mod-two Betti numbers.

**Originality — PASS, with literature risk.** The closest cited primary paper covers foundational general results, chordal-graph shellability, and specific graph families, not a theorem for arbitrary graphs with triangles and no four-cycles. An earlier triangle-free/no-four-cycle theorem excludes all graphs in the asserted scope. The distinct *total* cut-complex results do not cover the ordinary complex. Searches for aliases including `square-free`, `C4-free`, and `four-cycle-free` identified no equivalent all-parameter statement. Unindexed results or an unrecognized implication from a stronger published theorem remain possible.

**Value — PASS.** The theorem classifies the full homotopy type for a structurally natural infinite graph class, not just its Euler characteristic or a finite sample. Allowing triangles changes the rank by an explicit twice-triangle correction and covers nonchordal examples, including the truncated tetrahedral graph, which are not handled by chordal shellability. Four-cycle exclusion is a precise boundary where the proof's private-edge collapse fails.

**Limits.** No claim concerning shellability, equivariance, or graphs containing four-cycles; no independent validation.

Same-model review: passed. Independent audit: not yet performed.
