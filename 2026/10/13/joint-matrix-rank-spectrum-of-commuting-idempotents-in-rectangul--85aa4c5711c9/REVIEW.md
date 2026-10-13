# Self-review

## Correctness — PASS

The theorem quantifies all finite fields, positive rectangle dimensions, and sandwich ranks including zero. Its proof reconstructs the basis-normalized four blocks; the idempotent relations force the bottom-right block, and the commutation relations have no omitted lower-right condition. A simultaneous decomposition into four *canonical* orthogonal projection sectors gives the stabilizer denominator, while the top-right and bottom-left lift parameters contribute exactly the exponent \((m+n-2r)(b+c+d)\). Ordinary rank is retained because each idempotent factors through its upper-left projection, and its projection is a submatrix. The boundary \(r=0\) and characteristic two are explicit. An independently written exhaustive small-field checker compares actual matrix multiplication and actual rank pairs for ten finite cases including \(\mathbb F_4\); general correctness rests on the algebraic proof, not the experiments.

## Originality — PASS, with bibliographic risk

Dolinka and East, arXiv:1503.03139v1, Proposition 7.2 already enumerate individual sandwich-idempotents by rank; that formula is credited and not claimed as a contribution. Their Lemma 6.9 and Sections 6–7 were read, and do not state a commuting **ordered-pair** joint-rank enumerator. Their matrix-factorization and Green-relation results do not by themselves imply the enumerated commutation fibers without the simultaneous projection decomposition and coupled lift equations. The categorical framework in arXiv:1710.01890v1 (first public 2017-10-05) has been compared through available description/abstract, not full text; the original arXiv:2005.00309v1 was inspected in its algebra-homotope sections. Result searches for joint spectra, sandwich commuting idempotents and Munn-ring variants did not identify covering claims. Risk: an uninspected equivalent formulation or general projection theorem in semigroup literature may exist. No absolute novelty certificate is asserted.

## Value — PASS

This is a natural two-element refinement of a known one-element census: it completely measures **when idempotents commute**, stratified simultaneously by the ordinary ranks of both operands, across all finite fields and rectangle sizes. Such data governs the labeled commuting-idempotent graph and asymptotic commutation probability, and is not recoverable from the one-point rank distribution. The proof supplies a structural description and uniform closed formula, not an arbitrary isolated numerical example.

## Bibliographic boundary and limitations

The complete 2017 categorical-paper text was not inspected, and an older equivalent result under variant-semigroup or Munn-ring terminology remains possible. Only self-review and finite-case computational corroboration have been performed, without external validation.

Self-review: passed. Independent audit: not yet performed.
