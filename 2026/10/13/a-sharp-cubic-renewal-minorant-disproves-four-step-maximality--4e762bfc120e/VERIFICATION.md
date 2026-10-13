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

# Mathematical verification

The self-contained checker `verify.py` uses rational coefficient dictionaries in four variables and exact integer/rational arithmetic. Run it with `python3 verify.py` from the directory containing this document. A successful run reports:

`PASS: 3 exact polynomial identities; 20474 rational simplex points; positive witness; sharpness cases`

The three verified polynomial identities are the displayed factorizations of \(u_j-P\) for \(j=1,2,3\). Each certificate has nonnegative monomial coefficients in nonnegative probability variables. The proof that the first three masses control all later renewal masses follows by induction from the displayed convex-combination recurrence and does not depend on numerical tests.

The checker also evaluates every nonnegative integer quadruple whose coordinates sum to a denominator from 1 through 24 after normalization, verifies the nonnegative lower-envelope inequalities at each rational point, and checks an interior strict witness. A separate polynomial identity on the face \(c=0\) plus explicit rational choices shows why any perturbation coefficient greater than \(2\) is impossible. The finite grid does not establish continuum validity: the exact polynomial identities do.

The bibliography and originality comparison are reviewed against the full preprint and the publisher-hosted journal text. Independent audit and independent publication-priority verification have not been performed. No general extremal classification for larger supports is asserted.
