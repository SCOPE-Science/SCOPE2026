# Scientific review

## Correctness — PASS

The theorem precisely assumes coprime degrees and odd finite fields satisfying both signed congruences; these hypotheses imply tameness. The Chebyshev commuting identity, field-extension coprimality, integrality, and degree argument establish the normalization. Explicit cyclotomic parameters enumerate all and only \(\delta\) nodes; the differential equation shows every tangent cone is reduced. The ratios of tangent slopes transform by \(\epsilon_m\epsilon_n\) under Frobenius, and identifying branches on the affine normalization gives the exact count in every extension. The zeta identity is then formal. Independently, the included exact checker passed 84 prime-field and eight quadratic-field cases. Finite checks are not the proof; no claim outside the stated congruences is made.

## Originality — PASS (with residual literature risk)

Freudenburg–Freudenburg's characteristic-zero Proposition 3.1 already gives the normalization and geometric nodes, and is used as background. A comparison of its relevant full Section 3 found no finite-field Frobenius sign classification or zeta formula. Garcia–Stichtenoth's 1999 finite-field paper was inspected in its reflowed complete text: its models are maximal smooth Kummer covers derived from Chebyshev polynomials, not the affine nodal pair-equality \(T_n(x)=T_m(y)\). The 2017/2018 Kazemifard–Tafazolian–Torres treatment revisits those Kummer-cover models (Theorems 9 and 13); neither their genus formulas nor maximality claims imply the singular curve's rational branch-gluing zeta factor. Direct keyword, equation, and zeta-function searches found no statement of the uniform signed factor. The 2014 finite-field Chebyshev-polynomial book chapter was available only in abstract; a fuller comparison could still disclose related computations. No failure to retrieve a publication is treated as evidence of novelty.

## Value — PASS

The complete zeta function is a natural arithmetic invariant of the specific nodal affine curve family, which was previously studied primarily geometrically. One bit of simultaneous congruence information governs *every node's* arithmetic branch type and all extension point counts, not merely a chosen small parameter instance. In the mixed-sign regime the curve has \(q+\delta\) points despite normalization \(\mathbb A^1\) having \(q\), reflecting a substantive geometric distinction; for equal signs the opposite deficit is exact. This supplies a uniform structural bridge between the geometric node classification and arithmetic of singular rational curves. It is not proposed as a general smooth-curve bound or a result about projective completions.

## Close literature and limits

Most directly related: Freudenburg–Freudenburg (2009), Proposition 3.1; Garcia–Stichtenoth (1999); Kazemifard–Tafazolian–Torres (2017/2018). Residual risk: a 2014 finite-field Chebyshev-polynomial chapter was not inspected beyond its abstract, and literature indexing is imperfect. The scientific proof itself is self-contained in `RESULT.md`; `verify.py` supplies independently rerunnable finite tests.

Self-review: passed. Independent audit: not yet performed.
