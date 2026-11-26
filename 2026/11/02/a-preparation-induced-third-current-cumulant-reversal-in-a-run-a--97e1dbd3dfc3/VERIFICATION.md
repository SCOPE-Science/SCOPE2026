---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At fixed disorder, a current contribution is a crossing Bernoulli variable. Taking its log-MGF first gives b₃(U_±) for qq, whereas orientation averaging first gives b₃(m) for qa. With d=(U_+−U_−)/2 the symmetric difference is (6m−3)d². The symmetric unbiased displacement law has 0<m<1/2 on 0<z<vt by the positive ballistic atom and the positive interior one-flip density. Near vt the two orientation-conditioned tails differ by a positive quantity (limit e^(−γt)), proving both strict signs claimed for every t>0. At z=vty, a single flip has uniformly distributed time conditional on its count; from +, crossings require flip after t(1+y)/2, and from −, before t(1−y)/2. Combining with the no-flip term and a uniform O((γt)²) two-or-more-flip remainder gives the stated first-order crossing probabilities. The qq and qa integrands at that order are −γty/2 and +γty/4, respectively, yielding −ρvγt²/4 and +ρvγt²/8. The compensated sign martingale has deterministic bracket 4γt and jumps of magnitude 2, giving the conditional Brownian limit for either sign. E[S_s S_u]=e^(−2γ|u−s|) for either initial sign bounds E[Y_t²] by v²t/γ, where Y_t is the free displacement. Thus the positive scaled displacements have uniformly small integrated tails, justifying passage to the spatial limit against |b₃(p)|≤p. For f=erfc, twice integrating by parts gives I_k=k/√π [1−2(k−1)/√π ∫e^(−2y²)f(y)^(k−2)dy] for k≥2 on y≥0. Evaluating at k=2,3 and taking I₁/2−3I₂/4+I₃/4 recovers C₃. It is positive from the limiting integral directly. Almost-sure continuity of the displacement and absence of interior crossing-level atoms give continuity after spatial integration, hence at least one finite sign reversal for qq.

## originality

PASS

The earlier exact generating functions already imply the Bernoulli-polynomial integral representations, and the Brownian CGF determines the limiting Brownian coefficient. The distinct result is the evaluated all-time strict comparison, opposite initial signs, and proof of a preparation-dependent negative-to-positive third-cumulant reversal in the stated telegraph gas.

## value

PASS

The theorem distinguishes two standard preparations of the same gas by a qualitative skewness phenomenon not decided by their common diffusive leading law. The strict all-time ordering and rigorous short/long sign comparison give a usable criterion for which preparation can exhibit negative third current cumulant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
