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
# Verification details

Run `python3 verify.py` with a standard Python 3 interpreter. No nonstandard packages, datasets, or external services are required.

The verifier exactly enumerates sorted quadruples of positive integer box lengths with product at most \(4928\). The proof first excludes every length-one box from being a counterexample, then derives necessary bounds \(a^4\le4928\), \(ab^3\le4928\), \(abc^2\le4928\), and \(c\le d\le\lfloor4928/(abc)\rfloor\). The finite loop therefore exhausts all would-be counterexamples with no larger normalized volume than the explicit candidate. It returns \(10618\) quadruples and exactly one negative-coefficient example: \((7,8,8,11)\).

An independent exact Newton-forward-difference calculation recovers the linear coefficient of the Ehrhart polynomial from direct integer-lattice-slice counts for eight quadruples, checking the identity \([t]L_J=-\Delta/30\). The verifier also checks the seventh differences vanish for these test polynomials, the pair-balancing identity in \(3402\) integer cases, and the exact one-side-equal-to-one obstruction for sampled triples. These checks corroborate identities that are proved algebraically for **all** positive integer side lengths in `RESULT.md`; only the explicitly bounded integer extremum uses exhaustive computation.

The final conclusion is limited to the stated box-by-unit-segment join family. An independent external audit was not performed.
