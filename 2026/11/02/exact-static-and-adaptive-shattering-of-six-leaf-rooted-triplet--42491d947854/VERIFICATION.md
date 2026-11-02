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

## Reproduction
Run `python verify_rooted_triples.py depth9_certificate.json` with Python 3.9 or later. All inputs are embedded in the supplied files. `make_certificate.py` can deterministically regenerate the depth-nine witness tree from the enumerated class.

The verifier constructs \(945\) rooted full binary phylogenetic trees on six distinct leaf labels using root splits and independent leaf insertion, compares the sets of clusters, checks the unique true rooted-triplet orientation for each tree and triple, and exhausts all potential fixed supports containing a representative first query. Query symmetry makes this sufficient for all fixed supports. The valid support counts at sizes one through four are \((1,57,1458,18144)\); size five has zero. The four-query lower support realizes every one of \(16\) patterns.

The depth-nine certificate has \(511\) internal query nodes and \(512\) distinct leaf witnesses. Each witness is tested against the full path from the root. The cardinality bound \(945<1024\) gives depth-ten impossibility. Smaller cases are recalculated by an exact memoized Littlestone recursion. Program output is preserved in `verification_output.txt`.

## Limits
The upper VC bound is a finite exhaustive computation with executable source, not a compact handwritten classification of all supports. The adaptive certificate verifies existence at depth nine but does not supply a uniform construction for larger trees. All results are for the binary one-vs-rest encoding of rooted triples, not for multiclass Natarajan or multiclass Littlestone dimension. No independent audit has been performed.
