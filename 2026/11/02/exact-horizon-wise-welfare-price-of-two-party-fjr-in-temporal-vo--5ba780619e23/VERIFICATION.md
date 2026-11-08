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

PASS: In the static complete two-party election with majority a=n-b, minority b, L rounds, party-list FJR+ reduces to lower-quota representation (Teh Prop.3.4, affirmed explicitly in accessible public abstract). Thus minority requires q=floor(Lb/n), majority at least floor(La/n), and selecting q minority rounds is feasible and utilitarian-optimal since a>=b. Ratio R=aL/[aL-(a-b)q]. For x=b/n and j=floor(Lx), fixed j>=1 R strictly decreases with x in stratum, attaining maximum at x=j/L (n=L,b=j), while j=0 price1. The continuous envelope f(z)=(1-z)/(1-2z+2z²) has derivative sign 1-4z+2z² and unique maximizer alpha=1-1/sqrt2; floor/ceil adjacent grid j maximize. Independent all-feasible integer-seat enumeration for L=1..39 and electorate 2..99 agreed with proposed horizon bound and feasible optimum. Exact values P3=P4=P6=6/5, P5=20/17, P7=35/29 and O(L^-2) convergence by smooth stationary Taylor theorem follow analytically. Full original Proposition 3.4 manuscript could not be accessed, which is a material check limitation, but its lower quota equivalence is stated by Teh in accessible public abstract.

## originality

PASS

Best-of-knowledge originality of the stated final claim (not preceding methods or special cases), with explicitly bounded access and implication risks. Restating FJR+ as two-party apportionment lower quota is a valid alias. The new ratio is an additional extremal optimization across all rational party shares and L, not simply the old quota characterization.

## value

PASS

PASS: Determines a sharp all-population, integer-horizon utilitarian cost of a well-defined temporal proportionality axiom in a natural two-party subdomain, including attainment, oscillations and limiting irrational constant. Although optimization is elementary once the lower-quota reduction is known, the complete exact discrete price frontier answers the explicit welfare-loss question and can be used as a benchmark for more parties and competing axioms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
