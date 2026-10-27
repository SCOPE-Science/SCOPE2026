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

# Reproducibility and verification

The proof gives a universal symbolic calculation for irrational \(\alpha\): the visit counts to short intervals telescope to \(\lfloor n\alpha\rfloor\) plus membership in rotating arcs, after which a circular event count gives all Parikh vectors. Distinct cut phases and the two possible repeated extreme states are accounted for; Weyl equidistribution supplies the density statement.

Run `python3 verify.py` in a standard Python 3 environment. The standalone test uses the modulus \(10007\), enumerates all constant-itinerary phase intervals for selected \(p/10007\), and independently computes each distinct factor and multiplicity vector for \(2\le m\le11\) and \(1\le n\le31\). The expected output ends in `VERIFY_OK`. Tests at rational proxy angles are finite cross-checks, not analytic evidence for all irrational values; the full proof is required for the universal conclusion.

The exact historic priority of the formula is not independently certified, and an independent scientific audit has not been performed.
