# Scientific review: generalized Hilbert beta curves

## Correctness (C): PASS

The claim concerns the **Fredholm** essential spectrum of the nonsymmetric generalized Hilbert operator on complex \(H^2\), for every real \(b>0\), and an additional classification of nonzero crossings only for integer \(b=m\ge1\). The derivation proceeds from the exact beta-integral matrix formula, through a quantitative Hilbert--Schmidt comparison to the homogeneous kernel \(x^b/(x+y)^{b+1}\), to a one-sided convolution under logarithmic coordinates. That convolution has the explicitly computed beta-function Fourier multiplier. The standard scalar Wiener--Hopf Fredholm theorem establishes the criterion and index for every nonzero spectral parameter; a separate weakly-null basis sequence proves that zero is not Fredholm. Neither a finite matrix limit nor a numerical plot is used as a substitute for these steps.

The crossing statement follows from gamma recurrence, the Euler product for \(\cosh\), and strict angular/radial monotonicity. A radial proof excludes accidental non-real intersections; a phase proof gives every remaining crossing and shows it is transverse. All integer parameters, including \(m=1,2\), are covered, and zero is explicitly excluded from the double-point count.

For computational stress-testing, the packaged `CHECK.py` passed 6,909 deterministic assertions covering matrix coefficients, normalization, conjugation, phase and modulus, crossings, and representative gamma-ratio estimates. Such calculations independently check arithmetic, not infinite Fredholm or compactness claims.

**Limitations/risk:** The argument invokes the standard Wiener--Hopf Fredholm theorem and classical gamma/cosh identities as established external mathematical inputs. The complete operator spectrum (including isolated eigenvalues) is not obtained.

## Originality (O): PASS, best-knowledge comparison

**Closest initiating source:** Li--Pan--Zhou, arXiv:2608.19660 (first posted August 20, 2026). Its main results give precise Hardy-space norms, \(H^1\) boundedness and \(H^\infty\)-to-Bloch behavior for the same operator. Its full accessible HTML research text was checked by sections, and its discussion contains no Fredholm spectrum or winding-index determination. Their exact \(H^2\) norm is a consistency check here and is not presented as an original fact.

**Exact older operator, different questions:** Bhuyan--Naik (DOI:10.1108/AJMS-07-2024-0111) has the identical gamma-ratio matrix and studies mapping and boundedness on Hardy, weighted Hardy and Bloch spaces, not a Fredholm curve. An earlier Li--Stević introduction from 2009 is credited through the initiating paper. The distinction between the operator's introduction and the date of the newly motivating Hardy-norm result has been maintained.

**Closest spectral precedents:** Silbermann (DOI:10.1007/s00020-021-02637-5) treats shifted *Hankel* Hilbert matrices with entries of the form \(1/(j+k+\lambda)\); a shift in the denominator does not introduce the row weight \(j^b\), and its spectral interval at exponent two cannot imply the complex beta curve. Pushnitski (arXiv:2103.12642) studies Hermitian homogeneous Hardy kernels and real, self-adjoint Fourier symbols: the current positive-\(b\) kernel is nonsymmetric, and its complex Fredholm curves and transverse loops are outside the theorem's hypotheses. The established continuous-model comparison technique is appropriately credited. Bellavita and collaborators (arXiv:2307.15334) work with another generalized Hausdorff Hilbert construction and prove boundedness, norm, noncompactness and continuity statements, not the present spectral formula.

**Other related published statements:** Searches for the beta gamma ratio, Mellin-convolution equivalent, nonselfadjoint Hilbert matrix, exact Fredholm spectrum, and spectral self-intersections found several nearby published statements but no equivalent or dominating one. Those statements concern a different logarithmic Copson endpoint, slowly oscillating generalized Hilbert norms, and Gamma Hausdorff operators on BMOA/Bloch; they do not identify this operator on complex \(H^2\) or its beta-symbol crossing counts.

**Residual priority risk:** A pre-existing theorem on non-selfadjoint homogeneous Hardy kernels or a differently normalized Mellin/Toeplitz construction could imply the same boundary without matching words. Searches and primary-source inspection reduce but do not eliminate this possibility. No independent literature or priority certification is claimed.

## Mathematical value (V): PASS

The exact norm of this generalized Hilbert family is known, but norm information alone cannot describe invertibility modulo compact operators or the Fredholm index. The new result gives a complete Fredholm boundary and all off-boundary index values for the whole positive parameter range. The integer family exhibits a systematic and unbounded hierarchy of **genuine transverse spectral-curve self-intersections**, with the first appearing at the natural low rank \(m=3\) and another at each subsequent odd \(m\). This is a structural, parameter-dependent spectral classification of a familiar operator family, not a renaming or arbitrary finite computation.

The formula also supplies a concrete benchmark for nonnormal Fredholm spectral geometry and makes explicit why older self-adjoint Hilbert-matrix theory does not simply extend by shifting its usual parameter. A classification of the full spectrum, spectral multiplicities or the self-crossing structure for all nonintegral parameters would be separate work; their absence does not undermine the value of the complete Fredholm result.

Self-review: passed. Independent audit: not yet performed.
