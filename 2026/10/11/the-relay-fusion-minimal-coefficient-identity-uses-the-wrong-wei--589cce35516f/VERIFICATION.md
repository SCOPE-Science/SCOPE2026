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

Read the actual 2019 publisher article at Definition of coefficient direct sum, analysis and synthesis, Theorems 3.13 and 3.14, and the complete printed proof. For a one-block RFF A=I,v=2, S_R=4I; at f=1 the constraint f=4g forces g=1/4 and canonical a=S_R^-1 f=1/4. Its printed identity evaluates 1/16 on left and 1/4+9/16=13/16 on right; independently recalculated with exact fractions. The article actually proves sum v^2||a||^2=sum v^2<g,a>. Subtracting gives weighted orthogonality of a with g-a, hence the corrected weighted Pythagorean identity. In transformed coefficients h=v g, this is the ordinary canonical least-norm solution for the synthesis map. Finite scalar witness refutes the universal statement, and the Hilbert-space orthogonality supplies the general correction subject to the original frame/Bessel hypotheses.

## originality

PASS

Indexed Resultary searches found several related weight/dual defects, notably a Hong--Li local-relay-dual theorem 3.10 counterexample and a distinct K-fusion minimum-norm resolution, but their objects or theorem mechanisms do not imply Theorem 3.14's one-block weight mismatch. Full publisher text reveals exactly the wrong norm, and no checked erratum states this theorem-specific failure. Novelty is bounded by possible unindexed corrections.

## value

PASS

A published reconstruction/minimum-norm theorem is false under its actual advertised arbitrary positive weights. The scalar witness isolates the error without artificial parameter restrictions and the general weighted identity supplies the correct canonical coefficient geometry for relay synthesis. This has clear substantive consequences when comparing nonuniform communication-channel weights; it is not merely a cosmetic normalization complaint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
