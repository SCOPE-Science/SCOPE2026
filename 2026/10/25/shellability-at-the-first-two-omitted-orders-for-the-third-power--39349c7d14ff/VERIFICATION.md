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

Definitions and normalization were checked: C_n^3 connects residues of cyclic distance <=3; the ordinary three-cut facets are complements of disconnected induced 3-sets, not of independent sets alone. Every facet has n-3 vertices. The exact 169 masks at n=13 and 238 masks at n=14 in shellings.json were independently recomputed by graph-traversal connectivity and matched uniquely as the complete facet sets. For every facet after the first, independently computed its prior ridges and verified nonempty intersection and for every earlier facet a containing earlier ridge; zero failed checks. The complete down-closures had 7904 and 16067 nonempty faces. Exactly 1 and 8 facets have full restriction sets, proving respectively S^9 and wedge_8 S^10 via pure shellability. The cited Chauhan–Shukla Theorem 1.4 actually covers n>=6p-3, so p=3 covers n>=15. Combining the exact finite proofs with that published theorem yields shellability for every n>=13 and sphere multiplicity (n^2-13n+2)/2. No inference from finite enumeration to n>=15 is made.

## originality

PASS

The two exact finite cases n=13 and n=14 are the only newly established shellability claims. Homology and expected wedge counts were in a prior Table 2, while published shellability proved p=3 only for n>=15; therefore shellability of the two omitted orders is a mathematically sharper, not redundant, result.

## value

PASS

The published natural conjecture begins exactly at n=4p+1, whereas the existing proved p=3 range begins at n=15. Exhaustively certifying n=13 and n=14 therefore completes the p=3 positive conjectural range, a mathematically motivated sharp finite cutoff, rather than re-tabulating known Betti ranks. Full shellability is strictly stronger than homology and yields integral sphere-wedge homotopy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
