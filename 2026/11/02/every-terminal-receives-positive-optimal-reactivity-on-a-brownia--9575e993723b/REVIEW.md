# Independent mathematical audit

## correctness

PASS

For m≥3 compact arms ℓ_i>0, D>0 and budget Σκ_i=K>0, solve D u_i″=−1, Kirchhoff Σu_i′(0)=0 and Robin u_i′(ℓ_i)=−(κ_i/D)u_i(ℓ_i). The central lifetime is U=A(r)/(D B(r)), A=Σℓ_i(1+r_iℓ_i/2)/(1+r_iℓ_i), B=Σr_i/(1+r_iℓ_i)>0, r_i=κ_i/D, Σr_i=K/D=R. Setting V*=min A/B, h_i′(r)=−(ℓ_i²/2+V*)/(1+rℓ_i)² and h_i″(r)>0 makes A−V*B strictly convex on the compact simplex; hence unique minimizer. An inactive leaf would force active marginal λ≥ℓ_j²/2+V*>V*, which yields r_i≤ℓ_i/(4V*) for all i. But V*≥Σℓ_i/(2R) gives R≤Σℓ_i/(4V*)≤R/2, contradiction. Therefore all reactivities positive and KKT characterizes the unique optimum. Independently checked 48 heterogeneous SLSQP numerical cases for positive optimizers; not an infinite proof.

## originality

PASS

Best-of-knowledge originality of the final exact statement, with actual published-result comparisons rather than title matching; no inspected source mathematically implies the full stated result. Inaccessible closely related texts are explicitly retained as priority risks; failed search is not novelty proof.

## value

PASS

Uniform strict-interiority and uniqueness for an allocation problem on arbitrary heterogeneous multi-arm diffusion networks is a motivated global optimization theorem, excluding an intuitively plausible strategy of shutting off distant leaves. Exact KKT equations give actionable design characterization, not merely a local numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
