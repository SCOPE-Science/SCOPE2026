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

# Verification notes

The proof in `RESULT.md` treats every finite quiver, every prime-power field size, and all edge multiplicities and loops. The attached `rb_quiver_checker.py` independently enumerates nonzero rank-one linear tensors over explicit small finite-field algebras, evaluates the weight-zero Rota–Baxter identity on all ordered basis pairs, and compares those direct counts with the graph formula. It evaluates the path recurrence separately.

Run `python3 rb_quiver_checker.py` under Python 3.9 or later. The final expected line is `RANK_ONE_QUIVER_RB_OK 13`. Test configurations include linearly oriented paths on two to four vertices, the outward three-vertex fork, a triangle, parallel arrows, loops, a separated-graph four-cycle, and base fields of orders \(2\), \(3\), and \(4\). The order-four field is represented by the polynomial \(t^2+t+1\) over \(\mathbb F_2\).

Representative directly enumerated totals: a two-vertex path has \(7\), \(20\), and \(39\) rank-one operators over fields of orders \(2\), \(3\), and \(4\); the three-vertex directed path has \(61\) and \(308\) over orders \(2\), \(3\); the outward fork has \(69\) and \(380\); the four-vertex directed path over order \(2\) has \(421\). All tests passed. They verify finite instances only: correctness over arbitrary fields and quivers is established by the symbolic rank/Peirce-count proof. No external mathematical audit is represented by this file.
