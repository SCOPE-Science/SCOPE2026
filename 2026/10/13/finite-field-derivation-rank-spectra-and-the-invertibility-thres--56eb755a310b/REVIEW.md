# Scientific review

## Correctness — PASS
Every derivation is recovered uniquely from its images on \(e_1,e_2\) and the Leibniz identities. The general seven-parameter matrix and its converse are explicit. The common-zero-diagonal slice is partitioned by \(b_3,a_2,b_4\); outside that slice, the characteristic-dependent projective line arrangement controls full rank. The exceptional characteristic-two rank-two locus is the single exact equation \(b_3^2+a b_4=0\), whose solution count is proved. Four full finite-field enumerations and independent Leibniz linear-system ranks confirm the calculation. No assumption about field primeness is used.

## Originality — PASS, with residual risk
Burde's 2004 work treats nonsingular derivation existence and prederivations in characteristic zero, not finite-field cardinality spectra. Casas–Ladra–Omirov–Karimjanov (2012) classify complex solvable extensions and use explicit derivations but do not enumerate finite-field derivation ranks. The closest available related published results count ranks of **adjoint operators** rather than arbitrary derivations (and one covers dimensions at least six). Comparison of formulas and hypotheses therefore shows no direct implication. Historical duplicate risk cannot be eliminated by a finite literature search.

## Value — PASS
Whether a nilpotent Lie algebra admits a nonsingular derivation is a structural question studied in the primary literature. This theorem supplies a sharp finite-field descent threshold \(q\ge4\) for a canonical filiform example and refines a qualitative existence question to every rank multiplicity. The characteristic-two exceptional quadratic equation produces a genuinely different lower-rank stratum, and the classification covers every extension field.

## Evidence and limits
The source arXiv:math/0409276v1 (Sections 1–3) motivates nonsingular derivations; arXiv:1203.4772v1 (Sections 2–4) describes complex filiform extensions and related derivation forms. Related published adjoint-rank results are not full derivation-rank results. The program `artifacts/verify.py` performs exact independent arithmetic in sizes \(2,3,4,5\), including \(\mathbb F_4\). General validity rests on the direct proof, and bibliographic coverage is not exhaustive.

Self-review: passed. Independent audit: not yet performed.
