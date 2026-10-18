---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Taking \(r=x/y\) cancels the cubic terms to \(\dot r=y^2(1-r^2)\). The scalar solution \(y^2=b^2e^{2t}/[1-pb^2(e^{2t}-1)]\) defines a strictly increasing internal clock \(I=\int_0^t y^2\). The exact ratio trajectory \(r=(1+Ke^{-2I})/(1-Ke^{-2I})\) has its only pole at \(I=\frac12\log K\), before any scalar blow-up, giving the physical-time formula and \(x(t)\sim-1/[Y(T_p-t)]\) with finite \(Y>0\). Expansion of the exact time formula gives the three regimes; for \(p>0\), the exact difference \(t_b-T_p=-\frac12\log[1-K^{-p}/(1+pb^2)]\) has leading coefficient \(2^{-p-1}/(1+pb^2)\) and noninteger Hölder order \(p\). Setting \(p=\delta/\log K\) gives an exact \(F(\delta)=(1-e^{-\delta})/\delta\) crossover and compact-\(\delta\) uniform error. On the invariant line \(x=-y\) the positive-p blow-up exponent is \(1/2\), whereas on the escape side it is one. The actual check.py was read and checks these cancellations and sample limits numerically; no finite computation is used to prove the asymptotic quantifiers.

## originality

PASS

Volokitin’s 2023 work studies the exact cubic family, its invariant lines, phase portraits and Darboux integrability; those are not newly claimed. The present final statement concerns exact escape **in original physical time**, including asymptotic trichotomy, differentiability of the time-to-escape at the separatrix and the uniform two-parameter critical crossover. The general star-node literature describes phase/orbit equivalence and does not preserve physical flight time; the contracting-homogeneity result assumes contraction in every direction, which fails on this field’s zero homogeneous part at \(y=0\). Only the original abstract/record and source-model statement were accessible for Volokitin, and authorized full-PDF retrieval failed, so priority beyond those exposed results remains explicitly uncertain; inaccessible text alone is not treated as failure.

## value

PASS

Exact separatrix residence-time scaling in a canonical integrable cubic flow is motivated by global phase portrait theory. The three-regime transition, sharp Hölder exponent and uniform two-parameter crossover give nontrivial quantitative information beyond qualitative orbit classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
