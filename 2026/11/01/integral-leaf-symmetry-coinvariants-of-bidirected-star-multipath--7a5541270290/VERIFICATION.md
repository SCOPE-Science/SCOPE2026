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

Identified X_m exactly with connected crown graph on a_i,b_j with i!=j, graph cycle lattice all integer edge flows with vanishing row and column sums (rank m^2-3m+1). Fundamental graph cycles generate integrally; chord cutting reduces every >=8 cycle to shorter ones, and every six-cycle splits into four-cycles with a fourth label. For m>=5 every four-cycle has the same coinvariant image and the exact five-label relation Gamma(a,b;c,d)+Gamma(a,b;d,e)=Gamma(a,b;c,e) kills it. At m=4, six four-cycles have a unit 5x5 minor, rank-five lattice and a primitive relation (1,-1,1,1,-1,1); parity gives a nontrivial Z2 coinvariant and row swapping makes it at most Z2. For m=3 the crown is C6 and S3 acts by sign on H1. Independent symbolic minor, relation and integral SNF tests corroborate m=4, and the submitted finite verifier checks m<=8; the all-m proof is the lattice generation and five-label identity.

## originality

PASS

The exact final theorem is not implied by the materially inspected same-object and broader theorems; individual prior components are credited. Priority is best-of-knowledge with named risks, not absolute novelty proof.

## value

PASS

The natural directed-star multipath complex is the crown graph and its leaf permutations form a canonical S_m action. Integral coinvariants detect torsion annihilated upon rationalization; sharp threshold at m=5 and precise nonzero Z/2 at m=3,4 is a motivated integral equivariant boundary, not a tiny arbitrary parameter scan. It gives a reusable integral four-cycle generation/cancellation argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
