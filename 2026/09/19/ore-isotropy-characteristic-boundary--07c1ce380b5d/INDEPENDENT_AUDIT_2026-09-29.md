# Independent Audit — 2026/09/19/ore-isotropy-characteristic-boundary--07c1ce380b5d

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `28f97d397bbd989b4435568132ee5e7398f7a619`
- Disposition: **PASSED**

## Correctness

**PASS** — The characteristic boundary is correct. In characteristic zero, the known arbitrary-field automorphism description of A_h and arbitrary-characteristic-zero LND classification supply the only structural inputs needed by the recent isotropy proof. After affine normalization of h, an automorphism has triangular part t↦t+r(x). If D(x) has positive t-degree m, comparison of the next coefficient in the commutation identity produces a nonzero factor m and bounds deg r; if D(x)=p(x)≠0, the relation forces D(t)=b(x)t+c(x) and commutation gives p r'-b r equal to a fixed-degree expression, which again bounds deg r because formal differentiation has its expected leading term in characteristic zero. Thus unbounded isotropy forces D(x)=0, and the centralizer of x is k[x], so D(t)=g(x) and D is locally nilpotent. Conversely every such triangular LND commutes with all t-translations. In characteristic p, on A_x the Euler derivation E(x)=x,E(t)=0 is locally finite but not LND, while translations by r(x) commute exactly when x r'(x)=0, hence for every r∈k[x^p]; degrees are unbounded. This gives the claimed counterexample in every positive characteristic.

## Originality

**PASS** — Baltazar-Lopes-Morales state their 2026 Ore-extension isotropy theorem over an algebraically closed characteristic-zero field. Benkart-Lopes-Ondrus already describe A_h automorphisms over arbitrary fields, and Kaygorodov-Lopes-Mashurov develop the characteristic-zero additive-group/LND theory and positive-characteristic iterative substitute. Those are prior ingredients, not the exact isotropy boundary. The audited result combines them to remove algebraic closedness and then supplies a concrete Frobenius Euler counterexample showing failure in every positive characteristic, even under local finiteness. Targeted searches found no earlier statement of this exact field-characteristic dichotomy.

## Scientific value

**PASS** — The theorem sharpens a new isotropy characterization to its exact field-theoretic boundary and explains the obstruction by the Frobenius kernel of x d/dx. The locally finite counterexample is especially informative because it shows that a natural regularity repair does not rescue the criterion in positive characteristic. The scope is intentionally limited to differential Ore extensions A_h.

## Sources

- A Characterization of Local Nilpotence for Derivations of Ore Extensions (Rene Baltazar; Samuel Lopes; Oscar Morales): https://arxiv.org/abs/2609.19470 — Primary 2026 isotropy theorem, stated over algebraically closed fields of characteristic zero.
- A Parametric Family of Subalgebras of the Weyl Algebra I. Structure and Automorphisms (Georgia Benkart; Samuel A. Lopes; Matthew Ondrus): https://arxiv.org/abs/1210.4631 — Exact automorphism description for A_h over arbitrary fields.
- Actions of the additive group Ga on certain noncommutative deformations of the plane (Ivan Kaygorodov; Samuel A. Lopes; Farukh Mashurov): https://doi.org/10.2478/cm-2021-0024 — Open-access characteristic-zero LND/Ga theory for A_h and prime-characteristic iterative-higher-derivation framework.
- Isomorphism Problems and Groups of Automorphisms for Ore Extensions K[x][y; f d/dx] (Prime Characteristic) (V. V. Bavula): https://doi.org/10.1007/s10468-024-10301-w — Positive-characteristic automorphism background.

## Limitations

- The theorem concerns differential Ore extensions A_h with nonconstant h, not the first Weyl algebra or all algebras in the motivating paper.
- It does not classify positive-characteristic isotropy groups generally or replace iterative higher derivations by ordinary LNDs.
- Because the motivating theorem is very recent and the field-hypothesis sharpening is short once older structure results are combined, near-simultaneous priority remains possible.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "char_zero_degree_arguments_checked": true,
  "positive_characteristic_Ax_counterexample_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive comparison remained unavailable, so Oxford Download was not required.
