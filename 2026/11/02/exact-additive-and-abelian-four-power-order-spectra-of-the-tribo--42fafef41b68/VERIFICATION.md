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

The Tribonacci fixed point mu(0)=01,mu(1)=02,mu(2)=0 has exactly the five digrams 00,01,02,10,20. Every length-4d factor for d<=1705 (4d<=6820) lies in the union of its first containing level-16 letter image and the next adjacent image because each single image has length at least 10609. Conversely every allowed adjacent image pair occurs. Counts of 0 and 1 in each of four contiguous d-blocks determine both Abelian equivalence and additive equality via digit sum 2d-2a-b. Thus the finite exhaustive search is sound AND complete for every d<=1705; it is not an all-d result. I fetched the actual two 1705-row CSVs and verify.py, and separately regenerated all 1705 predicate bits using an independently written C++ adjacent-image prefix-counter: 579 additive, 462 Abelian, 117 additive-only, first 4-power d=6, first divergence d=10, exact stated cumulative cutoff totals. This independently tests the key finite certificate, rather than merely trusting its output.

## originality

PASS

Popoli–Shallit–Stipulanti directly study Tribonacci Abelian/additive cubes and explicitly pose higher additive power-order classification (Problem 38), noting k=4 computational difficulty. Their square/cube results do not determine the present exact fourth-power membership table. Generalized Abelian complexity of single factors and fourth-power avoidance in a different morphic word likewise do not imply simultaneous equality of four adjacent blocks. The natural finite bound 1705 leaves all larger orders open; exact unindexed prior tables remain possible.

## value

PASS

The two complete exact binary membership tables up to the natural Tribonacci substitution length 1705, with explicit positive witnesses and mathematically certified absences, give rigorous bounded progress on a published order-spectrum question, including the first additive-versus-Abelian divergence. Finite cutoff is large, natural and tied to a complete factor cover, not arbitrary illustrative sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
