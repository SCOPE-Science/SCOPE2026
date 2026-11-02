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
# Verification of the one-gap divisor-sum theorem

Run `python3 verify_divisor_gap.py` in the same directory as this document. Python 3's standard library suffices. Successful execution ends with `VERIFY_OK exact rational interval certificate for every real 1.9<=r<=1.91`.

The script constructs rational lower/upper bounds for each \(n^{-a/b}\) using exact integer-power comparisons at mesh \(10^{-9}\), for \(1\le n\le1024\), and bounds the remaining Dirichlet series by integral comparisons. It evaluates the bounds at the rational endpoints \(19/10\) and \(191/100\); monotonicity establishes the required worst-case comparisons for every intermediate **real** parameter. It checks the strict prime-seven and prime-eleven tail comparisons, the isolated prime-three gap, the overlaps among positive prime-three and prime-two powers, and the two necessary band joins. The assertions are in exact rational arithmetic, although readable decimal slack estimates are also printed.

The script additionally checks the 33,605 relevant consecutive-prime ratios below the cited finite cutoff; larger primes use the published analytical bound. The script is not a brute-force proof of an infinite claim. Infinitely many prime factors are handled by Defant's proved prime-ratio lemma and the prime-tail interval construction, detailed in RESULT.md. The one-gap topology and component densities then follow from explicit interval unions and divisibility by two and three. Independent mathematical audit has not been performed.
