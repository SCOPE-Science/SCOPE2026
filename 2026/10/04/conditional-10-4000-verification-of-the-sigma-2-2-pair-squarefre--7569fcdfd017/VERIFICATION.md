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
The exact replay is `verify.py`, with the explicit factor data also stored in `factorizations.json`.

The replay reconstructs the recurrence through \(t_{23}\), checks all three displayed \(\sigma_{2,2}\) pairs, verifies both cross-divisibilities, multiplies every complete factorization of \(x^2+x+1\), checks that no factor repeats, and certifies every listed factor as prime using a deterministic Miller--Rabin test valid for integers below \(2^{64}\).

The source paper's computer search to \(10^{4000}\) is not replayed. It is an explicit hypothesis of the final finite theorem, so the package makes no independent certification claim about that search.
