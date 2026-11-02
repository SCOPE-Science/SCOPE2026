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

# Reproducible checks

Run `python3 verify_biclique.py` from the directory containing the standalone script. The verifier requires only Python 3 and uses integer arithmetic throughout.

Observed passing checks: 15,300 explicit vertex colorings; 191,080 pairs checked for individual profitability; 26,760 truly profitable cross-part swaps; 272,868 profile states; 310,832 improving profile transitions; 30,696 profile states exhibiting multiple reachable terminal profiles in the truncated set used for checking. Each profiled state has matching minimum and maximum terminal lengths equal to the algebraic ticket count; every transition reduces both counts exactly once. A concrete irregular-biclique example independently confirms the decrease of the conventional monochromatic-edge count from 6 to 5.

The complete mathematical justification is the strict-inequality and ticket-decrement proof in `RESULT.md`. Finite enumeration is corroboration, not a proof for unbounded graph sizes or numbers of types. The model assumes no vacancies, no stubborn agents, and strictly mutually profitable exchanges only. No independent external audit has been conducted.
