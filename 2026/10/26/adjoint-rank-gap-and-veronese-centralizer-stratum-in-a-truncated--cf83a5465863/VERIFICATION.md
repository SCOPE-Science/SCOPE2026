---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The unital quotient has the 15 basis words of degrees 0 to 3. Its scalar and cubic coefficients contribute a 9-dimensional central factor. For v != 0 in the two-dimensional linear component, choose a basis with v=x: commutation with quadratic words gives 3 independent cubic images, and the linear-to-quadratic block adds 1 independent image; the kernel of that degree-two block contributes only a cubic image already counted. Hence rank(ad_a)=4 independent of Q and of characteristic. For v=0, only the map V -> V^⊗3, w |-> [Q,w], survives. A nonzero Q commutes with a nonzero w exactly when Q is a scalar w⊗w (five distinct word coefficients), so ranks 1 or 2 occur according to the quadratic Veronese locus. The q+1 projective lines w give q^2-1 nonzero Q tensors, yielding counts [q^9,(q^2-1)q^9,(q^4-q^2)q^9,0,(q^2-1)q^13] for ranks 0,1,2,3,4, summing to q^15. Averaging q^(15-r) centralizer sizes produces 2q^-4+q^-5-q^-6-q^-7. Independently enumerated every q^6 parameter pattern and computed full 15x15 commutator-matrix rank for q=2 and q=3, obtaining [1,3,12,48] and [1,8,72,648] before the q^9 factor. Those are finite corroborations, not the proof for all prime powers.

## originality

PASS

Dutta–Basnet–Nath arXiv:1510.08211 provides the finite-ring commuting probability, centralizer-sum machinery, bounds and Z-isoclinism invariants; it does not compute this 15-dimensional quotient. Bremner arXiv:1303.0920 develops word bases/noncommutative Groebner and universal envelopes, not an adjoint-rank census for this quotient. Bergman’s theorem on untruncated free algebras has fundamentally different centralizers owing to the length-three central socle in the quotient. Best-of-knowledge novelty assessment of the surviving precise mathematical contribution; unsuccessful database search is not proof of absolute priority.

## value

PASS

The first nontrivial two-generator length-four free associative truncation has an intrinsically motivated commutator-rank distribution. The forbidden rank 3, geometric Veronese rank-one stratum and all-field commuting probability together are a complete finite-ring invariant and a structural test case against general commuting-probability bounds; this is not mere substitution into a generic centralizer identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
