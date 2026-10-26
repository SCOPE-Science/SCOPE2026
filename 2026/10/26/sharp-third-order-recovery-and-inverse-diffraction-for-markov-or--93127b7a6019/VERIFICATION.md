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

The derivation in `RESULT.md` is analytic and applies to every admissible real parameter. It checks the exact stationary transition matrix, the phase averaging for each displacement, the absolutely convergent Poisson-kernel Fourier series, the reversible Markov conditional-independence identity, the sign-recovery formula, the diameter-two impossibility, and the attained optimization over the full admissible domain.

The standalone exact rational checker `verify.py` enumerates stationary finite Markov trajectories directly, independently of the closed-form autocorrelation and triple predictions. Execute with `python3 verify.py` in the directory containing this file. Observed output:

`VERIFY_OK: 10 rational Markov laws; 40 transition probabilities; 130 exact autocorrelation/Fourier identities (including primitive boundary cases); 30 three-site identities; complete signed-parameter inversion at all samples`

A finite list of rational cases does not prove all-parameter claims; those follow from the algebraic and measure-theoretic arguments. The global maximum is an exact symbolic calculation with unique positive critical point \(\sqrt2-1\) and is attained at a primitive one-zero-transition boundary chain. No external independent validation has been performed.
