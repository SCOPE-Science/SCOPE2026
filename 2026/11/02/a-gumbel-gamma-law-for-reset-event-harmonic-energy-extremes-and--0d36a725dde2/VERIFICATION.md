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

# Mathematical and computational verification

The proof of the asymptotic laws is in `RESULT.md`. The exact cycle law is represented independently by a beta-mixture Gaussian energy and the equivalent Kummer–Tricomi density. Numerical integrations can support consistency but cannot certify convergence of the extreme-value point process or the strict timescale separation for every parameter.

## Reproduction

From a directory containing `verify.py` and `requirements.txt`, with Python 3.10 or later:

```
python -m pip install -r requirements.txt
python verify.py
```

The executed version reported `PASS: 88 deterministic numerical checks`. It checks multiple reset-to-relaxation ratios; mixture density against Tricomi \(U\), conditional Gaussian exponential integrability and mean identities, normalized energy-tail convergence, and the first conditional-age moment. The numerical tail check uses a scaled complementary-error-function transformation to control underflow. This script does not provide a formal proof of the limits.

## Independent mathematical checks

The identity \(U=e^{-2\mu T}\sim\operatorname{Beta}(r/(2\mu),1)\) follows by direct change of variables from the exponential waiting time. The integral bound \(\operatorname{erfc}(\sqrt y)\le e^{-y}/\sqrt{\pi y}\) yields a parameter-dependent but integrable \(v^{\beta-1}e^{-v}\) majorant for the tail and marked-age asymptotics. The marked limiting intensity factorizes into the standard Gumbel intensity and a unit-rate Gamma mark, establishing independence of the two coordinates. The largest waiting time is order \(\log n\), while the maximizing-energy waiting time is order \(\log\log n\).

## Unproved limits and scope

No quantitative finite-\(n\) error estimate, finite-duration reset protocol, physical erasure-work law, multi-particle extension, non-Poisson waiting-time theorem or independent priority audit is claimed.
