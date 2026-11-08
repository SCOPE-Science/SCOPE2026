---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Using the exact adjacency predicate (adjacent cycle indices ±1 and distinct colors), I independently generated all 5281,18721,216257 nonempty independent faces for m=7,8,10. Repeated vertex-toggle matchings on ordinary nonempty posets have respectively 2635,9353,108121 pairs and critical vectors one c0 plus (4c3,6c4),(6c4,8c5),(8c5,6c6). I independently built all 25221,104568,1502070 Hasse incidences and reversed matched ones; all three full DAGs sorted exhaustively. Recomputed complete signed integer Morse differentials with matrices 4×6,6×8,8×6, exact ranks 3,5,5. Independent Smith normal-form reduction found every nonzero diagonal factor 1 (three/five/five unit invariants), agreeing with source unit maximal-rank minors. Wedge-of-spheres lower skeleton dimension d>=3 and Hurewicz pi_d≈H_d imply the unit attachments cancel, leaving stated S^d and S^(d+1) wedge multiplicities. Source independent cyclic 8-state transfer and direct F2 boundary checks are corroboration; finite checks exhaust these three graphs only and do not answer the infinite torsion-freeness conjecture.

## originality

PASS

Antolín Camarena–Carnero Bravo Theorems22–23 supply a general wedge-of-spheres and *possible Moore spaces* description; their pp26–27 mention these same C7×K3,C8×K3,C10×K3 as examples with nonzero free groups in two degrees, and explicitly ask Question24 about torsion. Those observations do not imply zero nonunit attaching invariants or the exact homotopy types. The 2025 Carnero paper changes the cycle factor to paths; Resultary C7×K4 has different color factor.

## value

PASS

The earliest non-divisible-by-3 cycle lengths m=7,8,10 for n=3 lie exactly in the remaining published torsion question for categorical C_m×K_n independence complexes. Proving integral wedge decompositions excludes possible Moore-space summands and settles these three natural benchmark cases rather than repeating free homology observations. This motivated finite cutoff is useful despite no all-m theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
