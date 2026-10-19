# Scientific review

## Correctness

**PASS.** Gaussian monomial orthogonality produces the exact second and fourth moments, reducing the squared coercivity constant to a rational polynomial quotient. The phase ordering is justified by monotonicity in the fourth moment, not by an assumed real-coefficient restriction. For each positive quadratic modulus, the first derivative has one positive zero and supplies the unique affine-to-quadratic amplitude ratio. The second stationary equation is eliminated by an explicit resultant; its only positive candidate is the unique positive root of a strictly increasing cubic in the squared quadratic parameter. The boundary cases have squared ratio at most \(2\), while the interior optimizer exceeds \(2\). An independent symbolic expansion and Gaussian moment quadrature confirm the algebra. No numerical search is used for the global argument.

## Originality

**PASS within the checked primary literature, with residual priority risk.** Bortolotto and Ramos prove a uniform estimate for the identical centered-square functional (arXiv:2608.26365, Theorem 1.1), but without an optimal constant on the three-mode sector. Bertolini and coauthors (arXiv:2605.20527, Theorems 1.3 and 2.1) prove a related general modulus stability and orthogonal coercivity bound, with a different numerator and denominator. Neither statement determines the algebraic three-mode best constant or its equality family by implication. Search evidence cannot rule out an unindexed independent finite-mode computation; further human historical verification is warranted.

## Value

**PASS.** The finite mode cutoff is intrinsic: \(\operatorname{span}\{1,z,z^2\}\) is the first Bargmann–Fock polynomial sector beyond affine signals. The sharp constant is not the affine continuation \(\sqrt2\): destructive interference from the quadratic mode increases the worst-case ratio to \(1.563357712\ldots\). This gives a concrete quantitative obstruction to improving the recent universal square-coercivity theorem and identifies the uniquely worst three-mode signal geometry. It is an exact natural baseline for truncation-based stability analysis, not an arbitrary polynomial example.

## Relationship and limitations

The conclusion is restricted to first three Fock modes, with normalized planar Gaussian measure. It does not give the best constant for higher modes or unrestricted entire functions. Equality cases are unique only modulo complex scaling and argument rotation, exactly as stated. The historical novelty conclusion is a qualified literature comparison, not an independent priority certification.

Self-review: passed. Independent audit: not yet performed.
