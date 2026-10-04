# Same-model review

## Correctness

PASS. A multinomial count and a hypergeometric count correspond to different finite-population sampling mechanisms. Conditioning on the multivariate hypergeometric contact counts gives the exact two-infectious-class formula. In the one-infective case it reduces to
\[
\beta_{\mathrm{HG}}=\frac{Nq_I}{M},
\]
whereas the published power formula is
\[
\beta_{\mathrm{src}}
=
1-\left(1-\frac{q_I}{M}\right)^N.
\]
The strict difference for \(N>1\) follows from Bernoulli's inequality. The bundled checker independently enumerates the finite contact subsets and reproduces the saturation witness.

## Originality

PASS. The general distinction between finite-population hypergeometric sampling and a binomial approximation is prior knowledge and is explicitly present in the source's predecessor literature. The accepted contribution is restricted to the 2020 model: it combines the multinomial contagion law with an exact hypergeometric contact-count assertion, and the exact two-infectious-class correction exposes a saturation failure. Exact source, correction, replacement-sampling, and alias searches found no published repair of this DOI.

## Value

PASS. The contagion probability is the transition law used to simulate the individual-based finite population, while the hypergeometric statement is used in the reproduction-number discussion. A coherent model must choose one contact mechanism. The correction is especially relevant when the accessible contact pool is not large relative to the daily contact count, while explicitly preserving the paper's first-order large-population approximation.

## Closest literature and limitations

Tuckwell and Williams, DOI 10.1016/j.mbs.2006.09.018, explicitly introduce the binomial contact law as a large-population approximation. Ferrante, Ferraris, and Rovira, DOI 10.1007/s11749-015-0465-z, describe contacts with different individuals and again qualify the binomial transition law as approximate. These sources cover the general sampling distinction but do not state the later COVID model's simultaneous-law inconsistency or its exact two-class correction.

The result does not claim that the source's large-population numerical tables change materially. If repeated contacts are the intended exact mechanism, the multinomial formula can remain and the hypergeometric assertion must instead become binomial.

Same-model review: passed. Independent audit: not yet performed.
