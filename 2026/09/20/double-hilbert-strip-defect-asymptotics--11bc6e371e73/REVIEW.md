# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The main identity was checked directly from the Fourier multiplier of the double Hilbert transform. For a diagonal tube with arbitrary transverse cutoff, the change of variables p=xi1+xi2 turns the two same-sign quadrants into the finite interval between 0 and p. This gives the exact formula
\[
\|(H-I)f_{\varepsilon,g}\|_2^2
=\frac{8\varepsilon}{\pi}\int |\widehat g(\xi)|^2F(\varepsilon|\xi|)\,d\xi.
\]
The constants agree with the Fourier normalization used in the direct source.

The smooth-cutoff asymptotic follows by dominated convergence from F(s)/s -> 1 and F(s) <= s. For a finite union of intervals, the endpoint Fourier formula for the indicator was expanded exactly. The only nontrivial universal constant is the large-a asymptotic of
\[
I(a)=\int_0^\infty(\cos(au)-1)F(u)u^{-2}\,du.
\]
The cosine-integral reduction and Mellin calculation give
\[
I(a)=-\log a-(5/2-\log2)+o(1).
\]
The Mellin transform
\[
\int_0^\infty (\sin u/u)^2u^{s-1}du
=\frac{\pi2^{-s}}{\Gamma(3-s)\sin(\pi s/2)}
\]
has Laurent constant 3/2-gamma-log 2 at s=0, producing the stated constant. The endpoint-sign identity sum_{j<k} sigma_j sigma_k=-P(E)/2 was checked, and it also verifies the scale covariance of the final expression.

The single-interval specialization was independently evaluated numerically from the direct-source double integral. For eps=0.05, 0.02, 0.01, the quantity
\[
Q(\varepsilon)/\varepsilon^2-\tfrac12\log(1/\varepsilon)
\]
was approximately 1.249953, 1.249982, 1.249986, consistent with the proved limit 5/4. The numerical calculation is only a check; the result rests on the analytic proof.

## Originality

**PASS, to the best of our knowledge.** The relevant sections of Abakumov--Domelevo--Petermichl--Poltoratski, arXiv:2609.15155, were inspected. Their bounded strip is exactly the L=1 case considered here. They estimate its defect from above by O(epsilon^2 |log epsilon|), hence obtain an O(sqrt(epsilon |log epsilon|)) relative error, and later cite that cost as the model computation in their quantitative-stability question. They do not state a matching lower bound, a leading constant, the +5/2 correction, the arbitrary-cutoff identity, or the finite-perimeter endpoint interaction formula.

Repository searches used the direct source identifier and the terms double Hilbert transform, strip defect, quasi-eigenfunction, diagonal strip, and epsilon-log asymptotics; no existing SCOPE record covering this claim family was found. External searches used exact and synonymous formulations, including the leading constant and hard-cutoff/H^{1/2} language, and did not locate an equivalent result or a stronger theorem visibly implying it.

The commutator paper Holmes--Treil--Volberg (arXiv:2101.00763), cited by the direct source, concerns dyadic bi-parameter repeated commutators rather than this Fourier defect calculation. Sanjay Patel's 2011 paper *Double Hilbert transform in R2* was checked at the primary-source statement level: its operator is a polynomial-surface singular integral and is mathematically different from H1H2 acting on planar indicators. Other search hits with “double Hilbert transform” likewise concern transforms along polynomial or real-analytic surfaces or numerical quadrature.

No inaccessible paper was identified as especially likely to contain the exact strip asymptotic. The principal residual risk is temporal: arXiv:2609.15155 is very recent, so an unindexed contemporaneous follow-up may exist. The originality assessment is therefore explicitly limited to the best of our knowledge.

## Value

**PASS.** The direct source uses the truncated strip as the model analytic mechanism behind its quantitative-stability question. The present theorem determines that model sharply: the logarithm is genuinely present for a hard cutoff, its relative leading constant is 2/pi, and the next constant is explicit. The arbitrary-cutoff identity additionally explains why the logarithm disappears for transverse data in H^{1/2}, while the finite-perimeter theorem shows that the leading hard-cutoff coefficient depends only on one-dimensional perimeter and the next term records logarithmic interactions between boundary points. This separates a universal endpoint mechanism from the special choice of one interval.

## Limitations

- Only diagonal tubes with transverse cutoffs are analyzed; no general near-invariant-set classification is proved.
- The finite-perimeter expansion is for a fixed bounded one-dimensional set as epsilon tends to zero; it is not uniform under endpoint collisions.
- No global extremality statement among bounded planar sets is claimed.
- The quantitative-stability question in arXiv:2609.15155 remains open.
- A contemporaneous unindexed overlap remains possible because the direct source is very recent.
- Cross-model review has not been performed, and no independent validation is claimed.
