---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Pinned RESULT.md and check_exact.py inspected. The Laurent–Nogueira horizontal rational-tongue bounds are explicitly credited. Coprime upper and lower mechanical binary words have cyclic prefix-sum discrepancies in {0,1}; summation by parts locates the q-cycle coordinates strictly inside (0,1) except a single zero/one contact. Differentiating their actual periodic recurrences at fixed hitting coordinate yields L′(λ),U′(λ)=−sum_j λ^(q−1−j)x_j/Q_q<0, ensuring globally unique inverse endpoints. Coprime floor sums S(1)=p and S′(1)=(p−1)(q−1)/2 yield L′(1)=−(q−1)/(2q) and U′(1)=−(q+1)/(2q). Independent rational Fraction calculation checked 597 (p,q,λ) configurations q≤25 including derivative signs and boundary width coefficients. Finite check does not replace arbitrary coprime p,q proof.

## originality

PASS

Laurent–Nogueira 2017/2018 Theorem 3 gave the horizontal λ-fixed intervals; Gaivão–Nogueira 2020/2022 Proposition 7 repeats and identifies fixed-b endpoints as not precisely known. The audited addition is strict global monotonicity of both boundaries and their unique inverse algebraic endpoints, with q-only tangent, not a new horizontal tongue formula. Later Gaivão–Laurent–Nogueira two-interval theorem covers a broader model but varies translation-like coordinate with slopes fixed; does not imply vertical λ inversion at fixed b. Unindexed engineering mode-locking results remain risk.

## value

PASS

The geometry of rational mode-locking tongues is a natural bifurcation object; global inversion makes a previously implicit vertical slice exact and the denominator-only sharp wedge coefficient identifies universal arithmetic scaling at each rational vertex. This is not routine substitution because nonfolding of the boundary functions needs a nontrivial cyclic mechanical-word argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
