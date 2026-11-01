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

## Reproducibility
Run `python verify_sections.py` from the directory containing that file with Python 3 and the NumPy, SciPy, and SymPy packages installed. This verifies exact symbolic derivatives and limiting coefficients and independently compares the integrated angular formula to separate two-dimensional angular quadrature on multiple polygonal bases, including an asymmetric triangle. It also checks the fixed-perimeter inequality, a width-variance stability instance, the segment endpoint limit, the disk conditional ellipticity law, and a direct invariant joint plane/offset rejection simulation on disk, square, and asymmetric triangle bases. A successful run ends in `ALL_CHECKS_PASSED`.

## What is and is not verified
The mathematical proof establishes the full class of convex bases and all positive heights. The numerical cases do not replace the zonoid representation, the equality classifications, the strong-convexity argument, or the analytic limiting laws. Literature comparisons document accessible sources and residual priority uncertainty, without claiming an independent validation.
