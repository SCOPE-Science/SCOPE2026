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

# Verification of the Erlang purity–fidelity threshold

Run the accompanying source file with `python3 verify.py` in Python 3. No third-party libraries or external data are required.

The script constructs the integer-coefficient polynomial \(Q_k\) directly from the printed binomial formula, carries out exact rational Euclidean polynomial division and Sturm sign-variation counts, and verifies zero positive roots for all \(2\leq k\leq13\), two positive roots at \(k=14\), shape-14 rational root brackets, and its positive exact witness. It also verifies the rational lower bound supporting the analytic every-\(k\geq15\) witness, and recomputes the characteristic-function identity and polynomial reduction by independent rational complex multiplication for 24 parameter combinations.

All 92 exact assertions passed. Separate numerical integration against the stationary age law corroborated representative qubit cases \(k=1,13,14,15\) to floating-point precision. The all-integer \(k\geq15\) result is proved by the analytical monotonicity and rational inequality in the proof, not by enumerated tests; numerical quadrature is corroborative only. Publication priority and an independent scientific audit were not established here.
