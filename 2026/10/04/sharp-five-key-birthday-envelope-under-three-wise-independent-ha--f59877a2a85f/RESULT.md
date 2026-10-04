# Sharp five-key birthday envelope under three-wise-independent hashing

## Finding

Let \(q\ge5\), and let
\[
Y_1,\ldots,Y_5
\]
be three-wise-independent random variables, each uniform on a \(q\)-point
alphabet. Then
\[
\boxed{
\max\!\left\{0,\frac{(q-1)(q-9)}{q^2}\right\}
\le
\Pr(Y_1,\ldots,Y_5\text{ are all distinct})
\le
\frac{q^2-5q+10}{q^2}.
}
\]

Both endpoints are attained for every \(q\ge5\), and every value between them
is attained.

Thus three-wise independence does not determine the five-key birthday
probability. Nevertheless, it restricts that probability to an exact interval
whose width is of order \(1/q\), and whose lower endpoint becomes positive
precisely at \(q=10\).

## Assumptions and scope

The five hash values are exactly uniform on a common \(q\)-point alphabet and
every three distinct coordinates are mutually independent. No assumption of
four-wise or five-wise independence is made.

The theorem concerns arbitrary three-wise-independent joint laws. It is not a
claim specifically about simple tabulation hashing, although the five-key
dependence phenomena highlighted in the simple-tabulation literature motivate
the question.

The restriction \(q\ge5\) ensures that every occupancy type of five labeled
keys used in the extremal constructions is available.

## Proof

Average the joint law over all permutations of the five coordinates and all
permutations of the \(q\) output symbols. This symmetrization preserves
three-wise independence, uniform marginals, and the event that all five values
are distinct.

For a symmetrized law, only the occupancy partition of five matters. Write the
seven possible types as
\[
A=1+1+1+1+1,\quad
B=2+1+1+1,\quad
C=2+2+1,\quad
D=3+1+1,
\]
\[
E=3+2,\quad
F=4+1,\quad
G=5.
\]

For an occupancy vector, let \(T_2\) be the number of equal unordered pairs of
coordinates and let \(T_3\) be the number of equal unordered triples. Their
values on the seven types are
\[
\begin{array}{c|rrrrrrr}
\text{type}&A&B&C&D&E&F&G\\
\hline
T_2&0&1&2&3&4&6&10\\
T_3&0&0&0&1&1&4&10.
\end{array}
\tag{1}
\]

Three-wise independence gives
\[
\mathbb E T_2
=
\binom52\frac1q
=
\frac{10}{q},
\qquad
\mathbb E T_3
=
\binom53\frac1{q^2}
=
\frac{10}{q^2}.
\tag{2}
\]

Let
\[
I=\mathbf 1_{\{\text{at least one collision}\}}
=
1-\mathbf 1_A.
\]
A direct check of the seven rows in (1) gives the two pointwise inequalities
\[
\frac12T_2-T_3\le I
\tag{3}
\]
and
\[
I\le T_2-\frac9{10}T_3.
\tag{4}
\]
Taking expectations and using (2),
\[
\Pr(I=1)\ge
\frac5q-\frac{10}{q^2},
\]
so
\[
\Pr(A)
\le
1-\frac5q+\frac{10}{q^2}
=
\frac{q^2-5q+10}{q^2}.
\tag{5}
\]
Similarly,
\[
\Pr(I=1)\le
\frac{10}{q}-\frac9{q^2},
\]
hence
\[
\Pr(A)
\ge
\frac{(q-1)(q-9)}{q^2}.
\tag{6}
\]
Probability is nonnegative, so the lower bound is the positive part of (6).

It remains to prove sharpness and genuine three-wise independence.

For the upper endpoint, use the occupancy probabilities
\[
p_A=\frac{q^2-5q+10}{q^2},
\qquad
p_C=\frac{5(q-4)}{q^2},
\qquad
p_E=\frac{10}{q^2},
\tag{7}
\]
with all other type probabilities zero. These masses are nonnegative for
\(q\ge5\), sum to one, and satisfy (2). Equality holds in (3) on exactly the
types used in (7).

For the lower endpoint when \(q\ge9\), use
\[
p_A=\frac{(q-1)(q-9)}{q^2},
\qquad
p_B=\frac{10(q-1)}{q^2},
\qquad
p_G=\frac1{q^2},
\tag{8}
\]
with all other masses zero. These masses sum to one and satisfy (2). Equality
holds in (4) on the types used in (8).

For \(5\le q\le9\), the value zero is attained by
\[
p_B=\frac{2(q-1)(q-4)}{q^2},
\qquad
p_C=\frac{(q-1)(9-q)}{q^2},
\qquad
p_G=\frac1{q^2},
\tag{9}
\]
again with all other masses zero. The three numbers in (9) are nonnegative,
sum to one, and satisfy (2).

To realize any such occupancy mixture as an actual joint law, condition on the
chosen type, choose uniformly a set partition of the five coordinate labels
with those block sizes, and then assign distinct output symbols uniformly to
the blocks. The resulting law is invariant under coordinate permutations and
output-symbol permutations.

For any fixed pair of coordinates,
\[
\Pr(Y_i=Y_j)
=
\frac{\mathbb E T_2}{\binom52}
=
\frac1q.
\]
For any fixed triple,
\[
\Pr(Y_i=Y_j=Y_k)
=
\frac{\mathbb E T_3}{\binom53}
=
\frac1{q^2}.
\]
Output-symbol symmetry makes each equal pair value have probability \(1/q^2\).
For three coordinates, the all-equal vectors each have probability \(1/q^3\);
each specified exactly-two-equal pattern has total probability
\[
\frac1q-\frac1{q^2}
=
\frac{q-1}{q^2}
\]
and therefore assigns probability \(1/q^3\) to each of its
\(q(q-1)\) labeled output vectors. The remaining all-distinct triples have
total probability
\[
\frac{(q-1)(q-2)}{q^2}
\]
and therefore assign probability \(1/q^3\) to each of their
\(q(q-1)(q-2)\) output vectors. Hence every ordered triple is uniform on the
\(q^3\) possible values, which is exactly three-wise independence.

Finally, convex mixtures of two three-wise-independent laws with the same
uniform three-coordinate marginals remain three-wise independent. Mixing the
upper and lower endpoint laws therefore realizes every intermediate
collision-free probability.

## Verification

A standalone exact-rational checker accompanies the theorem. It verifies the
two pointwise occupancy inequalities, the endpoint mass formulas, all collision
moments, and the claimed interval over a large symbolic range of alphabet
sizes.

It also explicitly enumerates the complete five-coordinate joint law for
small alphabets at the upper endpoint, lower endpoint, and midpoint, and checks
all ten three-coordinate marginals against the uniform law using exact
rational arithmetic.

The finite replay is supplementary. The proof for all \(q\ge5\) is the
occupancy reduction, inequalities (3)-(4), and the explicit endpoint
constructions.

## Relationship to prior work

Pătraşcu and Thorup emphasize that simple tabulation hashing is only
three-independent, yet can exhibit stronger application-level behavior. In
their discussion of fourth-moment bounds they single out sets of five keys:
one key can have a hash code independent of the other four in their specific
scheme. That five-key observation motivates asking what three-wise independence
alone permits for a basic five-key collision event.

Benjamini, Gurel-Gurevich, and Peled develop a general extremal framework for
\(k\)-wise-independent distributions, including linear-programming duality and
classical moment methods. Their inspected results concern Boolean functions and
moment constraints, not the \(q\)-ary five-key occupancy polytope or the exact
birthday interval above.

A published result on pairwise-independent uniform allocations gives a
one-moment reduction for occupancy-invariant statistics and an all-distinct
envelope under pairwise independence. The present theorem uses the additional
triple-collision moment forced by three-wise independence. Its sharp upper
extremizer uses the occupancy types \(2+2+1\) and \(3+2\), while its lower
threshold occurs at \(q=9\); these features are not implied by the pairwise
one-moment envelope.

A separate four-key three-wise-independent birthday calculation determines a
different seven-to-five occupancy reduction and different endpoint formulas.
The five-key theorem here requires the new occupancy types \(2+2+1\),
\(3+2\), and \(5\), and the dual inequalities (3)-(4); it is not a corollary of
the four-key interval.

## Limitations

The theorem is specific to five keys. For six or more keys the occupancy
polytope has additional partition types, and the supporting inequalities can
change.

The result treats arbitrary three-wise-independent uniform hash values. A
particular hashing construction may obey additional algebraic restrictions and
therefore have a smaller attainable interval.

The originality assessment used targeted searches over limited-independence,
birthday, collision-free, occupancy, and hashing terminology together with
inspection of the closest primary texts and published related results. An
equivalent five-key formula could exist under different design-theoretic
terminology not captured by those searches.

## References

1. M. Pătraşcu and M. Thorup, “The Power of Simple Tabulation Hashing,”
   arXiv:1011.5200, first submitted 2010-11-23.
2. I. Benjamini, O. Gurel-Gurevich, and R. Peled, “On K-wise Independent
   Distributions and Boolean Functions,” arXiv:1201.3261, submitted
   2012-01-16.
3. J. L. Carter and M. N. Wegman, “Universal Classes of Hash Functions,”
   *Journal of Computer and System Sciences* 18 (1979), 143–154.
