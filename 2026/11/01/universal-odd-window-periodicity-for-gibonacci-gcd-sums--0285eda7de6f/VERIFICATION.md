---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For nonzero integer seeds, normalize by d=gcd(|a|,|b|), obtaining primitive u,v; the quadratic norm mu=v^2-uv-u^2 cannot vanish because z^2-z-1 has irrational roots and zero-u case contradicts primitivity. The recurrence changes the norm sign each step. First-power windows obey an order-2 recurrence, hence infinite gcd equals gcd(g_{k+1}-g_1,g_{k+2}-g_2); for odd k, equality of shifted states modulo this gcd forces the norm difference 2mu to vanish modulo the gcd. Square-window sums obey the integer order-3 recurrence q_{n+3}=2q_{n+2}+2q_{n+1}-q_n and telescope to three reported differences; exact identity Z-2Y-X=2mu for odd k supplies the bound. Both gcds (after d/d^2 scaling) are divisors of M=2|mu| and depend only on the recurring state modulo M; invertible matrix determinant -1 gives period pi and even common T=lcm(2,pi). All-zero seeds give identically zero gcds. Independently implemented exact checks on 120 nonzero seed pairs in [-5,5]^2 and 15 odd k per seed: 1800 window/period/divisibility checks agreed. The all-input conclusion follows from the displayed algebra, not the checks.

## originality

PASS

Best-of-knowledge originality for an affirmative universal answer to Mbirika-Spilker Question 6.4, including all integer seeds, both odd-window gcd functions and a computable common even period. The 2021 paper gives the first-power gcd; the 2022 paper gives square gcd and odd-window bound, and explicitly asks the periodicity condition rather than answering it. The additional first-power norm bound and simultaneous finite-modulus reduction are short deductions; implicit-coverage risk is substantial and recorded.

## value

PASS

Explicitly resolves the natural, previously stated Mbirika-Spilker Question 6.4 about which integer seeds yield simultaneous odd-window gcd periodicity, with a uniform answer and constructive common period. Though short and highly dependent on published gcd identities, the observation links a nonzero Cassini norm to bounded gcds and modular dynamics for all integer initial conditions; this is a motivated complete classification, not a random numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
