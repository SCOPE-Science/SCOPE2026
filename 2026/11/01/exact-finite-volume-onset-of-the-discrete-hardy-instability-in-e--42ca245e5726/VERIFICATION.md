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

# Reproduction

Place `verify_certificate.py` and `certificate.json` in the same directory; execute `python verify_certificate.py` with a standard Python 3 interpreter. It enumerates signed-permutation orbits exactly, verifies detailed balance for every orbit adjacency, replays the 90 strictly positive supersolution inequalities at squared radius 23, computes the 98-orbit negative exact Rayleigh defect at radius 24, and verifies the small-dimensional witnesses. No numerical eigensolver or third-party dependency is used.

Observed output includes `CERTIFICATE_OK`, the minimum integer supersolution slack `100963`, and the negative scaled defect `-3740776448633821897328` (multiplier `5354228880`). Separate direct lattice-edge comparisons of the orbit quadratic-form identity passed in the full finite graphs at dimensions three, four and five.

The all-dimension assertion also invokes published infinite-lattice Hardy theorems for dimensions three through eight and explicit algebraic inequalities for high dimensions. Finite checks alone are not an infinite-dimensional proof, and the exact certificates do not establish publication priority. No independent external mathematical audit has been performed.
