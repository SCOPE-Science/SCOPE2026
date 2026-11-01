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

The standalone program `verify_hex_fixed.py` was executed from the packaged candidate contents with Python 3. It passed 48 independently reconstructed orbit-compatibility-graph cases (all four symmetry subgroups and chain lengths \(1\leq n\leq12\)), verified all generators as actual graph automorphisms, and computed mod-two simplicial homology for every subgroup at \(1\leq n\leq7\). The test uses the original graph definitions, not a table of expected homology alone.

The infinite-family argument rests on the orbit-barycenter fixed-space lemma, the direct quotient-graph identification, the explicit neighborhood folding of even half-chains, the relative collapse of an apex cone over a collapsible link, and the published homotopy theorem for ordinary hexagon-chain independence complexes (arXiv:2512.21318v1, Theorem 3.1). Finite homology checks do not establish all-width integral homotopy. The proof provides the general justification; the executable verifier checks small boundary and parity cases.

Independent mathematical validation remains unperformed. Literature-index coverage cannot rule out equivalent unindexed work.
