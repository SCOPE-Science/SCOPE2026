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

## Reproduction
Place `verify.py` and `paths.csv` together and run `python3 verify.py` using Python 3.8 or later. No third-party libraries, network access, or external files are required. A successful run emits `VERIFICATION_OK` and the complete candidate and cycle counts.

## Checks actually performed
- Complete trial-division primality checks for each candidate vertex and each factor in every candidate list.
- Exhaustive enumeration of all two-edge directed paths whose least vertex is a prime not exceeding \(349\).
- Exact comparison of all \(70\) recomputed paths with `paths.csv` and identification of the unique closing cycle.
- Exact checking of three displayed prime divisibilities, the squarefree three-prime product, and the integer reciprocal-gcd quotient.
- Independent exact factorization and modular-arithmetic calculation of the same \(70\)-candidate census and one closing cycle.

## Logical scope and limitations
The minimum proof depends on the elementary bijection between three-cycles with least vertex at most \(349\) and closing paths in the complete finite search; it does not extrapolate finite data to an unbounded cycle classification. No independent audit has been performed.
