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

# Reproducible checks
Run `python verify.py` from the directory holding this file. The program uses the Python standard library, carries out exact rational elimination, checks all four-coordinate supports in binary dimensions three and four, enumerates all without-replacement samples of the eight- and sixteen-row ambient Walsh matrices for representative dependent/independent supports, and compares exact occupancy recurrence probabilities at every length from one to twenty-eight. The program also checks the twelve rank-deficient cube quadruples and each five-vertex span, rational sample fractions, and strict sampled finite ordering through length 299. The program returned `all exact checks passed: 2 sampling models; 2 affine classes` when executed. The infinite-domain theorem and exact asymptotic coefficients are established by proof, not the finite verification.

The input sign diagonal and scaling cannot change rank and need not be randomly generated during verification. The program uses representatives because the proof and finite all-support type census establish the complete affine classification. Numeric floating-point or approximately singular matrices are not part of the result. No separate independent validation or publication-priority certification is asserted.
