# Independent mathematical audit

## correctness

PASS

For Q=P−I and two-stage Radau IIA R(z)=(1+z/3)/(1−2z/3+z²/6), eigenvalues of hQ have Re≤0, whereas poles of R lie at 2±i√2, proving a unique well-defined endpoint matrix at every h≥0. R(0)=1 ensures row/column conservation. Modulo P^n−1, the complete certificate arrays in pinned verify.py give exact numerator-polynomial rational expressions for n=2..6, all numerators nonnegative and strictly positive for n≤5 at h>0. For n=6 the displacement-5 numerator is h^5 f(h), f=h^5+15h^4+60h³+90h²+36h−12, f′>0; other numerators positive, including the sign-indefinite p_{6,0} via h≤1 and h=1+t coefficient bounds. Thus positivity holds precisely {0}∪[tau,infty), tau unique positive root ≈0.208608859735; the exact h=1/10 coefficient is −743849/19268401151106. Independently recomputed rational endpoint inverses in 63 cycle-step instances n=2..8; also independently checked the z^5 Taylor coefficient −1/108 of R, proving negativity at distance five for every n≥6 at small h. Fourier diagonalization Q gives limit 11^T/n as h→∞ for each fixed n, hence eventual strict positivity. No complete intermediate region for n≥7 is claimed. All-n statements follow exact Taylor/Fourier arguments, not finite samples.

## originality

PASS

Hairer–Wanner 1999 and Ketcheson Numipedia give the classical Radau IIA stability function; the positivity threshold is not a claim about a new RK method. Zappavigna–Colaneri–Kirkland–Shorten discuss Padé schemes and positive systems, including a different [2/2] Gauss-type eight-state obstruction; [1/2] Radau on uniform directed cycles is not that diagonal [2/2] map. A published Resultary record on an eight-state [2/2] Padé Markov positivity barrier and another SSP-SDIRK dimension threshold were located, but these are mathematically different methods and graph domains. Accessible primary results did not establish the six-state exact fifth-degree positivity recovery boundary, leaving unindexed overlap risk.

## value

PASS

Entrywise stochastic positivity is essential when RK steps approximate CTMC transitions. An exact minimal dimension WITHIN a canonical uniform one-way cycle family and its surprising nonmonotone timestep positivity recovery are meaningful intrinsic sharp invariants and a practical non-SSP numerical-analysis benchmark. The qualified higher-n eventual recovery statement is useful without asserting an unfinished global classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
