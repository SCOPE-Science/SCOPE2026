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

The analytic proof uses only the standard Hermite product identity, a triangular-to-Vandermonde argument, elementary real two-view linear algebra and divisibility of integers. The claimed rank formula holds for all dimensions in the stated range; the finite checks below are reproducibility checks, not an exhaustive infinite certificate.

`checker.py` computes the coefficients of the indicated Hermite products exactly, verifies their rank modulo the prime \(1000000007\), then constructs explicit Hermitian measurement matrices at angles separated by \(\pi/r\) and \(\pi/(2r)\), in exact integer arithmetic. It verifies seven \((d,r)\) pairs, dimensions \(2\) through \(7\) at the sufficient gap boundary and \((4,4)\), and fourteen resonant two-angle cases, plus a separate nonresonant exact algebraic rank test at \(d=4,r=4,\Delta=\pi/16\). `checker_output.txt` is the recorded successful output. Run using Python and SymPy as specified in `requirements.txt`.

**Limits.** The modular rank checks establish the displayed lower bound on rank for the finite cases but do not imply the general algebraic theorem; the independent upper bounds come from the explicit measurement matrix. These checks do not quantify finite-shot statistical error or the conditioning of inversions near resonant phase differences. The source comparisons do not constitute independent novelty or correctness certification.
