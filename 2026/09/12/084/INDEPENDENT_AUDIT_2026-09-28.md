# Independent audit — 2026-09-29

**Record:** `2026/09/12/084`  
**Disposition:** **repaired**  
**Audited tree:** `d6071444398ace0a2ebd45611a7e49f5949dea1d`

## Correctness
The topological conclusion is correct for proper branched coverings of C≅R^5 with compact branch set, but the clean justification is a direct application of Kauranen-Luisto-Tengvall Proposition 4.3: R^5 has torsion-free (indeed trivial) fundamental group at infinity. The repair also separates this branched-cover assumption from any unproved claim that every analytic step-3 Cartan quasiregular map is automatically open/discrete.

## Originality
The filed originality analysis was wrong. Proposition 4.3 is valid in every n>=3 and directly implies the entire-R^5 self-map statement; the submitted exterior-sheet proof is therefore an alternate proof/application, not a new theorem.

## Scientific value
The corrected note is still useful because it immediately rules out the proposed proper compactly-branched degree>1 Cartan construction and directs future searches to nonproper or noncompact-branch regimes.

## Findings
- Kauranen-Luisto-Tengvall Proposition 4.3 directly covers the topological claim.
- Originality claim withdrawn and record reframed as a Cartan-group corollary.
- Analytic quasiregularity is no longer used to assert openness/discreteness without a step-3 theorem.
- Artifact path corrected to `artifacts/check_numerology.py`.

## Independent checks
- Read Kauranen-Luisto-Tengvall Proposition 4.3 and its dimension hypothesis.
- Verified Cartan topological dimension 5 and homogeneous dimension 10 from the archived script.
- Checked that R^5 has trivial fundamental group at infinity, satisfying the published proposition.

## Limitations
- Only proper branched coverings are covered; nonproper maps and noncompact branch sets remain outside scope.

## Sources
- https://pmc.ncbi.nlm.nih.gov/articles/PMC9311082/
- https://doi.org/10.1112/blms.12565
- repository:2026/09/12/084/RESULT.md
