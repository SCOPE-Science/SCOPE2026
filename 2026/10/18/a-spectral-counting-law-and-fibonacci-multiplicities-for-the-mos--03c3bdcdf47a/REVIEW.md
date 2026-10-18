# Self-review

## Correctness — PASS

The base-\(4\) digit transition matrices follow from exhaustive enumeration of the four allowed input digit pairs. The two surviving carry-support types are complete; their transition matrix proves the exact support count for all \(k\ge0\). An induction bounds both carry-vector coordinates by consecutive Fibonacci numbers, and explicit digit words attain the bound. Positive-summand and terminal-carry arguments ensure the recurrence counts exactly the stated finite sumset. Exact brute-force and carry-state regression tests support, rather than replace, these infinite proofs.

## Originality — PASS, with stated residual risk

Moser (1962, pp. 37–38) proves unique representation with the coefficient \(2\); his existence theorem for separately tailored complementary sets does not imply the same original set has the coefficient-\(3\) count or Fibonacci extremum. De Bruijn (1964, pp. 537–546) treats signed, direct decompositions for other coefficients. OEIS A000695 records the underlying digit set and OEIS A126684 a different sumset. OEIS A007052 **already records the sequence and recurrence** \(1,3,10,34,\ldots\), so those numerical data are not independently novel. The literature comparisons did not identify the precise arithmetic interpretation *together with* the extremal representation-multiplicity theorem; a previously unindexed derivation remains possible. The Eigen–Ito–Prasad paper was available only through abstracts.

## Mathematical value — PASS

The coefficient-\(3\) change is the nearest natural nontrivial perturbation of Moser's coefficient-\(2\) complementing identity. The result simultaneously gives an exact support census, a sharp representation-multiplicity classification, and distinct support and multiplicity exponents. This provides a complete structural description of two natural additive invariants of a classical digital number-theoretic set, not merely a recomputation of a known sequence table.

## Scope and remaining limitations

No claim about arbitrary multipliers, a pointwise limiting distribution of multiplicities, or independence of validation is made. A publication prior to the consulted material may contain an unrecognized equivalent formula, particularly among digit-recursion literature. The earliest historical print antecedents have only year/issue-level public-date evidence here; the selected source date is the explicitly day-stamped OEIS comment of 2001-02-07, not an invented day for the 1962 printed paper.

Self-review: passed. Independent audit: not yet performed.
