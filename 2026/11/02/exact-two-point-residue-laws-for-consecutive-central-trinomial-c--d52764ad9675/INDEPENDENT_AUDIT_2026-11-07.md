# Independent mathematical audit

## correctness

PASS

The antecedent Krattenthaler–Müller Theorem 17 gives T_n≡1+2s₂(floor(n/2))+4e₂(n) mod8. Write n=2^(t+1)H+2^t−1, t=v₂(n+1); direct carry counting gives Δ(a,b)=(0,H mod2) for t=0 and (t mod2,(H+t−1) mod2) for t≥1. Every initial-state/low-bit triple is asymptotically uniformly distributed with O(√M) discrepancy by binary Walsh inversion and a signed 2×2 transfer with M_u M_u^T=2I. The parity-class trailing-run weights are t=0:1/2, positive odd t:1/3, positive even t:1/6; with conditional fair Δb this yields each 1/12 or 1/24 joint transition. Sum O(√(N/2^t)) over t gives O(√N) for every cutoff. A Rudin–Shapiro transfer shows B_r=∑_{n<2^r}(−1)^{e₂(n)}=2^ceil(r/2), a signed row-combination obstruction to a uniform smaller error exponent. Independent recurrence and digit checks verified first 514 coefficients and pair tables through 2^16; this does not substitute for infinite proof.

## originality

PASS

Krattenthaler–Müller Theorem 17 ALREADY determines each coefficient modulo 8 and is correctly credited. The new claim is its quantitative adjacent-pair distribution and sharp all-cutoff discrepancy, obtained via carry partition and signed automata; the inspected theorem/neighboring text does not state this joint law. Beukers p-linear schemes and Rowland–Yassawi automata provide wider techniques, not a located dominating two-point transition table. An unindexed automatic-sequence autocorrelation theorem might imply it, acknowledged as risk.

## value

PASS

Consecutive residues of a classical integer sequence have a natural 16-state joint distribution; the exact two-level Markov-like transition probabilities show persistent dependence despite uniform one-point frequencies. A sharp all-cutoff square-root error and its obstruction supply mathematically reusable quantitative digit-correlation information, not merely rephrasing the antecedent digit formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
