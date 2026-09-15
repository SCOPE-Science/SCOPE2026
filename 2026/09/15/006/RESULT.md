# Parity obstruction disproving the stated QTC2 enumeration

## Context
The admitted target asked for a proof, via an integrable six-vertex-model domain-wall
partition function with Hafnian-Pfaffian / non-intersecting-lattice-path evaluation, of
the closed-form enumeration of Conjecture 4.2 of Schreier-Aigner (arXiv:2301.12272)
for quasi transpose-complementary plane partitions of second kind (QTC2). That
conjecture asserts, for fixed a >= 2 and all c (after the shifts c -> c-a/2 for a even
and c -> c-1/2 for a odd), that qtcpp_2(a,c) equals an explicit binomial prefactor
times an even polynomial p_a(c), including qtcpp_2(2,c-1) = c*binom(c,1) = c^2,
qtcpp_2(3,c-1/2) = binom(c+1/2,2)*(4c^2+3)/12, and
qtcpp_2(4,c-2) = c*binom(c+1,3)*(5c^4+19c^2-16)/280. Its Appendix A.2 data table
likewise records nonzero values at odd box heights, e.g. qtcpp_2(2,1) = 4,
qtcpp_2(2,3) = 16, qtcpp_2(3,1) = 7.

## Definitions
Let pi = (pi_{i,j}), 1 <= i,j <= a, be a plane partition in an (a,a,c)-box: nonnegative
integers bounded by c, weakly decreasing along rows and columns. Under the literal
target definition, pi is quasi transpose-complementary of second kind (QTC2) if
pi_{i,j} + pi_{a+1-j,a+1-i} = c for all 1 <= i,j <= a with i != j; the main diagonal is
exempted. Let qtcpp_2(a,c) be the number of such pi.

## Result
For every a >= 2 and every odd c, qtcpp_2(a,c) = 0 under the literal definition above.
Hence the claimed universal closed form, which predicts nonzero values at such (a,c),
is false. In particular qtcpp_2(2,1) = 0, refuting the predicted value 4. The same
argument refutes infinitely many predicted values (all odd box heights c for every
a >= 2).

## Proof
Consider the involution sigma(i,j) = (a+1-j,a+1-i) on {1,...,a}^2. Its fixed points
satisfy i = a+1-j and j = a+1-i, i.e. exactly the anti-diagonal i+j = a+1. For a >= 2
the cell (1,a) lies on the anti-diagonal, and since 1 != a it is not exempted by the
condition i != j (the exemption is the main diagonal, while the fixed-point set of
sigma is the anti-diagonal). Applying the defining relation at (i,j) = (1,a) gives
pi_{1,a} + pi_{sigma(1,a)} = pi_{1,a} + pi_{1,a} = 2*pi_{1,a} = c, because
sigma(1,a) = (a+1-a,a+1-1) = (1,a). Since plane-partition entries are integers,
2*pi_{1,a} = c has no solution when c is odd. Therefore no QTC2 plane partition
exists in an (a,a,c)-box for any a >= 2 and any odd c. The counterexample a = 2,
c = 1 gives 0 != 4 and refutes the identity. No monotonicity or box constraint beyond
integrality is used, so the conclusion is independent of order conventions and of
0- versus 1-based indexing.

## Evidence (corroboration, not needed for the proof)
Exhaustive enumeration of all plane partitions in small boxes under the literal i != j
definition confirms qtcpp_2(2,1) = 0 (predicted 4), qtcpp_2(2,3) = 0 (predicted 16),
qtcpp_2(3,1) = 0 (predicted 7). Even box heights also disagree with the stated
examples (e.g. qtcpp_2(2,2) = 4 computed versus 9 predicted), showing the examples
fail twice over. Full-text inspection of the source paper shows the discrepancy is
structural: the proved first-kind class exempts the anti-diagonal, while QTC2
exempts the main diagonal, leaving the fixed cell constrained.

## Consequence for the requested proof route
Because the identity as stated is false, no sound proof via any six-vertex-model
domain-wall partition function, Hafnian-Pfaffian, or non-intersecting-lattice-path
determinant evaluation can establish it: a correct evaluation of a correct model for
this symmetry class must reproduce the zeros at odd c proved above. A corrected
conjecture would have to, at minimum, restrict to even c or change the exemption
from the main diagonal to the anti-diagonal fixed-point set, which is a different
statement and is not proved here.

## Limitations
The disproof targets the universal for-all-c closed form exactly as stated; it does
not establish any corrected even-c-only enumeration, nor does it rule out a
differently-exempted (e.g. anti-diagonal-free) variant, which would be a different
claim and is left open.

## Reproducibility
The analytic proof is checkable by hand from the definition. The corroborating script
output/artifacts/verify_parity.py enumerates all plane partitions for small (a,c)
under the literal i != j condition and was independently re-executed during audit,
reproducing the zeros at odd c and the even-c mismatch.

## References
- F. Schreier-Aigner, Fully complementary higher dimensional partitions,
  arXiv:2301.12272 (Conjecture 4.2, Appendix A.2; Theorem 1.2 for the distinct
  first-kind class).
- T. Inoue, A bijection between symmetric plane partitions and quasi transpose
  complementary plane partitions, arXiv:2509.17064 (first-kind QTCPP only).
- Classical symmetric / transpose-complementary / totally symmetric plane-partition
  enumerations (Andrews, Stembridge, Eisenkoelbl) for background scope comparison.
