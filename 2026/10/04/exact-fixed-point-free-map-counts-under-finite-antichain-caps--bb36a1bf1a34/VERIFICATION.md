---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Let \(Y=X\oplus A_r\) with all points of the antichain \(A_r\) above \(X\). If a fixed-point-free monotone map \(F:Y\to Y\) sent some \(x\in X\) to a new maximum \(a_j\), then monotonicity from \(x<a_i\) would force \(F(a_i)=a_j\) for every new maximum and in particular \(F(a_j)=a_j\), contradiction. Hence \(F|_X=g\) is a fixed-point-free endomorphism of \(X\). For fixed \(g\), the image of each new maximum \(a_i\) may independently be any common upper bound in \(X\) of \(g(X)\), giving \(u(g)\) choices, or any of the other \(r-1\) new maxima. No relation inside the antichain couples these choices. This gives exactly \((u(g)+r-1)^r\) extensions and summing over \(g\in\operatorname{Fpf}(X)\) proves the formula. The converse construction is immediate and proves exhaustiveness. The assigned verifier checks 265 labeled-poset instances, all \(r=2\) cases through four points and all \(r=3\) cases through three points; these computations are regression checks only because the symbolic extension bijection proves all finite \(X\).

## originality

PASS

Höft and Höft study fixed-point-free components and fixed-point-property criteria for lexicographic sums. The accessible full-text extraction is qualitative: it characterizes when fixed points must exist in components/sums and does not provide an exact count of fixed-point-free endomorphisms weighted by a common-upper-bound statistic. Barmak and Minian use non-Hausdorff suspension as a standard finite-space construction but do not supply this map-count formula in the inspected scope. Current Resultary search for suspension, ordinal sums, antichain caps and fixed-point-free map counts returns the assigned exact record plus neighboring homotopy/fixed-point classifications, but no stronger enumeration that implies \(\sum_g(u(g)+r-1)^r\).

## value

PASS

Non-Hausdorff suspension and ordinal sums are standard constructions in finite topology and poset theory. The theorem turns the known qualitative fixed-point-property behavior into an exact extension formula for every fixed-point-free base map and every cap size, isolating the natural common-upper-bound statistic. This is a concise structural lemma with reusable enumerative content rather than a small finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
