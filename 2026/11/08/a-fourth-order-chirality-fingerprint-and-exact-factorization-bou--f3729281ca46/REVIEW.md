# Scientific review

## Correctness — PASS
The model is a stationary four-direction chain with clockwise and counterclockwise jump rates and a stable isotropic harmonic filter. The polynomial generator identity gives exact moments through degree four; the complex-moment calculation independently establishes the signed mixed fourth moment. The thermal contribution is an independent isotropic Ornstein--Uhlenbeck Gaussian, so its independent coordinates cannot change either connected mixed fourth quantity. The sign and if-and-only-if factorization statements follow from strictly positive denominators and independence of rotated signs at equal rates. The extracted standard-library checker passes 1024 deterministic assertions. The analytical proof, not the finite checks, establishes the theorem.

## Originality — PASS, with limitations
Smith, Le Doussal, Majumdar and Schehr (arXiv:2207.10445) establish the **equal-rate** stationary product law. Mallikarjun and Pal (arXiv:2209.05912) treat the biased four-state walker **without a trap**, including free-displacement fourth moments. Loewe and collaborators (arXiv:2305.03663) and Olsen and Löwen (arXiv:2405.14326) analyze tumble-turn or chiral free transport. Sun, Ye and Podgornik (arXiv:2409.00578) give a general harmonic moment scheme with independently sampled new run directions rather than correlated quarter-turn transitions. An earlier related mathematical record also concerns free-space projected fourth-cumulant growth. None of those inspected claims states or directly implies this precise trapped, thermal-noise-invariant fourth-moment formula and exact iff product boundary. Nevertheless, a not-yet-identified calculation in the broader active-matter or Markov-modulated OU literature could precede it; novelty is not independently certified.

## Mathematical value — PASS
The previously exploited separation into two independent 1D trapped run-and-tumble problems has a complete and strict symmetry boundary. Stationary covariance and every polynomial of degree at most three are blind to chirality handedness, but the mixed degree-four moment detects its sign with a closed-form coefficient even under independent isotropic thermal noise. This provides both a structural integrability obstruction and a motivated static observable of chiral dynamics, with no need to observe paths or stationary probability currents.

## Limitations
The exact classification uses homogeneous quarter-turn rates, a positive isotropic harmonic trap, cardinal active velocities and independent isotropic thermal diffusion. The value of a fourth moment does not itself guarantee feasible finite-sample handedness estimation. Analytical and numerical verification have been performed within one mathematical review; independent verification and priority review remain absent.

Self-review: passed. Independent audit: not yet performed.
