# Self-review

## Correctness (C) — PASS

For every nonnegative integer shift, the explicit binary carry-parity automaton returns the required output on every finite LSD-first input. The residual after an arbitrary prefix is proved, and distinct reachable states are separated using a self-contained proof of Thue–Morse non-ultimate-periodicity. Every reachable quotient-and-parity state is counted by an exact layer argument; the six universal low-quotient states and four exceptional shifts are treated explicitly. The dyadic minimum and maximum follow from sharp, realized layer contributions. Finite code checks corroborate the argument without being substituted for an infinite proof.

## Originality (O) — PASS, with residual priority risk

The strongest directly relevant earlier result is Zantema and Bosma, *Complexity of automatic sequences* (2022), Section 7, which computes the one-step LSD-first Thue–Morse tail complexity as three states and proves general operation bounds, but does not imply the all-shift formula or the sharp dyadic extremizer sets. Moradi, Rampersad and Shallit (arXiv:2512.10017) give general LSD-first bounds and explicit **MSD-first** Thue–Morse shift results, not this exact LSD-first classification. Moradi et al. (arXiv:2603.18858) give exact LSD-first complexity for the **Fibonacci word in Zeckendorf representation**, a distinct sequence and numeration system. Charlier et al. (arXiv:1910.08543) address \(m\mathcal T+r\) with \(0\le r<m\), not the arbitrary translate \(t(n+c)\). OEIS A382296 is explicitly **MSD-first**. Targeted published-record and literature queries did not identify the present result; unindexed earlier computations remain a genuine risk.

## Value (V) — PASS

The object is the natural full-shift state-complexity function of the archetypal automatic sequence, not an ad hoc finite slice. The proof gives a complete exact answer for all shift parameters, a minimal automaton and exact \(2\)-kernel cardinalities, plus a sharp oscillatory dyadic envelope: one unique easiest shift versus \(2^{k-3}\) maximizers in every large dyadic block. These phenomena refine general logarithmic size bounds and make the memory cost of shifting an automatic sequence quantitatively explicit.

## Verification boundaries

The verifier evaluates 4,096 state counts and minimizations, 98,208 direct input words, 4,088 dyadic extremizer instances, and 300 additional large shifts. These finite checks are not exhaustive for all shifts, and publication priority and mathematical validation by others remain open.

Self-review: passed. Independent audit: not yet performed.
