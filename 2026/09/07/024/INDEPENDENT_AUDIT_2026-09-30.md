# Independent mathematical audit — 2026-09-30

## Outcome

**PASSED** for the final finding as stated.

## Correctness — PASS

The exact final claim is a finite classification in the reduced reflexive weighted-projective 4-simplex class. Re-enumeration of all nondecreasing five-tuples of divisors of Q with sum Q and gcd 1 for 5<=Q<=430, followed by the exact age histogram, gives 139 rows through Q=430 and exactly 136 through Q=377. The only violations of h2*<=3h1* through Q=430 are Q=378, q=(2,7,54,126,189), h*=(1,75,226,75,1), and Q=420, q=(3,7,60,140,210), h*=(1,83,252,83,1). Equality through Q=377 occurs exactly for the two Q=12 weights stated. This verifies the finite extremal statement, conditional only on the cited classical reflexivity criterion qi|Q for this reduced weighted-projective simplex model.

## Originality — PASS

No inspected prior source states or implies the sharp Q=377/378 h*-coefficient threshold. General reflexive-simplex classification and weighted-projective IDP/unimodality literature provide the ambient language and enumeration framework, but the exact coefficient inequality threshold and 14-member core-family crossing were not found. Residual risk remains from unpublished or differently indexed weight-system tables.

### equivalent_formulations

Searches: "h2* <= 3h1*" weighted projective reflexive simplex; "(2,7,54,126,189)" h*; reflexive weighted projective 4-simplex coefficient inequality

Evidence: The assigned RESULT.md is the only exact matching published-record hit in the semantic search; no external exact match was found.

Reasoning: The natural aliases are reduced reflexive weighted-projective simplex, reflexive simplex with reduced weight system, and age/h*-vector formulation. Searches across these aliases did not expose an earlier equivalent threshold statement.

### broader_coverage

Searches: Conrads reflexive simplices reduced weights; Braun Davis Solus weighted projective simplex IDP unimodality; Ghirlanda classification algorithm reflexive simplices

Evidence: Conrads gives a weight-system characterization/classification framework; Braun et al. address IDP/unimodality families rather than this finite coefficient threshold.

Reasoning: The broader results inspected do not logically imply the first violation volume 378 or the exact equality/violator list without performing the new finite classification.

### exact_database_or_table

Searches: reflexive simplex weight-system databases dimension 4; classification algorithm reflexive simplices weights

Evidence: Known classification machinery can enumerate candidate weights, but no inspected published database/table was found that tabulates the target inequality or identifies 377/378 as the threshold.

Reasoning: A raw complete weight table could make the numerical threshold mechanically extractable; no such exact table covering the target statistic was located in the inspected sources.

### claim_vs_prior_implication

Searches: h*-coefficient inequalities reflexive simplices; IDP implies h*-unimodality weighted projective simplices

Evidence: The cited IDP/unimodality work does not imply h2*<=3h1* up to a sharp volume cutoff; the target coefficient relation is distinct from ordinary unimodality.

Reasoning: No inspected prior theorem entails the final threshold as a corollary.

### source_inspections


- **Weighted projective spaces and reflexive simplices** (https://doi.org/10.1007/s002290100235): trigger=Classical reflexivity criterion used by the proof.; material read=Bibliographic metadata and accessible abstract/summary, not full text.; method=Primary-source metadata/abstract inspection.; assessment=Supports the reduced-weight characterization framework; no exact Q=377/378 coefficient threshold was found in the material read.; evidence=The source classifies reflexive simplices in terms of reduced weight systems.

- **The Integer Decomposition Property and Weighted Projective Space Simplices** (https://arxiv.org/abs/2103.17156): trigger=Highly relevant weighted-projective simplex literature.; material read=Abstract and stated scope.; method=Primary preprint abstract inspection.; assessment=Covers IDP classifications/stabilizations, not the target sharp h*-coefficient threshold.; evidence=No statement in inspected material gives the 377/378 threshold.

- **Detecting the Integer Decomposition Property and Ehrhart Unimodality in Reflexive Simplices** (https://arxiv.org/abs/1608.01614): trigger=Highly relevant reflexive-simplex h*-literature.; material read=Abstract and stated scope.; method=Primary preprint abstract inspection.; assessment=Concerns IDP and Ehrhart unimodality families; no implication to the exact target threshold was identified.; evidence=The target inequality is not ordinary unimodality.

- **Assigned finite classifier** (2026/09/07/024/artifacts/scan_weights.py): trigger=Critical exhaustive certificate.; material read=Complete source file.; method=Line-by-line inspection plus independent reimplementation of the enumeration.; assessment=The finite sweep logic matches the claimed universe under qi|Q and reproduces the headline counts and first violations.; evidence=Independent sweep reproduced 136 rows through Q=377, 139 through Q=430, exact equality and violator lists.

### checked_sources

- doi:10.1007/s002290100235
- arXiv:2103.17156
- arXiv:1608.01614
- arXiv:2510.09131
- assigned RESULT.md and scan_weights.py

### residual_risks

- Full text of Conrads was not available in the inspected access path; an unpublished/differently indexed finite weight table could overlap the numerical threshold.
- Originality is best-of-knowledge, not a priority certificate.

## Scientific value — PASS

The result identifies a sharp boundary for a natural h*-coefficient inequality on a standard reflexive-simplex class, gives exact extremizers/equality cases, and isolates a structured 14-member family explaining the first failures. This is a motivated finite cutoff and structural boundary, not an arbitrary slice or mere recomputation of a known table.

## Limitations

- Correctness of completeness uses the cited classical qi|Q criterion rather than re-proving it.
- The classification is computational rather than a hand proof.
- Originality remains best-of-knowledge because highly relevant classification literature was not all available in full text.
