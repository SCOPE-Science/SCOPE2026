---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For finite integer support choose a=min(supp X) and m=max(supp X)-a. H(z)=Σ_{k=0}^m P(X=a+k)z^k has H(1)=1, positive constant and leading coefficients, and nonnegative intermediate coefficients. Every finite-support tilt with r=e^θ>0 has φθ(t)=e^{iat}H(re^{it})/H(r); therefore all-tilt modulus decrease is exactly angular decrease of |H| on every circle of positive radius. If H had a nonreal zero, conjugation allows an upper-half-plane root z0=r exp(it0), t0∈(0,π). At that tilt |H(re^{it0})|=0 and nonnegative nonincreasing modulus forces zero on [t0,π], impossible for a nonzero polynomial. No nonnegative real zeros because H(s)>0 for s≥0; hence all m roots negative. Factor H(z)=Π_j(λ_j+z)/(1+λ_j), λ_j>0, giving independent Bernoulli(q_j), q_j=1/(1+λ_j) strictly between 0,1. Conversely tilt updates each q to rq/(1-q+rq), and d/dt |1-q+qe^{it}|^2=-2q(1-q)sin t<0 on (0,π); factors have positive modulus there, so the total product is strictly decreasing. Case m=0 is a point mass and vacuous product. Degree two: |p0+p1e^{it}+p2e^{2it}|^2 is quadratic in u=cos t, derivative 2p1(p0+p2)+8p0p2u; nonincrease on [0,π] iff p1(p0+p2)≥4p0p2, whereas strong iff discriminant p1^2−4p0p2≥0. Exact example (8,7,2)/17 satisfies former (margin 6) but not latter (discriminant -15); tilt r=2 yields (4+7z+4z²)/15 with root (-7+i√15)/8 on unit circle and nonzero value 1/15 at z=-1. All quantifiers and support-gap boundaries handled. Independent symbolic calculation and 4096 positive-weight triple tests corroborate the algebra, but all-degree theorem is established analytically, not by finite tests.

## originality

PASS

Best-of-knowledge: Aamand–Alon–Houen–Thorup define tilted strong monotonicity and prove sufficiency for Bernoulli, geometric and Poisson laws (Lemma 3.1), but their Theorem 3.2 concerns local probabilities under the assumption, not an inverse theorem. Tang–Tang Theorem 4.1 (Aissen–Schoenberg–Whitney/Edrei) characterizes finite negative-real-root PGFs as Poisson-binomial but does not equate this with the all-tilt angular modulus criterion. The new necessity is the zero-on-every-radius-semicircle contradiction, and the three-atom ordinary/strong boundary is distinct. Read the relevant full paper sections and compared published related results; priority is not absolutely certified.

## value

PASS

The property is the actual finite-support hypothesis used in sharp local and tilted point-probability estimates, not an arbitrary coefficient experiment. A complete if-and-only-if classification reveals that this apparently broader hypothesis imposes exactly the Poisson-binomial/Bernoulli-convolution structure for bounded integer laws; it excludes any further finite-support distributions and provides a directly applicable criterion in terms of generating-polynomial roots. The three-atom ordinary-versus-strong inequality gives an exact diagnostic of why the weaker Fourier condition is insufficient. The proof is short and uses classical factorization, but the natural converse classification and sharp separation are substantive mathematical information not supplied by the cited sufficiency lemma or a mere reparameterization. No infinite-support classification or improvement in local-limit constants is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
