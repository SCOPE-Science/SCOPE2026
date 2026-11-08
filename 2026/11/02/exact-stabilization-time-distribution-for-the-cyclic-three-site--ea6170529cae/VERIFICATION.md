---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The majority update flips x_i precisely if both incident walls are 1. XOR differentiation gives d_i’=d_i(1⊕d_{i-1}⊕d_{i+1}); zero walls persist while each bounded run of one-walls erodes by two from its ends, with an isolated 1 fixed. Thus first-fixed time is floor(q/2), q=max one-run length in a non-all-one wall word. Exactly the all-one wall state yields a nonfixed alternating temporal 2-cycle, possible only at even n and represented by exactly two x. A cyclic wall word comes from x iff its parity is even, with two preimages. A (L+1)-state transfer matrix counting cyclic one-runs bounded by L has det(I-zT)=Q_L(u,z); the trace/log determinant and parity projection yield the all-n,t cumulative rational GF. Edge cases n=1,2 are covered. Independent exhaustive synchronous evolution and coefficient enumeration checked n=1..14; all-n follows from wall and transfer proofs.

## originality

PASS

Tosic–Agha Lemmas 3–4 identify fixed states, alternating cycles and transients for majority update, and Tosic later counts fixed states t=0. These do not imply individual first-fixed times or joint all-n,t distribution. Inokuchi–Sato study fixed rather than cyclic boundaries; Nakar–Ron discusses general-radius eventual configuration structure. The early Goles–Martínez 1990 monograph is highly relevant but full text inaccessible, explicitly retained as priority risk.

## value

PASS

The longest-wall-run stopping time and bivariate rational count determine exact finite-ring relaxation statistics for a canonical deterministic cellular automaton; this is a natural complete time-distribution refinement of known attractor classes, not merely an elementary observation that fixed states exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
