---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For a path/cycle component with order at most k, the complete component weakly blocks any split, so it must stay intact. For a component >k, splitting coalitions into induced connected pieces preserves utility. Any piece of length <k may absorb adjacent endpoint without utility decrease for either side and with one strict gain, forcing all pieces length k; divisibility follows. Conversely any deviation improving a boundary endpoint of a full k-block must keep its utility-two internal neighbors and recurse through the original block, requiring k+1 vertices. k=1/2 and cycle boundary cases handled. Larger cycles have k tiling offsets, paths one; intact small labeled components can merge subject to total weight ≤k and are counted by restricted multivariate Bell EGF. Independent direct checks gave P4,k3 0; P6,k3 1; C6,k3 3; edge plus two isolated,k3 4. No heterogeneous weights or maximum degree>2 covered.

## originality

PASS

The friendship-game definitions and general bounded-size strict-core complexity are prior work. Here the exact path/cycle component-divisibility criterion and weighted-Bell enumeration under weak blocking and unrestricted disconnected coalitions is a distinct complete classification not implied by general hardness, ordinary-core or connected-communication restrictions. Mathematical value arises from an exact infinite network class and complete partition count.

## value

PASS

Complete all-k existence/partition classification for natural degree-two positive friendship networks, including sharp path divisibility obstruction and labeled disconnected-component census; exact counts can be needed for welfare/stability enumeration and are not inferred from generic core hardness alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
