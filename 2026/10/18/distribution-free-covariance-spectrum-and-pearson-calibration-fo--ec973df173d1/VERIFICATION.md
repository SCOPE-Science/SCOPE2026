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
# Verification and limits

`verify.py` is included alongside this file. Run `python verify.py` using a standard Python 3 interpreter. It uses `fractions.Fraction`, `itertools.product`, and exact sums to enumerate \(X_1,\ldots,X_{L+1}\) for \(q\in\{2,3,4\}\) and \(1\le L\le4\) under five different positive categorical laws. It checks direct enumeration against the covariance formula and all four eigenmode families, as well as the Pearson-trace formula. The recorded successful result is `VERIFY_OK 1988 exact rational assertions`.

The theorem for unrestricted \(q,L\) is proved analytically by the orthogonal-score decomposition, exact covariance structure, and standard finite-range central limit theorem. Enumeration is finite corroboration only. The statement does not address zero-probability categories, non-iid sequences, estimated probabilities, or increasing alphabet sizes. Priority assessment is restricted to inspected evidence and is not an independent certification.
