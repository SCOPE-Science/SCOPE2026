# Independent mathematical audit — The exponent of an abelian p-group from its modular zero-divisor graph

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** In the commutative modular group algebra, every augmentation-zero element \(x\) satisfies \(x^e=0\) for \(e=\exp(G)\) by Frobenius. Hence multiplication by \(x\) has nilpotent Jordan blocks of size at most \(e\), so its kernel has dimension at least \(N/e\). Equality is attained by \(g-1\) for an element \(g\) of order \(e\), because left translation by \(g\) has exactly \(N/e\) cycles. The graph degree differs from annihilator size by one or two according as \(x^2\ne0\) or \(x^2=0\), yielding the two stated minimum-degree branches. Independent direct enumeration over \(\mathbf F_2\) for \(C_2,C_4,C_2\times C_2,C_8\) reproduced the formula. The graph-isomorphism consequences then follow from the published field/order/abelianness/rank invariants.

Checked sources: Assigned RESULT.md; Aliniaeifard--Li 2014 full author copy; Independent small-group-algebra enumeration.

Residual correctness risks: The small-group enumeration is only corroborative; the proof is the Jordan-block argument.; The rank-two corollary uses the prior rank-determination theorem over the prime field exactly as stated..

## Originality

**PASS.** The inspected 2014 primary paper proves that the modular zero-divisor graph determines field/order information and, over the prime field, rank of a finite abelian \(p\)-group, but it does not state an exponent invariant or the minimum-degree formula. Targeted published-result and web searches did not locate a prior exponent recovery theorem for the ordinary modular zero-divisor graph.

### Equivalent formulations

Searches/sources: Resultary semantic search: modular zero-divisor graph abelian p-group exponent minimum degree; Aliniaeifard--Li 2014 DOI 10.1080/00927872.2013.827689; search for annihilator-size/minimum-degree formulations.

Evidence: The exact published-result hit was the audited theorem. Aliniaeifard--Li's abstract and full theorem section identify rank and cardinality, not exponent. Later annihilator-graph papers located concern different graph constructions.

No equivalent formulation recovering \(\exp(G)\) from ordinary graph minimum degree was found.

### Broader coverage

Searches/sources: Aliniaeifard--Li 2014 isomorphism theorems; Akbari--Mohammadian finite-ring zero-divisor graph results; later annihilator graph/group-ring searches.

Evidence: The 2014 paper is broader in general group-ring graph structure but its modular abelian invariant list stops short of exponent. General finite-ring graph theorems inspected do not specialize to the exact annihilator minimum derived here.

No inspected broader theorem mathematically dominates the stated exponent formula.

### Exact database or table

Searches/sources: Resultary exact/semantic theorem search; web search for the exact minimum-degree expressions.

Evidence: No earlier exact record or database formula was located.

This is a structural theorem, not a tabulated finite invariant; theorem-level exact search is the applicable check.

### Claim versus prior implication

Searches/sources: Can order and rank determine exponent for arbitrary abelian p-groups?; Can the 2014 graph invariants imply the rank-two conclusion without a new exponent invariant?.

Evidence: Order and rank do not determine exponent in general rank at least three. For rank two, order plus the newly recovered exponent determines the two cyclic exponents. The minimum-degree argument is needed to add exponent to the prior invariant list.

The main theorem is not mechanically implied by the previously known order/rank information.

### Source inspections

- **Zero-Divisor Graphs for Group Rings** — PRIMARY_NOT_COVERING.
  Identifier: https://doi.org/10.1080/00927872.2013.827689
  Trigger: Direct predecessor on modular group-ring graph isomorphism invariants.
  Material read: Full public author copy, including the modular isomorphism theorems identifying field/order/abelianness and the prime-field rank invariant.
  Method: lawful public author full text
  Evidence: The source gives rank and cardinality results but no exponent formula or minimum-degree computation.
- **Annihilator graphs derived from group rings** — DIFFERENT_GRAPH.
  Identifier: https://doi.org/10.56947/gjom.v15i2.1602
  Trigger: Later paper with potentially confusable annihilator terminology.
  Material read: Accessible article metadata/abstract and graph definition.
  Method: lawful public material
  Evidence: It concerns annihilator graphs, not the ordinary zero-divisor graph used in the audited theorem.

Residual originality risks:
- Because the proof is short and elementary once the augmentation ideal is used, an implicit observation in poorly indexed group-ring literature remains possible.

## Scientific value

**PASS.** Exponent is a natural missing invariant in the modular group-ring graph isomorphism problem. The exact minimum-degree formula recovers it from a single elementary graph statistic and, combined with the known rank invariant, settles the isomorphism question for every two-generated finite abelian \(p\)-group over the prime field.

Residual value risks: Order, rank and exponent do not classify arbitrary higher-rank abelian \(p\)-groups, so the general isomorphism problem remains open..

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
