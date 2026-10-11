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

The Katz–Kleiman conormal formula gives dual degree de times the cubic complete homogeneous polynomial in d-1 and e-1. With q=d+e-2 and s=e-d, algebra reduces this to a constant in q minus (q/8)(s squared minus 2(q+1)) squared. Thus the optimizer is exactly the admissible parity-lattice square nearest to 2(q+1). Adjacent admissible gaps tie iff 2q=s(s+2), forcing s=2k and q=2k(k+1), with the stated bidegrees. Mesh-two approximation gives the square-root asymptotic. Fresh exact enumeration through q=2000 reproduced every optimizer and the tie sequence.

## originality

PASS

The primary duality source supplies the pointwise projective-dual degree formula, but no inspected source optimizes that polynomial across codimension-two bidegrees with fixed sum. Fresh Resultary search returned the assigned theorem itself and nearby fixed-sum results for different invariants, not a stronger dual-degree statement. The completed-square reduction, nearest-square mode, tie sequence and square-root imbalance therefore survive best-of-knowledge originality.

## value

PASS

Projective-dual degree is a standard discriminant complexity, and fixing d+e fixes the adjunction coefficient. The complete optimizer classification exposes a non-obvious square-root imbalance and infinite exact tie law, making it a natural structural result rather than a finite parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
