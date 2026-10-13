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

# Reproduction and proof boundaries

Run `python verify_product_u4.py` using Python 3 without nonstandard packages. The verifier implements \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), checks all targets through effective-coordinate enumeration over \(q=2,3,4,5\), and independently performs full-matrix multiplication over \(q=2,3\). The expected terminal marker is `VERIFY_OK_PRODUCT_U4`.

The four-case argument in `RESULT.md` proves the theorem for arbitrary prime-power \(q\), including nonprime extension fields and all zero/nonzero patterns of \((u,v,w)\). Exhaustive finite experiments prove only their stated finite instances and are not evidence of independent or infinite verification. No external independent audit has been performed.
