# Scientific assessment: exact star-exclusion evacuation and its crossover

## Correctness — PASS

The rates and initial states are explicit. Symmetry reduces the stochastic exclusion process on the star to a sequence of two-state Markov renewal stages indexed by the number of particles. First-event conditioning gives a quadratic transform factor with no unproved independence assumption: independence follows from the strong Markov property at removal times. Its two positive real spectral rates give an independent-exponential representation and the exact first two moments. A Gamma-product identity yields the Gaussian, Gumbel and finite-convolution limits by uniform Stirling asymptotics and centered characteristic functions.

The standalone checker constructs the transient Markov generator independently, verifies 720 transform and 180 moment comparisons, and numerically probes the three asymptotic regimes. It does not substitute finite testing for the all-size proof. No finite/infinite logical gap was identified within the stated homogeneous-star, exponential-clock assumptions.

## Originality — PASS on the examined evidence, with historical-priority risk

The closest star-specific primary paper is Mottishaw–Waclaw–Evans, *An exclusion process on a tree with constant aggregate hopping rate* (2013, arXiv:1306.0360). Its actual Sections 2 and 5 concern driven, directed TASEP and stationary currents/correlations, not an initial finite population removed by a hub absorber. Meerson–Vilenkin–Krapivsky (2014, arXiv:1406.3502) studies an external target surrounded by spatially extended SSEP and the zero-capture survival probability, not the distribution of complete depletion of a finite star. Hathcock–Strogatz (2021, arXiv:2103.08522) provides important prior general Gaussian/Gumbel absorption-time universality, and its coupon-collector analogy is acknowledged. Their principal birth-death results do not specify the exact two-phase star-renewal transform or the parameter-dependent normal-plus-Gumbel convolution at outward rate proportional to the inverse square root of leaf count.

A semantic search of published relevant mathematical records, a comparison with the accessible preexisting local claim index, and targeted literature queries found no statement dominating the precise combined theorem. This supports originality under available evidence; it does **not** prove priority. Residual risks include older queueing/network-clearing models with algebraically equivalent Laplace products and specialized absorbed-exclusion literature not indexed under these phrases.

## Mathematical value — PASS

The object is a standard interacting-particle transport model with a localized imperfect absorber. Its entire depletion-time distribution is determined exactly for arbitrary initial occupancy, rates, and size. The nontrivial result is not simply a harmonic mean: a reverse-hop rate tending to zero at the exact physical scale \(a/\sqrt N\) produces a continuous convolution of independent Gaussian and Gumbel fluctuations, separating sharply different finite-size universality regimes. The full finite law, exact moments and crossover give reproducible benchmarks for crowded capture, return transport and finite-network extinction experiments.

## Scientific boundaries and reproducibility

The star geometry, homogeneous directed per-edge hopping, single occupancy, initially vacant hub and exponential removal clocks are essential. Extension to heterogeneous leaves, different trapping geometry or arbitrary correlated initial states is not established. The analytic proof is supplied in `RESULT.md`; `check_star.py` and `check_output.txt` contain an independently constructed finite-generator check. An independent audit has not yet been performed.

Self-review: passed. Independent audit: not yet performed.
