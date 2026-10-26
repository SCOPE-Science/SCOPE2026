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

# Reproducibility and scientific limits

Run `python3 verify.py` in a directory containing the embedded standalone Python script. No packages beyond the Python 3 standard library are needed.

The script computes the cumulative binary digit deficit directly by summing \(2\,s_2(n)-\operatorname{bitlength}(n)\) without using the Takagi formula. It checks exact minima and the complete predicted sets of attaining indices in seventeen complete shells. Independently, it evaluates the finite tent series defining \(2^\ell\tau(j/2^\ell)\) entirely in integer arithmetic and checks the maximum and full argmax set for every \(1\leq\ell\leq15\).

The script was executed successfully from the packaged source. Finite enumeration is not offered as a proof for unbounded depths; the all-depth assertions follow from the functional-equation and prefix-induction proof in RESULT.md. No external or independent audit has been performed.
