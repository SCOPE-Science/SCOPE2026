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

# Verification methods and limitations

`verify.py` is a complete standalone Python 3 script using only the standard library. Run `python verify.py` in the directory containing the script. It generates exactly specified rational initial opinions and implements both simultaneous opinion updates and the two branches of dyadic confidence updates. It separately computes the predicted first recovery time from exact rational inequalities rather than comparing floating-point logarithms.

The script compares actual and predicted receptive edge sets, absent-edge separation and confidence, the degree-weighted invariant and both modes of consensus. It checked \(n=3,\ldots,12\), four heterogeneous mediator configurations per size, six decay factors per configuration, and three reinforcement choices (720 complete trajectories). All 720 checks passed; 360 trajectories retain the missing edge forever and 360 exhibit finite reactivation. The critical equality is explicitly included. The non-symmetric four-agent example also passed at the threshold and above it.

Finite exact-rational trajectories support the explicit recurrence and catch boundary/normalization errors, but they do **not** establish a claim for infinitely many population sizes. The general induction, invariant weighted mean and strict threshold proof are in `RESULT.md`. These checks do not establish mathematical priority; available bibliographic comparisons and residual access limitations appear in `REVIEW.md` and `AUDIT.json`. There is no independent external audit.
