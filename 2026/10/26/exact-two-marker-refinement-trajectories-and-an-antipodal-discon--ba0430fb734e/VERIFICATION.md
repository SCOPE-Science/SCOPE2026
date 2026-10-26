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

Run `python3 verify.py` with Python 3 and no external packages. This directly implements neighbour-multiset counting colour refinement and independently constructs the formula's distance signatures; it checks every round for every size \(3\le n\le90\) and each allowed marker separation, plus the exact first stable round, class counts, and strict changes before stabilization. The saved `verification_output.txt` was produced from the included script.

A finite enumeration is not a proof for unbounded size. The arbitrary-size proof in `RESULT.md` uses the rooted-walk-unfolding characterization and the two-arc distance geometry; no external certificate or independent audit is claimed.
