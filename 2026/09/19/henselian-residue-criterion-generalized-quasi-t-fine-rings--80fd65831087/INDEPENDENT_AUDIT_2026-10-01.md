# Independent mathematical audit — 2026-10-01

## Final claim assessed

Henselian residue criterion for generalized quasi t-fine rings

## Correctness — PASS

PASS. For a local ring, every radical element is quasinilpotent and any element outside the radical is a unit; taking its inverse in its centralizer shows it is not quasinilpotent, so the quasinilpotent set equals the Jacobson radical. The defining decomposition is therefore exactly surjectivity of torsion units onto the residue division group's nonzero classes. A division ring with torsion multiplicative group is a locally finite field by the classical periodic-division-ring theorem. In the commutative Henselian case, every nonzero element of a locally finite residue field has finite order prime to the residue characteristic, so its simple root of X^n-1 lifts to a torsion unit. The Z_(p)/Z_p contrast follows immediately. The matrix obstruction is also sound: reduction of the quasinilpotent summand is nilpotent, while a rational finite-order matrix has cyclotomic characteristic polynomial; modulo p, a single repeated root forces the prime-to-p cyclotomic index to have Euler phi equal to one, hence residue root plus or minus one, contradicting the chosen class for p at least five.

## Originality — PASS

PASS to the best of current knowledge. Published-record semantic search found the audited record as the only exact Henselian/residue/torsion-lifting statement. The Bien–Danchev–Ramezan-Nassab preprint is the exact highly relevant source. Its accessible primary abstract states the new generalized quasi t-fine class, examples, and matrix/group-ring investigations but does not state a Henselian residue classification. Ordinary open full-text retrieval failed; an authorized institutional retrieval attempt did not yield readable full text in this run, so no whole-document noncoverage claim is made. That access risk is explicit. Standard Hensel theory and periodic-division-ring theorems are treated as prior ingredients, not novelty.

### equivalent_formulations

Searches: Resultary: generalized quasi t-fine Henselian local ring residue torsion units Z_(p) matrix; web search: generalized quasi t-fine Henselian residue field torsion units

Evidence: No earlier published record with the torsion-lifting/Henselian equivalence was returned. The defining local decomposition is equivalently surjectivity of torsion units modulo the Jacobson radical.

Reasoning: Equivalent residue-unit and roots-of-unity formulations were searched; no prior exact theorem was located.

### broader_coverage

Searches: arXiv:2609.19882v1; Stacks Henselian local rings; periodic division ring theorem

Evidence: The primary abstract describes the broader new class and structural investigations; Hensel lifting and periodic division rings are classical ingredients.

Reasoning: Those standard ingredients do not themselves state the generalized quasi t-fine classification or mixed-characteristic matrix consequence.

### exact_database_or_table

Searches: Resultary exact semantic search for Z_(p), Z_p and generalized quasi t-fine

Evidence: No database/table is relevant; no earlier exact published theorem record was found.

Reasoning: This is a structural ring theorem, so theorem-level search is the applicable exact check.

### claim_vs_prior_implication

Searches: Bien Danchev Ramezan-Nassab 2609.19882 accessible primary material; generalized quasi t-fine matrix rings mixed characteristic

Evidence: Accessible source material does not expose a Henselian residue criterion; full text could not be obtained, so residual implication risk remains.

Reasoning: The local Q=J observation plus Hensel lifting gives a concise proof, but no inspected prior statement was found that packages or implies the full final classification and matrix obstruction.

## Scientific value — PASS

PASS. The final claim gives a natural intrinsic classification on the important Henselian local subclass of a newly introduced ring property, together with a sharp localization-versus-completion boundary and a mixed-characteristic matrix obstruction. Although the Hensel-lifting step is short, the package organizes the property around residue torsion lifting and answers a motivated structural question rather than merely renaming a textbook lemma.

## Source inspections

- **Generalized t-Fine and Quasi t-Fine Rings** — https://arxiv.org/abs/2609.19882v1. Material read: Primary abstract and indexed descriptions stating the definitions, structural program, and matrix/group-ring investigations. Ordinary open full-text access failed, and a subsequent authorized institutional attempt did not produce readable text. Assessment: INACCESSIBLE_HIGHLY_RELEVANT_PRIMARY_SOURCE. Evidence: The accessible material does not state the Henselian residue criterion, but whole-document noncoverage is not asserted.
- **Henselian local rings** — https://stacks.math.columbia.edu/tag/04GM. Material read: Standard theorem context for Henselian lifting/complete local rings. Assessment: STANDARD_BACKGROUND. Evidence: Used only for the simple-root lifting step; it does not mention the generalized quasi t-fine property.

## Limitations and residual risks

No full matrix-ring classification over arbitrary Henselian local bases is claimed; originality is best-of-knowledge because the exact new-source full text remained inaccessible.

- The full text of arXiv:2609.19882v1 could not be read in this run despite open and authorized access attempts; it remains a genuine originality risk.
- The matrix argument relies on the source's stated quasinilpotent-reduction lemma as quoted in the assigned result; that lemma was not independently read from full source text in this run.

## Disposition

**passed**
