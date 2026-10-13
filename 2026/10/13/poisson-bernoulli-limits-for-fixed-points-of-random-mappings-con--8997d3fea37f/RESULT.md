# Poisson–Bernoulli limits for fixed points of random mappings conditioned on their fibres

## Finding

For each integer \(n\ge 1\), prescribe an arbitrary partition of \([n]=\{1,\ldots,n\}\) into nonempty blocks \(B_{1,n},\ldots,B_{k_n,n}\). Select a mapping \(f_n:[n]\to[n]\) uniformly among those whose nonempty fibres are **exactly** these blocks. Equivalently, assign distinct uniformly sampled output labels to the blocks. Let \(F_n=|\{v\in[n]:f_n(v)=v\}|\), and sort the block sizes in decreasing order:

\[
s_{1,n}\ge\cdots\ge s_{k_n,n}\ge1,\qquad p_{i,n}=s_{i,n}/n,
\]

padding the profile with zeros. If \(p_{i,n}\to a_i\) for every fixed \(i\), then \(a_1\ge a_2\ge\cdots\ge0\), \(\sum_i a_i\le1\), and, with \(\delta=1-\sum_i a_i\),

\[
\boxed{F_n\ \xrightarrow{\mathrm d}\ Z=\operatorname{Poisson}(\delta)+\sum_{i\ge1}\operatorname{Bernoulli}(a_i),}
\]

where all variables on the right are mutually independent. The Bernoulli sum is almost surely finite. Every sequence of prescribed partitions has subsequences with such limits; conversely, every nonincreasing summable profile of nonnegative \(a_i\) with \(\sum_i a_i\le1\) is attained by some prescribed-partition sequence.

The limit criterion is exact:

\[
\boxed{F_n\xrightarrow{\mathrm d}\operatorname{Poisson}(1)\quad\Longleftrightarrow\quad\max_i s_{i,n}/n\longrightarrow0.}
\]

This characterizes how individual macroscopic fibres survive as Bernoulli contributions while microscopic fibres combine into a Poisson contribution. The classification, not the elementary finite enumeration underpinning it, is the claimed result.

## Assumptions and scope

The partition may vary arbitrarily with \(n\); neither independence, exchangeability, nor boundedness of block sizes is imposed. Probability is over the uniform injective assignment of distinct target labels to the prescribed, labeled blocks. The asymptotic statements mean \(n\to\infty\) through positive integers. Convergence of the sorted normalized profile is coordinatewise, not convergence in total mass; missing limiting mass is \(\delta\). No assertion is made about deterministic target labels or mappings sampled from a different weighting scheme.

For integers \(0\le r\le k_n\), define \((x)_r=x(x-1)\cdots(x-r+1)\) with \((x)_0=1\), and let \(e_r\) be the elementary symmetric polynomial with \(e_0=1\). The following exact identities also hold:

\[
\mathbb E[(F_n)_r]=\frac{r!\,e_r(s_{1,n},\ldots,s_{k_n,n})}{(n)_r},
\qquad
\mathbb E F_n=1,
\]

and for \(n\ge2\),

\[
\operatorname{Var}(F_n)=\frac{n^2-\sum_i s_{i,n}^2}{n(n-1)}.
\]

## Proof

**1. Exact factorial moments.** For block \(B_{i,n}\), let \(I_{i,n}\) indicate whether its assigned image label lies in that block. At most one vertex in a block can be fixed, and the block has exactly one fixed point iff \(I_{i,n}=1\). Hence \(F_n=\sum_i I_{i,n}\). For distinct indices \(i_1,\ldots,i_r\), the target labels are chosen uniformly without replacement, and the blocks are disjoint. Therefore

\[
\mathbb P(I_{i_1,n}=\cdots=I_{i_r,n}=1)
=\frac{\prod_{j=1}^r s_{i_j,n}}{(n)_r}.
\]

Summing over ordered distinct block indices proves the factorial-moment identity. Taking \(r=1,2\) proves the expectation and variance above. In particular, the block indicators are generally not independent: for distinct blocks their covariance is \(p_{i,n}p_{j,n}/(n-1)\).

**2. Limits of symmetric polynomials.** Put \(H_n(t)=\prod_i(1+p_{i,n}t)\). For fixed \(J\), coordinatewise convergence gives convergence of the first \(J\) factors and of their total mass. For \(t\) in an arbitrary fixed compact subset of the complex plane and \(J\) sufficiently large, all tail factors satisfy \(|tp_{i,n}|<1/2\) for large \(n\). Uniformly on that compact set,

\[
\left|\sum_{i>J}\log(1+tp_{i,n})-t\sum_{i>J}p_{i,n}\right|
\le C_t\sum_{i>J}p_{i,n}^2
\le C_t p_{J+1,n}.
\]

Because \(a_{J+1}\to0\) and \(\sum_i a_i\le1\), first letting \(n\to\infty\), then \(J\to\infty\), yields locally uniform convergence

\[
H_n(t)\longrightarrow H(t)=e^{\delta t}\prod_{i\ge1}(1+a_it).
\]

The product is entire because \(\sum_i a_i<\infty\). By Cauchy's coefficient formula, \(e_r(p_{1,n},\ldots,p_{k_n,n})\to[t^r]H(t)\) for each fixed \(r\). Since \(n^r/(n)_r\to1\), the exact finite formula gives

\[
\mathbb E[(F_n)_r]\longrightarrow r![t^r]H(t)=\mathbb E[(Z)_r].
\]

The proposed \(Z\) is well defined: the expected number of its Bernoulli successes is \(\sum_i a_i\le1\), and its moment-generating function is finite at every real argument. The convergence of all factorial moments thus gives convergence of all ordinary moments, and moment determinacy of \(Z\) gives \(F_n\Rightarrow Z\).

**3. Completeness of the profile description.** The sorted profiles belong to \([0,1]^{\mathbb N}\), so successive subsequence extraction and a diagonal argument provide coordinatewise convergence along a subsequence. Conversely, fix any nonincreasing \((a_i)\) with sum at most one. Retain the first \(J_n\) positive entries with \(a_i\ge1/n\), taking \(J_n\le\lfloor\sqrt n\rfloor\) and \(J_n\to\infty\) unless only finitely many entries are positive. Form blocks of sizes \(\lfloor na_i\rfloor\) for these indices, and partition the remaining elements into singleton blocks. Each fixed positive mass eventually occurs among these blocks with normalized size tending to \(a_i\); all unrepresented sizes are singletons or smaller subsequent masses. Consequently, the sorted profile converges coordinatewise to \((a_i)\). This establishes attainability, including profiles with dust \(\delta>0\).

**4. Sharp Poisson criterion.** If \(\max_i p_{i,n}\to0\), every fixed profile coordinate tends to zero and the limit above reduces to \(\operatorname{Poisson}(1)\). Conversely, suppose \(F_n\Rightarrow\operatorname{Poisson}(1)\). For every fixed \(r\) and sufficiently large \(n\),

\[
\mathbb E[(F_n)_r]\le\frac{n^r}{(n)_r},
\]

because \(r!e_r(s_{1,n},\ldots,s_{k_n,n})\le(\sum_i s_{i,n})^r=n^r\). Uniform boundedness of moments through order four implies uniform integrability of the second moment. Hence \(\operatorname{Var}(F_n)\to1\). The exact variance identity gives \(\sum_i p_{i,n}^2\to0\), and therefore \(\max_i p_{i,n}\to0\). This proves both directions.

## Verification

Run `python checker.py` from the directory containing this document and the supplied standalone file. It exhaustively enumerates every set partition through six elements and every injective assignment of target labels for each partition, independently recomputing all factorial moments from the resulting fixed-point frequencies. It also compares exact low-order moments with the limiting Poisson–Bernoulli predictions for one- and two-macroscopic-fibre examples. On the supplied checker the run reported 278 exhaustive partition/assignment cases, 1,154 exact factorial-moment comparisons, and 54 numerical limit-profile comparisons. The infinite and equivalence assertions are proved analytically above, not by enumeration.

## Relationship to prior work

Hansen and Jaworski's *Random Mappings With Exchangeable In-Degrees* (first online publication September 4, 2007) defines uniform mappings with prescribed in-degree data in its Section 2, Eq. (2.1), and develops cyclic-point, connected-component, and component-size laws in Section 3. Its finite uniform conditional model provides a directly related counting framework; elementary factorial enumeration is not asserted to be new. Their *Local Properties of Random Mappings with Exchangeable In-Degrees* treats predecessor/successor structure of distinguished vertices, not this fixed-point weak-limit classification. Their *Structural Transition in Random Mappings* studies globally constrained in-degrees bounded by two and corresponding cyclic/component limits; that restricted setting forces the microscopic-fibre side of the present criterion. Classical rook-polynomial and weighted random-mapping perspectives explain portions of the finite calculations and possible proof reductions; the contribution claimed here is the arbitrary-profile Poisson–Bernoulli limit description and sharp if-and-only-if Poisson criterion for an exactly prescribed kernel partition.

## Limitations

No total-variation convergence rate is established. The classification concerns the number of fixed points, not the joint structure of higher cycles. Literature coverage cannot guarantee absence of implicit consequences in broader classical random-mapping or rook-theoretic results. The exact finite factorial identity is a straightforward consequence of uniform sampling without replacement and is not presented as independently novel. The work has received no independent scientific audit.

## References

1. J. C. Hansen and J. Jaworski, *Random Mappings With Exchangeable In-Degrees*, Random Structures & Algorithms 33 (2008), 105–126. DOI: `10.1002/rsa.20187`. First published online 2007-09-04; relevant model Eq. (2.1) and cyclic/component results in Section 3.
2. J. C. Hansen and J. Jaworski, *Local Properties of Random Mappings with Exchangeable In-Degrees*, Advances in Applied Probability 40 (2008), 183–205. DOI: `10.1239/aap/1208358892`. Relevant local-structure results in Section 3.
3. J. C. Hansen and J. Jaworski, *Structural Transition in Random Mappings*, Electronic Journal of Combinatorics 21 (2014), P1.18. DOI: `10.37236/3572`. Relevant bounded-in-degree and component-limit results.
