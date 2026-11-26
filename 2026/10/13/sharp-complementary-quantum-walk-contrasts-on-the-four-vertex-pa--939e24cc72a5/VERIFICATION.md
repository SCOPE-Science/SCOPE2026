---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The reversal blocks exponentiate using traceless parts squaring to 5I/4. In V-e^(-it)U(-t) the antisymmetric block cancels exactly; halving the entries of the symmetric block gives |sin t|sqrt(c^2+s^2/5) within each degree class and (2/sqrt5)|s cos t| across classes. Within a degree class the moduli form the unordered pair a+b, |a-b| with a+sqrt5 b<=1 (Cauchy–Schwarz), so the difference is at most 2/(1+sqrt5), the sum at most 2, and the product at most 1. The difference bound is sharp when the paired absolute coordinates in both unit vectors match, with the smaller squared coordinate 1/(1+sqrt5) giving a=b; the sum and product use a=1,b=0. Across classes the moduli are 2|sC|/sqrt5 and 2|sS|/sqrt5, making the difference extremal at |s|=|C|=1 and the sum and product extremal at |s|=1, |C|=|S|=1/sqrt2. The within-class complex contrast uses |c|=1 and |sin t|=1; the across-class one uses |s|=1 and |cos t|=1 on the torus. For any fixed phase phi=t/2 mod 2pi, the times 2phi+4pi k generate a dense first phase via irrational rotation by 2pi sqrt5. Thus all upper bounds have actual time sequences approaching them, without claiming finite-time attainment. The supplied verification notes and script were inspected, not executed; reported finite checks do not prove sharpness.

## originality

PASS

The metrics and general framework are already in Cooper et al.; known transfer/recurrence facts account for the same-class sum and product endpoints. The supported distinct claim is the exact joint amplitude optimization yielding the nontrivial sharp contrasts and across-class sum and product. The strongest primary comparison has slack in those cases and explicitly asks for tight bounds on paths.

## value

PASS

P4 is the smallest self-complementary path with nontrivial degree classes and supplies a concrete benchmark for the published tight-path question. The across-class bounds quantify a simultaneous tradeoff not visible from individual entry bounds, and the complete exact table distinguishes trivial recurrence or transfer from phase-constrained extrema. No paper-sized generalization, physical advantage or device claim is needed for this benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
