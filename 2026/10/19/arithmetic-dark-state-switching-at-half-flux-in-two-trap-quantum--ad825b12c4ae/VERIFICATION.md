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

# Verification and scope

The proof uses three independent logical steps: (i) Fourier eigenvalue pairing at precisely \(\Phi=0\) or \(\Phi=\pi\), (ii) exact congruence enumeration after factoring \(\gcd(N,d)\), and (iii) dissipative spectral separation of the strictly decaying complement. These establish the theorem for every allowed integer size without extrapolating from finite tests.

Run `python verification/check_cycle.py` with Python 3, NumPy, and SciPy installed. The script tests 5,307 individual two-sink Fourier evaluation maps across ring sizes 3 through 60 and three fluxes. It then checks modular index enumeration independently for every ring size 3 through 120 at both distinguished fluxes, before numerically propagating eight small conditional no-jump matrices to illustrate the limiting mixed-state survival. Its finite-time tolerance is a numerical approximation only, not an error theorem valid for arbitrary sizes or times.

For direct manual checks: at \(N=6\), \(d=2\), the zero-flux dimension is \(0\), whereas half flux gives \(1\), making the limiting maximally mixed survival \(1/6\). At \(N=8\), \(d=2\), the corresponding dimensions are \(1\) and \(0\). At \(N=12\), \(d=4\), they are \(1\) and \(2\). No independent audit or external certification is implied by these checks.
