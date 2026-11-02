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

The public proof in `RESULT.md` uses a complete classification modulo \(p\), one-step Hensel lifting, and direct counting of lifts; the theorem is not inferred from numerical tests. The packaged `verify.py` requires Python 3 and only its standard library. Run `python3 verify.py` from the directory containing the extracted files.

The program enumerates all \(p^6\) coefficient triples and all \(p^2\) inputs for each \(p\in\{2,3,5,7\}\), comparing their root counts against the exact generating-function coefficients (including colliding exponents when \(p=2\)). It also computes the full-space first and second moments, removes exactly the all-zero coefficient triple, and checks both conditional moments. Its successful output is `VERIFY_OK primes=4 coefficient_vectors=134067 full_root_enumeration=yes`.

This check covers four primes, not infinitely many. The asymptotic moments and the all-prime distribution are established by the proof in `RESULT.md`. No outside or independent audit has taken place.
