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

The argument is self-contained and applies without a size bound. Equation \(c_\chi(vw)=c_{\chi^{-1}}(v)c_{\chi^2}(w)\) is obtained directly from the multiplication \(e_xe_y=e_{2y-x}\). It gives both the idempotency equations and the pair-spectrum of right multiplication. The subgroup of squares has odd order precisely when the Sylow-two subgroup has exponent at most two; this is the structural step separating discrete and full spectra. Fourier inversion makes the order-four construction an actual algebra idempotent, not just a formal character assignment.

`verify.py` uses exact rational matrix arithmetic and symbolic fourth roots of unity through SymPy. Run with `python verify.py` in an environment containing SymPy. Its output in this package's validation was `PASS 27 exact checks for core-quandle idempotents and Peirce eigenvalues`. The six groups with fourth-order torsion were checked for three separate values of \(t\) each; nine groups without fourth-order torsion were checked for the expected right eigenvalue witnesses. All products were computed from multiplication tables, independently of the Fourier proof formula. This finite verification does not certify the infinite theorem without its proof.

The Peirce spectrum convention excludes the zero idempotent. A full independent mathematical audit has not been performed. The closest relevant primary texts are cited in `RESULT.md`; not every possible equivalent source was accessible in full.
