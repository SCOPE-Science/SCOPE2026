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

# Reproducibility

Run `python3 verify.py` from this directory using Python 3 and no third-party dependencies. Exact binary-field arithmetic uses the irreducible polynomials \(x+1\), \(x^2+x+1\), and \(x^3+x+1\) for \(q=2,4,8\). The verifier exhaustively tests the complete invertible algebra-homomorphism sets for dimensions \(3\) over \(\mathbb F_2\) and \(2\) over \(\mathbb F_4\), and directly enumerates all conjugation orbits, compares exact support stabilizers, and checks the divisor sum for ten small field/dimension pairs. The expected terminal line is `VERIFY_OK`.

The symbolic proof reconstructs the complete automorphism group, coefficient action, stabilizers and Burnside count for all \(e\ge1\), \(n\ge2\). Finite checks are evidence of agreement in the enumerated cases, not a replacement for the general proof. Literature priority remains qualified. Independent mathematical audit has not been performed.
