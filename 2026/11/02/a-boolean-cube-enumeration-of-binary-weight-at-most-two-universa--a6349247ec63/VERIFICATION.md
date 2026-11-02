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

# Reproducible verification

The entire all-orders proof is in `RESULT.md`. Verification programs test its boundary conditions and numerical consequences but are not independently certified proofs.

Run `python3 verify.py` using Python 3.8+ (standard library only). This independently reconstructs the full directed graph and computes reduced integer Laplacian cofactors by the fraction-free Bareiss method for \(2\le k\le11\), enumerates all singleton-edge selections for \(2\le k\le15\), and enumerates all indexed cyclic words for \(2\le k\le5\) without using the tree proof. Expected final line: `VERIFY_OK`.

Run `g++ -std=c++17 -O3 verify_large.cpp -o verify_large && ./verify_large`. The second implementation enumerates binary cyclic words with the mathematically necessary Hamming weight \(k\) for \(2\le k\le7\), and counts rotations by division by the period (which is valid because the unique all-zero factor forces full period). Expected final line: `VERIFY_LARGE_OK`. Its direct checks include \(U_6=4\) and \(U_7=8\).

All checks were executed on the delivered source versions with the expected terminating lines. Neither source assumes the desired enumeration in its graph-based or cyclic-word enumeration logic beyond comparing against the asserted formula. Independent external mathematical audit: not performed.
