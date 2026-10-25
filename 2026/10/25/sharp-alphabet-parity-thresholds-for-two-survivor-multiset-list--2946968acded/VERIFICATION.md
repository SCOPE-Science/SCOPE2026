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

# Verification of the mathematical claim

The counting bound and equality analysis are analytic. The standard-library checker `checks/verification.py` independently materializes the two construction families, computes their complete two-survivor incidence vectors, and checks that the code sizes meet the claimed bound at the stated source lengths and list allowances for alphabet sizes \(4\) through \(8\). The graph decompositions were tested for sizes \(4\) through \(23\) and up to four complete edge-partition cycles. As an optional independent formulation, `checks/finite_opt.py` solves the complete binary-integer optimization on all quaternary length-five multisets via SciPy's mixed-integer optimizer. It gives \(39,41,44,45\) for \(L=12,13,14,15\), respectively, including the first-attainment gap and equality instance.

Running the supplied checker requires Python 3 standard library; the optional optimizer requires NumPy and SciPy. The finite enumeration is only corroborating evidence; the infinite quantification in alphabet size, message length, and list allowance is proved by the incidence inequalities and explicit graph factorizations in `RESULT.md`. No external independent audit has been performed.
