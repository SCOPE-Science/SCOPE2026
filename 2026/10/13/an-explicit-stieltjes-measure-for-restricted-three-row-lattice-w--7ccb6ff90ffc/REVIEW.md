# Mathematical assessment: An explicit Stieltjes measure for restricted three-row lattice words

## Correctness — PASS

Shankar's verified input identities give \(B(z)=T(z)(T(z)-2)^2/(3-2T(z))\) with \(T=1+zT^3\). The present proof parametrizes the exact cut of this cubic branch, computes the imaginary part of its Stieltjes transform, and obtains an explicit positive density with exact Jacobian. Endpoint singularities are integrable, so a justified Cauchy contour gives every moment, not merely a finite sample. The polynomial controlling the density has a strict positive minimum \(68/27\) on the required interval. Generalized Vandermonde positivity then proves every Hankel minor is strictly positive. Symbolic computations verify critical algebra, and high-precision quadrature separately reproduces moments through order 14. No infinite conclusion is inferred from these finite checks.

## Originality — PASS, with disclosed literature risk

Shankar, *Avoiding patterns with three distinct letters in Canon permutations*, Theorems 6.2–6.3, proves the known counting formula and algebraic generating function, but Conjecture 9.5 expressly asks for Stieltjes positivity. OEIS A274969 records the same sequence under equivalent stack-word terminology. Borie–Falque's Proposition 1 gives a binary-tree enumeration, and Inagaki–Pramatarova's Proposition 5.6 gives a semisymmetric-height enumeration, without this positivity result. Górska–Penson proves a moment law for the distinct three-dimensional Catalan sequence. Bostan–Elvey Price–Guttmann–Maillard explain the general inversion technique and prove moment laws for distinct Catalan and Fuss-Catalan families; their statements do not certify the new sequence's density sign. Searches for the exact binomial formula, generating function, database ID, conjecture number, positivity and equivalent names did not reveal a covering theorem. Search incompleteness and disguised equivalent results remain possible; novelty is not a claim of exhaustive worldwide coverage.

## Value — PASS

The positive continuous probability law determines the entire natural restricted-lattice-word enumeration as moments on exactly \([0,27/4]\). This proves a mathematically motivated infinite part of an explicitly published two-sequence conjecture and upgrades finite observed Hankel positivity to strict positivity of arbitrary minors at every order. Neither a long list of numerical values nor the previously known cubic generating function supplies this structural conclusion.

## Scientific limitations

The result establishes the statement for \(B_k\) alone; it neither solves the \(Q_k\) half of Conjecture 9.5 nor the descent real-rootedness conjecture. Reproducibility includes a mathematical proof, exact algebraic checks and finite high-precision tests; there is no independent external audit. Potential equivalent unindexed prior work is a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
