---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact-rational verification
Run `python3 verify_rank3_kneser.py` from the directory containing the standalone code. The implementation requires only the Python 3 standard library and uses integer/Fraction calculations throughout.

It verifies the disjoint-triple edge relation, vertex Laplacian residuals, absolute electrical-current totals, and complementary projection trace identity on all full graphs with \(7\le n\le13\). It evaluates all ten antisymmetric orbit equations (where present) across \(8\le n\le25\), all four cut capacities across \(8\le n\le39\), and the exact successive-difference rational identities across \(9\le n\le39\).

The all-dimension identity comparisons use more than \(25\) distinct parameters. Once all explicitly displayed denominators are cleared, their polynomial numerator degrees are bounded by \(25\), so matching at \(31\) distinct integers establishes those identities for every integer input where the denominators are nonzero. The positivity of the numerator coefficient lists after the shift \(t=n-9\) and the strict orbit-potential ordering are verified algebraically in RESULT.md. Finite full-graph calculations are corroborative, not substitutes for the proof.

Expected successful result:

`RANK3_KNESER_EXACT_OK orbit_equations=179 threshold_counts=128 full_graphs=7 vertices=966 edges=34310 rational_identities=PASS peak_certificates=PASS`

No external or independent mathematical validation has been performed. Results concern canonical real unit-weight orthogonal projections only.
