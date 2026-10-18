# Independent mathematical audit

## correctness

PASS

The exact identities E=(x²+y²)/2, E'=y² z, Q=b+y²-a x², z'=z-Q are independently recomputed. Every bounded forward orbit obeys future filter z(t)=∫_0∞e^-s Q(t+s)ds. If z is eventually nonnegative then E is eventually nondecreasing and bounded; its compact ω-limit has E constant so y²z=0. A complete nonzero-y arc there would force z=0, a x²-y²-b=0, and derivative 2(a+1)xy=0; a=-1 contradicts b>0 and other a contradict x'=y. Thus only the equilibrium e=(0,0,b) can remain; eventual z>=0 forces the actual orbit stationary. Every nonstationary bounded orbit therefore visits z<0 and Q<0 arbitrarily late. Passing to its nontrivial compact ω-limit and a complete limit orbit upgrades these arbitrarily late sign crossings to strict liminf z<0 and limsup (a x²-y²)>b. If a<=0 pumping is impossible, giving only e; for a>0 necessary |x|>sqrt(b/a) somewhere on ω. Exact independent symbolic calculations reproduced E', z'-relation and the 2(a+1)xy derivative. There is no claim that this necessary condition ensures existence of bounded a>0 dynamics.

## originality

PASS

Best-of-knowledge original infinite-time all-bounded-orbit recurrent-sector restrictions for the precisely normalized single-unstable-node quadratic flow. Sprott et al. 2015 introduce equation (9) and numerically exhibit attracting sets at selected positive a; their reported average height constraints do not imply strict necessary excursions of ALL bounded forward trajectories, nor global exclusion at a<=0. Related generalized Sprott Resultary records are different polynomial flows. 2021 Chen et al. HTML loses some formulas and leaves residual coverage risk.

## value

PASS

Global rigorous obstruction replaces a parameter scan with an all-orbit theorem, constraining compact invariant sets and stationary measures; such necessary sectors are relevant even without proving existence for a>0. The strict asymptotic margins are stronger and naturally useful compared with period-wise numerical observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
