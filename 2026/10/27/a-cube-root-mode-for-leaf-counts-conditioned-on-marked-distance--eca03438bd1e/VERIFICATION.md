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

Run `python verify_cayley_leaves.py` using Python 3 standard library only. The script enumerates all labeled Prüfer-coded trees of orders two through eight and independently computes graph distance, degrees and the total number of leaves. It validates exact rational conditioning of the total leaf count and of endpoint and off-path counts, plus the distance marginal and difference-sign criterion. It also verifies the difference expression by exact rational arithmetic through order 350.

The executed source printed `VERIFY_OK 60859 exact assertions, 280392 enumerated labeled trees` after all checks completed. Computations are finite and not presented as a proof of the unrestricted theorem. The proof for all \(n\ge3\) is the rooted-forest enumeration and algebra in `RESULT.md`; the classical root-forest count follows independently from the displayed matrix-tree determinant. No external or independent audit was performed.
