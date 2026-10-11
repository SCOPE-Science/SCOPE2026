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

Run `python3 verify_hex_symmetry.py` with Python 3 (standard library only). The program constructs the specified hexagonal chain, all four graph automorphisms, and their admissible vertex-orbit conflict graphs. It checks exact independence-polynomial values at \(-1\) for \(n\) from 1 through 14, and separately evaluates every fixed oriented independent simplex in the original graph for \(n\) from 1 through 4.

Observed output:

`VERIFY_OK 56 orbit-graph evaluations (n=1..14) and 16 direct signed fixed-face enumerations (n=1..4)`

All finite checks passed. The general theorem does not rest on extrapolation: the all-parameter proof is supplied in `RESULT.md` and uses an explicitly cited established homotopy theorem. No integral representation splitting, broader-grid classification, or independent external audit is claimed.
