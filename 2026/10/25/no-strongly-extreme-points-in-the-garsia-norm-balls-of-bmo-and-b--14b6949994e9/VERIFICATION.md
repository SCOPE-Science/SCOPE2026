---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For a Garsia-unit function f in L², choose a common Lebesgue point ζ for f and |f|². Nontangential Poisson convergence yields Vf(z)=P|f|²−|Pf|²→0 in each Stolz cone at ζ. For a=rζ the disk-algebra function g_a=b_a+a has Poisson variance 1−|b_a|², norm exactly one, and its ε-superlevel sets are images of bounded pseudohyperbolic disks lying uniformly inside a Stolz cone tending to ζ. Hence Δ_r=sup_z min(Vf,Vg_a)→0. Centered Poisson L² triangle inequality gives ||f±g_a||_G<=1+sqrt(Δ_r), while both ||f|| and ||g_a|| equal one. Thus unit perturbations make both signed norms tend to one, contradicting strong extremity for every boundary point in all four spaces. No unsupported norm equivalence is used; analytic g_a belong to all four. Source checks/check_geometry.py inspected and the localization/Möbius algebra was independently reconstructed; finite sample checks are not proof for arbitrary f.

## originality

PASS

Dyakonov 2026 explicitly raises the strongly extreme Garsia ball question in Section 2 without resolving it; his 2025 Theorem 2.7 / Corollary 2.8 classify ordinary extreme points and make the VMO phenomenon particularly notable. For BMO-type arc-average norms and H-infinity sup norms, strong extremity differs from the Poisson-variance Garsia norm. The submitted construction answers the exact stated strongly extreme variant and is not a corollary of the earlier ordinary extreme statements.

## value

PASS

Answers an expressly formulated strongly extreme variant of a named Garsia-norm ball problem for four standard analytic/harmonic spaces with a simple but nontrivial boundary-concentration construction. It separates strong extremity from the known ordinary extreme VMO unit sphere, an informative geometric rigidity distinction, rather than restating a textbook implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
