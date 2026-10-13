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

The proof was checked directly against the exact truncation penalty stated in arXiv:2610.03674v1 and against the source's \(O(d^2m\log m)\) decoder-complexity statement. With \(\varepsilon=r^{d/2}\), the two required asymptotic identities are
\[
g(\bar n/\varepsilon)=\frac{\ln(\bar n/\varepsilon)+1+O(\varepsilon)}{\ln2}
\]
and
\[
h_2(\varepsilon)=\frac{\varepsilon\ln(1/\varepsilon)+\varepsilon+O(\varepsilon^2)}{\ln2}.
\]
They imply the displayed certificate expansion without numerical assumptions. Taking logarithms of the asymptotic equation for the target gap gives the continuous inverse law; the unrestricted integer threshold differs by \(O(1)\), and the prime restriction is used only at leading order through the prime number theorem.

`artifacts/verify.py` evaluates the exact penalty at high precision for several fixed energies and checks convergence to \(6\lambda/\ln2\). These calculations are finite consistency checks only. No optimality, converse, or finite-precision decoder claim is inferred from them.
