---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With u=log x and v=log y the domain isometry multiplies f(e^v) by v(1+epsilon cos(omega log v)). The resulting integral kernel differs from the weighted Copson step kernel by a Hilbert–Schmidt kernel, bounded in square by (1-|epsilon|)^-2 v^-2 exp(-2|u-v|). Absolute convergence also follows directly from Cauchy–Schwarz with the domain weight. The second log unitary identifies the Copson operator with the half-line compression of the bounded full-line exponential tail-convolution followed on its input by multiplication by a. The essential norm equals the full norm: take compactly supported near-norming test vectors and translate by integer periods toward +infinity; they converge weakly to zero, while the discarded full-line output tends to zero in norm. Its full-line Gram kernel is a(s)exp(-|s-r|/2)a(r), with no missing factor. Positive-kernel domination of each Bloch quadratic form by the zero fiber acting on the modulus, and norm continuity of the fibers, give exactly the stated compact kernel and top eigenvalue. Independently, the circle operator is M_a(-d_t^2+1/4)^-1 M_a, so its reciprocal top eigenvalue mu solves the lowest weighted periodic eigenproblem (-d_t^2+1/4)f=mu a^2 f. Testing that variational problem with f=1 gives an essential-norm lower bound 2 sqrt(mean(a^2)), which implies the stated bound by Cauchy–Schwarz and mean(a)=1/sqrt(1-epsilon^2). At epsilon=0, mu=1/4 is simple; normalize mean(f)=1. Its first-order eigenfunction is -cos(omega t)/(2 omega^2) because the first variation satisfies f_1''=(1/2)cos(omega t). Integrating the eigen-equation through second order gives mu=1/4-(3/2+1/(2 omega^2))epsilon^2/4+O_omega(epsilon^4), the odd terms vanishing by half-period unitary equivalence and analyticity. Taking mu^-1/2 gives the frozen coefficient, standard base value 2, and the stated even remainder.

## originality

PASS

The distinct claim is the exact periodic-cell norm and explicit frequency-dependent curvature for the continuously integrated, log-log-periodic domain weight. The endpoint value 2, Hilbert–Schmidt Copson comparison, periodic Floquet machinery and elementary positive-circle Green kernel are not separately credited. The strongest same-day analogy uses a discrete row multiplier on a different logarithmic scale; the closest analytic-space formula excludes fixed nonconstant periodic profiles by its vanishing-derivative hypothesis.

## value

PASS

The claim quantifies the sensitivity of a natural critical endpoint rather than giving another boundedness bound at the base weight. A fixed-amplitude periodic input weight changes the asymptotic essential norm, with an exact finite-cell spectral description for every permitted amplitude. The divergent coefficient as frequency decreases shows why the norm's response cannot be read off from the average weight alone and why fixed-frequency perturbation must be distinguished from uniform slow modulation. These are useful stability data at the critical continuous endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
