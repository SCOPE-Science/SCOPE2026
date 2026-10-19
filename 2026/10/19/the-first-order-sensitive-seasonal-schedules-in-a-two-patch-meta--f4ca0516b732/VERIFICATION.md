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

The algebraic proof in `RESULT.md` derives the common determinant and exact three-class trace identities. The standalone script `verify_exact.py` independently repeats symbolic factorization in SymPy and computes the numerical example with rational arithmetic using Python's `fractions.Fraction`. It checks 100 rational parameter combinations as supplemental tests, enumerates all 24 four-factor orders, and verifies every permutation of at most three seasonal factors. Run `python verify_exact.py` in an environment with SymPy installed.

In the example with \(p=1/4\) and common scale \(16/29\), exact determinants of identity minus monodromy have opposite signs: \(-290156895/500246412961\) for schedule 1243 and \(5503889057/500246412961\) for schedule 1324. Both monodromy determinants equal \(6442450944/500246412961\), strictly between zero and one, so the claimed linear growth versus decline follows exactly.

The result makes no probabilistic extinction-time, nonlinear persistence, or >4-season optimality assertion. An independent audit has not been performed.
