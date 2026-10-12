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

# Verification record

The claim and its scope are stated in `RESULT.md`. Proof-critical checks that do not require computation are: (i) the extremal-mass polytope reduction and total-variation passage, (ii) universal count bounds \(7,5,4,3\), (iii) the unique-reflected-center characterization of equality at \(7\), (iv) the three incompatible binary equations forced by simultaneous two-heavy equality at \(4\), (v) the resulting weighted one-unit deficit and expansion to two exact polynomials, and (vi) explicit extremizers realizing both bounds.

Run `python check_concentration.py` under Python 3. The standalone script performs integer-exact checks for \(197568\) two-law choices, optimizing the third law over all allowable heavy/light assignments on arbitrary three-element site sets in \(\{0,\ldots,7\}\). It verifies seven rational atom caps \(1/3,7/20,19/50,2/5,21/50,9/20,1/2\), and additionally tests the simultaneous-heavy-set obstruction in \(81\) configurations of equally spaced site progressions. The checks passed during preparation of the result.

The program's finite search is a reproducibility aid, not an infinite proof. The analytic argument in `RESULT.md` establishes all integer site sets, all real \(\alpha\) in the asserted interval, and arbitrary countable marginal supports. The result has not been independently audited or externally certified.
