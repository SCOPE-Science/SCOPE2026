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

# Verification and reproducibility

All mathematical claims are established in `RESULT.md` by the support-classification proof and distinct-maximal-face intersection argument. The attached `verify.py` provides separate finite computational checks using only the Python standard library:

- It constructs the distance-at-most-two graph by directly calculating Hamming distances and independently enumerates all maximal cliques with a pivoted Bron–Kerbosch algorithm.
- It separately constructs the three predicted maximal-subset classes and checks exact set equality for every \(3\le n\le7\).
- It counts every size-at-least-four face by an independent explicit facet-subset enumeration and verifies uniqueness of its maximal extension for these dimensions.
- It exhaustively tests every subset of the \(n=3\) and \(n=4\) binary cubes and compares the entire anticode polynomial.

Run `python3 verify.py`. The verified finite outputs are \((1,8,24,32,16)\) for dimension three, and \((1,16,80,160,120,16)\) for dimension four. The full family theorem follows from the proof, not from finite checks. No independent audit or machine formal proof is claimed.
