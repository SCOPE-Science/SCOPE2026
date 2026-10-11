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

The comparison is equivalent to Omega_N>(N+2)^2/8. The source proves Omega_N>(N+1)^2/varpi^2 and an exact shooting sign test. An elementary 16-cell upper Riemann-style bound gives varpi<2.7, so for N=21+m the desired tail follows from 800(N+1)^2-729(N+2)^2=71m^2+1666m+1559>0. The only admissible even cases left are N=2,...,20. I independently replayed the exact rational interval algorithm from the frozen verifier and reproduced the strict crossing indices {2:1,4:3,6:4,8:6,10:8,12:9,14:11,16:13,18:14,20:16}, as well as the certified varpi upper bound 2.685341233...<2.7. Thus finite computation is exhaustive only for ten explicitly bounded cases, while the infinite tail is analytic. The ratio limit follows directly from the source asymptotic Omega_N/(N+1)^2 -> 1/varpi^2.

## originality

PASS

Kim--Ryu--Das Gupta prove the exact LemniAcc certificate, the strict lower bound Omega_N>(N+1)^2/varpi^2, and an exact shooting/bisection criterion. On the comparison page they state the even-horizon OGM--OGM-G bound 64/(N+2)^4 but compare only the leading asymptotic constants. The inspected full primary PDF does not state all-even finite-horizon dominance. The submitted result supplies the missing finite-horizon implication by combining a certified elementary bound on varpi for the tail with exact shooting certificates for the ten exceptional even horizons.

## value

PASS

The source itself motivates the comparison but reports only the asymptotic constant improvement. Ruling out every finite even-horizon crossover is a natural guarantee-level boundary question, and the proof combines a meaningful finite cutoff with a rigorous analytic tail rather than extrapolating numerics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
