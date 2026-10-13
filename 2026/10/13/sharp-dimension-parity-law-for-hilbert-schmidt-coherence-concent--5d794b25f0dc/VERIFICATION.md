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

## Scope of checks
The exact theorem follows from (i) a zero-diagonal, traceless Heisenberg contraction for each equatorial output observable, (ii) the maximum squared eigenvalue sum \(2\lfloor d/2\rfloor\) on the trace-zero spectral cube, and (iii) explicit SIO Kraus operators and strictly positive input states saturating the resulting dual-norm bound. These derivations are included in `RESULT.md` and are the proof for all dimensions.

## Reproducible computation
Run `python verify.py` using Python 3 and NumPy. The program constructs channel matrices at every integer dimension \(2\le d\le12\), checks \(\sum_j K_j^*K_j=I_d\), verifies diagonal-state preservation and the single-nonzero-entry property of all Kraus matrices, computes the full-rank input spectrum, and checks the sharp amplification ratio. Independently enumerates every extreme point of the zero-sum eigenvalue cube for these dimensions. Observed output:

`VERIFY_OK dimensions=11 exact_spectral_vertices=passed Kraus_completeness=passed full_rank_saturation=passed incoherent_marginals=passed`

The enumeration is not an infinite-dimensional argument. Full correctness depends on the analytic polytope proof and Hilbert–Schmidt dual pairing, not on tests or logs.

## Remaining verification limits
No independent mathematical audit has been performed. No general-output-dimension constant is determined. One relevant paper's full text was not accessible, so its possible equivalent presentation has not been eliminated by whole-document inspection.
