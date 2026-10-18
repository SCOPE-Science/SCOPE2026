---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Let r=pg(V)-1>0. In the source canonical Stein factorization, canonical sections give a degree-a line bundle on a smooth curve Gamma with a>=h0-1>=r; curve Riemann-Roch/minimal degree forces genus zero when a=r. The base divisor inequality Ivol(V)=deg L>=a gives a=r under Ivol=r. If e=deg(Gamma -> canonical image T), then r=a=e*deg(T), while a nondegenerate integral curve T in P^r has deg(T)>=r: e=1 and deg(T)=r. Minimal-degree integral nondegenerate curve is the rational normal curve. On P1, degree of L is r, yielding L~Q O(r); the resolved canonical map factors as claimed. The pg>=2 boundary avoids r=0. Checked source Lemma 2.8 and Remark 2.6 assumptions against the actual RESULT and primary article.

## originality

PASS

Chen–Hu–Jiang–Liu arXiv:2610.02689 gives sharp volume bound Ivol>=pg-1 for kappa=1 and examples. Its explicit equality theorem concerns the kappa=2 case. The nondiagonal Stein degree-one and rational-normal-image geometry is a further equality deduction from source proof ingredients, not part of the printed inequality. No exact prior equality normal form located in checked targeted search; a standard minimal-degree curve argument may be tacit known to algebraic geometers.

## value

PASS

It identifies the entire canonical image and Iitaka base at the sharp boundary of a natural threefold Noether-type inequality, giving a geometric normal form rather than merely one equality example. It neither classifies fibers nor all equality threefolds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
