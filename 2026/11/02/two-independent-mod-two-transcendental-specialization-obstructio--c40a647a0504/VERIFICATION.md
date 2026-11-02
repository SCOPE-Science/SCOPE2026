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

# Reproduction and limits

The fully embedded `RESULT.md` gives an all-vector proof from Weierstrass fiber valuations, a cubic automorphism, an Eisenstein lattice structure and the mod-two norm obstruction. The assumptions on the published degeneration and the precise restriction to transcendental lattices are integral to the proof.

Execute `python3 verify_lattice.py` with any standard Python 3 interpreter. In the inspected package this printed `VERIFY_OK: 4A2, 7 index-four sublattices, unique 2A2, cokernel (2,2)`. The script uses only the standard library. It exhausts the **seven** rank-two Hermite normal forms of determinant four, not infinitely many vectors. The latter are handled by the written parity lemma. The external geometric premises are supported by the full arXiv preprint, not reproduced by the checker. No independent validation of these deductions has been performed.
