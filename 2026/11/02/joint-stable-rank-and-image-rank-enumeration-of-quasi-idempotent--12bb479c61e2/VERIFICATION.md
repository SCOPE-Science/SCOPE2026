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

# Reproducible verification

Run `python3 verify.py` with the standard Python 3 library. The program directly enumerates all \(\binom{2n-1}{n}\) nondecreasing self-maps of \([n]\) for every \(1\le n\le10\), constructs the second through fourth powers as actual maps, checks the two equivalent stabilization equations, and records each \((|\operatorname{im}f^2|,|\operatorname{im}f|)\) cell. It compares the complete direct counts with the closed binomial formula.

It also independently generates all admissible monotone maps from a rooted half-interval of lengths zero through nine and checks the critical \(\binom{a}{2j}\) count for each number of nonzero image values. The executed program produced `LOCAL_HALF_LEMMA_OK a=0..9`, `EXHAUSTIVE_OK` for each size one through ten, `RECURRENCE_OK 1..10`, `FIVE_POINT_CORRECTION_OK 53`, and `VERIFY_OK`.

The count at size five is 108 maps satisfying \(f^3=f^2\), 55 idempotents, and 53 strictly non-idempotent quasi-idempotents. All checks are finite and standard-library reproducible. The proof in `RESULT.md`, not exhaustive search, establishes the formula for unbounded \(n\). No independent mathematical audit has been performed.
