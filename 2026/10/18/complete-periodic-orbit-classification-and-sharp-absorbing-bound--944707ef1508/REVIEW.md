# Scientific review

**Correctness — PASS.** Euler's product formula and the least-prime-factor argument prove \(m-\varphi(m)\ge\sqrt m\) for every composite positive integer \(m\). For all \(n\ge26\), either one composite step decreases \(n\), or a prime step followed by a composite or twin-prime branch decreases \(n\) in at most three iterations. Strong induction gives entry into the explicitly checked invariant interval \(1\) through \(25\); its complete map table proves there are exactly three cycles. The packaged independent exact-integer verifier reproduces all small transitions, tests the reduction cases, and checks one million starting values. The infinite conclusion rests on the inequalities, not on finite testing.

**Originality — PASS within checked material.** Leonetti–Luca prove eventual periodicity for all shifts, but not the complete periodic orbit spectrum or the start-independent sharp endpoint \(25\) at shift \(3\). The closest public period-size result exhibits the \(23\leftrightarrow25\) cycle and bounds the maximum in terms of an arbitrary period \(T\); it cannot exclude longer periods or establish a universal absorbing interval. The Danh et al. improvement concerns the second-order recurrence. Targeted searches for the map, its cycles, the cototient form, and global absorption did not locate an equivalent statement. An unindexed duplicate remains a residual risk.

**Value — PASS.** Complete periodic classifications are fundamental invariants of arithmetic dynamics. This exact classification of a nonmonotone shifted-totient map determines the coexistence of three different least periods, gives a uniform transient-to-cycle reduction from every positive integer, and identifies an optimal universal absorbing endpoint, sharpening a qualitative eventual-periodicity theorem rather than enumerating arbitrary finite examples.

The result applies only to the shift \(3\). It does not solve other shifts or give closed-form global basin membership. The independent integer tests are finite, and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
