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

The analytic proof in `RESULT.md` is the basis for the unrestricted theorem. The standard-library script `verify_small_cases.py` enumerates all topologically ordered complete acyclic transition tables in the stated finite ranges, all accepting-state sets, and filters for reachability, coaccessibility, and distinct right-language signatures. Running `python3 verify_small_cases.py` printed `PASS: 7 (q,n) cases; final-state strata all match.` The tested ranges are \(q=2,n=2,3,4,5\) and \(q=3,n=2,3,4\). These checks validate small instances only and do not replace the proof.

Scope limits: \(q\ge2\), \(n\ge2\), and \(1\le f\le n\); the theorem does not cover unary alphabets, incomplete DFAs, or nondeterministic automata. The full intermediate cardinality spectrum is not classified.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
