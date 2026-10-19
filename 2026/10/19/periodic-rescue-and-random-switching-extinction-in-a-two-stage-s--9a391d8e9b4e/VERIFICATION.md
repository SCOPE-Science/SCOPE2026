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

The included `verify_exact.py` uses SymPy for exact equality of the two-step population matrices, constant-environment eigenvalue identities, the \(4\times4\) expected-state characteristic polynomial, and the exact threshold \(q=7/13\). A separately coded full path enumeration was compared with the expectation recursion for \(48\) parameter/time combinations using rational arithmetic. Three lengthy sample paths were inspected numerically and agreed with the almost-sure exponent within a conservative tolerance.

The mathematical proof additionally invokes the finite-state Markov ergodic theorem on the even and odd environmental subsequences; both are irreducible and aperiodic for \(0<q<1\). An irreducible nonnegative expected-state matrix supplies the Perron–Frobenius mean limit. Neither theorem is empirically certified by numerical experiments. The environmental endpoints \(q=0,1\) must be treated separately; the deterministic-growth limit at \(q=0\) is discontinuous in the generic case.

Independent audit has not been performed; no independent certification is implied.
