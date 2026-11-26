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

The proposed radial moment polynomials vanish on the boundary, are regular at the center, and substitution using Delta r^2=2d and Delta r^4=4(d+2)r^2 gives the Dirichlet equations for the first and second unreset exit moments. Their averages are R^2 a/(2dD) and R^4(4a+db)/[4d^2(d+2)D^2]. With common iid launch and relaunch laws, the attempt survival transform Phi gives renewal mean (1-Phi)/(lambda Phi); the finite second moment suffices to differentiate at zero, obtaining mean squared minus half the second moment. A fixed U yields bracket U[4-(d+4)U], so the first-order non-improving core is exactly U>=t=4/(d+4). The pointwise chord bound U^2<=(1+t)U-t on [t,1] gives the sharp bracket upper bound (a-t)[d-2(d+2)a]. The maximum possible second factor on this interval is (d^2-4d-16)/(d+4), negative through d=6 and positive from d=7. Endpoint mixtures attain the chord and give the printed strict q interval; direct rational substitution at d=7 gives 217/75625. Upward perturbation of the lower endpoint preserves strict improvement of the mixture while both components have strictly positive mean derivative. At equality the first derivative alone makes no finite-rate claim. This checks RESULT.md lines 28–65 for arbitrary laws, including atoms and angularly anisotropic laws. The recorded exact-fraction and optional Bessel-transform checks in verify.py were inspected, not rerun.

## originality

PASS

The distinct claim is the sharp d=7 cutoff for a reversal by some heterogeneous law supported wholly on the deterministic first-order non-improving core. Neither the renewal criterion, the radial moments, nor their direct averaging is credited as an independent novelty.

## value

PASS

Determines when spatial randomization can reverse the local effect of restarting despite every allowed fixed placement being first-order ineffective. The exact threshold and the exhibited two-radius mixture distinguish an impossibility over all laws from a genuine design option. This is meaningful beyond evaluating the known restart criterion at a chosen radius, without promising a globally optimal rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
