# Self-review

**Correctness — PASS.** The statement quantifies over every ternary cyclic word and uses the standard reversal-exclusion definition. The proof converts a cycle into a balanced subgraph, proves the six special vertex caps, and gives an explicit integral potential inequality for all 216 nonpalindromic five-edges. All 108 reversal pairs and their 486 total weight, the 72 special-vertex allowance, and all 93 windows of the extremal witness are rechecked from the packaged source. No external solver, floating-point tolerance, sampled hypothesis, or unproved infinite step is required.

**Originality — PASS under best-available-source comparison.** The most directly relevant primary paper, Mitchell and Wild's *New orientable sequences* (arXiv:2507.02526v1, 2025), reports 93 as a construction and 99 as an upper bound at precisely these parameters (Table 7); it states that the remaining gaps for order above four persist. Its general upper theorem therefore does not imply the claim that 93 is optimal. Gabrić and Sawada's *Constructing k-ary Orientable Sequences with Asymptotically Optimal Length* (arXiv:2407.07029v1, 2024) provides long constructions and a general asymptotic result, not this exact upper bound. Reversal symmetry, dual balance, or changes of terminology do not turn their lower constructions or weaker upper bounds into the explicit 93 upper certificate. Earlier unpublished or unindexed priority is a residual risk; absence from a database alone is not used as proof.

**Value — PASS.** The prior primary literature identifies the exact natural parameter as a genuine 93–99 gap in directional position-sensing sequence design. The theorem closes it completely with a human-checkable rational certificate, rather than incrementing a known table or refining only a numerical witness. The symmetry-compressed dual inequality is a reusable structural device for related de Bruijn constraints, although no broader theorem is claimed.

**Limits.** No classification of all optimal cycles or statement for other alphabets/orders; no independent external validation.

Self-review: passed. Independent audit: not yet performed.
