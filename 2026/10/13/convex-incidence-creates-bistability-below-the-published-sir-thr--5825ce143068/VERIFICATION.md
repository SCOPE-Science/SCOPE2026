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

Verified the motivating publisher PDF: Eq. (2.1) is the frozen vector field; Eq. (2.4) prints MB/[μ(B+μ)]; statement (i) on p. 7551 rules out positive equilibria below one; Thm. 4.1 makes a global stability claim for the same regime and system. For the actual vector field the infected linear equation at E0 has coefficient MK-(μ+η), with K=B/η; the other eigenvalues are -η and -(α+η). Away from the threshold the invasion condition is consequently governed by K/a, a=(μ+η)/M, not by the printed expression. At equilibrium N=S+I+R=K, and the last two equations for I>0 give S=a/(1+γI) and R=(c-1)I. Thus the quadratic in the finding is necessary and sufficient for positive endemic equilibria. For a>K its product of roots is positive; positive real roots also require Kγ>c. The discriminant's roots in γ are c(√a±√(a-K))²/K² and lie on opposite sides of c/K, giving exactly the asserted positive-root counts. At the witness, the endemic quadratic is proportional to (6I-1)(5I-2), yielding the two positive states and both ratios 1/2. In (N,I,R) coordinates -η splits off. At an endemic point the remaining block has upper row ((μ+η)γI/(1+γI)-v,-v), with v=MI(1+γI), and lower row (μ,-(α+η)). At I=1/6 its trace/determinant are -43/36 and -42/36; at I=2/5 they are -12/5 and 14/5. Hence the lower endemic point is a saddle and the upper one a sink, coexisting with the sink E0. The positive endemic states are admissible equilibrium initial conditions, refuting both printed subthreshold claims on their stated domain.

## originality

PASS

The local threshold calculation is standard linearization and convex-incidence backward bifurcation is not a new phenomenon. The distinct claim is a correction to the exact published vector field and its below-one theorems, with a sharp positive-root classification and an exact stability witness that does not depend on which threshold expression is used. The motivating article treats the same model but states opposite subthreshold results; the strongest catalog neighbors use different model mechanisms. Older nonlinear-incidence coverage was not exhaustively resolved.

## value

PASS

This corrects a published inference from a below-one threshold to global absence of endemic states. The exact example isolates the inference failure even when the printed and correct ratios agree, while the sharp general boundary explains why the example is not a numerical accident. The result is a specific mathematical correction, not a claim about a real pathogen or intervention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
