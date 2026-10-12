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

# Verification and limits

The proof proceeds through three explicit constructions: full recursive valuation on equivalence classes of known exact finite size; arithmetical extraction of the optional class partner for size at most two; and an injection-to-matching-equivalence-frame reversal recovered from \(\Box p_0\) at even worlds. The reversal uses a fixed parity-based atomic assignment; no modal nesting is required for it.

The Python 3 checker `verify.py` uses two evaluation procedures on the same finite frames: direct universal quantification over accessible worlds and the simplified evaluation via a class-partner map. It enumerates every partition of up to six labeled worlds into blocks of size at most two and tests eleven modal formula shapes under every one-variable assignment, then separately checks finite injection encodings. Run `python verify.py` in the directory containing that file; expected output:

`VERIFY_OK frames=119 valuations=5898 formula_world_comparisons=375078 range_checks=30`

Finite checks cannot establish implications over arbitrary countably infinite frames or formal-provability claims over \(\mathrm{RCA}_0\). Those rest on the mathematical proof, and no independent auditing has yet been performed.
