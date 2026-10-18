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

# Scientific verification

Execute `python3 verify.py` after extracting the embedded files. The executable is standalone Python 3 and consumes no external data. It exhaustively scans 1,048,576 vertex subsets with independent induced-degree and connected-component predicates; checks 62,049 augmented simplices, the complete face and facet vectors, 31,000 Morse pairs, the complete 400,760-incidence directed acyclicity, and all 44 signed integer Morse differential columns. Three specified columns are the basis vectors forming a determinant -1 minor and certify split surjectivity of the degree-seven differential. Independently, direct mod-two simplicial ranks in degrees 5 through 9 are recomputed.

Verified success output: `DESARGUES_IND2_INTEGRAL_HOMOTOPY_VERIFIED` with face, Morse and homology counts. The proof uses the integer Morse differential and the cellular attaching classification in dimension 6, not an unproved inference from mod-two homology. The scope is one graph and one second-independence construction. No independent scientific audit has been performed.
