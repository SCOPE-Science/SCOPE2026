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
# Verification

`verify.py` is a standalone finite checker using only the Python standard library. It reconstructs the Möbius–Kantor graph, enumerates every independent face, verifies the complete acyclic matching by topological sorting of the oriented Hasse graph, counts all relevant gradient paths, and computes simplicial boundary ranks over both \(\mathbb F_2\) and \(\mathbb F_3\).

The expected nonempty face vector is \((16,96,272,376,240,72,16,2)\). The critical-cell counts are one in dimension \(0\), four in dimension \(3\), and one in dimension \(4\). The relevant gradient-path counts are \((2,0,2,2)\), and the reduced Betti numbers over both checked fields are \(\widetilde\beta_3=4\) and \(\widetilde\beta_4=1\).

The checker also verifies that the cyclic-neighborhood graph \(G_8^3\) from the comparison family has girth \(4\), while the Möbius–Kantor graph has girth \(6\).

A successful replay ends with `MK_INDEPENDENCE_VERIFY_OK`. The computation proves only this finite graph case; no broader family statement is verified.
