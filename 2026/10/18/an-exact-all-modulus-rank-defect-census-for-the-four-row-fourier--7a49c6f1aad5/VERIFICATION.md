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

# Verification record

The standalone `verify_defect_census.py` uses the standard Python library. It checks the determinant factorization as an identity of exact four-variable integer polynomials before the cyclotomic computations. Running `python verify_defect_census.py` from the directory containing the file must produce the exact contents of `verification_output.txt` (besides ordinary process buffering). It recursively constructs each cyclotomic polynomial \(\Phi_N\) by integer monic division of \(\prod_{d\mid N}\Phi_d=X^N-1\), then reduces each six-edge product sum in the quotient ring \(\mathbb Z[X]/(\Phi_N)\). The resulting zero predicate is independently compared with the three explicit combinatorial classes for **every** four-column selection at nineteen listed moduli up to 60. It also checks the 15 possible opposite-edge pairings in the unique primitive six-term relation and both order-30 free orbits.

The exact test has no floating-point tolerance or numerical root calculation. It supplies finite replay evidence only: the infinite statement requires the determinant identity, the published classification of minimal vanishing sums, and the counting arguments given in the mathematical proof.

Independent audit: not performed.
