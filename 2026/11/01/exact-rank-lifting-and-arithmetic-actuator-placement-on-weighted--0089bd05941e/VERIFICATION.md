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

# Verification record

The theorem is proved analytically by the explicit Fourier--Jacobi and PBH argument in `RESULT.md`, valid for every stated positive conductance and every allowed integer dimension. Computational tests check finite instances rather than asserting infinite certification.

To reproduce the supplementary checks from this standalone directory, use `python verify.py`, with NumPy and SymPy available. The checker constructs both the full weighted Laplacian and the smaller Fourier blocks independently; compares their spectra, confirms strict separation of interbranch intervals, and computes eigenspace-wise PBH ranks for 1,126 total test instances. These include six exact characteristic-polynomial factorizations and forty full exact rational Kalman matrix ranks, obtained without assuming the Fourier-PBH rank formula.

The run reported `PASS 1126 spectral, PBH and exact rational Kalman checks; 6 exact characteristic identities and 40 exact Kalman ranks`. No numerical tolerance is used for the exact rational checks. The numerical spectral tests use an eigenspace grouping tolerance and are not an exhaustive certificate of the theorem.

The inaccessible full Liu--Ji (2017) source is a literature-priority risk, not a failure of a needed mathematical lemma. Independent audit is not performed.
