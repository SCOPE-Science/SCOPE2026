# Scientific review: logarithmic condensation threshold and nested fitness-gap laws

## Correctness — PASS

The result starts from the established exact stationary formula (Grange 2023, Section 5, equations 41–44), and derives a normalized decomposition with positive weights. The endpoint condition \(q(1-u)=O(u^\alpha)\) ensures the background integral converges; the strict bound \(\beta J_0<1\) ensures every stationary normalization is valid. An exact logarithmic substitution reduces the singular component to an integral with comparison kernel \([1+c s^\theta]^{-1}\), giving all four infinite-density regimes and the finite-density side. Ratios of restricted integrals give the beta/uniform scaling laws, including the second logarithm at \(\theta=1\). Positivity, boundary cases and parameter domains are explicit. An independent quadrature checker passed 46 deterministic checks; the analytic proof, not the finite checker, justifies all asymptotic assertions.

## Originality — PASS, qualified

The 2023 primary text supplies the entire forward stationary mean equation and addresses the three pure-power cases. Its Sections 5.2.1–5.2.3 assume \(r(1-u)\sim cu^\nu\), not \(cu[\log(1/u)]^\theta\) with nonzero \(\theta\), and do not present the \(\theta=1\) second transition or fitness-gap distributional limits. Earlier nonresetting and globally resetting processes are different physical protocols. Separate searches of publication literature and archived mathematical findings for equivalent rates, condensate boundaries, beta laws and nested logarithmic coordinate limits did not identify a prior statement entailing this precise combined theorem. An unstated regular-variation corollary or unindexed specialty work remains a risk. The original general mean formula, logarithmic asymptotic tools, and classic Kingman condensation are not claimed as original.

## Mathematical value — PASS

At the physically marginal linear-reset boundary the algebraic power alone cannot distinguish a finite-density phase from a condensed phase. The exact threshold at logarithmic exponent \(\theta=1\) repairs this classification, while the beta and double-logarithmic uniform limits quantify how near-maximal fitness particles distribute over exponentially nested gaps. The full result is a natural structured phase diagram for a motivated existing interacting-particle model, not an arbitrary chosen moment or trivial parameter substitution.

## Closest sources and residual limitations

P. Grange, arXiv:2311.12414 (Sections 5.1–5.2, equations 41–66); P. Grange, arXiv:1904.05604 and 1910.05991 (different no-reset/global-reset mechanisms); L. Yuan, arXiv:2001.07033 (random mutation rather than local reset rates). The theorem is restricted to mean-field stationary population profiles and asymptotically equivalent logarithmic-rate families. A broader published theorem may still cover these consequences; independent expert priority review is outstanding.

Self-review: passed. Independent audit: not yet performed.
