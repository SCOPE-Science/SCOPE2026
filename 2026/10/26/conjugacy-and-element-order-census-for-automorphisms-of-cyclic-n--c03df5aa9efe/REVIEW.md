# Self-review: Conjugacy and element-order census for automorphisms of cyclic nilpotent Leibniz algebras

## Correctness — PASS

The recursive bracket identity gives all and only invertible triangular maps \(F_{a,U}\), and their composition is the truncated principal-unit semidirect product. For each multiplier of order \(d\), the norm onto fixed units is surjective because the \(d\)-th power map is invertible on a finite \(p\)-group. Its kernel is the coboundary image, giving a genuine direct-product splitting. Burnside's lemma and characteristic-\(p\) Frobenius then give exactly the conjugacy and order-count formulas. The eleven enumerations in `verify_cyclic_leibniz.py` verify orders and commuting pairs over field sizes 2, 3, 4, 5, including prime-power fields. These checks are finite corroboration only.

## Originality — PASS (bounded)

Kurdachenko–Pypka–Subbotin (arXiv:2108.06794), Theorem 2.11, already gives the full semidirect-product automorphism description. This prior structure is not new. The current formula counts group conjugacy classes and elements of every exact order; the inspected type-I treatment does not establish these derived arithmetic quantities. Batten Ray et al. (arXiv:1207.3739) and Bugg et al. (arXiv:1402.5821) motivate cyclic nilpotent Leibniz algebras but do not give a finite-field census. Targeted mathematical literature and published research-record searches found no equivalent claim. An unexamined broader principal-unit orbit result could still imply the formulas.

## Value — PASS

Every finite-field automorphism group in an infinite classical nilpotent Leibniz family receives its exact conjugacy-class number and full order spectrum. The fixed-degree norm argument handles nontrivial scalar actions uniformly, including characteristic two. These are natural global finite-group invariants, not a relabeled known group isomorphism or a small ad hoc count.

## Limitations and closest literature

The 2021 group isomorphism is decisive structural prior work, and absolute priority for the new arithmetic census is unverified. The formulas do not address semilinear maps, nonnilpotent cyclic algebras or conjugacy-class-size distributions. The finite checker is not an external mathematical audit.

Self-review: passed. Independent audit: not yet performed.
