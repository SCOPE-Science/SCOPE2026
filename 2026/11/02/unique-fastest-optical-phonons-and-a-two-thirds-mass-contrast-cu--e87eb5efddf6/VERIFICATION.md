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

The uniqueness is on the reduced half-zone [0, π] and is for the speed magnitude, not its signed value. Diagonalizing the mass-weighted Bloch matrix gives ω₊²=Ω²(1+u). Eliminating q from its derivative gives (4|v₊|/(aΩ))²=(1−u)(1−c²/u²), with u decreasing bijectively from 1 to c. Its derivative has the sign of 2c²−c²u−u³, strictly decreasing from positive to negative at the endpoints. This proves the unique interior optimum and its formulas. The acoustic slope is aΩ√(1−c²)/(2√2), and (1−u)(1−c²/u²)<1−c² proves the strict ratio bound. With t=c^(2/3), the cubic becomes y³+ty=2 for y=u/t. The edge shift is 2u+O(t²) and the speed deficit is (u+c²/u²)/2+O(t²), giving all stated coefficients and sharpness of the limiting ratio. A fresh numerical check, replayable by bisecting the cubic on [c,1] and computing the edge shift as 2 asin(√((u²−c²)/(1−c²))), gives scaled values 1.259921038, 2.519842038 and 0.944940790 at c=10⁻¹¹. That check is corroboration, not the uniqueness proof.

## originality

PASS

Credit standard diatomic dispersion and group velocity as existing input. The supported distinct contribution is the global optical-speed optimizer together with its singular equal-mass asymptotics and sharp acoustic-normalized bound. The closest inspected transport, phase-resonance and defect-mode results do not give this combination. This is a bounded best-of-knowledge comparison, not a historical-priority determination.

## value

PASS

The meaningful result is not a rederivation of the standard dispersion or just a stationary cubic. It resolves how the fastest optical mode approaches the band-folding degeneracy, quantifying both the wavenumber boundary scale and the speed deficit with leading coefficients. The comparison to sound speed provides a sharp scale independent of mass contrast for this natural propagation observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
