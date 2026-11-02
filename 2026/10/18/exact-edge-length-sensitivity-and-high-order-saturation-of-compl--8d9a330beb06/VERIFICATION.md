---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For p,q≥2,d=p+q-1,h∈[1,3], the graph shortest-path metric gives cross edges 1 except a_1b_1=h, with a three-hop alternative at h=3. The determinant-one change t=f(b_1),u_i=f(a_{i+1})−t,v_j=f(b_{j+1}) reduces the entire anchored ball to coordinate cubes and |t+u_i−v_j|≤1,|t|≤h. Differentiation at ±h is justified by Fubini/slab sections and sign symmetry. For h≥1 the upper inequalities lead to min v−max u≥h−1, and integration of the u maximum gives S(h)=(p−1)!(q−1)!/(d−1)!·(3−h)^{d−1}. Thus V′(h)=2S(h). The h=1 baseline follows from range density p(p−1)r^{p−2} and beta integral, V(1)=2^d p!q!/d!. Integrating proves the displayed V(h), its strict growth, h=3 redundant-edge ratio, derivative vanishing through order d−1 and nonzero dth derivative, with fixed-n pq comparison. Independently enumerated 12 rational/integer Ehrhart cases directly from original anchored inequalities and four symbolic derivative examples. Finite tests corroborate but do not replace the all-parameter analytic proof.

## originality

PASS

Qualified best-of-knowledge novelty: the known h=1 complete-bipartite baseline is not claimed new. Primary full-text and Resultary comparisons cover the same polar Banach object, primal symmetric-edge lattice invariants, generic Lipschitz-polytope faces, a related rooted two-level signed-chain volume, and the all-within-part snowflake facet count. None of the inspected theorems supplies or is shown to imply the explicit one-distinguished-cross-edge volume for all real h∈[1,3] and its sharp (3-h)^d saturation. Earlier synonymous weighted-polar formulas or general volume-spline theorems may exist.

## value

PASS

The object and invariant are intrinsically motivated: quantitative Lebesgue-volume response of a finite-metric Lipschitz dual unit ball as a single cross-edge constraint weakens and becomes redundant. The exact all-p,q and all-real-h law determines a sharp d-th order contact at edge deletion and a nontrivial relative gain 2/(pq), distinguishing balanced from unbalanced bicliques. This is not a routine substitution into the known undeformed volume or merely a tiny finite enumeration, and serves as a precise benchmark for metric/polytope perturbation geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
