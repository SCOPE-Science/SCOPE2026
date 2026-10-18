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
# Exact verification

Place `INVOLUTION_CERT.json` and `verify_involution_standalone.py` in one directory and execute `python3 verify_involution_standalone.py INVOLUTION_CERT.json` using Python 3 (standard library only). The certificate uses complete lexicographically indexed rank classes for every \(1\le r\le n\le8\). The script reconstructs every map, verifies the involution property and both semigroup inverse equations for its partner, and checks the exact number of fixed idempotents against a separate closed formula. Expected final output: `PASS: exhaustive rank-preserving involution inverse matching, n=1,...,8`.

The proof is finite and exact, with \(\binom{2n-1}{n}\) maps checked at every \(n\le8\). The verification supplies no conclusion for \(n\ge9\). The identity and count formulas are explained in the result; no independent audit has been performed.
