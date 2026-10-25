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

The supplied `verify_spike_selector.py` uses only Python's standard library and was executed with `python3`. It checks the elementary planar formula
\[
s_x(\operatorname{conv}(B_2\cup\{t e_1\}))=\frac{t\arccos(1/t)-\sqrt{1-t^{-2}}}{\pi}
\]
against an independently sampled support-function integral, for \(t=2,5,50,10000\), with absolute errors below \(10^{-8}\). It additionally evaluates the proof's **rigorous analytic interval** for the ratio at \(t=10^9\) in dimensions \(d=2,3,4,7\), verifies that it brackets \(2^{-d}\), and confirms the strict planar comparison \(1/4<4/9\). All scripted checks passed.

The infinite-dimensional-parameter limiting assertion is *not* inferred from the numerical cases: its mathematical verification is the sandwich via \(D_d(\ell_t)\), \(D_d(u_t)\), \(D_d(q_t)\), continuity of the Steiner integral, and the Brunn--Minkowski translation upper bound. The script does not establish originality or independent validation.

The shape family is analytic and self-contained. No external file, remote computation, proprietary solver, or unprovided certificate is needed to reproduce the checks.
