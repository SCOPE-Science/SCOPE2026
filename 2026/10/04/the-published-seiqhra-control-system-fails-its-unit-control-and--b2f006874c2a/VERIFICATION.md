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

Checked the complete 28-page primary AIMS PDF directly, especially printed uncontrolled Eq(1) on page5 and controlled Eq(16) on page15: source incidence lambda*S*I/(1+c*A) becomes lambda*S*I/(1+A), so setting all ui=1 fails to reproduce Eq(1) when c!=1 and ASI>0. Summing all six human compartments in Eq(16) cancels every proper internal transfer except (1-u1)*A*(r1I+r2Q+r3H), yielding Ndot=Pi-dN-delta*(I+Q+H)+(1-u1)*flux. Independent Fraction arithmetic verifies original 1/44 vs 1/48 incidence and defect 7/400. Repairing recovered gain by u1 changes Hamiltonian derivative to B1 u1+(xi6-xi3)r1AI+(xi6-xi4)r2AQ+(xi6-xi5)r3AH, hence stated projected optimality law under paper’s quadratic 1/2 B1 u1². The correction is to the repaired MODEL, not to the printed original Hamiltonian.

## originality

PASS

Direct full-PDF comparison of uncontrolled system, controlled system and Hamiltonian found exactly the mismatches, with no published correction in the observed search. Earlier awareness/treatment models and generic internal transfer conservation illustrate the algebra but do not compare this 2026 model’s two vector fields or entail the source-specific costate correction. Resultary returned adjacent Pontryagin/model error records but not a dominating correction of this exact source.

## value

PASS

Two independent control-model inconsistencies affect the actual optimization problem: intervention values at one do not return the uncontrolled baseline, and recovery produces artificial population growth. The minimal consistent model has a different stationarity law; this changes interpretation and reproducibility of the published numerical optimal-control claims, beyond a cheap dimensional typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
