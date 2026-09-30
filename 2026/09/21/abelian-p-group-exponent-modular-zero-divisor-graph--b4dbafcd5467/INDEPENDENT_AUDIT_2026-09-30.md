# Independent Audit — 2026/09/21/abelian-p-group-exponent-modular-zero-divisor-graph--b4dbafcd5467

- Audit date: 2026-09-30 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `0c26066873471e3e8f4cb61a1b62652a784f4b04`
- Disposition: **PASSED**

## Correctness

**PASS** — The minimum-degree formula is correct. In the modular commutative group algebra the augmentation ideal is the unique maximal ideal, and for e=exp(G)=p^a every x in the augmentation ideal satisfies x^e=0. Thus multiplication by x is nilpotent with Jordan blocks of size at most e and has kernel dimension at least N/e. Taking x=g-1 for an element g of order e realizes equality because left multiplication by g has N/e cycles. Converting annihilator size to graph degree yields q^(N/2)-2 when e=2; for e>2 the element g-1 has nonzero square and degree q^(N/e)-1, while any square-zero x has kernel dimension at least N/2>N/e and hence strictly larger degree. The graph-isomorphism corollaries correctly combine this formula with Aliniaeifard-Li's field/order/abelianness theorem and, over F_p, their rank theorem. Independent finite checks gave delta=0 for F_2 C_2 and delta=1 for F_2 C_4, matching the formula.

## Originality

**PASS** — Aliniaeifard and Li's 2014 paper was checked in public full text: it proves that the modular zero-divisor graph determines the field, group order, abelianness, and in the prime-field abelian p-group case the rank, but it does not state an exponent or minimum-degree formula. Targeted searches for an exponent-recovery or q^(N/e)-minimum-degree theorem did not locate a prior result. The proof uses standard modular group-algebra and nilpotent-operator facts, so an implicit older antecedent remains possible; the novelty claim is therefore limited to the sharp annihilator/minimum-degree formula and its exponent-recovery consequences.

## Scientific value

**PASS** — The result adds a new graph invariant of modular abelian p-group algebras, resolving the graph-isomorphism question for all rank-at-most-two abelian p-groups over the prime field and sharpening the structural information available from order and rank alone. The invariant is explicit and inexpensive to read from the graph, although it does not classify arbitrary higher-rank abelian p-groups.

## Sources

- **Zero-Divisor Graphs for Group Rings** — Farid Aliniaeifard; Yuanlin Li. https://doi.org/10.1080/00927872.2013.827689 — Public full text checked. Theorem 3.1 gives field/order/abelianness invariance; Theorem 3.4 gives rank invariance over the prime field.
- **On zero-divisor graphs of finite rings** — S. Akbari; A. Mohammadian. https://doi.org/10.1016/j.jalgebra.2007.02.051 — Earlier finite-ring zero-divisor-graph invariance results used by the 2014 group-ring paper.

## Limitations

- The exponent formula uses commutativity of KG and is not asserted for nonabelian p-groups.
- The rank-two group-isomorphism corollary is stated over the prime field because the cited rank theorem has that hypothesis.
- Order, rank, and exponent do not classify arbitrary finite abelian p-groups.
- The proof is short and elementary enough that an unindexed equivalent formulation remains a residual originality risk.

## Independent checks

```json
{
  "aliniaeifard_li_public_full_text_checked": true,
  "theorem_3_1_and_3_4_scope_checked": true,
  "frobenius_nilpotence_step_checked": true,
  "annihilator_jordan_bound_checked": true,
  "attaining_element_g_minus_1_checked": true,
  "small_group_algebra_checks": {
    "F2_C2_delta": 0,
    "F2_C4_delta": 1
  },
  "open_access_first": true,
  "oxford_used": false
}
```

GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. Open-access/preprint sources were checked before authorized institutional retrieval. Inaccessible material is explicitly identified and is not claimed read.
