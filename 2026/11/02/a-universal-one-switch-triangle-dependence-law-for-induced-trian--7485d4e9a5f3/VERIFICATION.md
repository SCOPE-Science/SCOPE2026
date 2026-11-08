---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Conditioning on a designated induced H fixes e internal edges and forbids the other internal edges; the remaining x=m-e edges are uniform among B=N-choose(h,2). All unrestricted candidate triangles count A=choose(d,3)+h choose(d,2) and triangles with an internal H edge count ed, yielding E[T|H]=A(x)_3/(B)_3+ed(x)_2/(B)_2. Baseline is choose(n,3)(m)_3/(N)_3. The ratio reduces to K*x(x-1)(x-2+c)/[(x+e)(x+e-1)(x+e-2)], c=ed(B-2)/A in (0,3e]; 3A-d(B-2)=d(d-3)(h-2)/2>=0. The derivative numerator is affine in c; at c=0 it is product of strictly increasing nonnegative factors, while at c=3e it is e(e-1) times a polynomial strictly positive in y=x-2>=0 with positive coefficients. Strict positivity holds for all relevant integer parameters, giving one-switch and motif-shape invariance. Exact checker source was inspected; separately reran rational derivative and triangle enumeration in independent_checks.py.

## originality

PASS

Conditional triangle counting is classical and general overlap calculus known, but the inspected original results concern ordinary subgraph variance in G(n,p) or asymptotic deviations, not the finite induced-H conditional ratio monotonicity with a universal derivative sign certificate and all-H same-(h,e) covariance sign.

## value

PASS

A complete all-connected-triangle-free-motif fixed-edge dependence theorem: the sign depends only on size and edge count, and can switch at most once as the number of ambient edges changes. The path/claw same-(h,e) crossing illustrates a nontrivial exact transition. This is a natural structural relation between motif and triangle statistics rather than arbitrary computed numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
