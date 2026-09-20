# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The theorem was checked against the detailed proof of the directly relevant construction in arXiv:2609.20805. The source's Fourier-series estimate is uniform in its real phase parameter, so that stage is unchanged for arbitrary fixed real \(\beta\). The places where the detailed one-dimensional proof uses \(|\beta|<1/2\) admit explicit replacements: integer exceptional values are finite rather than singleton for each fixed pair \((j,\ell)\); auxiliary poles are within \(1+|\beta|\) rather than \(3/2\) of their integer labels; and the resulting weighted summability and pole-density arguments are unaffected after allowing constants to depend on \(\beta\).

Pairwise pole distinctness is guaranteed by the same nonresonance condition appearing in the source's higher-dimensional statement specialized to dimension one: equality of two poles implies \((\ell-\ell')(\alpha+\beta^{-1})\in\mathbb Z\). Uniform discreteness of the frequency set is checked independently: for an index difference \(d\ge1\), every frequency difference is one of \(d+\beta\{d\alpha\}\) or \(d-\beta(1-\{d\alpha\})\); nonresonance excludes zero, and only finitely many \(d\) can have magnitude comparable with \(|\beta|\). Bounded displacement plus injectivity gives uniform density one. The final Jensen zero-versus-pole density contradiction therefore carries over without a smallness hypothesis.

No computational experiment is used as a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** The strongest directly relevant source located is Bertolini--Florit-Simon--Liehr--Taylor, arXiv:2609.20805. Its Theorem 1.1 uses rational \(\beta\) with \(0<|\beta|<1/2\), while its Section 6 formulation strengthens the arithmetic hypothesis to general real \(\beta\) but still assumes \(|\beta|<1/2\) in dimension one. The source's detailed proof was inspected at the uniform Fourier coefficient estimate, meromorphic pole construction, weighted summability, pole distinctness, pole density, and Jensen step; no amplitude-free statement was found.

Targeted searches by source identifier, the explicit irrational-rotation frequency formula, the condition \(\alpha+1/\beta\notin\mathbb Q\), and combinations of universal completeness, simple quasicrystals, irrational rotations, and arbitrary-amplitude perturbations found no equivalent theorem or correction. Earlier simple-quasicrystal sampling results concern compact spectra or different stability questions and do not supply this arbitrary measurable finite-measure universality statement for the explicit family. Residual risk remains because arXiv:2609.20805 is very recent and a contemporaneous extension may not yet be indexed.

## Value

**PASS.** The result removes the only size restriction from the explicit one-dimensional quasicrystal family while preserving the full universal \(L^1\)-uniqueness and \(L^p\)-completeness conclusion. For every fixed irrational \(\alpha\), all but a countable set of nonzero real amplitudes are covered, and every nonzero rational amplitude is covered regardless of magnitude. This shows that the mechanism is arithmetic nonresonance rather than proximity to the integers in a small-perturbation regime.

## Limitations

The theorem is restricted to dimension one and makes no claim for the resonant parameter set, the critical spectral measure \(|S|=1\), stable sampling/frame inequalities, or a parameter-uniform separation constant. The higher-dimensional small-norm hypothesis is not removed. No independent validation, independent audit, or formal proof-assistant verification is asserted.
