# Mathematical review

## Correctness — PASS
The derivative-based Hardy–Sobolev space has the exact Fourier weight \(p_n(s)=\sum_{j=0}^n s^{2j}\) under the unitary Paley–Wiener transform. Substitution into the affine composition symbol gives a weighted-dilation formula; iterating yields a precise operator-norm supremum. The undamped supremum has exact high-frequency value, and the inverse norm gives the other annulus boundary. Both spectral interiors have explicitly exhibited infinite-dimensional eigenspaces (of the adjoint for zero displacement and of the operator for positive displacement), and closure supplies the boundary. Uniform tail domination yields the normalized power limit; a variational logarithmic quotient gives the sharp damping cutoff. A rescaling of the polynomial shows the exact \(b^{-n}\) prefactor. Pointwise eigenfunction identities and finite power values were checked by the standalone script. The essential-spectrum proof does not infer an infinite statement from finite tests. Risks: the theorem does not address complex dilation or nonaffine symbols; the two small-parameter limits cannot be interchanged by this proof.

## Originality — PASS with literature risk
The initiating full paper [1] develops the unweighted-derivative Hardy–Sobolev Fourier model and affine weighted-composition boundedness, but not the proposed composition spectra, power asymptotics, or damping cutoff. Chalendar–Partington [2] gives the closest method and a **qualitatively analogous** annulus/disk spectral transition on Hardy–Bergman Zen spaces. Its underlying weight is nonincreasing and its results neither assert the increasing polynomial-weight case nor determine the sharp positive damping cutoff and the \(b^{-n}\) amplification law. Thus the **general** annulus/disk phenomenon, spectral-radius technique, and multiplicative-periodic eigenvector mechanism are already known and not claimed as original. Galé et al. [3] and Liu et al. [4] use weighted derivatives of a distinct Hardy–Sobolev scale and discuss composition boundedness. Searches comparing exact claims, equivalent Fourier formulations, broader operator-spectrum claims, and database coverage did not reveal an implication establishing the complete quantitative classification. A residual risk remains from unindexed spectral literature or a broader weighted-dilation result not surfaced here.

## Mathematical value — PASS
The result determines a natural spectral invariant and sharp quantitative dynamics for the first derivative-based half-plane Hardy–Sobolev scale, where high-frequency regularity changes the undamped outer radius. It shows a singular perturbation: every positive vertical shift drops the spectral radius by the fixed factor \(a^n\), yet the operators converge strongly without converging in norm. The optimal power-amplification prefactor has a **nonzero finite critical damping boundary**, and its divergence exponent directly identifies Sobolev order. Those effects are nontrivial structural boundaries, not mere numerical recomputation of a known norm criterion.

## Sources and limitations
[1] Liang–Li–Qian, arXiv:2603.13983v1, Theorem 4.1 and Section 5.
[2] Chalendar–Partington, arXiv:2204.05894v2, Section 3, equations (6)–(7), Propositions 3.5–3.6, Theorem 3.7.
[3] Galé–Matache–Miana–Sánchez-Lajusticia, arXiv:2401.16091v1, definition and Section 7.
[4] Liu–Li–Kou–Qu, DOI 10.23952/jnva.9.2025.2.05, definition and Section 5.
Numerical diagnostics are finite and do not prove operator spectral statements. The interval of absolute novelty is limited to the investigated sources. No external independent review is implied.

Self-review: passed. Independent audit: not yet performed.
