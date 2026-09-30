# Independent audit — 2026-09-29

Record: `2026/09/19/almost-sure-coalescence-cusp-diffusions--3cc504535cf9`  
Assigned and audited source tree: `ceeb6ef5948362784ccd5672ae25e057b00ab17f`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `3abdec33c9bbc4463291524025b930d6c735a773`  
Disposition: **passed**

## Correctness

**independently_supported**. The local, time-scale, and global arguments check. Replacing Larsen's unit local-time threshold by a level a leaves the stopped Lyapunov estimate unchanged except for Markov's inequality, yielding the C d^(1-2beta)/a term. Under Dambis-Dubins-Schwarz, midpoint local time before exit from (-1,1) has the Brownian exponential law, while the nonnegative gap local martingale gives P(sup D>=1)<=d; this yields the tunable collision bound. Because the midpoint quadratic variation dominates physical time, the inverse-local-time tail is bounded by P(|N(0,t)|<a), and optimizing A/a+Ba gives the stated collision-time bound and O_P(d^(2-4beta)) upper scale. For the global step, D converges as a nonnegative local martingale. A positive limiting gap would make the gap diffusion coefficient uniformly nonzero whenever the recurrent midpoint visits a suitable interval; the midpoint clock has infinite recurrent occupation there and its local speed is bounded on that interval, forcing infinite gap quadratic variation, contradicting convergence. Hence on noncollision D->0. Recurrent zero returns of the midpoint then produce arbitrarily small symmetric pairs, and the strong Markov property plus the local collision probability tending to one forces the probability of perpetual noncollision to zero.

## Originality

**qualified_supported_after_legacy_check**. Larsen's September 2026 preprint proves that strict comparison fails for the subcritical cusp and establishes positive-probability collision for small symmetric gaps, but its public statement does not give collision probability tending to one, the quantitative upper time scale, or almost-sure coalescence for every fixed pair. The full 15-page Yamada 1986 paper was retrieved through authorized Oxford access after open-access attempts failed; it develops sufficient non-confluence conditions and does not supply these subcritical-cusp conclusions. Ouknine-Rutkowski 1990 remained inaccessible because publisher human verification was required and was not bypassed, so it remains an explicit residual prior-art risk. Barlow-Burdzy-Kaspi-Mandelbaum give almost-sure coalescence for skew Brownian motion, a different local-time model. Current searches did not locate the specific cusp conclusions.

## Scientific value

**meaningful_strengthening_of_counterexample**. The result changes the interpretation of Larsen's counterexample from a positive-probability contact event to unavoidable eventual coalescence for every fixed ordered pair, and supplies a shrinking-gap quantitative time scale. That is a substantial dynamical strengthening even though no matching lower scale is proved.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/almost-sure-coalescence-cusp-diffusions--3cc504535cf9
- https://arxiv.org/abs/2609.19389
- https://www.numdam.org/item/SPS_2001__35__202_0/
- https://doi.org/10.1080/17442508608833385
- https://doi.org/10.1016/0304-4149(90)90092-7
## Access note

The full 15-page Yamada (1986) article was obtained through authorized Oxford institutional access after open-access attempts failed and was inspected. It gives sufficient non-confluence criteria but does not supply the subcritical-cusp coalescence statements audited here. Authorized retrieval of Ouknine--Rutkowski (1990) reached a publisher human-verification gate; that gate was not bypassed, and the article is not claimed to have been read in full.

## Limitations

- The collision-time estimate is only an upper scale; no matching lower bound or limiting law is proved.
- The almost-sure statement is for each fixed deterministic pair, not a simultaneous statement for all starting points.
- The constants inherited from Larsen's local Lyapunov construction are not optimized.
- Yamada 1986 was fully inspected through authorized institutional access, but Ouknine-Rutkowski 1990 remained inaccessible behind human verification and is not claimed to have been read.
