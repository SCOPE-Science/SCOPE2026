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

# Reproducible finite checks

Run `python verify.py` to reproduce `verification_output.txt` using only the Python standard library. All six unrestricted ternary assignment cases check the original exactly-one-adjacent-defender definition: \(617{,}544\) assignments. Defender-set enumeration checks \(254{,}517\) subsets, and separate integer tests cover \(9{,}103{,}740\) inequality tuples. All completed checks printed `VERIFY_OK`.

The full statement has infinitely many parameter pairs, so finite runs do not prove it; the algebraic defender-count argument in `RESULT.md` carries that burden. The verifier counts labeled functions, not isomorphism classes. No independent external mathematical audit has been performed.
