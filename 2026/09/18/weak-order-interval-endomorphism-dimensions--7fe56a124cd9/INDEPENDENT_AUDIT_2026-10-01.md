# Independent audit — 2026-10-01

## Final claim

For a finite weak order with level sizes n_1,...,n_h, the global dimension of its interval endomorphism algebra is the stated maximum of adjacent F(n_i,n_{i+1}) terms and nonadjacent n_i+n_j terms, with the stated two-level, uniform and extremal corollaries.

## Correctness — PASS

Assuming Aoki's published saturated-pair global-dimension formula, the specialization is correct. In a weak order every multi-level interval has arbitrary nonempty endpoint pieces and all intermediate levels full. For any saturated pair, Max(C\S) and Min(S\C) lie on the top and bottom endpoint levels, giving the endpoint-size upper bound. Nonadjacent full endpoints attain n_i+n_j. For adjacent levels, an exhaustive classification of connected relative downsets/upsets yields exactly the piecewise F(a,b), with explicit saturated witnesses in every case. A fresh independent enumeration of small profiles reproduced the formula with no mismatches. The uniform-level and universal-bound equality corollaries follow directly.

## Originality — PASS

Best-of-knowledge originality passes. Aoki gives the general saturated-pair formula and works out rectangular grids, but the weak-order closed optimization requires a new classification of adjacent and nonadjacent saturated configurations. The earlier extremal record covers only the equality-at-N-1 slice, not the full formula.

### Equivalent formulations

Searches: Aoki arXiv:2609.15927; weak order/ordinal sum of antichains/complete multipartite order plus interval endomorphism algebra; published semantic search

Evidence: Aoki's public abstract gives the general formula and a grid application; no weak-order closed form appears in the checked material.

Reasoning: Weak orders and complete multipartite orders are equivalent formulations of the same poset family.

### Broader coverage

Searches: Earlier extremal interval-endomorphism global-dimension record; Aoki grid theorem

Evidence: The earlier record classifies only the N-1 extremal cases; Aoki's explicit family is rectangular grids.

Reasoning: Neither broader result determines the full adjacent/nonadjacent maximum formula for arbitrary level profile.

### Exact database or table

Searches: Exact searches for F(a,b), two-level weak-order threshold, uniform 2r stabilization

Evidence: No independent table or formula was located.

Reasoning: This supports best-of-knowledge originality but is not used as sole evidence.

### Claim versus prior implication

Searches: Aoki saturated-pair theorem versus the record's weak-order optimization

Evidence: Aoki reduces the invariant to a maximum over saturated pairs; obtaining the record's formula requires a nontrivial family-specific classification and optimization.

Reasoning: The prior theorem is an input, not a mechanical parameter substitution.

### Source inspections

- **Interval endomorphism algebras of posets: Reedy structure, combinatorics, and homological theory** (arXiv:2609.15927v1): The accessible material confirms the general saturated-pair/global-dimension framework and grid application, but not a weak-order specialization. Material read: Abstract and bibliographic material; full PDF retrieval failed after open-access and authorized-access attempts. Evidence: The abstract states an exact combinatorial global-dimension formula and the explicit grid formula.

Checked sources: T. Aoki, Interval endomorphism algebras of posets: Reedy structure, combinatorics, and homological theory, arXiv:2609.15927v1; Asashiba--Escolar--Nakashima--Yoshiwaki on interval resolutions; Published-record semantic search including the earlier extremal-global-dimension classification

Residual risks: An equivalent weak-order computation could exist under different poset terminology; no such source was found.

## Scientific value — PASS

The theorem gives an exact field-independent homological dimension for every finite weak order, isolates two distinct extremal mechanisms, yields a complete height-two formula, and shows immediate stabilization for uniform weak orders. These are natural structural invariants of a classical poset family.

## Limitations

- Best-of-knowledge originality remains subject to differently named weak-order calculations.
- The Aoki full PDF was inaccessible in this run; the general saturated-pair framework was confirmed from primary metadata/abstract and the specialization was independently checked.

## Conclusion

The final claim passes correctness, originality and scientific value.
