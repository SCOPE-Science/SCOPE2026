# Scientific review

## Correctness — PASS
The claim has explicit stationary SDE and jump generator conventions, exact mixed-moment linear systems, exact two-time Markov semigroup formulas, positive short-lag derivative and an algebraically reconstructed leading-residue formula. The quartic Routh–Hurwitz inequalities place every cubic generator eigenvalue strictly left of the slow linear eigenvalue; a unique-root Descartes certificate and denominator signs complete the global classification. The provided `verify.py` rechecks these identities directly. The result asserts eventual negative sign only above the strict threshold, and explicitly leaves the critical cancellation and possible intermediate-lag behavior unresolved.

## Originality — PASS (qualified best-knowledge)
The primary model source, Santra–Das (arXiv:2603.17027v1, full accessible sections II–III, appendix A), computes one-time second and fourth moments, kurtosis and stationary distributions, not the claimed fourth-order two-time time-antisymmetric correlation or slow-mode sign boundary. Biswas–Dubbeldam–Sandev–Pal (arXiv:2412.09260; *Chaos* 35, 031102) instead use renewal bath-memory resetting and focus on variance and ordinary correlation, not this probe-only-reset fourth-order boundary. Further published-result semantic searches and accessible prior-claim checks found no directly dominating assertion. The older related paper's full text could not be retrieved; broader generic nonequilibrium fourth-order-correlation literature might cover a derivation implicitly. Neither absence from search results nor partition ownership proves global uniqueness.

## Value — PASS
A fourth-order time-antisymmetric observable measures irreversible temporal ordering invisible to one-time marginals and ordinary symmetric autocovariance. The exact finite bath ratio separates opposite signs of the slowest observable mode; in the slow-bath region, a sign change is forced with no inertia, directly distinguishing the nonrenewal bath memory mechanism. The classification uses a nontrivial spectral separation and global algebraic root argument, rather than merely evaluating a known stationary kurtosis.

## Sources and limitations
Santra and Das, arXiv:2603.17027v1 (17 March 2026), full HTML model and moment sections; Biswas et al., arXiv:2412.09260 and *Chaos* 35 (2025), 031102 (abstract, methods and institutional repository listing); Sokolov, *Phys. Rev. Lett.* 130 (2023), 067101 (abstract, resetting FDR). The new claim is for reset rate one, all \(\gamma>0\); no finite-lag all-parameter sign classification below threshold or independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
