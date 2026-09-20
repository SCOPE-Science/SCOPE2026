# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The argument was checked against the theorem and proof structure of Zhang--Zhou, arXiv:2609.08679v1.

The source constructs, from a nonprojective \(M\in{}^\perp A\) with a finite range of self-extension vanishing, a pairwise nonisomorphic chain of indecomposable nonprojective syzygy summands. When \(J^3=0\), these terms are annihilated by \(J^2\), so they are \(B=A/J^2\)-modules. The source then discards the terms that are projective over \(B\), transfers the remaining triangular Hom/Ext vanishing to the separated algebra, and bounds the sequence length by the number of simple modules of that hereditary algebra.

Two refinements were audited separately.

First, only non-isolated vertices of the separated quiver are needed. An indecomposable nonprojective separated-algebra image cannot have a component on an isolated vertex: the separated algebra decomposes as the active path algebra times isolated copies of \(k\), and any nonzero isolated component is a projective direct summand. Thus the hereditary rank in the source argument drops from \(2s\) to \(\kappa+\rho\).

Second, when \(J^3=0\), every \(B\)-projective term \(Be_i\) in the chain has
\[
\Omega_A(Be_i)\cong J^2e_i,
\]
which is semisimple. Its prescribed nonprojective successor is therefore a nonprojective simple constituent of \(J^2e_i\). Distinct \(B\)-projective terms give distinct left vertices, and distinct successors give distinct right vertices. After adjoining one extra nonprojective syzygy summand beyond the source length-\(L\) list, this also covers a \(B\)-projective term in the last position. The resulting edges are a matching in \(\Gamma_2(A)\), so at most \(\nu\) terms are discarded.

The extra term is pairwise nonisomorphic to the preceding terms because for \(i<L\),
\[
X_L\mid\Omega_A^{L-i}X_i
\]
and the required stable Hom group is identified with the vanishing self-extension group in degree \(L-i\le L\). This closes the endpoint case without requiring an additional self-extension degree.

With \(L=\kappa+\rho+\nu+1\), at least \(\kappa+\rho+1\) nonprojective \(B\)-terms remain, contradicting the hereditary sequence bound for the active separated algebra, which has \(\kappa+\rho\) simple modules.

The larger-Loewy-length companion criterion uses only the weaker count \(\delta=\#\{i:J^2e_i\ne0\}\); it does not use semisimplicity of \(J^2e_i\). This matches the hypotheses of the source Proposition 4.3.

Boundary checks are consistent: for \(J^2=0\), \(\nu=0\); in the fully active/full-matching case the formula returns \(3s+1\); and for a semisimple algebra the contradiction arises before any nonprojective sequence can exist.

## Originality

The primary comparison is Zhang--Zhou, arXiv:2609.08679v1, submitted 8 September 2026. It proves the \(3s+1\) bound, says that bound is not claimed optimal, and explicitly leaves improving the estimate as a question. Its published argument counts all \(2s\) separated-quiver vertices and bounds the discarded \(B\)-projective terms by \(s\); it does not state the active-vertex count or the second-layer matching refinement.

Targeted literature checks covered synonymous formulations involving radical-cube-zero algebras, separated algebras/quivers, self-extensions, finite Auslander--Reiten tests, radical-square-zero reductions, and first nonzero self-extension bounds. No equivalent formula involving non-isolated separated-quiver vertices together with a matching in the \(J^2\)-layer was found.

Relevant older work includes Ringel--Xiong on radical-square-zero rings, Ringel--Zhang on short local algebras, Xu on local radical-cube-zero algebras, and Hoshino's radical-cube-zero papers. These establish sharper conclusions in important special classes but do not, in the inspected material, state the present algebra-sensitive bound.

The full text of Hoshino (1989), *On algebras with radical cube zero*, was not inspected. Its bibliographic record and later citations were checked, so it remains the principal inaccessible source capable of affecting the originality assessment. Because the Zhang--Zhou preprint is very recent, contemporaneous independent discovery is also possible.

Originality verdict: PASS, to the best of our knowledge, with the limitations above.

## Value

The source paper's \(3s+1\) theorem is uniform in the number of simple modules. The new bound replaces two coarse cardinality estimates inside that proof by computable structure of the individual algebra:
\[
3s+1
\quad\rightsquigarrow\quad
\kappa+\rho+\nu+1.
\]
It can therefore be substantially smaller for sparse separated quivers or sparse second radical layers while remaining valid for arbitrary basic split radical-cube-zero algebras. The same active-quiver observation also improves the source's eventual-\(J^2\)-annihilation criterion beyond Loewy length three.

The result is not claimed to improve the worst-case constant, and it does not replace sharper special-class theorems.

Value verdict: PASS.

## Review status

Same-model review: passed. Independent audit: not yet performed.

No independent validation, formal verification, or peer review is asserted.
