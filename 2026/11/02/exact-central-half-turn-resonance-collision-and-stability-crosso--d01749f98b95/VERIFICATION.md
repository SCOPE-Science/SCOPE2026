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

On the central strip with the stated parameters, the rotation increment lies in (0,1) and ω decreases strictly for 0<v<1, including ε=1 since 1+ε−2εv²>0 there. Hence a genuine half-turn at each step forces both heights to be ±Y, with the smaller quadratic root in (0,1). Equal heights force x=0,1/2; for reversing heights there is exactly one +Y endpoint per orbit and its sine equals 2Y/b. This proves the count, merger, and least period. The kick–twist derivative has determinant one; the second step reverses the cosine sign and, only on a reversing cycle, the sign of the twist derivative. The products have traces 2−c²w² and 2+c²w² respectively, and at the merger the two zero-cosine shears cancel exactly. The equality b_c/b_f=Q_ε(t) follows by eliminating a; Q_ε is strictly increasing throughout (0,1), with Q_ε(0)=0 and Q_ε(1/4)>1, and a(t) increases with a(1/4)<1 for all allowed ε. Thus a unique reachable t_*<1/4 decides nonempty open coexistence, and ε=1 gives the stated closed forms. The proof's use of b<1 describes the open coexistence interval: on the allowed endpoint b=1 itself the same traces also permit coexistence if b_c<1<b_f. The theorem does not exclude this endpoint and makes no assertion of nonlinear stability. Frozen VERIFICATION.md and verify_halfturn.py were inspected, not run. Independent lifted-map and Jacobian checks covered 117 orbit evaluations including mergers and b=1 (python -I /workspace/branches/independent_checks.py 3).

## originality

PASS

The numerical collision and the indicator points are already published. In fact the same-map indicator coordinates in Grime et al. make the collision threshold a short calculation: demanding a half-turn at (1/4,b/2) yields ω(b/2)=1/2 directly. Do not credit a new collision phenomenon or a new indicator criterion. The supported distinction is the exhaustive restricted census together with exact linear types, the full identity return at the singular merger, and the unique crossover comparing the two different thresholds. The closest prior statements and methods do not give or mechanically determine that combined stability classification. No absolute priority or conclusion about the full-cylinder period-two census is asserted.

## value

PASS

The scope isolates the primary half-turn resonance in a published model and relates to a concrete numerical bifurcation, rather than carving out an arbitrary parameter slice. The complete branch classification and crossover give an exact way to identify whether the reversing saddles can coexist with elliptic constant-height cycles, and the identity return distinguishes the merger from merely trace-two monodromy. These are useful for linear bifurcation diagrams without inferring nonlinear stability or global transport. The indicator calculation alone would not merit the same assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
