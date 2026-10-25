# Scientific review

## Correctness — PASS

For the explicitly stated noninteracting Rabi Hamiltonian and full global Poisson reset, the stationary reset age is exponential and the conditioned spin outcomes are binomial. The exact probability generating function follows directly. Under the rescaling \(\gamma_N=c_N\Omega\sqrt N\), the conditional binomial intensity converges to \(E^2/c^2\), and dominated convergence yields the mixed-Poisson law. A uniform sine bound and conditional variance establish the two off-critical regimes, including the stated \(L^2\) coupling. Explicit factorial moments give the variance and Fano factor; a Poisson Chernoff sandwich establishes the sharp stretched-exponential log-tail. Independent-clock resets yield an ordinary binomial and hence Poisson law. All formulas were reconstructed independently and 132 numerical checks passed. The results require stationary preparation before each growing-\(N\) limit and fixed \(\Omega,\Delta\).

## Originality — PASS, subject to independent priority assessment

Magoni et al., arXiv:2202.12655, Protocol I equations (1)–(4), give the same spin model, fixed-rate renewal steady state, stationary mean and pair covariance; they are explicitly credited, not represented as new. Its supplement discusses finite-size excitation readout for conditional reset. The inspected main text and supplement do not give a simultaneous \(\gamma_N\propto\sqrt N\) unconditional-reset spin-count limit, its factorial moments, or its stretched-exponential tail. Perfetto et al. arXiv:2106.13761 give a broader quantum reset-renewal framework, not the evaluated mesoscopic law. Mukherjee et al. arXiv:1806.00019 address quantum resetting and Zeno at fixed system scale; Rose et al. arXiv:1806.01298 address general reset spectra. Carollo et al. arXiv:2310.06981 study ordering probabilities of quantum-jump observables. All are relevant methodological background but none of the inspected claims dominates the evaluated two-clock mesoscopic count comparison. The mixed-binomial Poisson limit uses standard probability approximation; the contribution is the nontrivial physical scaling and its evaluated limit, not the generic convergence method. A wider undiscovered specialization remains a priority risk; independent audit has not been performed.

## Scientific value — PASS

The square-root-many-spin reset scaling is the natural boundary at which a finite number of excited spins survives the large-system limit. At that boundary the global reset clock generates a mixed-Poisson fluctuation law (Fano factor strictly above one) and stretched-exponential tails, whereas independent clocks with exactly the same single-spin stationary probability give an ordinary Poisson law. This quantitatively distinguishes mesoscopic burstiness caused exclusively by synchronized intervention and complements the established fixed-rate thermodynamic correlation divergence. The exact crossover is not a cosmetic restatement of a fixed-parameter mean: it controls a distinct point-process-scale observable and resolves its limiting count statistics.

## Limitations and priority risk

The external clock is Poisson, common to all spins, and independent of the coherent dynamics. Detuning is fixed. No resetting costs, interactions, or time-uniform convergence are addressed. A generic conditional-binomial mixture theorem could contain the probability limit as an unstated corollary; the literature search is evidence, not proof of uniqueness. Independent scholarly review is still required.

Self-review: passed. Independent audit: not yet performed.
