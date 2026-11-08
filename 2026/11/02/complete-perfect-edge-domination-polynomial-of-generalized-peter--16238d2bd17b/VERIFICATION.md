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

For cubic H, a perfect external-edge-dominating set F has vertex selected degree 0,1,3, with L={degree0} independent and A_H 1_L=0 over F2; conversely the independent parity kernel constructs F uniquely. For GP(n,3), a_i=1_L(u_i), b_i=1_L(v_i)=a_{i-1}+a_{i+1} and the inner equations yield (1+T²+T⁴+T⁶+T⁸)a=0, hence (1+T^10)a=0. Thus sequences have period gcd(n,10) and reduction to at most 2^10 binary outer words is exhaustive. I independently enumerated every word of periods 1,2,5,10 and recovered counts {0:1},{0:1},{0:1,4:5},{0:1,4:10,6:20,8:5} by L size. Since |F|=3n-3|L|, this proves the complete stated polynomial for all n>=7 and clarifies the d=10 coefficients and minimum 5 matching sets. A finite direct edge-definition checker is part of the package; the all-n argument is the period reduction plus exhaustive finite table, not extrapolation.

## originality

PASS

The 2022 GP(n,3) perfect two-coloring paper already establishes a 5-divisibility existence pattern corresponding to the minimum dominating induced matching case. The present result is only the complete labelled size-refined perfect external-edge domination polynomial, especially the 20 and 10 nonmatching classes at even multiples of five. Historical exact counts remain a risk.

## value

PASS

Full exact perfect edge domination generating polynomial on an infinite natural cubic family is a useful benchmark and exhibits a nontrivial parity/divisibility transition. The nonmatching 20- and 10-solution branches are not implied by the prior induced-matching existence theorem; the finite state reduction is a complete legitimate proof component.

The dated certificate retains the supplied scientific assessment, sources and limitations.
