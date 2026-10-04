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
# Verification

The theorem is proved symbolically in `RESULT.md`. The standalone file `verify_three_point_spectral.py` provides an exact finite replay using only integer polynomial arithmetic.

For each tested character value, the checker computes its exact root-of-unity order and tests whether the corresponding three-term mask is divisible by the appropriate cyclotomic polynomial. It therefore avoids numerical root approximations.

The replay exhausts every three-subset for \(3\le N\le30\): \(31{,}465\) sets and \(742{,}574\) exact cyclotomic zero tests. It then exhausts every candidate three-element spectrum for every spectral three-subset for \(3\le N\le20\): \(468\) spectral supports and \(269{,}476\) spectrum-pair tests. It checks the claimed zero set, the iff spectrality criterion, the coset characterization of every spectrum, and the count \(Nh^2/3\). The expected final line is `VERIFY_OK`.

These finite checks do not prove the theorem for arbitrary \(N\); the infinite proof is the unit-triangle, Bézout, and pairwise-difference argument in `RESULT.md`.
