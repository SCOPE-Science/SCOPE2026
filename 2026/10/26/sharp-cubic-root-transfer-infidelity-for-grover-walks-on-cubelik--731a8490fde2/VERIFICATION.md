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

# Reproducibility and verification

Run `python3 verification.py` with a standard Python 3 interpreter. No external packages, network access, simulated quantum hardware or stored input data are required. The script constructs the explicitly stated generator family and its exact Fourier-binomial character distribution; it also performs direct moving-shift and Grover-coin evolution for the smallest member.

Observed direct-evolution position probability for \(h=2\): \(0.6654649078163376\). Independently computed Fourier/binomial probability: \(0.6654649078163382\), discrepancy below \(10^{-12}\). Exact Fourier reductions give the following finite outcomes:

| \(h\) | \(\Delta\) | \(T\) | \(p_T(\sigma)\) | \(h(1-p_T)\) |
| ---: | ---: | ---: | ---: | ---: |
| 2 | 9 | 15 | 0.665464907816 | 0.669070184 |
| 4 | 65 | 103 | 0.881758106069 | 0.472967576 |
| 8 | 513 | 805 | 0.964708846916 | 0.282329225 |
| 16 | 4097 | 6435 | 0.980333052775 | 0.314671156 |
| 32 | 32769 | 51473 | 0.989810022429 | 0.326079282 |
| 64 | 262145 | 411777 | 0.994703893132 | 0.338950840 |
| 128 | 2097153 | 3294201 | 0.997365422308 | 0.337225945 |

All implemented finite assertions passed. The values oscillate mildly as the nearest parity-matched integer changes; the limiting constant is not estimated by blindly extrapolating the first few cases. The analytic Gaussian integral is

\[
c_*=\frac{2}{\sqrt{2\pi}}\int_{-\infty}^{\infty}
\left[1-\cos\left(\frac{\pi z^3}{12}\right)\right]e^{-z^2/2}\,dz
\approx0.3340087115.
\]

The verification program computes finite exact binomial weights using logarithmic gamma values; its outputs are floating-point approximations, not interval certificates. The universal degree bound, graph connectivity, nonzero target, limit law, error exponent sharpness and positivity of the integral rely on the written mathematical proof rather than finite tests. No independent audit has been performed.
