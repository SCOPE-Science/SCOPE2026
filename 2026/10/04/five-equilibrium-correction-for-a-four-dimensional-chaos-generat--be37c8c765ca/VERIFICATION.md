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

Run `python3 verify.py` in the package directory. The checker uses only Python's standard library and exact rational arithmetic for every root-count certificate.

It verifies that eliminating the printed equilibrium equations produces
\[
P(x)=x^5+9x^4-720x^3-492480x^2+113400x+1166400,
\]
constructs the exact Sturm sequence, confirms three and only three real roots, confirms one root in each stated rational isolating interval, and applies the exact sign constraint \((x^2-360)/x>0\) to retain precisely two roots. It then reconstructs the four nonzero equilibria and checks their vector-field residuals numerically after the exact root-count proof is complete.

The checker separately verifies the exact characteristic factor
\[
\lambda^2+37\lambda-\frac{323999}{900}
\]
at \(E_0\), its negative constant term, and the approximate values of its positive and negative roots.

The numerical equilibrium coordinates are not used to prove completeness. Completeness comes from the exact Sturm count plus the exact branch reduction. The package does not verify attractor existence, basin geometry, hidden-attractor status, or encryption security.
