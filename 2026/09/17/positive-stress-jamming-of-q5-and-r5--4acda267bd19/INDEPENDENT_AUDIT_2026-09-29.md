# Independent audit — Positive stresses certify infinitesimal jamming of Q5 and R5

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/17/positive-stress-jamming-of-q5-and-r5--4acda267bd19`
**Audited tree:** `4b8102fe21013c3021d7cb607f9091045f890e43`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The positive-stress argument is valid: every feasible contact derivative is nonpositive, the strictly positive equilibrium weights make their weighted sum zero, and hence every contact derivative vanishes. An independent exact reconstruction produced 40 norm-squared-2 points and 240 contacts for each of Q5 and R5, reproduced all stated contact-orbit sizes and 4/5/6 weights, verified the equilibrium identity at every vertex, and independently recomputed rigidity rank 190 modulo 1,000,003. Full span gives the matching 10-dimensional rotational kernel, so the claimed infinitesimal jamming follows.

### Independent checks

- Independently reconstructed D5, Q5 and R5 over rational coordinates; obtained 40 points and maximum pairwise inner product 1 in each configuration.
- Independently enumerated 240 contacts for Q5 and 240 for R5.
- Regenerated the stated stress orbits: Q5 sizes 60,120,30,30 and R5 sizes 24,24,48,24,24,12,24,12,12,12,12,6,6; all contacts were covered exactly once with weights in {4,5,6}.
- Checked exactly that sum_j w_ij x_j = 30 x_i at every vertex.
- Built the 280x200 equality-rigidity matrices independently and computed rank 190 modulo 1,000,003 for each configuration.

## Originality

Matthew Self’s arXiv:2609.12640 (submitted 2026-09-11) explicitly treated Q5 and R5 as the remaining open infinitesimal-jamming cases after the earlier rigidity work. Cohn–Rajagopal supplies the configurations/contact data and Cohn–Jiao–Kumar–Torquato supplies the general rigidity framework, but neither gives these two jamming certificates. A fresh search through 2026-09-29 located no earlier or concurrent source that resolves Q5 or R5 by these exact positive stresses and rank certificates.

### Literature checked

- https://arxiv.org/abs/2609.12640 — Self, Non-convex unit-edge polytopes on kissing configurations in dimensions 5–7; explicit pre-record open-status source for Q5 and R5.
- https://doi.org/10.1007/s00454-026-00841-x — Cohn–Rajagopal, Variations on Five-Dimensional Sphere Packings; construction/contact context.
- https://doi.org/10.2140/gt.2011.15.2235 — Cohn–Jiao–Kumar–Torquato, Rigidity of spherical codes; general jamming/rigidity framework.

## Scientific value

The result closes two explicit, newly isolated rigidity questions for the known 40-point five-dimensional kissing configurations and supplies compact exact certificates rather than only numerical evidence. The common equilibrium constant and small integer stresses make the result readily reusable and independently checkable.

## Limitations

- The audit does not claim that 40 is the five-dimensional kissing number, local uniqueness of either code, or a classification of all equilibrium stresses.
- Because the explicit open-problem source is very recent, unindexed concurrent work remains a residual originality risk; no concrete conflicting source was found.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
