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

# Verification and limits

The proof is self-contained in `RESULT.md`; it establishes the theorem for every integer pair \(m,n\geq3\). The critical ingredients are the exhaustive tight-edge vertex classification, exact evaluation of the permutation-invariant quadratic form, and the optimality bound for every positive-definite quadratic form after symmetrization.

`verify_complete_bipartite.py` is a standalone Python 3 script using only `fractions` and `itertools`. Run `python verify_complete_bipartite.py` in the directory containing the file. Expected and observed output: `COMPLETE_BIPARTITE_HILBERT_EXACT_OK 6228`. It tests all sign patterns for part sizes from three to eight, exact extremal vectors and a rational grid of invariant-form lower certificates. These checks do not prove the classification for unbounded dimensions; that conclusion uses the analytic arguments.

The assertion of originality is limited to the inspected literature and searched scientific records. A separate independent literature and proof review has not been performed.
