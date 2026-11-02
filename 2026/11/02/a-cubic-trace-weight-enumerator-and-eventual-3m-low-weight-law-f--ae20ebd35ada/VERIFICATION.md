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

The `verify.py` program uses Python 3 standard library only. Its two logically distinct construction paths are (a) direct exhaustive support enumeration of all \(\omega s+\Gamma_m s\) graph-code words for each \(3\le m\le14\), and (b) exact integer polynomial arithmetic on the three cubic-trace recurrences. All enumerator coefficients agree in each finite case. The same script tests the displayed low-weight laws for every \(3\le m\le110\), normalizes every enumerator to \(2^{m+1}\), and checks their leading coefficients. The recorded output is `VERIFY_OK: independent exhaustive graph support through 15 vertices; exact cubic recurrences through rim length 110; low sectors and normalization checked`.

Use `python3 verify.py`. No external packages, downloaded data or random seeds are required. The algebraic proof in `RESULT.md` establishes the claim for all rim lengths; **finite verification alone cannot certify an infinite family**. An independent mathematical audit has not been performed.
