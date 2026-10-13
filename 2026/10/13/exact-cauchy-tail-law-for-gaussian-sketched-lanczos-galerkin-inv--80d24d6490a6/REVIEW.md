# Scientific review — Gaussian-sketched Lanczos Galerkin inverse tails

## Correctness: PASS

The exact Lanczos residual relation reduces the sketched Galerkin matrix to a positive-definite tridiagonal matrix plus one random last-column update. The terminal reduced-solution coefficient is exactly \(c/(1+D)\), with \(c\ne0\) by the irreducible tridiagonal cofactor identity. Standard Gaussian block regression gives \(D\) a scaled Student-t law with precisely \(s-k+1\) degrees of freedom. Its density is positive at the pole, establishing the sharp \(1/R\) tail and divergence of all unconditional error moments of order at least one. At Krylov invariance the sketched approximation is exactly the true inverse action. The rational verification cases test the determinant and coefficient reductions; numerical integrations test the tail coefficient, not the infinite-dimensional quantifiers.

## Originality: PASS, with residual risk

Güttel–Liu–Nyman's 2026 sketched Arnoldi formula (11) supplies the algorithm and high-probability embedding context, but its inspected sections do not establish an unconditional inverse-moment dichotomy. Timsit–Grigori–Balabanov's 2023 result establishes conditional quasi-optimality and documents sporadic spikes, without the exact Student-t law or any universal infinite-moment conclusion. Palitta–Schweitzer–Simoncini's analysis compares sketched rank-one Krylov modifications and the effect of spurious Ritz values but does not give the present \(k\)-step Gaussian inverse-tail classification. Grigori–Kressner–Shao–Simunec describe a *different*, similarity-restoring method whose approximants agree with ordinary Arnoldi. An earlier one-direction Gaussian Ritz analysis contains the scalar denominator mechanism; the new claim is explicitly for every \(k\ge2\), including the exact degree-of-freedom shift \(s-k+1\), sharp coefficient, and invariant/nonsingular dichotomy. Classical Student-t regression supplies an ingredient, not by itself this Lanczos error result. Equivalent formulations in older unindexed literature remain possible; external independence or literature exhaustiveness is not established.

## Value: PASS

This theorem settles a natural stability question for the non-harmonic sketched FOM inverse: irrespective of finite oversampling, the unconditional expected norm error is undefined (infinite) unless the target Krylov subspace is invariant. The exact tail constant makes the rare-event probability quantitative, including for systems with condition number below three. The result distinguishes high-probability subspace-embedding guarantees from unconditional moment guarantees; those are mathematically different assertions. The result is not a prediction of typical observed error or of behavior under certified embeddings, safeguards, harmonic projection, or floating-point arithmetic.

## Closest references and scientific limitations

Güttel, Liu and Nyman, arXiv:2607.10354v1, Sections 2.2, 4–5; Timsit, Grigori and Balabanov, arXiv:2302.07466v3, Sections 3 and 5; Palitta, Schweitzer and Simoncini, doi:10.1002/nla.2596, Sections 2.3 and 5–7; Grigori, Kressner, Shao and Simunec, arXiv:2601.10248v1, Section 4. No statement is made about Gaussian-sketch variants conditioned on success, sparse-sign sketch distributions, numerical conditioning monitors, or multi-restart methods. The sharp scalar moment boundary does not automatically classify all subunit moments of the full vector error.

Self-review: passed. Independent audit: not yet performed.
