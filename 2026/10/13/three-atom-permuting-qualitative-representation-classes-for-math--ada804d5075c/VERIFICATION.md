---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

Run `python3 verify.py`. This uses exact finite enumeration and the standard library only. Every one-factorization is isomorphic to one containing the fixed matching, since its factors are perfect matchings and all perfect matchings are equivalent under vertex relabelling. The script enumerates the fixed-factor exact covers and groups them by vertex relabellings. In every case it tests the equivalence of full triangle-triple coverage and pairwise Hamiltonian union. It constructs the affine representative separately and checks that its fixed-factor orbit is precisely the 64 factorizations with full coverage. It checks the full colour-permuting automorphism group, then recounts triangle triples **after** deleting each vertex of the affine representative. For the explicit triple \(\{2,4,5\}\), it checks that its sole witness is lost by deletion of \(0\).

```
fixed-factor census: 416 {7: 2, 11: 42, 13: 28, 17: 168, 26: 112, 35: 64}
fixed-factor class sizes: [2, 28, 42, 64, 112, 168]
automorphism order: 42 ; vertex orbit sizes: 1, 7
restriction triple counts (finite vertices, then infinity): [29, 29, 29, 29, 29, 29, 29, 35]
VERIFY_OK
```

The script verifies finite graph claims. The published structural theorem on base size and seven-to-eight point extension is the separate input identified in `RESULT.md`.
