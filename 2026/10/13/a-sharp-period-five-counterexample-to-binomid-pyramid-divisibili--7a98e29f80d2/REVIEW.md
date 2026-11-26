# Independent mathematical audit

## correctness

PASS

Shapiro's definition is exactly the binomidness of every column, equivalently integrality of the pyramid, without any extra recursive requirement. For a periodic exponent word, complete blocks cancel from each column exponent and again from each comparison of a consecutive block sum to the initial block sum; only the two remainder lengths and the starting residue matter. The five column residues of the proposed word give cyclic minima equal to their prefix sums, respectively (0,1,2,2), (0,1,1,2), (0,0,1,1), (0,2,3,4), and (0,0,0,0). The exponent two appears once per period, and f_2=q does not divide f_4=1. For period T≤4 apply the inequalities to each prime separately. The first column forces its initial valuation A to be minimal. For T=3, the length-two comparison in column two forces B≤A, hence A=B≤C. For T=4, column one's length-three comparison forces B≤D, and column three's length-two comparison forces C≤A, hence C=A≤B≤D. Together with A≤B for T=2 and the constant case, these are exactly the required divisibility orders: odd indices have the bottom value for T=2,4, multiples of four have the top value for T=4, and for T=3 the residue-zero class has the top value. The proof covers every prime, unbounded lengths and all integer q≥2, including composite bases. Independent replay `python3 /workspace/checks/frozen_replay.py 3` reproduces all displayed cyclic minima, checks 780 bounded valuation words using a divisor/multiplier residue test, and checks 9750 direct integer coefficients for bases 2, 6 and 9. Finite regressions do not prove the primewise classification.

## originality

PASS

The distinct supported contribution is a positive pure-periodic all-level witness and its least possible period. Inspected sources treat first-level indices, sufficient divisor-product conditions, restricted second-order subclasses, or signed/nonperiodic examples; none covers either assertion in this combination. The order-two side remark in the frozen relationship section should not be treated as a present-day claim: a later indexed result gives a signed nonperiodic counterexample to the unrestricted all-level implication for second-order recurrences.

## value

PASS

This is a sharp answer to a natural converse in a published framework: even integrality in all columns does not force divisibility, and the first possible period for a positive purely periodic example is five. The example and the primewise impossibility below five are both needed; neither could be replaced by observing a small finite triangle. It gives a reproducible obstruction in the higher-order recurrence setting, without claiming to resolve the positive order-two case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
