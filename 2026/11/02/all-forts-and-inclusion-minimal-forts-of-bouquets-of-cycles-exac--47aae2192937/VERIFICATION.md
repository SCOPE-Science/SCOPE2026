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

The accompanying standalone `CODE/bouquet_verify.py` is runnable with Python 3 (standard library only). It constructs each bouquet's adjacency from its cycle edges, checks the fort definition for each nonempty vertex subset, and determines inclusion-minimal forts by comparison against all proper fort subsets. It checks all coefficients against a separate implementation based on independent and maximal independent sets of peripheral and interior paths. It also directly simulates the standard zero forcing rule and compares the complete inclusion-maximal failed-set spectrum and extremal multiplicities on a second graph suite. Weighted recurrences for the three path-polynomial families are cross-checked against direct independent-set enumeration through path length sixteen.

Run: `python CODE/bouquet_verify.py`.

Recorded result from executing the distributed script: 47 graph instances, 167593 nonempty vertex subsets, followed by `SECOND_CHECKS_OK weighted H/Q/E recurrences through 16; zero forcing on 8 graphs`. The script uses assertions and raises an error if a check fails. Example size spectra: for petals of lengths \(3,3\), minimal-fort coefficients are \(2z^2+4z^3\); for lengths \(3,4,6\), the spectrum is \(2z^2+z^3+z^4+2z^5+4z^6\).

The proof of the formulas is the structural bijection in RESULT.md. Computational comparisons do not constitute a proof for unbounded numbers or lengths of petals. Publication originality is not a computational property; the strongest inspected source is Becker et al., arXiv:2404.05963, Section 5, which gives general vertex-sum minimal-fort constructions and a known all-triangle count.
