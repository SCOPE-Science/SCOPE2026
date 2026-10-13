# Sharp six-sample Wilcoxon size under pairwise-independent ranked signs

## Finding

For the ordinary one-sided six-observation Wilcoxon signed-rank statistic, consider the usual independence-calibrated rejection event \(W^+\ge19\), whose independent-sign probability is \(3/64\). If, conditional on all six observed absolute values, the six ranked signs are individually fair and pairwise independent, then the **complete sharp attainable range** of its true rejection probability is
\[
\boxed{0\ \le\ \Pr(W^+\ge19)\ \le\ \frac16.}
\]
Every value in this interval is attained, including both endpoints. Both extremes can be realized with six observations having the same atomless distribution symmetric about zero, such that **every two observations are independent**. The largest attained rejection rate is \(32/9\) times the classical exact independent-sign size \(3/64\).

## Assumptions and scope

Let \(X_1,\ldots,X_6\) be nonzero real random observations with almost surely distinct absolute values. Order their absolute values increasingly and define \(B_j=\mathbf 1\{X_{(j)}^*>0\}\), where \(X_{(j)}^*\) is the signed observation with the \(j\)-th smallest absolute value. Thus \(B_j\in\{0,1\}\), \(W^+=\sum_{j=1}^6 jB_j\), and \(\mathcal A=\sigma(|X_1|,\ldots,|X_6|)\). Assume for all \(j\) and all distinct \(i,j\), almost surely,
\[
\Pr(B_j=1\mid\mathcal A)=\frac12,\qquad
\Pr(B_i=B_j=1\mid\mathcal A)=\frac14.
\]
These conditions permit higher-order sign dependence. They are **stronger than merely demanding pairwise independence of the observations**: the interval theorem is asserted for the rank-conditioned class, while the constructions additionally realize pairwise independence of the observations themselves. No independent-sample validity beyond that class is asserted.

## Proof

**1. Rejection geometry.** The total positive-rank weight is \(21\). The four largest ranks \(3,4,5,6\) sum to \(18\), while the first two ranks sum to \(3\). If any of the four largest signs is zero, then \(W^+\le18\). If all four are one, \(W^+=18+B_1+2B_2\). Consequently
\[
\{W^+\ge19\}=\{B_3=B_4=B_5=B_6=1,\ B_1+B_2\ge1\}.
\]
Under six fully independent fair signs this contains precisely three of the \(64\) sign vectors, hence has probability \(3/64\).

**2. Universal conditional upper bound.** Put \(K=B_3+B_4+B_5+B_6\). Pairwise fairness conditional on \(\mathcal A\) gives
\[
\mathbb E(K\mid\mathcal A)=2,\quad
\mathbb E\!\left(K(K-1)\mid\mathcal A\right)=3,
\]
and therefore \(\mathbb E((K-1)(K-2)\mid\mathcal A)=1\). For integers \(0\le k\le4\), \((k-1)(k-2)\ge6\mathbf1\{k=4\}\). Thus
\[
\Pr(W^+\ge19\mid\mathcal A)
\le\Pr(K=4\mid\mathcal A)\le\frac16
\]
almost surely. Taking expectations establishes the upper bound; nonnegativity gives the lower bound.

**3. Upper extremizer.** Choose \(K\in\{1,2,4\}\) with masses \(1/3,1/2,1/6\). Given \(K=k\), choose uniformly a \(k\)-subset of the four high-rank positions \(3,4,5,6\), setting exactly those signs positive. For \(K=1\) or \(K=4\), choose \((B_1,B_2)\) uniformly from \((1,0),(0,1)\); for \(K=2\), choose it uniformly from \((0,0),(1,1)\). The moment identities \(\mathbb EK=2\) and \(\mathbb E[K(K-1)]=3\), together with exchangeability of the four high signs, show they are pairwise independent fair bits. Each low sign is fair conditional on the entire high vector, and \(\Pr(B_1=B_2=1)=\frac12\Pr(K=2)=1/4\). Hence all six signs are pairwise independent fair. Rejection occurs exactly when \(K=4\), giving probability \(1/6\).

**4. Lower extremizer and full interval.** Choose instead \(K\in\{0,2,3\}\) with masses \(1/6,1/2,1/3\); conditionally choose a uniform \(K\)-subset of the four high positions, and take the two low bits independently fair and independent of those high bits. The same two moment identities establish pairwise independence of all six bits. Since \(K\le3\), the rejection probability is zero. Mixing these two sign-vector laws in any proportion preserves pairwise independence and produces every probability in \([0,1/6]\).

**5. Realization by symmetric continuous observations.** Independently of either sign-vector law, draw six iid magnitudes \(A_i\) uniformly on \((1,2)\). Give the observation with the \(j\)-th smallest magnitude the sign \(2B_j-1\), defining \(X_i=(2B_{r(i)}-1)A_i\). Almost surely the magnitudes are distinct. Conditional on all magnitudes, the ranked signs have the requisite joint law. For any two distinct observation labels, their individual signs are conditionally fair and jointly independent. Thus the conditional two-observation law is the product of the independent symmetric signings of their two magnitudes; integrating over independent \(A_i,A_j\) shows that \(X_i\) and \(X_j\) are independent. All six share the same continuous symmetric marginal. The extreme and mixed rates are therefore realized in the stated class even when the original observations themselves are pairwise independent. \(\square\)

## Verification

The independent standard-library script `verify.py` enumerates all \(64\) ranked-sign configurations with exact rational arithmetic. It checks normalization, six fair marginal probabilities, fifteen pairwise joint probabilities, both endpoint rejection probabilities, the independent-sign benchmark, the quadratic pointwise bound, and five mixtures. An independent numerical linear program on the same \(64\)-atom probability simplex, with all pairwise moment constraints, returned minimum \(0\) and maximum \(1/6\); the mathematical proof does not rely on this numerical computation. Execute `python verify.py` in the directory containing this document.

## Relationship to prior work

The classical Wilcoxon signed-rank statistic and its independent-sign calibration are standard. Rosenblatt and Benjamini [1] define it and study relative power for independent sampling, rather than the sharp tail-probability range under pairwise-independent ranked signs. Datta, Nevalainen and Oja [2] devise modified signed-rank procedures for clustered dependent data and asymptotic validity, not this particular finite-sample extremal calibration. Ramachandra and Natarajan [3] give important general bounds and linear-programming formulations for pairwise-independent Bernoulli sums, including intersection probabilities; accordingly the **general intersection bound and the moment method are not claimed as new**. The present claim is the explicit complete sharp range for this natural weighted Wilcoxon rejection event, including attainable lower and upper endpoint couplings and realization through pairwise-independent symmetric continuous observations. A generic linear program represents the problem but does not by itself provide these closed-form constructions or the statistical interpretation.

## Limitations

Only the one-sided \(n=6\) rejection event \(W^+\ge19\) and the stated **magnitude-conditional** pairwise sign assumptions are analyzed. The analysis does not claim a uniform \(1/6\) upper bound over every law of merely pairwise-independent symmetric observations without the conditional assumption; it supplies examples of such observations attaining the endpoints. No claim is made for other sample sizes, other critical levels, or fully arbitrary dependence. The mathematical bound is exact, but historical priority beyond the inspected literature is not independently certified.

## References

[1] J. Rosenblatt and Y. Benjamini, *Another Argument in Favour of Wilcoxon's Signed Rank Test*, arXiv:1311.5354v1, first public 2013-11-21, https://arxiv.org/html/1311.5354v1.

[2] S. Datta, J. Nevalainen and H. Oja, *A General Class of Signed Rank Tests for Clustered Data when the Cluster Size is Potentially Informative*, Journal of Nonparametric Statistics 24 (2012), 797–808, first public online 2012-05-01, DOI:10.1080/10485252.2012.672647, https://pmc.ncbi.nlm.nih.gov/articles/PMC3467023/.

[3] A. K. Ramachandra and K. Natarajan, *Tight Probability Bounds with Pairwise Independence*, arXiv:2006.00516v1, first public 2020-05-31, https://arxiv.org/html/2006.00516v6; subsequently SIAM Journal on Discrete Mathematics 37 (2023), 516–555.
