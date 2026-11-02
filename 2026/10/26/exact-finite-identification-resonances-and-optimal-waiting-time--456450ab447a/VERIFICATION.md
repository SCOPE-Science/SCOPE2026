---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed the ProxSkip Algorithm 1 normal/tangential decomposition on every finite-dimensional proper affine subspace under an isotropic quadratic and normal-initialized control. At a successful prox step normal displacement becomes zero; between successes the normal trial displacement is gamma*S_j(c)*v, giving successive exact multipliers 1-p*S_j(c). Strict growth of S_j proves that a multiplier vanishes iff p=1/S_m(c) for exactly one integer m>=2. I.i.d. geometric inter-success gaps yield a.s. finite normal absorption precisely on those resonance curves and infinitely many feasibility exits off them for nonzero normal error. First matching gap has probability s=p(1-p)^(m-1), generating function s*w^m/[1-p*w/(1-(1-p)*w)+s*w^m], mean 1/[p^2*(1-p)^(m-1)]. For m=2 the mean (1+c)^3/c uniquely minimizes at c=1/2, p=2/3 to 27/4; m>=3 has mean >=16. Independently recalculated 30 exact-rational finite gap recurrences in three resonance settings, showing the recurrence and zero condition. Those cases do not prove the infinite-a.s. statement; geometric renewal and recurrence do. Finite identification is normal feasibility/control, not finite tangential optimizer convergence.

## originality

PASS

The statement-specific finite-absorption resonance, renewal law and global optimal waiting parameters are not part of the inspected ProxSkip convergence theorem. The elementary geometric first-hit calculation and individual deterministic proximal-identification phenomena are prior tools, so the originality assessment is limited to the exact combination for this randomized method, not those tools.

## value

PASS

Exact finite-time feasibility is qualitatively different from expected asymptotic Lyapunov contraction, and the discrete resonance curves plus universal 27/4 optimum diagnose a meaningful finite-precision/tuning boundary for randomized proximal algorithms. The result has a justified optimization motivation despite the deliberately simple affine-quadratic family; no general-purpose runtime optimality claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
