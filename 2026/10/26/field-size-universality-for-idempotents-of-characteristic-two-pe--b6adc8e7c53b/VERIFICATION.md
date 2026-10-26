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

# Verification of the characteristic-two idempotent distribution

The package includes standalone `verify.py` using only the Python standard library. Run `python verify.py`. It uses independent polynomial-basis arithmetic for binary fields, enumerates every invertible structure matrix in the stated small dimensions, counts all nonzero idempotents directly, then compares to subspace-Möbius inversion. It does not use the formula being tested to count individual idempotents.

Exact observed counts:

| Dimension | Field order | Invertible matrices | Distribution of nonzero idempotents (count: matrices) |
| --- | ---: | ---: | --- |
| 1 | 2 | 1 | 1: 1 |
| 1 | 4 | 3 | 1: 3 |
| 2 | 2 | 6 | 0: 2; 1: 3; 3: 1 |
| 2 | 4 | 180 | 0: 60; 1: 90; 3: 30 |
| 2 | 8 | 3528 | 0: 1176; 1: 1764; 3: 588 |
| 3 | 2 | 168 | 0: 48; 1: 98; 3: 21; 7: 1 |

The exact Gaussian-binomial formula and unit expected number of nonzero idempotents are additionally checked for each dimension from one through twelve. Successful execution terminates with `VERIFY_OK`.

These checks are exhaustive only for the finite tested cases. The general theorem follows instead from the proved independence lemma, frame double count, invertible triangular moment system, and subspace-lattice Möbius inversion. The precise comparison with derangements uses integer arithmetic: the fixed-point-free proportions \(2/7\) and \(103/280\) are unequal. No claim of external or independent audit is made.
