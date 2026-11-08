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

The radical decomposes into length 1 (A+B+C), length 2 (A⊗B+B⊗C), and length 3 (A⊗B⊗C) path spaces. Vanishing of the commutator yields exactly two adjacent tensor equations and one length-three equation. For endpoint-pair ranks i,j, the last equation is a surjective map onto (<a,a_prime>⊗B⊗C)+(A⊗B⊗<c,c_prime>), of rank s(it+rj-ij), leaving q^(D-E) choices. Partitioning middle pair by ranks 0,1,2 gives precisely the three displayed terms and free longest-path factor q^(2rst). Independent direct small-case values are 1024,41553,30208,108544 for (q,r,s,t)=(2,1,1,1),(3,1,1,1),(2,2,1,1),(2,1,2,1), respectively; all match the formula. The proof covers all prime powers, not only tested prime fields.

## originality

PASS

Hennecart–Perry formulate the quiver radical commuting-pair invariant and prove polynomiality for quivers without paths exceeding length two; positive r,s,t creates length-three paths. The classical one-arrow q^7(2q²+q-2) is expressly old (unitriangular). No exact independent-multiplicity formula appeared in Resultary or the accessible primary abstract. The full Hennecart–Perry source was not accessible through arXiv/OA or institutional service, so a hidden quiver reduction remains a significant risk.

## value

PASS

An exact three-parameter polynomial for the first natural path-length regime beyond the known length-two theory is a meaningful extension. The endpoint-rank stratification isolates a reusable commutator mechanism rather than merely one tiny table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
