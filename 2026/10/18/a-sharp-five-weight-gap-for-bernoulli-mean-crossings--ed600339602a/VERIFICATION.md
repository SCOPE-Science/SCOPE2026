---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Heavy weight w_i≥p immediately gives probability at least p. Otherwise all five weights <p implies p>1/5, and every ≥3-success subset wins since complement two weights sum<2p and 1−2p≥p for p≤1/3. For p≤1/4 all pairs win by complement-of-pair argument. For 1/4<p≤1/3 sorting five weights shows at least six winning pairs; therefore P≥Bin(5,p) tail ≥3 +6p²(1−p)³ and excess F(p)=p(p−1)(3p²−5p+1), with F'=12p(1−p)²−1>0 on [1/4,1/3], F(1/4)=3/256. Analytic sharp family p=1/4+ε, w=(ε,(1−ε)/4×4) has event exactly at least two large successes and excess approaches 3/256, never attains; heavy dominant weight yields equality of baseline even all w_i>0. Recomputed F factor and rational 67/256, 3/256 independently; finite tests not universal proof.

## originality

PASS

Milojević–Sudakov's 2026 primary paper poses broad mean-crossing lower bound and proves limited p cases, not the full all-p at most five-support case or sharp light-stake stability. Fokkink–Meester–Pelekis optimize an upper probability over stakes, not the lower mean-threshold infimum. The 3/256 pair-combinatorial quantitative gap is additional; exact small-support prior results in older chance-constrained gambling literature remain possible.

## value

PASS

A motivated finite-support instance of an explicit open Bernoulli mean-crossing conjecture, with new quantified sharp gap distinguishing automatic heavy-coordinate witnesses from light-stake configurations. It pins down minimal possible counterexample support at six and is useful as a tractable exact boundary rather than arbitrary five-variable calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
