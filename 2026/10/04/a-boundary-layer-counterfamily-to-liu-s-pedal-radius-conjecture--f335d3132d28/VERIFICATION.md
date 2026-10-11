---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For \(A=(-1,0)\), \(B=(1,0)\), \(C=(0,2)\), and \(P=(0,y)\) with \(0<y<2\), direct orthogonal projection gives the three pedal vertices and hence \(R_p=(1+y^2)/(1+2y)\) and the stated closed formula for \(r_p\). The ambient circumradius is \(R=5/4\). At \(y=1/100\), substituting the exact formulas reduces the claimed reversal to an inequality involving \(\sqrt2\) and \(\sqrt{50005}\); the rational lower bounds \(\sqrt2>140/99\) and \(\sqrt{50005}>1118/5\) certify it exactly. Moreover the defect tends as \(y\downarrow0\) to \(-1/4+(4/5)(\sqrt{10}-2\sqrt2)>0\); continuity therefore gives an open interior boundary layer of counterexamples, not a single numerical accident.

## originality

PASS

Liu's primary paper explicitly states \(R_p+\sqrt2\,r_p<R\) for every interior point as Conjecture 1. Huang's later open-access paper explicitly identifies and proves Liu's conjectures (3.4) and (3.5), not the linear Conjecture 1 / equation (3.2). Targeted web and Resultary searches found no earlier counterexample or counterfamily to this exact inequality; the closest same-day SCOPE hits concern different Liu pedal/cevian parameter problems.

## value

PASS

An exact counterfamily to a published universal triangle-geometry conjecture is a motivated boundary result. The construction identifies the failure mechanism and proves an open layer of counterexamples rather than reporting a floating-point anomaly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
