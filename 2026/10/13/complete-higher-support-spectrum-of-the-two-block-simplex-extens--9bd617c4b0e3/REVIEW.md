# Review: Complete higher-support spectrum of the two-block simplex extension

## Correctness
PASS. The proof reduces every \(r\)-subcode to an \(r\)-subspace \(U\le\mathbb F_2^m\). The simplex part always contributes \(2^m-2^{m-r}\) coordinates because the omitted nonzero columns are exactly \(U^\perp\setminus\{0\}\). The appended blocks are controlled by the two independent linear functionals \(a_1+a_2\) and \(a_1\), so the four multiplicities follow from Gaussian-binomial counting in two hyperplanes and their codimension-two intersection. Exhaustive enumeration for the source examples \((3,6,2)\) and \((4,10,4)\) agrees exactly with both the formula and the published \(r=1\) weight distributions.

## Originality
PASS. The closest source, Li--Chen--Jin--Qu Theorem 6.6/Table VIII, determines only ordinary codeword weights. Qiao--Du and Meng--Liu--Liu--Wang--Zheng determine generalized weights for different defining-set families. Searches for the source title together with “generalized Hamming weights,” “weight hierarchy,” “support spectrum,” and “simplex appended blocks” did not locate the claimed two-hyperplane spectrum or its hierarchy. A previously published systematic-simplex hierarchy concerns \([I_m\mid S_2(m)]\), whose appended block comprises \(m\) independent coordinate functionals rather than two repeated functionals, so it does not imply this result.

## Value
PASS. Generalized Hamming weights and full subcode-support spectra are natural structural invariants used in wiretap, erasure, and trellis questions. The result upgrades a newly published four-weight construction from its one-dimensional spectrum to every subcode dimension, in closed form for the entire infinite family. The qualitative consequence—that all weights through \(r=m-2\) remain exactly simplex-like and only the top two levels change—is a structural boundary not visible from the ordinary weight enumerator.

## Closest literature and limitations
The classical simplex hierarchy supplies the base term but not the effect of the appended repeated coordinates. The 2025 Qiao--Du and 2026 Meng--Liu--Liu--Wang--Zheng papers demonstrate that higher-weight analysis of few-weight and self-orthogonal codes is an active, nontrivial problem, but their defining-set constructions are different. The theorem here is intentionally limited to Theorem 6.6's two-block extension and does not claim a general classification of simplex extensions.

Self-review: passed. Independent audit: not yet performed.
