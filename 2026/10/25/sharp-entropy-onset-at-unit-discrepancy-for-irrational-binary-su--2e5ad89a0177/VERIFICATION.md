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

Analytic verification: check the height-residue identity, the two possible integer window sums at the unit boundary, the disjoint interval-coded \(01\) sites, the single-height \(+1\) adjustment, the height range \((\theta-1,\theta+\varepsilon)\), equidistribution of rotation phases with density \(\varepsilon\), and the injective coding of independent choices into finite factors. This proves the exact boundary and a positive lower bound for every irrational slope; it is not a numerical extrapolation.

Execution: `python verify.py` (Python 3 standard library only). It checks illustrative irrational slopes using floating-point arithmetic, six corridor cases, and four local subset patterns per case on finite windows. It cannot certify the infinite statement, the exact entropy above threshold, or publication priority.

No independent audit was performed.
