---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Writing a=3t and putting the oriented Pearson sum over a common denominator gives exactly D=(3s−2)²/4+3(m−as)²/[4(1−a²)]. The oracle a=m/s is unique and interior for every admissible truth. For the moment matcher a=3m/2, division by the oracle loss for s≠2/3 gives the inverse of c(m) exactly; at s=2/3 both losses are zero, so the inequality also holds there. The fixed s=5/6 witnesses no positive constant uniform in m without sacrificing full support. In the additive problem convexity in s gives the larger endpoint limit even on the open interval. For a<0 the first endpoint alone exceeds 3m²/4. With 0<a≤m the first endpoint dominates, strictly; for a>m the switch is at a=2m/(1+m). The active first branch decreases and the active second branch increases (derivative has sign (a−m)(1−am)). This proves the claimed unique minimizer, its value, and the moment-matching coincidence at m=1/3 in the stated domain. In RESULT.md §4 the phrase 'intersection is unique' means the unique positive crossover: the branches also touch at a=0, which does not affect the argument. The supplied exact-rational script and VERIFICATION.md were inspected, not executed; the identities and sharp endpoints here follow algebraically.

## originality

PASS

The matched reconstruction paper asks the relaxed multiplicative question and illustrates a positive Pearson projection gap. Its inspected evidence does not establish collapse of a universal constant, an exact optimal fixed-mean constant, or an exact additive minimax rule. The comparison is specific to Pearson divergence and does not decide all non-KL cases.

## value

PASS

The collapse on three atoms is a sharp, full-support counterexample to a uniform relaxed Pearson projection property, rather than just another example of noncoincidence. The same loss decomposition gives a unique action from exactly the available information and a finite worst-case excess where moment matching becomes arbitrarily bad. The small alphabet isolates the mechanism and makes the formulas useful as benchmark cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
