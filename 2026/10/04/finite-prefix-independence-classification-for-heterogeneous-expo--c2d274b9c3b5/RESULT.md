# Finite-prefix independence classification for heterogeneous exponential records
## Finding
Let \(n\ge2\). Let \(X_1,\ldots,X_n\) be independent exponential random variables with positive scale parameters \(\lambda_1,\ldots,\lambda_n\), meaning
\[
\Pr(X_i\le x)=1-e^{-x/\lambda_i},\qquad x\ge0.
\]
Define the upper-record indicators
\[
I_1=1,\qquad I_j=\mathbf 1\!\left\{X_j>\max_{i<j}X_i\right\},\qquad 2\le j\le n.
\]
Then \(I_2,\ldots,I_n\) are mutually independent if and only if
\[
\lambda_1=\lambda_2=\cdots=\lambda_{n-1}.
\]
There is no restriction on the terminal scale \(\lambda_n\).

There is also an exact local sign law. Suppose \(2\le k\le n-1\) and
\[
\lambda_1=\cdots=\lambda_{k-1}=\lambda.
\]
Then
\[
\operatorname{sign}\operatorname{Cov}(I_k,I_{k+1})
=
\operatorname{sign}(\lambda-\lambda_k),
\]
and this sign is independent of \(\lambda_{k+1}\). Hence equality of the first \(k-1\) scales makes a change at time \(k\) visible exactly one record-indicator step later: the prefix ending at \(k\) can still have mutually independent record indicators, but \(I_k\) and \(I_{k+1}\) become dependent unless \(\lambda_k=\lambda\).

## Assumptions and scope
The variables are independent, one-dimensional, continuously distributed, and exponentially distributed with the scale convention above. Records are strict upper records. The theorem concerns a finite prefix of length \(n\); it does not assume stationarity or identical distributions.

The recent motivating preprint arXiv:2602.20416v1 claims independence of record indicators for independent, not necessarily identically distributed observations. The finite exponential family is a canonical setting in which that general claim can be tested exactly. Earlier work of Ahsanullah and Nevzorov treats nonidentically distributed exponentials and already records that record indicators are not independent in general. The result here classifies exactly when finite-prefix independence survives inside that family and determines the sign of the first adjacent dependence created by a scale change.

## Proof
Write the exponential rate as the reciprocal scale. The key step is the following adjacent-sign lemma.

Assume \(\lambda_1=\cdots=\lambda_{k-1}=\lambda\), put \(q=k-1\), and rescale time by \(\lambda\). Then the first \(q\) variables have rate \(1\). Put
\[
x=\frac{\lambda}{\lambda_k},\qquad z=\frac{\lambda}{\lambda_{k+1}},
\]
so \(X_k\) and \(X_{k+1}\) have rates \(x\) and \(z\), respectively. Let
\[
M=\max(X_1,\ldots,X_{k-1}),\qquad Y=X_k,\qquad Z=X_{k+1},\qquad K=\max(M,Y),
\]
and let \(A=\{Y>M\}\). Thus \(A=\{I_k=1\}\), while \(I_{k+1}=1\) exactly when \(Z>K\). Since \(Z\) has rate \(z\),
\[
\Pr(I_{k+1}=1\mid K)=e^{-zK}.
\]
Therefore
\[
\operatorname{Cov}(I_k,I_{k+1})
=
\Pr(A)\left(\mathbb E[e^{-zK}\mid A]-\mathbb E[e^{-zK}]\right).
\]
It remains to compare the law of \(K\) conditional on \(A\) with its unconditional law.

For \(t>0\), the density of \(K\) is
\[
f_K(t)=(1-e^{-t})^{q-1}
\left[q e^{-t}(1-e^{-xt})+x e^{-xt}(1-e^{-t})\right],
\]
whereas the joint density of \(K\) and \(A\) is
\[
f_{K,A}(t)=x e^{-xt}(1-e^{-t})^q.
\]
Up to the positive normalizing constant \(\Pr(A)^{-1}\), the likelihood ratio \(f_{K\mid A}(t)/f_K(t)\) has the same monotonicity as
\[
R(t)=\frac{1}{1+(q/x)T_x(e^{-t})},
\qquad
T_x(u)=\frac{u^{1-x}-u}{1-u},\qquad 0<u<1.
\]
A direct differentiation gives
\[
T_x'(u)=\frac{1-x+xu-u^x}{u^x(1-u)^2}.
\]
If \(x>1\), convexity of \(u\mapsto u^x\) and its tangent at \(u=1\) give
\[
u^x\ge 1+x(u-1)=1-x+xu,
\]
strictly for \(0<u<1\). Thus \(T_x'(u)<0\), so \(T_x(e^{-t})\) increases in \(t\) and \(R(t)\) decreases. Hence \(K\mid A\) is smaller than \(K\) in likelihood-ratio order, and therefore in stochastic order. Since \(t\mapsto e^{-zt}\) is strictly decreasing,
\[
\mathbb E[e^{-zK}\mid A]>\mathbb E[e^{-zK}],
\]
so the covariance is positive. If \(0<x<1\), concavity reverses every inequality and the covariance is negative. If \(x=1\), the likelihood ratio is constant and the covariance is zero. Because \(x=\lambda/\lambda_k\), this proves
\[
\operatorname{sign}\operatorname{Cov}(I_k,I_{k+1})
=
\operatorname{sign}(\lambda-\lambda_k).
\]

For sufficiency of the classification, suppose \(\lambda_1=\cdots=\lambda_{n-1}\). The first \(n-1\) observations are iid and continuous. Their full rank permutation is independent of their order statistics, and \(I_2,\ldots,I_{n-1}\) are functions only of that rank permutation; by the classical record theorem they are mutually independent. The maximum \(M_{n-1}=\max(X_1,\ldots,X_{n-1})\) is an order statistic and is therefore independent of the entire preceding record-indicator vector. Since \(X_n\) is also independent of the first \(n-1\) observations,
\[
I_n=\mathbf 1\{X_n>M_{n-1}\}
\]
is independent of \((I_2,\ldots,I_{n-1})\), whatever the positive value of \(\lambda_n\). Thus all \(I_2,\ldots,I_n\) are mutually independent.

For necessity, the case \(n=2\) is immediate because the condition imposes no equality beyond the single scale \(\lambda_1\). Let \(n\ge3\) and suppose \(I_2,\ldots,I_n\) are mutually independent. Pairwise independence of \(I_2\) and \(I_3\), together with the adjacent-sign lemma for \(k=2\), forces \(\lambda_2=\lambda_1\). Inductively, suppose \(\lambda_1=\cdots=\lambda_{k-1}\) for some \(2\le k\le n-1\). Mutual independence gives independence of \(I_k\) and \(I_{k+1}\), so their covariance is zero; the adjacent-sign lemma then forces \(\lambda_k=\lambda_1\). Hence \(\lambda_1=\cdots=\lambda_{n-1}\), completing the proof.

## Verification
The proof is exact and does not depend on numerical experimentation. As an algebraic cross-check, if
\[
L_q(s)=\mathbb E[e^{-sM}]=\prod_{j=1}^{q}\frac{j}{s+j},
\]
then direct integration yields
\[
\Pr(I_k=1)=L_q(x),
\]
\[
\Pr(I_{k+1}=1)=L_q(z)-\frac{z}{x+z}L_q(x+z),
\]
and
\[
\Pr(I_k=1,I_{k+1}=1)=\frac{x}{x+z}L_q(x+z).
\]
Consequently
\[
\operatorname{Cov}(I_k,I_{k+1})
=
\frac{x+zL_q(x)}{x+z}L_q(x+z)-L_q(x)L_q(z).
\]
The likelihood-ratio argument above proves the sign of this expression for every integer \(q\ge1\) and all \(x,z>0\), rather than merely checking selected parameters.

The boundary cases are explicit. When \(x=1\), corresponding to \(\lambda_k=\lambda\), the ratio \(f_{K\mid A}/f_K\) is constant and the covariance is exactly zero. When \(n=2\), there is only one nonconstant record indicator, so mutual independence is automatic and the theorem's equality condition is vacuous.

## Relationship to prior work
Lo and Babou, arXiv:2602.20416v1, state a much broader independence claim for record indicators from independent, non-identically distributed observations. The theorem above instead gives an exact finite-prefix classification in a concrete parametric family; it is compatible with published counterexamples to the broader claim and does not rely on that claim.

Ahsanullah and Nevzorov, DOI:10.2991/jsta.2017.16.3.1, study records from nonidentically distributed exponential variables. Their short paper gives explicit low-index record-indicator probabilities and states that independence is not preserved in general when the exponential parameters differ. Those formulas cover the earliest special cases of the dependence phenomenon, but the inspected article does not state the all-\(n\) finite-prefix equivalence, the unrestricted terminal scale, or the adjacent covariance sign law under an equal-scale prefix.

The \(F^\alpha\)-scheme literature, including Doukhan, Klesov, and Steinebach, DOI:10.1007/978-3-319-12442-1_16, records that record indicators are independent in an \(F^\alpha\)-scheme and cites a converse for an entire independent continuous sequence. That infinite-sequence structural result is consistent with the corollary that an infinite exponential-scale sequence can retain independent record indicators only when its scales stay equal. It does not subsume the finite-prefix theorem here, because a finite prefix may have an arbitrary terminal scale while still having mutually independent record indicators.

A focused comparison against published research records found the closest item to be “A counterexample to universal record-indicator independence for non-identical observations” (identifier `2026/9/21/SCOPE-nonidentical-record-indicator-independence-counterexample--638a911adad4`). That result uses a three-observation uniform-scale family to show positive or negative covariance and does not imply the present exponential all-\(n\) classification or its one-step sign law.

## Limitations
The theorem is specific to independent exponential scale families and strict upper records. It does not classify finite-prefix independence for arbitrary nonidentical continuous distributions, multivariate records, lower records, dependent observations, or censoring/truncation schemes. The sign law assumes the scales before the tested time are equal; no claim is made about the sign of adjacent record covariance under an arbitrary heterogeneous history.

The inspected literature supports originality of the stated finite-prefix classification, but literature search cannot prove uniqueness. An equivalent finite-prefix result could exist in older record-theory literature under a different parameterization or terminology. The infinite-sequence equal-scale corollary is not presented as a new theorem because it is consistent with, and may be obtained from, the known \(F^\alpha\)-scheme converse.

## References
1. G. S. Lo and E. H. Babou, “Independence of the indicator functions of record values for Multivariate independent data,” arXiv:2602.20416v1, first public 23 February 2026.
2. M. Ahsanullah and V. B. Nevzorov, “On Records in Sequences of Nonidentically Distributed Exponential Random Variables,” Journal of Statistical Theory and Applications 16 (2017), 284–287, DOI:10.2991/jsta.2017.16.3.1.
3. P. Doukhan, O. I. Klesov, and J. G. Steinebach, “Strong Laws of Large Numbers in an \(F^\alpha\)-Scheme,” in Mathematical Statistics and Limit Theorems (2015), 287–303, DOI:10.1007/978-3-319-12442-1_16.
