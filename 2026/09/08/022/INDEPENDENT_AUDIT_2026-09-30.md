# Independent audit — 2026-09-30

## Final claim
Inversion-refined census of the exceptional triple {1324,1243,1432}

## Correctness — PASS
A fresh independent max-insertion generator produced exactly 5,150, 21,517, 90,921 and 387,595 avoiders for n=8,9,10,11. Its inversion distributions reproduce every stated k=0..16 value, including av_8^6=15>11=av_9^6, av_10^8=26>22=av_11^8, monotone decrease for every k<=15, and the sharp k=16 row (405,422,350,299). The prepend-maximum and append-minimum maps have inversion shift +n and their avoidance proofs follow directly from the positions of rank 1 in the three forbidden patterns.

## Originality — PASS
Best-of-knowledge originality passes after comparing statements and implications, not merely titles.

### Equivalent formulations
Searches: Resultary semantic search for 1324 1243 1432 inversion distribution; Claesson et al. arXiv:2604.01143; Callan–Mansour arXiv:1705.00933
Evidence: Callan–Mansour identify the same exceptional triple at the univariate enumeration level. Claesson et al. study inversion refinements for pairs containing 1324, including {1324,1243}, but not the checked triple table.
Reasoning: The audit distinguished the triple from the broader pair class; pair inversion counts do not determine counts after additionally forbidding 1432.

### Broader coverage
Searches: Claesson et al. arXiv:2604.01143 section 5.3; Callan–Mansour arXiv:1705.00933; Resultary exact-topic search
Evidence: For the pair {1324,1243}, Claesson et al. prove eventual partition-number values and explicitly classify it as non-inversion-monotone; that does not imply the triple's finite n=8..11 bivariate distribution or its shift lemmas. Callan–Mansour's broader univariate treatment leaves this triple exceptional.
Reasoning: The prior pair theorem is structurally related but neither stronger nor sufficient to derive the triple-specific finite table.

### Exact database or table
Searches: Exact web search for 1324,1243,1432 inversion; Resultary exact-topic search; OEIS A257562 as cited univariate control
Evidence: No checked source supplies the same bivariate inversion table; OEIS is univariate only.
Reasoning: The exact refined table was not found independently; this is best-of-knowledge evidence, not a proof of novelty.

### Claim versus prior implication
Searches: Claesson et al. pair theorem; Callan–Mansour exceptional-triple classification
Evidence: The pair theorem gives p(k) only in a stable range for a larger avoidance class; adding 1432 changes the counts and can only decrease them, so the exact triple values are not implied. The Callan–Mansour univariate totals sum over inversions and cannot recover the refined cells.
Reasoning: Neither prior implication determines the final claim.

### Source inspections
- **Inversion monotonicity in subclasses of the 1324-avoiders** (arXiv:2604.01143): Shows relevant pair non-monotonicity and stable partition numbers, but does not cover the triple-specific census. Material read: Pair classification and section 5.3 on {1324,1243}, including Proposition 5.5 and row-difference discussion. Evidence: Section 5.3 labels {1324,1243} non-inversion-monotone and proves av_n^k=p(k) for n>=k+3.
- **Enumeration of small Wilf classes avoiding 1324 and two other 4-letter patterns** (arXiv:1705.00933): Motivates the object at univariate level; no inversion-refined table is supplied in the inspected material. Material read: Abstract and bibliographic record identifying the unique exceptional triple among triples containing 1324. Evidence: The abstract states that all but one such triple are enumerated and the exceptional triple is conjectured intractable.

Checked sources: Claesson et al., arXiv:2604.01143; Callan–Mansour, arXiv:1705.00933; OEIS A257562; Resultary published-record search
Residual risks: Best-of-knowledge originality may miss unpublished or unindexed refined tables. The antitone statement is intentionally confined to n=8..11 and k<=15.

## Scientific value — PASS
The object is the singled-out exceptional Callan–Mansour triple, and inversion monotonicity is an active refinement of the 1324-avoidance program. A complete small-window bivariate census, sharp failure boundary, and two structural shift injections are therefore motivated rather than arbitrary finite data.

## Limitations
- No general-n antitonicity theorem is claimed.
- Partition-number agreement remains empirical for the triple.

## Conclusion
The final claim passes correctness, originality, and scientific-value review on the evidence stated above.
