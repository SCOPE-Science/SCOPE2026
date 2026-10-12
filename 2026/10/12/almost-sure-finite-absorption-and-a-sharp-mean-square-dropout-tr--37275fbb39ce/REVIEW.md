# Self-review: Bernoulli error-feedback dropout

## Correctness — PASS

The binary compressor and error-feedback update give exact state maps for transmission and dropout. Two consecutive transmissions deterministically erase both the iterate and memory, proving finite-time absorption almost surely. First-success conditioning yields the exact renewal equation; strictly positive kernel coefficients at all indices from two onward prove the unique simple dominant pole, and evaluating its renewal generating function at one gives the sharp threshold \(p=2/3\). At equality a rational pole decomposition yields the limiting expected squared-error ratio \(2/5\). The degenerate boundary \(p=1\) is handled directly. Exact rational state enumeration in `verify.py` supports but is not substituted for the infinite proof.

## Originality — PASS (with priority risk)

The exact same identity-or-zero Bernoulli compressor appears in Stich and Karimireddy, arXiv:1909.05350, Section 5. Its small-step sufficient convergence bounds do not give the claimed unit-step exact necessary-and-sufficient mean-square boundary, the nonzero critical limit, or the coexistence of finite a.s. absorption and exponentially divergent expected squared error. The classical EF recurrence from Karimireddy et al., arXiv:1901.09847, and the preceding sparsification analysis by Stich et al., arXiv:1809.07599, have different assumptions and conclusions; EF21 uses a different correction state. Indexed search of matching formulations and stronger-coverage possibilities found adjacent but non-covering recurrences, not this entire statement. Residual risk: equivalent results may appear in unindexed specialized compressor or renewal-process work. Search absence is not a proof of global novelty.

## Value — PASS

Random whole-message loss is an important canonical communication-compression model. The exact stability boundary exposes a genuine distinction between almost-sure termination and expected-squared-error reliability. At the critical probability the expected squared error stays positive even while every trajectory reaches the optimum in finite time, so ordinary stochastic optimization stopping and risk guarantees need careful distinction. The finding is a mathematically complete scalar fixed-step classification, not a claim of broad algorithm superiority.

## Scientific limitations

Only noiseless scalar unit-curvature quadratics, classical zero-initial-memory error feedback, independent Bernoulli identity-or-zero compression, unit learning rate, and expected squared iterate at fixed attempted-update counts are covered. No higher-dimensional, stochastic-gradient, rescaled-compressor, or wall-clock statement is proved. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
