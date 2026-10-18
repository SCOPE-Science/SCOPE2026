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

Prefix extension exhausts ternary linear square-free words, because adding a letter can only introduce a suffix square. Independent implementation gives 168546 at n=36,219516 at n=37. Testing every cyclic start and every half-length h with 2h<=n in ww gives 16416 and 18870 circular-square-free representatives; checking all 36*3 insertions for each n36 circular candidate against the exhaustive n37 set yields 540 extremal linear representatives. Each is primitive, hence exactly 540/36=15 circular rotation classes. Complete S_3 letter permutations and reversal action gives exactly 3 symmetry orbits of sizes 3,6,6 and reproduces three stated representatives. No extrapolation beyond n36.

## originality

PASS

Mol–Rampersad 2020/2021 Theorem 1.3 identifies length 36 as the last sporadic existence length and 37 as absent; their proof describes finding an extremal witness for each finite relevant length by computer search, not the complete 15-class equality census and dihedral/alphabet symmetry orbits. The strict difference between existence and complete enumeration is verified at the primary theorem/proof, not guessed from the title. No indexed same 36 exact census found; unpublished original search output remains a risk.

## value

PASS

Length 36 is mathematically singled out by the published sharp existence spectrum as the final isolated attainable length before the forbidden 37 and all lengths >=38. Classifying EVERY extremal object at this natural boundary into 15 rotation classes and 3 symmetry types supplies complete combinatorial information not obtainable from an existence witness; finite scope is intrinsically justified by the boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
