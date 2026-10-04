# Review of Integer-area mixed-arithmetic four-point Gabor independence

## Correctness

PASS. The symplectic normalization is exact: if the marked core has oriented area \(q\in\mathbb N\), then the determinant-one map \(DS^{-1}\), with \(D=\operatorname{diag}(1,q)\), sends it to \(e_1,qe_2\). Rational rank is unchanged by the rational rescaling of the second coordinate. An integral determinant-one change of variables then makes the rogue point \((a,p/m)\) while keeping the core inside \(\mathbb Z^2\), now as an index-\(q\) sublattice.

The Zak return calculation in the source needs only integer core vectors, so its Laurent return multiplier survives unchanged. The only critical-lattice input that must be replaced is the source's unimodular trinomial zero lemma. For linearly independent integer character vectors of determinant \(q\), the character map is a degree-\(q\) covering of \(\mathbb T^2\). The target three-term equation has at most two solutions, hence the original trinomial has at most \(2q\) zeros. This restores a finite exceptional-fibre set. Direct inspection of the source's active-arc, measurable-winding, holonomy-quantization, analytic-rigidity, Laurent-holonomy, and irrational-character lemmas shows that their hypotheses after this point are finiteness, zero-freeness on an arc, irrationality of the return, and Laurent structure; none requires determinant one. The contradiction therefore extends to all integer \(q\).

Risk: the proof imports several long analytic lemmas from the cited source rather than reproving them from first principles. Their statements and dependency points were inspected, and the accepted claim is explicitly restricted so that every cited hypothesis is preserved.

## Originality

PASS. The closest paper, arXiv:2609.27970v1, states the rational-rank-two theorem only at \(|\sigma(u,v)|=1\), labels the supercritical mixed-arithmetic cell as partially classified, and attributes the finite exceptional-fibre reduction to the unimodular trinomial lemma. The inspected large-covolume paper arXiv:2604.21228 covers \(|\sigma(u,v)|>1\) only in the maximally irrational rank-three case, together with the rational-coordinate case. The inspected mixed-integer trichotomy arXiv:2508.04613v2 gives necessary constraints for Schwartz-window counterexamples but does not imply \(L^2\) independence in rational rank two.

Searches for integer symplectic area, finite-index lattice, supercritical mixed arithmetic, rational rank two, and equivalent HRT/Gabor formulations returned no statement of the integer-area theorem or its finite-covering mechanism.

Residual risk: a finite-index variant could have been observed elsewhere under different notation, especially in literature on mixed-integer Gabor configurations. No such result was found in the primary papers or database searches inspected.

## Value

PASS. The source paper presents the supercritical mixed-arithmetic cell as a live partial-classification frontier. Positive integer area is a natural invariant slice, not an arbitrary numerical specialization: exactly there the core can be symplectically normalized to a finite-index sublattice of the standard Zak lattice. The result supplies all-window \(L^2\) independence on an infinite family \(q=2,3,\ldots\) and identifies the structural reason the critical proof persists—finite covering replaces unimodularity without losing finite torus zeros. This materially enlarges the proved positive region while leaving the genuinely noninteger supercritical problem open.

Same-model review: passed. Independent audit: not yet performed.
