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

# Verification instructions and limits

Execute `python3 artifacts/verify.py` from the package root and compare its stdout, byte-for-byte, with `artifacts/expected.txt`. The complete check uses only the Python standard library; no computer-algebra library or external database is needed.

The program constructs all \(24\) projective transformations over \(\mathbf F_3\), all smooth members of the \(2186\)-element nonzero sextic coefficient space, all \(69\) isomorphism orbits, and all Weil coefficient pairs by counting points in \(\mathbf F_3\) and \(\mathbf F_9\). Assertions check the complete \(1296\)-equation smooth locus, \(50\) distinct Weil types, exact eight singleton fibers, and the independent order-three fixed-form locus with \(42\) equations. The output prints the exact eight Weil pairs with representative coefficient vectors and orbit sizes. Finite exhaustion is mathematically complete because the entire input parameter space is enumerated, not sampled.

The hyperelliptic reduction and characteristic-three invariant-ring argument are presented in `RESULT.md`; the executable check supports its exact count and Weil uniqueness conclusions. No claim is made about extensions of the base field or an independent human audit.
