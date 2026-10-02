# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-51dd101ca283`

## Correctness — PASS

The negative direction is an actual infinite Besicovitch family: concavity of the temporal exponent \(\sigma=p/\kappa<1\) puts the origin in every ball and the recursive separation inequality excludes every center from every other ball. In the positive direction \(\sigma\ge1\), the near-ray deficit is valid under the stated angular and size hypotheses; it forces geometric growth of the time coordinates in the mixed case, while convexity gives the vertical exclusion and the same deficit gives the horizontal exclusion. Fixed-scale volume packing plus finitely many spatial caps and separated radius buckets then bounds backward intersection degree in the greedy sequence, which yields strong BCP. The endpoint \(p=\kappa\) is included because only convexity, not strict convexity, is used.

### Correctness sources

- research package RESULT.md
- N. Dobronravov, arXiv:2609.15560
- Resultary 2026-09-19 anisotropic-threshold full RESULT.md

### Correctness residual risks

- The last packing/coloring step is a standard Besicovitch selection argument and is summarized rather than reproved line-by-line in the record.
- No optimal covering constant is established.

## Originality — PASS

The exact all-\(\kappa\ge1\) threshold was not found in the primary or current published searches. Dobronravov covers only \(\kappa=2\). A later 2026-09-19 published result proves the same threshold for \(\kappa\ge2\) and explicitly leaves \(1<\kappa<2\) untreated, so it overlaps a large subrange but does not imply the audited theorem. The audited result therefore retains a genuine uncovered range and a strictly broader statement.

### equivalent_formulations

Searches:
- Resultary: anisotropic parabolic Besicovitch mixed-power threshold p kappa
- Dobronravov arXiv:2609.15560
- synonyms: snowflaked product metric, higher-order parabolic metric

Evidence:
- Dobronravov's theorem is the \(\kappa=2\) case.
- The later Resultary theorem uses the same metric but assumes anisotropy parameter at least 2.

Reasoning:
The natural equivalent formulation is the convexity threshold for the temporal exponent \(p/\kappa\); the searched sources do not cover it for every \(\kappa\ge1\).

### broader_coverage

Searches:
- Resultary record SCOPE-besicovitch-threshold-anisotropic-parabolic-metrics--3d5e368ccdf9
- Itoh parabolic max metric
- Le Donne--Rigot graded-group BCP

Evidence:
- The later Resultary record proves the threshold only for anisotropy \(a\ge2\) and expressly says \(1<a<2\) is not claimed.
- Existence of some BCP homogeneous metric on a graded group does not classify this explicit metric family.

Reasoning:
The closest stronger-looking current result is only partial coverage, while the structural existence results concern a different quantifier.

### exact_database_or_table

Searches:
- Resultary exact/semantic search for the metric formula and threshold
- published theorem tables for Besicovitch constants

Evidence:
- No database/table supplies an all-anisotropy classification for this explicit family.

Reasoning:
The result is a theorem about an infinite parameter family, not a finite table lookup; the current semantic corpus contains only the partial later overlap above.

### claim_vs_prior_implication

Searches:
- comparison with Dobronravov \(\kappa=2\) and the 2026-09-19 \(a\ge2\) theorem

Evidence:
- Neither prior/surrounding statement entails the interval \(1\le\kappa<2\) of the audited theorem.

Reasoning:
A special case cannot imply the strictly broader all-\(\kappa\ge1\) theorem; no reduction from small anisotropy to \(a\ge2\) was found or is apparent because the metric power changes.

### source_inspections
- **Besicovitch's covering theorem in the parabolic metric** — https://arxiv.org/abs/2609.15560. Trigger: Exact \(\kappa=2\) predecessor. Material read: Current abstract/theorem scope. Method: Primary-source scope comparison. Assessment: Covers only the standard parabolic anisotropy \(\kappa=2\). Evidence: The advertised threshold is \(p\ge2\) for the \(p/2\) temporal power.
- **Besicovitch threshold for anisotropic parabolic metrics** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-besicovitch-threshold-anisotropic-parabolic-metrics--3d5e368ccdf9. Trigger: Highly relevant later current published result. Material read: Complete RESULT.md. Method: Full statement/proof/limitations comparison. Assessment: Overlaps the audited theorem for \(a\ge2\) but explicitly excludes \(1<a<2\); it therefore is not complete current coverage. Evidence: Its limitations say the intermediate range \(1<a<2\), \(a\le p<2\), is not claimed.
- **Assigned final theorem** — research package RESULT.md. Trigger: Correctness and exact quantifier audit. Material read: Complete RESULT.md. Method: Line-by-line proof reconstruction of the negative family, local positive lemmas and final packing reduction. Assessment: The argument covers the missing small-anisotropy range as well as the overlapping range. Evidence: The positive near-ray estimate is valid for every \(p\ge1\), leaving the transition to the sign of \(p/\kappa-1\).

### checked_sources

- https://arxiv.org/abs/2609.15560
- https://doi.org/10.32917/hmj/1544238028
- https://arxiv.org/abs/1512.04936
- https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-besicovitch-threshold-anisotropic-parabolic-metrics--3d5e368ccdf9
- research package RESULT.md

### residual_risks

- A large subrange \(\kappa\ge2\) is now independently covered by a later publication, so originality of that subrange no longer rests on this record.
- The highly recent literature leaves some risk of unindexed contemporaneous work in \(1<\kappa<2\).

## Scientific value — PASS

The theorem gives a sharp structural phase boundary for a canonical anisotropic metric family and identifies the mechanism as convexity versus concavity of the temporal power. The uncovered \(1<\kappa<2\) range is mathematically meaningful, and the failure side is witnessed by an explicit infinite Besicovitch family rather than a numerical example.

### Value sources

- Dobronravov's \(\kappa=2\) classification
- the later \(a\ge2\) partial extension
- research package all-\(\kappa\) theorem

### Value residual risks

- The result does not optimize constants or treat multiple anisotropic coordinates.

## Limitations

- Finite \(p\) and one anisotropic coordinate only.
- Current literature now covers the \(\kappa\ge2\) subrange, while the audited theorem remains broader because it includes \(1\le\kappa<2\).
- Originality is best-of-knowledge for the genuinely uncovered range.

## Disposition

**PASSED**
