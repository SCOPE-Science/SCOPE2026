---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof reduces the original vertex-level linear program only after deriving every local resolving neighborhood from graph distances. The included checker reconstructs each complete multipartite graph of orders \(2\) through \(10\), computes all-pairs distances by breadth-first search, rebuilds every edge neighborhood from the definition, and solves the original vertex-variable linear program using `scipy.optimize.linprog`.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
edge_local_neighborhoods_checked = 2926
orders = 2..10
all direct local-resolving neighborhoods matched endpoint-part unions
all LP optima matched 1 for two parts and k/2 for k>=3
K3 explicit feasible witness weight = 3/2
```

The checker also verifies the explicit \(K_3\) feasible witness of weight \(3/2\). The finite computation is corroborative only; the arbitrary-order correction and optimizer classification follow from the proof.
