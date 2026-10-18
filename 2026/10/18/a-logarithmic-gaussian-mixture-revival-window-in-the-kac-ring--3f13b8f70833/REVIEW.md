# Scientific review: Kac-ring logarithmic revival

## Correctness — PASS

The mathematical statement is an annealed-over-static-disorder limit, with fully aligned deterministic initial spins and \(0<p<1/2\). The exact half-recurrence identity reduces the magnetization magnitude to an average of overlapping \(k\)-fold Bernoulli sign products. Direct interval-overlap counting gives the finite variance; a block-separation Lindeberg argument gives the Gaussian law for growing \(k=O(\log N)\). A distinct sparse-coordinate characteristic-function argument proves asymptotic independence of the global flipper parity and the centered Gaussian. This independence is essential for the *symmetric mixture*, and cannot be inferred from variance alone. Exact weighted enumeration on rings up to 12 sites and a seeded large-ring moment test corroborate the finite formulas and mixture variance. The limiting distribution is proved analytically, not by simulation.

## Originality — PASS, subject to bibliographic limitations

Gottwald–Oliver (2009) already derive the relevant finite second-moment law, including its half-recurrence complement, so that formula is not claimed as new. Hiura's 2021 macroscopic-fluctuation theorem uses a fixed observation horizon as system size increases; its full text expressly sets recurrence aside. Neither examined full text contains the present logarithmic backward-window central limit theorem or the global-parity-independent two-Gaussian law. Searches for the model, equivalent formulations involving sliding Bernoulli products, and finite-size recurrence Gaussian mixtures did not locate that statement. Chandrasekaran–Jain (2012), on entropy and recurrence of statistical fluctuations, is a plausible additional comparison, but the publisher's full text was not accessible; its abstract does not establish whether the precise critical-window law is included. This is a material residual originality risk, not a claim of proven worldwide uniqueness.

## Value — PASS

This identifies the exact \(\log N\) time scale separating finite-size noise from the emerging macroscopic revival in a canonical reversible model of apparent thermodynamic relaxation. The crossover profile is not merely a new moment: for nonzero shift it is a genuinely non-Gaussian symmetric mixture produced by a global parity variable. This sharp distributional resolution complements the classical moment and recurrence descriptions and supplies a finite-size benchmark for distinguishing random fluctuations from true recurrence in trajectories.

## Limits of review

Only the new stated theorem was evaluated. The proof covers fixed Bernoulli flipper density strictly between zero and one-half, a fully aligned initial spin word, and logarithmic backward windows. It does not give Berry–Esseen bounds, dynamically refreshed disorder, or a general initial-magnetization classification. The full-text access limitation for the 2012 recurrence paper remains unresolved.

Self-review: passed. Independent audit: not yet performed.
