# Independent audit — Sumset growth from the first Kunz layer at prime multiplicity

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/17/prime-multiplicity-kunz-layer-sumset-growth--70739bc22a00`
**Audited tree:** `1d3113df55b1cdea0c8c69fa55235851289dc5fa`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

For r in hX, representing each zero summand by m and each first-layer residue a by m+a gives (h+t)m+r in S with 0<=t<=h-1, hence x_r<=2h-1 for r!=0. Repeated Cauchy–Davenport in Z/pZ yields |hX|>=min(p,h eta+1), giving the stated B_h. Substitution into the exact cumulative-layer identity produces the displayed |L| and Wilf bounds, and the monotonicity difference is (q-2k-2)(B_{k+1}-B_k). An independent shortest-path Apéry computation for the displayed multiplicity-29 semigroup reproduced all stated invariants and the new criterion.

### Independent checks

- Re-derived the carry bound t<=h-1 and the Apéry minimality step proving x_r<=2h-1.
- Re-derived repeated Cauchy–Davenport to B_h=min(p-1,h eta).
- Rechecked the cumulative-layer summation and the monotonicity increment.
- Independently computed Apéry data for <29,41,42,54,56,57>: c=218, q=8, rho=14, eta=5, Theta_1..Theta_6=(5,7,13,16,21,24), |L|=107, W=424, and B_1..B_3=(5,10,15).

## Originality

Yang–Zhang’s April 2026 preprint supplies first-layer staircase bounds, the cumulative-layer identity, and explicitly identifies interactions among exact low Kunz layers as a direction for refinement. It does not state the hX-to-Theta_{2h-1} containment or the prime-multiplicity Cauchy–Davenport criterion. Classical additive-combinatorial ingredients are not claimed as new. Fresh searches through 2026-09-29 located no matching propagation theorem.

### Literature checked

- https://www.preprints.org/manuscript/202604.0551 — Yang–Zhang, Wilf’s Conjecture from the First Kunz Layer; closest source, including cumulative-layer formulas and an explicit call to study interactions between layers.
- https://doi.org/10.1112/jlms/s1-10.37.30 — Davenport, classical residue-class addition theorem used as an ingredient.
- https://arxiv.org/abs/1710.03623 — Eliahou–Fromentin, prior additive-combinatorial Wilf context; no matching layer-propagation inequality.

## Scientific value

The theorem supplies a reusable mechanism coupling the first Kunz layer to all odd cumulative layers and converts it into explicit prime-multiplicity Wilf certificates. The multiplicity-29 example demonstrates strict reach beyond the two closest first-layer tests, so the result is more than a reformulation of known bounds.

## Limitations

- The explicit linear growth B_h is prime-multiplicity specific; composite multiplicities can have subgroup obstructions.
- The resulting Wilf inequalities are sufficient, not necessary, and do not resolve Wilf’s conjecture in full.
- For q<3 there is no admissible k in Theorem 2; the statement about the strongest member at H is naturally read only when the admissible family is nonempty.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
