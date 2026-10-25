---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The displayed CRT conditions have unique residues c,d in [1,M_k], and 0<c<b, 0<d<a force all nonnegative solutions of N=kab-ac-bd to have exactly t=1,...,k-1. At index t the prime p_t divides both x=tb-c and y=(k-t)a-d, excluding primitive multipliers without a finite-enumeration assumption. For k=2 positivity follows from both strict inequalities. The primorial PNT bound log M_k~k log k with k=floor((1-epsilon)log H/loglog H) gives M_k=o(H) and the uniform liminf at least one. At k=5, M=210, H>=413 gives ab/(a+b)>206, hence the strict 4(ab-a-b) bound. Independent diagnostic verified 104 CRT witnesses with 270 explicitly enumerated nonprimitive representations.

## originality

PASS

The fixed-generator-sequence lower bound of Ding–Wang–Zhang does not imply a uniform growing all-pairs lower bound; their Theorem 1.6 only gives the ab-scale globally. Jaffe explicitly conjectures a 4-times classical Frobenius lower bound, rather than proving the claimed large-minimum-parameter version. The uniform primorial obstruction is an additional quantified result, though independent derivation by older CRT/Jacobsthal methods remains possible.

## value

PASS

Primitive-coordinate two-generator Frobenius gaps are a natural Diophantine invariant with an explicit prior lower-bound conjecture. Upgrading G/(ab) from a universal constant to divergent all-pairs growth, with constructive witnesses and a finite sufficient fourfold threshold, is a motivated gap and not merely a computational slice. The lower constant is not claimed sharp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
