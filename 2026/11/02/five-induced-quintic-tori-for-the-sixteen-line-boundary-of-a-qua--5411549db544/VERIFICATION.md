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

The standalone Python program `verify.py` uses exact integer graph operations and finite arithmetic; no nonstandard packages are required. `python3 verify.py` reconstructs the sixteen vertices and forty intersection edges, checks the absence of graph triangles, and identifies Frobenius orbits of lengths \((1,5,5,5)\) on components, eight degree-five orbits on nodes, and sixteen degree-five orbits on branches.

The program constructs a Frobenius-invariant spanning tree and the twenty-five oriented integral fundamental cycles. It verifies that Frobenius maps each oriented cycle to the next in its orbit, not merely that rational character values agree. This establishes a computational cross-check of the five regular integral modules. An independent even-half-cube model checks all sixteen even sign lifts of the underlying five-cycle and their conjugacy.

The arithmetic checks compare the zeta-derived point counts and the motivic formula on \(\mathbb F_{q^n}\) for \(q\in\{2,3,4,5,7,11\}\) and \(1\le n\le20\). The recorded execution in `verification_output.txt` ends with `VERIFY_OK`. Finite checks do not prove the theorem for arbitrary \(q\) or \(n\); the separate symbolic proof uses the graph's exact structure, the gluing character lattice, the invariant blowdown, and Frobenius orbit decomposition. The source and output files are included in this package, with byte counts and hashes verified at packaging.
