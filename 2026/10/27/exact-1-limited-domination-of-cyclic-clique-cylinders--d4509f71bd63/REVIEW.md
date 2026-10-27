# Scientific review: exact 1-limited domination of cyclic clique cylinders

## Correctness — PASS

The theorem is \(\gamma_1^{\mathrm L}(C_n\square K_m)=m\gamma_t(C_n)\) for all integers \(n,m\ge3\). A clique fiber meeting a 1-limited set in any vertex must have at least \(m-1\) selected vertices. Write \(z,p,f\) for empty, exactly-one-missing and full fibers. The identity \(|D|=mn/2+(m/2)(f-z)+(m/2-1)p\) is exact. Empty-free families have size at least \((m-1)n\ge m\gamma_t(C_n)\); partial-free families project to a total dominating set of the cycle. In mixed families, the disjoint cyclic empty runs have length at most two, nonempty intervening runs have at least two full fibers, and a run containing a partial fiber has at least four full fibers. Hence \(f\ge z+2\) and \(|D|\ge mn/2+m\ge m\gamma_t(C_n)\). Lifting a minimum total dominating cycle set to all clique coordinates achieves equality. Boundary cases \(n=3,4,5,6\) are explicitly addressed by the cyclic constructions.

The standalone checker tests eight exhaustive labelled instances, 240 cyclic exact transfers, and 4424 constructive instances and returns `VERIFY_OK`. These checks cannot certify the unrestricted theorem; its proof is combinatorial.

## Originality — PASS, with limited bibliographic confidence

The foundational 2026 article states the total domination formula for a *single* cycle. Tepeh's Cartesian-product Theorem 7 yields the needed upper bound, but only a weaker \(mn/2\) lower bound in cycle classes \(n\not\equiv0\pmod4\). The exact subcase \(4\mid n\), and the \(K_3\square K_3\) corner, are already covered and are not separately claimed novel. Theorem 10 there handles Cartesian products of paths, not cyclic clique cylinders. The October cubic study is inapplicable when clique width \(m\ge3\), since product degree is \(m+1\ge4\). Semantic mathematical-record checks for clique cylinders, (1,m)-domination and (0,1)-pitchfork domination did not locate a stronger theorem. Records concerning the same \(C_n\square K_m\) graph refer to unrelated Rips invariants. See structured scientific comparisons in `AUDIT.json`.

Residual risk: unpublished or unindexed equivalent results might exist, and this review does not establish definitive priority.

## Value — PASS

The sharp four-periodic, two-parameter formula closes a documented Cartesian-product upper/lower gap for a natural infinite family, and the proof identifies a structural obstruction involving empty and nearly full clique fibers. The clique width-three onset is essential: the corresponding equality fails at width two. The theorem neither asserts a general product principle nor extends to other restriction parameters.

## Independent validation

Self-review: passed. Independent audit: not yet performed.
