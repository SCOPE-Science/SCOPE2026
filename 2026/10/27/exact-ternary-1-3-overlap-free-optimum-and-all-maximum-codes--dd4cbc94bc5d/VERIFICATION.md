---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For n>=6 the three-letter endpoint blocks are disjoint, and every cross-prefix/suffix comparison is decided by these blocks, including self-pairs. For the observed prefix set P, the suffix set lies in the full compatible set S(P), so the code is contained in P times the free middle words times S(P). Conversely the full product is admissible. The independent chunked subset-OR census exhausts every one of the 134217728 prefix masks, obtaining product 72 for exactly 42 masks with (prefix size,suffix size) multiplicities (6,12):6, (8,9):15, (9,8):15 and (12,6):6. A maximum code must use the full product; S(P) is nonempty and its code recovers P as the set of actual prefixes, so there are exactly 42 labelled maximum codes at every n>=6. Permuting symbols and reversing words acts on the saturated pairs as stated; an independent check finds disjoint representative orbits of sizes 12,12,12,6 whose union is all 42 maximizing pairs. The proposed size-72 witness passes all 15552 ordered pair/overlap-length comparisons at n=6. The valid reason for that witness is that every forbidden-length prefix starts with 0 and every forbidden-length suffix starts with 1 or 2; different first and last symbols alone would only exclude length one. Replay with python3 /workspace/branches/58b5f690-3f98-400f-a95a-e5adec20c352/census.py (NumPy); equality_pairs.txt in the same directory contains the equality pairs. The finite calculation proves the base problem, and factorization proves the all-length statement.

## originality

PASS

The length reduction and the lower bound of 72 times 3^(n-6) are prior. The supported distinct claims are the matching global upper bound and the complete equality classification for the labelled ternary codes. The closest exact results differ in alphabet, overlap interval or fixed-weight restriction. No inspected general bound forces this optimum, and the exact prior construction gives only some maximum codes.

## value

PASS

The first short-overlap parameter beyond the exact k=2 result gives a natural ternary base capacity problem. The prior construction provides a concrete extremal candidate and the inspected general bounds are looser; the unrestricted upper bound closes that gap. A complete equality classification distinguishes inequivalent optimal constructions that the size alone could not identify, and applies at every length of the factorization, rather than just to a single small codebook.

The dated certificate retains the supplied scientific assessment, sources and limitations.
