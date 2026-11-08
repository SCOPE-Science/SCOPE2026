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

Every odd 2-adic square fills 1+8Z2. For a odd and b even, (au+bu²)-(av+bv²)=(u-v)(a+b(u+v)) has second factor odd; thus the map is an isometry/bijection on each Z/2^k and Z2. Direct expansion of F2(x)=x^4−4x²+2 across valuation classes odd, 2×odd,4×odd, divisible by8 gives exactly the three stated base balls (-1+16Z2), (2+128Z2), (194+512Z2), including full surjectivity. For odd-centre balls f increases exponent one, for centre a≡2 mod8 it increases exponent two; induction yields all r. Factor c_{r+1}−2=(c_r−2)(c_r+2), with v2(c_r+2)=2, establishes v2(c_r−2)=2r+2 and disjointness at precision k>=2r+3. Counts come from full residue-ball reductions including k<=2r+2 overlap, densities from stable exponents, and fixed-point intersection from contracting centres. Independently checked actual SET equality (not just size) for 72 pairs 2<=r<=7, 1<=k<=12; finite checks corroborate but the all-r,k result is the lifting induction.

## originality

PASS

Best-of-knowledge original as a precise 2-adic three-ball and all-modulus image classification of iterated first-kind Dickson polynomials; classical polynomial identities and lifting are prior. The historically close 1991 Galois-ring paper could contain a stronger equivalent formula and was only accessible by abstract; this unresolved full-text comparison is a major qualified priority risk, NOT a proof of noncoverage. No decisive coverage evidence was obtained.

## value

PASS

Exact images and densities of the canonical Chebyshev-doubling dynamical system over Z2 provide natural p-adic arithmetic structure and a complete precision-dependent invariant; the two even branches separate at an exact sharp depth. Unlike general upper bounds or generic polynomial composition, the calculated three-ball classification is a useful self-contained exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
