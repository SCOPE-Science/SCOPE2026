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

# Verification of the eighteen signed-cycle formulas

Run `python3 verify.py` with Python version 3.10 or newer. It requires no third-party packages.

The computation reconstructs the sixteen even-parity vectors in \(\mathbb F_2^5\), their forty Hamming-distance-four edges, all \(1920\) even signed coordinate permutations, and their eighteen signed-cycle types. It verifies class sizes, individual invariant constancy, and each row of the full table. Direct tests identify the only two possible zeros, at \(q=3\) of positive type \((2,2,1)\) and at \(q=5\) of the identity type. For \(q\ge7\), positivity follows by checking the eighteen displayed quadratics (and the minimum for integer \(q\ge7\)); for the small values below seven, the verifier checks each type separately. It also checks the blowup models over \(\mathbb F_3\) and \(\mathbb F_7\) by exhaustive rational-point enumeration in their projective planes.

Expected final line: `VERIFY_OK`.

**Proof inputs not certified by the finite calculation.** Every smooth degree-four del Pezzo surface is geometrically a five-point blowup; its sixteen geometric \((-1)\)-curves realize the described incidence graph with no triple intersections; and its rational-point count is obtained from the Frobenius action on the Picard lattice by the Weil–Lefschetz formula. The verifier does not independently verify these classical facts, does not infer universal assertions from sampled finite fields, and does not assume realizability of every signed Weyl type. Independent external mathematical validation has not been performed.
