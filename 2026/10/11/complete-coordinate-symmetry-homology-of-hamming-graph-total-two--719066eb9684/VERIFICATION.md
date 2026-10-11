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

# Finite verification and limits

The accompanying `verify_hamming.py` uses Python 3 standard library only. It constructs Hamming-graph adjacencies directly, enumerates total two-cut faces by testing whether the complementary vertex set is a clique, and calculates signed simplicial Lefschetz sums with orientations determined by vertex order. These checks are mathematically independent of the coordinate-line incidence-kernel proof. It also computes actual mod-2 boundary ranks rather than relying on Euler characteristics.

Run `python verify_hamming.py` in the directory containing the script. The observed replay prints `VERIFY_OK trace_cases=36 full_F2_homology_cases=5` and `EXHAUSTIVE_GROUP_OK elements=140`. The exhaustive element counts are \(8+12+72+48=140\) for the full natural groups of shapes \((2,2)\), \((2,3)\), \((3,3)\) and \((2,2,2)\), and all characters agree. Five full homology computations cover graph orders \(4,6,8,9,12\), with total-two-cut top reduced Betti ranks \(1,2,5,4,9\), respectively. The script also confirms finite face counts for graph orders up to \(16\).

The finite tests do not establish the theorem for unbounded coordinate number or alphabet sizes. The proof uses an exact equivariant chain argument and Alexander duality for all permitted parameters. No external independent audit or certification has been performed.
