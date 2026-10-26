# Universal negative Shannon–Simpson covariance for arbitrary finite Dirichlet priors

## Finding
Let \(m\ge2\) and \(\alpha_1,\ldots,\alpha_m>0\). For \(P\sim\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_m)\), define Shannon entropy \(H=-\sum_{i=1}^mP_i\log P_i\) and Simpson concentration \(Q=\sum_{i=1}^mP_i^2\). Write \(A=\sum_i\alpha_i\), \(w_i=\alpha_i/A\), \(\kappa=\sum_{i<j}\alpha_i\alpha_j\), and \(\psi\) for the digamma function. For sequences \(f_i,g_i\), define
\[
\operatorname{Cov}_w(f,g)=\sum_iw_if_ig_i-\Big(\sum_iw_if_i\Big)\Big(\sum_iw_ig_i\Big).
\]
The **exact identity**, for all positive real parameters, is
\[
\boxed{\displaystyle\operatorname{Cov}(H,Q)=-\frac{2}{A(A+1)(A+2)}\left\{\frac{\kappa}{A+1}+A\operatorname{Cov}_w\bigl(\alpha_i,\psi(\alpha_i+1)\bigr)\right\}<0.}
\]
In particular, the concentration and Shannon entropy are strictly negatively correlated (the variables have strictly positive variances). Equivalently, Shannon entropy and Gini–Simpson diversity \(1-Q\) have strictly positive covariance. More precisely,
\[
-\operatorname{Cov}(H,Q)\geq \frac{2\kappa}{A(A+1)^2(A+2)},
\]
with equality **if and only if** \(\alpha_1=\cdots=\alpha_m\).

## Assumptions and scope
The integer \(m\ge2\) is finite; every concentration parameter \(\alpha_i\) is strictly positive and real. No exchangeability or equality of the parameters is assumed. The natural logarithm is used. On the positive simplex the functionals are bounded, so all expectations and covariances exist. A single category is excluded because both diversity statistics are constant in that case. The term *Simpson concentration* unambiguously means \(Q=\sum_iP_i^2\), rather than the alternative diversity convention \(1-Q\).

## Proof
The Dirichlet moment formula, for any nonnegative real \(r_i\), is
\[
\mathbb E\prod_{i=1}^m P_i^{r_i}=\frac{\Gamma(A)}{\Gamma(A+\sum_i r_i)}\prod_i\frac{\Gamma(\alpha_i+r_i)}{\Gamma(\alpha_i)}.
\]
Differentiating this identity at a unit exponent yields
\[
\mathbb E H=\psi(A+1)-A^{-1}\sum_i\alpha_i\psi(\alpha_i+1).
\]
Let \(S=\sum_i\alpha_i(\alpha_i+1)\), \(B=\sum_i\alpha_i\psi(\alpha_i+1)\), and \(T=\sum_i\alpha_i(\alpha_i+1)\psi(\alpha_i+1)\). The elementary quadratic moment is \(\mathbb E Q=S/[A(A+1)]\).

For any bounded measurable functional \(F\), quadratic Dirichlet tilting gives the **normalized** identity
\[
\mathbb E_{\alpha}[P_i^2F(P)]=\frac{\alpha_i(\alpha_i+1)}{A(A+1)}\,\mathbb E_{\alpha+2e_i}[F(P)].
\]
Inserting the entropy expectation with the modified parameters \(\alpha+2e_i\), and using \(\psi(z+1)=\psi(z)+1/z\), gives
\[
\mathbb E(HQ)=\frac{S}{A(A+1)}\psi(A+3)-\frac{SB+2T+2S+A}{A(A+1)(A+2)}.
\]
This follows because the shifted numerator of the entropy formula is \(B+2\psi(\alpha_i+1)+(\alpha_i+2)[1/(\alpha_i+1)+1/(\alpha_i+2)]\), and multiplying it by \(\alpha_i(\alpha_i+1)\) and summing gives \(SB+2T+2S+A\).

Subtract \(\mathbb E H\,\mathbb E Q\), apply \(\psi(A+3)-\psi(A+1)=1/(A+1)+1/(A+2)\), and collect the terms with \(B,T\). This gives
\[
\operatorname{Cov}(H,Q)=-\frac{2}{A(A+1)(A+2)}\left\{\frac{\kappa}{A+1}+A\left[\frac{T-B}{A}-\frac{(S-A)B}{A^2}\right]\right\}.
\]
The bracketed expression in square brackets equals \(\operatorname{Cov}_w(\alpha_i,\psi(\alpha_i+1))\), because \(T-B=\sum_i\alpha_i^2\psi(\alpha_i+1)\) and \(S-A=\sum_i\alpha_i^2\). This proves the displayed exact identity.

Finally, the standard pairwise rearrangement identity reads
\[
\operatorname{Cov}_w(\alpha_i,\psi(\alpha_i+1))=\sum_{i<j}w_iw_j(\alpha_i-\alpha_j)\bigl[\psi(\alpha_i+1)-\psi(\alpha_j+1)\bigr]\ge0.
\]
The digamma function is strictly increasing on positive arguments, so equality occurs precisely when all \(\alpha_i\) agree. Since \(m\ge2\) and all parameters are positive, \(\kappa>0\), proving strict negativity and the equality characterization for the quantitative bound. When parameters are equal to \(a\), direct substitution yields
\[
\operatorname{Cov}(H,Q)=-\frac{(m-1)a}{(ma+1)^2(ma+2)}.
\]
For fixed total concentration \(A=4\), direct evaluation using \(\psi(k+1)=\sum_{j=1}^{k}1/j-\gamma\) for integer \(k\) yields \(\operatorname{Cov}_{(1,3)}(H,Q)=-37/1200\) and \(\operatorname{Cov}_{(2,2)}(H,Q)=-1/75\). Thus the equality case for the pair-mass lower bound is not a universal extremizer over parameters of fixed total concentration.

## Verification
The accompanying standalone \(\texttt{verify.py}\) uses exact fractions and harmonic numbers for several integer parameter vectors. It independently reconstructs \(\mathbb E(HQ)\) by summing Dirichlet-tilted entropy expectations and then compares the outcome against the separate pairwise-covariance formula. It asserts both rational fixed-concentration examples and the symmetric expression. Symbolic algebra also verified the identity of the general three-coordinate moment formula with the claimed pairwise decomposition when each digamma value is treated as an independent symbol, so that no special-function identity beyond the stated recurrence is concealed in the simplification. These finite and symbolic checks supplement, but do not replace, the general proof above.

## Relationship to prior work
Huillet and Paroissin [1] study symmetric finite Dirichlet species partitions and calculate the mean of Simpson concentration; their discussion introduces Shannon entropy but explicitly proceeds with the Simpson functional. Archer, Park, and Pillow [2] derive Bayesian means and variances of Shannon entropy, not its joint covariance with Simpson concentration. Cerquetti [3] addresses both diversity measures as members of the Tsallis index family, chiefly through first and second moments of each index under Gnedin–Pitman laws, whose finite Dirichlet subclass is symmetric; the paper does not state the cross-index covariance or the arbitrary asymmetric Dirichlet sign-and-remainder identity proved here. Thus these papers supply the probabilistic motivation and related moments but not an identified implication yielding this result. The direct moment algebra is elementary; no assertion of exhaustive priority or independence verification is made.

## Limitations
This statement concerns **population-level random probabilities** under a finite Dirichlet law, not observed sample plug-in estimators, arbitrary priors, or infinite-dimensional Dirichlet processes. The pair-mass bound becomes equality at symmetric parameters, but it does **not** claim global minimization or maximization of covariance over all parameter vectors of fixed \(A\). The example explicitly shows that such an interpretation would be incorrect. A targeted historical search cannot exclude every equivalent formula in older joint-diversity literature; independent expert validation and exhaustive priority review remain to be done.

## References
[1] T. Huillet and C. Paroissin, *Sampling from Dirichlet populations: estimating the number of species*, arXiv:0809.4181v1, submitted 24 September 2008. https://arxiv.org/abs/0809.4181

[2] E. Archer, I. M. Park, and J. W. Pillow, *Bayesian Entropy Estimation for Countable Discrete Distributions*, Journal of Machine Learning Research **15** (2014), 2833–2868. https://jmlr.org/papers/v15/archer14a.html

[3] A. Cerquetti, *Bayesian nonparametric estimation of Tsallis diversity indices under Gnedin–Pitman priors*, arXiv:1404.3441v1, submitted 14 April 2014. https://arxiv.org/abs/1404.3441
