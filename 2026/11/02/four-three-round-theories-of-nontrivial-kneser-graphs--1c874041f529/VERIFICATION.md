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

The finite verification uses only the Python standard library and requires Python 3.8 or later. Run `python3 verify_kneser.py` and `python3 verify_ef3.py` from the directory containing the extracted files.

`verify_kneser.py` uses vertex masks for every \(k\)-subset, explicit disjointness adjacency bitsets, and independent fresh-third-vertex profiles. It checked \(28\) parameter pairs with graph orders at most \(924\), matching the algebraic profile criterion and exactly four class signatures. The matching regime is separately tested rather than inferred from its connected counterparts.

`verify_ef3.py` constructs an explicit finite Hintikka rank-three invariant by recording all atomic equality/adjacency diagrams of triples, including repeated selections, and then nesting sets of attainable extensions at the second and first moves. Nine examples span all four classes and several different parameters within each class. The resulting four signatures are pairwise distinct.

Expected output files are `verify_kneser.out` and `verify_ef3.out`, each ending in `PASS`. These bounded computations are corroborative only. The proof of the infinite parameter statement consists of vertex transitivity and the exact threshold \(t\ge3k-n\) for a common neighbor of two \(k\)-subsets with intersection size \(t\). The chromatic consequence uses the established Kneser–Lovász formula. Independent mathematical audit and exhaustive historical-priority review have not been performed.
