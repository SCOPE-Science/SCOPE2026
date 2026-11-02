# Self-review

## Correctness — PASS

The scope is all integers \(n\ge2\), \(t\ge1\), \(\ell\ge1\), with complete allocation of four-item blocks under disjoint pair-complement valuations. In a non-whole block, the most possible completed useful pair count is one, establishing welfare at most \(t+h\) for \(h\) whole blocks. EF-\(\ell\) imposes \(n h\le t+(n-1)\ell\); EFX imposes the sharper \(nh\le t\) because a primed good in any whole block is irrelevant to the other agents' horizontal-pair value. Both bounds are attained by explicit allocations. A second construction is ordinary envy-free, establishing equality between the EF and EFX welfare optima. Exhaustive checker output covers \(1,722,355\) assignments across specified small sizes. No finite testing substitutes for the analytic proof.

## Originality — PASS (subject to publication-priority risk)

The natural object is the explicit infinite block family of Pyne–Viswanathan–Yang–Zick, Theorem 4.7. The full-text source gives asymptotic obstruction bounds for EF-\(\ell\) rather than finite optimum formulas or EF-versus-EF1 equality/separation. Direct comparison of assertions finds no implication of those exact equalities from its stated theorem. Targeted semantic research-record and literature searches found no identified dominating exact formula. The result is a finite-parameter refinement on a previously published construction rather than a wholly new allocation model. Closest source: arXiv:2610.15801v1 and its October 2026 full-text revision. Residual risk: an unindexed equivalent calculation or a short derivation in less-visible commentary remains possible.

## Value — PASS

The source introduces this family to bound the welfare attainable subject to relaxed envy criteria, but leaves its exact discrete price of fairness open in the published analysis. The exact answer for every market size, block count and deletion allowance supplies a precise calibration benchmark; in particular it reveals that strongest EF has **no additional optimal-welfare cost** relative to EFX in this construction, whereas EF1 can improve welfare by one indivisible unit, with a complete residue-class threshold. This is a motivated complete invariant for the source's canonical extremal family, not an arbitrary small numerical slice. Value is limited to the stated family and does not imply a stronger general welfare approximation.

## Scientific limitations

The sources did not certify publication priority; complete verification of all related unpublished work is impossible. This statement is not a general EF existence theorem for arbitrary binary SPOC preferences. The code exhausts small parameter values only; the arbitrary-parameter result rests on the explicit proof and upper bounds.

Self-review: passed. Independent audit: not yet performed.
