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

# Reproducibility and proof boundaries
The analytical proof uses only quadratic Gauss-sum evaluation, finite Fourier inversion, the endpoint convolution row-sum identity and elementary two-variable norm optimization. The two residue classes each have \((p-1)/2\) elements. Parseval gives the exact kernel squared sum \((p-1)/p\); equality in Cauchy–Schwarz makes the necessary and sufficient flatness condition unambiguous. The exceptional \(p=3\) maximizers must include both the degenerate phase pair and the two nondegenerate phases; this is explicitly handled.

Execute `python3 CHECK.py` in the extracted directory. The checker constructs inverse Fourier transforms directly and recomputes the norm profile for forty-five odd primes below two hundred at seven relative angles, checks all forty-five phase optima, the flat-kernel property in the congruence-one class, and five five-cycle imaginary-power parameters. The observed output was `CHECK_OK primes=45 comparisons=727`. All tests passed in the inspected package. The program uses finite-precision complex arithmetic and numerical tolerances: it is supplementary evidence, not an independent audit, a formal proof, or a certificate for infinitely many primes.

Boundary distinctions: the zero Fourier frequency is set to zero even for exponent zero in the five-cycle application, so the exponent-zero operator is the mean-zero projection rather than the identity. Norms are complex-induced norms on all functions, not inherited norms on the mean-zero subspace. The five-cycle correspondence does not extend automatically to larger primes because the graph-Laplacian eigenvalues cease to be constant on the two multiplicative quadratic-character classes.
