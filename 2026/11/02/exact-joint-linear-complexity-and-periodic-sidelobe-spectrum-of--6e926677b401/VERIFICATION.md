---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Each order-five de Bruijn cycle has one rooted 00000 occurrence and corresponds uniquely to a reversible 5-bit feedback map T_g(a,u)=(u,a XOR g(u)), g on 16 four-bit arguments; checking all 2^16 truth tables and a full 32-state orbit is exhaustive, not sampling. A second Euler-tour characterization on the four-bit de Bruijn graph supplies an independent structural enumeration. Periodic complexity is L=32-v_(x+1)(sum w_i*x^i) over F_2 because x^32-1=(x+1)^32; sidelobe P=max_{1<=t<=31}|32-2d_H(W,shift_t W)|. The bundled verifier implements polynomial/Games–Chan and signed/XOR comparisons. Independent feedback-table enumeration reproduced 2048 cycles, all 32 nonzero joint cells and their exact 32 integer counts, 12 with P=4, and 8 with L=31,P=4. Proof of exhaustiveness is fixed order-five, not an infinite extrapolation.

## originality

PASS

Qualified best-of-knowledge originality: compare exact statement and model rather than terminology. Known foundational tools, marginal/special cases and directly overlapping results are credited. No actually inspected stronger result is shown to imply the complete final claim. Unavailable or only partially inspected plausible primary work is identified in residual risks; failed searches are not treated as proof of novelty.

## value

PASS

The natural joint distribution of recurrence complexity and periodic sidelobe correlation resolves a simultaneous optimization question not settled by either known marginal distribution. The eight extremal cycles, three 4-element symmetry orbits at minimum sidelobe, and exact full joint table can support selection of finite pseudorandom/spreading sequences. The small but complete natural class is mathematically motivated and finite exhaustiveness is proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
