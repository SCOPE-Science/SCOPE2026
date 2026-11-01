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
# Exact finite verification

Run `python3 verify_q4_two_ind.py` with Python 3.8 or later. The file requires only Python's standard library. `checker_output.txt` records an actual successful execution of that precise checker.

The checker independently compares the induced-degree and induced-component definitions for all 65,536 vertex subsets, reconstructs the full 3,055-face complex, and verifies its face vector. It uses the explicit sixteen-label pivot order to build 1,519 matched Hasse pairs and confirms acyclicity by a directed topological sort over all 13,584 cover incidences. The critical-cell spectrum is sixteen cells in dimension three and one in dimension four; the empty face is matched.

The unique potential nonzero Morse boundary is computed by exact integer signed-incidence elimination, yielding sixteen zeros. The independent full-chain calculation over the field of two elements gives reduced Betti ranks 16 in dimension three and one in dimension four, vanishing elsewhere; Euler characteristic also agrees.

**Logical limit:** The mod-two calculation alone would neither show absence of odd torsion nor determine the homotopy type. The integral statement follows instead from acyclicity of the matching, exact signed attaching degrees, and the Hurewicz isomorphism for the wedge of sixteen three-spheres. The classification applies to \(Q_4\), not to higher-dimensional cubes. The evidence is self-reviewed, not independently audited.
