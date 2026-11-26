---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For anchored x with range r, the y-fiber is a product of q intervals of length 2-r. In each chart specifying the two distinct extreme labels, anchoring leaves Jacobian r^(p-2) for the p-2 normalized interior coordinates and r; the determinant after removing this factor has absolute value one whether the anchor is extreme or interior. The common chart density therefore gives both the beta range and the independent indexed sampler. Permutation symmetry of the zero-sum representative excludes all mixed sector blocks. The endpoint/interior sample has E(sum_i(T_i−mean T)^2)=(p+1)(p+2)/(12p) and Var(mean T)=(p−2)/(12p²); combining these with the beta second moments yields the two within-part eigenvalues. The squared unit-contrast component is pq/N times the squared part-mean gap; the gap variance is (1+2/(pq))/(3(N+1)), giving the third eigenvalue. The anchored-to-zero-sum Gram determinant is 1/N. The covariance determinant and volume then give the stated isotropic constant. Uniformly in both part sizes, replacing log((p+1)(p+2)) by 2 log p incurs O(1/p) before multiplication by p−1; the analogous q term, contrast and Stirling factorial errors give O(log N/N) after division and cancellation. For fixed p, qS tends to Gamma(p−1,1), independently of the CLT fluctuation of the independent uniforms and of T; the shift √q S times the bounded anchor term vanishes. Independently integrating the K_{2,2} fibers (length 2−|x_2|) gave intrinsic volume 8/3, half-range density 3(1−s)^2 and sector variances 1/5, 1/5, 1/10. The frozen verifier was inspected, not run; its reported eight cases use floating hull triangulation and exact rational integration, and are not the general proof. No issue found at p=2 or at eigenvalue coincidences.

## originality

PASS

The supported contribution of this frozen record is the continuous bulk disintegration and full covariance with their asymptotic consequences, not the dual volume alone. Distinct later indexed records materially reproduce the beta range and, in one case, the same sampler and covariance; this is verified equivalent coverage in the current catalogue, not evidence that these results predate the frozen record. The inspected earlier or contemporaneous statements establish the volume, vertex structure, vertex-optimization quantity, or statistics of other objects, not the claimed bulk evaluation. Priority is not certified.

## value

PASS

An exact sampler and covariance give interior geometric information not captured by enumerating vertices or measuring volume. The decomposition resolves two internal fluctuation scales and the inter-part contrast, and the fixed-part regime separates non-Gaussian extremes from Gaussian mean fluctuations. The uniform isotropic asymptotic compares balanced and arbitrarily unbalanced splits in a single Euclidean normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
