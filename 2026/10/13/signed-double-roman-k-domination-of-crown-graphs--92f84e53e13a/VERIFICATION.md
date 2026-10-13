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

The bundled `verify.py` checks the theorem directly from the definition. It exhausts all \(4^{2n}\) labelings for \(n=3,4,5\), tests the rescue rules, computes the minimum closed-neighborhood sum, and records the minimum weight for every \(1\le k\le3n\). These values are compared to the closed formula.

The same script checks the explicit matching-symmetric constructions for every \(3\le n\le40\) and every admissible \(k\), and checks the two exceptional witnesses separately. It also confirms that no labeling can satisfy \(k>3n\) from the closed-neighborhood size bound.

The exhaustive computation is a finite stress test. The proof in `RESULT.md` establishes the arbitrary-order theorem analytically; no finite enumeration is treated as evidence for an infinite quantifier.
