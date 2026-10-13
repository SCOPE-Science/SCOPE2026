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

Run `python3 verify.py` with Python 3 (standard library only). The enumerator considers each prime pair under the necessary abundance and scale inequalities for \(1\le k\le8\), using the exact criterion that forbids a representation \(a=r+sp+tq\) with \(0\le r,s,t\le M\). Its expected counts of weird numbers are \(1,1,5,3,10,23,29,53\). The observed terminal line was `VERIFY_OK candidate_pairs=29490 published_counts=(1, 1, 5, 3, 10, 23, 29, 53)`.

The script checks only finite instances. It does not certify the infinite theorem, novelty, or independent audit status. For the universal conclusion, verify the algebraic identity for the abundance, the binary subset-sum obstruction, the exact quotient/remainder transformation used to force \(q>2M\), the distinct residue pigeonhole inequality \(a<(p-M-1)q\), and the two cases \(p-M\ge M/3\) or \(p-M<M/3\).
