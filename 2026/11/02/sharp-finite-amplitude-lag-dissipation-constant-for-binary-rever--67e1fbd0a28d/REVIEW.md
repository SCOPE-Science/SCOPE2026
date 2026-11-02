# Scientific assessment: sharp binary lag–dissipation constant

## Correctness — PASS

For every positive pair of transition rates and every interior instantaneous distribution, the entropy production is exactly \(s(x-q)[\operatorname{logit}(x)-\operatorname{logit}(q)]\). Dividing squared lag by this rate reduces the sharp constant to the maximum of a positive log-odds secant quotient. The derivative numerator and its sign are derived explicitly in the proof: when \(q<1/2\) the quotient increases to one unique root beyond \(1/2\) and decreases thereafter, with both endpoint limits zero. State reflection and the pointwise bound \(h'\ge4\) cover the other cases. The exact rare-output root equation yields the asserted \(L+\log L\) expansion by monotone bracketing. The standard two-state semigroup proves the memory normalization. The standalone checker performed 96,157 deterministic assertions, including optimizer equality and a dense parameter grid. Such finite checks do not certify the continuous domain: that is the role of the analytical proof.

## Originality — PASS (qualified, best-knowledge)

Chen and Limmer's 2026 paper gives the reversible-generator dissipation identity, the small-lag correlation-time bound, and an all-amplitude nonsharp log-Sobolev bound. Its main and supporting relevant derivations have been examined. Its small-lag coefficient agrees with the equilibrium limit here; it is **not asserted** to be a global coefficient in that source. The present claim instead optimizes the precise binary squared-lag/entropy-production ratio over all distributions, identifies a unique biased nontrivial equality state, and gives sharp rare-equilibrium asymptotics. The classical exact two-state logarithmic Sobolev time in Aldous–Fill uses an entropy-versus-Dirichlet quotient, not this observable quotient. Bibliographic examinations of further entropy-dissipation sources have not identified this exact three-part theorem. Full exhaustive priority is not established: the result might be a corollary of an unexamined general nonlinear two-point functional inequality.

## Value — PASS

The optimal finite-amplitude constant is a natural, experimentally interpretable thermodynamic performance parameter for a binary-output Markov network. It shows exactly how much the equilibrium autocorrelation coefficient underestimates possible large-deviation lag at fixed entropy-production rate. The unique equality distribution makes the bound attainably sharp for every biased equilibrium; the logarithmically corrected rare-output law gives an analytically nontrivial scale, rather than a numerically selected special case. This is a motivated structural refinement of the recent computational thermodynamics result, not a renaming of the author's existing small-lag inequality or a generic textbook comparison.

## Closest literature and limitations

Primary comparison: Songela W. Chen and David T. Limmer, *Entropy Production Bounds the Accuracy of Computation in Markov Networks*, arXiv:2608.23764v1, main text equations (11)–(18), Supporting Material I–II. The source's exact modified log-Sobolev bound is general and nonsharp for the present objective; the susceptibility bound is a near-equilibrium statement. Classic exact two-state log-Sobolev optimization: Aldous and Fill, Chapter 8, Example 8.28; its optimized functional differs. Diaconis–Saloff-Coste (1996) and general entropy-dissipation literature remain possible sources of implicit broader coverage and are not claimed exhaustively excluded.

The theorem does not extend to arbitrary state spaces or input trajectories, and no independent mathematical or publication-priority audit has been performed.

Self-review: passed. Independent audit: not yet performed.
