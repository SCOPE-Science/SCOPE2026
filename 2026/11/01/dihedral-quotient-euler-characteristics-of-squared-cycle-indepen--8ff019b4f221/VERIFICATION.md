---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For n≥6, every invariant independent set in Ind(C_n²) is a union of g-orbits, so the reduced signed Lefschetz trace is −I(B_g,−1) with the empty face and simplex orientation correctly counted. Rotations reduce to squared cycles of length gcd(n,a), or empty admissible orbit for d=1,2. A three-state transfer with characteristic x³−x²+1 gives recurrence W_d=W_{d−1}−W_{d−3}. Odd reflections yield a path square with one endpoint pendant, even reflections yield either a path with two pendants or a plain path square, giving stated A recurrences including n=6,7,8. Rational averaging after equivariant subdivision computes actual topological orbit quotient reduced Euler characteristic; χ is integer. The cubic characteristic polynomial has a negative real root of modulus <1 and conjugate pair modulus ρ>1. Infinitely many n have cos(nθ)≥1/2, so W_n dominates proper-divisor and reflection corrections O(n²ρ^{n/2}), proving absolute quotient Euler unbounded and infinitely many rationally non-acyclic quotients. Rebuilt orbit-subset sums for all dihedral elements n=6…18; every formula matched, finite corroboration only.

## originality

PASS

Compared the underlying squared-cycle independence complex to nonequivariant splittings, ordinary circulant Euler tables, and published equivariant studies of ordinary cycle matching, full strong Morse, and circular arc nerves/clique complexes. Different face conditions and dihedral actions prevent direct implication; no precise orbit-space formula found in inspected primary texts.

## value

PASS

The squared-cycle independence complexes form a classical all-order topological family, but the dihedral orbit-space alternating homology invariant is not derivable from unquotiented Betti numbers. Complete reflection-corrected arithmetic formulas and the unbounded/non-acyclic quotient consequence are nontrivial uniform structural information rather than a small fixed computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
