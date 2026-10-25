# Independent mathematical audit

## correctness

PASS

The exact k-discordant-leaf generator has transitions k->k-1 at rate k and k->n-k at rate ck/n (including null transitions for n even). Telescoping the backward equations sum_{k=1}^n[(tau_k-tau_{k-1})+(c/n)(tau_k-tau_{n-k})]=H_n to obtain tau_n=nH_n/(n+c); the k=n row gives tau_{n-1}=H_{n-1}, the k=1 row yields tau_1. The weighted opinion martingale sum_v(deg(v)/rate(v)) eta_v establishes fixation; bounded stopping is valid on a finite absorbing chain. Exact independent matrix inversion of the n-state chain for n=2..6, c=1/3,3/2,4,n+2 reproduced both time formulas. Only the backward-equation and martingale proofs justify arbitrary n and c; no extrapolation from examples.

## originality

PASS

The classical heterogeneous voter and standard star results establish the martingale or homogeneous star fixation, but the inspected primary results do not give the exact variable-center-rate star time crossover or its separation from fixation threshold. The final claim specializes nontrivially to this location-weighted chain rather than replacing a known general formula by a name change.

## value

PASS

The two natural observables—fixation probability and mean consensus duration—order central and peripheral initial dissent differently on an explicit nonempty parameter window. The sharp n-dependent boundary, exact invariant tau_{n-1}, and n/log n window width are meaningful structural properties of the canonical heterogeneous-update voter star, not a generic one-line substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
