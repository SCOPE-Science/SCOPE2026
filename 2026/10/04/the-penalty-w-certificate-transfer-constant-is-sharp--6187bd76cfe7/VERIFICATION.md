---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the affine example, the separated penalty model is exact. On the radius interval centered at the reference point, the base penalty model has slope \(\gamma/2\), so its normalized Wolfe residual is exactly \(\gamma/2\); the feasibility inequality also holds with equality. Replacing \(\gamma\) by \(\tilde\gamma>\gamma\) changes the slope and exact residual to \(\tilde\gamma-\gamma/2\). The feasibility lower requirement is only \(\tilde\gamma/2\), so the Wolfe residual is the active minimum tolerance. Substituting \(\nu=\gamma/2\) into Proposition 4.3 gives exactly the same value. The package verifier checks these identities over exact rational test cases, and I independently reconstructed the algebra from Definition 3 and the proposition statement.

## originality

PASS

The complete relevant portion of Lin--Zhang's primary preprint was inspected through authorized PDF access after open full-text retrieval failed. Definition 3 gives the two certificate inequalities, Proposition 4.3 states the transfer tolerance \(\nu+2\nu(\tilde\gamma-\gamma)/\gamma\), and its detailed proof gives an upper bound by model monotonicity and feasibility. The surrounding remarks motivate the transfer but do not claim sharpness or give an equality example. Exact searches found no follow-up sharpness result.

## value

PASS

Proposition 4.3 is the mechanism that preserves certificates while the algorithm changes its penalty estimate. Showing its deterioration coefficient is genuinely unavoidable establishes that the parameter-update analysis cannot be uniformly improved by tightening that step alone. The one-dimensional affine example is simple because it is an extremal sharpness certificate, not because the constant is unmotivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
