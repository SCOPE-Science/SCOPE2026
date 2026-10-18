# Independent mathematical audit

## correctness

PASS

From the inspected signSGD update and uniform noise, the transition probability P(k->k-1)=P(xi>B-2Bk/M)=k/M for 0<=k<=M, with the complementary upward probability. States outside move deterministically toward the band, including boundary inward transitions. Detailed balance yields pi_k=2^{-M}binom(M,k), unique by irreducibility, and every move flips parity. Setting Y=k-M/2 gives E[Y'|Y]=(1-2/M)Y and E[(Y')²|Y]=(1-4/M)Y²+1. The exact second-moment recurrence, stationary E f=delta B/4, M=1 constant loss, M=2 period-two loss, and M>=3 convergence follow analytically. Independently checked the M=7 rational transition matrix against its binomial invariant and E Y²=M/4; finite code verified only representative cases, not infinity.

## originality

PASS

A standard Ehrenfest birth-death chain is obtained by a concrete support-aligned uniform-noise signSGD reduction; the urn's binomial invariant and parity are classical, not claimed as new. Best-of-knowledge originality is in the exact model identification, resulting step-linear optimizer noise floor and exceptional last-iterate behavior for this specified optimization oracle. Bernstein et al introduce signSGD but do not supply this exact chain; the closest recent Singh–Mishra–Raut source considers primarily multiplicative signSGD noise and a different additive-SGD comparison. The failed semantic-index search and inaccessible full recent paper remain material risks.

## value

PASS

An exact finite-state invariant law and phase-resolved transient loss for a natural optimizer under a canonical bounded additive oracle are useful diagnostics of constant-step stochastic optimization. Step-linear loss and M=2 nonconvergence quantify behavior that a generic stationary upper bound misses. The support lattice and commensurability are motivated by noise-band resolution; no general dimension or off-lattice claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
