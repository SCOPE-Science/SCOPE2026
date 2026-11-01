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

# Verification

The bundled `verify_mcgee.py` uses Python 3 and `networkx`. Running `python3 verify_mcgee.py` recomputes the 24-vertex LCF graph and all 276 unordered distances, checks the six distance-four four-cycles, and validates all 96 claimed radius-two elementary collapse pairs individually against the current complete face set. It also enumerates every graph automorphism and checks the signed orientation determinant against a second computation using fixed-face Lefschetz traces on the 728 simplices of the sixfold join of two-point complexes. The exact output from successful execution is in `verification_output.txt`.

The verifier is a finite, exhaustive check of the required graph, collapse and group-action identities. The sphere and persistence conclusions additionally invoke the written standard topological facts: elementary collapses are homotopy equivalences, joins of six two-point spaces form the five-sphere, and rational homology of a finite-group quotient is the invariant subspace. The calculation does not prove any statement about other cages, integral homology of quotients or global publication priority. No independent audit has been performed.
