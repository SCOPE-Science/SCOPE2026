# Scientific review: radial inference of the killing index

## Correctness — PASS

The statement fixes \(0<p<1\), \(c,\lambda>0\), all positive observation radii, and all positive integer killing indices. The independent-segment characteristic function and Gamma–normal variance-mixture identity reconstruct the exact conditional position densities. The ratio of the variance-mixing posterior densities at two radii is strictly increasing in the variance coordinate, establishing the strict likelihood-ratio theorem for every index pair. The marked Fourier transform splits algebraically into a Bessel resolvent and a positive subordinate-semigroup integral. The integral is exponentially smaller than the resolvent for fixed parameters as the observed radius grows; the complex-uniform large-argument Bessel expansion proves the displayed conditional cumulant expansion and hence the centered Gaussian limit. The analytic proof addresses all stated quantifiers, with no inference from finite numerical samples to an infinite theorem.

An executable finite verifier checks 275 independent numerical identities and inequalities using two different evaluations of the marked density. This supports arithmetic and normalization but does not itself verify infinitely many radii or asymptotic convergence. Relevant exact calculation and limit steps appear in `RESULT.md` under Proof.

## Originality — PASS with residual historical-priority risk

The principal primary comparison is Orsingher and Marchione, *Killing random motions with finite velocity*, arXiv:2610.15094 (first submitted 2026-10-10). The actual text of its planar Section 4 and Theorems 7–11 was inspected. It explicitly gives the geometric killing count, each count-conditional terminal spatial density, and the unconditional spatial density. Consequently the formal Bayes posterior formula is **already implied by prior work** and is not claimed as an independent advance. The claim here is the exact strict likelihood-ratio ordering of that posterior and the distant-radius Gaussian limit, including its explicit linear cumulant coefficients and constant-order shifts. The inspected paper does not state those comparisons or this limit. The earlier infinite-direction work of Kolesnik and Orsingher treats deterministic-time planar flights, and Kolesnik's integral-equation treatment addresses fixed-time transition densities; neither inspected statement supplies the conditional far-radius theorem.

The most plausible remaining overlap is a more general historical total-positivity result for Gaussian variance mixtures, which could subsume the monotonicity component, or a general compound-geometric saddlepoint/local-limit theorem giving the full posterior asymptotics. Both are priority risks; the absence of a matching search result is not evidence of uniqueness. The full combined theorem and constants were not found in the actual inspected sources. Independent literature review is not claimed.

## Mathematical value — PASS

Given only the terminal distance of a planar motion that has ceased, the natural latent statistic is the number of Poisson events before death. A geometric prior and fixed-index Bessel densities do not alone describe how the observation changes this latent count. Strict likelihood-ratio ordering provides exact monotone inference at all radii, and the Gaussian law quantifies large-distance uncertainty at its natural linear scale. Explicit order-one mean and variance corrections distinguish this result from a qualitative concentration statement. The theorem is motivated by the source paper's killed-flight model and concerns an intrinsic inferential statistic rather than an arbitrary parameter slice.

## Scope and outstanding limitations

The theorem is restricted to isotropic fresh directions, Poisson event times, constant speed, independent eventwise killing with fixed \(0<p<1\), and radius-conditioned observations at \(r>0\). The limit is not uniform in \(p\), and no pathwise reconstruction or non-Poisson extension is proved. Possible broad total-positivity and compound-geometric results remain a scientific priority risk. The finite verifier is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
