---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

A rainbow path with only two named colours has length at most two. In a complete biclique the opposite-side pairs are adjacent, while same-side pairs are rainbow connected exactly when their red-incidence rows or columns differ. Therefore the binary matrix must have distinct rows and columns. Ordering the u distinct length-v row words by Hamming weight proves the minimum red budget and forces all lower layers plus a terminal subset. At u=v the zero word and v-1 unit words separate all columns; at u≥v+1 every unit word appears, so no extra column constraint spoils any minimum. Multiply the terminal subset choice by u! label bijections. Möbius inversion on equality partitions of rows and columns gives the exact weighted rectangle product for every coefficient, and swapping red/blue gives reciprocity. Infeasible u>2^v follows by pigeonhole. Boundary cases u=v=2 and u>2^v explicitly checked.

## originality

PASS

The feasibility threshold for two-colour rainbow connectivity is classical: Chartrand–Johns–McKeon–Zhang 2008 Theorem 2.6 obtains rc(K_{v,u})=2 iff u≤2^v; Septyanto–Sugeng 2018 formalizes rainbow colour-code methods. These are credited and not claimed new. The asserted additional mathematics is the minimum budget of one named colour, all labelled minimizers and full coefficient-by-coefficient red budget enumerator via double partition-lattice Möbius inversion. Those specific distribution and optimization statements are absent from the relevant theorems/sections read. Closely related separating binary-array literature could contain equivalent formulas; this is recorded as a genuine risk.

## value

PASS

Once rainbow connectivity in two colours is possible, minimizing the edges assigned to a distinguished costly colour is a natural new optimization over the same graph. The theorem does not stop at feasibility or a fixed small parameter: for every feasible bipartition it gives the sharp budget, every attaining labelled coloring, and an exact weighted enumeration of the entire feasible sample space. The proof discovers that column-distinction imposes no extra cost at the minimum, including the balanced boundary. The full distribution can support uniform random colouring and resource-constrained enumeration and is not mere renaming of the classical rc=2 formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
