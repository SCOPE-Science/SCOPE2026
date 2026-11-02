# Independent mathematical audit

## correctness

PASS

Read the finite generator and verified row sums, irreducible sixteen-cycle, stationary phase π_j=1/16 and strictly positive λ_j=1+10^-3 cos(πj/8). Palm event phase α_j=π_j λ_j/λ̄ with λ̄=1. Duhamel expansion C=Q-I-εV gives S_t-S_e=ε²e^-u I(u)+E, |E|≤ε³e^-u u² e^{εu}/2, I=1/2∫_0^u e^{-(1-cos π/8)s} cos(s sin π/8)ds. At u*=3π/(2sin π/8), the exact Fourier integral I=(1-e^{-3πtan(π/16)/2}/tan(π/16))/4<-1/6, while εu*²e^{εu*}/2<169/1974<1/6. The strict negative gap follows; derivative at zero is ε²/2>0. Independent 55-digit matrix exponential and analytic inequalities (nine checks) independently yielded S_t(u*)-S_e(u*)≈-1.08728715778341885e-12. This magnitude is tiny and numerical subtraction was not used as a proof.

## originality

PASS

The full Asanjarani–Nazarathy 2022 paper frames time-stationary stochastic dominance over event-stationary as Conjecture 3.9 (statement IV) for general MMPPs; its proven regimes are MSPPs and two-state MMPPs and its four-phase example concerns nonmonotonic hazard rate rather than failure of the waiting-time order. The earlier 2018 arXiv:1802.08400 abstract says an associated stochastic order was proved, whereas the authors later call the general order conjectural. Its full text could not be accessed; this inconsistency is material, not dismissed. The explicitly checked strict counterexample is logically incompatible with any valid universal dominance theorem, so a purported earlier universal proof does not establish strong factual coverage of the counterexample itself. A prior example may still exist.

## value

PASS

A rigorous explicit counterexample to a published universal stochastic-order conjecture is scientifically consequential even when the system has only sixteen phases. The Fourier-mode construction explains the mechanism (nonreversible oscillatory modulation) and provides a verifiable analytic sign margin independent of fragile numerical subtraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
