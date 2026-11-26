# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 19–54. Multiplication and addition are monotone for the natural order; s≼s² makes every positive power nondecreasing, and the evaluation of θ on A is Σ_a w_a^|A|, so adding elements cannot decrease it. For any candidate prenex existential NNF sentence, separate its expansion on J_t into old assignments and assignments that use b. At t=1 all factors are 0 or 1. The old sum equals 1, and the new total is 1, so unit nonabsorption and zero-sum-freeness force every extra monomial to have a zero factor. No zero factor changes at t=u≠0, so extra assignments still contribute zero; equality with θ would force u²=u. The argument requires no absence of zero divisors, and works for arbitrary existential tuple length, including no quantifiers. The saturation map from ℕ preserves both operations (including multiplication by zero). The natural order is the ordinary order and u=2 distinguishes the powers at M≥3; at M=1,2 multiplication is idempotent, so θ collapses to ∃x R(x). Both sentences are zero on the empty domain if allowed. VERIFICATION.md and checker.py were inspected, not executed. The proof, not bounded checks over example interpretations, addresses every existential formula.

## originality

PASS

Pass for the fixed one-unary-symbol finite nondefinability theorem, its algebraic criterion, and the cap threshold for this witness only. General failure of finite extension preservation for capped counting is already covered, including at cap two with another sentence. The original does not assert global minimality of four elements. The unbounded-semiring formulation for the same sentence is also prior work.

## value

PASS

Unlike generic transfer from a classical counterexample, a sentence that is already classical-existential fails elimination on a one-predicate annotated domain. The two-domain mechanism locates an algebraic obstruction and explains exactly when this witness stops working under saturation. This isolates a different mechanism even though general finite capped failure is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
