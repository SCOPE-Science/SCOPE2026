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

The analytic proof uses the source's scalar equation
\[
a x=\left(\frac{1+x}{b+x}\right)^k
\]
and the exact fold quadratic. The critical point is reconstructed from the double stationary root:
\[
b_0=\left(\frac{k+1}{k-1}\right)^2,\qquad
x_c=\frac{k+1}{k-1}.
\]
At that point the package checks
\[
F_{xb}=\frac{(k-1)^4}{4k(k+1)^2},
\qquad
F_{xxx}=-\frac{(k-1)^4}{2k^2(k+1)^2},
\qquad
-\frac{2F_{xb}}{F_{xxx}}=k.
\]
Together with the exact source discriminant, these identities give the square-root fold separation and the \(3/2\) threshold-width law.

`verify.py` uses only the Python standard library. It verifies the exact rational identities for a broad finite range of integer degrees, checks the \(k=2\) specialization, and numerically compares the exact source fold formulas with the asymptotic for representative degrees. Finite numerical checks are corroborative only and do not replace the analytic proof.

No claim is made about solutions outside the \(z_0=1\) branch, extremality, stability, or thermodynamic dominance.
