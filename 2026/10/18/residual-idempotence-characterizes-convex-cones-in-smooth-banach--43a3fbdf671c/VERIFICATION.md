---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The smooth duality J(x)=D||x||²/2 gives the necessary/sufficient variational inequality P_K(z)=q iff ⟨J(z−q),k−q⟩≤0 for every k∈K (using convexity, differentiability and Chebyshev uniqueness); it includes zero residual. Assuming 0∈K, first inequality with k=0 at x,p forces ⟨J(r),p⟩≥0; testing P_Kr=0 against k=p forces ≤0. Conversely zero pairing implies ⟨J(r),k⟩≤0 for all k∈K and thus P_Kr=0. If R²=R, evaluating y∈K gives R0=0 and 0∈K. For each y∈K and t>1, at x=ty the idempotence criterion plus variational inequality k=y yields ||r||²=t⟨J(r),y⟩−⟨J(r),p⟩≤0, so ty∈K; convexity gives 0≤t≤1. Conversely if K is a cone, use comparison points 0 and 2p in K to force exact pairing zero, hence R²=R. In independent one-dimensional boundary tests K=[0,1] fails at x=2 and K=[0,∞) succeeds; proof not based on finite checks.

## originality

PASS

Domokos–Marsh full paper establishes standard duality inequalities and projection behavior for sets assumed cones, whereas the new converse classifies a previously unknown K from an idempotent residual. The contemporary Kumar–Bin Abu Baker–Botelho paper addresses nonlinear idempotents and is the most plausible stronger prior source; only abstract-level necessary-condition coverage was accessible. Full text was blocked, including authorized institutional access (Oxford VPN disconnected), so priority is explicitly provisional and not declared certified.

## value

PASS

The paper-defined nonlinear residual bi-potency problem has a natural structural answer over a broad real smooth Chebyshev class, including non-Hilbert ℓ_p and unpointed cones. Characterizing the exact geometric condition on unknown K, not just supplying necessity, is a useful complete classification with a pointwise duality test; it is not asserted as a new general projection method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
