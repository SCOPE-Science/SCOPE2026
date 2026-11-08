---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Automaton acceptance separation is equivalent to A^a B^b != B^b A^a for some permutations. Power-generated H_t is normal; H_t=1 iff L_m|t. For m>=5 every nontrivial normal subgroup of S_m contains nonabelian A_m, so pairwise centralization fails; for m=3,4 the abelian A_3 and V_4 cases give the listed exceptional congruences. The function L_m increases precisely at prime powers, and explicit exponent witnesses prove the least-degree spectrum. For q>=7, failure at q−1 forces an exponent multiple of L_{q−1}, yielding sharp length and uniqueness. Exhaustive independent S3–S5 residue-pair checks corroborate, not replace normal-subgroup proof.

## originality

PASS

The S3 x²y²=y²x² identity, S_m normal-subgroup lattice, symmetric-group exponents, and general permutation-word separation were known. The relevant full 2017 paper studies other shortest identities and general lower bounds; it does not present an exhaustive two-block parameter criterion, all attainable least state counts, and sharp word-length optimization. Best-of-knowledge PASS with 2026 Xu–Regan and other group-identity priority caveats.

## value

PASS

The family is the simplest nontrivial conjugate pair of distinct words for reversible automata, and a complete infinite parameter-state classification gives an exact arithmetic spectrum of prime powers and optimal witnesses; a motivated model problem in separation complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
