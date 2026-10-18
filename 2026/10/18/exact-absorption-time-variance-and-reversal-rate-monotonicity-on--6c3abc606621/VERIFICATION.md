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

# Reproducibility and verification

`verify.py` constructs a \(2n\)-state transient Markov generator including both headings at the absorbing site and directly computes first and second absorption moments from the backward equations. For every \(3\le n\le40\), every site, and reversal rates \(0\), \(0.23\), \(1\), and \(7\), it compares the computed mean and fair-heading mixture variance with the theorem using \(\kappa=1.7\): 3,268 checks. Numerical checks substantiate only these finite cases; the analytic proof solves arbitrary \(n\ge3\), \(\lambda\ge0\), \(\kappa>0\).

The coupled heading-resolved first/second-moment identities were separately checked by symbolic polynomial substitution, including the incoming site-zero boundary. No external independent audit was performed.
