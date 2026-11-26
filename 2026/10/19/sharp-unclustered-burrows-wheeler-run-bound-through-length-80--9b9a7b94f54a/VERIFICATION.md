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

The exact same U_q(n) lower bound is established in Kumallagov Proposition 3.2 by applying the factor-two BWT amplification inequality to the Lyndon rotation, whose endpoints differ and thus whose linear and cyclic run numbers agree. For the upper bound an independent bounded program parsed the witness file with duplicate-key rejection and checked the exact set of 67 keys. For each row it verified length, ternary support and n-1 unequal adjacent output pairs; reconstructed a candidate by traversing Psi, the inverse of stable-ranked LF; verified n distinct length-n rotations and recovered the stated BWT by sorting them and extracting last letters; and counted exactly ceil(n/2) cyclic input changes including the closing edge. The checks are exact for every listed length. A ternary solution embeds in every ordered q-letter alphabet for q>=3 without changing the order of its rotations or any run count.

## originality

PASS

The actual primary preprint establishes the identical lower bound, small values and eight sharp lengths in this window: 28,29,36,37,52,53,60,61. It does not establish sharpness at the remaining 59 lengths, starting at 14; its all-length formula is a conjecture and its all-length relaxation omits one-cycle realizability. Later distinct Resultary entries cover the exact numeric assertion on 14–64 and go beyond it there in some respects; one even has the exact same length-14 certificate. Credit that overlap without inferring independent discovery or priority. The complete finite interval, in particular its tail 65–80 beyond those later consecutive ranges, was not already established by the inspected statements.

## value

PASS

This closes the first consecutive block of unchecked lengths after the previously established small cases for a named natural extremal problem, rather than choosing isolated favorable parameters. Relative to the primary preprint it fills 59 explicit gaps; the checked neighboring records still do not cover the continuous tail 65–80. The full prefix is a compact exact testbed for potential constructive proofs and rules out any counterexample at the certified lengths. The numerical endpoint is a certificate extent, not a claimed phase transition or an extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
