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

# Verification and reproducibility

The complete algebraic derivation is in RESULT.md. To reproduce the finite-field computations using the Python 3 standard library, run `python3 verify.py`. The checker enumerates the \(|\mathrm{GL}_2(\mathbb F_q)|\) matrices for prime \(q\in\{3,5,7,11\}\), checks the cosquare eigenline criterion and its four-case discriminant alternative, verifies all stratum cardinalities, and independently counts the two-sided and one-sided vanishing pairs for a representative matrix from each nonempty class. At \(q=3\), every triple of brace elements is checked for the Yang--Baxter identity and every pair for involutivity for each occurring class.

Expected successful final line: `VERIFY_OK`. The preceding lines report exact counts. These checks cannot prove the arbitrary-prime-power theorem by themselves, and the Python script implements only prime fields. The all-prime-power claim is supported by the symbolic quadratic-character and kernel-rank proof, which applies over every odd finite field. No external independent mathematical audit has occurred.
