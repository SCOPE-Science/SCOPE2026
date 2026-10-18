---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Take complete odd-length binary palindrome layers at L_1=5 and L_(k+1)=2L_k+3. No fixed-length binary palindrome AP exists: if consecutive differences have valuation j, mirrored least/highest differing digits force the middle term to have both bit values at position j. When y,z have common length L=2h+1 and x=2y−z lies in (0,2^h), endpoint gaps of size 2^h force y=2^(L−1)+1, z=2^L−1 and x=3. In a mixed-length selected AP y,z necessarily same layer as z<2y, while x is shorter than 2^h but min selected length5 excludes x=3; impossible. At N=2^L−1, layer contains 2^h palindromes and total length<=L has 3*2^h−2, so limsup relative density≥1/3. Independent no-3AP brute checks for full layers 3..19 and selected lengths 5 and13 agree; infinite proof is structural.

## originality

PASS

The published 2023 Pongsriiam–Saito Question27 explicitly asks whether positive upper-relative-density subsets of base-b palindromes must contain 3AP; this supplies explicit negative b=2 answer with quantitative 1/3. The source Theorem12 concerns repeated palindrome differences, and 2021 decimal max progression questions do not imply a dense binary progression-free set. No identical length-lacunary construction found in Resultary or targeted searches.

## value

PASS

A counterexample to a published density-Roth assertion about an arithmetically sparse set is valuable in its own right. The construction achieves macroscopic upper relative density and provides two nontrivial binary rigidity lemmas, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
