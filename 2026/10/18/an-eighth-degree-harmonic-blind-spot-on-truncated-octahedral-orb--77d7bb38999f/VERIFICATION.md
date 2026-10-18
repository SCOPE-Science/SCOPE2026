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

The accompanying Python 3 / SymPy script `check_sampling.py` was executed from its packaged path. It returned ranks \((1,3,5,6,9,9,10,12,11)\) for degrees \(0\) through \(8\), checked the alternating null vector at degree \(8\), and proved nonzero modular determinants at every integer degree \(9\) through \(528\) for each of two large primes. The concatenated residue certificate SHA-256 was `db404eb282a54c7cb605520f99a6c727a841e6f1c0bfc50e3635aa7414e9ee01`.

The exact computation covers a finite interval only. The separate Laplace-integral Legendre inequality proves strict diagonal dominance at every degree at least \(529\). The signed-alternant and transcendental-parameter statements rely on their algebraic proofs in `RESULT.md`, not on finite numeric sampling. Independent mathematical validation has not been performed.
