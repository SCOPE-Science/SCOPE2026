---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The update is invariant under rescaling s. For unit s put q=sᵀHs and m=||Hs−qs||. When m>0 the only nonidentity block has diagonal q, 1+m²/q and off-diagonal m; it has positive determinant q and det(I−block)=−m²/q, so its eigenvalues straddle the extra ones and are the full spectral extremes. The spectral inequality H²≤(κ+1)H−κI yields m²≤(q−1)(κ−q), sharp at fixed q by endpoint spectral weights. The block's eigenvalue ratio is monotone in trace/√q, and the sharp envelope (κ+2−κ/q)/√q has derivative [3κ−(κ+2)q]/(2q^(5/2)). Its unique maximum for κ>1 is at q*=3κ/(κ+2) in the open interval, realized by weight 2/(κ+2) on the upper endpoint. Its value 2(κ+2)^(3/2)/(3√(3κ)) equals √Γ+1/√Γ and gives the stated Γ using (κ+2)^3−27κ=(κ−1)^2(κ+8). The value at q=κ corresponds to condition κ, so the strict interior maximum exceeds κ. The case m=0 cannot beat κ, and κ=1 gives B₁=I. Expanding the numerator gives the stated 4κ²/27 leading term. The κ=4 witness has trace 4 and determinant 2, giving 2±√2. The extremizer extends by identity blocks and is realizable under exact line search from gradient −s because only the direction matters. The proof, not the supplied finite rational/decimal checks, establishes all dimensions; uploaded code was inspected without execution.

## originality

PASS

The exact maximization for the ordinary direct update with the initial scalar fixed at the lower curvature is distinct from the checked classical formula, conditioning-based choices of update, and the accessible one-step trace-potential criterion. The supported claim is the attained worst spectral condition number at a prescribed curvature ratio, not BFGS positivity or the idea that poorly sized updates can hurt conditioning.

## value

PASS

The scale choice and condition-number comparison are natural in a secant update, and the extremum reveals a specific pathology rather than just positivity or an arbitrary example: a perfectly conditioned estimate can overshoot the target curvature ratio on the very first exact-line-search-compatible step, and the sharp growth is quadratic, not linear. The endpoint eigenspace characterization gives a reproducible adversarial case even in two dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
