# Self-review

## Correctness
**PASS.** For a fixed firm count \(k\) and excess total \(r=N-k\), writing \(n_i=1+y_i\) makes HHI ranking depend exactly on \(\sum_i y_i^2\), while entropy ranking is the reverse ordering of \(\prod_i(1+y_i)^{1+y_i}\). Zero excess coordinates do not change either comparison, so a finite partition census through \(r=7\) proves the universal statement for every \(k\ge3\). Exact enumeration gives no strict reversal through \(r=6\) and a unique reversal at \(r=7\), namely \((3,4)\) versus \((1,1,5)\). The packaged verifier returns `VERIFY_OK`.

Risk: allowing zero-share firms or comparing different fixed firm counts changes the domain.

## Originality
**PASS.** Prior literature explicitly compares Herfindahl and entropy and therefore owns the fact that they are distinct concentration measures with different weighting properties. The accepted claim is not that they can differ in general; it is the sharp fixed-firm positive-integer boundary. Published-result searches, exact-profile searches, and concentration-literature searches did not locate the theorem that six excess units allow only tie splitting while seven are necessary and sufficient for strict reversal, with a unique first layer.

Risk: the finite reduction is elementary once posed, so an unindexed exercise, implementation test, or specialist note could contain an equivalent witness or boundary.

## Value
**PASS.** HHI and entropy are established summary concentration measures. A fixed-firm integer market is a natural setting when shares arise from indivisible customers, contracts, or capacity units. The excess-unit formulation isolates resolution from firm count and shows a universal threshold independent of \(k\): the first strict disagreement always occurs exactly seven units above the one-per-firm floor. The uniqueness of the first layer gives a compact diagnostic benchmark for concentration calculations.

Self-review: passed. Independent audit: not yet performed.
