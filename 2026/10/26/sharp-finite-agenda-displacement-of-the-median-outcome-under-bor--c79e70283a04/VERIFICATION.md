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

# Exact verification

Run `python3 verify.py` using the Python 3 standard library. It deterministically outputs JSON, compared without approximation to the included `certificate.json` (JSON key ordering and indentation agree). The script uses independent brute-force generation of valid strict single-peaked orders, direct verification of within-side monotonicity, exhaustive anonymous preference profiles in thirteen finite parameter regimes, and independent construction checks for 1960 parameter pairs. In all exhaustive regimes, the observed largest median-to-unique-Borda-winner distance matches the formula exactly.

The proof of unrestricted parameter ranges is **analytic**: at least \(r+1\) voters impose a rank-loss of at least \(d\), and the remaining at most \(r\) voters can offset it by at most \(m-1\) each. An explicit two-order construction attains the resulting sharp integer bound. No numerical or finite test is used to infer a theorem for larger parameters. The separate manuscript states the exact hypotheses, strict-tie boundary and known bibliographic limitations.

Independent scientific audit and independent validation have not been performed.
