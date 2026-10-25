---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For odd d>a and positive a, least positive odd u≥B/A gives unreduced A⁺=Au−B, B⁺=Bu and 0≤A⁺<2A. With Q_j=∏_{i=j}^{h−1}2lcm(1,…,2^i a), equal positive numerator and B congruent mod Q_j imply the odd ceilings differ by 2Q_{j+1}t, hence both successor numerators match exactly and denominators match mod Q_{j+1}; induction proves all fixed-h stopping classes periodic even without termination. For 2/d, first branches yield T=2 at d≡1 mod4 or d≡3 mod12; elsewhere numerator 3→4→5 with B=d(d+3)/2, C=B(B+4)/3≡7 mod8, finishing at fourth step iff B≡0 or1 mod5. CRT gives {7,35,47,55} mod60; maximal proper divisors 30,20,12 fail as periods. Hence relative densities 2/3,2/15 and <=4 total 4/5. Independent bounded recurrence implementation agrees; no infinite stopping claim.

## originality

PASS

The existing algorithm, parity alternation, and the two-term numerator-two classification are credited. Fixed-prefix parametric expansions (Louwsma–Martino 2023/2025) are closer than generic modular numerators but inspected theorem statements do not supply a uniform fixed-initial-a horizon period or the exact minimal mod-60 four-step census as stated. Best-of-knowledge residual broad-fixed-prefix implication remains.

## value

PASS

A general bounded-horizon rational density theorem is a rigorous partial invariant in an unsettled odd-greedy termination problem, and the first nontrivial 2/d four-term density, exact residue classes and smallest modulus quantify a natural follow-up to the known two-term theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
