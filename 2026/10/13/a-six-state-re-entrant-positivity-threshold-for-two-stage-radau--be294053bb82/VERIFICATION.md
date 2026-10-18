---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The uncorrected RESULT.md asserted all-h row-stochasticity, a genuine contradiction: at h>3 c0=2(3-h)/(h²+4h+6)<0 and for N=6, 0<h<eta has t5<0. Correcting this single theorem sentence to row-sum-one resolves it, since Q_N 1=0 and R(0)=1. Independently reconstructing R(h(-I+S)) gives c0..c4=h^k R^(k)(-h)/k! and absorbing tails t_m=1-sum_{k<m}c_k; rational symbolic calculations verify displayed factors and witnesses t5(1/4)=-1607/18424351793 and t5(1/2)=4237/39135393. c0..c4 and t1..t4 nonnegative on [0,3]; p has one positive root by Descartes plus sign at 0 and 3; for h>3 negative diagonal precludes positivity. Covers N=2..6 and h=0, 3, eta boundaries, not stages/nonuniform rates/arbitrary Q.

## originality

PASS

The exact nonmonotone six-state endpoint threshold for two-stage Radau IIA was not found in inspected prior mathematical results. General Runge--Kutta positivity-threshold theory concerns uniform small-step preservation, not this nonmonotone window; related Padé/Gauss and SSP-SDIRK2 results have different rational maps and dimensions. Best-of-knowledge only; an unindexed specialization remains a genuine priority risk.

## value

PASS

The first finite-state obstruction to small-step Markov positivity and its explicit restored interval in a natural monotone birth hierarchy is a meaningful structural boundary: it corrects the intuition that smaller time steps necessarily restore positivity for all stiffly accurate RK endpoints. The exact eta and N=6 onset are not routine substitutions into a generic threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
