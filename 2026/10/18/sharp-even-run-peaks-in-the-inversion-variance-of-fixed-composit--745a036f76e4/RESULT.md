# Sharp even-run peaks in the inversion variance of fixed-composition binary words

## Finding

Sample a binary word uniformly among all words with exactly \(m\ge1\) ones and \(n\ge1\) zeros. Let \(U\) count ordered pairs of positions containing a one followed later by a zero, and let \(R\) count maximal constant-symbol runs. Write \(N=m+n\) and \(P=mn\). The conditional mean is completely insensitive to the run count:
\[
\mathbb E[U\mid R=r]=\frac P2
\]
for every feasible \(r\). In sharp contrast, its conditional variance exhibits strict parity oscillation.

For each feasible even run count \(r=2k\), where \(1\le k\le\min(m,n)\), the exact variance is
\[
V_{2k}:=\operatorname{Var}(U\mid R=2k)
=\frac{P\left[(k+2)(2P-(k-1)N)+k(k-1)\right]}{12k(k+1)}.
\tag{1}
\]
For each feasible odd count \(r=2k+1\), where \(1\le k\le\min(m,n)\) and \(N>2k\), it is
\[
V_{2k+1}=\frac{P}{12(k+1)}\left(2P-k(N-1)-1+\frac{N^2-8P+2kN}{N-2k}\right).
\tag{2}
\]
There are no one-run words when both symbol counts are positive. Consequently, these expressions cover every feasible conditional run count.

**Sharp parity and monotonicity conclusions.** Every feasible even run count is a strict local maximum of conditional inversion variance relative to each feasible adjacent odd run count:
\[
V_{2k}>V_{2k+1}\quad\text{if }N>2k,
\qquad V_{2k}>V_{2k-1}\quad\text{if }k\ge2.
\tag{3}
\]
Along even counts, variance falls strictly:
\[
V_{2k}>V_{2k+2}\qquad(1\le k<\min(m,n)).
\tag{4}
\]
For example, with eight ones and eight zeros, the respective conditional variances at three, four, and five runs are \(256\), \(400\), and \(144\). Thus learning an additional run can increase inversion uncertainty sharply, despite leaving the conditional expected inversion count unchanged.

## Assumptions and scope

The word is uniform **conditional on the exact two class sizes**; no i.i.d. unconditional model or random class sizes are assumed. The statistic \(U\) is the inversion count of the binary word and, up to exchanging which symbol is called first, a standard two-sample Mann–Whitney pair-count/rank-sum statistic. The statistic \(R\) is the ordinary two-sample Wald–Wolfowitz number of runs. Conditioning is only on values of \(R\) that have positive probability. For even \(2k\), feasibility is \(1\le k\le\min(m,n)\). For odd \(2k+1\), feasibility is \(1\le k\le\min(m,n)\) and \(N>2k\). Formulae apply to all positive integer class sizes, without asymptotic approximations.

## Proof

**(i) Uniform composition moments.** For a uniform positive integer composition \(A=(A_1,\ldots,A_s)\) of an integer \(M\ge s\), exchangeability and stars-and-bars give
\[
\mathbb E A=\frac Ms\mathbf1_s,\qquad
\operatorname{Cov}(A)=\frac{M(M-s)}{s(s+1)}\left(I_s-\frac{\mathbf1_s\mathbf1_s^\top}{s}\right).
\tag{5}
\]
To check the coefficient directly, subtract one from each part and use the uniform weak-composition second factorial moments
\(\mathbb E[(A_i-1)(A_i-2)]=2(M-s)(M-s-1)/(s(s+1))\), together with \(\sum_i A_i=M\). The coefficient and projection in (5) follow.

**(ii) Conditional bilinear structure.** Fix the run count and the initial symbol. The lengths of all one-runs form a uniform positive composition of \(m\), independently of the uniform positive composition of \(n\) obtained from the zero-runs; these compositions are called \(A\) and \(B\). Suppose they have \(s\) and \(t\) parts. The inversion statistic is exactly \(U=A^\top C B\), where the zero-one matrix is \(C_{ij}=\mathbf1\{i\le j\}\) for a word starting with a one and \(C_{ij}=\mathbf1\{i<j\}\) for one starting with a zero. Use one-based indices. Put \(J_s=I_s-\mathbf1_s\mathbf1_s^\top/s\), \(J_t=I_t-\mathbf1_t\mathbf1_t^\top/t\), and
\[
c_A=\frac{m(m-s)}{s(s+1)},\qquad c_B=\frac{n(n-t)}{t(t+1)}.
\]
Writing \(T=\mathbf1_s^\top C\mathbf1_t\), independence and (5) yield exactly
\[
\mathbb E U=\frac{mnT}{st},
\quad\operatorname{Var}(U)=
\frac{n^2c_A}{t^2}\|J_sC\mathbf1_t\|^2+
\frac{m^2c_B}{s^2}\|J_tC^\top\mathbf1_s\|^2+
 c_Ac_B\|J_sCJ_t\|_F^2.
\tag{6}
\]
This identity is obtained by expanding the centered bilinear statistic into two independent linear components and one bilinear centered component, which are mutually orthogonal in \(L^2\).

**(iii) Evaluate the staircase matrices.** At \(R=2k\), either orientation has \(s=t=k\). For either orientation, the two projected row/column squared norms in (6) are each \(k(k^2-1)/12\), and the doubly projected Frobenius squared norm is \((k^2-1)/12\). The two orientations are equally likely. Their means are \(P(k+1)/(2k)\) and \(P(k-1)/(2k)\); the between-orientation variance is \(P^2/(4k^2)\). Averaging (6) and including that between-orientation term gives (1).

At \(R=2k+1\), the start-with-one case has \((s,t)=(k+1,k)\), while the start-with-zero case has \((s,t)=(k,k+1)\). In the first case the squared norms \(\|J_sC\mathbf1_t\|^2,\|J_tC^\top\mathbf1_s\|^2,\|J_sCJ_t\|_F^2\) are, respectively,
\[
\frac{k(k+1)(k+2)}{12},\qquad
\frac{k(k^2-1)}{12},\qquad
\frac{(k-1)(k+2)}{12}.
\tag{7}
\]
In the other orientation swap the row and column expressions. Both orientations have conditional mean \(P/2\). Their multiplicities are \(\binom{m-1}{k}\binom{n-1}{k-1}\) and \(\binom{m-1}{k-1}\binom{n-1}{k}\), giving orientation probabilities \((m-k)/(N-2k)\) and \((n-k)/(N-2k)\). Substitution into (6) and this weighted average yield (2). Reversing a word sends \(U\) to \(P-U\) while preserving \(R\), independently verifying the common conditional mean \(P/2\).

**(iv) Strict parity signs and monotonicity.** Simplifying differences between (1) and (2) gives
\[
V_{2k}-V_{2k+1}=
\frac{NP[2P-N(k-1)-2k]}{6k(N-2k)(k+1)}.
\tag{8}
\]
Let \(a=m-k\) and \(b=n-k\). The numerator's bracket becomes \((k+1)(a+b)+2ab\), strictly positive because feasibility of \(2k+1\) forces \(a+b>0\). For \(k\ge2\), the other difference is
\[
V_{2k}-V_{2k-1}=
\frac{P\left[a^2b+ab^2+(4k+6)ab+(k^2+4k+3)(a+b)+2(k+1)^2\right]}{6k(k+1)(a+b+2)}>0.
\tag{9}
\]
Finally,
\[
V_{2k}-V_{2k+2}=
\frac{P[2N+Pk+4P-k]}{6k(k+1)(k+2)}>0
\tag{10}
\]
whenever \(k<\min(m,n)\). The bracket is positive since \(N\ge2\), \(P\ge1\), and \(P\ge k\) in its domain. These explicit positive factorizations prove (3) and (4) without extrapolation from numerical examples.

## Verification

Execute `python3 verification/verify.py` using the Python standard library. The checker exhausts every binary word for all pairs of class sizes from one through eight, verifying exact conditional means, variances, and orientation-count identities. Independent rational evaluation of the matrix moment formula (6) checks class sizes through twenty-three. The three factored strict-gap identities are checked with exact rational arithmetic for all class sizes from one through thirty-nine. It reports **136004 exact assertions passed**. The proof of the unrestricted theorem is (5)--(10), not the finite checks. No statistical simulation, numerical tolerance, external data, or computer-algebra assumption is needed.

## Relationship to prior work

The 2005 work of Conger and Viswanath studies the marginal inversion and descent distributions of uniform multiset permutations, including their normal approximations; its theorem scope does not imply the fixed-run conditional inversion variances or inequalities (3). Classical Wald--Wolfowitz theory concerns the marginal run-count distribution and the two-sample random-arrangement null. A published exact analysis of fixed-composition run-transition covariances gives the local transition-indicator phase diagram, but does not supply any mixed conditional moment involving \(U\). A published corner-weighted rectangle generating-function identity records area and a Young-diagram corner statistic. That broader enumerative apparatus is a plausible route to related joint generating functions, but it does not directly state or imply the evaluated fixed-\(R\) variance formulas and strict even-run peaks without additional endpoint refinement and analysis. Madden's generating function for runs of specified lengths in binary words is similarly different from this conditional area statistic. The present claim is specifically the unconditional-in-size, conditional-in-run exact second-moment classification and parity inequalities, not the classical run-count or inversion-count distributions.

## Limitations

The classification assumes exactly two symbols, each appearing a positive number of times, and uniform sampling of fixed-composition words. The theorem concerns conditional means and variances, not the complete conditional distribution, tails, normal approximations, or power of any testing procedure. Previous enumerative literature could contain equivalent formulas implicitly; an exhaustive historical priority determination is not asserted. The comparison to older original runs monographs is limited by their availability; full-document noncoverage is not asserted for sources not read in full.

## References

1. M. Conger and D. Viswanath, “Normal approximations for descents and inversions of permutations of multisets,” first posted 2005-08-14, arXiv:math/0508242, https://arxiv.org/abs/math/0508242.
2. A. Wald and J. Wolfowitz, “On a Test Whether Two Samples are from the Same Population,” *Annals of Mathematical Statistics* 11 (1940), 147–162, doi:10.1214/aoms/1177731909.
3. A. M. Mood, “The Distribution Theory of Runs,” *Annals of Mathematical Statistics* 11 (1940), 367–392, doi:10.1214/aoms/1177731825.
4. J. Madden, “A Generating Function for the Distribution of Runs in Binary Words,” first posted 2017-07-13, arXiv:1707.04351, https://arxiv.org/abs/1707.04351.
5. “Exact dependence phases of fixed-composition run transitions,” publicly indexed mathematical finding (2026), with a distinct local-indicator covariance focus.
6. “Closed q-binomial expansion for the corner-weighted rectangle generating function,” publicly indexed mathematical finding (2026); its area/corner enumerator is a potential indirect prior route.
