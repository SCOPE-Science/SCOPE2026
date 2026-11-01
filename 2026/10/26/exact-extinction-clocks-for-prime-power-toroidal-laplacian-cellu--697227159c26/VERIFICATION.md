---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Read exact operator in RESULT.md including repeated neighbors for 2-cycles and the -4f term. Via X=1+u,Y=1+v, the periodic group algebra becomes F_p[u,v]/(u^(p^a),v^(p^b)); the Laplacian multiplier is u^2/(1+u)+v^2/(1+v). Each candidate term A^j B^k has unique lowest bidegree (2j,2k) among j+k=t, preventing cancellation. Lucas no-carry criterion gives maximal surviving t: p odd j=(p^a-1)/2,k=(p^b-1)/2, while p=2 maximal t=2^(a-1)-1. Top odd-degree A^j B^k becomes u^(p^a-1)v^(p^b-1), equal to full group sum, with coefficient (-1)^(b(p-1)/2); rank-one kernel count then exact. Independent sparse-polynomial ring iteration verified 9 parameter triples including small 2-cycle sides. These finitely many tori are not proof of the general clock.

## originality

PASS

The exact p-characteristic finite-torus extinction clock and odd-prime final rank-one group sum are additional to the inspected broad Frobenius dilation identity and the revised source paper. Residual group-algebra priority risk remains.

## value

PASS

A complete universal extinction-time classification for a natural finite linear cellular automaton, including a striking characteristic-two versus odd-prime distinction and an explicit final one-dimensional image. It supplies mathematically useful precise transient and survival-count information not contained in a generic nilpotence assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
