# Self-review

## Correctness — PASS

For any independent centered Gaussian numerator factor, conditioning on all other factors produces a strictly decreasing positive-half-axis Gaussian mixture; the mixing scale is almost surely positive. With no numerator, reciprocal-product inversion and exponential tilting give the exact positive density as a rescaled logarithmic-Rayleigh convolution. Strict log-concavity plus analyticity gives one and only one positive mode, and symmetry gives the second. The Mellin-gamma characteristic function admits exponentially decaying Fourier inversion; expanding the derivative at the tilted-sum mean gives the shift of \(3\zeta(3)/\pi^2\) with \(O(N^{-1})\) remainder. The strong law for \(\log|G|\) gives the exponential typical-size separation. The package checker verifies the one- and two-factor special cases, Fourier derivative signs and finite large-factor behavior. These checks cannot establish the all-factor theorem by themselves; the proof supplies that quantifier.

## Originality — PASS with priority risk

Gaunt–Sutcliffe (arXiv:2601.12997v1, Section 2.2 and Remark 2.10) derive the ratio density and distinguish origin-unimodal from non-unimodal regimes. The qualitative split, Meijer-G formulas and normal-product laws are existing results and are not separately claimed. The primary paper's non-unimodality statement does not imply exactly two off-origin modes or the moving-factor displacement. Salo–El-Sallabi–Vainikainen (DOI:10.1109/TAP.2005.863087) derive finite Rayleigh-product densities without the asymptotic reciprocal-Gaussian mode or contrast with the typical observation. Standard log-concavity and Fourier asymptotics are acknowledged as proof techniques, not novel general theorems. Related historical product-normal work was available only in bibliographic/abstract form; it is a residual priority risk, as is any unindexed specialized modal theorem.

## Value — PASS

The number and positions of density modes are natural, identifiable shape statistics of the source's probability model. This is not a reparameterization or a numerical optimum alone: it provides a complete global two-mode classification in the all-denominator family, an analytic finite-dimensional characterization for every number of factors, a sharp large-factor location with a non-Gaussian zeta correction, and a surprising separation of an exponentially vanishing modal location from exponentially growing typical values. Those statements inform interpretation of mode-based summaries in heavy-tailed multiplicative models, without claiming downstream risk guarantees.

## Closest literature and limitations

Primary paper: R. E. Gaunt and H. L. Sutcliffe, arXiv:2601.12997v1 (2026), and *Metrika*, DOI:10.1007/s00184-026-01045-2; inspected Sections 2–3 and appendices. Rayleigh antecedent: J. Salo, H. M. El-Sallabi and P. Vainikainen, IEEE TAP (2006), DOI:10.1109/TAP.2005.863087; its product-density construction was inspected. Historical source: Springer and Thompson, SIAM J. Appl. Math. (1970), DOI:10.1137/0118065; bibliographic/abstract evidence only. The source already states the qualitative modality distinction; this contribution is narrower. The comparison cannot rule out all uncatalogued equivalences. No claims are made outside independent centered Gaussian factors or outside the stated number-of-factors asymptotics.

Self-review: passed. Independent audit: not yet performed.
