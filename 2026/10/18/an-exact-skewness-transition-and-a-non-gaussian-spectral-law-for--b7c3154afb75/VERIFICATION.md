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

Execute `python3 verify.py` from this package using Python 3.10 or newer. No third-party dependency is required. The program independently checks exact three-vertex edge-count distributions over several finite circular grids, rational third-moment identities and sign cases for sample sizes through 100, and finite Fourier sums against the continuous triangle and variance formulas. The recorded run completed **993 checks** with status PASS.

The discrete grids approximate continuously uniform locations; they do not themselves prove the continuum result. The exact proof for all \(n\ge3\) and \(0<r<1/2\) uses forest independence, Dirichlet-gap integration, the third-cumulant combinatorial expansion, and a quadratic sign polynomial. The fixed-radius limiting distribution uses the uniform \(L^2\) bound for Fourier-truncation remainders and a multivariate central limit theorem. The nonzero third cumulant of the limit follows from the centered triangle integral. No independent audit or external theorem certification has been performed.
