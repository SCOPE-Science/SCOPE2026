# Exact optimal coverage depth for binary length-eight dimension-three codes

## Finding

Let \(G\in\mathbb F_2^{3\times 8}\) have rank \(3\). At each read, choose one of its eight columns independently and uniformly with replacement. Let \(T_G\) be the first number of reads whose sampled columns span \(\mathbb F_2^3\). Then

\[
\min_{\operatorname{rank}G=3}\mathbb E[T_G]=\frac{422}{105}.
\]

Equality holds exactly when, up to column permutation and invertible row operations, the columns are the seven nonzero vectors of \(\mathbb F_2^3\), with one vector repeated once. This optimum is \(\frac{43}{420}\) larger than the expected coverage time \(\frac{47}{12}\) of the binary \([7,3]\) simplex code.

## Assumptions and scope

The code is a full-rank binary generator matrix, and every read independently selects one of the eight column indices with probability \(1/8\). Repeated indices are allowed. The claim concerns only parameters \((q,n,k)=(2,8,3)\); it does not assert an all-length or all-alphabet formula.

A zero column cannot help a sampled set span the information space. Replacing a zero column by any nonzero column weakly increases the span after every possible sequence of sampled indices, so some optimum has no zero columns. Over \(\mathbb F_2\), each one-dimensional subspace has a unique nonzero vector. Thus a no-zero generator matrix is described, up to column order, by seven nonnegative multiplicities \(m_P\) summing to \(8\), one for each point \(P\) of the Fano plane.

## Proof

For a projective point \(P\), put \(p_P=m_P/8\). For each of the seven projective lines \(L\), put \(p_L=\sum_{P\in L}p_P\). A profile has rank \(3\) exactly when \(p_L<1\) for every line.

For every integer \(t\ge1\), the event \(T_G>t\) means that the first \(t\) sampled directions fail to span \(\mathbb F_2^3\). This happens exactly when all sampled directions lie on at least one projective line. Inclusion-exclusion over the seven lines gives

\[
\Pr(T_G>t)=\sum_L p_L^t-2\sum_P p_P^t.
\]

Indeed, any two distinct Fano-plane lines meet at one point, and exactly three lines pass through each point. The pairwise intersections therefore contribute \(-3p_P^t\) at each point, while the triple intersection of those three lines contributes \(+p_P^t\); no four lines have a common point. Summing the tail probabilities, with \(\Pr(T_G>0)=1\), yields the exact identity

\[
\mathbb E[T_G]=1+\sum_L\frac{p_L}{1-p_L}-2\sum_P\frac{p_P}{1-p_P}.
\]

There are exactly \(\binom{14}{6}=3003\) weak compositions of \(8\) into seven point multiplicities. A profile spans rank \(3\) if and only if its support is not contained in any Fano-plane line. The included checker `verify_rank3_binary_n8.py` enumerates all 3003 profiles and evaluates the displayed expression using exact rational arithmetic. It finds 2702 spanning profiles; the minimum is \(422/105\), attained by exactly seven profiles, each with multiplicities \((2,1,1,1,1,1,1)\) in some order. The next distinct objective value is \(88/21\), so no other profile ties the minimum.

For a minimizing profile, three lines contain the repeated point and each have mass \(4/8\); the other four lines have mass \(3/8\). The point masses are one copy of \(2/8\) and six copies of \(1/8\). Substitution gives

\[
1+3\frac{4}{8-4}+4\frac{3}{8-3}-2\left(\frac{2}{8-2}+6\frac{1}{8-1}\right)=\frac{422}{105}.
\]

For the length-seven simplex code, all seven point masses are \(1/7\) and all seven line masses are \(3/7\), so the same identity gives

\[
1+7\frac{3}{7-3}-2\cdot7\frac{1}{7-1}=\frac{47}{12}.
\]

The difference is \(\frac{422}{105}-\frac{47}{12}=\frac{43}{420}\). The finite census is complete because every full-rank matrix is represented by one of the enumerated profiles after the zero-column replacement argument.

## Verification

The checker uses only the Python standard library and exact `fractions.Fraction` arithmetic. It verifies seven Fano-plane lines, 3003 total profiles, 2702 spanning profiles, the minimum \(422/105\), exactly seven minimizers, the next distinct value \(88/21\) with 21 profiles, and the difference \(43/420\) from the length-seven simplex benchmark. No floating-point computation or random experiment is used to establish the minimum.

## Relationship to prior work

Gross, Grunbaum, Bertuzzo, Yaakobi, and Ravagnani, *Optimal Codes for the Coverage Depth Problem and the Performance of Random Codes* (first public version 5 October 2026, arXiv:2610.07370), develop a general coverage-depth formula, prove optimality for several code families including simplex codes at their natural lengths, and analyze expected coverage depth for random linear codes. Their uniform-projective lower bound gives the length-seven binary simplex value \(47/12\), but it does not determine the integer multiplicity optimum at length eight. The result here is a finite exact optimization over all full-rank binary \(3\times8\) column profiles, rather than a restatement of the general lower bound.

A related 2026 article titled *The random variables of the DNA coverage depth problem* is cited in the inspected paper. Its citation and contextual description were available, but its full text was not inspected here; this remains a literature-overlap risk. No claim is made about other parameter sets.

## Limitations

The theorem is restricted to binary full-recovery coverage depth for \(3\times8\) full-rank generator matrices with independent uniform sampling with replacement. It does not classify optimal codes for other lengths, dimensions, or fields. The finite minimization is certified by the included exact checker and the stated exhaustive profile reduction. The related 2026 coverage-depth article noted above was not fully inspected, so independent literature review may change the originality assessment.

## References

1. R. Gross, Y. Grunbaum, M. Bertuzzo, E. Yaakobi, and A. Ravagnani, “Optimal Codes for the Coverage Depth Problem and the Performance of Random Codes,” arXiv:2610.07370, first submitted 5 October 2026. https://arxiv.org/abs/2610.07370.
2. Ş. Bodur, S. Lia, H. H. López, R. Ludhani, A. Ravagnani, and L. Seccia, “The random variables of the DNA coverage depth problem,” *IEEE Transactions on Information Theory* (2026). This citation is listed in reference 1; its full text was not inspected for this finding.
