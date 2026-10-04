# Same-model scientific review

## Correctness
**PASS.** The four-candidate profile domains for one, three, and five voters are exhausted. The full labeled verifier computes Schulze strongest paths by Floyd–Warshall and Ranked Pairs by explicit locking over every ordering within tied strength groups. An independent anonymous-profile verifier computes Schulze strengths by direct simple-path enumeration and Ranked Pairs using Tideman's ranking-elimination formulation. The two implementations reproduce the same \(51840\) divergences, the same one-sided containment, and the same two weighted-majority margin types.

Risk: the finite theorem stops at five voters and four candidates. The proof does not extrapolate to larger domains.

## Originality
**PASS.** Tideman's and Schulze's papers establish the two rules, and Parkes–Xia directly compare them and exhibit differing outcomes, so mere existence of disagreement is prior. The inspected literature and targeted searches did not state the sharp odd-voter threshold at four candidates, the \(51840/7962624=5/768\) census, the universal containment \(RP(P)\subsetneq S(P)\), or the two-margin-type classification.

Risk: failed search is not proof of bibliographic uniqueness. An unindexed election-software test suite, thesis appendix, teaching note, or unpublished computation could contain an equivalent finite enumeration.

## Value
**PASS.** Schulze and Ranked Pairs are two canonical Condorcet-consistent methods built from the same weighted majority information but aggregate it differently: strongest paths versus sequential locking. The smallest electorate where that distinction matters for four candidates is therefore a natural structural boundary. The exact first-layer census shows that the initial separation is highly constrained rather than generic: every disagreement has the same refinement direction and only two pairwise-margin geometries.

Same-model review: passed. Independent audit: not yet performed.
