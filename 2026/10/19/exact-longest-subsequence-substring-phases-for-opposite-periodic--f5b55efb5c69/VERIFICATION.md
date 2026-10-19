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

# Reproducibility and limits

`check.py` is a standalone Python 3 script that computes each candidate substring of the reversed periodic word directly and checks scattered embeddability in the increasing periodic word by scanning source symbols. It compares the exact optimum and the set of all distinct optimal strings against the closed forms for \(q=2,\ldots,8\), \(m,n=1,\ldots,9\), covering 567 parameter triples. A separate exhaustive test of the per-factor descent criterion covers 70,756 factor cells for \(q=2,\ldots,7\), \(m,n=1,\ldots,7\). The recorded output in `check_output.txt` is from an actual execution of the packaged script.

The mathematical proof in `RESULT.md` is unrestricted over positive integer period counts and alphabet sizes at least two. The tests are finite corroboration, not exhaustive verification of the infinite claim. The originality comparison covers the inspected primary papers and searches, not all possible indexed or unindexed literature. Independent scientific validation was not performed.
