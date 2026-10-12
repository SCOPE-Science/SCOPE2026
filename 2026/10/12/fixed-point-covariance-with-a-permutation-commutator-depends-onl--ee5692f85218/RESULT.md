# Fixed-point covariance with a permutation commutator depends only on fixed support

## Finding

Let \(n\ge3\), let \(\eta\) be an arbitrary deterministic permutation of \([n]\), and draw \(\Pi\) uniformly from the symmetric group \(S_n\). Write \(f=\#\{i:\eta(i)=i\}\), and consider two random counts
\[
F=\#\{i:\Pi(i)=i\},\qquad
C_\eta=\#\{i:\Pi(\eta(i))=\eta(\Pi(i))\}.
\]
The second count is precisely the number of fixed points of the permutation commutator \(\eta^{-1}\Pi^{-1}\eta\Pi\). For every \(n\ge3\), without restriction on the cycle structure of \(\eta\),
\[
\boxed{\operatorname{Cov}(F,C_\eta)=\frac{f(n-f)}{(n-1)(n-2)}.}
\]
In particular the covariance depends **only** on the number of fixed points of \(\eta\), not on the remaining cycle structure; it is positive exactly when \(1\le f\le n-2\) and zero precisely when \(f=0\) or \(f=n\). The formally possible value \(f=n-1\) is not realized by a permutation. Over all deterministic \(\eta\in S_n\), the sharp upper bound is
\[
0\le \operatorname{Cov}(F,C_\eta)\le
\frac{\lfloor n^2/4\rfloor}{(n-1)(n-2)},
\]
attained, for example, when \(f=\lfloor n/2\rfloor\), with the remaining elements arranged in one nontrivial cycle.

There is a dependence/uncorrelatedness distinction: for **every** fixed-point-free \(\eta\in S_n\), the two counts are uncorrelated but not independent. Indeed \(F=n\) forces \(\Pi\) to be the identity and hence forces \(C_\eta=n\), while at least one permutation fails to commute with nonidentity \(\eta\), so \(\mathbb P(C_\eta<n)>0\). If a sequence satisfies \(f/n\to\alpha\in[0,1]\), then
\[
\operatorname{Cov}(F,C_\eta)\longrightarrow \alpha(1-\alpha).
\]

## Assumptions and scope

Here \([n]=\{1,\dots,n\}\), permutation composition is functional, and \(\Pi\) has probability \(1/n!\) at each element of \(S_n\). The reference permutation \(\eta\) is held fixed, not independently resampled. All formulae concern the finite distribution on permutations and exact covariance (not conditional covariance, independence, or covariance after Poisson approximation). The integer domain is \(n\ge3\); division by \(n-2\) makes the formula inappropriate at \(n=2\), where the symmetric group is abelian and the commutator count is constant.

## Proof

For each \(i\in[n]\), define \(V_i={\bf1}\{\Pi\eta(i)=\eta\Pi(i)\}\). Then \(C_\eta=\sum_iV_i\), and \(\mathbb E F=1\). We calculate \(\operatorname{Cov}(F,V_i)=\mathbb E(FV_i)-\mathbb E V_i\) by splitting the index set according to whether \(\eta(i)=i\).

**Case 1: \(i\) is fixed by \(\eta\).** The event \(V_i=1\) means \(\Pi(i)\) is one of the \(f\) fixed points of \(\eta\), so \(\mathbb EV_i=f/n\). If \(\Pi(i)=i\), the conditional expected total number of fixed points of \(\Pi\) is \(2\). If \(\Pi(i)=b\ne i\), the conditional expected fixed-point count is \((n-2)/(n-1)\), because exactly \(n-2\) remaining positions can map to themselves and each has chance \(1/(n-1)\). Thus
\[
\mathbb E(FV_i)=\frac1n\left(2+(f-1)\frac{n-2}{n-1}\right),\qquad
\operatorname{Cov}(F,V_i)=\frac{n-f}{n(n-1)}.
\]

**Case 2: \(i\) is moved by \(\eta\).** Put \(a=\eta(i)\ne i\), \(m=n-f\). For \(V_i=1\), the ordered pair of images must have the form \((\Pi(i),\Pi(a))=(b,\eta(b))\) for one of the \(m\) moved points \(b\); each distinct ordered pair has probability \(1/[n(n-1)]\). Write \(t_b=|\{i,a\}\cap\{b,\eta(b)\}|\). The two prescribed positions contribute exactly \(2{\bf1}\{b=i\}\) fixed points, and the remaining \(n-2\) positions contribute an expected \((n-4+t_b)/(n-2)\) fixed points. (There are \(n-4+t_b\) indices that are neither prescribed positions nor prescribed target values.) Hence
\[
\mathbb E(FV_i)=\frac1{n(n-1)}\sum_{b:\eta(b)\ne b}
\left(2{\bf1}\{b=i\}+\frac{n-4+t_b}{n-2}\right).
\]
Because each of \(i,a\) occurs exactly once as a moved point \(b\) and exactly once as \(\eta(b)\), we have \(\sum_bt_b=4\). The indicator sum is one. Therefore
\[
\mathbb E(FV_i)
=\frac{2+[m(n-4)+4]/(n-2)}{n(n-1)},
\qquad
\mathbb EV_i=\frac{m}{n(n-1)},
\]
and subtraction gives
\[
\operatorname{Cov}(F,V_i)=\frac{2f}{n(n-1)(n-2)}.
\]
The argument holds for all \(n\ge3\); an apparent negative intermediate count \(n-4+t_b\) never occurs for an admissible ordered pair.

Finally, summing the first covariance over \(f\) fixed indices and the second over \(n-f\) moved indices yields
\[
\operatorname{Cov}(F,C_\eta)
=\frac{f(n-f)}{n(n-1)}+\frac{2f(n-f)}{n(n-1)(n-2)}
=\frac{f(n-f)}{(n-1)(n-2)}.
\]
Nonnegativity, sign cases and the sharp upper bound follow from maximizing the integer product \(f(n-f)\) over feasible \(f\). The nonindependence argument in the Finding uses the fact that the center of \(S_n\) is trivial for \(n\ge3\). The limiting statement follows by dividing numerator and denominator by \(n^2\). This completes the proof.

As a normalization check, the same event probabilities give
\[
\mathbb EC_\eta=\frac{f^2}{n}+\frac{(n-f)^2}{n(n-1)}
=1+\frac{(f-1)^2}{n-1},
\]
which agrees with the previously known commutator fixed-point mean.

## Verification

The standalone standard-library script `verify_commutator_covariance.py` exhaustively evaluates the pair \((F,C_\eta)\) over every \(\Pi\) for every \(\eta\in S_n\) and \(3\le n\le6\), plus selected reference permutations for \(n=7,8\). It uses exact rational arithmetic, checks the joint mixed moment, the known marginal mean, the covariance identity, the sharp finite maximum, and a concrete lack-of-independence witness. Run `python3 verify_commutator_covariance.py`; the script prints `PASS` only when all assertions succeed. Enumeration checks finite examples; the displayed proof establishes all \(n\ge3\).

## Relationship to prior work

Diaconis, Evans and Graham introduced the commutator fixed-point count in the study of unseparated pairs, and in Section 6 analyzed its marginal expectation and Poisson approximation for fixed \(\eta\). Fulman's Theorem 3.5 gives all **marginal moments** of \(C_\eta\), including a second moment that also depends on the number of 2-cycles of \(\eta\). Moreno and Rivera enumerate permutations by their number of noncommuting points for selected classes of reference permutations. Those marginal results do not specify the same-permutation mixed moment \(\mathbb E[F C_\eta]\) or the all-cycle-type covariance classification here. No claim is made that the commutator-count definition, the marginal mean, the general character method, or the unseparated-pair distribution is new.

## Limitations

The formula assumes exactly uniform \(\Pi\) and deterministic \(\eta\); it does not establish independence, a joint limit theorem, or higher mixed moments, and its covariance universality need not extend to non-uniform permutations. Although the cited primary literature was materially compared, a hidden older character-theoretic mixed-moment identity or equivalent formulation could establish historical precedence. No historical priority claim beyond the literature comparison is independently established.

## References

1. P. Diaconis, S. N. Evans and R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Statistics Technical Report 822 (dated 2013-08-01); arXiv:1308.5459; *Advances in Applied Mathematics* 61 (2014), 102–124, Section 6. Primary MSC 60C05.
2. J. Fulman, *Fixed points of non-uniform permutations and representation theory of the symmetric group*, arXiv:2406.12139 (2024), Theorem 3.5.
3. R. Moreno and L. M. Rivera, *Blocks in cycles and k-commuting permutations*, *SpringerPlus* 5 (2016), article 1949, doi:10.1186/s40064-016-3638-7.
