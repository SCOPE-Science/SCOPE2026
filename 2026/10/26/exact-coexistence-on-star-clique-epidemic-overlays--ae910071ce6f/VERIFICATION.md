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

The proof treats arbitrary integers \(m\ge2\) and positive effective rates; the verification program is auxiliary, not an infinite proof.

Run `python verify.py` with Python 3 and SymPy. The program derives the susceptibility/coordinate algebra symbolically and substitutes into all four uncompressed stationary equations. It compares the full exact-rational positivity conditions against the displayed sharp threshold for \(25,872\) admissible parameter triples, and directly evaluates all \(2(m+1)\) vertexwise residuals, each as an exact rational number. The calculation identified \(2,208\) strictly positive examples and no disagreements.

The two explicit rational examples are cross-checks: \(m=3,a=2,b=1\) and \(m=2,a=3,b=2\). All calculated fractions are exact. No finite grid confirms uniqueness for all real rates; uniqueness is proved by the strictly increasing leaf-susceptibility equation and nonsingular two-variable linear system. General asymptotic dynamics, basin geometry, and nonpositive boundary equilibria were not checked. No independent audit was performed.
