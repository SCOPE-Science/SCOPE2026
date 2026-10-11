---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

In the closed nonnegative SEIR system, \(\dot C=\beta SI=-\dot S\), so \(C(t)=C(0)+S(0)-S(t)\) and \(C\) converges because \(S\) is nonincreasing and bounded below. If two perfect sliding-window outputs agree, \(D(t)=C_1(t)-C_2(t)\) satisfies \(D(t+h)=D(t)\). Because \(D\) also converges, every periodic value equals the same limit, so \(D\) is constant. A constant shift of the auxiliary \(C\) state has no effect on \(S,E,I,R\) or the parameters, hence perfect window-incidence observation has exactly the same parameter equivalence relation as perfect cumulative-incidence observation. Equality of instantaneous incidences gives the same conclusion by integration. The parameter involution transcribed from the source preserves the three source input-output combinations and is checked exactly by the assigned verifier.

## originality

PASS

Saucedo et al. analyze cumulative-incidence structural identifiability and report markedly better practical identifiability from incidence, but their incidence observable is a time difference of cumulative incidence and their structural tools did not resolve that difference output. The audited periodic-plus-convergent argument closes exactly that gap and proves that the practical improvement cannot come from a different perfect-data ambiguity class. Current Resultary searches did not retrieve a prior same-model fixed-window equivalence theorem.

## value

PASS

The theorem resolves a concrete methodological gap in a published identifiability comparison and cleanly separates structural from practical reasons for preferring incidence data. It is short, but the distinction is scientifically consequential for interpreting finite-noise experiments and uses a model-specific convergence fact to establish exact observation equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
