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
# Verification record

The theorem is proved analytically through the rational generating function, a short exact interlacing recurrence for simple negative roots, and endpoint/product-sign classification at \(s=-1\). The exceptional character \((q,r)=(2,1)\), the boundary collision \(q=2r+4\), and the forced central zero when \(r>0\) are all separated in the argument.

The executable `verify_cyclic_bergman.py` rederives the cubic using formal power series, checks endpoint identities symbolically, and evaluates exact rational coefficient and Sturm tests for \(1770\) parameter pairs with \(2\le q\le60\). Its actual recorded stdout is `verification_cyclic_bergman.txt`. The finite checks do not prove the infinite-parameter theorem; that depends on the displayed analytic proof. These checks are not an independent audit.

Limitations: the proof treats weight exponent \(2\) and scalar cyclic character spaces on the disk only. Negative real-rootedness has broader antecedents; historical publication priority of the finer attainable zero-orbit transition has not been independently certified.
