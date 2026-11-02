---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Test the weak parabolic equation against the constant spatial function, using the no-flux boundary. The aggregate stored drawdown M(t)=int_Omega S(x)s(x,t) dx satisfies Mdot=Q-L and M(0)=0 for all admissible locally integrable source histories. If lambda/S=kappa a.e., then L=kappa M exactly; solving Mdot+kappa M=Q yields the stated convolution and constant-rate law, independent of T, Omega and spatial pump profile. Conversely, fix an arbitrary nonnegative spatial profile w integrating to one and a regular time profile with Q(0)>0. Strong continuity of the parabolic semigroup in the storage variable gives L(t)=Q(0)t int(lambda/S)w+o(t), even when pointwise time derivatives of a weak L1 source need not exist. If all spatial profiles give the same L(t), the initial slope is independent of w, forcing lambda/S to equal a constant a.e. For lambda=0 the output vanishes, including kappa=0. No pointwise drawdown invariance is claimed. An independent exact two-cell finite-volume generator with distinct storages and common lambda/S was shown to preserve Mdot+kappa M=Q under arbitrary no-flux exchange; perturbing the ratio made the initial output slope location-dependent. This is corroboration, not the infinite-dimensional proof.

## originality

PASS

Butler–Tsou (Water Resources Research 2003, DOI:10.1029/2002WR001484) prove homogeneous bounded aquifer scale invariance via image wells and state a fully general proof for complicated geometries had not been obtained in their framework. Their theorem and transfer formula are PRIOR for homogeneous leakance/storage. They do not formulate the heterogeneous coefficient iff lambda/S constant for all spatial pump profiles and arbitrary time total-rate histories. The new result is not that generic conservation of total mass is new. Best-of-knowledge novelty assessment of the surviving precise mathematical contribution; unsuccessful database search is not proof of absolute priority.

## value

PASS

The invariant makes a physically useful, geometry-independent exact aggregate leakage prediction and states the sharp condition under which heterogeneous storage and leakance preserve it. Its necessity supplies a falsifiable diagnostic: varying pumping placement reveals nonconstant lambda/S at initial time. Although the proof is short mass balance plus a source-separation argument, the iff classification across arbitrary transmissivity tensors and Lipschitz geometries is motivated by an explicit historical aquifer-invariance question and is more substantive than an isolated normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
