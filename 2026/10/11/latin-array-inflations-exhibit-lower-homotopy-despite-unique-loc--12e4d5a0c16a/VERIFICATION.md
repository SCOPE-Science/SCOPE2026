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

Run the included `verify.py` with Python 3. It requires only the standard library. Expected final output: `VERIFY_OK 11`.

The checker constructs the additive Latin-array family for eleven parameter pairs, enumerates all simplices, checks that each codimension-one partial word is completed by exactly one facet, computes mod-two boundary ranks via exact bit-vector elimination, and verifies that the only reduced Betti number agrees with \(B(n,q)=(q-1)(q^{n-1}-(q-1)^{n-1})\) in degree \(n-2\).

The general proof relies instead on free-face collapses, connectivity of joins, a binomial face-count identity, and standard Hurewicz and Whitehead theorems. The computation proves no statement about general nonlinear arrays or all parameter values. No independent audit has been performed.
