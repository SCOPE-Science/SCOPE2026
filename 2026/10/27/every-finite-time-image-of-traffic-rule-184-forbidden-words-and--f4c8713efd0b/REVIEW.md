# Review of the Rule 184 finite-time image theorem

## Correctness

PASS. The proof reconstructs the binary configuration from parity-constrained equal-symbol bonds and verifies their exact local velocity and annihilation law. The forward and reverse constructions establish the same complete finite-time image for every nonnegative time, not just for finite rings. Cross-bifix-free forbidden words give the exact recurrence and generating function. The algebraic Perron-root equation follows by factoring the denominator, and the entropy limit and sharp coefficient follow by a controlled root expansion. `verify.py` passed 16 complete local transitions, 80 independent finite-language enumerations, 20,782 finite-ring lift cases and numerical root checks. These finite tests support but do not substitute for the unrestricted proof.

## Originality

PASS under the accessed primary literature; historical priority remains provisional. Fukś (arXiv:math/9904182) derives arbitrary-time traffic flow and the special preimage language for zero blocks, not an evaluated whole-image forbidden basis or its entropy. Hellouin de Menibus and Sablik (arXiv:1602.06093) establish the two-species particle factor and asymptotic measure-dependent information, but do not state the reverse-lifting characterization of every image or the generating-function and sharp entropy-relaxation law. Belitsky and Ferrari (1995, 2005) are plausible earlier covering sources, but only abstracts were accessible; none of their accessible claims resolves the exact finite-time comparison. Literature searching and comparison with existing local research claims did not identify this specific theorem. The particle law itself is prior knowledge, not a novelty claim.

## Mathematical value

PASS. Entire iterated image languages and their convergence to the limit set are natural global symbolic-dynamics invariants for a classical conservative cellular automaton. A single exact all-time forbidden-word family controls every finite-time SFT, proves strict nonstabilization, and yields a closed word-count series and a sharp golden-ratio entropy-relaxation constant. This is not a one-rule one-time count or an incidental numerical value. It does not claim the original ballistic-particle interpretation or probabilistic mixing results.

## Sources and limits

Primary sources inspected: Fukś (1999), arXiv:math/9904182, particularly the preimage and flow results; Hellouin de Menibus and Sablik (2016), arXiv:1602.06093, especially the Rule-184 particle factor and measure-asymptotic applications. Historical-priority risks: the full Belitsky–Ferrari 2005 and 1995 papers were inaccessible. No external validation or independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
