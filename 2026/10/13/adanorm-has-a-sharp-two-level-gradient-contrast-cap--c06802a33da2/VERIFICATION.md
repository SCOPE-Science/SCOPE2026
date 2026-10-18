---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Starting with e_0=0, the two-step recurrence is e_{2n}=gamma^2 e_{2n-2}+(1-gamma)(gamma A+B). It has fixed point E_B=(gamma A+B)/(1+gamma), giving e_{2n}=E_B(1-gamma^{2n}), and e_{2n-1}=E_A-E_B gamma^{2n-1} with E_A=(A+gamma B)/(1+gamma). Since E_A<A high steps never boost. Since E_B>B the low steps eventually boost, and strict e_{2n}>B is precisely gamma^{2n}<gamma(A-B)/(gamma A+B), yielding the claimed floor-plus-one onset even at equality. The rational contrast ((1+gamma)q)/(gamma q+1) has derivative (1+gamma)/(gamma q+1)^2>0 and limit (1+gamma)/gamma. Independent exact rational recurrence for gamma=19/20, A=100, B=1 through 100 steps agrees termwise, gives E_B=640/13 and contrast 65/32=2.03125. These calculations corroborate, rather than replace, the unrestricted algebraic proof. The claim concerns corrected gradient norms, not host optimizer updates.

## originality

PASS

The defining AdaNorm gradient-norm EMA and conditional low-norm boosting are prior work; the submitted contribution is a sharp periodic input-output response, a strict correction-onset index, and a gamma-only contrast cap. Resultary queries returned other adaptive optimizers, but not a stated AdaNorm two-level contrast law. This is best-of-knowledge, not proof of noncoverage, because original full text was inaccessible in this execution.

## value

PASS

The simplest persistent heterogeneous gradient pattern gives an operationally interpretable worst-contrast ceiling and a finite correction-onset formula, directly quantifying the optimizer front end at its recommended gamma; the cap explains why arbitrarily disparate raw norms cannot persist in corrected contrast. This is a motivated quantitative mechanism/bound, not an unmotivated algebraic restatement or a guarantee about whole-optimizer convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
