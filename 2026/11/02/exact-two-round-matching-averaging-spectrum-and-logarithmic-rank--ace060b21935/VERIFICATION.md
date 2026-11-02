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

# Verification of two-round matching-averaging theorem

The file `verify_two_round_matching.py` is a standalone reproducibility program. It requires Python 3 and NumPy. To reproduce the finite checks, run `python verify_two_round_matching.py` in the folder containing the program; the exact run output is supplied as `verification_output.txt`.

The program enumerates every perfect matching of the \(2m\) labeled vertices for \(1\leq m\leq6\) while holding the first matching fixed, constructs both pair-averaging matrices directly, checks every computed singular value against the cyclic cosine formula, and checks the claimed rank. Exhaustive matching counts are \(1,3,15,105,945,10395\), totaling \(11464\). Exact rational polynomial coefficients are independently compared against the enumerated distributions. The code further compares a generating-function recurrence with the unlabeled cycle-index expansion through \(m=11\).

The replay passed 124,975 assertions. The numerical singular-value comparisons use a strict tolerance, not a formal exact-arithmetic matrix certificate; the rank identity and singular spectrum also have an analytical derivation in `RESULT.md`. No finite test establishes the Gaussian limit, the rare-event constant, or the expected Wasserstein rate; these depend on the infinite \(m\)-asymptotic proof. No independent audit has been performed.
