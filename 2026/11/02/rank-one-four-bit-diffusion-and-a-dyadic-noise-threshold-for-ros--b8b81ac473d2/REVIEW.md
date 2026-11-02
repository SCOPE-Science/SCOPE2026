# Scientific review — rank-one four-bit diffusion and dyadic noise threshold

## Correctness — PASS

The statement has an explicit probability space: a stationary positive-density Rosenblatt-conjugate baker map, with binary branch-boundary exceptions of measure zero. The proof reduces every paired quantile discrepancy to a reversal-odd finite-bit window plus at most eight endpoint terms. For lengths up to three, all such windows are graph coboundaries; for length four, an explicit eight-vertex potential proves that the obstruction space is one-dimensional. The sole noncoboundary basis vector has exact autocovariances \((1/8,-1/32,-1/64,0)\), giving the limiting variance \(1/32\). Its finite dependence yields the normal law; all zero-obstruction cases have bounded sums. A second argument using independent tent branch cylinders proves the same-target sampler contrast. The finite exact-rational program confirms every edge and covariance calculation, but the indefinite-time conclusions follow from the explicit proof and standard finite-dependent limit theory, not the finite checks alone.

## Originality — PASS within inspected evidence

Fox, Hsiao and Lee, *Solutions of the Multivariate Inverse Frobenius–Perron Problem* (arXiv:2106.00177; DOI 10.3390/e23070838), give the conjugacy, baker map and componentwise triangle maps, which are prior ingredients. The inspected source sections establish preservation, mixing and numerical examples but do not state a classification of reversal-odd four-bit Green–Kubo forms or the four exceptional paired thresholds. The classical two-sided symbolic baker model is also prior background. Searches of mathematical research records for paired Rosenblatt quantile noise, four-bit reversal coboundaries and de Bruijn variance formulas did not retrieve an implication covering this specific rank-one formula. The nearest variance/coboundary record concerns a randomly switched pair of expanding circle maps and does not treat stationary two-coordinate baker discrepancies. Searches cannot establish exhaustive novelty: equivalent symbolic computations in unpublished notes, older coarse-graining literature or unindexed sources remain possible.

## Mathematical value — PASS

A natural unresolved statistical question after choosing a map with a prescribed target distribution is which observables have sampling fluctuations. The theorem proves that for a whole six-dimensional, mathematically canonical time-reversal-odd class, only one degree of freedom produces diffusive noise. It sharpens this invariant into the first binary-resolution threshold for paired quantiles, with a complete classification of all fifteen fourth-level cuts, and shows that a different sampler with exactly the same stationary density has genuinely independent half-quantile noise. The finding is more than a selected covariance entry or a zero-variance normalization check: it identifies the entire coboundary quotient and a sharp onset of nonzero variance.

## Closest literature and limitations

The defining 2021 article's Sections 4 and 6 were read in full relevant part through both arXiv HTML and the open full text at https://pmc.ncbi.nlm.nih.gov/articles/PMC8306100/. Section 6.1 already defines the same baker map; Section 6.2 already compares alternative invariant-density samplers. The rank-one temporal classification is the separated contribution. The normal law is for stationary starts only, and the threshold census is restricted to dyadic words of length at most four. A broader unindexed time-reversal-coboundary theorem might imply this computation, which is a residual originality risk. Independent verification by another researcher has not occurred.

Self-review: passed. Independent audit: not yet performed.
