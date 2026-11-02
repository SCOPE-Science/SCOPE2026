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

For n≥3 and 0<p<1, Q(t)=pT_n(t)+(1-p)T_{n−2}(t) has Q(±1)≠0. At the n−1 Chebyshev grid the signs alternate for p≠1/2, creating n−2 distinct real roots; polynomial parity excludes more than one nonreal conjugate pair and forces it to ±i sinh(v). Strict monotonicity and endpoint values of cosh(nv)/cosh((n−2)v) (even n) and sinh(nv)/sinh((n−2)v) (odd n) give the sharp p-threshold. For odd n the derivative at 0 settles the intermediate real-root region and the triple collision; p=1/2 factors as tT_{n−1}(t). Because Q(±1)≠0, holomorphic cosine lifting preserves multiplicities and supplies exactly 2n zeros per 2π strip. Taylor expansion establishes stated square-root collision coefficients. Independent exact Sturm isolation covered 33 parameter cases n=3..13, including both parity thresholds; these bounded checks are not the proof.

## originality

PASS

Best-of-knowledge: primary same-object comparisons, alias/implication checks and published finding searches distinguish the assessed exact statement from covered components. Historical priority uncertainty is retained; failed search is not novelty proof.

## value

PASS

For the natural four-atom symmetric probability law with adjacent same-parity frequencies, an explicit necessary-and-sufficient classification of all complex Fourier zeros, their number and collision multiplicities determines the zero-realness boundary and quantitative near-critical zero height. The even/odd sharp transition is mathematically structural, not an arbitrary sample or elementary restatement of equal-weight factorization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
