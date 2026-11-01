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

# Mathematical and computational verification

**Analytical checks.** The Zak normalization, the geometric-series identity for the summed frame multiplier, the normalization \(\Phi_{q,a}(0)=1/q\), the rank-one positivity criterion, integrability of the logarithmic edge and the two endpoint asymptotics were checked directly in the accompanying proof. The resulting theorem quantifies the exact post-erasure sharp lower bound, not merely the existence of a positive lower frame bound. No result about uniqueness of critical pole depth is asserted.

**Supplementary numerical checks.** Run `python3 verify_erasure.py` with the Python 3 standard library. The script checks formula consistency for integer redundancies \(2\le q\le5\), representative strict edge tests on both sides of one threshold for \(q=3,4\), and the leading asymptotics at small and large depth. It prints `All supplementary numerical checks passed.` when successful. These quadratures are numerical diagnostics, not proofs of an integral inequality for all parameters, spectral multiplicity, or an asymptotic limit.

**Source and integrity limits.** Exact Cauchy Gabor operator formulas and unperturbed frame bounds are treated as prior scientific background. Comparisons with inspected primary literature support a provisional historical novelty assessment; a published source with a stronger implicit edge calculation remains a residual risk. Independent mathematical audit has not been performed.
