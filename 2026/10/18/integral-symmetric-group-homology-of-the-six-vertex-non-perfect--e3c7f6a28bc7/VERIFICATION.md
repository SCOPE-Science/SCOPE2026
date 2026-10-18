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

# Exact verification instructions

Run `python3 verify.py` in this folder. No input files or third-party packages are required. The script reconstructs every edge subset of \(K_6\), all perfect matchings, ten maximal triangle-pair facets and the remaining subcomplex. It checks the complete reversal of 43920 Hasse incidences after a deterministic matching of 3967 face pairs, rejecting any gradient cycles. A 52-term integral four-cocycle is checked on every five-simplex of the remaining complex; all ten attaching evaluations are exactly \(+1\) or \(-1\). Every one of the 720 permutations of six vertices is checked against the normalized signed action on the ten cells; eleven conjugacy types are represented.

Expected success token: `VERIFY_OK_NPM6_INTEGRAL_SIGNED_AUGMENTATION`. The underlying homology identification then uses the exact relative long sequence and the sign character of the intermediate four-sphere. The checking is exhaustive for this fixed finite complex; no parameter range outside six graph vertices is covered. The review reported in these files is not an independent audit.
