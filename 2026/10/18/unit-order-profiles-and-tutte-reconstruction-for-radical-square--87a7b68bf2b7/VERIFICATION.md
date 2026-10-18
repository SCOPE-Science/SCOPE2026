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

The general result is supported by a proof, not an experimental extrapolation. Directly checked algebraic identities are: the single-arrow coefficient of \((\lambda+a)^r\) in an algebra with \(J^2=0\), the finite-field geometric sum at equal and unequal diagonal roots, the conjugation identity for \(1+x\), and \((1+x)^p=1\). The resulting divisor counts are converted to exact-order counts by ordinary Möbius inversion. The two-variable polynomial is reconstructed by interpolation at infinitely many prime-power field sizes and a classical Fortuin–Kasteleyn transformation.

A standalone Python 3 checker, `torsion_tutte_checker.py`, independently iterates over finite-field unit coordinates, multiplies them in the arrow basis, finds each exact multiplicative order, and compares the histogram with the proof formula. It checks 49 quiver/field cases, including extension field \(\mathbb F_4\), loops, parallel arrows, reversed arrows, and an oriented five-cycle over \(\mathbb F_3\). Expected output: `ALL_DIRECT_UNIT_ORDER_CASES_PASSED 49`. Its finite checks do not establish polynomial recovery over infinitely many fields; that relies on the stated algebraic proof.

Previously known Potts/Tutte identities are used with attribution. No independent audit or historical priority certification is claimed.
