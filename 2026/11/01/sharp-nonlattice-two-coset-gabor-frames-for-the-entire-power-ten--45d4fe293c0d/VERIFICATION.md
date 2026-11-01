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

The exact Zak multiplier and its sharp extrema are proved in `RESULT.md`. The lower extremum occurs at \(x=1/2\) with a phase making the cosine sum equal to \(-2|\cos\pi\delta|\); the upper extremum occurs at \(x=0\), with \(\mathsf S\equiv2\). These fibres are approached on positive-measure neighbourhoods, making the resulting constants essential spectral bounds. The standalone `CHECKER.py` tests direct scalar-Zak samples and the formula on finite grids. Grid results are not used to certify all-real-parameter validity. Nonlattice historical coverage remains a literature risk. Independent mathematical audit has not been performed.
