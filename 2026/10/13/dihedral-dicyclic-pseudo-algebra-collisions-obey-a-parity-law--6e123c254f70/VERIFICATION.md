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

The claim is for the two presented groups of order 4n, not every group with an index-two cyclic subgroup. In each, the cyclic subgroup of order 2n has inversion as the action of the other coset. A character of that subgroup of order d>2 is not fixed by inversion, and induction gives a degree-two irreducible; different pairs {λ,λ⁻¹} are inequivalent by restriction. The induced character is zero off the subgroup and restricts to λ+λ⁻¹, so its kernel is ker λ and its codegree is d. There are φ(d)/2 inversion pairs of exact order d. The abelianization is C₂×C₂ in the dihedral case and in the even dicyclic case; for odd n it is C₄ by a=x². The principal and three other linear characters exhaust the missing degree squares, since 4+4(n−1)=4n. Linear codegree equals image order, yielding the stated additions; 4 does not divide 2n for odd n and does not merge. The criterion follows, and n=2 gives the stated Q₈/D₈ multiplicities. For all n≥2, an element off the dicyclic rotation subgroup squares to aⁿ≠1, whereas every element in the dihedral reflection coset squares to 1; the involution counts differ. The packaged artifacts/verify.py was inspected, not executed. Its finite checks are not needed for the proof.

## originality

PASS

Pass is for the unrestricted-in-n parity law and its exact same-order collision and separation statements, not for the standard character tables or the power-of-two subfamily. A distinct same-day catalogue record proves exactly the power-of-two overlap for 4n=2^m, m≥4, and mentions a broader dihedral–dicyclic calculation without a separate identifier; the mention and metadata do not establish an independent earlier proof of the full law. Its own proved claim does not cover the general parameter or the odd split. The inspected primary papers do not otherwise establish the parity law. This does not certify historical priority.

## value

PASS

The exact parity criterion tests a structural question about an invariant intended to distinguish finite groups: it determines precisely when it cannot see the distinction between the two canonical inversion extensions with the same order, producing nonisomorphic collisions beyond 2-groups and a uniform contrasting odd branch. The value is the complete structural comparison rather than recomputing a particular character table or naming the Q₈/D₈ example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
