---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For every h,x0 positive, inspect the primitive pair (u0,v0)=(x0/g,h/g), T:(u,v)->(u²+v²,uv), and the exact Q_(j) square identity. Coprimality and odd/2-adic valuations give F_j iff a prime divisor of h divides u_(j-1). Locally the initial nonzero projective ratio z modulo p has exactly one x0 residue class modulo p^(a+1). Depth-1 preimages z²+1=0 and depth-2 preimages z² ± i z+1=0 (discriminant -5) give c_(p,2), c_(p,3) including p=2 and repeated-root p=5. Depth-1 and depth-2 sets are disjoint and ∞ absorbs all subsequent zero hits. CRT over h rad(h) yields all four exact joint probabilities and proves all-index rigidity iff h has no factor 5 and no p≡1,9(mod20). Actual RESULT.md/verify.py read; independent exact integer-residue calculations reproduced h=1,2,4,5,13,17,26,41,65, including h=26:175/676 and overlapping events h=65:4 classes. The finite checks corroborate the analytic all-h proof, not replace it.

## originality

PASS

Best-of-knowledge original scope is the precisely quantified final claim, not known ingredients or convention changes. Four independent implication/convention comparisons and identifiable primary literature were assessed; inability to read a plausible source is explicitly retained as a residual risk, not treated as proof of noncoverage.

## value

PASS

The source asks for density laws for its reciprocal-sum square anomalies; the two-index joint distribution with exact prime-power periodicity and sharp characterization of a natural all-index Bernoulli class solve a motivated arithmetic/dynamical problem. This is not merely the known one-failure-per-prime criterion or the routine inverse quadratic: the full density and zero-depth stopping law depend on how the local preimage trees meet the recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
