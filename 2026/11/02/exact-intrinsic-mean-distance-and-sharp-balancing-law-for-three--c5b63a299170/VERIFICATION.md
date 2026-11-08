---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. With three positive sorted metric edge lengths 0<a<=b<=c and independent arclength-uniform X,Y, the only simple routes lead to same-edge integral I(L,s)=L³/3-(L-s)_+³/12 and distinct-edge baseline J0(r,s)=r²s/2+rs²/4−r³/12; the unused short edge supplies an exact two-corner correction on (b,c). Assembling ordered pairs recovers the homogeneous cubic numerator. Setting u=b−a,v=c−b, direct coefficientwise algebra verifies 108T²(E−5T/27)=36au²+36auv+36av²+2u³+3u²v+15uv²+7v³, strictly positive except u=v=0. The isosceles derivative (x−1)(11x−3)/48 changes sign at 3/11, refuting Schur-convexity and the strict equilateral minimum refutes Schur-concavity. Independent exact symbolic and numerical integral checks agreed; no use of finite sampling as proof.

## originality

PASS

Qualified best-of-knowledge novelty of the unrestricted three-positive-length theta-graph cubic, sharp equilateral minimizer and majorization counterexample. The original mean-distance-of-shapes work is prior and potentially close, but its full 1982 source was inaccessible; the broad 2023 graph algorithm and bounds do not explicitly settle the all-triples sharp inequality.

## value

PASS

PASS. Mean intrinsic distance is a standard metric-graph geometric invariant; the complete all-positive-length theta formula and sharp equal-edge minimization at fixed total length form a natural continuous optimization classification. The failure of Schur majorization is mathematically informative, and 5T/27 with unique optimizer is not a routine bound substitution or arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
