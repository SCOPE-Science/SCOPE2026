---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The superior state solves x=K/(1+q e^-rt), and the inferior growth rate a(t)=lambda+delta(t) strictly decreases, with delta=d e^-rt/(1+q e^-rt). The exact reciprocal z=1/y solves a linear equation and yields z-C/lambda=e^-F(1/y0-C/lambda-(C/lambda)I(t)), I=integral(delta e^F). Its improper integral is finite iff r>lambda, giving the explicit ycrit=lambda/[C(1+Iinf)]. The moving nullcline h=a/C decreases, and at each crossing y=h one has (y-h)'=-h'>0; hence at most one strict peak. The reciprocal sign forces existence precisely for ycrit<y0<h(0) if r>lambda and for all 0<y0<h(0) if r<=lambda. The exact equation L(y0)=G(t_peak) has G'=C e^F delta'/a²<0. Asymptotics of its two terms give A0=C zeta d r/[lambda²(r-lambda)] and thus logarithmic delay and power-law peak height. In independent checks the displayed example reproduces ycrit=1/(40+12pi), phase signs, and near-critical delay; numerical quadrature truncation is not an analytic proof. Boundary y0=ycrit increases without peak; y0=h(0) has zero initial slope and decreases afterwards.

## originality

PASS

PASS (qualified): Tilman (1994) supplies exactly the two-species hierarchical mean-field model and equilibrium; the theorem concerns initial-value transient peaks and a quantified near-threshold singularity. The inspected Tilman sections do not present this classification. Doncaster–Pound–Cox extend competition theory, while Hastings (1980) has a particularly plausible title but full text remained inaccessible. The close model match raises a material residual priority risk, but absence of that text alone does not warrant false scientific failure. Resultary search returned no same mathematical model formula.

## value

PASS

PASS: Strict ecological overshoot versus monotone recovery and the critical delay exponent form a sharp, interpretable phase classification in an established competitive-colonization model. The result distinguishes transient peaks from equilibrium coexistence, not a trivial sign check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
