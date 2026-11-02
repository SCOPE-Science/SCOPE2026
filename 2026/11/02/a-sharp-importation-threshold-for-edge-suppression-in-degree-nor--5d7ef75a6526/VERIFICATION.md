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

The accompanying `verify.py` executes solely exact symbolic rational operations using Python 3 and SymPy: `python3 verify.py`. It builds the actual transition generators from the stated susceptible and infected rates, reduces four-vertex state spaces to six and nine automorphism-orbits, obtains stationary expectations algebraically, and reconstructs the complete rational numerator and denominator factors.

The checker verifies: (i) \(P_D-P_{C_4}=-\alpha\beta^2F/(UV)\) exactly; (ii) both denominator polynomials have strictly positive coefficients; (iii) all five nontrivially signed numerator coefficients have unique positive zeros in the stated disjoint rational brackets; (iv) at \(\alpha=7/8\), the shifted coefficient polynomial is coefficientwise nonnegative; (v) the exact positive difference for \(P_3\to K_3\); and (vi) agreement with independent unreduced \(16\)-state stationary solutions for five sets of rational rates, plus the illustrative \(\alpha=\beta=1\) fractions.

The universal beta-root count is analytical via Descartes' sign rule and sign at zero/infinity. Testing five rational rates does not prove arbitrary-rate identities by itself; those are checked by exact symbolic elimination. The work does not provide an external independent audit, a formal theorem prover certificate, or an empirical disease-dynamics validation.
