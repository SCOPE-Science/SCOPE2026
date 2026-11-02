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

PASS: Exact infection arrival is sum of d i.i.d. Exp(λ) stages, immunization completion sum h i.i.d. Exp(μ). Interleaved event streams give the negative-binomial race (1-q)^h Σ_{j<d}C(h+j-1,j)q^j; strict descendants N_d=Σ_{i=1}^{H-d}b^i. For w_j=C(h+j-1,j)q^j the ratios w_(j+1)/w_j=q(h+j)/(j+1) decrease, implying strict log-concavity of partial sums S_d. The geometric descendant sequence N_d is strictly log-concave too, so W_d has decreasing adjacent ratios, allowing a unique optimum or two adjacent tied depths. Adjacent ratio S_{d+1}/S_d strictly increases with q from 1 to 1+h/d, so crossings exist exactly at the displayed strict inequality; the monotone depth-ratio order makes them an initial segment with increasing q_d. Since N_d/N_{d+1}>b, h=1 never crosses, and for h=2 only b=2,d=1 can cross, with Q_H as claimed. Recomputed exact 2,4,2,3/4 example (7/8,15/16,67/128). Independent rational race-DP checks passed for 1920 b,H,h,q cases; proof applies to all positive λ,μ.

## originality

PASS

Best-of-knowledge PASS on the particular final statement after comparing objects, hypotheses, quantifiers, dominating statements and actual inspected materials; accessible primary evidence does not imply this exact result. No search failure constitutes a novelty proof. Specific same-source risks are retained; any inaccessible literature remains explicitly qualified.

## value

PASS

PASS: Exact ordered vaccination-depth phase transitions isolate a nontrivial effect of maturation-time shape at fixed mean, sharply distinguishing one from two Erlang stages and showing when b-ary geometry suppresses outward shift. It is a complete optimization classification within a natural idealized epidemic model, not just an isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
