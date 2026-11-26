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

The diagonal phase change reduces λ to r=|λ|, with the full operator only multiplied by a scalar of unit modulus. In the adjoint the left tail rows use precisely the coordinates n≤0 and the right rows use n≥1. On the left the vector (βy_{n+1})_{n≤−1} has norm β times the full left-half norm, and (ry_n)_{n≤−1} has norm at most r times it; on the right (ry_n)_{n≥1} has norm r times the full right-half norm and the shifted term has norm at most α times it. The reverse triangle bounds therefore give δ=min(β−r,r−α) without using the interface row. Expanding each half yields the published gradient and boundary terms, which are nonnegative beyond δ² times the squared norm. Equality forces both half-lines constant, hence both zero in ℓ². Blocks supported strictly within either tail have squared quotient (w−r)²+2rw/L, so the lower bound is sharp without a minimizer. A bounded-below adjoint implies closed and dense range for B. The kernel recurrence fixes both geometrically summable tails from x₀ and yields exactly one free parameter. The positive inverse (BB*)⁻¹ gives the stated norm for B†, and norm attainment would give a bottom eigenvector of BB*. Perturbations of norm less than δ preserve the positive adjoint bound. Replacing a nearest full tail by weight r costs exactly δ and makes long phase-matched adjoint blocks have norm tending to 0, ruling out surjectivity. Either tail works at the midpoint. Independent replay `python3 /workspace/branches/frozen_replay.py 5` checked both ordinary and critical-tail squared quotients for complex λ=3+4i, multiple interfaces and lengths 1–6.

## originality

PASS

The exact defect-independent bottom of BB*, its nonattainment, and a nearest non-surjective shift obtained by changing just one constant tail are the supported contribution. Classical step-shift examples and shadowing or surjective-spectrum theorems supply qualitative structure, not this modulus for all interface weights. The norm of the right inverse, the numerical distance once the modulus is known, and existence of some nearest perturbation among unrestricted bounded operators are not in themselves novelty. The corpus match computes a different quantity, the two-sided ℓ_p shadowing constant for a step shift.

## value

PASS

Two opposed constant tails are the natural model for an annulus of eigenvalues on which T−λI is still onto. The exact margin quantifies the largest guaranteed norm-stability radius, and invariance even under arbitrarily large or small single-link weights is not explained by the qualitative spectrum or by tail symbols alone. A nearest perturbation inside the same simple shift family specifically identifies how surjectivity fails at that radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
