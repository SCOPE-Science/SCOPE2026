---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The four transverse intersection points on C1 are parameterized by u=-1,2,3,6 and form a projective frame; any projectivity preserving {C1,C2} must induce one of 24 permutations. Independently reconstructed each unique 3x3 projective map using SymPy exact rationals, checked both quadratic-form pullbacks, and got 4 preserving the ordered pair, 0 exchanging the pair, 1 preserving C3 in addition. As the source combinatorics distinguishes C3 as the unique conic tangent to both others and there is a single line component, any arrangement equivalence lies in the trivial ordered-triple stabilizer; four distinct displayed lines give four PGL3-orbits and trivial automorphism groups. A finite exhaustive 24-permutation search is a complete proof here because of projective-frame uniqueness, not extrapolation.

## originality

PASS

Prior Amram et al. (2023) and 2024 follow-up establish just two deformation components of these explicit conic-line arrangements, not exact projective orbit/stabilizer equality of the four representatives. The independently reconstructed 24-frame calculation is a distinct finite moduli assertion, with residual possibility of unindexed earlier stabilizer work.

## value

PASS

Determines the actual orbit relation and automorphism groups for concrete representatives of an established two-component Zariski-pair construction, showing inequivalence even within each deformation component; a motivated, nonformal moduli refinement with an exact small stabilizer invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
