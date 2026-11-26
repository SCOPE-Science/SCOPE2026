---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Under the stated positivity and mixed-allele hypotheses, the transport matrix makes both allele masses strictly positive after one pulse. The Hardy–Weinberg marginal survivals give a row-stochastic mixing of susceptible/resistant ratios followed by a nonnegative selection defect. Normalized resistant masses have a uniform positive bound after one step; hence every mixing weight is bounded below, and the strict loss at a selected stage forces the maximum ratio to zero in a two-step argument. The two mass recursions are then bracketed componentwise by (1 ± epsilon) times their respective positive limiting matrices; comparison with Perron powers and strict Perron monotonicity give the log root-ratio exponent. When s_i h_i vanishes identically, resistant mass is exactly linear and the susceptible defect is exactly quadratic to leading order. The minimum ratio has an inverse-pulse lower bound; the weighted quadratic drift and uniform mixing give an inverse-pulse upper bound and O(k^-2) stage spread. Thus the reciprocal of the Perron-weighted ratio has increment tending to sum_i s_i w_i v_i with w^T v=1. This also justifies converting ratios back to frequencies and does not require growth of the total population. A separate two-stage diagnostic with rho(P)<1 agrees with the two scalings; it is not used as proof. Replay the analytic checks in RESULT.md lines 42–112; the archived verify.py is supplemental, not formal verification.

## originality

PASS

The inspected academic model proves qualitative fixation, not either sharp asymptotic formula. A distinct catalogue result states both exact formulas on a materially overlapping common-dominance, s_i<1 domain, including the same dominant coefficient and an additional between-pulse extension. Credit that overlap in full: the common model and the coefficient there are not distinct findings relative to that record. The frozen theorem covers pulse laws for a wider nonlinear system, including stage-specific dominance at fixed independent homozygote and heterozygote survivals and allowed s_i=1. The closest statement does not give that scope; no earlier equivalent coverage of the full claim was established. Catalogue path dates are not a determination of priority or dependence.

## value

PASS

Qualitative fixation alone cannot distinguish an exponential tail from an inverse-pulse tail. The theorem distinguishes them using measurable model parameters and shows how stage transport and survival jointly determine the actual coefficient, not merely its order. It applies when selection acts on heterozygotes in some stages but not others and also when the population itself shrinks, separating allele-frequency predictions from demographic persistence. Its value is a deterministic asymptotic prediction for the stated model, not an empirical control recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
