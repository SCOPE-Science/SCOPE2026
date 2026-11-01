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

# Verification and mathematical scope

Run `python3 verify.py` with Python 3. The file `verification_output.txt` is the exact recorded standard output of the supplied standalone checker. No external packages, data files, remote services, or network access are needed.

The program constructs the twelve-vertex eighteen-edge graph from the explicit generalized-Petersen definition. It tests all 4096 subsets at each of three cutoffs in two independent ways, confirming augmented face counts 171, 810, and 1469 and minimal forbidden connected-set counts 18, 32, and 66. It constructs vertex-toggle discrete-Morse matchings and performs complete directed-Hasse topological sorting on respectively 462, 3180, and 6528 incidences. Critical-cell vectors are \((1\text{ at }0,1\text{ at }2)\), \((1\text{ at }0,4\text{ at }3,2\text{ at }4)\), and \((1\text{ at }0,1\text{ at }3,8\text{ at }4,16\text{ at }5)\).

For cutoff two, it reconstructs the complete signed integral \(4\times2\) Morse differential \(\partial_4\), whose first column is \((-1,0,0,0)^\mathsf T\). For cutoff three, it reconstructs the signed \(1\times8\) Morse differential \(\partial_4\) and \(8\times16\) differential \(\partial_5\), checks \(\partial_4\partial_5=0\), and computes determinant \(+1\) for the stated \(7\times7\) minor of \(\partial_5\). These integral attaching-degree computations and CW cancellation in Hurewicz dimensions prove the homotopy types; mod-two homology is independently recomputed as a consistency check and is not treated as an integral proof.

The checker terminates with `DURER_INITIAL_HIGHER_INDEPENDENCE_INTEGRAL_OK`. It verifies exactly the graph and cutoffs specified; nothing is extrapolated to higher cutoffs or other generalized Petersen graphs. This is self-review only, not an independent audit or external certificate.
