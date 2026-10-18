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

# Verification and limits

The analytical proof rests on the exact source-conditioned formula (1), the exact one-step exchange (2), and the inequality (3), followed by a one-variable derivative and a uniform fixed-argument Taylor expansion. All assume independent open bonds, one uniformly random source and distinct preplaced sentinels on a simple undirected path.

The standalone `verification/verify.py` is executable with `python3 verification/verify.py`; it requires only Python's standard library. It enumerates all open-bond outcomes and all sources at each placement, and compares exact rational probabilities to the theorem's formula for path orders 2 through 9 and three different transmissibilities (360 exact comparisons). It separately tests the exchange formula for path orders 3 through 19 and four rational transmissibilities, and the exact four-vertex example.

Output reproduced before packaging: `PASS: 360 exact percolation enumerations, all threshold comparisons, exchange identities.` Enumeration is finite corroboration, not evidence for the unrestricted path-length claim; the latter relies on the provided analytical proof. This verification does not establish equivalence-free novelty and is not an independent audit.
