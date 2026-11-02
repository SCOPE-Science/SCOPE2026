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

# Reproducibility

Execute `python3 verify.py` in the directory containing this document and the complete, unmodified `verify.py` source. Python 3 standard library suffices; no network service or external dataset is needed.

Actual execution passed 20,765 exact-rational assertions: 10,000 four-digit grouping identities; 10,000 paired-cancellation identities; 750 odd-prefix recursions; nine sequence identities; five full 4-by-4 matrix products at step counts \(3,13,53,213,853\); and one full matrix product at total time \(T=7/5\). The checker uses rational arithmetic rather than floating-point tolerance.

Those finite checks do not certify the infinite statement. The proof in `RESULT.md` proves the recurrence for every odd prefix and consequently for every indicated subsequence index. The computed matrix products serve as a separately formulated consistency check. Only the self-review has been performed. An independent audit is not available.
