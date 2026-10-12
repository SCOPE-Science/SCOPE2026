# Mathematical review: one-entry-deleted Segre toric varieties

## Correctness — PASS

The theorem is derived from explicit affine coordinate rings rather than a guess about the image of a rational projection. Every projective point belongs to a chart with a nonzero retained matrix entry. In a chart \(z_{ij}\ne0\) with \(i,j>1\), the coordinate ring is polynomial in \(a+b-2\) free variables. In a row chart, the generators separate into independent free variables \(t_q\) and the rank-one matrix variables \(s_i,w_i\), with kernel exactly the prime two-by-two minor ideal. The column chart is symmetric. These identities establish scheme-theoretic normality, the complete reduced singular-locus decomposition, multiplicity, and local class-group computations. The cone over \(\mathbb P^1\times\mathbb P^{m-1}\) has local class group \(\mathbb Z\) for \(m\ge2\), and the canonical class modulo the polarization tests \(\mathbb Q\)-Gorensteinness. The blowup at the omitted point resolves the projection; the description of projective lines on a Segre variety establishes that its only positive-dimensional fibers are the ruling lines through that point. Smallness and crepancy then follow with the parameter boundaries stated in RESULT.md.

The included exact Python checker ran successfully: 25 formats, 375 affine charts, bounded monomial and Hilbert-function tests, and rational Jacobian tests. These are corroboration, not a replacement for the symbolic proof. The assertion concerns closed complex points and reduced singular support, not scheme-theoretic singular multiplicities.

## Originality — PASS, with residual risk

Ohsugi–Hibi's complete-bipartite graph example supplies the full Segre determinantal ideal and the broader graph-toric framework. Aluffi's projection-of-rank-loci work treats projection degrees, including coordinates and resolution of indeterminacies. Kubjas–Rosen and Kahle–Kubjas–Kummer–Rosen treat rank-one partial matrix/tensor completions, including semialgebraic constraints, algebraic elimination and componentwise zero-completability. These are prior ingredients, not independent discoveries claimed here. The specific joined assertion of all affine transverse cones, pointwise local class groups, the two-disjoint-strata criterion, and the blowup being small for both dimensions at least three is not stated in the inspected relevant passages, though a logically equivalent specialization in work not located remains a genuine possibility. Repeated semantic database queries for the deleted-entry pattern and the equivalent coordinate projection did not return an identical result; database absence is not proof of novelty. No statement of independent novelty certification is intended.

## Value — PASS

This provides a complete geometric classification in a natural infinite two-parameter family of normal projective toric varieties, distinguishing smooth, Gorenstein, and non-\(\mathbb Q\)-Gorenstein regimes and determining local class groups, multiplicities, and the exceptional geometry of a concrete projective birational model. The result is useful for understanding which coordinate projections of Segre varieties retain crepant or small resolutions; these are geometrically motivated properties and not simply a recomputation of a known degree.

## Source comparisons and limits

The closest written contexts are Ohsugi–Hibi, *Toric ideals of finite graphs and adjacent 2-minors*, arXiv:1108.2850, Example 2; Aluffi, *Degrees of projections of rank loci*, arXiv:1408.1702, introduction and Sections 2–4; Kubjas–Rosen, *Matrix Completion for the Independence Model*, arXiv:1407.3254, Sections 1–4; and Kahle–Kubjas–Kummer–Rosen, *The Geometry of Rank-One Tensor Completion*, arXiv:1605.01678, Sections 1–3. The general determinantal cone geometry and standard blowup construction are used, not claimed as novel. A source not located in these comparisons could contain the one-coordinate-deletion specialization. There is no independent mathematical audit; the nonreduced singular scheme and arbitrary deletion patterns are outside scope.

Self-review: passed. Independent audit: not yet performed.
