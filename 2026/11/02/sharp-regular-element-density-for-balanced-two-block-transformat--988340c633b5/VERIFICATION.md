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

# Reproduction and limits

Run `python3 verify_regular_bipartition.py` with a standard Python 3 interpreter. No third-party modules, external data, randomness, or network access are needed. In the direct tests for \(m=1,2,3\), the script enumerates all four characters and all pairs of restrictions, then checks \(fgf=f\) by actual composition over all candidate inner inverses. The results are \(4/4\), \(60/64\), and \(2400/2916\). This direct method is independent of the subsequent Stirling-number calculation. The script also checks exact formulas through \(m=12\), computes the saddle numerically by bisection, and checks the asymptotic ratio at \(m=40,80\), printing `VERIFY_OK` on success.

The finite computations do not prove the assertion for all \(m\). The unrestricted proof uses image-set classification, inclusion-exclusion, and a full-lattice two-dimensional local limit argument. The script verifies numerical consistency of the proposed correction, not publication priority or independent scientific validation.
