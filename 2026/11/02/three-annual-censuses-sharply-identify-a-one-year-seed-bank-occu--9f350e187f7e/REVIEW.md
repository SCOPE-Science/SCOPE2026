# Assessment of the three-census seed-bank identification theorem

## Correctness — PASS

The statement is proved over all strictly interior \((c,g_0,g_1,d)\in(0,1)^4\), not inferred from simulation. The key ecological premise \(B_{t+1}=Y_t\) follows from the one-year bank rule of the motivating 2013 model. Independence and common disturbance then yield the exact order-two transition table. Algebraic inversion proves global one-to-one recovery and the complete strict feasible-domain inequalities. The four-state stationary pair chain is irreducible; the two-year law depends on only two smooth ratios with differential rank two, proving the sharp failure of two-year identification. An exact-rational checker tested 256 parameter quadruples and symbolic Jacobians. The result requires perfect detection and exact population laws; numerical tests are supplemental.

## Originality — PASS within inspected sources, residual historical risk

The full accessible principal article (Fréville et al., 2013, DOI 10.1111/1365-2745.12141) introduces the four-state model and discusses HMM fitting and structural nonidentifiability when delayed recruitment vanishes. It does not state the global rational four-parameter inverse, the feasible-table characterization, or the sharp *stationary three-observation law* theorem in its inspected main text. Choquet and Cole (2012) develop generic local identifiability tests rather than these exact statements. The accessible complete Borgy et al. (2015) and Louvet et al. (2021) papers use different longer-lived or survival-based bank models. Manna et al. (2017) report three-year simulated scenario discrimination with 1,000 sites but not this exact universal structural theorem; only its abstract and bibliographic material were accessible. Algebraic noisy-OR inversion is elementary known methodology, not separately claimed as novel. The 2013 supplementary matrix appendix could not be accessed, so an unlocated equivalent formulation remains a genuine risk. Published-finding comparisons did not identify an exact dominating theorem, but absence of such a match does not certify novelty.

## Value — PASS

The article's core practical mathematical issue is how above-ground surveys distinguish unseen dormancy, colonization, and disturbance. Here a nominal hidden four-state model becomes an *observable* two-step process, giving the precise minimal calendar horizon and an exact admissibility test from four observable conditional probabilities. This is a natural diagnostic and survey-design boundary rather than an arbitrary numerical slice. No claim of small sample error, robustness to patch heterogeneity, or field-ready three-observation estimation is made. Conditioning becomes poor near zero delayed recruitment, supporting the need for substantial replication in practice.

Self-review: passed. Independent audit: not yet performed.
