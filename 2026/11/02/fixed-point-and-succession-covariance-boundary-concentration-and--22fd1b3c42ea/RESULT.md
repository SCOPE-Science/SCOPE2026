# Fixed-point and succession covariance: boundary concentration and an odd-order null direction

## Finding

Let \(n\ge3\) and let \(\Pi\) be uniformly distributed on the symmetric group of \([n]\). Write
\[
A_j=\mathbf1\{\Pi(j)=j\}\quad(1\le j\le n),\qquad
B_i=\mathbf1\{\Pi(i+1)=\Pi(i)+1\}\quad(1\le i<n).
\]
Thus \(A_j\) marks a fixed point and \(B_i\) marks a succession (an increasing adjacent pair of consecutive values). Their entire \(n\)-by-\((n-1)\) cross-covariance matrix has entries
\[
\boxed{\operatorname{Cov}(A_j,B_i)
=\frac{n\mathbf1\{j\in\{1,n,i,i+1\}\}-2}{n^2(n-1)(n-2)}.}
\]
In particular, the entries are positive on the two endpoint rows and on the incident positions, and negative elsewhere. Let \(F=\sum_{j=1}^{n}A_j\) and \(U=\sum_{i=1}^{n-1}B_i\). Then
\[
\boxed{\operatorname{Cov}(F,U)=\frac{2}{n(n-1)},\qquad
\operatorname{Corr}(F,U)=\frac{2}{(n-1)\sqrt{n^2-n-1}}.}
\]
Exactly \((n-1)/n\) of the positive aggregate covariance comes from the two endpoint fixed-point indicators:
\[
\operatorname{Cov}(A_j,U)=
\begin{cases}
1/n^2,&j=1\text{ or }j=n,\\
2/[n^2(n-1)(n-2)],&2\le j\le n-1.
\end{cases}
\]
The matrix has a sharp parity-dependent linear kernel:
\[
\boxed{\operatorname{rank}(\operatorname{Cov}(A,B))=
\begin{cases}n-1,&n\text{ even},\\n-2,&n\text{ odd}.\end{cases}}
\]
For odd \(n\), its one-dimensional right nullspace is spanned by \((1,-1,1,-1,\ldots,-1)\). Consequently the nonconstant alternating succession contrast \(B_1-B_2+\cdots-B_{n-1}\) is uncorrelated with **every** fixed-point indicator. For even \(n\), every nonzero linear succession contrast has nonzero covariance with at least one fixed-point indicator.

## Assumptions and scope

The permutation is uniformly distributed among all \(n!\) bijections of \([n]\), with \(n\ge3\). The indices \(j\) and \(i\) range over \(1\le j\le n\) and \(1\le i\le n-1\) respectively. Only linear (second-moment) uncorrelatedness is claimed; the theorem does not assert statistical independence of the fixed-point and succession vectors or of the alternating contrast. The endpoint rows refer to the numeric labels \(1\) and \(n\). The rank is over the real numbers.

## Proof

**One succession.** Fix \(i\in[n-1]\). The random ordered pair \((\Pi(i),\Pi(i+1))\) is uniform over the \(n(n-1)\) distinct ordered value pairs. The event \(B_i=1\) has probability \(1/n\), and, conditional on it, \(H=\Pi(i)\) is uniform on \(\{1,\ldots,n-1\}\), with \(\Pi(i+1)=H+1\). All other positions are filled by a uniform bijection onto the remaining \(n-2\) values.

If \(j=i\) or \(j=i+1\), the fixed-point event \(A_j=1\) is equivalent, under the conditioning, to \(H=i\). Hence \(\Pr(A_j=1\mid B_i=1)=1/(n-1)\). If \(j\notin\{i,i+1\}\), fixing the value at \(j\) is possible precisely when \(j\notin\{H,H+1\}\). For an endpoint \(j\in\{1,n\}\), precisely one of the \(n-1\) possible \(H\) values excludes \(j\); the other \(n-2\) possibilities each give conditional fixed-point probability \(1/(n-2)\). For an interior \(j\in\{2,\ldots,n-1\}\) outside the incident positions, precisely two values of \(H\) exclude \(j\), leaving \(n-3\) possibilities. Therefore
\[
\Pr(A_j=1\mid B_i=1)=
\begin{cases}
1/(n-1),& j\in\{1,n,i,i+1\},\\
(n-3)/[(n-1)(n-2)],&\text{otherwise}.
\end{cases}
\]
Since \(\Pr(A_j=1)=\Pr(B_i=1)=1/n\), multiplying the conditional difference from \(1/n\) by \(1/n\) gives the boxed entry formula, with positive entries \((n-2)/[n^2(n-1)(n-2)]\) and negative entries \(-2/[n^2(n-1)(n-2)]\).

**Aggregate and boundary concentration.** For \(j=1,n\), each of the \(n-1\) entries equals \(1/[n^2(n-1)]\), so \(\operatorname{Cov}(A_j,U)=1/n^2\). For \(2\le j\le n-1\), exactly two indices \(i=j-1,j\) are incident; hence the corresponding row sum is
\[
\frac{2(n-2)-2(n-3)}{n^2(n-1)(n-2)}
=\frac{2}{n^2(n-1)(n-2)}.
\]
Summing the endpoint and interior rows yields
\[
\operatorname{Cov}(F,U)=\frac2{n^2}+\frac2{n^2(n-1)}=\frac2{n(n-1)},
\]
and the exact endpoint fraction is \((2/n^2)/(2/[n(n-1)])=(n-1)/n\).

**Rank and parity.** Let \(x=(x_1,\ldots,x_{n-1})\) satisfy \(\operatorname{Cov}(A,B)x=0\), and put \(S=\sum_{i=1}^{n-1}x_i\). An endpoint row gives \((n-2)S=0\), so \(S=0\). Each interior row \(j=2,\ldots,n-1\), after multiplication by \(n^2(n-1)(n-2)\), gives \(n(x_{j-1}+x_j)-2S=0\). Thus \(x_j=-x_{j-1}\) for all \(j\ge2\), so \(x\) is alternating. Its coordinate sum vanishes for nonzero amplitude exactly when \(n-1\) is even, i.e. when \(n\) is odd. Rank-nullity gives the stated ranks and the unique nonzero null mode at odd order. This mode is not a constant random variable: a decreasing permutation has no successions, whereas, for example, for every odd \(n\ge5\), the permutation beginning \((2,3,n,1,4,5,\ldots,n-1)\) has a nonzero alternating succession contrast (the case \(n=3\) is checked directly).

**Correlation.** \(\mathbb EF=1\) and \(\operatorname{Var}(F)=1\) for \(n\ge2\), since different fixed-point indicators have joint probability \(1/[n(n-1)]\). For the succession indicators, the probability that one occurs is \(1/n\), and for any two distinct indices it is \(1/[n(n-1)]\), including overlapping pairs: prescribing two successions merges two or three consecutive values into ordered blocks, and exactly \((n-2)!\) permutations satisfy the constraints. Consequently \(\mathbb EU=(n-1)/n\), and
\[
\operatorname{Var}(U)=\frac{n^2-n-1}{n^2}.
\]
Combining this with the aggregate covariance proves the stated correlation.

## Verification

The accompanying standalone standard-library program `verify.py` independently enumerates all permutations for each \(3\le n\le8\), computes all individual cross-moments directly, and compares them using exact rational arithmetic. It also checks the total covariance, both variances, the predicted parity rank by rational row reduction for \(3\le n\le30\), and the odd-order null vectors. On execution it reports `PASS 266 assertion groups`. These are finite checks; the preceding conditional counting and matrix argument prove the statements for every \(n\ge3\).

## Relationship to prior work

Diaconis, Evans and Graham established that the set of succession positions has the same **marginal distribution** as the set of fixed-point positions excluding the final label. That result neither specifies the joint coupling of the two sets within the *same* permutation nor determines their cross-covariance matrix or its rank. Reilly and Tanny enumerated successions; their work supplies classical marginal context. Later work by Ma, Qi, Yeh and Yeh studied joint distributions of successions with Eulerian statistics and relates such enumerators to fixed-point polynomials on the opposite side of equidistribution identities; Chen and Fu, and Du and Ji, established further bijections and marginal equidistributions; the inspected statements do not identify the same-permutation cross-covariance operator. The present calculation is a focused joint-dependence law, not a new formula for either marginal distribution.

## Limitations

The theorem concerns exactly the uniform permutation law, ordinary increasing successions, and second-order dependence; it does not imply higher-order independence or independence of the alternating mode. The rank concerns linear observability from individual fixed-point indicators, not nonlinear prediction. The literature comparison supports a best-knowledge difference from the inspected statements, not absolute historical priority; older successions enumeration and uninspected derivations may contain equivalent material. The program's finite verification is not a substitute for the proof.

## References

1. P. Diaconis, S. N. Evans, R. Graham, *Unseparated pairs and fixed points in random permutations*, technical report (August 1, 2013), https://statistics.berkeley.edu/tech-reports/822; preprint https://arxiv.org/abs/1308.5459; *Advances in Applied Mathematics* 61 (2014), 102–124. Primary MSC: 60C05.
2. J. W. Reilly, S. M. Tanny, *Counting Successions in Permutations*, *Studies in Applied Mathematics* 61 (1979), 73–81, https://doi.org/10.1002/sapm197961173.
3. S.-M. Ma, J. Ma, J. Yeh, Y.-N. Yeh, *The gamma-positivity of Eulerian polynomials and succession statistics*, https://arxiv.org/abs/2002.06930 (2020).
4. S.-M. Ma, H. Qi, J. Yeh, Y.-N. Yeh, *On the joint distributions of succession and Eulerian statistics*, https://arxiv.org/abs/2401.01760 (2024).
5. W. Y. C. Chen, A. M. Fu, *A Grammar of Dumont and a Theorem of Diaconis-Evans-Graham*, https://arxiv.org/abs/2402.02743 (2024).
6. L. R. Du, K. Q. Ji, *A Refinement of a Theorem of Diaconis-Evans-Graham*, https://arxiv.org/abs/2404.00607 (2024).
