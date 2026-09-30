# Independent audit — Depth-one local Clifford ensembles are non-plussed distinct

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/local-cliffords-nonplussed-distinct--1434efbb2fb7`  
**Audited tree:** `512dfc27fe385e3e68c8d226f06248bf95bcae00`

## Disposition

**PASSED.** Correctness, originality on the stated narrow boundary, and scientific value all pass. The record may remain in the validated set.

## Correctness

**PASS.** The lifting argument is sound. The Foxman–Lombardi–Ma–Nehoran–Wright projector-intersection estimate reduces DNP failure to ordinary-distinctness failure, NoPlus failure, and the stated Friedrichs-angle penalty. For NoPlus, I-Q is bounded by the sum of the t one-register plus projectors, so averaging conjugates gives at most t times the operator norm mu_+. For a product of independent local exact 2-designs, the local equal-label projector twirls to [2/(d+1)] Pi_sym because it has trace d inside a d(d+1)/2-dimensional symmetric subspace; independence therefore gives pair-collision norm [2/(d+1)]^n. The pair-event union bound yields the stated binomial factor, and tensor products of independent local 1-design twirls are the global depolarizing twirl, so mu_+=1/d^n. The qubit Clifford specialization and negligibility for polynomial t follow.

## Originality

**PASS, with the limitations below.** The originality claim survives on a narrow boundary. Raza–Eisert–Fefferman's September 2026 source explicitly poses non-plussed distinctness of the depth-one independent single-qubit Clifford ensemble as an open question; their result establishes ordinary distinctness, not the DNP lifting proved here. Foxman et al. provide the DNP geometry/global-design analysis, but not this product-local corollary. The audited repository history showed no changes to the assigned tree and no earlier cited theorem covering this exact lifting statement. Because the deduction is short and the source is extremely recent, contemporaneous or unindexed priority remains a real limitation, but I found positive source evidence that the motivating question was open rather than merely an unsuccessful search.

## Scientific value

**PASS.** The result answers an explicit open structural question for the shallowest Clifford distinct ensemble and supplies a reusable sufficient condition—ordinary distinctness plus one-copy plus-state flatness—for DNP concentration. The explicit qudit product-design bound is useful for assessing which PRU ingredients can plausibly be removed, while the record correctly stops short of claiming the full phase-layer-free PRU security reduction.

## Independent checks

- Re-derived the NoPlus union bound for arbitrary entangled t-register inputs.
- Computed the local equality-projector 2-design twirl from symmetry and trace and tensorized it across sites.
- Checked the pair-collision union bound and the product-local 1-design depolarizing identity.
- Verified that the motivating source explicitly leaves local-Clifford non-plussed distinctness open.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.03065 — Raza–Eisert–Fefferman source; its discussion poses non-plussed distinctness of the depth-one independent single-qubit Clifford ensemble as open.
- https://arxiv.org/abs/2606.30281 — Foxman–Lombardi–Ma–Nehoran–Wright source for the distinct-nonplussed subspace geometry and global-design analysis.

## Limitations

- The theorem controls parallel forward-query DNP concentration; it does not itself establish pseudorandom-unitary security after deleting the phase layer.
- The explicit bound is used only for t<=N/2 and constants are not claimed optimal.
- The motivating papers are very recent, so contemporaneous or unindexed independent observations remain a priority risk.

## Repository identity

The assigned source-tree SHA `512dfc27fe385e3e68c8d226f06248bf95bcae00` matched the current tree at the audited path after comparing the assignment inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` with the source-tree checked commit `253a0fe5d0217455660a277f9adb940030e567ad`; none of the intervening changed files touched this record. GitHub was read only during the audit.
