---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

I inspected the complete frozen census algorithm and reran its exact 2,002-case modulus search in an isolated checkout (50.4 seconds). The optimum for moduli 7 through 20 is the nine-modulus set 7,8,9,10,11,12,14,15,16 with 36,340 of 55,440 residues covered, reducing to 1817/2772. The algorithm's CRT peel for private prime factors is an exact independent-coverage factorization; the remaining affine unit-and-translation orbit pruning enumerates residue tuples with stabilizers rather than sampling. Its bit masks count the union exactly. The published interval bound for 7..60 is a bound, not an assertion of full optimization there.

## originality

PASS

The closest full-text primary source treats minimum least common multiple of complete covering systems, not the exact maximal covered fraction for the fixed nine distinct moduli 7..20. Resultary returned this record as the exact hit. No inspected broader theorem or exact database yielded 1817/2772 or its maximizer; this is best-of-knowledge, with bounded literature risk.

## value

PASS

Near-covering at the natural Hough boundary seven is mathematically motivated, and a complete exact optimum for the contiguous 7..20 modulus window is a reusable benchmark in covering-system search. The record makes no claim that 7..60 is fully solved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
