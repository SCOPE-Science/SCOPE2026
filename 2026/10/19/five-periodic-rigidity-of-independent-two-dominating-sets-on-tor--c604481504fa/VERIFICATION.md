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

# Verification instructions and scope

Run both self-contained scripts from the extracted directory with Python 3.9 or later:

```
python verify_direct.py
python verify_transfer.py
```

`direct_output.txt` and `transfer_output.txt` are complete recorded standard outputs. An actual replay checks that both programs exit normally, print their success markers, and reproduce the recorded output.

The direct script constructs graph-neighbor masks and enumerates independent subsets without assuming column-periodicity. For \(n\in\{3,4,5,6\}\), the exact numbers are \(0,0,10,0\). It also tests directly the formula for all \(5\mid n\) up to \(n=80\); this establishes validity of the explicit witnesses at those lengths, not completeness for every length.

The independent transfer script enumerates the eleven independent column masks of \(C_5\), builds 81 admissible pair states and 40 compatible transitions, and takes closed-walk traces for \(3\le n\le40\). These traces are ten exactly at multiples of five and zero otherwise. Its recurrent subgraph consists of two disjoint five-cycles. The proof in `RESULT.md`, not finite replay, establishes existence, nonexistence, and uniqueness for all arbitrary \(n\ge3\).

No external formal or independent validation has been performed. The originality comparison depends on the published 2016 theorem and the listed directly inspected sources, with residual unindexed-literature risk.
