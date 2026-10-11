# Scientific review: lacunary finite-field Fourier synthesis

## Correctness — PASS

The fourth-moment normalization is reconstructed exactly from the sum over frequency variables. The first and third monomials recover every unordered pair with nonzero sum because the field characteristic is greater than \(3\). Zero-sum collisions are equivalent to the fourth roots of unity; the pair multiplicities produce the coefficient \(8\) in the additional quartic energy. Cauchy–Schwarz and the four-variable arithmetic–geometric inequality yield the optimal bound and recover all equality cases. The code checks nine finite fields including two quadratic extensions and directly evaluates the synthesis norm on two small prime fields. The field-uniform proof is analytic, not an extrapolation of finite tests.

## Originality — PASS, residual equivalence risk

The closest literature comprises Mockenhaupt–Tao's finite-field restriction framework (arXiv:math/0204234), Koh–Shen's theory for planar algebraic curves (arXiv:1003.4240), and the sharp endpoint theory of full consecutive-power moment curves (arXiv:2508.08377). None of the inspected relevant statements contains the exact sharp fourth-moment norm for \(t\mapsto(t,t^3,t^4)\) or its complete four-point phase classification. A published result concerning \(t\mapsto(t,t^4)\) calculates unweighted plane-curve energy, not the present weighted three-coordinate norm. Published-record and available prior-claim comparisons did not reveal stronger coverage; an older reformulation through additive-combinatorial energy remains possible.

## Mathematical value — PASS

The result supplies an exact all-field sharp Fourier endpoint and a structural arithmetic phase transition. It distinguishes complete-modulus extremizers from an extremal concentration on only four points. The fourth-root collision mechanism explains why the apparently small change of adding a coordinate alters the optimizer geometry, making this a motivated concentration/equality phenomenon rather than a routine normalization computation.

## Limitations

Fields of characteristic \(2\) and \(3\) are excluded, and input/output normalization is essential to numerical constants. The argument does not address higher moments or general lacunary exponent sets. No claim of exhaustive novelty certification is made.

Same-model review: passed. Independent audit: not yet performed.
