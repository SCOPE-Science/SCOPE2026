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

The cyclic unit group order 2047=23*89 makes the nonprimitive set precisely mu23 union mu89. Independently evaluated all four explicit GF(2)[T] carryless Bezout polynomial identities for (r,s)∈{23,89}²: each U(T)(T^r+1)+V(T)((T+1)^s+1)=1 exactly; hence no common root in any extension. Separately constructed F_2048 via x^11+x^2+1 and exhausted nonzero elements: exactly 111 nonprimitive, zero consecutive pairs. Composite m<11 have proper subfields with nontrivial x and x+1 of lower order; prime m<11 give Mersenne prime 3,7,31,127. Euler phi gives 1936/2047 and the threshold implication follows by counterexample, not extrapolation.

## originality

PASS

The actual obstruction is a negative first-boundary for fields with composite multiplicative order; prior sufficient conditions at theta<8/9 do not imply either a pair or a no-pair result at theta=1936/2047. Relevant 2026 specialist preprint could not be read in full because lawful full-text routes failed and the institutional connection reported VPN disconnected; best-of-knowledge PASS retains explicitly high comparison risk.

## value

PASS

Exact first composite-order failure and universal upper bound on an existence-threshold parameter answer a concrete boundary question in finite-field primitive-element theory. Four extension-independent polynomial certificates make the fact independently reusable, not merely a failed random search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
