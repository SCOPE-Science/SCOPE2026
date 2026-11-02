# Review: Sharp longest nondivisibility runs in Pascal rows modulo prime powers

## Correctness — PASS

The imported Kummer theorem equates the \(p\)-adic valuation of each binomial coefficient with a base-\(p\) subtraction borrow count. The proof first removes \(r=\nu_p(n+1)\) terminal maximal digits, repeating every reduced-row survival bit exactly \(p^r\) times. The reduced row has \(N=m-1\), \(Q=p^\alpha\), \(R=m\bmod Q\) and ends in digits \(R-1\). The initial \(R\) coefficients have fewer than \(\alpha\) borrows. In any longer block, the digitwise maximum of the block's first index modulo \(Q\) and the digits of \(R\) is a valid index in the block and produces at least \(\alpha\) borrows. This establishes both the upper bound and attainment for all quantified parameters. Exact-integer tests independently verified 8,320 parameter rows, 1,221,990 forbidden windows, and 667,809 explicit digit certificates. Tests are not substituted for the proof.

## Originality — PASS, with residual priority risk

Fine's 1947 result counts nonzero entries modulo a prime; Rowland's arXiv:1001.1783v1 (2010-01-12), Sections 1–3, generalizes counts to prime powers. Spiegelhofer and Wallner's arXiv:1604.07089v1 (2016-04-24) gives explicit generating functions for exact valuation **counts**. Their later arXiv:1710.10884v1 investigates typical distributions. Their inspected theorems do not give maximal consecutive runs or a constructive bad-index certificate for every longer interval. Kummer's pointwise theorem is used as an assumption; the new result is a sharp global optimisation of the borrow geometry. Exact counts alone do not imply a formula for consecutive ordering. A separately indexed study of arithmetic progressions in rows with odd coefficients has a different objective and does not imply contiguous run maxima for arbitrary prime powers. Search terms included longest zero-free Pascal block, consecutive nonzero binomial coefficients, prime-power row streaks and equivalent digitwise formulations. Unlocated classical work, especially Granville's 1997 prime-power survey not inspected in full, remains a historical priority risk. Search failure is not proof of novelty.

## Mathematical value — PASS

Maximum uninterrupted nondivisibility runs are natural exact invariants of Pascal-row modular patterns. Unlike the number of surviving entries, this extremal statistic controls the maximum length of an interval avoiding any coefficient divisible by a specified prime power. A uniform optimal digitwise covering certificate is mathematically stronger than tabulating small rows. The complete all-prime/all-exponent formula is a meaningful structural complement to the classical counting literature, with both edge blocks realizing sharpness.

## Limitations and closest literature

The theorem does not enumerate all individual maximal runs, evaluate coefficient units, handle general composite moduli without reduction, or extend to multinomial rows. The classical 1852 Kummer valuation theorem is an essential ingredient. Complete historical coverage is not claimed, and no independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
