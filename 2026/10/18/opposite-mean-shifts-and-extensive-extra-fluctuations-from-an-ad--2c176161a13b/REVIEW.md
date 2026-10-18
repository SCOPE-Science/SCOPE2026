# Scientific review

## Correctness

**PASS.** Exact rare-event couplings distinguish hub-first wheel deposition from first-successful-even-site gear deposition. The critical gear probability is \(\lambda/m+o(m^{-1})\); a factorial causal-radius bound and a fourth-moment dependency-graph estimate make cycle-size concentration strong enough to condition on an event of probability \(\Theta(m^{-1})\). The second-moment subtraction yields both extensive variance corrections. The full pathwise argument is given in `RESULT.md`; independent finite recursions and exhaustive small-order checks are in `verify.py`. The baseline one-dimensional variance is taken from Penrose–Sudbury (2005), Theorem 11.

## Originality

**PASS within accessible comparisons.** The 2005 primary paper establishes path bulk variance but not the two high-degree hub responses. The 2015 greedy-set study and published complete-multipartite/threshold/chain graph results have different graph families or conclusions. A relevant older paper on graph adsorption was accessible through bibliographic data rather than full text; an equivalent wheel/gear formula in uninspected literature is a residual risk. This is not a claim of independently certified uniqueness.

## Mathematical value

**PASS.** The same local kinetic deposition rule responds with opposite mean signs under two natural hub geometries, while both high-degree defects create order-size extra variance. The result separates the near-zero-probability macroscopic event mechanism from ordinary bounded-degree bulk fluctuations, furnishing exact checks for irreversible deposition on wheel and gear substrates.

## Limits

Fixed \(\lambda>0\), one-shot continuous clocks, simple wheel/gear topology, first two terminal moments; no rate-uniform limit, time-to-jam law, higher moment law, or independent audit.

Self-review: passed. Independent audit: not yet performed.
