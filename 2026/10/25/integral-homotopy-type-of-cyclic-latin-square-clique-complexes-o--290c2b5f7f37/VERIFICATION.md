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

The exact standalone `verify_latin.py` enumerates cliques independently from the graph and compares them to the formula for all line faces together with \(n^2(n-1)\) mixed triangles, for odd \(n=3,5,7,9\). Direct mod-two boundary elimination checks that reduced homology is confined to dimension two with rank \((n-1)^3\) in each case. Its recorded stdout is in `verify_latin_output.txt`, reproduced from the embedded source.

The general claim is proved by the four structural arguments in `RESULT.md`: classification of all simplices, one-dimensional homotopy core, surjection from a torus killed on two generators, and integral two-dimensional Whitehead equivalence. The finite checks are stress tests and are not an infinite proof. No independent audit has been performed, and there is residual bibliographic risk from unindexed sources.
