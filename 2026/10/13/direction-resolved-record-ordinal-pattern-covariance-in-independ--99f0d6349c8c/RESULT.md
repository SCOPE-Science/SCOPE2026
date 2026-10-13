# Direction-resolved record--ordinal-pattern covariance in independent samples

## Finding
Let \(X_1,\ldots,X_n\) be independent and identically distributed from an atomless real distribution, with \(n\ge 3\). Let \(R_n\) count strict upper records, including the first observation. For each permutation \(\sigma\) of the ranks \(1,2,3\), let \(N_{n,\sigma}\) count consecutive triples whose increasing ranks, in positional order, form \(\sigma\). Then the **complete six-coordinate mixed-covariance law** is

\[
12n(n-1)\operatorname{Cov}(R_n,N_{n,\sigma})=
\begin{cases}
(n-2)(5n-1), & \sigma=123,\\
-(n-5)(n-2), & \sigma=132,\\
2(n-2)^2, & \sigma\in\{213,231\},\\
-2(n-2)(2n-1), & \sigma\in\{312,321\}.
\end{cases}
\]

Every covariance is independent of the common atomless marginal law. The \(132\)-coordinate is positive for \(n=3,4\), zero for \(n=5\), and negative for \(n\ge6\). The \(123,213,231\) coordinates are positive, and the \(312,321\) coordinates negative, at every \(n\ge3\). The respective limits as \(n\to\infty\) are \(5/12,-1/12,1/6,1/6,-1/3,-1/3\).

## Assumptions and scope
The sample is a finite iid sequence of real-valued observations with an atomless common distribution; no density, moment, or support assumption is necessary. Apply the probability integral transform, or use exchangeability and absence of ties, to replace its relative order by a uniform random permutation. For \(1\le j\le n\), put

\[
I_j={\bf1}\{X_j>\max(X_1,\ldots,X_{j-1})\},\qquad I_1=1,\qquad R_n=\sum_{j=1}^{n}I_j.
\]

For \(2\le i\le n-1\), define \(A_{i,\sigma}\) as the indicator that the triple \((X_{i-1},X_i,X_{i+1})\) has ordinal pattern \(\sigma\), and \(N_{n,\sigma}=\sum_{i=2}^{n-1}A_{i,\sigma}\). A triple has, for example, pattern \(132\) when its first observation is smallest, its middle observation is largest, and its last observation lies strictly between them. The covariance uses the ordinary product expectation minus the product of expectations.

## Proof
By distribution-freeness it suffices to work with iid \(\mathrm{Unif}(0,1)\) observations. For fixed \(i\) and \(\sigma\), the record event \(I_j=1\) is independent of \(A_{i,\sigma}\) when \(j\le i-2\), since it depends on disjoint observations. It is also independent for \(j\ge i+2\): conditional on the values of the first \(j-1\) observations, the law of their ranks relative to their unordered values is uniform; the event that observation \(j\) is the new maximum depends on the unordered earlier values and the independent new observation, not on their order. Consequently only \(j=i-1,i,i+1\) contribute to \(\operatorname{Cov}(R_n,A_{i,\sigma})\).

Write \(q_{j,\sigma}=\mathbb P(A_{i,\sigma}=1\mid I_j=1)\) for these three indices. As \(\mathbb P(I_j=1)=1/j\) and \(\mathbb P(A_{i,\sigma}=1)=1/6\),

\[
\operatorname{Cov}(R_n,A_{i,\sigma})
=\sum_{j=i-1}^{i+1}\frac{q_{j,\sigma}-1/6}{j}.
\]

At \(j=i-1\), the record value has beta density \((i-1)u^{i-2}\), while the next two values are iid uniform. Conditioning on the rank \(a\in\{1,2,3\}\) of the first member of the triple gives

\[
q_{i-1,\sigma}=
\begin{cases}
1/[i(i+1)],&\sigma_1=1,\\
(i-1)/[i(i+1)],&\sigma_1=2,\\
(i-1)/[2(i+1)],&\sigma_1=3.
\end{cases}
\]

At \(j=i\), the middle triple member is a record. Conditional on its value \(u\), the preceding member is uniform on \((0,u)\) and the following member is independent uniform on \((0,1)\). Averaging against the beta \((i,1)\) density yields \(q_{i,123}=1/(i+1)\), \(q_{i,132}=q_{i,231}=i/[2(i+1)]\), and zero for the remaining patterns. At \(j=i+1\), the last triple member is the largest, so \(q_{i+1,123}=q_{i+1,213}=1/2\) and all others are zero.

Substitution and simplification produce the exact local covariance vector, in the order \(123,132,213,231,312,321\):

\[
\left(\operatorname{Cov}(R_n,A_{i,\sigma})\right)_{\sigma}
=\frac{(3i+1,\;7-3i,\;3i-5,\;3i-5,\;1-3i,\;1-3i)}{6i(i-1)(i+1)}.
\]

This formula depends on \(i\), not on the terminal sample size \(n\). Summing over \(i=2,\ldots,n-1\), partial-fraction telescoping gives the stated six closed forms. In particular, each is an identity for **every integer \(n\ge3\)** and hence determines the displayed limit and the exact sign transitions without any limiting approximation.

## Verification
The standalone `verify.py` uses Python's `fractions.Fraction` and `itertools.permutations`. It directly enumerates all uniform permutations at \(3\le n\le8\), independently counting records and the six ordinal patterns and comparing all \(36\) mixed covariances with the formulas. A second exact enumeration checks all \(108\) pattern/record joint event probabilities for \(2\le i\le7\). It prints `VERIFY_OK exact_covariance_checks= 36 exact_joint_local_checks= 108` on success. An independent symbolic telescoping calculation found a zero difference for each of the six proposed sums. These computations are **finite corroboration**; the preceding conditional-probability proof establishes the theorem for all \(n\).

## Relationship to prior work
Chen and Cheng (2000) derive joint distributions for the unrefined peak, double-rise, trough, and double-fall counts in uniform permutations. Their inspected full article does not mix these counts with the number of upper records. Gnedin (2007) describes record statistics via independent initial ranks and supplies relevant record-generation theory but not the stated six mixed covariances in the inspected sections. Warren and Seneta (1996) treat the marginal peak-count distribution; only their abstract and bibliographic record were accessible for comparison. These results supply the established components of the argument rather than the complete direction-resolved mixed-covariance law.

The coarser peak count \(N_{n,132}+N_{n,231}\) has covariance \((n-2)(n+1)/[12n(n-1)]\) with \(R_n\); that **aggregate identity is not asserted as new**. The full six-coordinate result distinguishes the orientations within peaks and troughs and exhibits the change of sign specific to the \(132\) component.

## Limitations
The theorem assumes iid atomless observations. It does not cover tied, dependent, or nonidentically distributed samples; their record indicators need not enjoy the requisite symmetry. Only first mixed moments (covariances) are classified, not the joint distributions. Priority comparisons cannot rule out an unlocated general joint permutation generating function implicitly containing all six identities; in particular the full text of Warren and Seneta (1996) was not available for inspection. No independent scientific audit has been performed.

## References
1. Y.-L. Chen and W.-H. Cheng, “A Note on Joint Distributions of Some Random Vectors Defined on Permutations,” *Ars Combinatoria* **54** (2000), 139–148. Publisher PDF: https://combinatorialpress.com/article/ars/Volume%20054/volume-54-paper-11.pdf . Publisher records first public date 2000-01-31.
2. A. Gnedin, “Coherent random permutations with record statistics,” *Discrete Mathematics & Theoretical Computer Science*, Proc. AH (2007), 157–170. Open PDF: https://dmtcs.episciences.org/en/articles/3551/download .
3. D. Warren and E. Seneta, “Peaks and Eulerian numbers in a random sequence,” *Journal of Applied Probability* **33** (1996), 101–114. DOI: https://doi.org/10.2307/3215267 .
