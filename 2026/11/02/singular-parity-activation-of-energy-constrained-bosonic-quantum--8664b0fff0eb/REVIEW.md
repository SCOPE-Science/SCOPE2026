# Review: singular parity activation of energy-constrained bosonic quantum communication

## Correctness — PASS

The proof derives the complementary qubit exactly, including its determinant \((1-r)q(1-q)\). The complementary output factors through the bosonic output's number measurement, proving degradability for the discrete noise model without applying an inapplicable continuous-density theorem. Finite-energy entropy bounds justify the energy-constrained coding reduction. Conditioning photon number on parity and maximizing two nonnegative-integer entropies proves the geometric optimizer and the exact one-parameter capacity formula. Concavity of classical–quantum conditional entropy and strict concavity of thermal entropy prove uniqueness. The derivative and integrated entropy expansions yield the stated essential singularity, including its prefactor. `verify.py` passed 382 checks, but its finite tests are only corroboration. The limit is at fixed \(E>0\); no assisted capacity is claimed.

## Originality — PASS (best-knowledge, not independently certified)

The 2026 motivating result gives the general Fock-diagonal characterization under a phase-density hypothesis and explicitly leaves model-specific optimization open. It does not cover the singular two-point phase law as stated or give a parity-sector optimum. The 2023 Lami–Wilde exact formula addresses unconstrained capacities, while the 2020 Arqand–Memarzadeh–Mancini problem concerns Gaussian phase diffusion. The standard degradable coding theorem is appropriately credited to Wilde–Qi. Targeted mathematical-record searches found no exact statement of a geometric distribution in each parity sector together with a nonperturbative \(\exp[-c/r]\) activation law. The remaining priority risk is an older or differently described special case of discrete bosonic phase randomization.

## Value — PASS

The source identifies explicit optimum photon-number distributions for concrete noise as a mathematically motivated outstanding step. The binary \(0/\pi\) phase channel is a natural exactly solvable non-Gaussian boundary case with an infinite-dimensional, finite-energy constraint. Its optimal input is not simply the noiseless even-sector state whenever \(p<1/2\): the unique odd-sector weight becomes exponentially small, exposing an essential singularity invisible to any fixed-order expansion. The exact finite-energy capacity envelope and sharp activation law provide an operational quantitative characterization, not a routine reparametrization of the general capacity theorem.

## Closest literature and risks

- A. Arqand and G. Smith (arXiv:2610.13854v1, 2026): capacity characterization for absolutely continuous phase noise; concrete optimization left open.
- L. Lami and M. M. Wilde (arXiv:2205.05736; Nature Photonics 2023): unconstrained bosonic dephasing capacities, not the finite-energy binary case.
- A. Arqand, L. Memarzadeh and S. Mancini (arXiv:2007.03897; PRA 2020): Gaussian phase-diffusion optimization rather than two-point parity noise.
- M. M. Wilde and H. Qi (arXiv:1609.01997; TIT 2018): pre-existing energy-constrained degradable-channel coding theorem used as background.

No claim is made that this result has passed independent literature-wide priority verification. Strict code constraints, correlated uses, general noise, and two-way assistance lie outside the mathematical scope.

Self-review: passed. Independent audit: not yet performed.
