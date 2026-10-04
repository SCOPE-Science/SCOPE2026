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

The bundled `verification/verify.py` uses only the Python standard library and exact rational arithmetic. It checks two source-specific witnesses at \(b=2\), so \(\omega=1\) and no floating-point or radical approximation is involved.

For \((a_1,d_1,c_1,j_1,e)=(1,2,1,-2,-1)\), it verifies
\[
U_*=1,\qquad r_*^2=4,\qquad
\det D\bar f=-3,
\]
and the nontrivial quadratic factor \(\lambda^2+\lambda+1\), whose roots have real part \(-1/2\). It also verifies that the existence expression printed in the source has the opposite sign and therefore excludes this stable corrected branch.

With only \(e\) changed to \(+1\), the checker verifies that the source's printed positive-radius existence expression is positive while the corrected value is \(r_*^2=-4\). Thus the correct first-order average has no real positive-radius zero at that witness, although no claim is made about periodic orbits arising by a different or higher-order mechanism.

The general symbolic derivation is given in `RESULT.md`; the finite exact witnesses are supplementary checks, not a substitute for that proof. The recorded replay output is `VERIFY_OK`.
