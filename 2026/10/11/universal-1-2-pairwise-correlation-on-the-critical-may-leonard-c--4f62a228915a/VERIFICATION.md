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

C PASS: Independently expanded the full three-component vector field and confirmed u-dot=u(1-u) at alpha+beta=2. Invariance of log u and u on compact interior support gives E u=E u^2=1, so u=1 almost surely. Invariance against arbitrary C1 test functions of x yields E[per-capita x growth|x]=0; on u=1 this equals (alpha-1)(z-y), independently checked symbolically. Cyclic conditioning forces E[y|x]=E[z|x]=(1-x)/2. The repeated conditional equations imply equal means 1/3, equal second moments and cov=-variance/2; zero variance is the coexistence Dirac state. No infinite measure conclusion is extrapolated from finite examples.

## originality

PASS

PASS within accessed evidence: The original May-Leonard system and Leach-Miritzis critical-line analysis yield the logistic total and periodic critical geometry, but do not determine coordinate-conditional invariant-measure means, equal variances, or universal -1/2 Pearson correlations. The candidate derives these from the stationary generator with nontrivial coordinate conditioning, not merely from the logistic reduction or existence of periodic orbits. A complete 2013 same-model Blé et al. primary paper remained inaccessible and could contain equivalent moments; that risk is recorded without treating failed access as disproof of priority.

## value

PASS

V PASS: The critical integrable line is a geometrically distinguished classical May-Leonard regime. The all-compact-invariant-measure conditional equal-sharing identity, coordinate variances, and universal amplitude-independent -1/2 correlation are precise measurable rigidity constraints that distinguish the deterministic stationary dynamics from arbitrary simplex-supported distributions. They can test long-time orbit data without knowing periodic orbit amplitudes; this is stronger than merely recovering known simplex geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
