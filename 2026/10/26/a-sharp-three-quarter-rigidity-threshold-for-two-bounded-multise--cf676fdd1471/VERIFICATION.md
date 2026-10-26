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

The script `verify.py` uses only the Python standard library. Execute `python3 verify.py` in the directory containing the package files. The resulting output must agree with `verify_output.txt`.

For each \(n=2,3,4,5\), the script enumerates all \(\{0,1,2\}^n\) vectors of even total multiplicity, verifies the two-bit dot-product parity identity for every ordered pair, builds the exact compatibility graph, enumerates its maximal cliques by a pivoted Bron–Kerbosch routine, and records the largest maximal clique containing a multiplicity-one vector. It separately constructs the proposed extremal family and directly verifies every pairwise minimum-intersection condition. The four observed maxima are \(3,6,12,24\).

The maximal-clique census is complete for those four finite instances only. The full infinite-family claim is established by the isotropic-space and coordinate-projection proof in `RESULT.md`, not by extrapolating finite counts. The code does not perform an independent mathematical audit or rule out inaccessible prior results.
