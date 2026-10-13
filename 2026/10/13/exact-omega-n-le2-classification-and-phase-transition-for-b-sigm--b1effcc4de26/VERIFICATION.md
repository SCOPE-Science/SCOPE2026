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

The theorem is proved symbolically in `RESULT.md`. The executable check in `verify.py` is a bounded regression test, not an infinite certificate.

The checker constructs the predicted \(\Omega(n)\le2\) solution set from the three theorem branches: the linear prime condition, the quadratic prime-square condition, and signed divisor pairs of \(T=ab-(a-b)k\). It treats \(T=0\) by the exceptional prime family. It then compares that set with direct evaluation of \(b\sigma(n)=an+k\) for every tested parameter triple and every tested \(n\).

The saved output in `verification_output.txt` was produced by running the bundled program from this package. The final ledger row is also re-extracted after serialization and the same program is replayed from the extracted package path.

Limits: finite enumeration can detect implementation or algebra mistakes in the tested range but cannot prove the theorem for unbounded parameters. The proof in `RESULT.md` supplies the infinite argument.
