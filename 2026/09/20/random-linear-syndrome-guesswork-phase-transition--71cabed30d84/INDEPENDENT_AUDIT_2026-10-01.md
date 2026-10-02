# Independent audit — 2026-10-01

## Record

**Random linear syndromes attain the all-rate Renyi guesswork exponent**

Final claim: For every fixed finite field size \(q\) and \(\rho>0\), a uniform random linear syndrome map gives a source-independent finite constant-factor law \(\mathbb E_H[G_H(x)^\rho]\asymp_{q,\rho}(1+q^{-m}(G_0(x)-1))^\rho\); consequently, for arbitrary source sequences with a Rényi-entropy rate, random linear maps attain the all-encoder exponent \(\rho[h_{1/(1+\rho)}-r]_+\), with the same exponent for a typical matrix.

Disposition: **PASSED**

## Correctness — PASS

Fresh reconstruction verifies the collision-count representation, rank-of-span tuple bound for all integer moments, the second-moment/Paley–Zygmund lower bound for \(0<\rho<1\), the full-row-rank kernel containment probabilities, and the Arıkan cellwise converse. The endpoint where the kernel is trivial is harmless because the proxy remains bounded while the constrained rank is one. These arguments prove the finite law and the positive-part exponent without relying on the package's saved finite enumeration.

## Originality — PASS

Tavakoli's 2026 preprint proves the IID random-linear coset exponent only under the explicit subcritical condition \(h_b(\delta^*)>1-R\) and \(h_b(p)>1-R\), and extends it to q-ary IID sources through a weight-spectrum theorem. It does not imply the audited pointwise source-independent finite moment comparison, nor the arbitrary-source-sequence all-rate positive-part theorem. Classical guessing/task-encoding results provide the entropy converse but not structured linear-map achievability in this finite form.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Source inspections distinguish material actually read from inaccessible full text.

## Scientific value — PASS

The finite moment law explains linear hashing at source-word level, removes IID and weight-spectrum hypotheses, closes the low-rate regime where the existing coset theorem's exponent formula cannot remain negative, and shows structured linear syndromes match arbitrary encoders at exponential scale. That is a motivated strengthening rather than a parameter substitution.

## Checked scientific sources

- Hasan Tavakoli, Guesswork Under Linear Constraints: Exact Exponent for Coset Decoding, arXiv:2607.00205 (2026).
- E. Arıkan, An Inequality on Guessing and Its Application to Sequential Decoding, IEEE Trans. Inf. Theory 42 (1996), DOI:10.1109/18.481781.
- C. Bunte and A. Lapidoth, Encoding Tasks and Rényi Entropy, IEEE Trans. Inf. Theory 60 (2014), arXiv:1401.6338.
- Resultary semantic search for random linear syndrome guesswork, Rényi exponent, positive-part transitions, and constant-factor moment laws.

## Residual risks

- Older universal-hashing or task-encoding literature could contain an equivalent finite pointwise moment comparison under different terminology; no such implication was located in the searched sources.

## Verification boundary

The audit reconstructed the mathematical argument from the record and performed fresh logical or algebraic checks where needed. Existing package logs were treated only as reproducibility evidence. No formal proof-assistant verification or expert attestation is asserted.
