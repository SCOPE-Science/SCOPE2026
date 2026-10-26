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

# Exact checks and limits

Run `python3 verify.py` from the extracted package directory. `verify_output.txt` is the output from executing the included script. It uses only the Python 3 standard library and no external packages or services. The checker enumerates unlabelled unrooted binary tree shapes by subdividing each edge and adding one leaf, then deduplicating by a canonical centered-tree encoding. It tests every sample size \(6\le k\le n\) for every noncaterpillar shape through eleven leaves, derives the independent three-branch sextet count, checks the four-destructive-leaf lemma and the unique nontrivial equality, and explicitly reduces 770 sampled minimal connecting subtrees for a second structural criterion. These are finite checks, not a proof for arbitrary \(n\); the analytical deletion argument supplies that proof. No independent mathematical or bibliographic validation has been performed.
