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

Run `python3 verify.py` with Python 3.8 or later. This standalone script uses only the standard library. It checks all odd primes below \(152\), for \(n=3,5,7\) (prime \(\ell=2^n-1\)); for every field and every rotation it explicitly enumerates allowable nonzero first coefficients and verifies each defining product equation, independently enumerates all nonzero idempotents, and compares against the formulas. It additionally tests one prime with a nontrivial \(\ell\)-th-root kernel and a positive \(\ell\)-th power-residue condition for each dimension (\(631\), \(683\), and \(78233\) respectively). Expected output: `VERIFY_OK exhaustive_prime_field_cases= 105 high_residue_cases=3`.

The infinite-dimensional-index theorem, group isomorphism types, and natural densities do not follow merely from this finite check; their algebraic and number-theoretic arguments are in RESULT.md. In particular, the Chebotarev density theorem is invoked as a classical external theorem. The \(p=\ell\) group scheme is nonreduced, but the finite-field classification concerns rational automorphisms. Independent audit: not performed.
