---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The 13 independent checks (overall binary parity and two F64 field moments of exponents 1,5) leave dimension 64-13=51. The four points a+v F4 have vanishing zero, first and fifth moments because sum t=sum t^2=0 and t^4=t in F4. Every 4-point zero-syndrome set has form {a,a+s,c,c+s}; the fifth moment forces ((a+c)/s)^4=(a+c)/s and distinctness yields the two nontrivial subfield values. Exact independent GF64 arithmetic enumerated 336 distinct lines, checked all zero syndromes and rank 51 for their GF2 incidence vectors, and exhausted 336 weight-four solutions; so inclusion plus equal dimension yields equality. Earlier known line automorphism group is transferred, not rediscovered.

## originality

PASS

Best-of-knowledge original full statement after specific same-object and theorem-level comparisons, including relevant published Resultary findings and primary sources. The results attributed to earlier authors are not counted as new; residual risks remain explicit. The near-corollary potential for the code bridge has been acknowledged and its coordinate-level identification is the narrow accepted contribution.

## value

PASS

The coordinate-level equivalence of a newly constructed cyclic completely regular code with a classical affine geometry incidence code identifies its minimum supports and makes established geometric structure immediately applicable to a separately defined code. This is a useful exact cross-description bridge, although not a new rank, automorphism group or parameter theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
