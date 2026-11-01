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

# Verification notes

The package's `checker.py` was executed from its actual file path using Python 3 and SymPy. It enumerated 24 small primitive-word ensembles (alphabet orders 2 through 5, lengths 2 through 10 according to computational size), checked 115 exact pair-character moments derived independently from equal-letter counts, verified 24 complete rational characteristic polynomials, and performed 1,071 additional exact-arithmetic checks across alphabet orders 2 through 10 and lengths 2 through 120. All tests passed. To replay, run `python checker.py` in the directory containing these files.

The universal statements are proved by the Möbius period sieve, cyclic Fourier orthogonality, a positive sum-of-squares identity and a uniform union bound. Exhaustive small cases are not claimed to prove the infinite theorem. Higher-degree, nonuniform, and historical-equivalence questions remain outside these checks. An independent audit has not been performed.
