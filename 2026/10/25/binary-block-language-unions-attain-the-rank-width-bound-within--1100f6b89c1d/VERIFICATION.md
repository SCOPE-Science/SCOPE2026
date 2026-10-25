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

## Checks performed

- Reconstructed the right quotient at every rank from the two block sets \(A=\{00,10\}\) and \(B=\{01,10\}\).
- Distinguished the three quotient types at internal block boundaries using \((00)^r\) and \((01)^r\).
- Distinguished the five intermediate half-block quotients by their first bit and the strict inequality \(A^r\ne B^r\).
- Counted the quotient widths symbolically and applied Myhill--Nerode, including the single dead state.
- Ran `python3 verify.py`; it checks every prefix/suffix quotient for \(2\le d\le8\) and prints `VERIFY_OK`.
- Confirmed that the two endpoint ranks lose at least three and two states, respectively, relative to the rank-width expression for this operand profile.

## Limits

The finite checker is corroborative, not a proof for unbounded \(d\). The theorem is restricted to the stated family and rank-width profile. The literature comparison is bounded and cannot rule out an unindexed equivalent result. No independent audit has been performed.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
