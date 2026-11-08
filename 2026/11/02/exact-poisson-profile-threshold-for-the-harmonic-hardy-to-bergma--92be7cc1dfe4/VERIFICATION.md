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

The harmonic Poisson boundary Fourier expansion gives h2-norm^2=(1+x)/(1-x), while absolute convergence of binomial Fourier series yields angular fourth moment (1+9x+9x²+x³)/(1-x)^3. Radial integration and the displayed antiderivative yield exact normalized profile R(x); its derivative has coefficients x²/2+x³/2+sum_{k>=4}6(2k²-8k+3)x^k/[k(k-1)(k-2)(k-3)], all strictly positive. Hence R strictly increases from 1 to nonattained Poisson-family supremum 5/2 as x->1-. The cited upper bound (3+2sqrt2)/2 is imported from the 2026 theorem with exact normalized measures; no globally sharp constant is asserted. Independently quadrature-checked 7 x values, strict sample monotonicity and 3 angular fourth-moment identities. Sample checks support but do not establish coefficient positivity for all k, which the closed coefficient inequality does.

## originality

PASS

The general 2026 polydisc harmonic isoperimetric embedding upper bound and Problem 7.1 precede the profile calculation; present claim is precisely the explicit real Poisson one-parameter barrier 5/2 and global monotonicity, not a solution of the global sharp norm. Relevant older 2011 and 2019 harmonic inequalities may contain equivalent tests; primary full texts not fully inspected and 2026 motivating paper download was unavailable. O is best-of-knowledge qualified by that material access risk.

## value

PASS

The Poisson harmonic concentration family is a canonical stress test of the new open sharp embedding inequality. Its exact sup 5/2 versus previous easy lower bound 1 supplies a meaningful quantitative barrier and identifies a boundary-only extremal mechanism; narrow but relevant and not merely a numerical experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
