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

Final repaired RESULT.md: both deterministic maps preserve the cube and lie below Bp by the union bound and the nonnegative reinfection losses. Using the positive left Perron vector, mass is nonincreasing and strictly drops in two steps from every nonzero state: a positive coordinate persists, an adjacent coordinate becomes positive, and then the corresponding p_i q_i loss is positive. Compactness excludes a nonzero limit of the mass. The non-Perron eigenvalues of B are 1-δ+βλ for non-Perron eigenvalues λ of A and lie strictly inside the unit disk even if λ=-ρ, since δ<1. With a=wᵀp and r=p-av, positivity bounds ||p|| by a constant times a. The projected linear recurrence for r/a is a strict contraction with forcing O(a) because a'/a→1, whence r/a→0. Expanding the product through degree two gives projected losses δ(1-δ)S+T and δS+T. Thus 1/a'-1/a→κ in each map, and Cesàro yields the exact per-vertex limits; the ratio for arbitrary separately evolved nonzero initial conditions follows and is strictly above one. The repair corrects the eigenvalue label in the original proof and the ancillary endpoint overstatement: at δ=β=1 on the two-vertex graph, symmetric WOR u'=u(1-u) gives t u_t→1 for 0<u_0<1 by reciprocal increments, but u_0=1 becomes zero in one step. The theorem itself excludes that endpoint and is unchanged. A bounded independent replay used an incremental union probability and confirmed the six finite diagnostics to relative error at most 0.000181; this is not the asymptotic proof.

## originality

PASS

Credit only the reviewed WOR equality-case amplitude and strict two-model critical relaxation comparison. The common WIR/WOR linear threshold and prior WIR bifurcation curvature were already known, and the strongest distinct indexed result gives the exact same single-model WIR law. The repaired literature paragraph explicitly credits this overlap. Neither the matching indexed WIR theorem nor the inspected primary sources establish the additional WOR critical amplitude and the pairwise comparison on all scoped graphs. This is a bounded statement-level assessment, not a claim of historical priority.

## value

PASS

With an already shared linear threshold, the natural unresolved comparison is whether the two modeling conventions also agree at critical time. The reviewed result proves that their relaxation amplitudes differ by a strict, normalization-consistent amount for every connected graph in scope and every nonzero start; the effect can yield a divergent amplitude ratio at the two-vertex boundary. This quantitative distinction is not apparent from the common linearization and remains useful even though WIR by itself is already covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
