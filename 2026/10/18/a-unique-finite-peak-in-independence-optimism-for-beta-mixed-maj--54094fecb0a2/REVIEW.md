# Scientific review: A unique finite peak in independence optimism for Beta-mixed majority juries

## Correctness — PASS
The proof starts with the exact two-added-voter majority difference, integrates the Beta weight, and obtains the explicit positive gain ratio. The ratio's successive quotients differ from one by the sign of a quadratic with a positive leading coefficient and a negative constant, so there is one positive root. Starting below one and diverging to infinity, the ratio crosses one exactly once. The signs of the signed gap follow from its positive asymptotic limit, covering all positive shapes, both orientations, and the symmetric exception. The 336 exact-rational checks in `verify_jury_beta.py` were executed successfully. They supplement the analytic proof, not replace it.

## Originality — PASS (best-knowledge, residual access risk)
The full readable Kaniovski–Zaigraev (first online 2009) and Kaniovski (2010) primary documents were compared with the claim. They study specific higher-order constrained correlated-jury mechanisms, not the Beta-distributed latent competence gap across all odd jury sizes. General de Finetti-dependent-jury results, including Ladha's and Berg's 1993 work, are important and are acknowledged; their complete texts were inaccessible in this review, leaving a nontrivial residual equivalence risk. Berend–Sapir's augmentation results were readable only as an abstract, so no full-text exclusion is asserted. Actual indexed research searches found no direct prior theorem about this particular exact one-peak calibration error. The previous finite-support exchangeable-jury sign-change result concerns a different sequence and law. No claim of exhaustive publication novelty is made.

## Mathematical value — PASS
The natural target is the discrepancy in panel-majority correctness predictions when a common latent expertise variable is mistakenly replaced by independent competence of the same mean. The theorem establishes a global finite worst panel size with a transparent formula for identifying it, as distinct from standard signs of correlation effects or asymptotic correctness. It is a complete classification across an unrestricted two-parameter family, not a small numerical improvement. It does not assert real-world juror fidelity, arbitrary dependence, or strategic behavior.

## Verification limits and sources
Only exact rational instances were computationally replayed; the analytic proof establishes the infinite-parameter claim. The uncertainty due to inaccessible classical full papers persists. Main sources are Kaniovski–Zaigraev, DOI 10.1007/s11238-009-9170-2; Kaniovski, DOI 10.1007/s11238-008-9120-4; Berend–Sapir, DOI 10.1007/s00355-006-0179-y; Berg 1993, DOI 10.1007/BF00187435; Ladha 1993, Social Choice and Welfare 10:69–85.

Self-review: passed. Independent audit: not yet performed.
