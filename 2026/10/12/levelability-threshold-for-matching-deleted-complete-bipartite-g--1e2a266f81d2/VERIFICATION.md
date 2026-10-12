---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof is analytic and applies to all admissible parameters. It classifies maximal independent sets directly, solves the weighting equations in every positive case, and uses the published four-set positive-weight obstruction in every negative case with \(t\ge2\) and \(a+b>4\).

The standalone script `verify.py` reconstructs the graph from adjacency, enumerates every nonempty vertex subset, identifies maximal independent sets without using the claimed list, and checks all parameter triples with \(1\le a,b\le6\). For positive cases it verifies explicit positive integer weight witnesses. For negative cases it checks the exact four maximal independent sets and strict-union certificate used by the analytic proof.

Replay command: `python verify.py`

Observed output: `ALL CHECKS PASSED; parameter_cases=127; maximal_sets_checked=438; nonlevel_obstructions=54; a,b_range=1..6`

The finite enumeration is not an exhaustive proof for unbounded \(a,b\); it is only a stress test of the structural proof and boundary handling.
