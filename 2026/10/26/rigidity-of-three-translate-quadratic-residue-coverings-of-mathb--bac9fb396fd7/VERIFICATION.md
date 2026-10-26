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

# Verification evidence

Execute `python3 verifier.py` using Python 3 with no third-party dependencies. The arithmetic represents \(a+bu\in\mathbb F_{25}\) as the integer \(a+5b\), where \(u^2=2\). The checker verifies distributivity across all \(25^3\) argument triples, the complete list of \(13\) squares including zero, all \(23\) cubic character sums, the character-sum identity and Hasse bound for all \(2300\) three-element subsets, and that exactly \(100\) subsets cover the field. It independently checks the two-root parametrization, the explicit affine-square orbit and its stabilizer order \(3\), and absence of any two-element covering.

Expected final lines:
```
CERTIFICATE_OK squares=13 triple_subsets=2300 covers=100
CUBIC_SUM_CLASSES {-10: 2, -6: 2, -2: 8, 2: 4, 6: 7}
AFFINE_SQUARE_ORBIT 100 STABILIZER 3
```

The finite enumeration is exhaustive for the claimed \(25\)-element field. The conceptual character-sum reduction separately invokes Hasse's proved elliptic-curve inequality, not an experimental estimate. The verifier does not establish novelty over all possible literature or any asymptotic claim, and it does not constitute independent mathematical review.
