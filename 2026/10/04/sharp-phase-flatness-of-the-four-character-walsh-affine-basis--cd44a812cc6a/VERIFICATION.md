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

The eight Walsh samples give, up to a global sign, all sixteen signed sums of four planar unit vectors. Their convex hull is the four-generator centrally symmetric zonogon \(Z\), whose perimeter is exactly 16 and which has at most eight vertices. Any convex \(m\)-gon in a radius-\(R\) disk satisfies \(P\le2mR\sin(\pi/m)\), hence with \(m\le8\), \(R\ge\csc(\pi/8)\). Equality forces an eight-vertex regular octagon, which in a four-generator zonogon is equivalent to the four generator directions being equally spaced modulo \(\pi\). The inspected exact verifier confirms the displayed extremizer has four samples at each of \(4\pm2\sqrt2\).

## originality

PASS

Targeted Walsh/Rademacher, trigonometric-polynomial and vector-balancing searches did not locate the four-character discrete minimax or its equality class. Neuwirth's primary work treats continuous trigonometric spectra (three frequencies in the 2007 paper, and the still-open unrestricted Sidon problem for \{0,1,2,3\} in a 2026 preprint), while Seigner determines the infinite Rademacher Sidon constant rather than this equal-modulus four-coordinate finite problem. The proof is short because classical polygon geometry solves the reduced convex problem, but no checked source states the signed-sum specialization or equality classification.

## value

PASS

This is a natural finite phase-flatness problem for the basic four-character affine Walsh spectrum, with an exact optimum and complete equality geometry. The regular-octagon extremizers provide a reusable bridge between Walsh phase design and planar zonogons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
