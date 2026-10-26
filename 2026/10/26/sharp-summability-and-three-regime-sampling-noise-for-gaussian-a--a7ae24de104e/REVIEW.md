# Review

## Correctness — PASS

The normalized Gaussian circle restriction is the von Mises density \(\psi_\sigma(x)=e^{2\sigma^{-2}\cos(2\pi x)}/I_0(2\sigma^{-2})\). Squaring and integrating gives the exact Bessel-ratio energy \(E(\sigma)\). Laplace asymptotics establish \(\sigma E(\sigma)\to\sqrt{2\pi}\), while continuity and strict positivity provide two-sided positive bounds for every \(0<\sigma\le1\). Orthogonality of distinct centered coordinates proves the exact additive kernel energy and hence the if-and-only-if fourth-root summability criterion. Dominated convergence, harmonic splitting and an integrable Riemann sum give the sharp three power-weight limits. The Monte Carlo variance identity is exact by independence. Numerical checks only confirm representative finite calculations; the infinite statements are proved analytically.

## Originality — PASS, with residual risk

Sun (2026), *Weight-adapted ANOVA kernels for high-dimensional periodic approximation*, Sections 3–5 and Proposition 5.1, already provides the kernel construction, orthogonal energy formula, and a sufficient dimension-independent upper estimate under weight summability. That established material is not claimed as new. The contribution is necessity for the admissible Gaussian additive family, the \(p=4\) logarithmic transition and exact supercritical/subcritical constants, plus the constant-input sampling lower bound. The author manuscript of Di Marzio–Panzera–Taylor (2011) treats toroidal von Mises density estimation and its risk, not the same truncated additive ANOVA operator. Ebert–Pillichshammer (2021) treats optimal worst-case Korobov information complexity, which does not imply these particular kernel-energy constants. Additional topical record searches yielded no covering implication. A historical or unindexed equivalent remains a genuine residual originality risk; a failed search is not a novelty proof.

## Mathematical value — PASS

The source's upper sampling-noise bound leaves open whether its weight summability requirement is structurally necessary in a natural, explicitly normalized kernel family. This theorem gives a matching necessity test with an exact boundary and distinguishes three asymptotic divergence rates. The critical logarithmic penalty persists for constant target data, so it cannot be attributed to low smoothness of the approximated function. These provide quantitative guidance for how increasing ambient dimension and weight decay change sampling complexity of this specific quasi-interpolant.

## Limits and sources

The kernel is restricted to the Gaussian seed, \(q=1\) singleton interactions, product coordinate weights, and the source's adaptive bandwidths. There is no asserted lower bound for every approximation method, and no independent assessment. Main references: Sun, arXiv:2610.19409v1; Di Marzio–Panzera–Taylor (2011), author manuscript at https://eprints.whiterose.ac.uk/id/eprint/42947/8/taylorcc1.pdf; Ebert–Pillichshammer, arXiv:2102.01449v2.

Self-review: passed. Independent audit: not yet performed.
