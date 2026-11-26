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

Let u=a+b, T=u²+R and r=2ab. Then Δ=1/(T−r)−1/T is strictly increasing in r at fixed T and strictly decreasing in T at fixed r>0. Thus at each u∈(0,1) the unique maximizing shape has a=b=u/2 and untouched entries (1−u)/q, including q=1. Substitution of z=2(1−u)/(qu) gives the stated F_q; differentiating its log gives a numerator proportional to 8−12z−4qz³−q²z⁴ with positive multiplier. It decreases strictly from 8 to a negative value at 2/3, so the derivative changes sign exactly once and both excluded endpoints lose to the positive interior maximizer. The quartic bounds z=O(q^−1/2), and then qz²→√8 and M_n/q→3−2√2. The relative loss r/T is <1/2 because R>0 and a²+b²≥2ab; the half limit is approached at equal merged shares and vanishing untouched mass. Equal shares give 2n/(n+2). An independent numerical illustration using bisection of the derivative in u reproduces maxima for n=3,4,10; replay `python3 /workspace/checks/exact_checks.py`. Finite examples are not evidence for the quantifier over n. This is an exact optimization over known positive real proportions, not sampling, repeated mergers, or loss of species in the assemblage.

## originality

PASS

Credit the inverse-Simpson definition, raw Herfindahl increment and prior studies of taxonomic aggregation. The supported distinct result is the absolute loss extremum, including the unique optimizer and its all-dimension asymptotic; no inspected statement subsumes it. This is a bounded search assessment, not priority certification.

## value

PASS

One merger is the elementary coarsening step in taxonomy and other categorical measurements. The exact dimension-dependent maximum and extremizer quantify how large a distortion this one step can cause, and distinguish linear growth in effective-species loss from the bounded loss at equal shares. The result quantifies a measurement effect, not biological extinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
