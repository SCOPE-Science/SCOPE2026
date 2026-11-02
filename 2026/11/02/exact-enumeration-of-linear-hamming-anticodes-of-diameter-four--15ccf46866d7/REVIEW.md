# Scientific review: Exact enumeration of linear Hamming anticodes of diameter four

## Correctness (C): PASS

For each prime power \(q\), the code is a linear subspace of \(\mathbb F_q^n\), and its diameter is the largest codeword Hamming weight. For every positive-dimensional code of full support \(s\), double-counting nonzero coordinates gives \(s(q-1)q^{k-1}\le4(q^k-1)\), hence the strict upper bound \(s<4q/(q-1)\). This reduces the all-length assertion to finite supports seven, five and four in the three field-size regimes. On supports at most four all subspaces qualify and inclusion-exclusion gives the displayed closed coefficients. On remaining supports, the supplied checker enumerates every unique reduced-row-echelon subspace, every corresponding codeword, and all supports; it verifies completeness against Gaussian-binomial subspace counts and checks the decomposition against a direct ambient census. The strict cutoff closes the infinite quantifier. A separate second-moment argument determines the unique length-seven binary simplex type and its thirty labeled realizations. The field arithmetic and finite counts were reproduced using the embedded program's actual package source and output. No numerical extrapolation is used.

## Originality (O): PASS, with residual priority risk

Horlemann and Ravi, arXiv:2610.31618v1 (October 22, 2026), Proposition 4.3 and Theorem 4.6, provide the fixed-diameter support decomposition and only an *unspecified* growth degree \(\sigma_q(d)\). Their general statements do not themselves evaluate the complete coefficients or the exact field-dependent \(\sigma_q(4)\) values. Ravagnani (2016) classifies optimal-dimension anticodes, not all maximum-weight-bounded subspaces, while Di Giusto–Gorla–Ravagnani (2025) address generalized weights. The binary simplex code is long established, so only the full support enumeration and complete polynomial across every field and length are presented as new. Primary literature, exact-title and equivalent-term searches, research-record searches and accessible prior claims revealed no direct coverage. The residual risks are an unindexed older enumeration or a source inaccessible in the inspected set; lack of hits is not treated as a proof of uniqueness.

## Value (V): PASS

The source's fixed-diameter theorem leaves the growth degree and polynomial coefficients unevaluated. Determining them at the first diameter displaying alphabet-dependent exceptional support lengths resolves a natural quantitative gap: degree seven for binary, five for ternary/quaternary, and four for all larger fields. The exact counts give precise finite-length enumeration, not just an asymptotic rate, and the unique maximal-support binary simplex structure explains the leading binary term. The counting problem is mathematically motivated by linear Hamming anticodes and support geometry and is not a renamed standard Gaussian-binomial exercise.

## Limits and comparison

The proof concerns actual coordinate-labeled linear subspaces of diameter **at most** four, not arbitrary nonlinear anticodes or classifications at larger diameter. Exceptional coefficients have exhaustive finite enumeration certificates with a transparent standard-library checker; independent mathematical validation is not claimed. The closest paper's support decomposition is credited, and its result is distinguished by the absence of any evaluated diameter-four polynomial or precise degree. Priority should be independently checked before publication.

Self-review: passed. Independent audit: not yet performed.
