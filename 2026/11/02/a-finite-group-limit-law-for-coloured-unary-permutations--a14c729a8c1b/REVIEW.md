# Scientific review: finite-group limit law for coloured unary permutations

## Correctness

PASS. The automorphism-group decomposition follows directly from colour-preserving cycle rotations and permutations of isomorphic cycles. Each necklace type has labelled EGF weight \(z^\ell/s\). Marking finitely many types yields independent Poisson limits; a uniform-in-size estimate on nonprimitive long cycles plus repeated long primitive necklaces upgrades this to total-variation convergence for the full group. There are exactly two order-two mechanisms, giving the stated EGF; the Witt necklace identity supplies the rigid factor. The limiting constant follows from analytic coefficient extraction. Exhaustive finite checks for small sizes returned `ALL_CHECKS_OK`; they are corroboration, not proof of convergence.

## Originality

PASS within inspected evidence. Band–Harrison–Sepanski (2016), arXiv:1610.03808, Theorem 2, already proves the exact rigidity-count identity via strictly decreasing Lyndon factorizations; this part is explicitly credited. Kuželka (2026), arXiv:2608.30580, gives an automorphism-marking model-counting construction, and Ercolani–Ueltschi (2012/2014) describe Poisson finite-cycle limits. None of the materially inspected claims identifies the complete group-valued limit together with the two order-two mechanisms and its exact EGF. Scientific risk remains that classical weighted permutation-species results or inaccessible sections imply the exact theorem; independent priority review has not been done.

## Value

PASS. Automorphism-sensitive enumeration is motivated by the 2026 unary-function counting literature. Unlike simply checking whether the centralizer is trivial, the theorem identifies the **entire limiting symmetry group**, establishes why infinitely many cycles coexist with only finitely many surviving symmetry factors, resolves the smallest nontrivial group stratum exactly, and exposes the sharp one-colour versus multiple-colour boundary. The result is for a natural complete class of finite models, not a selected small table.

Self-review: passed. Independent audit: not yet performed.
