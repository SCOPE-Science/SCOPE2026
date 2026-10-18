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

The proof establishes the normal form and the two count formulas for all integers \(k\ge2\) by explicitly reducing the five axioms to independent allowed row pairs. No computational evidence is used to justify an infinite quantifier.

Run `python3 verify_rank_two_preconditionals.py` with a standard Python 3 installation. This enumerates all tables meeting the first four axioms after an independently justified two-value row reduction, then directly checks axioms 1–5 for every triple of lattice elements. It also checks whether each accepted table is induced by an antitone precomplementation. Observed results:

- \(k=2\): total 41, induced 25, stratified total counts \(4,6,6,25\).
- \(k=3\): total 278, induced 150, stratified total counts \(8,18,18,18,216\).
- \(k=4\): total 2633, induced 1361, stratified total counts \(16,54,54,54,54,2401\).

The script uses only the Python standard library. Larger finite cases and isomorphism orbit counts have not been checked. An independent audit has not been performed.
