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

# Verification and limits

The mathematical proof in `RESULT.md` establishes the statement for all \(d\ge3\) by classifying point-stabilizing rotations and invoking the classical orbit-space fundamental-group theorem. Finite programs only corroborate the proof.

Run `python3 verification.py` for the full orbit-by-orbit exhaustive checks of 9,996 nonidentity rotations with \(3\le d\le100\), comparing every vertex orbit's eligibility with the closed gcd criterion and verifying the generated subgroup order.

Run `python3 quotient_chaincheck.py` for an independent mod-prime first-homology calculation of the **geometric barycentric quotient two-skeleton**, with \(d\in\{3,4,5\}\). It constructs quotient vertices, edges and triangles from strict face chains, uses a spanning tree to eliminate boundaries in degree one, and computes ranks of degree-two relations modulo \(2,3,5,7,101\). The results appear in `verification_output.txt` and agree with the predicted cyclic groups \(\mathbb Z/3\), \(\mathbb Z/4\), \(\mathbb Z/5\) in their tested dimensions. Finite fields do not themselves distinguish all possible prime powers or prove the infinite classification; those deductions use the proved orbit-space formula.

No independent audit was performed. The full homotopy types and higher integral homology of the quotients remain open in this statement.
