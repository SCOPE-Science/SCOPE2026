# Review status

Independent audit date: 2026-10-01 UTC

Disposition: **repaired**.

- Correctness: **PASS** — The filed proof omits the possibility that a sampled boundary vertex is already initially infected, so its event F_v alone is not a one-step failure event. The claim is nevertheless repairable with the same stated constant. Let H_v be the event that v is initially healthy and at most d-1 of its 2d-1 non-slab neighbours are initially infected. For d>=16, 1-p>=1/4. The filed point-mass calculation gives P(F_v)>=exp(-6)/(4 sqrt(d)), hence P(H_v)>=exp(-6)/(16 sqrt(d))>=exp(-8)/(4 sqrt(d)). A spacing-4 packing makes the H_v events independent. Whole-layer success excludes every H_v, proving the same bound as the m-th power of (1-c/sqrt(d)), with c=exp(-8)/4. The repaired RESULT states this missing healthy-vertex factor explicitly.
- Originality: **PASS** — Best-of-knowledge search found broad majority-bootstrap critical-window results for high-dimensional geometric graphs, including tori, but no primary source implying this particular one-step thickness-2 slab obstruction. The finding is an obstruction to a proof mechanism, not a new critical-window theorem.
- Scientific value: **PASS** — The result addresses a specific proposed mechanism for proving slab invasion and gives a structural reason it cannot work: an exponentially large independent packing of initially healthy under-supported vertices blocks simultaneous one-step advance. This is a motivated boundary/counterexample to a proof route, not an arbitrary numerical slice, and it clearly states that multi-round cleanup and the full window law remain open.

The detailed source comparisons and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
