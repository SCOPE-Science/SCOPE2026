---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Gamma(10,m) is minimum count of tenth-power summands needed to cover EVERY residue; zero padding allowed and gamma(10,1)=1. For p odd!=5, nonzero-base Hensel lifting is possible since p does not divide 10: for all a>=2, gamma(10,p^a)=max(g_p,z_p), where g_p covers F_p and z_p is shortest nontrivial sum of tenth-power units equal to zero. Necessity of z_p follows by representing residue p mod p^2. For p>=6000, Fermat curve X^10+Y^10=cZ^10, genus36, Hasse–Weil and <=30 coordinate-zero/projective exceptions yield at least p-29-72sqrt(p)>0 unit representations of each nonzero c. Thus g_p=2; z_p=2 for p=1 mod4 and 3 for p=3 mod4. An independent exact bitmask implementation enumerated all 781 odd primes p<6000 excluding 5, checked the 24 exceptional prime-layer rows and 18 high-power exceptions from the inspected prime_exceptions.csv with zero mismatches. For p=2, odd tenth powers are 1 mod8; gamma exponents 1,2,3=>1,3,7 and >=4=>8, with lower bound via residue 8 mod16. For p=5, tenth powers mod25 are 0,+1,-1 giving sharp12, and binomial lifting by changing a unit base by 5^(a-1) maintains 12 for all a>=2; mod5 gamma=2. CRT gives gamma(10,m)=max of local prime-power values. Full exception lists and boundaries are in inspected RESULT.md/prime_exceptions.csv; pre-existing global supremum12 is not claimed novel.

## originality

PASS

Arias–Borja–Anaya 2023 Table 3 addresses global k up through 9, not local tenth-power prime-power lists. Alnaser–Cochrane 2008 gives general upper bounds and lifts (indeed Small 1977 already offers prime-power procedures), plus special p=2/5 values; no inspected theorem gives this exact tenth-power 24/18 exceptional table. General algorithms and upper bounds do not automatically imply particular sharp finite classifications absent execution or a closed computation. Prior published SCOPE tenth-power stable obstruction semigroup concerns positive-integer Waring gaps rather than modular p^a. Small 1977 full text was inaccessible: a same-exponent local table could exist and is residual risk.

## value

PASS

The complete local classification of an established natural modular Waring invariant for fixed exponent 10—including each exceptional prime and all power towers—fills exact arithmetic data beyond global bound12. The cutoff p>=6000 with Hasse–Weil plus an exhaustively checked finite prime range gives complete, not arbitrary sampled, classification; its local exceptions are independently reusable for composite moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
