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

# Reproduction and scope

The analysis assumes integer \(m,n\ge2\), positive weights and sink strength, and a full-rank finite vertex basis. The decay term is exactly \(-i\gamma|0,0\rangle\langle0,0|/2\). The survival law keeps the size and positive detector parameters fixed as the detuning tends to zero.

With Python plus NumPy, SciPy, and SymPy installed, run `python artifacts/verification.py` and `python artifacts/test_survival.py` from the extracted finding directory. The first test independently constructs full spectral projectors by matrix polynomial interpolation and compares 170 exact-rational absorption identities. It also checks 24 eigenvalue linewidths across six board/absorber choices. The second test evaluates 32 full-matrix propagator predictions at long times, including all four initial-position classes. The test tolerance is under \(0.022\) relative for the linewidth and \(0.025\) absolute for the survival probabilities. Tests passed on the packaged programs.

Neither the matrix checks nor the numerical limits prove the all-size theorem independently; the product spectral decomposition, weighted Cauchy identity, dissipativity argument, and rank-one resolvent derivation in `RESULT.md` do so. No external independent audit has been performed. Originality is limited to the explicitly inspected literature and available research-record comparisons.
