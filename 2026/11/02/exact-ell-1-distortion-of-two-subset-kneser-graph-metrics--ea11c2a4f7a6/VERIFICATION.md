---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For KG(n,2), n>=6, disjoint vertex-label pairs have metric distance 1 and intersecting pairs have distance 2. Every L1 cut semimetric has conditional negative type on zero-sum vectors: sum(z_e z_f rho(e,f))=-2(sum_(e in S)z_e)^2<=0. Symmetrization over S_n reduces rho to values u (disjoint) and v (intersecting). With unsigned incidence matrix B and A=B^TB−2I, vector z=B^Ta (sum a=0) lies in the eigenvalue (n−4) subspace, forcing (n−4)v<=(n−3)u, so D>=2(n−4)/(n−3). For the Hamilton-cycle edge-set cut orbit, elementary disjoint/intersecting crossing fractions p_D=4(n−4)/((n−1)(n−2)), p_I=4(n−3)/((n−1)(n−2)). Scaling the averaged nonnegative cut metric by 2/p_I gives intersecting distance 2 and disjoint distance D, proving the upper bound. Independent exact intersection/crossing tests on 46449 unordered vertex-label pairs over n=6..18; finite checks not all-n proof.

## originality

PASS

All-n sharp real L1 graph distortion of reverse-Johnson/2-subset Kneser shortest-path metric, with a Hamiltonian-cycle cut upper certificate matching an incidence eigenspace negative-type lower bound. Petersen n=5 is previously published and explicitly excluded. Qualified best-knowledge priority.

## value

PASS

L1 metric distortion is a natural graph metric invariant. The family gives an exact rational sequence rising from 4/3 toward 2, with spectral obstruction unexpectedly cut-cone sharp. Hamilton cycles provide explicit optimal cuts for every n>=6; this is a full natural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
