---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reassessed complete /workspace/repairs/3/RESULT.md, not the original wording. RESULT.md:22,32 of the frozen record overstate two implications: positive trace is not almost-sure nonselection, and the stable interval allows a zero multiplier moment q. For u=(4,5), v=(3,4), η=1/400 the samples (1,1),(2,2), of probability 1/16, hit x† exactly and stop, although 0<q<1 and the overall floor is positive. For u=(1,1), v=(1,1,1), η=1, q=0; the original risk rises from 1/3 to 2/3 only on the first update. The replacement gives the correct quantifiers and q=0 coverage. Independently, the scalar residual multiplies by 1−ηu_I²v_J² with square mean q. The nullspace-projected increment has zero conditional mean by uniform coordinate sampling and conditional covariance η²U₄s_k²H/c with H=Σv_j²(Pe_j)(Pe_j)ᵀ. Summing uncorrelated increments and adding the orthogonal residual component gives the two risk identities and the covariance. L² norms of the full increments are summable by q<1; this proves L² and almost-sure convergence and justifies the limiting moments. The sign of the increment of risk is the sign of (1−q)q^k(η−η_risk), and the residual-optimal step minimizes the strictly convex quadratic q. The repaired normalized-step scope is valid since U₄/U₂≤max_i u_i². Direct substitution for the original two-row example gives q=65/128 and F=17/126; scaling the data scales the coupled iterates and the two stopping limits hold. The original verifier was inspected, not executed, and its finite path counts do not prove convergence. The new absorption witness is verified by its two rational updates in the repaired file.

## originality

PASS

Assessed the repaired arbitrary-v, full-covariance and constant-step frontier claim. The same two-row example/floor and an entire all-ones scalar risk subfamily have direct published coverage, acknowledged in the replacement. Neither that coverage nor the other checked sources supplies the general-v covariance and threshold comparison. This is best-of-knowledge, not exhaustive priority.

## value

PASS

For this standard residual-fitting rule the full covariance describes where unresolved reconstruction error persists, not just how the scalar residual decays. The sharp frontier and divergent floor give a quantitative distinction between choosing a step for residual and for reconstruction across weighted rank-one problems. The repaired scope separates this broader stability phenomenon from the counterexample within the conservative bound and does not rely on the already covered all-ones example for its scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
