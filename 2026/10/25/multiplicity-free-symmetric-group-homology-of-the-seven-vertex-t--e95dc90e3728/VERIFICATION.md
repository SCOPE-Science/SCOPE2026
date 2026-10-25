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

The attached three Python verifiers and their recorded actual outputs perform exact finite calculations. Place all six files in one directory and run `python3 homology_verifier.py`, then `python3 equivariant_verifier.py`, then `python3 character_decomposition.py`. Python 3 and SymPy are required. The first program checks every face, every incidence, acyclicity and integer Smith computations. The second checks exact chain projection/inclusion, all fifteen conjugacy representative chain actions, fixed-face Lefschetz identities, and recorded character. The third reads `equivariant_output.txt` to compute the rational Specht decompositions and verify orthogonality. This is not an external or independent audit.

The finite checks certify this seven-vertex calculation only. Mathematical code checks do not establish uniqueness in the published literature. The directly relevant chapter of Jonsson's monograph was not available in full; its homology table is acknowledged as prior work.
