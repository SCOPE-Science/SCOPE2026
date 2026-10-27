# Review

## Correctness

**PASS.** The critical cut probability is exactly \(x^{-2}\). The range-two separator argument gives a strict exponent gap for every non-unit separator, leading to the block-tail asymptotic \(\Pr(Q_1>x)\sim\mu_Px^{-2}\). The centered block reward therefore has truncated second moment \(2\mu_P\log x\), and the normal-domain-of-attraction normalization reduces to \(\sqrt{n\log n}\). The pivot residual is tight and does not affect the limit.

## Originality

**PASS.** The closest recent result, Dey and Kim (arXiv:2607.28865), assumes identically distributed edge weights and states the Gaussian and stable passage-time limits on the strict sides of its critical exponent. Ahlberg (2015) also assumes identically distributed edge weights and finite second moment for the ordinary Gaussian passage-time theorem. Neither covers the length-dependent Pareto family on \(\gamma_1+2\gamma_2=2\). The proof here supplies the weighted-cut comparison required for that model rather than treating the common-law result as if it already applied.

## Value

**PASS.** The exponent balance is forced by the unique three-edge unit cut: one length-one edge and two length-two edges. The resulting boundary theorem identifies a natural critical fluctuation regime with a universal variance-one Gaussian limit under infinite-variance edge laws.

## Closest literature and limits

The result is restricted to the range-two line and independent Pareto laws with length-specific exponents on the stated critical curve. It does not establish a full phase diagram for other exponent pairs, other graph ranges, dependent weights, slowly varying corrections, or functional convergence. The closest sources are arXiv:2607.28865 and Ahlberg's 2015 regenerative FPP paper.

Self-review: passed. Independent audit: not yet performed.
