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

Run `python3 checks/verify.py` from the package root with standard Python 3. It prints twelve `CHECK_OK` lines and ends with `VERIFY_OK`. No third-party packages, internet access, or random inputs are needed.

The checker enumerates both quadratic Gauss signs and both level choices for every dimension parameter \(m\in\{1,2,3\}\). It evaluates all time-frequency ambiguity coefficients as exact signed integer sums and checks the six analytic amplitude cases, class multiplicities, symmetric-domain rank and zero-pattern count. In each \(16\)-dimensional design instance, it independently constructs all \(256\) real Gabor window vectors and verifies the full lift-second-moment identity on all \(136\) real symmetric matrix basis elements, using integers only.

The mathematical proof in `RESULT.md` treats every binary dimension parameter and every nondegenerate quadratic form. The finite program corroborates these statements but cannot replace that universal argument. The projective design identity follows from an explicit operator equation rather than numerical sampling. No external audit is reported.
