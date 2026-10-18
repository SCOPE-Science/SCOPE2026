---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For Φ(X)=sX+(1−s)Tr(X)σ the unnormalized Choi matrix J=s|Ω〉〈Ω|+(1−s)I⊗σ. Partial transpose decomposes into diagonal sectors and 2×2 |ij〉,|ji〉 blocks with determinant (1−s)²p_i p_j−s², hence PPT iff s≤√(p_(1)p_(2))/(1+√(p_(1)p_(2))). To prove sufficiency (not generally implied by PPT), average 3^d explicit product projectors using independent cubic phases with weights p_i^(−1/4),√s p_j^(1/4), yielding s|Ω〉〈Ω|+sΣ_{i≠j}√(p_j/p_i)|ij〉〈ij|. The residual J−S is diagonal with coefficients (1−s)p_j−s√(p_j/p_i)≥0 under precisely that PPT condition; all d≥3 and endpoint s=0/equality work. Semigroup s=e^(−γt) and Lindblad operators √(γp_i)|i〉〈j| establish exact first EB time. Independent complex-tensor computations through d=4 checked this finite separable decomposition and PPT eigenvalue signs.

## originality

PASS

Choi separability and the ordinary unital depolarizing EB threshold are classical and explicitly excluded. The literature inspection did not show the all-spectrum anisotropic two-lowest-eigenvalue EB cutoff nor the explicit cubic-phase decomposition. Specialized shifted-depolarizing paper by Baitenov (2024) could not be read in full: open/preprint attempts failed and authorized access returned VPN disconnected; this risk is explicit and does not, by itself, negate a best-of-knowledge originality PASS.

## value

PASS

Exact EB horizons are operational invariants for quantum noise channels. The full-rank arbitrary-dimensional reset model has a simple but previously unchecked dependence on the *two smallest* target populations; the proof provides an explicit separable Choi certificate establishing when PPT is sufficient despite generally failing at d≥3, not merely a generic threshold guess.

The dated certificate retains the supplied scientific assessment, sources and limitations.
