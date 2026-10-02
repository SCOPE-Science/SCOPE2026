# Independent audit — 2026-10-01

## Final claim

Sharpness of the nonnegative-parameter range for the ultraspherical lower envelope

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

For \(-1/2<\alpha<0\), direct normalized-Jacobi algebra at \(\xi_1=-1/(2\alpha+3)\) gives \(U_5(\xi_1)-U_1(\xi_1)=4\alpha(\alpha+2)(2\alpha+1)(2\alpha+7)/(2\alpha+3)^5<0\); an independent symbolic derivation reproduced this factorization exactly. At \(\alpha=-1/2\), the normalized family is Chebyshev and \(T_4(-1/\sqrt2)=-1<-1/\sqrt2=T_1(-1/\sqrt2)\). For \(-1<\alpha<-1/2\), the standard central-value formula \(U_{2m}(0)=(-1)^m\Gamma(\alpha+1)\Gamma(m+1/2)/(\sqrt\pi\,\Gamma(m+\alpha+1))\) has magnitude growing like \(m^{-\alpha-1/2}\), so the lower envelope is unbounded below. Together with Castillo--Sadigova's theorem for \(\alpha\ge0\), these cases give the exact parameter range.

## Originality

Castillo--Sadigova's September 2026 theorem explicitly covers \(\alpha\ge0\). Targeted searches found no prior theorem classifying failure for all negative Jacobi parameters. The audited degree-five defect, Chebyshev endpoint witness, and unbounded-below regime therefore survive as a best-of-knowledge sharpness classification; a later SCOPE record about the Legendre case \(\alpha=0\) concerns minimizer multiplicities rather than negative-parameter sharpness.

### Equivalent formulations

**Searches**
- Published-record semantic search: ultraspherical lower envelope negative alpha Jacobi sharpness degree five Chebyshev
- Web search: negative alpha ultraspherical Jacobi lower envelope Castillo Sadigova

**Evidence**
- The exact 2026-09-17 record and a later Legendre-only minimizer-classification record were found; no earlier negative-parameter classification was located.

**Reasoning**

Searches covered ultraspherical/Gegenbauer/Jacobi terminology, lower envelope, negative parameter, and Chebyshev specialization.

### Broader coverage

**Searches**
- K. Castillo and S. Sadigova, arXiv:2609.15473
- NIST DLMF Chapter 18
- F. M. de Oliveira Filho 2009 thesis context

**Evidence**
- Castillo--Sadigova state the interval-by-interval theorem for \(\alpha\ge0\). DLMF supplies classical Jacobi identities and asymptotics, not the three-regime sharpness theorem.

**Reasoning**

The negative-parameter counterexamples lie outside the proven parameter range of the motivating theorem and are not dominated by a broader envelope theorem located in the search.

### Exact database or table

**Searches**
- Published-record search for exact defect factor and negative-parameter threshold
- Classical orthogonal-polynomial reference search for central Jacobi values

**Evidence**
- Classical references contain the identities used in the proof, but no table was found asserting the exact \(\alpha=0\) validity boundary for this lower-envelope theorem.

**Reasoning**

The individual Jacobi evaluations are classical; the new content is their organization into the sharp parameter classification, not the formulas themselves.

### Claim versus prior implication

**Searches**
- Direct comparison with Castillo--Sadigova theorem domain \(\alpha\ge0\) and classical Jacobi/Chebyshev formulas

**Evidence**
- The source theorem establishes sufficiency for nonnegative alpha. Classical formulas permit explicit counterexamples below zero but do not themselves state the global three-regime lower-envelope classification.

**Reasoning**

The classification is a motivated boundary theorem obtained by deriving and comparing the decisive counterexamples across all negative parameters.

### Source inspections

- **The lower envelope of ultraspherical polynomials** — SOURCE_DOMAIN_STOPS_AT_ZERO. Current arXiv abstract with the exact interval-by-interval theorem for normalized Jacobi polynomials and domain \(\alpha\ge0\); direct PDF access was unavailable. The theorem is stated for \(\alpha\ge0\), leaving the negative Jacobi range outside its conclusion.

- **NIST Digital Library of Mathematical Functions, Chapter 18** — CLASSICAL_INGREDIENTS_NOT_CLASSIFICATION. Relevant classical orthogonal-polynomial formulas at the level needed to check normalization and central values. The formulas are classical and not claimed as new; no matching three-regime sharpness statement was identified.

### Checked sources
- https://arxiv.org/abs/2609.15473
- https://dlmf.nist.gov/18
- Published SCOPE record dated 2026-09-19: complete-ultraspherical-minimizer-classification--58eedb8b1030
- Published-record semantic search

### Residual risks
- The motivating theorem is very recent and its full PDF was unavailable through the audit route, so rapid revisions or contemporaneous negative-parameter notes remain the principal originality risk.

## Value

Determining the exact maximal Jacobi parameter range of a newly proved lower-envelope theorem is a natural sharpness question. The three distinct failure mechanisms, including a uniform degree-five obstruction immediately below zero and unbounded-below behavior below the Chebyshev threshold, give structural information beyond a single counterexample.

## Limitations

The classification concerns the interval-by-interval lower-envelope theorem in the natural Jacobi range \(\alpha>-1\). It does not alter the original motivating question, which was posed for \(\alpha\ge0\). Full arXiv PDF access to the new Castillo--Sadigova paper was unavailable during this run, so comparison used its current abstract plus the exact theorem statement reproduced in the audited record and standard Jacobi identities.
