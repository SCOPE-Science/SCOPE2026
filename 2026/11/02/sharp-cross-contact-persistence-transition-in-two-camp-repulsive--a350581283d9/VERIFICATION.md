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

Kann–Feng equations (3.1)–(3.2) give the stated strict threshold, negative-edge force and self-loop normalization (RESULT.md's reference to equation (3) is imprecise). In the active regime the homogeneous camps are invariant because all vertices in a camp have the same signed degrees. Updates of the lower and upper opinion are respectively −α(c−d) and +β(c−d); the deficit is therefore multiplied by 1−η. For 0<η<1 this gives positive geometrically decreasing deficit at every finite iterate. If η≥1 the first iterate is at or beyond c; the next update uses only identical-opinion within-camp neighbors and the system freezes, without continuing the active recurrence. For η>1 the normalized overshoot is strictly below 1 since both degree fractions are strictly below 1 and d0>0. Connected negative K_{m,m} with d0/c→0 realizes the supremum; the positive cliques with a negative matching or all negative cross edges realize the other phases. The proof in RESULT.md lines 14–25 works also for unequal camp sizes. I inspected VERIFICATION.md and verify_signed.py without running them; the latter implements the edge updates directly with fractions on 30 symmetric examples, advancing 22 steps with assertions inside the loop, not a general proof.

## originality

PASS

The comparison supports the general sign-biregular degree-ratio trichotomy and sharp one-step excess, not the generic fact that strict-threshold contacts may differ at a limit. The complete signed network threshold contains an exactly overlapping boundary case, which is not credited separately.

## value

PASS

This natural homogeneous two-camp class isolates when mixed-sign graph structure leads to persistent links or actual finite-time contact loss. Exact boundary, realizability of all three phases and the sharp nonattained maximum of the one-step excess make the classification useful beyond observing a linear active-regime recurrence. It also separates a dynamical limit from evaluation of the strict threshold at that limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
