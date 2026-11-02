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

# Supplementary verification

The complete proof appears in `RESULT.md`. Run `python3 verify.py` in a directory containing the supplied standalone file, with no dependencies beyond the standard library.

The program was run on the exact embedded source text before package acceptance. It checked the exact rational two-mode cancellation \(E(v)=4\), \(E(w)=28\), \(E(2v-w)=4\), \(D_h(v)=0\), \(\Delta_h(v)=24\); and it exercised hundreds of deterministic seeded positive spectra, modal-to-direct energy identities, sharp ratio envelopes, monotonic effective spectral mean, and bracketed zero crossings. It also tests pure eigenmodes. These are finite reproducibility checks; the statements over all dimensions, spectra, and positive lookbacks rest on the analytic argument, not extrapolation from finite experiments.

No independent mathematical audit has been performed. Published-priority uncertainty is recorded separately from correctness.
