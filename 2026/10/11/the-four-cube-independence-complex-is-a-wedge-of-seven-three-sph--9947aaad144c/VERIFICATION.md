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

The complete finite certificate comprises `morse_certificate.json` and `verify_q4.py` in this directory. Run `python3 verify_q4.py morse_certificate.json` with Python 3.10 or later. The script requires only the standard library.

The exact run checks the graph's sixteen four-bit vertices and all vertex subsets; it enumerates \(743\) independent sets counting the empty set, and validates the face vector \((16,88,208,228,128,56,16,2)\). It checks the \(367\) pairs and eight critical masks, reconstructs all \(2816\) covering incidences, and tests every incidence against a complete topological ordering of the oriented Hasse diagram. This ordering is a finite proof of acyclicity. It independently computes all mod-two boundary ranks \((15,73,135,86,42,14,2)\).

Successful output:

`VERIFY_OK independent_sets=743 nonempty_faces=742 pairs=367 critical=1x0+7x3 acyclic_edges=2816 mod2_b3=7`

By the discrete-Morse theorem, a complex with this acyclic matching has a Morse CW model with one zero-cell and seven three-cells. There are no one- or two-cells, so the attaching maps of the three-cells are constant. This completes the homotopy, integral homology, and fundamental-group argument; the binary boundary calculation alone would not do so.

No infinite graph-family claim is made. The certificate proves this finite case exhaustively, but it does not resolve originality against all unindexed literature.
