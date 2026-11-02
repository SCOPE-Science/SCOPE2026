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

Run `python3 verify.py` with Python 3 and the standard library. No external dependencies, cached data, or network access are necessary. The resulting output is included in `verification_output.txt` and ends in `VERIFY_OK`.

The exact finite certificate constructs all 48 classical-line labels and their intersections from the given equations, checks the symmetric intersection matrix and its valency, performs fraction-based Gaussian elimination to obtain its rank, and computes Frobenius orbit-sum Gram ranks for all odd residues modulo eight. It also enumerates projective points on the Fermat quartic over \(\mathbb F_3\) and \(\mathbb F_7\). The short finite computations are not being used to infer an infinite family of primes: the ordinary Hasse argument and supersingular Hermitian-cover/Tate argument are required for the global rank statement.

The proof does not construct explicit missing divisor representatives or determine integral indices. The comparison with generalized classical Fermat character-sum formulas may warrant further historical scrutiny.
