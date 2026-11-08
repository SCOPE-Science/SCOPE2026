# Scientific review: the fifteen-point supersingular locus

## Correctness — PASS

The statement concerns exactly the genus-four hyperelliptic members of the characteristic-five marked two-parameter family with the stated nonzero smoothness factors. The ten-degree polynomial is squarefree there, and its two genus-two involution quotients are explicitly related by a Möbius transformation to one genus-two curve. Their Jacobian pullbacks give a prime-to-five isogeny to a square, which preserves the Newton polygon, \(5\)-rank, and Cartier \(a\)-number. Characteristic-five expansion of the squared genus-two equation gives a \(2\)-by-\(2\) Cartier matrix with a nonzero constant entry. Its rank and Frobenius-stable rank determine all three strata. On the rank-one divisor, the remaining condition eliminates to the degree-fifteen polynomial \(H\) with one rational root and an irreducible degree-fourteen factor. Euclidean gcd certificates verify separability and exclude every singular parameter. The exact standard-library verifier was executed and returned `VERIFY_SQUARE_JAC_P5_OK`; its separate projective counts in two finite fields are consistent. The proof is algebraic over the entire algebraic closure; finite counts are only cross-checks.

## Originality — PASS, with stated risk

Bruin--Kulkarni (arXiv:2309.01959v1, Example 7.3) supplies the two-parameter geometric family and square-Jacobian framework, but does not classify characteristic-five supersingular parameters. Kudo--Harashita--Senda (arXiv:1903.08095, Sections 1--2) proves existence for a different genus-four Howe family and supplies a classical genus-two Cartier test, not the arithmetic stratification of this hyperelliptic square family. Harvey--Sutherland supplies the established Hasse--Witt coefficient algorithm. An earlier calculation of the very same marked family already determined the nonordinary divisor and its one rational supersingular parameter. That earlier result is **not** claimed new, and it does not give a fifteen-point geometric supersingular census, the degree-fourteen Frobenius orbit, or the full stable-rank partition of the nonordinary divisor. Statement-level comparison against these stronger nearby inputs leaves a genuine new exact classification. Risk remains that older genus-two tables implicitly encode the same fourteen algebraic parameters after a change of normal form; targeted searches did not reveal such a decisive source.

## Mathematical value — PASS

This is an intrinsic arithmetic question motivated by the exceptional two-dimensional locus of genus-four Jacobians isogenous to squares of genus-two Jacobians. Beyond the previously known nonordinary divisor, the theorem identifies all geometrically supersingular fibers, shows that their locus is reduced and has degree fifteen, determines the complete Frobenius field-of-definition structure \(1+14\), and distinguishes the generic nonordinary \(5\)-rank-two fibers from the finite supersingular exceptional set. These natural complete strata are not arbitrary small-field examples or routine polynomial substitutions. The result has no claims about global moduli isomorphism counts, other characteristics, or full zeta functions.

## References and limits

1. N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959v1, September 5, 2023, especially Section 7.1 and Example 7.3. https://arxiv.org/html/2309.01959v1
2. M. Kudo, S. Harashita, H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, arXiv:1903.08095, March 19, 2019; Research in Number Theory 6 (2020), 44. https://link.springer.com/article/10.1007/s40993-020-00217-x
3. D. Harvey and A. V. Sutherland, *Computing Hasse--Witt matrices of hyperelliptic curves in average polynomial time*, arXiv:1402.3246, February 13, 2014. https://arxiv.org/abs/1402.3246

Self-review: passed. Independent audit: not yet performed.
