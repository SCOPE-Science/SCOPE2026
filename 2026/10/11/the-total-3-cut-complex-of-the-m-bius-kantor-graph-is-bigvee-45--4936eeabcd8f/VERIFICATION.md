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

Run `python3 verify.py`. The script uses only the Python standard library.

It reconstructs the Möbius–Kantor graph \(G(8,3)\), enumerates every independent triple and every face of the total \(3\)-cut complex, performs the full sequential element matching, and directly verifies the resulting Hasse orientation is acyclic. The expected checks are \(272\) independent triples, \(64{,}883\) faces including the empty face, \(32{,}419\) matched pairs, \(45\) critical cells all of dimension \(10\), \(515{,}872\) checked Hasse arrows, and Euler characteristic \(46\).

The computation is finite and exhaustive for this graph. It does not establish any family-wide result for generalized Petersen graphs. The homotopy inference uses the standard discrete-Morse theorem that an acyclic matching with the empty face paired and all remaining critical cells in one positive dimension gives a wedge of spheres in that dimension.
