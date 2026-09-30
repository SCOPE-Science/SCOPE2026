# Independent Audit — A weighted-histogram lower bound for the edge multiset dimension of the 6-cube

Audit date: 2026-09-29 (UTC)
Record path: `2026/09/17/a-weighted-histogram-lower-bound-for-the-edge-multiset-dimension-of-the--a8bf122d428e`
Audited tree: `d25f454b8741ebff3e0b98b41d17a481f5a58357`

## Disposition

**PASSED** — All three audit axes pass, subject to the explicit qualifications below.

## Correctness

**PASS**. The weighted-histogram obstruction is correct. For a fixed landmark s and direction of Q6, the 32 parallel edges project to Q5, so exactly C(5,r) edges in that direction have edge-distance r; summing over six directions gives 6C(5,r). Therefore for |S|=m, the global weight W=2(h0+h5)+(h1+h4) has forced total 84m. For a fixed edge, the r-shell contains exactly 2C(5,r) vertices, so when m<=7 the only binding shell capacities are h0,h5<=2. Independently enumerating all nonnegative six-part compositions with these two caps gives low-weight counts (7,12,27,36,54,60) for m=6 and (8,14,32,44,68,80) for m=7. The minimum possible total weights of 192 distinct admissible histograms are thus 670 and 612, respectively, contradicting the forced totals 504 and 588. Combined with Allikvere's published lower bound >=6, this proves edim_m(Q6)>=8.

## Originality

**PASS**. Allikvere's arXiv:2608.09983, posted 2026-08-05, explicitly states only the lower bound edim_m(Q6)>=6 while giving finite resolving sets for Q6 through Q10. Targeted searches for edim_m(Q6)>=8, Q_6 edge-multiset dimension 8, and the weighted-histogram argument did not locate the strengthened bound. The foundational 2023 paper defines edge multiset dimension but does not cover this hypercube result. The audit therefore finds the two-step lower-bound improvement original within the accessible pre-2026-09-17 literature.

## Scientific value

**PASS**. The exact value remains open, but narrowing the first finite hypercube case from [6,15] to [8,15] by a short analytic moment/capacity argument is substantive incremental progress. The method is not a brute-force exclusion of individual landmark sets; it introduces a global histogram-weight obstruction that is plausibly reusable for other distance-regular graphs or higher cubes. That is sufficient scientific value for a compact lemma/note-level contribution.

## Literature evidence

- https://arxiv.org/abs/2608.09983 — Allikvere, The edge multiset dimension of hypercubes, posted 2026-08-05; explicitly states edim_m(Q6)>=6 and finite resolving sets for Q6 through Q10.
- https://www.mdpi.com/2073-8994/15/3/762 — Ikhlaq–Ismail–Siddiqui–Nadeem, 2023 foundational paper defining edge multiset dimension.
- https://arxiv.org/abs/2607.10311 — Farhan–Klavžar–Kuziak–Yero, 2026 survey/context on multiset resolvability parameters.

## Independent checks

- Re-derived the edge-shell identity 6*C(5,r) for each fixed landmark.
- Independently enumerated capped histogram compositions and reproduced the exact low-weight counts for m=6 and m=7.
- Recomputed the minimum aggregate weights 670>504 and 612>588.

## Limitations

- The exact value of edim_m(Q6) remains unresolved; the known upper certificate is 15.
- The repository package lacks the local verifier mentioned by the source report, so the audit used an independent re-enumeration rather than claiming to have run an unavailable artifact.
- No inaccessible source is represented as read.

GitHub was used only as read-only evidence. The repository tree matched the assigned tree exactly.
