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

## Mathematical verification

The exact ambiguity formula follows by completing a Gaussian square with complex coefficient of positive real part. Its modulus is positive, and Gaussian integration over Doppler frequency yields the displayed one-variable moment integral. The Tricomi and modified Bessel formulas follow by their standard integral representations. Dominated convergence below and above the critical exponent proves the two power-law regimes; the Bessel small-argument expansion proves the critical logarithmic regime. The exact domain is all real chirp parameters, all real delay and Doppler variables, and each fixed positive moment exponent.

The included `check_moments.py` evaluates four original defining integrals independently of the closed form. It compares the analytic moment integral and special-function evaluation for \(p\in\{1,2,3,4,5,6,8\}\), and explicitly checks the \(p=2\) normalization and \(p=4\) Bessel identity. The recorded output is provided in `checker_output.txt`. Finite quadrature cannot certify any of the unrestricted formulas or a literature-priority assertion; those are established analytically or left as a publication-priority limitation, respectively.

## Scientific scope and limitations

The result does not make a claim for time-limited chirps, arbitrary amplitudes or cross-ambiguities, nor does it assert uniformity as the moment exponent varies with chirp strength. A separate independent audit has not been performed.
