# A U-shaped fixed-point influence on records in a uniform permutation

## Finding
Let \(\pi\) be a uniform permutation of \(\{1,\ldots,n\}\), with \(n\ge2\). Write \(I_j=\mathbf1\{\pi(j)=j\}\), \(R_i=\mathbf1\{\pi(i)>\max_{h<i}\pi(h)\}\), with \(R_1=1\); let \(F=\sum_j I_j\), \(R=\sum_i R_i\), and \(H_n=\sum_{i=1}^n1/i\). For every \(1\le j\le n\), the exact effect of conditioning on a fixed point at position \(j\) is
\[
\mathbb E[R\mid I_j=1]-H_n=\frac1{\binom{n-1}{j-1}}-\frac1n.
\]
Equivalently,
\[
\operatorname{Cov}(I_j,R)=\frac1n\left(\frac1{\binom{n-1}{j-1}}-\frac1n\right).
\]
For every \(n\ge5\), this covariance is strictly positive exactly at \(j\in\{1,2,n-1,n\}\) and strictly negative at all \(3\le j\le n-2\). It is symmetric under \(j\mapsto n+1-j\) and decreases toward the center. The aggregate covariance is nevertheless positive:
\[
\operatorname{Cov}(F,R)=\frac1n\sum_{k=1}^{n-1}\binom{n-1}{k}^{-1}
=\frac2{n^2}+O(n^{-3}).
\]
The complete indicator-level cross-covariance for \(1\le i,j\le n\) is
\[
\operatorname{Cov}(I_j,R_i)=
\begin{cases}
0,&i=1\text{ or }j>i,\\
\frac1{ni(i-1)},&j<i,\\
\frac1n\left(\binom{n-1}{i-1}^{-1}-\frac1i\right),&j=i\ge2.
\end{cases}
\]

## Assumptions and scope
All permutations are equally likely, fixed points are exact equalities of one-line positions and values, and records are strict left-to-right maxima. The results hold for each integer \(n\ge2\), not only asymptotically. Conditioning is on one specified fixed point, not on the number or complete pattern of all fixed points. The finite-vector covariance formula is not a statement of independence.

## Proof
For \(i\ge2\), consider \(\Pr(R_i=1\mid I_j=1)\). If \(j>i\), fixing a value outside the prefix leaves the relative order of the first \(i\) positions uniform, so this probability is \(1/i\). If \(j<i\), the other \(i-1\) values in the prefix are a sample excluding \(j\). They contain at least one value exceeding \(j\), because only \(j-1\le i-2\) values are smaller than \(j\). Their relative assignment to the remaining \(i-1\) positions is uniform, so the largest occurs at \(i\) with probability \(1/(i-1)\). Finally, if \(j=i\), the record occurs precisely when all preceding \(i-1\) values are \(\{1,\ldots,i-1\}\). Of the \(\binom{n-1}{i-1}\) equally likely unordered sets of preceding values, one qualifies. Thus
\[
\Pr(R_i=1\mid I_j=1)=
\begin{cases}
1/i,&j>i,\\
1/(i-1),&j<i,\\
\binom{n-1}{i-1}^{-1},&j=i.
\end{cases}
\]
For \(i=1\), both the conditional and unconditional record probabilities are 1. Since \(\Pr(I_j=1)=1/n\) and \(\Pr(R_i=1)=1/i\), subtracting products gives the displayed complete cross-covariance kernel.

For \(j\ge2\), summing the conditional record deviations over \(i\) yields
\[
\left(\binom{n-1}{j-1}^{-1}-\frac1j\right)
+\sum_{i=j+1}^n\left(\frac1{i-1}-\frac1i\right)
=\binom{n-1}{j-1}^{-1}-\frac1n.
\]
For \(j=1\), only the second sum is present, from \(i=2\), and equals \(1-1/n\), the same formula. Multiplying by \(1/n\) proves the conditional-mean and covariance identities.

For \(n\ge5\), the four end indices have binomial coefficient \(1\) or \(n-1\), both less than \(n\). Every remaining index has binomial coefficient at least \(\binom{n-1}{2}=(n-1)(n-2)/2>n\). Symmetry and the unimodality of binomial coefficients give the asserted sign pattern and U-shaped monotonicity.

Summing the positionwise covariance over \(j\) yields \(n^{-1}\sum_{k=0}^{n-1}\binom{n-1}{k}^{-1}-n^{-1}\), giving the aggregate expression. With \(N=n-1\), the terms \(k=1,N\) contribute \(2/N\), and all the remaining terms sum to \(O(N^{-2})\): the two terms with \(k=2,N-1\) are \(O(N^{-2})\) and the middle \(O(N)\) terms are each at most \(\binom N3^{-1}=O(N^{-3})\). Therefore \(\operatorname{Cov}(F,R)=2/n^2+O(n^{-3})\).

## Verification
The attached standalone `verify.py` enumerates every permutation through size eight using integer counts and rational arithmetic, compares the full conditional rank kernel and both derived covariance identities, and checks the sign classification and row-sum formulas symbolically for sizes up to 100. Run with `python verify.py` from the directory containing this document. The arbitrary-size assertions rely on the preceding proof; finite enumeration does not certify claims beyond its tested range.

## Relationship to prior work
Dubach (2024), *A geometric approach to conjugation-invariant random permutations*, analyzes record counts for conjugation-invariant permutations, including a large-fixed-point phase transition (Section 2.3), using a planar construction. This provides the direct motivation for asking about one fixed point at a specified location. Its statements concern global asymptotics under prescribed cycle types; they do not supply the present finite-position conditional expectation and sign law. Grübel (2023), *Ranks, copulas, and permutons*, surveys the general rank/permutation viewpoint. Familiar separate marginal facts \(\mathbb E F=1\) and \(\mathbb E R=H_n\) do not determine their cross-covariance. Prior results about fixed points with descents or cycles with records likewise involve different statistics.

## Limitations
The result does not quantify the distribution of \(R\) conditional on one fixed point, nor conditioning on a fixed total number of fixed points, and does not establish independence. An earlier equivalent first-moment identity could exist under different terminology; the inspected literature and database comparisons establish only a best-knowledge originality assessment, not historical priority.

## References
- V. Dubach, *A geometric approach to conjugation-invariant random permutations*, arXiv:2402.10116, initial public submission 15 February 2024; see Section 2.3 and the proofs on records in Section 6. https://arxiv.org/abs/2402.10116
- R. Grübel, *Ranks, copulas, and permutons*, Metrika 87 (2024), 155–182, first published online 12 May 2023. https://doi.org/10.1007/s00184-023-00908-2
