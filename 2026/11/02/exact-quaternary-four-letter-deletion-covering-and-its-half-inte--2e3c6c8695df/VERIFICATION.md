---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The 64 received triples split into symbol-equality types AAA (4), ABA (12), AAB/ABB (24), ABC (24). Independent exact arithmetic confirms nonnegative dual masses 1/2,1/8,3/8,1/4 with total 37/2; every one of 256 length-four words has distinct-deletion dual weight at most 1, equivalently all fifteen equality-pattern orbits have maximum 1. This yields integer code size >=ceil(37/2)=19. Independently recomputed full deletion shadows of all nineteen listed words; their union equals all 64 triples. The proposed fractional primal weights 1/6,1/3,1/3,1/12,3/16 on codeword equality patterns 0012,0100,0101,0122,0123 give coverage exactly 1 for each 64 triple and total 37/2. Strong LP duality establishes exact fractional optimum. This is COMPLETE finite exhaustion of the stated 256x64 universe, not a sample or an infinite-family claim.

## originality

PASS

The same single-deletion covering problem has established asymptotic bounds, hypergraph formulations and VT constructions. Xie–Sun–Ge 2026 studies large alphabet and burst deletions and did not state the q=4,n=4 exact optimum or 37/2 LP pair in the inspected full article. Lenz et al. covers general bounds, and perfect deletion-correcting codes impose a distinct packing property. Resultary published exact ternary length-five and odd-alphabet length-three coverage, neither covers this quaternary length-four instance.

## value

PASS

This exact 4-ary, length-four, one-deletion cover is a natural first small hypergraph incidence optimization beyond trivial counting: the exact integer value 19 exceeds the elementary counting lower bound 16, and the half-integer fractional optimum explains an integrality gap. Complete explicit rational optimality certificates are independently replayable and useful as benchmark data; no need to invent a larger all-parameter theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
