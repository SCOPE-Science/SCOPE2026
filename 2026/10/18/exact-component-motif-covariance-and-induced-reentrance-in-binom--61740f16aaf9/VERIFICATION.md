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

The complete supporting program is `verify.py`, using only the Python standard library. Run `python verify.py` in the same directory as this document. The verification enumerates every labeled graph on two through five vertices, enumerates designated six small connected isomorphism classes, and computes exact rational mixed moments for both the induced and the edge-subgraph copy conventions and four rational values of the edge probability. The script checks 660 exact equalities and strict-sign conditions.

The script is a finite consistency check; it does not verify the proof's quantifiers for arbitrarily large graph orders. The all-size claims depend on conditioning on a component vertex set, factorization of the untouched complement, covariance linearity, and elementary monotonicity of \(p^e(1-p)^q\). Asymptotic root scales follow from the displayed polynomial equation, not numerical extrapolation. Independent scientific validation has not been performed.
