# Independent Audit — 2026/09/20/finite-abelian-k0-cotorsion-obstructions--7ad39a71543a

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `061a844dd2f5bc07cc4e861c58c7f20af7c935f0`
- Disposition: **PASSED**

## Correctness

**PASS** — The finite-index K_0 construction is internally consistent. Euler class is additive on degreewise split conflations, so A_Lambda is extension closed; if Y=X⊕Z with X,Y in A_Lambda then epsilon(Z) is again in Lambda, proving weak idempotent completeness. Standard cone sequences remain inside the subcategory and make the contractible complexes exactly the projective-injectives. If e is the exponent of G=K_0/Lambda, every X is a summand of X^⊕e in A_Lambda, proving that the idempotent completion is the ambient bounded-complex category, while a simple class outside Lambda supplies a nonsplitting idempotent. Semisimplicity gives the displayed Ext^1 cohomology formula. Maps killing H^{>=1} factor, modulo a contractible null-homotopic part, through e copies of H^{<=0}; the dual statement gives the second object ideal. The explicit e-fold cone constructions supply complete ideal approximations. At object level a special F-precover exists exactly when the truncated Euler class alpha vanishes, and dually for beta; direct sums multiply those classes, so the least stabilizing multiplicity is exactly their order in G. The final realization A=L⊕L[-3] has total Euler class zero and realizes any prescribed quotient class.

## Originality

**PASS** — Ren-Wang's September 2026 preprint gives precisely the parity case: bounded finite-dimensional complexes with even total cohomology dimension, explicit doubled ideal approximations and parity obstruction to object approximations. The earlier Wang-Wang-Zhu example is intrinsically non-weakly-idempotent-complete, while Sun-Tan-Wang-Zhu provide general positive ideal-approximation theory in Frobenius categories. Targeted searches did not locate the finite-index K_0 quotient construction, G-valued truncated Euler obstruction, or exact element-order stabilization law. The audited claim is appropriately scoped as a finite-abelian generalization of a very recent parity mechanism, not a new theory of ideal cotorsion pairs.

## Scientific value

**PASS** — The result identifies the parity obstruction as one instance of a complete finite-abelian K_0 mechanism and realizes every finite abelian group, including exact element orders, as an approximation defect. That is a meaningful structural classification of the newly discovered phenomenon, even though the semisimple construction is deliberately elementary.

## Sources

- **A parity obstruction to completeness of object cotorsion pairs** — Junpeng Ren; Yucheng Wang. https://arxiv.org/abs/2609.18681 — Primary 2026 parity example generalized by the audited record.
- **A Counterexample to the Open Question on Object Ideals** — Qikai Wang; Yuxiao Wang; Haiyan Zhu. https://arxiv.org/abs/2609.14382 — Earlier counterexample whose construction is intrinsically non-weakly-idempotent-complete.
- **Ideal approximation theory in Frobenius categories** — Dandan Sun; Zhongsheng Tan; Qikai Wang; Haiyan Zhu. https://arxiv.org/abs/2502.11146 — General Frobenius ideal-approximation background and positive completeness criteria.

## Limitations

- The theorem is a narrow generalization of a very recent parity construction and is elementary once the finite-index K_0 viewpoint is identified.
- It is proved for bounded complexes over a finite-dimensional semisimple algebra, not arbitrary Frobenius exact categories.
- Near-simultaneous follow-up work to the September 2026 parity preprint remains a material priority risk.
- The result classifies the obstruction within this model family rather than every possible obstruction to object-level completeness descent.

## Independent checks

```json
{
  "frobenius_and_idempotent_completion_argument_checked": true,
  "object_ideal_factorizations_checked": true,
  "ideal_approximation_cone_sequences_checked": true,
  "alpha_beta_criteria_checked": true,
  "stabilization_order_and_realization_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access/preprint sources were checked before institutional retrieval, and inaccessible material is explicitly identified rather than inferred.
