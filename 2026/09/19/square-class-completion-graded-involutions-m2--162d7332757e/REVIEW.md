# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The classification is a direct two-case analysis of the involution on the two primitive idempotents of the neutral diagonal component. In the fixed-idempotent case, anti-multiplicativity forces e12* = a e21 and e21* = a^{-1}e12. In the swapped-idempotent case it forces e12* = ±e12 and e21* = ±e21 with the same sign. The graded automorphism group normalizes the diagonal algebra and is represented by monomial matrices; diagonal conjugation changes a by a square and coordinate interchange sends a to a^{-1}, giving exactly the square-class invariant. Identity and central-polynomial equivalence follows after adjoining a square root of a/b and using scalar-extension invariance over an infinite field, with characteristic zero providing multilinearization.

Adversarial checks included the possibility of conjugating a diagonal-fixing involution to a swapping one (excluded by the induced permutation on primitive diagonal idempotents), the antidiagonal normalizer action (it only inverts a, which preserves its square class), and the central-polynomial scalar-extension step (valid here because the center of M_2 extends from F I_2 to K I_2).

## Originality

PASS, qualified to the best of our knowledge. The square-class/discriminant phenomenon for orthogonal involutions on matrix algebras is standard background and is not claimed as new in isolation. The specific issue is that arXiv:2609.20488v1 states an arbitrary characteristic-zero base field while its Theorem 2.1 uses a list sourced from Bahturin--Zaicev, whose classification explicitly assumes an algebraically closed field. Targeted searches for the current arXiv identifier, the theorem's matrix/involution setting, square-class variants, and graded-PI equivalence did not locate a public correction or an explicit arbitrary-field completion of this theorem. The additional PI-equivalence statement explains why the missing structural classes do not require new transpose-class identity formulas.

The most relevant older source is Bahturin--Zaicev, *Involutions on graded matrix algebras* (J. Algebra 315 (2007), arXiv:math/0609417), which was inspected at the abstract/assumption level and explicitly works over an algebraically closed field of characteristic different from 2. Standard general literature on algebras with involution may contain equivalent square-class language under discriminants or adjoint forms; this is the main residual originality risk. The recent source is very new, so an author correction or independent contemporaneous observation may also appear later.

## Value

PASS. The result gives an exact sharp replacement for the order-two elementary branch over arbitrary fields: F^×/(F^×)^2 plus the two swapping classes. It supplies explicit counterexamples over Q and shows the omitted family can be infinite. At the same time it localizes the downstream impact by proving that all missing orthogonal square-class forms are graded-*-PI equivalent, so existing transpose identity, central-polynomial, cocharacter, and codimension formulas extend to them without recomputation.

## Scope and limitations

The result does not claim a complete arbitrary-field classification of all G-gradings on M_2(F), nor does it settle possible extra forms for the Klein (-1)-grading. No independent validation, formal verification, or peer review is asserted.
