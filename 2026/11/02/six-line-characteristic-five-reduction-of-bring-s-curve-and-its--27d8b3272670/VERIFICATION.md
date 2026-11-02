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
# Exact verification

Run `python3 verify_bring.py` in this directory. The checker uses only the Python standard library and exact arithmetic in \(\mathbb F_5\). The observed success marker is `BRING_CHAR5_SIX_LINES_CONIC_OUTER_S5_DELTA9_OK`.

The script reconstructs the three elementary-symmetric equations after substitution in \(\mathbb P^3\), verifies the exact \(q,h\) identity, enumerates all \(31\) points of \(\mathbb P^2(\mathbb F_5)\), independently checks that the full curve has \(31\) points among \(156\) points of \(\mathbb P^3(\mathbb F_5)\), checks the six conic/cubic intersection directions and affine residue orderings, and verifies that the \(120\) coordinate permutations yield \(120\) different permutations of the six components. Independent non-computational steps in the proof establish that the conic is smooth and geometrically irreducible, the cubic does not contain the conic, Bézout length is \(6\), and the complete-intersection arithmetic genus and normalization sequence give the local delta invariant. Finite enumeration alone does not prove these geometric completeness statements.

The work does not provide a semistable-reduction theorem or a classification of the full automorphism group of the reducible curve. No independent audit or external certification has been performed.
