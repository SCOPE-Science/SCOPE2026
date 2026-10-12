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

The proof has three structural steps.

1. The published Anti-Foundation component theorem supplies countably infinitely many connected components isomorphic to any chosen finite connected graph.
2. Frucht's theorem supplies a finite connected simple graph \(\Gamma_G\) with \(\operatorname{Aut}(\Gamma_G)\cong G\) for each finite group \(G\).
3. The automorphism group of countably many disjoint copies of a connected finite graph \(\Gamma\) is \(\operatorname{Aut}(\Gamma)^{\mathbb N}\rtimes S_\infty\). Fixing every vertex outside those components pointwise realizes this as a closed subgroup of the full graph automorphism group.

Run `python3 artifacts/verify.py`. The script exhaustively enumerates automorphisms for several disjoint unions of \(K_2\) and \(K_3\), verifies the finite formula \((q!)^k k!\), and checks explicit combined within-block and block-permuting automorphisms. It prints `VERIFY_OK 41814 exact assertions`.

The script does not prove the infinite Anti-Foundation or Frucht ingredients; those are cited mathematical theorems. Its role is to independently replay the only group-combinatorial assembly step introduced in the finding.
