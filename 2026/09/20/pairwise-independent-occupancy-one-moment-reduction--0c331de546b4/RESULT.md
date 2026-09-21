# One-moment reduction for symmetric occupancy statistics under pairwise-independent uniforms

## Statement

Let \(q\ge 2\) and \(n\ge 2\), and let
\[
X=(X_1,\ldots,X_n)\in [q]^n
\]
have uniform one-dimensional marginals. Call the law *pairwise independent uniform* if every \((X_i,X_j)\), \(i\ne j\), is uniform on \([q]^2\).

For an occupancy type \(\lambda=(\lambda_1,\ldots,\lambda_r)\vdash n\) with \(r\le q\), define its pair-collision count
\[
c(\lambda)=\sum_{a=1}^r \binom{\lambda_a}{2},
\qquad M=\binom n2.
\]
Let \(U_\lambda\) denote the uniform law on all vectors in \([q]^n\) having occupancy multiset \(\lambda\).

### Theorem: one-moment reduction

Let \(F:[q]^n\to\mathbb R\) be invariant under permutations of the coordinates and under a common permutation of the \(q\) labels. Thus \(F(x)=f(\lambda(x))\) depends only on the occupancy type. Then the exact minimum and maximum of \(\mathbb E F(X)\) over all pairwise-independent uniform laws are the minimum and maximum of the finite linear program
\[
\sum_\lambda w_\lambda f(\lambda)
\]
subject to
\[
w_\lambda\ge 0,\qquad
\sum_\lambda w_\lambda=1,\qquad
\sum_\lambda w_\lambda c(\lambda)=\frac{M}{q}.
\]
Every feasible weight vector is realized by the mixture \(\sum_\lambda w_\lambda U_\lambda\). Consequently, each linear extremum has a realizing law supported on at most two occupancy types.

Thus, after symmetry reduction, *all* pairwise-independence constraints collapse to the single scalar condition
\[
\mathbb E C=\frac{\binom n2}{q},
\qquad
C=\sum_{1\le i<j\le n}\mathbf 1\{X_i=X_j\}.
\]

## Proof

Start from any pairwise-independent uniform law. Average it over all coordinate permutations and all common label permutations. Pairwise independence and uniform marginals are preserved, while the expectation of every occupancy-invariant statistic \(F\) is unchanged. Hence it is enough to optimize over laws invariant under both symmetry groups.

The orbits of this action on \([q]^n\) are exactly the occupancy types \(\lambda\vdash n\) with at most \(q\) parts. Therefore every invariant law is uniquely a mixture
\[
P=\sum_\lambda w_\lambda U_\lambda.
\]

Fix an orbit law \(U_\lambda\), and a coordinate pair \(i\ne j\). Every vector of type \(\lambda\) has exactly \(c(\lambda)\) equal-coordinate pairs among the \(M\) unordered coordinate pairs. Coordinate symmetry therefore gives
\[
\Pr_{U_\lambda}(X_i=X_j)=\frac{c(\lambda)}{M}.
\]
Common label symmetry then gives, for every \(a\in[q]\),
\[
\Pr_{U_\lambda}(X_i=a,X_j=a)
=\frac{c(\lambda)}{Mq},
\]
and, for every \(a\ne b\),
\[
\Pr_{U_\lambda}(X_i=a,X_j=b)
=\frac{1-c(\lambda)/M}{q(q-1)}.
\]

For a mixture \(P=\sum_\lambda w_\lambda U_\lambda\), write
\[
\bar c=\sum_\lambda w_\lambda c(\lambda).
\]
The preceding formulas show that every ordered pair \((X_i,X_j)\) is uniform on \([q]^2\) if and only if
\[
\frac{\bar c}{M}=\frac1q,
\]
i.e. if and only if \(\bar c=M/q\). This proves both necessity and sufficiency of the stated one-moment constraint for the symmetrized law, and therefore proves the extremal reduction for any occupancy-invariant objective.

Finally, the feasible set is a simplex cut by one additional scalar equality. A linear objective has an optimum at an extreme point, and every extreme point has support on at most two occupancy types. Equivalently, the optimization is the lower or upper convex envelope of the finitely many points \((c(\lambda),f(\lambda))\) evaluated at \(c=M/q\).

## Exact birthday / collision-free probability

A direct consequence is an exact finite-sample answer to the collision-free problem.

### Corollary

For every \(2\le n\le q\), among all pairwise-independent uniform \([q]\)-valued random variables,
\[
\boxed{
\max\!\left(0,1-\frac{\binom n2}{q}\right)
\le
\Pr(X_1,\ldots,X_n\text{ are all distinct})
\le
1-\frac1q
}
\]
and both endpoints are attained. In fact, every probability in this interval is attained.

Equivalently,
\[
\boxed{
\frac1q
\le
\Pr(\exists i<j:X_i=X_j)
\le
\min\!\left(1,\frac{\binom n2}{q}\right)
}.
\]

### Proof of the corollary

Let \(D\) be the all-distinct event and let \(p=\Pr(D)\). The event \(D\) is the unique occupancy type with collision count \(C=0\). On \(D^c\),
\[
1\le C\le M.
\]
Since pairwise independence fixes \(\mathbb E C=M/q\),
\[
1-p\le \frac{M}{q}\le M(1-p).
\]
This is exactly
\[
\max(0,1-M/q)\le p\le 1-1/q.
\]

It remains to prove sharpness. Let

- \(U_0\) be the uniform law on injections \([n]\to[q]\), with occupancy \((1^n)\) and \(C=0\);
- \(U_1\) be the uniform law on occupancy type \((2,1^{n-2})\), with \(C=1\);
- \(U_M\) be the uniform law on constant vectors, with occupancy \((n)\) and \(C=M\).

These orbit laws exist for \(n\le q\). The upper endpoint is realized by
\[
\left(1-\frac1q\right)U_0+\frac1q U_M,
\]
whose mean collision count is \(M/q\), so the theorem implies pairwise independence. Its all-distinct probability is \(1-1/q\).

Write \(\mu=M/q\). If \(\mu\le1\), the lower endpoint is realized by
\[
(1-\mu)U_0+\mu U_1,
\]
which has all-distinct probability \(1-\mu\). If \(\mu\ge1\), then for \(M>1\) put
\[
t=\frac{\mu-1}{M-1}
\]
and use
\[
(1-t)U_1+tU_M.
\]
This has mean collision count \(\mu\) and no all-distinct mass, realizing the lower endpoint \(0\). The boundary case \(\mu=1\) is simply \(U_1\). Convex mixtures of the lower- and upper-endpoint laws preserve the same pairwise-uniform two-coordinate marginals, so every intermediate value is attainable.

For example, when \(n=q\), mutual independence gives
\[
\Pr(D)=\frac{q!}{q^q}\sim \sqrt{2\pi q}\,e^{-q},
\]
whereas pairwise independence alone permits the full interval
\[
0\le \Pr(D)\le 1-\frac1q
\]
for \(q\ge3\).

## Relation to prior literature

Carter and Wegman's universal hashing framework and later treatments of pairwise-independent hashing make pair collisions a standard object. Luby and Wigderson explicitly use pairwise independence to obtain
\[
\mathbb E C=\binom n2/q
\]
and then a collision-free guarantee from the first moment. The corollary above shows that this familiar first-moment guarantee is globally sharp over the entire class of pairwise-independent uniform laws, and also supplies the sharp opposite inequality \(\Pr(\text{collision})\ge 1/q\).

Orthogonal arrays of strength two are the equal-weight finite-sample counterpart of pairwise-independent uniform vectors. Modern work and reviews on orthogonal arrays emphasize constructions, classification and design criteria. Recent work on collision-flat universal hashing studies collision profiles and seed-size/design questions. These provide closely related languages for the same pairwise-marginal constraint, but the sources inspected did not state the one-moment occupancy reduction above or the exact all-distinct interval for arbitrary \(2\le n\le q\).

There is also a separate literature on tight bounds for unions of pairwise-independent Bernoulli events. That hypothesis does not directly apply to the collision indicators \(\mathbf 1\{X_i=X_j\}\): pairwise independence of the variables \(X_i\) does not make the family of collision indicators pairwise independent, because intersections of overlapping collision events depend on higher-order joint laws.

## Verification

The proof is exact and does not depend on numerical computation. The accompanying verification script enumerates all vectors for \(2\le q\le6\), constructs the endpoint orbit mixtures with exact rational arithmetic, checks every two-coordinate joint probability against \(1/q^2\), and checks the claimed all-distinct endpoint probabilities.

## Limitations

- The reduction applies to objectives invariant under coordinate permutations and a common relabeling of the alphabet. It does not characterize arbitrary nonsymmetric objectives or all nonsymmetric pairwise-independent laws.
- The result concerns a finite uniform alphabet and pairwise independence. No analogous one-moment characterization is claimed for nonuniform marginals or higher \(k\)-wise independence.
- The all-distinct corollary is stated for \(n\le q\); for \(n>q\) the all-distinct probability is identically zero.
- Originality is asserted only to the best of our knowledge. The symmetrization and convexity argument is elementary, so an equivalent formulation could exist under the languages of finite exchangeability, weighted orthogonal arrays, universal hashing, or probability bounds without using the same terminology.

## References

1. J. L. Carter and M. N. Wegman, “Universal Classes of Hash Functions,” *Journal of Computer and System Sciences* 18 (1979), 143–154. https://research.ibm.com/publications/universal-classes-of-hash-functions--1
2. M. Luby and A. Wigderson, “Pairwise Independence and Derandomization,” *Foundations and Trends in Theoretical Computer Science* 1(4) (2005), 237–301. https://doi.org/10.1561/0400000009
3. N. Etemadi and M. Kaminski, “Strong law of large numbers for 2-exchangeable random variables,” *Statistics & Probability Letters* 28 (1996), 245–250. https://doi.org/10.1016/0167-7152(95)00131-X
4. A. K. Ramachandra and K. Natarajan, “Tight Probability Bounds with Pairwise Independence,” *SIAM Journal on Discrete Mathematics* 37 (2023), 516–555. https://doi.org/10.1137/21M1408294
5. M. Wiese and H. Boche, “ε-Almost collision-flat universal hash functions and mosaics of designs,” arXiv:2306.04583 (2023). https://arxiv.org/abs/2306.04583
6. N. A. Harvey and C. Sahami, “Explicit Orthogonal Arrays and Universal Hashing with Arbitrary Parameters,” STOC 2024; arXiv:2405.08787. https://arxiv.org/abs/2405.08787
7. C. D. Lin and J. Stufken, “Orthogonal Arrays: A Review,” *WIREs Computational Statistics* 17 (2025), e70029. https://doi.org/10.1002/wics.70029
