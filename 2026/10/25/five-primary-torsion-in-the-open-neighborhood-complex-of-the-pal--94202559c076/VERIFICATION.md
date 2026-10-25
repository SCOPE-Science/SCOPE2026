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

# Exact reproducibility record

Run `python3 verify.py` in the directory containing `morse_matrix.json`. The verifier requires Python 3 and SymPy (see `requirements.txt`). The run saved as `verification_output.txt` finished with `VERIFY_OK_PALEY25_NEIGHBORHOOD_FIVE_TORSION`.

It reconstructs the order-25 Paley graph over the field \(\mathbb F_5[u]/(u^2-2)\), checks graph degree and pairwise intersection parameters, enumerates 93,350 nonempty neighborhood simplices, tests all 43,546 free-face elementary collapses, constructs the 2,967-pair acyclic matching and topologically sorts all 6,258 nodes against 24,126 directed incidences.

It then recomputes the signed critical-four-to-critical-three boundary with 262 rows, 61 columns and 923 nonzero entries and compares the canonical `morse_matrix.json` byte-for-byte. Exact integral Smith normal form gives 56 unit factors and one factor five, proving \(H_3\cong\mathbb Z^{205}\oplus\mathbb Z/5\mathbb Z\) and \(H_4\cong\mathbb Z^4\). Direct sparse boundary ranks on the collapsed complex are separately checked over both \(\mathbb F_2\) and \(\mathbb F_5\), with a one-rank difference in the degree-four boundary.

The finite enumeration is exhaustive for this graph. The computation makes no statement about larger graphs, all possible literature, any uncomputed attaching maps beyond homology, or independent mathematical certification.
