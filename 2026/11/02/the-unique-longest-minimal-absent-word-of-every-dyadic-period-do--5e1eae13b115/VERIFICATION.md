---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The period-doubling substitution μ(0)=01, μ(1)=00 produces two halves of P_j agreeing except for their last letter. Every one occurs at an odd position and there is no 11 or 0000, so two identical length≥4 factors start with the same parity. Induction on the substitution level shows all length-h factors of P_k are distinct and the unique repeated length-(h−1) factor is Q_k at starts 0,h. A minimal absent word of length ℓ≥3 has both length-(ℓ−1) borders present but its interior must repeat at different starts, forcing ℓ≤h+1. The left/right contexts of Q_k permit only c_k Q_k c_k absent with both borders present. For all k≥3, c_k=(k−1) mod2; no circular or arbitrary-prefix claim.

## originality

PASS

Qualified PASS: exact witness word existed in earlier lower-bound work and is not claimed new; the assessed theorem adds sharp upper bound and uniqueness at every dyadic length. The same-period-doubling attractor paper establishes two-half and parity structural identities, but the inspected complete section does not claim the maximal minimal-absent-word classification. Automatic-sequence factor and MAW algorithm papers cover different implications.

## value

PASS

Minimal absent words are canonical string reconstruction and combinatorial fingerprints; an all-level exact extremal length and unique witness for a natural automatic sequence gives a nontrivial boundary classification, not an arbitrary finite sequence of computed numbers. Repeated-factor induction is independently mathematically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
