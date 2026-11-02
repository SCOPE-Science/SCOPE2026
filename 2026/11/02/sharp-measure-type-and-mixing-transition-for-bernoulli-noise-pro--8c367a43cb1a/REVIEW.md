# Scientific review

## Correctness — PASS

Every update map is a global contraction with constant \(q=1-ah\), giving a unique invariant measure. Endpoint images show a sharp union-versus-gap threshold at \(q=1/2\). For \(q<1/2\), the maps restrict to a strongly separated affine self-similar pair, yielding the Cantor law and standard dimension. At equality, their half-interval images preserve uniform Lebesgue measure. For \(q>1/2\), interval coverage and arbitrarily small cylinder diameters let a finite word force every starting point into the soft-threshold plateau, followed by a zero-reset step. This supplies a uniform Doeblin minorization, geometric total-variation mixing, and a stationary measure concentrated on the countable forward orbit of zero; density of that orbit and positivity of all its atoms follow. Exact rational checks of 18 parameter cases and a five-step reset illustrate, but do not replace, the proof. The rigorous result is confined to the specified scalar model.

## Originality — PASS, qualified

The motivating proximal stochastic-gradient support-identification study (Dai et al., arXiv:2302.06790v1) uses a variance-reduced estimator, not the fixed independent two-point persistent noise whose invariant law is classified here. The constant-step random forward–backward study (Bianchi et al., arXiv:1702.04144v1) provides general invariant-measure theory rather than this exact atomic/continuous/Cantor and total-variation transition. Sun et al. (AISTATS 2019) examine manifold identification and persistent gradient error, not this stationary law. Classical Hutchinson self-similar measure theory directly covers the separated Cantor component but not the overlapping nonlinear flat-branch reset and full-support pure-point regime. The closest accessible published mathematical records on scalar composite trust-region updates, deterministic lasso ADMM identification, and noisy signSGD analyze different recurrences and cannot imply this theorem by simple specialization. No direct equivalent was located in the inspected materials. General flat-spot random-IFS literature is a genuine remaining priority risk; searches do not establish global novelty.

## Value — PASS

The result sharply classifies a natural stochastic proximal-gradient scheme that minimizes a sparse strongly convex quadratic with unbiased persistent additive gradient noise. It shows that exact stationary sparsity and total-variation mixing can coexist with dense full-interval support, and that a small change in step crosses into non-atomic invariant laws with maximal finite-time total variation from deterministic starts. These are methodologically meaningful diagnostics beyond second moments or weak convergence, and the transition uses no arbitrary chosen invariant statistic or unmotivated parameter slice.

## Closest literature and limitations

The most relevant primary studies are Dai et al. (2023), Bianchi–Hachem–Salim (2017), Sun et al. (2019), and Hutchinson (1981). The first three do not state this exact phase diagram in the inspected sections and general classical contraction theory covers only background aspects. Direct earlier specialized random-IFS results remain possible. The theorem concerns the exact one-dimensional fixed-step recurrence with independent fair-sign noise; multidimensional, nonquadratic and continuous-noise extrapolations remain unproved.

Self-review: passed. Independent audit: not yet performed.
