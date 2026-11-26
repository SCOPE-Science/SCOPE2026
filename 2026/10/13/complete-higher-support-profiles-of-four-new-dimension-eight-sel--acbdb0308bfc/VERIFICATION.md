---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The four hexadecimal matrices agree with An et al. arXiv:2511.05440v1, Section 5, pp. 15–16, and with v2 pp. 21–23; verified zero-padding lengths are 1, 2, 2, 1 bits. Independent exact calculation checked rank 8, GG^T=0 and the ordinary distances. For an r-dimensional message space U, the unsupported columns are exactly those lying in U's annihilator; complementing dimensions gives a bijection with (8-r)-subspaces. The independent reproduction checked both direct encoded-basis support unions and maximal column-section masses, visiting the Gaussian totals (1,255,10795,97155,200787,97155,10795,255,1). At lengths 91,98,114,191 the hierarchy/minimizer pairs reproduced exactly: (42,64,75,81,84,87,89,91)/(54,982,872,334,5,12,1,1); (46,70,82,88,91,94,96,98)/(74,2337,6468,1481,19,12,1,1); (54,82,96,103,107,110,112,114)/(70,2016,4715,805,66,23,2,1); (94,142,166,178,184,187,189,191)/(94,4340,24800,25420,4774,125,2,1). Independent script and terminal output: branches/fd2afc81-a5f1-41a0-8c7d-d141dc8f52ae/reproduce_profiles.py and reproduction.txt. The frozen verifier was inspected, not executed. The result is for these exact representatives, with no generalized-weight optimality assertion.

## originality

PASS

Credit the published generators, their construction and ordinary minima. The supported distinct claim gives four full hierarchies together with a census of the minimizing subcodes at every rank. Inspected stronger-looking parameter and algorithm sources do not evaluate these profiles for the four representatives.

## value

PASS

The matrices are the four representatives used to close specific dimension-eight optimal self-orthogonal minimum-distance entries, not arbitrary length cutoffs. Higher-support minima describe how these same codes constrain sets of jointly active coordinates for subcodes, and counts distinguish rare from abundant extremizers. For example the length-91 example has only five minimizing five-dimensional subcodes, whereas the length-191 example has 4774. The exact profiles are useful benchmarks for comparing constructions or checking shortening behavior; they do not follow from d_1 or claim optimality in the new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
