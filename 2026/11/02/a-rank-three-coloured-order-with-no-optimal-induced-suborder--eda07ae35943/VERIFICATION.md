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

# Reproducibility and mathematical checks

The executable source `verify_rank3.cpp` contains both words as literal strings and implements exact rank-two characters as an unsigned \(32\)-bit presence mask. It constructs rank-three characters from ordered triples of left-mask, colour and right-mask, using exact set comparison. It verifies the reference has \(70\) distinct characters, the candidate shares the same character set, and **all** \(62\,196\) possible three-deletion induced suborders fail rank-three equivalence. The maximum size of their intersection with the reference character set is \(68\). No probabilistic hash, heuristic cutoff, timeout inference or limited sample is used in this decisive enumeration.

Run `g++ -O2 -std=c++17 verify_rank3.cpp -o verify_rank3` followed by `./verify_rank3`. Separately, `python3 verify_independent.py` computes the signatures through explicit Python frozensets rather than the packed bit representation. It also verifies the first-move game recursion for all \(961\) ordered pairs of words of length at most four and tests \(1203\) of the \(62\,196\) deletions. The Python deletion sample is not treated as the exhaustive proof.

The proof uses the standard correspondence of rank-\(q\) fingerprints with \(q\)-round Ehrenfeucht–Fraïssé games, available in Mwesigye–Truss, Theorem 1.1. It gives no general characterization of minimal representatives and claims no independent validation beyond these reproducible checks.
