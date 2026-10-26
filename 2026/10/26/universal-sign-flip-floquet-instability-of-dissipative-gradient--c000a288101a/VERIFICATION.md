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

The theorem's complete proof and boundary assumptions are in RESULT.md. The analytic bottleneck is the identity \(B_-=B_+^{\mathsf T}\) and the exact singular-mode equation \(\det(I-Q)=-\rho(2-\rho)t^2\). The latter is negative throughout the stated open parameter domain; one positive-definite Hermitian period multiplier therefore lies below \(1\) and another above \(1\). The synchronized starting vector's Rayleigh quotient is \(1+t^2/2\), so no nonzero synchronized singular mode can be confined to the stable multiplier. Nonvanishing modal coupling then transfers this exponential growth to the primary coordinates.

Install packages listed in `requirements.txt` and run `python verify.py` in the directory containing both files. The program performs exact symbolic simplification of the trace, determinant, characteristic signs, Rayleigh identity, and the scalar special case; it then assembles and compares \(240\) random real period products in dimensions \(1\)–\(4\), tests synchronized projections, and checks auxiliary-variable elimination at \(\rho=1/2\). Observed execution output:

```text
VERIFY_OK exact symbolic trace/determinant/root threshold, 240 SVD Floquet tests, stable-frozen comparator and OGDA equivalence
```

The numeric examples are regression tests only; they do not establish the universal theorem or originality. This package does not establish stability for other payoff schedules, rank-deficient couplings, constrained games, or alternative auxiliary initialization. An independent scientific audit has not been performed.
