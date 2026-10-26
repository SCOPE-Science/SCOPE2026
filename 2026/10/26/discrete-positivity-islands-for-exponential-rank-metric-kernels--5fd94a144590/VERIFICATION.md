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

## Analytic checks
The finite Fourier transform convention is unnormalized, with frequency \(B\) indexed by additive characters. The rank-\(s\) multiplicity is the number of rank-\(s\) matrices, and all multiplicities sum to \(q^{mn}\). The Gaussian-binomial Newton identity is proved for infinitely many choices \(z=q^h\) by counting linear maps and therefore holds identically. Fourier-transforming the annihilator-subgroup indicators yields the formula for every \(\lambda_s(t)\). At isolated strengths the subgroup coefficients vanish exactly above the appropriate degree. At excluded strengths, \(\lambda_{n-1}\) and \(\lambda_n\) have opposite signs. This establishes every quantified claim without a computational cutoff.

## Standalone executable check
Run `python verify_rank_kernel.py` under Python 3, requiring only its standard library. Its exact rational tests compare 3,957 direct character sums with the claimed transform on binary and ternary matrix spaces; further exact polynomial calculations check sign and Fourier rank support for four prime-power cardinalities and dimensions up to five. No approximate numerical tolerances are used. These are finite corroborations, not proof of universal claims.

## Limits and external validation
The claim is restricted to \(0\le t\le1\) and full matrix groups. Independent audit and external replication are not claimed. The inspected literature does not exhaust all potential equivalent sign analyses of generalized Krawtchouk spectra.
