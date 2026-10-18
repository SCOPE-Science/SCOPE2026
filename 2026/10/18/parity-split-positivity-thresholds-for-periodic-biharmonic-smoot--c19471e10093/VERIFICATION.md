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

# Verification and reproducibility

The proof of the universal assertion is given in `RESULT.md`. To reproduce the finite checks run `python3 CHECK.py` with Python 3 and its standard library. The checker derives cyclic inverses by direct elimination, independently evaluates the Fourier kernel, checks the continuous closed Green expression against its Fourier expansion, and samples grid sizes of both parities around the transition. One execution gave `CHECK_OK 1604 assertions`, with \(\rho\approx2.365020372431352\), \(c_*\approx0.0004994367335134717\), and second coefficients approximately \(0.00104656691\) (even) and \(-0.00359547329\) (odd).

The cutoff coefficients are defined by absolutely convergent series and require no fitted parameters. Finite tests are not proofs of the infinite asymptotics, global parameter positivity, or bibliographic priority. The asymptotic derivation and its applicability restrictions are in the mathematical proof; independent validation has not been performed.
