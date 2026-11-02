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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.8 or later and the standard library only. The executable independently enumerates cyclic length-three factors directly from all \(2^n\) binary source words for each \(1\le n\le16\), groups the profiles by word Hamming weight, and compares those sets against the separately enumerated Eulerian parameter vectors. It checks total length counts against the independently derived rational generating function for \(1\le n\le42\) and the exact stabilization and one-step deficit for weights 2 through 24. It also verifies complement symmetry.

The anticipated output includes `VERIFIED: source instances = 131070`, followed by completion messages for the length and weight ranges. These are bounded checks only, not a finite certificate for the infinite identities. The infinite proof is the connected-support classification and formal generating-function derivation in RESULT.md. No third-party programs, files, or numerical databases are needed for reproduction.

A comprehensive independent scientific audit has not been performed. Priority risk remains concerning the inaccessible full text of a 2012 Markov-type enumeration paper.
