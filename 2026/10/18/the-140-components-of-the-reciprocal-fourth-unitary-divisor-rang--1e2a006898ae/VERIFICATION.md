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

# Reproducing the exact result
Place `verify.py` and `INTERVALS.tsv` in the same directory and run `python3 verify.py`. The program uses only Python 3 standard-library integers and rational fractions. Its complete terminal output includes `VERIFY_OK`, `finite_tail_prime_tests=456`, `components=140`, `min_gap_lower_bound_gt_0=True`, and `interval_endpoint_table=VERIFIED`.

The prime sieve checks all 456 primes from 17 through 3271 and the transition to the 463rd prime 3299. For larger primes, the analytic step uses the published Dusart prime-gap bound; the checker verifies the remaining rational inequality \((10/11)^4+(10/11)^8>1\), not the external prime-gap theorem itself. The Machin series rigorously bounds \(\pi\); there are no floating-point comparisons in the certificate. The endpoint file records exactly 140 rows, each \((a,b)\) meaning the real interval \([a,Tb]\), where \(T=105/(\pi^4\prod_{p\le13}(1+p^{-4}))\).

A separate bounded floating-point enumeration of small-prime exponents reproduced counts 2, 4, 8, 16, 48 and 140. This was only a consistency check. The full infinite claim follows from the proof in `RESULT.md` plus the cited prime-gap theorem and the integer/rational certificate. Independent external audit is not performed.
