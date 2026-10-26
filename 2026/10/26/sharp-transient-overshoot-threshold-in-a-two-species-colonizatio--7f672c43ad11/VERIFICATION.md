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

The proof in RESULT.md establishes the parameter-wide theorem using a scalar reciprocal linearization, a moving-nullcline crossing argument, and the exact critical peak-time equation. The equality cases at \(y_0=y_{\rm crit}\), \(y_0=h(0)\), and \(r=\lambda\) are included.

`CHECK.py` is self-contained Python using only the standard library. It checks the exact parameter example, evaluates the convergent integral by quadrature, locates the peak through a scalar equation, and compares peak-time and height asymptotics near threshold. Execute as `python3 CHECK.py` from the containing directory. Success prints `VERIFY_OK` followed by figures. The numerical check is not an exhaustive certificate or substitute for the analytic proof.

The closest known source fully inspected is Tilman (1994), DOI 10.2307/1939377. Complete access to Hastings (1980) DOI 10.1016/0040-5809(80)90059-3 was unavailable, and possible older equivalent formulations remain an originality risk. Independent scientific audit and independent validation have not been performed.
