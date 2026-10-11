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

Summing the exact six compartment equations gives \(T'=b-\delta T\). At \(\xi=0\), summing the three noncompliant equations gives \(X'=(q(T-X)-(\nu+\delta))X\). At equality, with \(Y=T-K=Y_0e^{-\delta t}\), this is \(X'=q(Y-X)X\); the exact equation for \(1/X\) has an exponentially convergent integrating factor and yields \(tX\to1/q\) for every \(X_0>0\), including the explicit invariant slice \(X=X_0/(1+qX_0t)\) when \(T_0=K\). For \(R_D<1\), the infection subsystem is eventually dominated by a Hurwitz Metzler matrix, so infected classes decay exponentially; the recovered classes are stable linear equations with exponentially decaying forcing. The stated limits for \(S^*\) and \(K-S\) then follow from the exact population identities. For \(R_D>1\), the positive disease eigenvalue gives instability. The package verifier's rational example independently matches the zero behavioral eigenvalue, negative disease eigenvalues, and reciprocal solution, but the proof is analytic rather than experimental.

## originality

PASS

The primary deterministic noncompliance paper analyzes the fully compliant disease-free equilibrium only under strict behavioral subthreshold/superthreshold inequalities; the equality case has a zero behavioral eigenvalue and is not covered by its local-stability theorem. The later controlled model likewise advertises reproductive-ratio stability analysis but no inspected result supplies the exact critical reciprocal law or the full six-compartment asymptotic. Published-finding search located the audited result but no earlier equivalent or stronger critical-threshold theorem.

## value

PASS

The result closes a genuine nonhyperbolic boundary left open by the source's strict threshold classification and supplies the sharp algebraic constant governing noncompliance persistence. Because that center-direction tail controls the asymptotic approach of two epidemiologically meaningful susceptible compartments, it is a motivated threshold theorem rather than an arbitrary scalar exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
