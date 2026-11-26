---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The four-cycle through r proves strong connectivity on the same seven positive arcs for every z>0. Of the eight nonroot parent assignments, two close b↔x and one closes b→x→y→b. The five remaining assignments (parents of b,x,y in that order) are (r,b,r), (r,b,b), (r,y,r), (r,y,b), (x,y,r), of weights z²,z³,z,z²,1. The second alone has off-diagonal LCA b; the first, second and fourth contribute to x's ancestor probability, and the second and fourth to y's. Thus with Z=1+z+2z²+z³ the probabilities Hx,Hy,a are z²(z+2)/Z,z²(z+1)/Z,z³/Z. The stated law gives f(x)Hx=f(y)Hy and the diagonal LCA events are zero, so the iid ratio is a/(2HxHy)=Z/[2z(z+1)(z+2)]. Its small-z divergence is 1/(4z); subtracting the denominator from the numerator gives 1−3z−4z²−z³, strictly decreasing from 1 to −∞. Exact substitution at 1/8 gives Hx=17/593, Hy=9/593, a=1/593, and ratio 593/306. All identities follow from the complete symbolic enumeration; the frozen seventeen-parameter checker was inspected, not run or relied on.

## originality

PASS

The supported distinct claim is unbounded failure at fixed size under arbitrary positive asymmetric arc weights, not an undirected result or priority for general failures of negative dependence. The closest source controls the same observables on weighted undirected trees only. No inspected result covers this directed witness or implies the unbounded LCA ratio on a fixed strong digraph.

## value

PASS

A four-vertex construction with an exact divergence rate answers a natural robustness question for a structural undirected ancestor inequality. It rules out every graph-independent multiplier, not just the original constant, even under strong connectivity. The witness is useful when deciding which hypotheses directed analogues need; the finding does not assert minimal size or address reversible subclasses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
