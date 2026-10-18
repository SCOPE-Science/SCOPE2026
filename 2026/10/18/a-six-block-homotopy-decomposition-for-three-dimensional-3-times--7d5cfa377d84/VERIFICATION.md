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

# Reproduction and limitations

Run `python3 verify.py` with Python 3 and no third-party packages. The checker reconstructs all nonempty faces for board lengths \(n=3,4,5,6,7\), tests the six permutation block covering, unique block membership of every one-simplex and two-simplex, twofold vertex membership, absence of triple intersections, and the nine pairs of intersecting blocks. It calculates ordinary chessboard signed simplicial-boundary ranks in characteristic two and 101, with an explicit orientability and manifold-link test for the \(n=4\) torus. Its printed `VERIFY_OK` confirms only these finite consistency checks.

The theorem for **all** integers \(n\ge3\) is proved separately by the combinatorial uniqueness and graph-of-spaces argument and by the published ordinary-chessboard connectivity theorem. In particular, modular ranks on sampled boards are not asserted to be integer Smith-normal-form certificates or proofs for unsampled lengths. There is no external or independent review recorded.
