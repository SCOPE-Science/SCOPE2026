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

# Reproducibility and bounds of verification

Run `python verify.py` with a standard Python 3 interpreter. The script generates direct channel outputs by recursively selecting disjoint neighboring swaps and discarding swaps of equal symbols. Independently, it computes the product of Fibonacci counts over maximal runs of unequal-neighbor indicators. It tests agreement on all words over alphabets of sizes two, three, four and five, respectively through blocklengths ten, eight, seven and six: 53,260 words. It also evaluates exact rational moments of orders one and two via the first-run recurrence and independently aggregates the direct output-ball volumes.

The recorded output `verify_output.txt` ends with `VERIFY_OK`. Numerical checks compute the explicit limiting coefficients at six alphabet sizes and compare the first large-alphabet correction. These finite calculations are *checks*, not proofs of infinite-volume limit laws or the large-alphabet asymptotics. The actual proofs rely on the explicit positive-pole generating function, implicit differentiation, and standard asymptotic analysis. No independent scientific audit has been performed.
