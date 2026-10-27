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

Execute `python3 verify_delannoy.py` in the folder containing this document. The checker uses the Python standard library only and reconstructs every coefficient of the finite congruence \(\sum_{k=1}^{8}2^k\binom{4w}{k}^2\equiv64w^3\pmod{128}\) using exact fractions. It checks the bounded cases \(9\le k\le31\) of the tail estimate and computes central Delannoy numbers independently for \(1\le n\le512\). The infinite tail and functional reflection are proved analytically in RESULT.md, not certified by finite enumeration. The standalone script is supporting evidence, not an external certification or independent audit.
