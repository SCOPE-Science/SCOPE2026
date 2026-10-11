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

# Verification instructions
Run `python3 verification.py` with a standard Python 3 interpreter. It checks the defining simplices directly, including their orientation signs, and evaluates every rotation/reflection for \(2\le d\le5\) and \(2d\le n<\min(2d+7,17)\). It separately verifies adjacent-contraction contiguity for \(d=2,3,4\) and \(2d+1\le n\le2d+3\). The observed output is `VERIFY_OK: signed dihedral Lefschetz identities 560 ; adjacent contraction-contiguity pairs 126`.

The finite checks are not proofs for all parameters. The complete proof is in RESULT.md and depends on the published coloring homotopy-equivalence theorem, the explicit adjoining-increment contiguity lemma and the orientation computation for the base join of simplex boundaries. Verification does not assess integral homology of quotient spaces or independent mathematical certification.
