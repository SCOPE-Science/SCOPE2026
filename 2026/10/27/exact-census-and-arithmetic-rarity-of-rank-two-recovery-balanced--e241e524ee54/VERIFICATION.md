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

# Verification evidence and boundaries

The accompanying `verify.py` independently evaluates coordinate-recovery expectation by summing recovery events over all subsets of column positions, then compares the result with the exponential-arrival integration derived in the proof. It exhausts projective multiplicity profiles over the binary field at lengths \(2\)–\(8\) and the ternary field at lengths \(2\)–\(6\). It also exhausts ordered full-row-rank generator matrices over prime fields at the parameter grids listed in `verification_output.txt`, dividing by \(|\mathrm{GL}_2(\mathbb F_q)|\) only after checking the free orbit sizes analytically.

The exact enumeration reproduces \(B_2(6)=25\), \(B_3(4)=20\), and \(B_5(4)=240\). A separate numerical comparison of the exact probability with the asymptotic equivalent checks the scale at selected larger lengths. The execution record ends with `RANK2_BALANCE_VERIFY_OK`.

The exhaustive matrix code supports prime fields \(q=2,3,5\); it does not implement extension-field multiplication. The theorem for all finite fields rests on the projective-line and orbit-count proof. Likewise, numerical asymptotic agreement is a sanity check, not a proof of the limit. The status of any independent audit remains unperformed.
