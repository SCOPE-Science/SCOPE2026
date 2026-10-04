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

The checker enumerates every labeled simple graph \(H\) on one through five vertices. It computes the connected components of \(H\), constructs \(H\circ K_1\), and tests the super domination definition directly for every candidate subset of size at most \(|V(H)|\).

For each base it independently verifies that no smaller set works, that the complete set of minima is exactly the family obtained by choosing a union of base components and swapping originals for their private leaves on those components, and that the number of minima is \(2^{c(H)}\).

Recorded output:

```text
VERIFY_OK
base_graphs_checked = 1099
vertex_subsets_checked = 664105
minimum_super_dominating_sets_checked = 3260
all labeled simple base graphs on n = 1..5
all corona minima have size n
all minimum sets correspond exactly to unions of base components
all minimum-set counts equal 2^c(H)
```

The exhaustive computation is finite corroboration only. The arbitrary-order theorem follows from the component-separation proof.
