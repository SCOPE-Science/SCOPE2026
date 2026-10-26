# A sharp three-summand point-concentration phase transition under an atom cap

## Finding

Let \(X_1,X_2,X_3\) be independent, integer-valued random variables. Write \(Q(X)=\sup_{k\in\mathbb Z}\Pr(X=k)\). For any \(1/3\le\alpha\le1/2\), the exact sharp point-concentration bound under \(Q(X_i)\le\alpha\), for \(i=1,2,3\), is
\[
\sup_{(X_i),\,s\in\mathbb Z}\Pr(X_1+X_2+X_3=s)
=\begin{cases}
7\alpha^3-6\alpha^2+2\alpha,&1/3\le\alpha\le2/5,\\
3\alpha^2(1-\alpha),&2/5\le\alpha\le1/2.
\end{cases}
\]
The optimal arrangements change at the nontrivial threshold \(\alpha=2/5\).

## Assumptions and scope

The random variables are independent and integer-valued; their laws need not coincide, and their integer supports can be infinite or arbitrarily separated. Only the individual maximal-atom constraints \(Q(X_i)\le\alpha\) are assumed; no interval-concentration bound or moment assumption is needed. The theorem concerns exactly three summands and the stated closed interval of common atom caps, not other sample sizes or unequal caps.

Put \(\beta=1-2\alpha\) and \(t=\beta/\alpha\in[0,1]\). A three-point profile of type \((\beta,\alpha,\alpha)\) on sites \(0,1,2\) is denoted \(L\), and one of type \((\alpha,\alpha,\beta)\) is denoted \(R\). Zero-weight sites may be retained formally at the endpoint \(\alpha=1/2\).

## Proof

### Step 1: Reduction to three-point cap-saturated laws

For a fixed integer target \(s\), fix any two of the laws. The probability of reaching \(s\) is a linear functional \(\sum_k p(k)c_k\) in the remaining law, where \(c_k=\Pr(Y+Z=s-k)\in[0,1]\). Since the convolution is a probability mass function, \(c_k\to0\) as \(|k|\to\infty\). Under \(0\le p(k)\le\alpha\) and \(\sum_kp(k)=1\), a greedy rearrangement maximizes this functional by placing mass \(\alpha\) at each of its two largest coefficients and the remaining mass \(\beta\) at the third largest (arbitrary zero-coefficient sites may be used if needed). Indeed, transfer mass from any lower-ranked positive coordinate to a higher-ranked coordinate not yet at cap; this does not decrease the objective. Taking a limit of the finite transfers is valid by bounded convergence and \(\sum p(k)=1\); alternatively, direct rearrangement yields the same bound. At \(\alpha=1/3\), all three weights are equal; at \(\alpha=1/2\), the third has zero weight.

Replace the three laws successively in this manner. Each replacement cannot decrease the target probability, so it suffices to prove the bound for three arbitrary three-site support sets \(A_1,A_2,A_3\subset\mathbb Z\), each of size three, with weight \(\alpha\) at two heavy sites \(H_i\subset A_i\) and weight \(\alpha t\) at the remaining site. This reduction is for a fixed target, and so covers the maximum over targets as well.

### Step 2: Additive representation bounds

For a set triple \((B_1,B_2,B_3)\) and a fixed integer \(s\), let \(N(B_1,B_2,B_3;s)\) be the number of ordered solutions \(b_1+b_2+b_3=s\), with \(b_i\in B_i\). The elementary bounds are
\[
N(2,2,2)\le3,\quad N(3,2,2)\le4,\quad N(3,3,2)\le5,\quad N(3,3,3)\le7,
\]
where the arguments denote the three cardinalities, with arbitrary actual sets.

To see this, first count the representations of a sum from the first two sets. Two two-point sets have at most one sum with two representations, so their top two representation counts add to at most three. A three-point set plus a two-point set has each representation count at most two, so its top two counts add to at most four. For two three-point sets every count is at most three, and at most one sum has count three. Thus their top two counts add to at most five and their top three to at most seven. These four claims give the displayed bounds by choosing two or three target complements from the last set.

There is rigidity at seven: if \(N(A_1,A_2,A_3;s)=7\) with all three sets of size three, the first pair must have representation multiplicities at least \(3,2,2\). Three representations of the same sum for two three-element sets imply that both sets are translates/reflections of the same set. To have at least two further sums with two representations each, that set must be a three-term arithmetic progression. More explicitly, writing the first set \(\{a<b<c\}\), three representations of a fixed sum force the second set to be \(\{u-c,u-b,u-a\}\); the six off-central sums then have counts \(2\) only when \(b-a=c-b\). Consequently \(A_1,A_2\) are progressions with the same nonzero step. The third set must consist of the three complementary sites for the central sum and its two adjacent sums; hence \(A_3\) is an aligned three-term progression of the same step. Translating each set, reversing all three if needed, and dividing by the common step reduce the target to \(s=3\) and all three supports to \(\{0,1,2\}\).

### Step 3: Uniform upper envelope

For each \(i\), the unnormalized mass profile is \(1_{H_i}+t1_{A_i\setminus H_i}=(1-t)1_{H_i}+t1_{A_i}\). Expand the product over the three coordinates, grouping by the number of full sets \(A_i\). If the representation count \(N(A_1,A_2,A_3;s)\) is at most six, the four cardinality bounds yield
\[
\alpha^{-3}\Pr(X_1+X_2+X_3=s)
\le 3(1-t)^3+12t(1-t)^2+15t^2(1-t)+6t^3=3+3t.
\]

If \(N(A_1,A_2,A_3;s)=7\), the rigidity above reduces the count to coefficient \(z^3\) in \(\prod_{i=1}^3(1+z+z^2+(t-1)z^{\ell_i})\), where the light position \(\ell_i\) belongs to \(\{0,1,2\}\). Expanding all \(3^3=27\) choices of \((\ell_1,\ell_2,\ell_3)\) gives exactly six distinct possible polynomials:
\[
3+2t+2t^2,\quad 2+3t+2t^2,\quad 2+2t+3t^2,\quad
1+6t,\quad 2+4t+t^3,\quad 6t+t^3.
\]
All are bounded by \(3+2t+2t^2\) on \(0\le t\le1\). In the displayed order after the first, subtracting each from the first yields respectively \(1-t\), \(1-t^2\), \(2(1-t)^2\), \((1-t)(1-t+t^2)\), and \((1-t)(3-t+t^2)\), all nonnegative. This exhausts the full-support cases.

Combining both regimes establishes
\[
\Pr(X_1+X_2+X_3=s)
\le\alpha^3\max\{3+3t,\;3+2t+2t^2\}.
\]
The two expressions cross at \(t=1/2\) (and agree at \(t=0\)); since \(t=(1-2\alpha)/\alpha\), the interior crossing is \(\alpha=2/5\). Expanding both branches in \(\alpha\) gives exactly the piecewise formula in the Finding.

### Step 4: Equality examples

For \(1/3\le\alpha\le2/5\), let \(X_1,X_2\sim L\) and \(X_3\sim R\), independently. A coefficient calculation gives
\[
\Pr(X_1+X_2+X_3=3)=\alpha^3(3+2t+2t^2)=7\alpha^3-6\alpha^2+2\alpha.
\]
For \(2/5\le\alpha\le1/2\), take \(X_1,X_2,X_3\sim L\), independently. Then
\[
\Pr(X_1+X_2+X_3=4)=\alpha^3(3+3t)=3\alpha^2(1-\alpha).
\]
Both constructions obey \(Q(X_i)\le\alpha\), establishing sharpness for the full interval.

## Verification

Run `python3 verify_three_sum_concentration.py` using the standard library. Its exact rational assertions enumerate the 27 aligned-progression light placements, identify the six cubic polynomials, verify their pointwise order at a rational test grid, check the additive-count bounds on a finite test lattice, and check the displayed equality examples at six rational values of \(\alpha\), including both endpoints and the phase transition. The executed output was:

`VERIFY_OK polynomial_profiles=6 additive_bounds={0: 3, 1: 4, 2: 5, 3: 7} exact_witness_profiles=6`

The finite script checks arithmetic and the displayed polynomial list; the unrestricted claims follow from the direct combinatorial argument, not from finite lattice enumeration.

## Relationship to prior work

Kurauskas, *An asymptotically optimal bound for the concentration function of a sum of independent integer random variables* (arXiv:2603.11043v1, first public 2026-03-11), states the point-mass extremal conjecture for independent integer laws. It gives an asymptotic result and notes exact general cases at atom caps reciprocal to an integer and in the Bernoulli regime, leaving the intervening non-integer-cap regime unresolved. The result here proves the exact sharp three-summand formula in precisely the intervening \(1/3<\alpha<1/2\) regime, including the change of extremizer arrangement.

Juškevičius and Kurauskas, *On Littlewood–Offord theory for arbitrary distributions* (arXiv:1912.08770), prove an optimal common-cap point bound for even numbers of summands; their stated main theorem does not cover three summands. Juškevičius, *Sharp form of the Kolmogorov–Rogozin inequality* (arXiv:2201.09861), concerns interval-concentration hypotheses distinct from a cap on singleton atoms. Neither theorem entails the present odd-three-summand point formula.

## Limitations

Only exactly three independent integer-valued summands and a common cap \(\alpha\in[1/3,1/2]\) are covered. No claim is made for unequal caps, other ranges, more summands, vector-valued laws, or uniqueness of extremizers. The six-polynomial table is an exact finite classification, supplied with reproducible code; the unrestricted universal step is supported separately by the additive-representation proof. A differently formulated exact three-summand concentration result in the broader additive-probability literature remains a residual literature-priority risk.

## References

1. V. Kurauskas, *An asymptotically optimal bound for the concentration function of a sum of independent integer random variables*, arXiv:2603.11043v1, 2026-03-11, primary MSC 60C05. https://arxiv.org/abs/2603.11043
2. T. Juškevičius and V. Kurauskas, *On Littlewood–Offord theory for arbitrary distributions*, arXiv:1912.08770, 2019-12-18. https://arxiv.org/abs/1912.08770
3. T. Juškevičius, *Sharp form of the Kolmogorov–Rogozin inequality*, arXiv:2201.09861. https://arxiv.org/abs/2201.09861
