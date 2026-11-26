---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Two sources in one half-open unit cell are less than √2 apart, so they are lattice neighbors; triangle-freeness rules out triple fibers. The positive horizontal and vertical source edges give phase windows [0,1−a/q)×[0,1−b/q) and [b/q,1)×[0,1−a/q). Because a,b are units modulo q and h²=−1 modulo q, the source phases equidistribute on the q elements (r,[hr]_q), with q sources per phase in one q×q source period. Boundary cells along the inverse target square contribute O_q(M), so the double-fiber density is (H+V)/q. Rotation of phases (r,t)↦(−t,r) takes the horizontal points except zero exactly to the vertical points: t=0 forces r=0 and the potentially unmatched endpoint r'=b is excluded since [hb]_q=q−a. Thus V=H−1. The full source count over target squares differs from the number of target cells by O(M), giving equality of the limiting zero- and double-fiber frequencies. For the discrepancy, with q=u²+v² the modular graph lift has vectors (u,v) or (v,u) according to the leg orientation, and their quarter turns. The determinant q equals the lattice index, so their centered square tiles have covering radius ρ=√(q/2). The tile union from each rectangle's lattice centers lies between its erosion and dilation by ρ; the enclosing-box area error is at most 2ρ(w+z)+4ρ², valid also when an eroded side is empty. Summing both errors and dividing by q² gives exactly the stated bound. The triple (3,4,5) has H=1, and the generic continuous benchmark there is 4/25 rather than 1/5.

## originality

PASS

The closest primary paper already has the same floor quantizer, horizontal collision rectangle and finite Pythagorean phase group. Exact raw collision counts by a finite sum can be recovered from those ingredients, so the novelty is not nearest-neighbor reduction, phase parametrization, positivity, or even the idea of a modular count. The supported distinct result is the structural odd-numerator collapse of the two frequencies to one rectangle count, coupled with an explicit uniform comparison to the nonresonant density by the square phase-lattice geometry. The inspected prior work does not give those conclusions; the related Resultary record concerns a different iterate and statistic. Review does not assert exhaustive priority.

## value

PASS

The one-step multiplicity distribution quantifies how irreversible a standard floor discretization is in the dense rational-coordinate exceptional family. The parity obstruction and the uniform q-dependent discrepancy distinguish actual resonant values from a smooth generic benchmark and quantify how that distinction shrinks uniformly over large primitive hypotenuses. These are substantive geometric and arithmetic conclusions beyond reporting a finite period count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
