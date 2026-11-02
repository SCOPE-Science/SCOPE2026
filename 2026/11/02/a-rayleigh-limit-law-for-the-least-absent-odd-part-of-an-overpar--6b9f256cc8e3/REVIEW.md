# Mathematical review

**Claim:** Rayleigh convergence, exact fixed-size survival generating function, and all fixed positive real moment convergence for the first absent odd part of a uniformly chosen overpartition of \(n\), counting either overline state as present.

## Correctness — PASS
The positive-multiplicity overpartition factor is \(2q^j/(1-q^j)\). The exact coefficient identity and independent geometric-plus-Bernoulli representation follow algebraically. The Fourier proof uses a common geometric component to control conditional coefficient extraction for all forced odd sets; the central limit remains unchanged when \(m=O(n^{1/4})\). The exact presence product yields the survival exponent \(-\pi y^2/16\) and its global Gaussian majorant ensures fixed real moment convergence. The executable verifier checks 2394 finite coefficient identities with exact integers; it is explicitly not a proof of the limit.

## Originality — PASS, subject to independent priority review
The most relevant 2026 preprint studies parity-filtered *ordinary* mex, distinct from an odd-restricted search. The 2024 paper defines odd-only mex on overpartitions **into odd parts**, unlike the candidate on the complete overpartition measure. Chern–Xia's moment theorem is for ordinary partitions. Donato addresses ordinary overpartition mex and Bhoria–Eyyunni–Santra count all missing integers. None of their examined theorem statements implies the all-overpartition Rayleigh law. Actual mathematical searches and semantic record comparisons were performed as documented in `AUDIT.json`; possible broader abstract equivalences or unindexed work remain residual risks.

## Mathematical value — PASS
This supplies the full first-order law for a naturally distinguished gap statistic rather than only a summatory mean or a modular identity. All fixed positive real moments, the exact mean \(2n^{1/4}\), the sharp variance constant and the Gaussian-tail uniform integrability are new kinds of information relative to the closest inspected literature. The central probabilistic argument is an explicit, nontrivial fixed-size transfer rather than a finite numerical fit.

## Boundaries
Uniform all-overpartitions of each fixed \(n\), first absent positive odd size, overlined-or-not presence. No claim about overpartitions into odd parts alone, the parity indicator of conventional mex, changing moment exponents, or quantitative convergence rates. Search cannot certify absolute priority and no independent audit was conducted.

Self-review: passed. Independent audit: not yet performed.
