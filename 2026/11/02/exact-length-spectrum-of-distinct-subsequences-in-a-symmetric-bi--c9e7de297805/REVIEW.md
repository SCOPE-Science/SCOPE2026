# Scientific review

## Correctness — PASS
The deterministic append-bit update exactly characterizes weighted **distinct** subsequence strings ending in each letter (it does not count duplicate embeddings). Conditioning on the last Markov bit and using bit-complement symmetry gives the exact two-state affine recursion in the proof, with correct length-marking factor. The matrix resolvent yields the rational bivariate generating function coefficientwise. At length one and two it gives \(t\) and \((1+r)t+t^2\). Primitive Perron–Frobenius growth applies to the positive-switch regime; the zero-switch endpoint is handled separately. The independent packaged exact-rational enumerator checked every binary host to length ten at five parameters, totalling 10,230 hosts and 275 length coefficients. Limits: the finite checks alone do not prove the identity, and no concentration or nonstationary result is claimed.

## Originality — PASS, with residual risk
The closest direct source, Biers-Ariel–Godbole–Kelley (arXiv:1704.08661, Section 3.2), establishes a four-state matrix for **unrefined** expected total distinct-subsequence counts in an asymmetric Markov source and expressly does not provide a scalar closed form. It does not state the exact expectation at each subsequence length or the symmetric-chain two-variable rational generating function. Collins (arXiv:1310.7288) treats independent bits; Flaxman–Harrow–Sorkin (2004) treats deterministic extremal words. Neither implies the length-refined Markov law. Exact targeted database, accessible historical, and literature searches did not identify an equivalent result. Risk: a later paper could contain an equivalent marked transfer-matrix calculation not found here. This finding is not claimed as an independent peer certification.

## Value — PASS
The target is a standard subsequence-complexity statistic, now resolved jointly by host length, scattered-subsequence length, and temporal correlation, rather than only its unrefined expectation. The identity gives exact \(\mathbb E[D_{n,k}]\) for every \(n,k,r\), an order-three recurrence in host length, and an explicit strictly increasing growth-rate interpolation between three canonical regimes. This is a natural correlation-resolved enumerative invariant; it is not an arbitrary finite table or a routine restatement of an already length-marked result.

## Closest literature and limitations
The source comparison is to the Markov total-count matrix in the 2018 paper and to the earlier i.i.d. and deterministic endpoints. The claimed extension is length refinement plus its all-parameter exact solution, not a correction of prior research. A hidden equivalent source remains a risk, as does any use of the formula beyond symmetric stationary two-state sources. The verifier tests finitely many \(r\) and host lengths; the proof supplies the infinite quantifiers.

Self-review: passed. Independent audit: not yet performed.
