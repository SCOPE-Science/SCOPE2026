---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Unrestricted distinct deletion shadows form a set-packing instance on all 64 outputs; binary constraints exactly express disjointness. I independently exhausted it using integer exact cover, not the packaged MIP. Give a triple weight 4 if constant, 2 if nonconstant with an adjacent repeat, 1 otherwise, for total 100. Each of the 256 word shadows has weight at least 4, checked during exact generation. Add a singleton unused-output tile for each output, with cost its weight; a word tile costs its shadow weight minus 4. A code plus its unused outputs is an exact tiling, with total nonnegative cost 100−4|C|. Thus no code has more than 25 words. To test size 25 and exhaust size 24, fix budgets 0 and 4. At each step choose a remaining output and branch over all tiles containing it that fit entirely in the remaining set and within the remaining budget; accept only complete tilings of exact cost. Bit masks are integers and the branches exhaust all codes without trying to infer anything from time limits. Budget 0 has no tiling (21 recursive calls). Budget 4 has exactly the six claimed profiles (108752 calls): (4,8,4,8), (4,9,2,9), (4,10,0,10), (4,10,2,8), (4,11,0,9), (4,12,0,8), with respective coverages 64,64,64,62,62,60. All six frozen witnesses were also verified independently by direct deletion and set disjointness. Defect is 64 minus coverage and only a full cover is perfect.

## originality

PASS

The optimum, both endpoint coverage witnesses, and in fact all three n_3=0 profiles are prior or implied by the published constructions. The distinct supported result is the complete profile spectrum, including the three n_3>0 profiles and exclusion of every other profile. The existence of coverage 62 alone is not a distinct claim.

## value

PASS

At the smallest nonbinary even alphabet size, the result determines how every optimal-length-four deletion code uses the received space, not simply whether optimal codes can be perfect. The joint run/shadow profile resolves a natural equality-structure question, giving three new types with 3-shadow words and sharp exclusions not furnished by the known optimum and constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
