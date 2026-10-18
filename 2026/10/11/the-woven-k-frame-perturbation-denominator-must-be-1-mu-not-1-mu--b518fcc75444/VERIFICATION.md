---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Directly checked the actual source theorem, 2-inner-product quotient, and proof inequality. For any t in (0,1), r=(1-t)/(1+t), lambda=mu=t, p=(e1,0,...), q=(r e1,0,...), K=I, the source perturbation inequality reduces to 1-r=t(1+r) on the sole active index and vanishes on all other subsets. Its printed lower bound A_p min{1,((1-t)/(1-t))^2}=1 contradicts the q-only weave energy r^2. Triangle inequality instead gives (1+mu)sqrt(Eq)>= (1-lambda)sqrt(Ep), hence sharp corrected lower bound A_p min{1,((1-lambda)/(1+mu))^2}, attained by the family. No necessity or all-geometry optimality claim.

## originality

PASS

The formula with 1+mu appears already as an inequality IN the source proof, so a corrected factor by itself is not newly proved here. The new scientifically distinct contribution is a source-specific parametric counterexample to the printed quantitative theorem and an exact optimality witness; no inspected independent correction or erratum establishes it. Closely related K-frame perturbation counterexamples use other source theorems and do not imply this example under the same hypotheses.

## value

PASS

The printed statement promises a lower frame constant one, but the same perturbation hypotheses permit the q-only lower constant ((1-t)/(1+t))^2 tending to zero. Thus the unsupported stability claim can be arbitrarily inaccurate, and the corrected sharp universal quantitative guarantee resolves an explicit defect in published perturbation theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
