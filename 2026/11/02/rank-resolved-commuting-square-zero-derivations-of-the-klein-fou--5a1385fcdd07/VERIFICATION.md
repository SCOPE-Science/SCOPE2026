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

# Reproducibility
Run `python check.py` using Python 3 (standard library only). The program independently enumerates eight-parameter derivations of the indicated four-dimensional associative algebras over the fields of sizes two and four. It tests squares and pairwise commutators from the full four-by-four matrices, not from a presumed three-by-three classification. The four-element field is represented as binary polynomials modulo the irreducible polynomial \(t^2+t+1\), with addition and multiplication implemented directly. All fields represented here have characteristic two.

The checked results are 22 and 316 square-zero derivations, complete ordered pair totals of 148 and 9136, complete pairwise rank histograms, and 736 ordered commuting triples with a full rank-triple histogram over the field of size two. `check_output.txt` contains the actual run output. Finite enumeration only supports the general theorem: the proof of arbitrary \(q\) and \(m\) is in `RESULT.md`. Independent audit has not been performed.
