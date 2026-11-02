# Twin off-uniform variance maxima for alternating subsequences of Mallows permutations

## Finding

Let \(n\ge4\) and \(q>0\). Draw a permutation \(\Pi_n\) of \(\{1,\ldots,n\}\) with Mallows law \(\Pr_q(\Pi_n=\pi)=q^{\mathrm{inv}(\pi)}/[n]_q!\). Let \(L_n\) be the maximum length of a subsequence with strict alternation starting with a descent (down–up–down–up). Write

\[
T(q)=1+q+q^2,\qquad U(q)=1+q+q^2+q^3+q^4.
\]

The exact mean and variance for every \(n\ge4\) are

\[
\mathbb E_qL_n=1+\frac{q}{1+q}+(n-2)\frac{2q}{T(q)},
\]

\[
\operatorname{Var}_q(L_n)=nV(q)+K(q),\qquad
V(q)=\frac{4q(q^6-q^5+2q^3-q+1)}{T(q)^2 U(q)},
\]

\[
K(q)=-\frac{q(11q^{10}+5q^9-15q^8+5q^7+17q^6+13q^4+q^3-19q^2+q+7)}{(1+q)^2(1+q^2)T(q)^2U(q)}.
\]

In particular the asymptotic variance per item is \(V(q)\), which is strictly positive. It is reciprocal-symmetric, \(V(q)=V(q^{-1})\). It has exactly two global maximizers over all \(q>0\), at \(q=r\) and \(q=r^{-1}\), where \(r\in(0,1)\) is the unique positive root below one of

\[
P(q)=q^{10}-3q^9-6q^8-q^7-2q^6-3q^5-2q^4-q^3-6q^2-3q+1.
\]

Numerically, \(r=0.225445665412468\ldots\), \(r^{-1}=4.43565857950931\ldots\), and \(V(r)=0.341971551962112\ldots\). The uniform case \(q=1\) is the unique *interior local minimum* of \(V\), with \(V(1)=8/45\), despite being the unique global maximizer of the asymptotic mean density \(2q/T(q)\). The function \(V\) tends to zero at both parameter extremes.

## Assumptions and scope

The inversion count is \(\mathrm{inv}(\pi)=\#\{(i,j):1\le i<j\le n,\;\pi_i>\pi_j\}\), and \([n]_q!=\prod_{j=1}^n(1+q+\cdots+q^{j-1})\). The parameter \(q\) is a positive real number fixed as \(n\) grows. The alternating subsequence is required to begin with a strict descent; the first and last permutation entries may or may not be selected. The finite-size variance identity requires \(n\ge4\). No claim is made about a parameter \(q\) varying with \(n\), nor about the maximizer of the finite-size variance for a fixed finite \(n\).

## Proof

**Local-extremum identity.** For a deterministic sequence of \(n\) distinct real numbers, a longest descent-first alternating subsequence consists of its interior local extrema, its last entry, and additionally its first entry precisely when the first two entries descend. This elementary canonical construction is proved in Romik's Lemma 1 and Corollary 2. Consequently, defining

\[
B=\mathbf1\{\Pi_1>\Pi_2\},\quad E_i=\mathbf1\{\Pi_{i-1}<\Pi_i>\Pi_{i+1}\;\text{or}\;\Pi_{i-1}>\Pi_i<\Pi_{i+1}\}\quad(2\le i\le n-1),
\]

we have the **pointwise** identity \(L_n=1+B+\sum_{i=2}^{n-1}E_i\).

**Finite overlap probabilities.** Under Mallows sampling, the relative order inside each consecutive block of length \(m\) has the Mallows law on \(m\) symbols. Relative orders on disjoint consecutive blocks are independent: condition on which *values* lie in each block; inversions within each block contribute an independent factor of \(q^{\mathrm{inv}}\), while all cross-block inversions depend only on the assigned value sets. These facts also follow from consecutive homogeneity and weak dissociation in Crane–DeSalvo–Elizalde.

Writing \(a=\Pr(E_i)\), \(b=\Pr(E_iE_{i+1})\), \(c=\Pr(E_iE_{i+2})\), \(t=\Pr(B)\), \(u=\Pr(BE_2)\), \(v=\Pr(BE_3)\), direct exact Mallows-weighted enumeration of respectively \(3,4,5,2,3,4\) symbols gives

\[
\begin{aligned}
t&=\frac{q}{1+q},&
a&=\frac{2q}{T(q)},\\
b&=\frac{q(q^2+3q+1)}{(1+q)^2T(q)},&
c&=\frac{q^2(3q^4+7q^3+7q^2+7q+3)}{(1+q)^2T(q)U(q)},\\
u&=\frac{q}{T(q)},&
v&=\frac{q^2(2q^2+q+1)}{(1+q)(1+q^2)T(q)}.
\end{aligned}
\]

The enumerations require only the \(2!+3!+4!+5!\) patterns, with the relevant indicators directly tested on each pattern and each weight \(q^{\mathrm{inv}}\) divided by \([m]_q!\). All further covariances vanish: \(\operatorname{Cov}(E_i,E_j)=0\) when \(|i-j|\ge3\), and \(\operatorname{Cov}(B,E_i)=0\) when \(i\ge4\).

**Exact moments.** Therefore, for \(n\ge4\),

\[
\begin{aligned}
\operatorname{Var}(L_n)={}&t(1-t)+(n-2)a(1-a)\\
&+2(n-3)(b-a^2)+2(n-4)(c-a^2)\\
&+2(u-ta)+2(v-ta).
\end{aligned}
\]

The mean is \(1+t+(n-2)a\). Collecting the variance into its coefficient of \(n\) and its constant yields exactly the displayed rational functions \(V\) and \(K\). Both identities can be verified by a symbolic common-denominator calculation, which is implemented independently in `VERIFY.py`. At \(q=1\) they reduce to \(\mathbb E L_n=(4n+1)/6\) and \(\operatorname{Var}(L_n)=(32n-13)/180\), matching the established uniform-permutation formulas.

**Complete maximizer classification.** Direct differentiation and factorization give

\[
V'(q)=\frac{-4(q-1)(q+1)P(q)}{T(q)^3U(q)^2}.
\]

All denominator factors are strictly positive for \(q>0\). The ten-degree polynomial \(P\) is reciprocal, \(q^{10}P(1/q)=P(q)\), and its nonzero coefficient sequence in descending degree has exactly two sign changes. Descartes' rule of signs gives at most two positive roots counted with multiplicity. Since \(P(0)=1>0\), \(P(1)=-25<0\), and \(P(q)\to+\infty\) as \(q\to+\infty\), there are at least two distinct positive roots, one on each side of one. Thus these are exactly the two positive roots, both simple and reciprocal. The derivative sign is \(+,-,+,-\) across the intervals divided by \(r,1,r^{-1}\); consequently \(r\) and \(r^{-1}\) are strict local maxima and \(1\) is a strict local minimum. The numerator \(q^6-q^5+2q^3-q+1\) is positive: it equals \((1-q)(1-q^5)+2q^3>0\) for \(0<q\le1\), and equals \(q^5(q-1)+(2q^3-q+1)>0\) for \(q\ge1\). As \(V(q)\to0\) at \(q\to0\) and \(q\to\infty\), the two local maxima are the **only global maxima**, and reciprocity makes their heights equal. Finally, differentiation of \(2q/T(q)\) yields \(2(1-q^2)/T(q)^2\), so the leading mean density is uniquely maximized at \(q=1\).

## Verification

The accompanying standalone `VERIFY.py` enumerates all consecutive patterns of lengths two through five, checks all six overlap formulas exactly by symbolic rational arithmetic, verifies the coefficient and derivative identities and reciprocal symmetries, and independently enumerates full Mallows-weighted permutation distributions using a dynamic-programming longest-alternating-subsequence algorithm. The verifier passed 110,195 exact assertions for sizes four through eight and parameter values from \(\{1/3,1/2,1,2,3\}\) (at size eight, \(\{1/2,1\}\)). Finite checks corroborate the algebra; the all-size and all-parameter claims rely on the proof above, especially weak dissociation and the algebraic root argument.

## Relationship to prior work

Stanley gives the uniform distribution's longest-alternating-subsequence moments; Romik proves the deterministic local-extrema representation and rederives the uniform moments. Houdré–Restrepo establish a probabilistic treatment for uniform permutations and certain words and Markov models. Bhatnagar–Peled treat *monotone* longest subsequences of Mallows permutations. Crane–DeSalvo–Elizalde give weak dissociation for Mallows consecutive patterns, together with an exact general variance/normal-approximation formula for the occurrence count of a **single** consecutive pattern. Their method supports the present overlap calculations, but does not itself state the combined four-pattern turning-point covariance, finite variance formula, or the reciprocal pair of globally maximizing Mallows parameters. The distinction is at the level of mathematical implication, not similarity of terminology. A later Mallows permutation-walk study analyzes ascent/descent increment sums and arcsine functionals, not this alternating-subsequence fluctuation phase.

## Limitations

This is a self-contained finite moment identity and a sharp extremal statement for the **linear variance coefficient**. It does not classify the finite-size variance maximizers, prove a new central limit theorem, determine a full distribution, or address \(q\) depending on \(n\). The local dependence identity and uniform case are prior results. The formulas can be derived using standard Mallows-block machinery; the independent contribution assessed here is the explicit combined statistic and its nontrivial two-maximizer classification. Undetected equivalent presentations or implicit deductions in broader permutation-statistics references remain a publication-priority risk. No independent audit has been performed.

## References

1. R. P. Stanley, *Longest alternating subsequences of permutations*, arXiv:math/0511419, first public 2005-11-16, https://arxiv.org/abs/math/0511419.
2. C. Houdré and R. Restrepo, *A probabilistic approach to the asymptotics of the length of the longest alternating subsequence*, arXiv:1005.1893, first public 2010-05-11, https://arxiv.org/abs/1005.1893.
3. D. Romik, *Local extrema in random permutations and the structure of longest alternating subsequences*, DMTCS Proceedings, DOI:10.46298/dmtcs.2956, https://dmtcs.episciences.org/en/articles/2956.
4. N. Bhatnagar and R. Peled, *Lengths of Monotone Subsequences in a Mallows Permutation*, arXiv:1306.3674, first public 2013-06-16, https://arxiv.org/abs/1306.3674.
5. H. Crane, S. DeSalvo and S. Elizalde, *The probability of avoiding consecutive patterns in the Mallows distribution*, arXiv:1609.01370, first public 2016-09-06, https://arxiv.org/abs/1609.01370.
6. X. Fang et al., *Arcsine laws for random walks generated from random permutations with applications to genomics*, *Journal of Applied Probability* 58 (2021), DOI:10.1017/jpr.2021.14.
