# Scientific review

## Correctness — PASS
The proof has explicit domain, global-period normalization, four mutually exclusive residue classes, and a matrix lifting lemma for ternary valuations. The Cayley–Hamilton factorizations determine the first nonvanishing ternary layer, and direct residue counting proves all six multiplicity formulas. The resulting counts partition all \(3^{2e}\) parameter pairs. An exhaustive independent small-modulus enumeration in `verify.py` agrees for every pair at exponents \(e=1,2,3,4\). These finite checks only corroborate the infinite proof; they do not replace it.

## Originality — PASS, subject to residual priority risk
The closest directly matching primary text is Chen–Wong–Liao–Xiang (2014), Definition 1 and Section 5. It explicitly leaves \(3^e\), \(e>1\), as future work. Their 2012 prime-power abstract covers primes strictly greater than three; their 2013 sequel covers powers of two. The 2014 prime case does not imply depth-dependent multiplicities over \(3^e\). Nance (arXiv:1111.2984v1) only studies the fixed classical matrix. Bao–Yang (2012) supplies some individual-period formulae, but a complete \(3^e\) parameter census was not verified in its abstract; inaccessible full text leaves a specific priority risk. Targeted published-record and literature searches found no equivalent claim. No historical uniqueness is asserted.

## Mathematical value — PASS
The claim answers a specifically formulated open prime-power case in a well-studied finite dynamical family, not a private artificially sliced invariant. It supplies a closed-form classification for every exponent and a nonobvious scale-invariant proportion \(4/27\) of maximal-period shuffles. This matters directly to the distribution of finite-state periods and to distinguishing short-period parameter choices.

## Scope and unresolved checks
The theorem concerns global periods of the matrix family, not individual state orbit counts. One relevant earlier Springer article and the 2012 IEEE article were only available as abstracts; full-text historical priority therefore remains unconfirmed. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
