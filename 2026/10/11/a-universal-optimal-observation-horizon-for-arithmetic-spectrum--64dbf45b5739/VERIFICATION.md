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

# Reproducibility and scope

Run `python3 CHECK.py` with standard Python 3. No third-party software or downloaded datasets are needed. The checker uses exact fractions and rational Gaussian elimination for \(k=2,3,4,5\), \(q=1/2,2/3\), and the rate pairs \((a,d)=(1,1),(6,3)\). It checks 16 exact determinant identities. It also compares the exact two-time optimum against a numerical root, checks large-mode roots, and computes the limiting integral numerically. Expected text: `VERIFY_OK 31 exact_or_numeric_tests cstar=2.121467655793`.

The determinant identity for all \(k\), uniqueness of the D-optimal equal-mesh spacing, and universal horizon are proved symbolically in `RESULT.md`. Only the enumerated sample cases and approximate constant are computationally tested. A numerical agreement is not a certificate of any universally quantified step. Equal-variance independent sensor readings and a fixed arithmetic spectrum are assumptions, not consequences of the data.
