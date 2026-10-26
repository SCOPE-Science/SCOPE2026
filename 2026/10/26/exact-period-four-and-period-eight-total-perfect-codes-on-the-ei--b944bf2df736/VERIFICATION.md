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

The theorem reduces every efficient open dominating set on \(C_8\square C_t\) to a periodic orbit in a deterministic partial map on \(65{,}536\) states. `verify_transfer.py` exhaustively constructs all transitions with exact integer bit operations and identifies all cycles. There are exactly four cycles of length four and sixteen of length eight. The bijection between closed state walks of length \(t\) and codes is proved in `RESULT.md`; the program's entire state enumeration is a finite certificate used for every \(t\), not a finite sample of torus lengths.

Directly independent `verify_exact_cover.py` enumerates exact partitions by vertex open neighborhoods rather than using the column recurrence. It confirms the code totals for six individual lengths. Outputs from executing both present program files are embedded in the package. Python 3 standard library suffices.

Scope: simple cycles with \(t\ge3\), fixed first circumference eight, and vertex-labeled counts. No theorem about other first circumferences is claimed. The full 2007/2008 paper cited in the originality comparison could not be inspected; later accessible primary treatments and its abstract were inspected. External scientific audit has not been performed.
