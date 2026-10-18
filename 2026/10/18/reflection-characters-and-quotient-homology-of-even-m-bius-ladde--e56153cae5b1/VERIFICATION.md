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

# Verification record

Run `python3 verify_reflections.py` using standard Python 3. The verifier independently reconstructs the labeled Möbius ladder and enumerates its perfect matchings and all simplicial faces, then checks signed simplicial Lefschetz characters of both mirror classes. It also constructs the proposed pairwise-incompatibility graph without reading the enumerated perfect-matching faces, verifies full equality of the complexes for even widths \(4,6,8,10\), and performs independent exact mod-two boundary-rank reductions at widths \(4,6,8\). It checks the false-twin and triangle-chain orbit-graph description for every even width from \(4\) through \(40\). The output is recorded in `verification_output.txt`.

The infinite statement is not established by the finite tests. Its proof rests on the exact orbit-graph and independent-vertex-cover arguments in RESULT.md, plus the two published mathematical inputs: the incompatibility-graph description and nonequivariant homotopy type. The explicit source has been inspected and the critical finite instances independently reconstructed. Rational quotient homology follows from finite-group invariants after barycentric subdivision, not from any assumed free action.
