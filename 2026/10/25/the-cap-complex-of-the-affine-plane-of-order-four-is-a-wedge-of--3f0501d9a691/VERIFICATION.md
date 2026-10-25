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

# Computational verification of the cap-complex homotopy certificate

The exact accompanying files `verify.py` and `MATCHING.csv` constitute the finite certificate. Place them together and run `python3 verify.py`. Only the Python standard library is used. The certificate is generated using bitmasks indexed by \(4x+y\) with \(x,y\in\{0,1,2,3\}\), where the element labels of \(\mathbb F_4\) are \(0,1,t,t+1\).

The verifier checks field-line incidence and unique two-point lines, compares independently enumerated determinant and line collinearity triples, exhaustively constructs the cap complex on all nonempty subsets of sixteen points, and confirms its face vector and the counts of maximal faces. It reproduces and byte-compares all 783 face-pair records, rejects any repeated matched face or non-cover relation, constructs the full directed Hasse graph from 6768 incidences, and tests a topological ordering of all 1792 vertices. Exactly one critical vertex and 225 critical three-faces remain. The acyclic-matching CW theorem yields the homotopy conclusion.

Expected final output line: `VERIFY_OK`. This check is exhaustive for the sixteen-point field model, but it does not imply a theorem for arbitrary affine planes, guarantee prior-literature uniqueness, or constitute independent scientific validation.
