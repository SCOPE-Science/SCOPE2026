---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed necessary-and-sufficient Boolean completion: all m distinct (m-1)-attribute coatom rows must occur, because each missing coatom forbids closure separation, and all coatoms make every subset closed. Under one Dirichlet draw frozen across objects, required row-category mass R=pi_{m-1}~Beta(a_m=beta_m/(m+1),b_m=m beta_m/(m+1)); conditional each of m coupon types has probability R/m. Coupon-collector identity yields E[T|R]=mH_m/R and exact inclusion–exclusion. Beta inverse first moment gives E[T]=infinity if a<=1 and mH_m(beta_m-1)/(a-1) if a>1. For beta_m=m+1, mR=>Exp(1) and coupon concentration conditional on mR yields CDF exp(-1/x) for T/(m² log m). For fixed beta, -log R/m=>Exp(beta) and elementary coupon delay bounds vanish after /m log scaling. Independently inspected standard-library exact-rational verifier of closure equivalence and Dirichlet-multinomial moments for m<=3; finite checks only corroborate, not establish the weak limits. All results concern one frozen vector and unlimited sequential rows, not resampled vectors or fixed finite contexts.

## originality

PASS

Felde–Hanika (2018) introduces exactly the Dirichlet formal-context generator and coatom conditional coupon observation; Felde–Hanika–Stumme (2020) studies null models and precision. These premises are expressly credited. Inspected source material does not establish the unconditional inverse-beta mean threshold or the two different precision-scaling weak limits. Sakurai (2021) studies independent Bernoulli incidences, not frozen Dirichlet row-size mixture. Yang et al (ICMLC 2024), Counting Formal Concepts of A Random Formal Context, is a plausible source by title but no lawful OA/arXiv full text was found and authorized publisher access reported VPN disconnected; material read is only abstract/bibliography, so no whole-document noncoverage claim.

## value

PASS

Distinguishes typical polynomial completion time from infinite mean in the natural simplex-uniform model and shows an exponential time scale at fixed total prior precision. The sharp integrability threshold and two limiting laws answer natural stopping-time questions for a published random-context generator, beyond mere coupon collector conditional expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
