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

The analytic proof uses the following exact steps: the graph Laplacian factorization for an oriented edge, the product heat-kernel integral, the strictly decreasing radial potential, the binomial collapse of transverse edge variations, the trace/edge-transitivity diagonal identity, and norm minimization by averaging using the all-alphabet invariant-projection theorem in the cited literature.

Reproduce finite checks by running `python3 check_hamming.py` with Python 3 (standard library only). During preparation it printed nine exact cut/cycle/diagonal comparisons for \((d,q)=(1,2),(1,3),(1,5),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3)\), and exactly verified five radial identities for each of 49 pairs \(2\le d,q\le8\): **281 exact-rational assertions passed**. The \(d=1\) and binary tests are consistency tests, not new claims. All-parameter correctness depends on the proof, not sampling. The program is included in this package, not referenced from another record.

Literature checking compared all-alphabet Theorem 43 against binary-only Theorem 45 and Corollary 60 in the full-text arXiv manuscript. Equivalent unindexed or later results remain a bibliographic risk. No independent mathematical audit, verification, or priority determination has been performed.
