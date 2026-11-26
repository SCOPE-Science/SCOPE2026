---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Normalize ||T||=1 and let δ=||(T*T)^2−(T²)*T²||. For a unit x, Cauchy–Schwarz gives δ≥a²−b with a=||Tx||² and b=||T²x||². For a>0 the same inequality at Tx/√a yields δ≥b²/a²−ε²/a. A norm-maximizing sequence with a→1 and a subsequential limit b→s∈[0,1] gives δ≥max(1−s,s²−ε²). Minimizing, including ε=1 where the crossing is at s=1, gives the stated envelope. Rescaling restores precisely the fourth and third powers of ||T||. At ε=0 the norm-one three-site shift with squared weights 1 and τ=(√5−1)/2 has defect diag(1−τ,τ²,0), and these nonzero entries coincide. At ε=1 the identity has zero defect. This covers both fields and non-norm-attaining operators. No intermediate sharpness is inferred. Replay is analytic from RESULT.md lines 22–53; the supplied NumPy script was inspected, not executed, and its finite checks are not needed for the theorem.

## originality

PASS

The earlier primary sources checked supply qualitative exact or one-sided moment criteria, not a quantitative nilpotent gap or its stability law. The strongest distinct indexed match really has the same sharp constant and equality chain for two weights; it is a later record and covers only weighted shifts, not the unrestricted bound. No inspected prior statement subsumes the supported general result.

## value

PASS

The cubic-zero case is the first nilpotent stage at which (T²)*T² can cancel part of (T*T)^2. A sharp dimension-independent lower bound resolves that cancellation question for arbitrary operators, not merely shifts. The envelope additionally gives quantitative separation as cubic powers get small, while the attained constant makes the estimate usable without quantitative conjectures about intermediate ε.

The dated certificate retains the supplied scientific assessment, sources and limitations.
