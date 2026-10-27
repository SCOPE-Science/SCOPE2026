# Scientific review

## Correctness — PASS

The claim is a joint random-centered, two-scale limit. Independent Poisson splitting and conditioning on the maximum first-arrival time give an exact binomial conditional law. The centered conditional binomial characteristic functions converge uniformly for bounded Gumbel offsets; tightness transfers this to the joint Gaussian scale. The continuous-time cover differs from the observed draw count divided by the number of coupons by a mean-square error \(H_n/n\), small enough even after multiplication by \(\log n\). The observable pivot follows by a continuous mapping. The packaged independent finite-state checker verifies exact finite moment consequences through fourteen coupon types. Infinite weak convergence rests on the proof, not computation.

## Originality — PASS (historical priority uncertain)

Myers--Wilf (2003) **already determines the entire finite joint law** of terminal singleton count and discrete cover time, and Ilienko (2020 preprint; 2026 publication) **already determines the first-order exponential singleton limit** by point-process methods. These are explicitly excluded from the novelty claim. Mahmoud--Smythe (2012) and Betken--Thäle (2022 preprint) prove related fixed-time occupancy central limit theorems. The inspected main theorems and relevant proofs do not supply the second-order Gaussian fluctuations **after the observed random completion-time center is removed**, nor the joint asymptotic independence of the resulting pivot and Gumbel time. This last claim requires a separate conditional-binomial expansion and a sufficiently sharp depoissonization estimate. Residual risk: an unlocated general or older theorem might imply this specialization; an exact finite joint law is sufficient to derive the result with additional asymptotic analysis, but does not itself state or immediately settle that analysis.

## Value — PASS

At coupon completion the fluctuation of singleton abundance of order \(\log n\) is entirely controlled by the random extreme completion time. The theorem identifies the next, \(\sqrt{\log n}\), fluctuation scale and yields an observable, asymptotically normal pivot that is independent of the cover-time extreme. It resolves a natural conditional uncertainty left open by the known first-order exponential law and is useful for refined diagnostics of occupancy models.

## Scope and residual risks

Only iid equally likely coupon labels, the first complete collection, and weak-convergence asymptotics are proved. No independent mathematical audit has been performed. Possible historical equivalence with broader fluctuation results remains to be checked by an independent specialist.

Self-review: passed. Independent audit: not yet performed.
