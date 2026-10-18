# Scientific assessment

## Correctness — PASS

The exact conditional survival-difference formula gives \(r_k=p_kH_k\). The large-index expansion \(H_k=w_1+w_2p_k(1+o(1))\) is justified without any sample-size moment assumption by the uniform inequality \(nS_k^{n-1}\le3S_k^2\) for \(n\ge3\) and \(S_k\le1/2\). Since consecutive Poisson masses satisfy \(p_k/p_{k-1}\to0\), the ULC defect has the claimed positive first-order asymptotic. The endpoint proof uses a log-concave convolution and the 2023 fixed-sample preservation theorem. Reproducible exact-rational and high-precision numerical checks agree with the analytic derivation. Risks: the finite checks do not certify all indices; the analytical proof, rather than testing, bears that burden.

## Originality — PASS, with priority risk

The closest inspected paper, Badiella–del Castillo–Puig (2023), establishes ULC of order statistics for **fixed** sample size, including both pure endpoint laws. Its fixed-sample theorem is inapplicable to a random sample-size mixture; the current asymptotic proves that this closure extension is false. Watt's full mathematical argument treats expected order statistics as functions of deterministic sample size, not the ULC sequence inequality. Aravinda–Marsiglietti–Melbourne treats concentration for laws assumed ULC. Searches for randomized order statistics, equivalent Poisson-weighted curvature formulations, and stronger covering results identified no matching published result. A 2023 journal paper's repository PDF and an institutional retrieval route were unavailable, although its indexed mathematical theorem and proof were inspected; an earlier equivalent formulation remains possible.

## Value — PASS

The result identifies the exact smallest random-sample-size boundary of the fixed-size ULC preservation principle and shows a universal, quantifiable loss of shape for arbitrary higher-size contamination. The positive asymptotic coefficient depends on only two sample-size probabilities, and the loss persists for mixtures arbitrarily close to either deterministic endpoint. This distinguishes an intrinsic structural failure from a numerical anomaly in a single parameter example. Limitations: no assertion about random-size laws with \(w_1w_2=0\), ordinary log-concavity, or underdispersion.

Self-review: passed. Independent audit: not yet performed.
