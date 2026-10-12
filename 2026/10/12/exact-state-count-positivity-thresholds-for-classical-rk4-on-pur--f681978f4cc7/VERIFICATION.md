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

`verify.py` uses only exact rational arithmetic. It reconstructs \(P_N\), \(Q_N=P_N-I\), the degree-four RK4 polynomial, and the coefficient representation
\[
R_4(xQ_N)=\sum_{j=0}^{4}a_j(x)P_N^j.
\]
It checks the identity for several rational \(x\) and dimensions \(2\le N\le7\), verifies row sums exactly, and replays boundary/failure witnesses for the four-state and five-state cases.

The exact classification does not depend on those finite checks. The proof uses the displayed coefficient formulas, the absorbing-path power structure, and strict monotonicity of the two cubic boundary polynomials.

The verifier does not assess arbitrary CTMC generators, floating-point rounding, internal RK4 stages, or nonuniform rates.
