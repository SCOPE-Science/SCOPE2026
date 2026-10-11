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
The verification is finite and exact. `verify_q4_cech3.py` constructs the four-dimensional hypercube from Hamming distance, creates the 32 scale-three Čech generators \(N_1[v]\cup N_1[w]\), and enumerates every nonempty face.

It checks all 18,800 Hasse covers and verifies that the staged toggle matching consists of 1,959 disjoint cover pairs. Reversing the matched covers and directing every other cover downward gives an acyclic directed graph: a topological sort visits all 3,944 faces. The critical-cell vector is one cell in dimension \(0\), one in dimension \(3\), and 24 in dimension \(4\).

Using sorted vertex order for simplex orientations, the program then performs exact integer gradient-path elimination. The entire Morse boundary from the 24 critical 4-cells to the unique critical 3-cell is zero. This is the decisive attaching-map check: the 3-skeleton is \(S^3\), and each 4-cell attachment represents degree zero in \(\pi_3(S^3)\cong\mathbb Z\).

As a separate cross-check, direct simplicial boundary reductions over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) all give Betti vector \((1,0,0,1,24,0,0,0)\). The program output is stored in `certificate.json`.

The verification does not make any assertion for higher-dimensional hypercubes or other scales.
