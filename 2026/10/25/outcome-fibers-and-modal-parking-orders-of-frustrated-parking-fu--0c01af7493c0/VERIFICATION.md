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

# Reproducibility and limits

Use Python 3's standard library to execute `python3 verify.py` from the extracted package directory. The companion file `verify_output.txt` is the captured, exact stdout of that checker. The verification directly simulates every one of the \(n^n\) possible preference words for \(1\le n\le7\) rather than generating words from the product formula. It independently constructs outcome fibers, checks the established double-factorial total, compares all fibers for all permutations, verifies the sharp inequality and its complete equality case at each fixed number of right-to-left maxima, then compares every modal permutation with the classified set.

All output rows for \(n=1,\ldots,7\) terminate in `OK` and the final output line must equal `VERIFY_OK`. These are finite corroborative checks, not a proof over every \(n\). The general conclusion rests on the predecessor-counting and equality proofs in `RESULT.md`.

There has been no external independent mathematical audit. Bibliographic priority risk remains despite the explicit primary-source comparison.
