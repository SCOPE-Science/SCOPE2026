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

Perfect state transfer implies spectral strong cospectrality, hence same degree via the simple H=0 projector. Across bipartition, only root-hub can have equal degree; S^2(root,root)=(1/m)*sum_i 1/(p_i+1)<=1/2 while S^2(hub,hub)=(p_i+1/m)/(p_i+1)>=3/4 for degree-matched p_i=m-1, contradiction. Coutinho-Baptista Corollary 8 reduces any same-class PST in a tree to sibling leaves. The vector z with root 1, hubs 0 and leaves -1/p_i lies in ker A, so D^1/2 z lies in H=1 eigenspace and overlaps e_u+e_v for siblings; e_u-e_v independently lies there. Thus E_1(e_u+e_v) and E_1(e_u-e_v) both nonzero, incompatible with E_1e_u=+/-E_1e_v. Exact for all m,p, no finite extrapolation.

## originality

PASS

No prior mathematical result located implying the all-parameter family-specific theorem; best-of-knowledge, with residual indexed/access limitations.

## value

PASS

Attacks the explicit normalized-Laplacian tree PST problem by ruling out a natural unbounded, heterogeneous diameter-four family, with independent spectral mechanisms separating cross-bipartition and symmetric sibling pairs. The explicit obstruction is reusable for nearby rooted trees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
