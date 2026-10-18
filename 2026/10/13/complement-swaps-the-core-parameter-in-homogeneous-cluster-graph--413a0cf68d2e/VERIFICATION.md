---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For C_{m,n}=disjoint m copies K_n and its complement D_{m,n}, every automorphism preserves class adjacency in both so automorphism groups and all injective tuple orbits coincide (partitions of k positions into ≤m blocks size≤n). A homomorphism from a loopless source clique K_n injects into one target clique: when n finite its image is exactly n vertices, and with m infinite possible finite ranks are positive multiples of n; when n infinite all ranks infinite. For D, distinct source parts must map into disjoint sets of target parts. If m finite,n infinite, each uses exactly one target part, so finite ranks are every integer ≥m; if m infinite, all ranks infinite. C is homomorphically equivalent to K_n, D to K_m, so uniqueness of countably categorical model-complete core yields respective cores, including ℵ0 and finite edge cases. Finite exhaustive checks of small m,n confirm image-rank mechanisms but infinite proof is structural.

## originality

PASS

Automorphism invariance under graph complementation is elementary and homomorphism equivalences to complete graph are short; those facts by themselves are not claimed novel. Coleman arXiv:1812.01934 treats precisely countable homogeneous cluster and multipartite graph families and their homomorphism-homogeneity, but its relevant Props 5.8–5.9 do not tabulate these paired endomorphism rank spectra or contrast same oligomorphic Aut with finite versus infinite core. Bodirsky arXiv:cs/0612069 supplies general core existence/uniqueness and is necessary prior theorem, but does not state this paired-graph parameter-swap classification. Resultary semantic searches found no identical combined invariant statement; substantial folklore risk acknowledged.

## value

PASS

The precise negative example has a conceptual target: an identical permutation automorphism group and full orbit profile need not determine the finite versus countably infinite model-complete core, even for homogeneous graphs. Explicit image rank spectra give independently usable invariants for the classical cluster/multipartite family. Although its proof is short and uses a known general theorem, it clarifies a natural structural limitation rather than an unmotivated substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
