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

Inspected every analytic estimate: reciprocal summability ensures compact-uniform convergence of G(w)=prod_j(1-w/s_j)^2 and log H(T)=o(T) for H(T)=prod_j(1+T/s_j) by dominated convergence. For |w|=s_j, the exp(w) maximum angular loss has a quadratic lower bound in |w-s_j|; the double zero of G provides an upper perturbation proportional to the same square. Because B_j=R_j(2/s_j+4)e^(-s_j)H(s_j)^2 tends to zero, a single positive epsilon makes all off-root inequalities strict. On w=s_j the perturbation vanishes, giving exactly n maxima; f'(0)=epsilon, upper e^(r^n)+o(e^(r^n)) and lower values at R_j give exact order n/type 1. The s_j=(j+1)(log(j+2))^2 sequence is reciprocal-summable and yields the claimed near-power lower count. All quantifiers are analytic and no finite truncation is used as proof.

## originality

PASS

The closest earlier works prescribe maximum-modulus discontinuity radii for an entire function or individual maximum points at different radii, often with geometric separation to retain finite order. These are not equivalent to exactly n simultaneous global maxima at every arbitrarily dense reciprocal-summable prescribed radius, with first Taylor exponent one, exact order and type and near-power exceptional count. Li proves generic two-point bound outside a locally finite exceptional set but no upper density on that set. The double-zero perturbation idea has antecedents, which are credited. This is best-of-knowledge originality, not priority certainty.

## value

PASS

There is a substantive tension between the generic maximum-count bound set by the first Taylor gap and unrestricted exceptional-radius accumulation toward infinity. The theorem shows near-power frequency of n-fold exact global maximizing sets with complete growth control and no geometric separation, a motivated sharp qualitative strengthening of prior exceptional-circle existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
