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

The proof is symbolic and valid for every integer \(n\ge2\). The accompanying `artifacts/verify.py` provides a finite replay that does not assume the closed degree formula when counting local coarsenings.

For each relative permutation through \(n=8\), the program identifies all marked right-to-left maxima, directly counts the two allowed kinds of codimension-one harmonic coarsenings, and compares that count with \(2n+s-3-\varepsilon_- -\varepsilon_+\). It then checks the exact simple marked-permutation count \(3(n-1)!+(n-2)!H_{n-2}\). The final line is `VERIFY_OK harmonic-polytope simple-vertex classification n=2..8`.

The computation is finite and therefore does not establish the theorem for untested \(n\); the all-\(n\) proof is the combinatorial argument in `RESULT.md`. No independent audit has been performed.
