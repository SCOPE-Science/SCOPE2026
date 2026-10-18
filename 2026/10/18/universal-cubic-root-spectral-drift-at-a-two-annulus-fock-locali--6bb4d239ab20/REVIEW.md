# Review of a two-annulus Fock spectral threshold

## Correctness — PASS

Direct angular integration gives the Gamma-distribution diagonal entries with the normalization \(1/k!\). A uniform Stirling expansion on the two fixed scaled intervals yields the first-order term \(h=g'+xg''/2+g'''/3\). The positive-axis derivative reduces modality to a strictly increasing hyperbolic-sine quotient. At the supercritical mode, the inequalities \(x_*<a\) and \(0<c\coth(cx_*)-b\coth(bx_*)<2\delta\) prove \(h(x_*)<0\), not just numerically. At criticality, \(g^{(4)}(0)=-24\gamma_\delta\) and \(h'(0)=-8\gamma_\delta\); their competition forces the unique optimizing scaled degree \(-\sqrt[3]{2}\) and the coefficient \(6\sqrt[3]{2}\gamma_\delta\). The proof handles tails and the integer lattice. The supplied checker passed 119 finite corroboration assertions; it is not used to infer infinite convergence.

## Originality — PASS with historical risk

Grudsky–Vasilevski (2002) and Esmeral–Maximenko (2015, Proposition 6.5) already cover radial diagonalization and the leading Gaussian approximation. Oldfield (2014, Theorem 2.4 and Corollary 2.5) covers global localization trace/counting asymptotics under different scaling assumptions. The new statement requires a uniform first-order correction and optimization at a quartic degeneracy. None of those inspected primary results supplies the cubic-root displacement or strict negative-branch preference. The relationship to broad Edgeworth expansions has been acknowledged, and alternative-language historical coverage remains possible; an independent literature audit is needed.

## Value — PASS

Spectral norm alone does not reveal which monomial degree realizes maximal localization. At the exact parameter where two spectral peaks fuse, an ordinary Gaussian limit cannot resolve this index; the theorem computes its universal \(N^{1/3}\) displacement and the \(N^{-2/3}\) norm correction. Above that transition it identifies the otherwise invisible skew-induced preferred branch. These quantify a genuine spectral-localization boundary rather than a routine rewriting of the radial eigenvalue formula.

## Scope and remaining risk

The result covers a symmetric pair of equally wide squared-radius shells in one complex dimension, with parameters fixed as \(N\to\infty\). It does not provide a full spectrum, varying-parameter crossover, or independent priority certification. General coalescing-saddlepoint or Gamma Edgeworth references may encode an equivalent corollary without the same terminology.

Self-review: passed. Independent audit: not yet performed.
