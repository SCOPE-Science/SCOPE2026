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

`VERIFY.py` uses the Python 3 standard library and requires no data files. Run it as `python VERIFY.py`. It checks all explicitly labelled functions through literal graph neighbourhoods independently of the nine-type formula; the two approaches yield identical full weight polynomials for graph orders indexed by \(2\le n\le7\). It also evaluates the independent binomial minimum-count expressions, giving the exact sequence \(1,10,84,900,3280,44100\) for these orders. Six complete polynomial comparisons and six minimum-count comparisons passed. All computations are finite confirmations of the algebraic proof, not proof of the unrestricted theorem. No other formal or independent validation has been performed.
