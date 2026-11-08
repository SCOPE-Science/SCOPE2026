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

Constructed CTMC on infected subsets with rate alpha+beta sum_{infected neighbor u}1/deg(u) to infect susceptible v, recovery rate 1. Quotient generator by automorphism orbits (6 for C4, 9 for diamond), solve stationary linear equations symbolically. Difference is -alpha beta²F(alpha,beta)/(UV) with U,V positive-coefficient polynomials and beta degree-8 numerator F. Coefficients c0..c4 each have exactly one positive alpha root r4<r3<r2<r1<r0=7/8; c5..c8 positive. Thus for alpha>=7/8 F>0; for lower alpha coefficient signs have exactly one negative-to-positive change giving unique positive beta root by Descartes and endpoint signs. For connected n<=3 only possible edge addition P3->K3 has exact positive prevalence difference. Independent 16-state stationary-generator solver confirms 8 parameter/graph checks, including negative difference at alpha=beta=1 and smaller-n cases. Full universal sign proof uses exact polynomial and rational sign brackets in inspected verify.py, not numerical sampling.

## originality

PASS

Exact source-normalized four-site finite stochastic stationary comparison and the alpha=7/8/unique-beta frontier are not stated in source-degree contact-model mean-field literature or generic monotone infection processes with unchanged old directed edge rates.

## value

PASS

A sharp, surprising edge-addition suppression threshold in a natural finite epidemic model with fixed per-infected-source contact capacity; includes exact one-crossing phase and minimum network size. Gives a substantive counterexample to naive edge-monotonicity intuition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
