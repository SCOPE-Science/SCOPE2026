# Self-review

## Correctness

**PASS.** The statement is about zeros of the explicit first-order Melnikov function, rather than finite-perturbation global dynamics. The proof conditions on the independent Gaussian offset, computes the one-harmonic crossing probability exactly by a Rayleigh integral, bounds the entire higher-harmonic tail in expected supremum norm, and controls the number of critical points by explicit first- and second-derivative inequalities. The two key error estimates hold uniformly over every finite harmonic cutoff. The Rayleigh integral and two geometric-series identities were replayed with the included standalone verifier. No finite experiment is used as proof.

## Originality

**PASS under the inspected evidence.** Ittayem–Lundberg, arXiv:2610.33620v1, supplies the Melnikov formula, an exact *expected number* of roots, and an upper bound for the *probability* of any roots at high frequency. Their displayed high-frequency proof already contains the same exponential rate and a polynomial prefactor; neither that rate nor the first-harmonic formula is claimed as new. The probability prefactor for arbitrary, possibly frequency-growing degree and the proof that the events with four or more roots are lower-order are additional statements. The general effective zero bound of Benditkis–Novikov concerns different perturbations and does not compute Gaussian probabilities. Some older probabilistic perturbation literature was visible only through abstracts/previews, and a broader general theorem could imply this special result. These are genuine priority limitations, not mathematical exceptions.

## Value

**PASS.** The question addressed in the motivating work is the probability of observing homoclinic splitting when the forcing frequency is high. Knowing the mean zero count, or only an exponential upper bound, does not distinguish a sparse population of two-crossing realizations from a population with many crossings. The theorem identifies the sharp event probability with its leading constant and proves that the event is asymptotically comprised of exactly two simple crossings. Its uniformity in degree means adding arbitrarily many Gaussian forcing harmonics cannot change this rare-event leading law, a structurally useful conclusion for Fourier-truncated random forcing.

## Closest literature and limits

- A. Ittayem and E. Lundberg, *Zeros of Melnikov functions for periodically perturbed Hamiltonian systems with random coefficients*, arXiv:2610.33620v1 (2026), Theorems 2.1, 3.1 and 4.1. Directly provides the model and all normalization factors, but not the claimed all-degree two-zero probability law.
- S. Benditkis and D. Novikov, *On the number of zeros of Melnikov functions*, Ann. Fac. Sci. Toulouse 20 (2011), 465–491. Effective general upper bound, not Gaussian sampling or a sharp high-frequency probability.

The proof does not provide a uniform perturbation size in the full Duffing flow, classify all separatrix intersections, or certify historical priority. Exactly two always means first-order Melnikov phase roots.

Self-review: passed. Independent audit: not yet performed.
