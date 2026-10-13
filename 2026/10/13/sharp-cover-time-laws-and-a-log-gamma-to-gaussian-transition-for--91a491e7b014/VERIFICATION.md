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

Run `python verify.py` with Python 3 and no third-party packages. It executes 906 checks: exact rational dynamic programs for optimal decisions and odd/even cover CDFs over \(2\leq m\leq6\) at five steering probabilities; independent convolution of geometric laws; and numerical finite-size Laplace-transform comparisons for four critical parameters and two transform arguments.

Critical analytical steps independent of those tests are: monotone coupling for the *whole* adaptive policy class, independence of the two alternating-part clocks, exact gamma-ratio asymptotics on a neighborhood of the origin, and a vanishing Lyapunov ratio when \(m\varepsilon_m\to\infty\). No finite computation is treated as proving these limits. The checker prints the number of passed checks and exits nonzero on a failed assertion.

The limiting conclusions are for \(\varepsilon_m\to0\) only, whereas the finite exact cover-time formula holds for all \(\varepsilon\in[0,1]\). No independent scientific audit or infinite formal certification is asserted.
