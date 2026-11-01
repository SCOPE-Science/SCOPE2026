---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Using the exact Gibbons–Veselov gamma=a band-edge factorization, w0=delta0 and wn=delta_n-delta_(n-1), where delta_n is the Dirichlet harmonic-oscillator energy excess above 2n, once delta_n>delta_(n-1) for sufficiently large a. For u_n=H_n exp(-x^2/2), differentiate the boundary-value solution with respect to energy; the Wronskian equals minus the half-line L2 mass I_n=2^(n-1)n!sqrt(pi). The growing solution u_n J_n, J_n=integral u_n^-2, gives delta_n=1/(I_n J_n(a)) up to exponentially smaller errors. Endpoint Laplace plus Hermite leading coefficients yields J_n=e^(a^2)/(2^(2n+1)a^(2n+1)) [1+(n^2+n+1)/(2a^2)+O_n(a^-4)]. Adjacent displacement ratio is n/(2a^2)+O_n(a^-4), so the relative bandwidth correction becomes (n+1)^2/2; the n=0 convention works. Independent high-precision Kummer zero calculations at n<=3, a=6,8 gave correctly signed/better two-term approximations, not an infinite proof.

## originality

PASS

Gibbons–Veselov (2026) already derive constant gap 2 and exact band edges for this operator, explicitly leaving precise large-a shrinking low-band widths for further investigation. Gannot (2014) proves the leading confined harmonic-oscillator displacement and existence of further expansion, but his inspected Corollary 1.1 does not evaluate the first relative coefficient or the subtraction of preceding level. Thus the exact displayed second band-width coefficient is not identified as a prior printed result. General all-order asymptotic machinery may mechanically yield it, which is a material priority/value limitation, not an automatic FAIL absent a previously evaluated implication.

## value

PASS

A fixed-band two-term exponentially small width law is a natural quantitative invariant of an explicitly solvable periodic quantum lattice. The correction encodes both single-well boundary confinement and the neighboring-level subtraction, going beyond known exact edge locations and leading exponential scale. The result is narrow but supplies a precise coefficient future spectral comparisons can use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
