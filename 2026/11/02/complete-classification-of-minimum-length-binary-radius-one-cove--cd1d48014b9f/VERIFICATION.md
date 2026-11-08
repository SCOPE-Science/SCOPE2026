---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For L=1,...,22 each indexed cyclic binary word is one of 2^L integer masks, with seven-bit cyclic windows even for L<7. OR of 128-bit radius-one masks equals universal coverage iff every 7-bit target occurs within Hamming distance one. Independent C++ enumeration checked all 8,388,606 candidates: no solution through L=21, precisely 132 at L=22. For all 132, checked 11 ones, 22 distinct windows, two extended dihedral/complement orbits of sizes 44 and 88 and target hit multiplicities 80 once and 48 twice; integer orbit representatives 141243 and 158331. This exhaustive finite check proves the precisely bounded census, not any all-order statement.

## originality

PASS

The shortest length 22 is prior art (Chung–Cooper 2003/04); neither that scalar optimum nor the seed construction of Chee et al. 2025 subsumes the full enumerated optimal words, complement/reversal orbits, balanced weight, and multiplicity histogram. Independent Resultary and targeted exact-number searches did not identify a prior all-optima census. Best-of-knowledge priority is restricted by incomplete access to the 2003 full text and other unindexed code tables.

## value

PASS

Order-seven binary one-error cyclic covering sequences are an independently motivated optimal seed design: Chee et al. 2025 Example 26 uses a length-22 seed in 2D covering constructions. Knowing every optimal seed, the six rotation classes, and exact neighbor overlaps gives a natural complete finite classification, not a trivial rediscovery of the known minimum length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
