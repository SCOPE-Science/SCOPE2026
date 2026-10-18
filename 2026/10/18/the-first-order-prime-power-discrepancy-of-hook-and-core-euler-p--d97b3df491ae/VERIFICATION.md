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

The theorem follows from the explicit coefficients of the formal \(p\)-adic logarithm of a quotient of Euler products. Its only analytic-looking steps are identities of formal series; no numerical limiting procedure is required. The valuation estimate \(k(a+1)-\nu_p(k!)\ge a+2\) for \(k\ge2\) certifies exponential truncation, including the dyadic boundary.

Run `python3 verify.py` from the directory containing this document and the accompanying verifier. The program uses exact integers and only the standard library, checking the nine specified \((p,a)\) cases at all degrees through \(96\). Its observed output is `VERIFY_OK cases=9 coefficients=873 max_index=96`. No finite check certifies the infinite claim by itself. The original motivating preprint could be compared only at abstract level; its unseen body remains an originality risk. Independent audit is not performed.
