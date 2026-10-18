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

Execute `python3 verify.py` with `witnesses.json` in the same directory. Only the Python 3 standard library is used; the computation requires no downloaded graph tables or external programs.

The verifier generates all finite partial orders of size at most eight by adjoining a maximal element over each lower ideal and removes isomorphic duplicates by exact bijective backtracking preserving the strict-order relation. It rejects nontransitive generated relations, computes global colour-refinement signatures for all three off-diagonal order types, and tests the four explicitly listed witnesses against the two observed ambiguous classes.

Expected order totals: 1, 2, 5, 16, 63, 318, 2045, 16999. Expected distinct counting-logic signature counts: 1, 2, 5, 16, 63, 318, 2045, 16997. At eight elements, the generator visits 48,346 extensions and produces exactly two logical ambiguity classes, both of multiplicity two. The verifier performs both a direct signature check and an exact nonisomorphism check for every supplied pair.

The mathematical justification is that the ideal-extension enumeration covers every poset, the full bijection test identifies precisely its isomorphism classes, and stable colour refinement over all three binary atomic relations captures exactly \(C^2\) equivalence. A run of the script is a finite exhaustive certificate within the stated cutoff, not a theorem for larger orders. The reference literature supplies the general \(C^2\)-equivalence theorem and the independent unlabeled-poset counts. This evidence has not been independently audited.
