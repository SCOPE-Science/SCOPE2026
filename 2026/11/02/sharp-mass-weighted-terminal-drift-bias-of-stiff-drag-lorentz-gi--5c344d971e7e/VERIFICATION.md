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

The analytical proof in `RESULT.md` establishes the result for all finite species counts and positive coefficients. To reproduce the supplementary tests with Python 3 and no external packages, execute:

```sh
python3 verify.py
```

Expected output: `PASS: 236 exact-rational charged-dust instances; s*=0.429047164748; C*=0.174872575596`.

Checks: exact rational polynomial identities for the stability function and error rationalization; independently assembled one-, two- and three-species complex block matrices, exact inversions, exact forced numerical fixed points, exact error transfer functions, positive kinetic metric evaluations and the rigorous loose rational square bound \(\|W_{\rm fp}-W_*\|_Q^2<(7/40)^2\|W_*\|_Q^2\). The cubic maximum is isolated numerically after an analytic uniqueness argument. None of these finite cases proves the universal functional calculus inequality or uniqueness of publication priority. Only the analytic argument supplies the infinite quantifiers.

Independent mathematical validation has not been performed.
