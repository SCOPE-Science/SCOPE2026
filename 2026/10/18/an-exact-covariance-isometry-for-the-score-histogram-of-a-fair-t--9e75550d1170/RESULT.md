# An exact covariance isometry for the score histogram of a fair tournament

## Finding

Let \(n\ge 2\). Orient each edge of the complete graph on \(n\) labeled vertices independently and fairly, obtaining a random round-robin tournament. Write \(S_v\in\{0,\ldots,n-1\}\) for the number of games won by vertex \(v\) and \(H_j=|\{v:S_v=j\}|\) for the frequency of score \(j\). Put \(K=n-1\), \(p_j=2^{-K}\binom K j\), and \(P=\operatorname{diag}(p_0,\ldots,p_K)\). Every \(p_j\) is positive.

**Exact covariance-isometry theorem.** For any functions \(f,g:\{0,\ldots,K\}\to\mathbb R\), if \(R\sim\operatorname{Bin}(K,1/2)\), then
\[
\operatorname{Cov}\!\left(\sum_{v=1}^n f(S_v),\sum_{v=1}^n g(S_v)\right)
=n\left[\operatorname{Cov}(f(R),g(R))-
\frac{\operatorname{Cov}(f(R),R)\operatorname{Cov}(g(R),R)}{\operatorname{Var}(R)}\right],
\qquad \operatorname{Var}(R)=K/4.
\]
Thus the covariance of all additive score statistics agrees *exactly*, at every finite \(n\), with \(n\) independent binomial scores after orthogonal removal of the constant and linear score directions. This is a second-moment identity, not equality in distribution.

In particular, for \(\Sigma=\operatorname{Cov}(H)\), define the vectors
\[
 u_j=\sqrt{p_j},\qquad
 w_j=\frac{2j-K}{\sqrt K}\sqrt{p_j}\quad(0\le j\le K).
\]
They are orthonormal and
\[
 \boxed{\ P^{-1/2}\Sigma P^{-1/2}=n(I-uu^{\mathsf T}-ww^{\mathsf T}).\ }
\]
For \(n\ge3\) its complete spectrum is \(0\) with multiplicity \(2\), and \(n\) with multiplicity \(n-2\). For \(n=2\) the matrix is zero (the multiplicity \(n-2\) is zero). The two null directions encode \(\sum_j H_j=n\) and \(\sum_j jH_j=nK/2\).

Consequently the ungrouped Pearson quadratic score
\[
 X_n=\sum_{j=0}^K\frac{(H_j-np_j)^2}{np_j}
\]
has the **exact mean** \(\mathbb E X_n=n-2\). No claim that \(X_n\) has a chi-square law, approximately or exactly, is made.

For every \(f\),
\[
 \operatorname{Var}\!\left(\sum_v f(S_v)\right)
 =n\min_{a,b\in\mathbb R}\mathbb E\big[(f(R)-a-bR)^2\big]
 \le n\operatorname{Var}(f(R)).
\]
The variance vanishes exactly when \(f\) is affine on \(\{0,\ldots,K\}\), and the upper bound is attained exactly when \(\operatorname{Cov}(f(R),R)=0\). Both conditions are sharp; nonconstant upper-bound equality functions exist when \(n\ge3\).

An explicit simultaneous orthogonalization is provided by the classical symmetric binomial Krawtchouk polynomials \(Q_r(j)\), defined by
\[
 \sum_{r=0}^{K} Q_r(j)z^r=(1-z)^j(1+z)^{K-j}.
\]
For \(2\le r,s\le K\),
\[
 \operatorname{Cov}\!\left(\sum_v\frac{Q_r(S_v)}{\sqrt{\binom K r}},
                           \sum_v\frac{Q_s(S_v)}{\sqrt{\binom K s}}\right)
 =n\,\mathbf1_{\{r=s\}}.
\]
The \(r=0,1\) additive modes are deterministic. The higher modes are uncorrelated; **independence is not asserted**.

## Assumptions and scope

All \(\binom n2\) game outcomes are independent and each direction has probability \(1/2\). Scores count outgoing wins, not signed win margins. The theorem concerns the complete score histogram \((H_0,\ldots,H_{n-1})\) with fixed size \(n\). It does not extend as stated to heterogeneous Bradley--Terry win probabilities, randomly missing games, or tournaments conditioned on regularity. The case \(n=2\) is included as a degenerate boundary; nonzero covariance eigenvalues occur only for \(n\ge3\).

## Proof

Fix distinct vertices \(v,w\). Let \(B_v,B_w\) independently have distribution \(\operatorname{Bin}(n-2,1/2)\), representing their wins against vertices other than each other. Let \(Z\) be an independent fair Bernoulli variable recording whether \(v\) beats \(w\). The independent-edge model gives
\[
 (S_v,S_w)\ \overset d=\ (B_v+Z,B_w+1-Z).
\]
Set \(\delta_f=\mathbb E[f(B+1)-f(B)]\), where \(B\sim\operatorname{Bin}(K-1,1/2)\). Conditioning on \(Z\) and using conditional independence yields, for distinct vertices,
\[
 \operatorname{Cov}(f(S_v),g(S_w))=-\tfrac14\delta_f\delta_g.
\]
The independent fair-edge model also implies \(S_v\sim R\sim\operatorname{Bin}(K,1/2)\). Summing diagonal and off-diagonal contributions gives
\[
 \operatorname{Cov}\!\left(\sum_v f(S_v),\sum_v g(S_v)\right)
 =n\operatorname{Cov}(f(R),g(R))
 -\frac{nK}{4}\delta_f\delta_g.
\]
The binomial size-bias identity, valid for every function on the finite support, is
\[
 \operatorname{Cov}(f(R),R)=\frac K4\,\delta_f.
\]
Indeed, write \(R=B+Z\) as a sum of \(K\) independent fair Bernoulli indicators, condition on each one, and sum their centered covariances. Substitution proves the theorem for all \(f,g\), including \(n=2\).

For the histogram matrix, take \(f(j)=\mathbf1_{\{j=a\}}\) and \(g(j)=\mathbf1_{\{j=b\}}\). Writing \(p=(p_j)\), the identity becomes
\[
 \Sigma=n(P-pp^{\mathsf T})-
 \frac{nK}{4}dd^{\mathsf T},\qquad
 d_j=\Pr(B=j-1)-\Pr(B=j)
 =\frac{2(2j-K)}K p_j,
\]
with zero probabilities outside the support of \(B\). In the last equality, the relations \(\Pr(B=j-1)=2j p_j/K\) and \(\Pr(B=j)=2(K-j)p_j/K\) hold at the endpoints as well. Therefore \(P^{-1/2}p=u\) and \(P^{-1/2}d=2w/\sqrt K\), giving the displayed covariance projector.

The binomial identities \(\sum_jp_j=1\), \(\mathbb E(2R-K)=0\), and \(\mathbb E(2R-K)^2=K\) show that \(u,w\) are orthonormal. An orthogonal projector of rank \((K+1)-2=n-2\), multiplied by \(n\), has exactly the stated spectrum. The observed histogram constraints supply both zero modes. Taking the trace gives \(\mathbb EX_n=\operatorname{tr}(P^{-1/2}\Sigma P^{-1/2})/n=n-2\).

Projecting \(f(R)\) in \(L^2(\operatorname{Bin}(K,1/2))\) onto the span of \(1,R\) gives the minimum-square-error and both equality characterizations. For the final orthogonal basis, multiply the two Krawtchouk generating functions, average over \(R\), and use
\[
 \mathbb E\!\left[(1-z)^R(1+z)^{K-R}(1-y)^R(1+y)^{K-R}\right]=(1+zy)^K.
\]
Comparison of coefficients gives \(\mathbb E Q_r(R)Q_s(R)=\mathbf1_{\{r=s\}}\binom K r\); modes of degree \(r\ge2\) are orthogonal to both \(1\) and \(R\). Applying the general covariance identity proves their covariance statement.

## Verification

The standalone Python standard-library program `verify.py` evaluates exact rational covariances for all labeled orientations of complete graphs on \(2\) through \(6\) vertices, totaling \(33{,}866\) tournaments. It checks every histogram covariance entry, both deterministic constraints, the projector polynomial identity, the exact Pearson expectation, the all-score-function residual-variance equality for three nonaffine probes, and the complete Krawtchouk cross-covariance identities up to \(n=8\). Its recorded run completed with \(871\) exact assertions. The proof, rather than these finite checks, establishes all \(n\).

Reproduce with `python verify.py` using a standard Python 3 installation; no extra packages or input datasets are required. The implementation explicitly enumerates individual edge orientations for \(n\le6\), not just realizable score sequences.

## Relationship to prior work

The complete score-sequence constraints are classical (Landau and Moon). Aldous and Kolesnik's 2018 probability preprint analyzes mean scores and Bradley--Terry representations; Kolesnik and Sanchez's 2020 work gives zonotopal characterizations of possible scores. Claesson and collaborators' 2022 preprint enumerates distinct score sequences, not their probabilities under independent fair orientations. The present claim instead addresses the full finite-sample covariance of **score frequencies under the uniform probability measure on labeled tournaments**, with an exact isometry for all additive score statistics.

Binomial Krawtchouk orthogonality is classical, and neither that orthogonality nor the fixed total-win identity is claimed as new. What is assessed here is their exact combination into the entire covariance projector and its implications. A 2026 thesis by Zegers studies concentration and a local central limit theorem for random-tournament score-bin sizes; only its repository abstract was accessible for comparison, leaving a nontrivial residual risk of implicit overlap. An Erdős--Rényi graph study by Alarfaj, Taylor and Bogachev concerns a different model: a shared **undirected** edge contributes positive, not complementary, score dependence.

## Limitations

The result concerns second moments only and does not prove asymptotic independence, a multivariate central limit theorem, a chi-square approximation, optimal goodness-of-fit critical values, or robustness under biased/missing games. Unusually small expected counts at extreme scores make chi-square distributional calibration delicate. The proof is self-contained under the stated fair independent-edge assumptions, but priority over all historical literature has not been independently established. The unavailable full text of Zegers's related 2026 thesis is a specific remaining comparison risk; its abstract does not by itself establish either equivalence or noncoverage.

## References

- D. J. Aldous and B. Kolesnik, *To stay discovered: On tournament mean score sequences and the Bradley--Terry model*, arXiv:1811.06662v1 (first public 2018-11-16), https://arxiv.org/html/1811.06662v1.
- B. Kolesnik and M. Sanchez, *The geometry of random tournaments*, arXiv:2009.09322v1 (first public 2020-09-19), https://arxiv.org/html/2009.09322v1.
- A. Claesson, M. Dukes, A. F. Franklín and S. Ö. Stefánsson, *Counting tournament score sequences*, arXiv:2209.03925v1 (first public 2022-09-08), https://arxiv.org/abs/2209.03925.
- B. Alarfaj, C. Taylor and L. Bogachev, *The joint node degree distribution in the Erdős--Rényi network*, arXiv:2303.05138 (2023), https://arxiv.org/abs/2303.05138.
- S. P. C. Zegers, *The Heat Capacity of Random Tournaments*, master's thesis, TU Delft (2026), repository abstract: https://repository.tudelft.nl/record/uuid:673a65cb-d6aa-4e3f-a4b6-43d567e500ca.
- B. Alspach and K. B. Reid, *Degree frequencies in digraphs and tournaments*, Journal of Graph Theory 2 (1978), 241--249, https://doi.org/10.1002/jgt.3190020307.
