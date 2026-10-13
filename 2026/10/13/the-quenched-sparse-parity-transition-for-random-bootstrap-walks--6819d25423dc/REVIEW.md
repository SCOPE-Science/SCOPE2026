# Scientific review

## Correctness — PASS
Conditional on the entire input-sign path, the number of active Boolean coefficients at step \(n\) is precisely \(2^{N_n}\); their independent Bernoulli parity yields the exact mean \((1-2r_n)^{2^{N_n}}\). Independent coefficient rows and Hoeffding--Borel--Cantelli establish quenched Cesàro concentration by Fubini. The strong law separates the subcritical/supercritical cases. The supercritical coupling is eventually exact, not merely distributional. At criticality, elementary two-sided bounds on the parity mean and almost-sure negligible occupation of every fixed strip about zero prove pathwise convergence of normalized cross-variation to the positive-time occupation functional. Donsker, the arcsine law and the established cross-variation necessity criterion finish the proof. The exact checker passes 684 assertions; it supports finite identities only. No unproved continuum assertion is delegated to code.

## Originality — PASS, with residual priority risk
The principal 2026 source studies random coefficient environments and proves independence of the Brownian coordinates under uniform ellipticity; the present coefficients vanish exponentially and are outside its hypotheses. The 2022 foundational source supplies a general Brownian-limit criterion and non-Gaussian deterministic sign-recycling examples, but not this sparse random-family threshold or the quenched phase classification. Comparison is by implication: the old criterion alone cannot calculate the row-parity asymptotics or determine the almost-sure critical environment behavior. A targeted search of published mathematical records and primary literature found no covering result. An older/unindexed equivalent sparse parity calculation remains possible.

## Value — PASS
The natural number of coefficients evaluated along a typical path is approximately \(2^{n/2}\); tuning their individual activation probability across the reciprocal scale produces qualitatively distinct quenched regimes. The theorem gives a sharp structural boundary, a singular non-Brownian critical phase with an explicit arcsine law, and eventual pathwise coalescence in the supercritical regime. These are infinite-time conclusions in a current, motivated random-transformation model, not arbitrary parameter plugging or a finite tabulation.

## Closest sources and limitations
Hamza–Tournier, arXiv:2610.01658v1, Section 3, Theorem 2; Collevecchio–Hamza–Shi–Williams, arXiv:2010.16000v2, Sections 3--4. The full pair's critical limiting process, convergence rates, and nonhomogeneous/dependent-coefficient extensions remain outside scope. Priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
