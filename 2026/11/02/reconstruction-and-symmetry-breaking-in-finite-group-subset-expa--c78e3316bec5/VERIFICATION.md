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

PASS: Units of S(G) are exactly (empty,g) and idempotents exactly (A,1), with Boolean union atoms singletons. Thus a semigroup isomorphism gives group isomorphism phi and atom permutation s satisfying s(ga)=phi(g)s(a), whence s(a)=phi(a)t and F(A,g)=(phi(A)t,phi(g)). For the pointed inverse semigroup, minimum idempotent ({1},1), atoms e_g=({1,g},1), and unique nonidempotent with range e_g equal a_g=({1,g},g) recover the multiplication: a_g a_h has range support {1,g,gh}, and its second coordinate distinguishes gh=1. Thus phi is multiplicative. Factorization (A,g)=(A,1)a_g completes all-group reconstruction, including the trivial group. Composition conjugations yield Hol(G), |G| distinct pointed copies, faithful inner unit conjugations. Explicitly inspected standalone checker for C1/C2/C3/C4/V4/S3; finite cases are corroboration, proof uses arbitrary finite G.

## originality

PASS

PASS, best of knowledge and with substantial caveat. The Szendrei/prefix and full subset expansions are established prior objects, and universal-property literature is closely related. The inspected full Lawson–Margolis–Steinberg section on the prefix expansion presents strong factorization/morphism properties but does not give the exact simultaneous isomorphism-group reconstruction and |G|-orbit theorem. Full Gould–Johnson recent paper was inaccessible; priority risk remains serious but no decisive covering theorem was identified.

## value

PASS

PASS: This is a complete isomorphism classification of two canonical finite-group inverse-semigroup constructions and an explicit symmetry-breaking stabilizer/orbit theorem. It answers a natural group-reconstruction question and provides usable intrinsic invariants for future automorphism and representation work, beyond naming the classical holomorph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
