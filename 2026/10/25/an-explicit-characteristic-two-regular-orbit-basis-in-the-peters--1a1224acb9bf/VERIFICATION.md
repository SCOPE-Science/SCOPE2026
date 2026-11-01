---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Constructed the Petersen graph independently from disjoint two-subsets and enumerated all 2^15 edge masks by a disjoint-set forest test. Found exactly 2,000 spanning-tree nine-edge faces, 4,680 eight-edge faces, and exact complete mod-two top boundary rank 1,760; H8 has dimension 240 because no degree-nine simplices exist. Parsed both actual hexadecimal seed bit-vectors from the checked verify_mod2.py Git blob, verified all 4,680 equations on both, enumerated 120 permutations of five labels, transported each active facet and independently eliminated all 240 orbit columns. Their rank is exactly 240. This is an exhaustive finite certificate, not an empirical sample; it proves the full modular group-algebra decomposition.

## originality

PASS

Best-of-knowledge modular free orbit-basis refinement beyond previously known rational two-regular S5 character. The rational/complex representation is not sufficient over characteristic 2 because the group order is divisible by 2 and semisimplicity fails; explicit modular cycles and rank certificate add substantive structure.

## value

PASS

An explicit free module over the nonsemisimple group algebra F2[S5] captures automorphism action invisible in ordinary Betti numbers and rational character; the two concrete orbit cycles are an exact reproducible structural certificate and a natural small symmetric graphic-matroid benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
