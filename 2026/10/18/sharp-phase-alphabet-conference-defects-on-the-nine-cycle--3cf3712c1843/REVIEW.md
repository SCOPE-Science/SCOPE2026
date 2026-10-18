# Scientific assessment: nine-cycle phase-alphabet conference defect

## Correctness: PASS

The statement fixes all quantifiers: the four specified phase alphabets, the zero at the identity, the zero Fourier coefficient, and the unnormalized nine-point DFT. A global phase normalizes the first nonzero coordinate to one, leaving exactly seven free exponents. Minimal-polynomial reduction certifies the zero-mean constraint without tolerance, and the exact autocorrelation representation places every admissible defect in either the integers or \(\mathbb Z[\sqrt2]\). An integer comparison algorithm orders the latter without floating-point approximation. The standalone code iterates all \(q^7\) candidate exponent tuples for each prescribed \(q\) and recomputes the correlation defect, proving the minima and complete octary minimizer list by finite exhaustion. The printed counts of admitted normalized sequences are \(35,1225,9135,23765\); all asserted checks pass. A secondary direct trigonometric and Fourier evaluation confirms the normalization for one octary minimizer. The exhaustive proof is finite and makes no claim about unbounded alphabets.

## Originality: PASS (bounded best-knowledge comparison)

Fallon and Iverson, *Conference signals: Applications, existence, and constructions*, arXiv:2610.09169v1, Theorem 2.1 and Section 3, study exact flatness and continuous-phase numerical energy searches including the nine-cycle. They do not give the four sharp finite-alphabet correlation defects, the algebraic octary minimum, or its complete optimizer family. Their exact continuous-phase constructions have zero defect, but this value is generally unattainable for a restricted phase alphabet and does not imply the quantitative discrete optimum. Chee, Tan and Zhou, *Almost p-Ary Perfect Sequences* (2010), study exact existence and nonexistence of perfect or nearly perfect sequences; their prime-ary exactness conditions do not imply the least-squares minima for the four present alphabets. Distinct prior results on fourth moments of nine modes on a Cartesian square involve a different group and unrestricted zero-mean conditions. No coverage was identified in targeted published-record and literature comparisons. Historical priority remains a live residual risk because an unindexed earlier finite search cannot be ruled out.

## Value: PASS

A punctured finite cyclic signal is a natural discrete realization of a conference matrix. Requiring finite phase resolution is an operationally meaningful restriction; the squared autocorrelation defect is exactly the nonzero-frequency energy variance around perfect Fourier flatness. On the first nonprime odd square cyclic order, the theorem gives an exact arithmetic performance frontier for the natural two-, four-, six-, and eight-phase alphabets, quantifies the strict octary obstruction, and classifies every octary optimum. It is more than a trivial feasibility check or a sampled estimate, while making no claim of a general alphabet theorem.

## Scope and risks

This classification does not establish minima for other group orders or phase alphabets, nor over arbitrary complex phases. It relies on a self-contained finite exact certificate; it has not been independently audited. The possibility of a previously published but unindexed equivalent computation remains unresolved.

Self-review: passed. Independent audit: not yet performed.
