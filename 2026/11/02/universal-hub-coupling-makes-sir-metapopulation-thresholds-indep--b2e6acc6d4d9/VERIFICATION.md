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

# Reproducibility and limits

The exact proof appears in `RESULT.md`, including the invariant-block derivation, the discriminant, the global minimizer, and every criticality boundary. The included `verify.py` is stand-alone and uses Python 3, NumPy and SymPy; execute `python3 verify.py` from a folder containing the extracted file.

It reports 575 random heterogeneous-flux spectral comparisons (maximum absolute error approximately \(3.55\times10^{-15}\)), 42 exact characteristic-polynomial comparisons, 9 exact-rational boundary spectral checks, and 1863 randomized threshold comparisons. Three distinct peripheral structures realize \(\mathcal R_0=(53+\sqrt{2377})/120\) at the given parameters. These finite samples cannot prove the all-dimensional assertion, for which the invariant-subspace proof is supplied. No external theorem prover or independent reviewer was used. The findings concern only the stated SIR-network and equal-population, symmetric-stochastic hub hypotheses.
