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

# Verification notes

The analytic argument in `RESULT.md` proves the Bloch-norm expansion for all fixed \(n\ge3\) and centered zero splittings with first nonzero elementary symmetric sum \(e_k\), \(2\le k<n\). Its critical steps are a uniform rational Taylor expansion, strict radial localization near the norming circle, a cosine first variation, positivity via \(\operatorname{artanh}(x)/x\), and a fixed-mode degree asymptotic.

The independent finite arithmetic route in `checker.py` evaluates derivative perturbations of \(z^{n-k}(z^k-t)/(1-tz^k)\) and compares against the closed coefficient, tests signs and large-degree scaling, and checks non-real centered tuples numerically. It completed 572 deterministic assertions. To rerun: `python checker.py`, with `mpmath` installed. Finite checks do not establish the infinite quantifiers; their role is corroboration and fault detection.

No independent mathematical audit has been carried out. Historical priority may depend on results not included in the inspected full texts. The \(k=n\) regular-polygon (unicritical) case and uncentered directions are outside the claimed contribution.
