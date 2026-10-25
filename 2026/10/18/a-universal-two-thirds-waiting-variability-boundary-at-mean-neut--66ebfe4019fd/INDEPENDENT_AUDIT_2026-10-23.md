# Independent mathematical audit

## correctness

PASS

For killed excursions E from (0,L), the Dirichlet ODEs D u=-1, D h=-x/L, D u2=-2u yield u=x(L-x)/(2D), h=E[E 1_{exit L}]=x(L^2-x^2)/(6DL), and u2=x(L-x)(L^2+Lx-x^2)/(12D^2). Reflected moments solve Dirichlet at 0 and Neumann at L. Renewal recursion T=E+J(W+Tprime) with P(J)=q=x/L gives mS=(u+q tau)/(1-q); this matches reflected mR=x(2L-x)/(2D) iff tau=(L-x)^2/(2D). Squaring the renewal identity gives MS=(u2+2h(tau+mS)+q(tau^2+v+2tau mS))/(1-q). At tau*, squared means cancel and symbolic simplification leaves x/(L-x)(v-2tau*^2/3). Independent SymPy substitutions exactly verified both mean equality and polynomial variance identity for symbolic positive x,L,D,v; representative deterministic, exponential and shape-3/2 Gamma holding laws realize both signs/equality. All parameter quantifiers and iid finite-second-moment assumptions matter; these are algebraic proof checks, not time-series simulations.

## originality

PASS

Chen-Bressloff (2026) model non-target boundary-triggered resetting with waits and comparison to reflecting walls in a 2D small-interior-target domain, but accessible abstract emphasizes MFPT, not a 1D all-wait-law mean-neutral variance transition. The full primary body could not be inspected, as open access attempts and authorized Oxford access failed with vpn_disconnected. García-Valladares et al. treat random spontaneous reset and refractory periods, a different trigger; Bressloff-Linn treat an active run-and-tumble particle with a sticky target. These works furnish renewal methodology, not a demonstrated statement with the same coefficients and geometry.

## value

PASS

Comparing protocols at equal mean passage time removes trivial speed advantages and reveals a sharp, dimensionless waiting-law volatility boundary. The exact sqrt(2/3) coefficient-of-variation cutoff distinguishes deterministic, exponential, and Gamma waiting protocols without reliance on their higher moments. This is a natural second-order search-performance invariant, not merely recomputing the MFPT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
