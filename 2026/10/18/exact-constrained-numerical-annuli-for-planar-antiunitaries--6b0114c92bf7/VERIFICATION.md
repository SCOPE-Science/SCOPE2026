---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The inspected proof fixes the inner product linear in its first variable and correctly transforms conjugate-linear coefficient matrices by unitary congruence. Splitting unitary M into symmetric S and skew K gives K* K=b²I, and a Cayley–Hamilton SU(2) identity yields S* S=a²I. Takagi congruence gives canonical real M=[[a,b],[-b,a]], including a=0. For a unit x the self-overlap modulus fills m∈[0,a]. Each allowed y=qbar x+s exp(i phi)v, and ||Ax||=c, so the possible |<Ax,y>| at fixed x are exactly [|tm−s sqrt(c²−m²)|,tm+s sqrt(c²−m²)]. Connectedness and simultaneous phase rotation fill every annular radius/argument; maximizing and minimizing over m give the claimed piecewise sharp formulas. Check pure symmetric a=c/b=0, pure skew a=0/b=c, q=0 and |q|=1 explicitly. Inspected check.py Gram constraints and extremizers, but these finite examples are supplemental.

## originality

PASS

The closest Majumdar–Müller 2026 paper already defines the same q-generalized range, derives circular symmetry and planar annulus topology with implicit infimum/supremum radii (Remark 6.7), and treats the pure-skew boundary (Example 6.3). Those are COVERED subclaims; no novelty is claimed for them. Relevant full §6 does not supply the two congruence-invariant closed formulas or independent sharp thresholds. Kołaczek–Müller 2024/2025 cover ordinary numerical range q=1 rather than complete constrained family; Resultary rank-one q papers are complex-linear operators and do not dominate this antiunitary result. Older equivalent parametrizations remain a literature risk.

## value

PASS

An exact all-parameter classification with two independently ordered transitions is a motivated refinement of the known annulus-existence theorem, revealing where the central hole vanishes and the operator norm stops being attained; the pure symmetric/skew limits are intrinsic geometry, not an arbitrary small numeric instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
