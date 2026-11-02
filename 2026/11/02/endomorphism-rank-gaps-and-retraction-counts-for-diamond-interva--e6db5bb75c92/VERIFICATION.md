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
# Verification record

Run `python3 verify.py` in the same directory as this file. The verifier constructs both binary operation tables and exhaustively checks semiring homomorphisms for \(n=1\) and \(n=2\), including every ordered input pair. Observed endomorphism ranks and counts are \((1:1,2:6,3:4,4:1)\) for \(n=1\) and \((1:1,2:20,3:96,4:96,6:2)\) for \(n=2\); the idempotent endomorphism counts are four and ten, respectively. A distinct enumeration of zero-product image assignments for \(n=3\) gives the rank counts \((1:1,2:42,3:540,4:2400,5:2880)\). The script ends with `VERIFY_OK`.

The general result is not inferred from exhaustive small-size testing: the proof reduces all semiring endomorphisms to two disjoint forms and counts them by a closed polynomial. The verifier does not inspect historical novelty, evaluate higher-height posets, or constitute an independent mathematical audit.
