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

Run `python3 verify.py` with Python 3 and no third-party dependencies. The script tests 12 binary cases (68,160 nonzero values), 11 full finite-level unit power images (6,720 units), and the Singer witness sets at degrees \(7\), \(13\), and \(21\). It checks distinct difference residues and the full finite quotient power-class group for these witnesses. Its printed `PASS` lines provide the exact finite checkpoint counts.

The claim for **all** prime powers is proved in `RESULT.md` by the finite-field trace-pairing and projective-plane intersection argument. The program cannot establish an infinite assertion by enumeration; it provides replayable error detection for its small cases only. The underlying input coordinates are integers, and rational quotients of single-coordinate values are dense within the permitted nonzero power classes. No independent audit has been performed.
