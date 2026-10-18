# Independent mathematical audit

## correctness

PASS

Reconstructed greedy complete-alphabet arch criterion, not assuming alphabet shrinks on short prefixes. A base-b aligned block B_j of t_b(bj+u) equals a_j+u mod (b+1), u=0..b-1, so exactly one symbol a_j-1 is missing. Digit carry identity a_q-a_(q-1)≡1+2ν_b(q) mod b+1 holds also for composite base b. For even b each pair (B_(2i),B_(2i+1)) completes an arch only at its final letter. For odd b, the unique missing letter appears in the second block at even offset d_b(q)=−2(ν_b(q)+1) mod(b+1), q=2i+1. The remaining suffix together with following even-index block still misses a_q when ν_b(q)>0, preserving induction; ν=0 gives terminal offset b-1. Thus every prefix N=bq+r obeys the claimed odd/even exact U_b(N) and arch positions. Radial density U_b(N)/N→1/(2b) and the asserted bounded discrepancy follow. Independent direct greedy scan for 20,000 prefix/base pairs (bases 2..21, 0≤N<1000) matched formulas, but proof is the all-base digit-carry induction.

## originality

PASS

Known greedy arch characterization of subsequence universality and generalized Thue–Morse binomial complexity are correctly credited. Their algorithms/invariants do not print or imply without added carry analysis this digit-sum family’s all-base all-prefix formula. Published Resultary binary word distribution and universal insertion-radius results describe different ambient alphabet/model; no direct covering theorem identified. Possible unindexed automatic-word formulas remain an explicit risk.

## value

PASS

An exact all-prefix scattered-subsequence universality law for a natural automatic digit-sum word, across all integer bases including composite, is a meaningful enumerative invariant. The parity split and trailing-zero-dependent early arches are nonobvious structural features unavailable from generic arch-count algorithms without number-theoretic block reasoning; exact arch boundaries enable later combinatorial analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
