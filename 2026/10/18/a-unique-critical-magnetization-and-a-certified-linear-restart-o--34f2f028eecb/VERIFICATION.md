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

# Verification instructions and limitations

`verify.py` is self-contained and should be run with `python3 verify.py` in the unpacked package directory. The script computes fixed-point enclosures using integer arithmetic, with certified outward rounding at every multiplication and division. It encloses \(\log 2\) via a positive alternating-hyperbolic expansion, constructs the first three absorption-time moments through positive-series recurrences, and adds rigorous estimates of every omitted tail.

It asserts the strict threshold sign change at \(0.63058\) and \(0.63062\), an enclosing interval showing \(B(m_c)>0\), and finite positive bounds for the emerging local minimum's slope. The uniqueness and implicit-function steps are analytical arguments in RESULT.md rather than inferred from sample calculations. Higher-precision approximate decimals are auxiliary only.

The verification does not simulate an infinite state space, establish a global minimum in reset intensity, certify historical priority, or assess the finite-population scaling error. Independent audit: not performed.
