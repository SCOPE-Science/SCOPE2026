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
# Verification details

The complete finite checker is `verify_triangles.py`. Execute `python3 verify_triangles.py` with standard Python 3. It computes distinct one-deletion output sets for every source word, builds edges by literal intersection cardinality, and compares all edges with a separately coded alternating-interval construction. For binary words the direct comparisons cover lengths \(1\)–\(7\), for ternary lengths \(1\)–\(5\), and for quaternary lengths \(1\)–\(4\). It then exhaustively enumerates unordered triangles using the alternating graph, compares the displayed exact formula, and checks the unique one-long/two-adjacent-short interval structure through binary length \(8\), ternary length \(6\), and quaternary length \(5\). The successful execution ended with:

`VERIFY_OK direct_edge_cases=16 triangle_structural_cases=19`

Examples: \(T_2(4)=2\), \(T_2(5)=12\), \(T_2(6)=46\), \(T_2(7)=144\), \(T_2(8)=402\); \(T_3(4)=6\), \(T_3(5)=48\), \(T_3(6)=252\). These tests check the implementation and small cases but do not prove infinite validity; the proof in `RESULT.md` does. External independent mathematical validation has not been undertaken.
