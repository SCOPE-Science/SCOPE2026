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

Run `python3 verification/check.py` from the root of this package. The checker is standalone and uses only Python's standard library. It must print `VERIFY_OK` followed by the finite-check summaries. It confirms by exact rational arithmetic the prime-power divisor-ratio identity and the first two correction-atom predicates, checks every square-completion shift for \(1\le n\le40000\), and verifies prime-factor computations for \(1\le m\le30000\), with independent trial-division divisor counts for \(1\le m\le1600\). The full phase grids are explicitly enumerated through \(m=69\).

A completed test run returned:

```
VERIFY_OK shift_checks=40000 square_roots=30000 direct_divisor_checks=1600 exact_factor_identities=PASS correction_atom_tests=PASS exact_phase_grids=PASS
weighted_squarefree_frequency= 0.6081049688888889
limiting_squarefree_atom= 0.6079271018540267
weighted_first_correction_atom= 0.20040379
```

The two empirical frequencies are finite samples, **not proofs** of the limit probabilities. The exact atom probabilities are derived from the independent geometric prime valuations in the mathematical proof. The infinite joint weak convergence is proved analytically using a fixed-progression moment method, uniform summable prime-power tails, and exact conditional phase averaging; numerical checks cannot substitute for these steps. This package does not claim an independent external proof audit or a computer-assisted infinite theorem certificate.
