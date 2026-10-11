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

The accompanying `verify.py` enumerates all cyclic time and frequency shifts directly for each integer order from 5 through 18. For every order it evaluates explicit extremal and nonextremal triples realizing each support-size level, and also tests the action of a nontrivial primitive affine reindexing. A fixed-seed random sample of 30 nonvanishing coefficient triples at each order supplies additional comparisons. The extracted script printed `VERIFY_OK tests=560; cyclic orders=5..18; every predicted support level witnessed`.

The independently implemented prediction comes from coefficient algebra: the two-tap row cancellation criterion is tested by an \(N\)-th-root relation, while the central polynomial's zeros are classified by equal endpoint magnitudes and a finite cosine identity, or by the even-order root at \(-1\). Direct enumeration of the complex Fourier sums supplies a distinct numerical route for the finite tests.

Numerical comparisons use a specified tolerance and **cannot** certify exact vanishing beyond tested instances, all cyclic orders, or originality. The unrestricted proof is the symbolic five-row argument in `RESULT.md`. Literature comparison directly inspected the relevant arXiv full texts and an indexed two-sparse result, with remaining unindexed-publication risk. Independent audit has not been performed.
