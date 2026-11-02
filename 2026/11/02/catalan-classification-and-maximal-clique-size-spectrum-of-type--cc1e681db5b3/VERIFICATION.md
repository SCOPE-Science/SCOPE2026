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

Run `python3 verify.py` using only the Python standard library. The verifier constructs the longest parabolic permutations and calculates actual 0-Hecke Demazure products from reduced words, not by assuming the proposed compatibility criterion.

For each \(1\le m\le7\), it enumerates every pair of the \(2^m\) parabolic idempotents, confirms the component criterion, enumerates **every** maximal clique by the Bron–Kerbosch algorithm, enumerates every ordered binary-search-tree ideal family independently, and compares the sets of families and their size histograms exactly. It additionally checks idempotents among **all** \((m+1)!\) monoid elements for \(1\le m\le5\), and the predicted Catalan counts and minimum-size multiplicities through \(m=10\).

Expected terminal diagnostic: `VERIFY_OK`. These finite checks corroborate exact low-rank instances, not the infinite theorem. The general proof is the separate mathematical argument in `RESULT.md`. No independent external audit or verification is represented by this document.
