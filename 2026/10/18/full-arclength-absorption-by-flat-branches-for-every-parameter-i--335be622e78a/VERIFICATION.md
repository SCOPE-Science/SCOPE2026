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

The mathematical claim is proved in RESULT.md by a transfer-operator and bounded-variation argument; infinite-time convergence is not inferred from finite tests.

1. Analytic checks: for each fixed iterate \(r\) the surviving affine-branch partition is finite; every slope is at least \((\sqrt2)^r\); endpoint traces yield the explicit inequality \(\operatorname{Var}(K^r h)\le3\cdot2^{-r/2}\operatorname{Var}(h)+C_r\|h\|_1\). At \(r=4\), the contraction coefficient is \(3/4\). Bounded variation compactness, transfer invariance and density of the hole-preimage set finish the contradiction.
2. Source-dependent hypotheses: arXiv:2410.01052v2, Theorem B, Lemmas 21–22, Proposition 23, Theorem C. The exact full-source graph case census is not independently replayed here.
3. Artifact check: execute `python3 check_branches.py` using ordinary Python 3. This checks the four quadrant matrices, all sixteen direction images and the displayed contraction coefficient with integer arithmetic. It does not replace the infinite proof.
4. Priority comparison: arXiv:2503.02411v4, Theorem 3 (formerly Theorem 2 in v1), proves full arclength only on specified parameter intervals; this theorem extends those intervals. An earlier restricted \(2\le b\le4\) calculation is not claimed as new.

Independent audit has not been performed. No formal proof assistant or external certification was used.
