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

The standalone script `verify_coprime_artinian.py` implements finite commutative \(\mathbb F_2\)-algebras with explicit multiplication tables, lists every additive subspace, selects the ideals, and computes annihilators from multiplication. A nonzero ideal \(C\) is admitted exactly when for every pair of ideals \(I,J\), containment \(C\operatorname{Ann}(I)\subseteq J\) implies \(C\subseteq I\) or \(C\subseteq J\). This is the **defining condition**, so the checker does not assume the theorem in its coprimality test.

The program also computes each local socle by annihilating the maximal ideal, classifies mixed direct-product ideals coordinatewise, and checks that every subset of the computed spectrum is realized as a closed coprime hull. It covers 17 finite examples, including fields, local chain rings, square-zero non-Gorenstein rings, a two-generator Artinian complete intersection, and products of two or three factors.

Run `python verify_coprime_artinian.py`. Expected final output: `VERIFY_OK 17 Artinian examples, all ideals tested`. The direct exhaustive computation is confined to these Artinian examples, and is not a proof of the universal Noetherian claim. That claim is established in RESULT.md by the local Nakayama argument, Krull intersection (Stacks Project Tag 00IP), and clopen-idempotent decomposition. No external or independent audit has been performed.
