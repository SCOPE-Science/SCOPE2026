---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For 1D real periodic Korobov smoothness alpha>1/2, Fourier aliasing Q_p-I=sum_{p|m,m!=0} hat f(m). Choosing all nonnegative Fourier coefficients proportional to omega_nu(m)|m|^{-2alpha} attains both triangle and Cauchy–Schwarz bounds for expected absolute error, giving E^2=2zeta(s)nu^T A nu, s=2alpha, A=diag(u_p(1-u_p))+uu^T, u_p=p^{-s}. Positive definite quadratic inverse gives unique w/W by Sherman–Morrison; K=#primes<=p_min and s>1 imply 1-c u_p>0, so no boundary optimum. w_p increases strictly with p. PNT uniform weighted prime sums produce the sharp nontrivial limiting ratio; single-prime edge case covered. Independent exact rational n=12,s=2 gives nu_7=2/7,nu_11=5/7, ratio 301/247; n=30 probabilities positive and increasing. These finite tests are not PNT proof.

## originality

PASS

Kuo–Nuyens–Wilkes 2023 random-prime fixed-vector paper samples primes uniformly and analyzes error; its inspected PDF formulas do not optimize unrestricted nonuniform 1D prime probabilities. Distinct work changes generator, shifts or RMS criteria. General quadratic optimal design supplies machinery but not the established prime-specific positivity and asymptotic ratio.

## value

PASS

Selecting the prime distribution is a genuine design variable in randomized lattice integration; the optimized absolute-error objective, unique distribution and nonvanishing asymptotic uniform-sampling penalty give immediately useful exact guidance under explicitly stated cost-free sampling assumptions. Not a generic renaming of linear algebra because positivity and Fourier attainment require arithmetic structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
