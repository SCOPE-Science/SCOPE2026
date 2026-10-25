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

Starting from Stern recurrence and the published uniform distribution of primitive pairs modulo m, conditioning on h=v2(t+1) gives a unimodular transform and geometric frequency 2^{-(h+1)}; the tail mass <=2^{-H} justifies natural density, not merely dyadic density. Direct even/odd four-term formulas imply the two congruence K_m branches. The branch overlap is one primitive quadruple (a,b,b-a,-a). A(m)=sum over primitive (a,b) of m/gcd(2b,m), multiplicative by CRT; splitting v_p(b) proves the odd and 2-power formulas, including 0 and m=2. Independent exact residue enumeration for m=2..12 matched S=2A-J2, giving 3,32,28,184,96,256 at 2,3,4,5,6,8. Tests finite; proof relies on Reznick/Deshouillers-Schinzel pair equidistribution for all m.

## originality

PASS

PASS best of knowledge for complete four-term joint density and full-support arithmetic. Reznick Theorem 4.7 and Deshouillers–Schinzel Theorem 1.1 determine primitive PAIR frequencies, not the two additional overlapping terms, their geometric correlations and branch-intersection correction. Automaton frameworks could in principle compute four-state laws, but no inspected theorem directly supplies exact K_m or S(m).

## value

PASS

Four-block support/density is a natural finer modular-complexity invariant of the Stern diatomic sequence: it goes beyond a pair marginal, yields positive probability support for every m and a multiplicative closed arithmetic count, and is useful for longer-block automata comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
