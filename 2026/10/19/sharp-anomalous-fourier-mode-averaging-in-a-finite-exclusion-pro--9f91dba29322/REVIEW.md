# Scientific assessment

## Correctness

**PASS.** The first sine density observable is an exact nonzero eigenmode of the finite-ring exclusion generator with eigenvalue \(-4\sin^2(\pi/L)\). Its stationary conditional mean given the reset clock is the exponential of minus the age times this eigenvalue. The total covariance decomposition isolates a conditional SEP contribution bounded exponentially in the lag. The other contribution has an exact two-path renewal equation. The standard second-order renewal-function expansion supplies its integrated asymptotic, with constants calculated from the exact Pareto tail. Stationarity and the covariance-to-integrated-variance identity yield the two nonstandard growth laws. When the second waiting-time moment is finite, standard iid-cycle reward variance theory gives the finite positive linear coefficient; stationary boundary segments contribute sublinear variance. The executable independent checks include 1329 assertions but are not offered as infinite-time proofs.

## Originality

**PASS under the inspected comparison; independent priority remains unassessed.** Mishra and Basu (arXiv:2211.14120, sections 2–6 and appendices) develop exactly this resetting model and its stationary density profile and current statistics. The stationary Fourier-mode mean is therefore known through their results, whereas the variance growth of the stationary *time-integrated* mode, with its exact finite-size constants and logarithmic boundary, is not established by the material inspected. Sadekar and Basu (arXiv:2004.00951, section 5.4) study temporal site correlations under memoryless dichotomous resetting, where the clock is different. Basu, Kundu and Pal (arXiv:1906.11801) treat exponential resets. Doney (arXiv:1909.11458, equation (3)) supplies the classical second-order renewal theorem used as an ingredient. Broad renewal-reward and long-memory theory could have an equivalent specialization; a negative search is not a proof of absolute novelty.

## Value

**PASS.** The slowest nonconstant spatial Fourier density mode is a natural observable of relaxation to the nonuniform reset profile. Its long-horizon time average is experimentally and mathematically distinct from the previously calculated static density and bond currents. The rigorous growth-phase diagram demonstrates that global heavy-tailed reset timing produces superlinear variance at *every fixed finite size*, despite fast internal mixing, and provides sharp measurable amplitudes plus a nontrivial logarithmic critical boundary. The theorem does not purport to extend to arbitrary modes, power-law-reset exponents with infinite mean, or a joint size–time limit.

## Risks and limits

The claim assumes exactly Pareto-distributed independent reset interarrivals, a deterministic half-ring reset configuration, complete rebuilding of the SEP state at each renewal, the stationary equilibrium clock, and fixed finite even ring size. The renewal theorem is not reproved. A sufficiently general already-published theorem about finite-state regenerative observables could imply the variance trichotomy; subject-specific and general literature comparisons do not remove that residual priority risk. No independent scholarly audit has occurred.

Self-review: passed. Independent audit: not yet performed.
