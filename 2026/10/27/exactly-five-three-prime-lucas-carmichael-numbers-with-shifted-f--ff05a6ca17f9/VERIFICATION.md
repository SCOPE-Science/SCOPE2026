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

The congruence p+1 | qr−1 follows by substituting p≡−1 under that modulus, and cyclically. If d divides two normalized shifts, the associated original shifts share gd, and the congruence forces the third prime to be −1 modulo gd. Thus d divides the third normalized shift, making all three normalized shifts pairwise coprime since their triple gcd is one. This proves the LCM is gabc, so the displayed quotient T is integral. For x=1/a, y=1/b, z=1/c in (0,1], xy+xz+yz≤x+y+z, so λ=g²−T is positive for g≥2; also λ<3g/a. Hence a<3g. At g=4 each coordinate reciprocal has strictly positive coefficient 4 minus the other two reciprocals, so the bound with b=a+1 and c=a+2 decreases as a increases; it gives 422/429 at a=11 and leaves just p=3,7,11,19,23,31. The positive integer h=(pq−1)/(r+1) is less than p, and h(pr−1)=p²(q+1)−(p+1)(p+h). This bounds q≤2p²+p−2, with r≤pq−2. These bounds also prove effective finiteness for every fixed even G. Independent replay (python3 /workspace/lucas_g4_check.py) used an Eratosthenes sieve and traversed r≡p⁻¹ mod q+1, testing all original conditions and the shifted gcd. In p order the six unrestricted counts were 1,3,9,9,10,5 and the exact-gcd counts 1,1,1,1,1,0. The additional coarse-bound prime 43 gave none at G=4. The exact outputs are (3,7,19):399, (7,19,43):5719, (11,31,67):22847, (19,83,787):1241099, (23,67,139):214199. Exhaustion rests on proven bounds, not extrapolation. The frozen script was inspected but not run.

## originality

PASS

The supported distinct claim is global exhaustion of the three-prime exact G=4 stratum, with a uniform effective least-prime bound for any fixed even shifted gcd. The known membership of individual integers and the precursor congruences, normalization and fixed-first-factor bounds are not novelty claims. Among checked sources, no theorem covers the new least-factor bound or full G=4 exhaustion.

## value

PASS

The common shifted gcd controls overlap of the three defining congruences. The result resolves the next possible stratum after G=2 without an arbitrary size cutoff and gives an effective reduction for any fixed even stratum. It provides a usable exact benchmark and a structural reason that a finite census is complete, rather than merely listing five known values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
