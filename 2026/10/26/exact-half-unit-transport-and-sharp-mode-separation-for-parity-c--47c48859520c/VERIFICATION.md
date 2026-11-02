---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For positive independent {0,1/2,1} factors, the generating polynomial G(w)=prod(L_i+T_i*w+W_i*w^2) is Hurwitz stable and has decomposition P(w^2)+w*Q(w^2). The strict Hermite-Biehler theorem yields alternating simple negative roots with P having one extra factor, hence interlacing Bernoulli parameters a_1<b_1<a_2<...<b_(n-1)<a_n. Pairwise uniform couplings yield J <=_st K <=_st J+1, where K has integer conditional law and J+1/2 half-integer conditional law. One common-quantile coupling then makes K-J in {0,1} a.s., proving every W_p=1/2 including infinity; positive-probability simplex limits handle zeros. Darroch strict mode-mean inequality gives modal distance <5/2, hence <=3/2 by half-integer lattice parity. The supplied two-factor example realizes 3/2. Independently checked 10,330 nondegenerate factor sets on the denominator-three probability grid through four variables against the exact CDF sandwich and mode bound. These are finite corroborations, not proof for arbitrary real factors.

## originality

PASS

Broadie–Petkova Theorem 1 and Section 3 already give conditional Poisson-binomial structure, mean comparisons, and 5/2 cross-mode bound; Holtz gives classical strict root interlacing. The assessed novel statement is the *sharp coupling at lattice distance 1/2* and consequently 3/2 sharp modal separation, a short but nontrivial stochastic-order consequence rather than the already-published decomposition/interlacing.

## value

PASS

Every optimal W_p exactly 1/2 is a strong structural relation between the two conditional laws, directly useful for coupling arguments and distributional comparisons of three-outcome sums. The exact best-possible modal constant improves a currently published bound with a witness; these are natural, reusable invariants, notwithstanding the short proof once root interlacing is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
