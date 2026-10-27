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

# Reproducibility

Run `python3 verify.py`. Only Python's standard library is required. The program prints `PSEUDOPERIOD_13_CYCLIC_PASS` if all assertions succeed; it otherwise raises an exception.

The first test independently constructs all indexed binary words of circumferences \(1\) to \(18\), directly evaluates the original periodic pseudoperiod condition and the cyclic transition number, and compares with the proposed coefficient formula. This comprises exactly \(524{,}286\) words. A second test independently constructs cyclic difference vectors for circumferences \(1\) to \(14\) and checks the forbidden-triple equivalence. Two more tests compare the exact coefficients against direct four-state polynomial-matrix traces through \(70\), and a separately implemented cubic Newton-sum recurrence through \(180\).

The universal binomial count, generating function, zeta function, primitive-orbit formula, and spectral asymptotics are proved mathematically in `RESULT.md`; finite checks cannot certify statements beyond their enumerated domains. Literature coverage and novelty remain subject to independent inspection. No independent audit has been performed.
