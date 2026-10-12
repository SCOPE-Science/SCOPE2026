# Adjacent changes recover latent Gini–Simpson diversity in symmetric Pólya sampling
## Finding
Let \(m\ge2\), \(lpha>0\), and \(n\ge2\). Draw a random probability vector \(P=(P_1,\ldots,P_m)\) from the symmetric Dirichlet law \(\operatorname{Dirichlet}(lpha,\ldots,lpha)\). Conditional on \(P\), let \(X_1,\ldots,X_n\) be iid categorical observations with probabilities \(P\). Define the latent Gini–Simpson diversity
\[
D=1-\sum_{j=1}^m P_j^2,
\]
and the adjacent-change count and rate
\[
T_n=\sum_{i=1}^{n-1}\mathbf 1\{X_i
e X_{i+1}\},\qquad A_n=rac{T_n}{n-1}.
\]
Then the local change rate is conditionally unbiased for the latent diversity:
\[
\mathbb E[A_n\mid P]=D.
\]
Consequently,
\[
\operatorname{Cov}(A_n,D)=\operatorname{Var}(D)=rac{2lpha(lpha+1)(m-1)}{(mlpha+1)^2(mlpha+2)(mlpha+3)}>0.
\]
Writing \(c=mlpha\), the complete finite-sample variance is
\[
\operatorname{Var}(T_n)=rac{lpha(lpha+1)(m-1)\left[c^2(n-1)+c(7n-9)+2n^2+2n-6ight]}{(c+1)^2(c+2)(c+3)}.
\]
Thus
\[
\operatorname{Corr}(A_n,D)=rac{\sqrt2\,(n-1)}{\sqrt{c^2(n-1)+c(7n-9)+2n^2+2n-6}}>0,
\]
and for fixed \(m,lpha\),
\[
\operatorname{Corr}(A_n,D)=1-rac{(c+1)(c+6)}{4n}+O(n^{-2}).
\]
In particular, the adjacent-change rate becomes asymptotically perfectly correlated with the latent Gini–Simpson diversity even though the observed sequence remains exchangeable rather than iid unconditionally.

## Assumptions and scope
The closed forms above use a symmetric finite-color Dirichlet directing law with \(m\ge2\), \(lpha>0\), and a sample of length \(n\ge2\). The identity \(\mathbb E[A_n\mid P]=D\), and hence \(\operatorname{Cov}(A_n,D)=\operatorname{Var}(D)\), does not require symmetry and holds for any random categorical directing vector for which the displayed second moments exist. Symmetry is used only for the explicit Dirichlet moments and the closed correlation formula.

## Proof
Conditional on \(P\), every adjacent pair is iid from the same categorical law, so
\[
\mathbb P(X_i
e X_{i+1}\mid P)=1-\sum_{j=1}^mP_j^2=D.
\]
Averaging the \(n-1\) indicators gives \(\mathbb E[A_n\mid P]=D\). Therefore
\[
\mathbb E[A_nD]=\mathbb E[D\,\mathbb E(A_n\mid P)]=\mathbb E[D^2],
\]
which proves \(\operatorname{Cov}(A_n,D)=\operatorname{Var}(D)\).

For a symmetric Dirichlet vector, with rising factorial \((x)_r=x(x+1)\cdots(x+r-1)\),
\[
\mathbb E\!\left[\prod_{j=1}^mP_j^{r_j}ight]=rac{\prod_{j=1}^m(lpha)_{r_j}}{(mlpha)_{\sum_jr_j}}.
\]
Applying this with exponent patterns \((2)\), \((4)\), and \((2,2)\) to \(S_2=\sum_jP_j^2\) gives
\[
\mathbb E[D]=rac{lpha(m-1)}{mlpha+1},
\qquad
\operatorname{Var}(D)=rac{2lpha(lpha+1)(m-1)}{(mlpha+1)^2(mlpha+2)(mlpha+3)}.
\]

Write \(I_i=\mathbf 1\{X_i
e X_{i+1}\}\). For adjacent edges, conditional on \(P\),
\[
\mathbb E[I_iI_{i+1}\mid P]=1-2S_2+S_3,
\qquad S_3=\sum_jP_j^3.
\]
Dirichlet moments then yield
\[
\operatorname{Cov}(I_i,I_{i+1})=rac{lpha(lpha+1)(m-1)}{(mlpha+1)^2(mlpha+2)}.
\]
For disjoint edges, conditional independence gives
\[
\operatorname{Cov}(I_i,I_j)=\operatorname{Var}(D)\qquad (|i-j|\ge2).
\]
There are \(n-1\) edge variances, \(n-2\) unordered adjacent-edge pairs, and \((n-2)(n-3)/2\) unordered disjoint-edge pairs. Summing them gives the stated closed form for \(\operatorname{Var}(T_n)\). Combining it with \(\operatorname{Cov}(T_n,D)=(n-1)\operatorname{Var}(D)\) gives the correlation formula. Expanding its denominator at fixed \(c=mlpha\) gives the stated \(n^-1\) correction.

## Verification
The accompanying exact-arithmetic checker enumerates every sequence in 45 parameter cases with \(m\in\{2,3,4\}\), \(lpha\in\{1/2,1,3/2\}\), and \(2\le n\le6\), covering 20,007 sequence states. It verifies normalization, the mean transition count, the variance of \(T_n\), and the mixed moment with the posterior expectation of \(D\). These finite checks support but do not replace the analytic proof for arbitrary admissible parameters.

## Relationship to prior work
Eryilmaz's multicolor Pólya-urn paper identifies the sampled color sequence as exchangeable, gives its Dirichlet de Finetti measure, and derives joint distributions of run statistics. Those results supply the natural model and the run-statistic literature context, but the inspected full text integrates over the directing probability vector and does not state a mixed moment between the observed transition count and a functional of that latent vector. The present result keeps the directing vector explicit and links the local transition rate to its Gini–Simpson diversity.

A separate 2008 paper by Eryilmaz derives distributions of the total number of runs, longest runs, and shortest runs for exchangeable multi-state trials. Its accessible abstract does not state the latent-diversity covariance or correlation. Because its complete text was not available from the open sources checked, it remains a residual literature risk rather than negative evidence.

## Limitations
The explicit variance and correlation are for the symmetric Dirichlet family. No claim is made that the transition rate is an optimal estimator of latent diversity, nor that the same closed correlation holds for asymmetric Dirichlet parameters, infinite-color directing measures, or nonexchangeable reinforced sequences. The full body of the 2008 Statistics & Probability Letters paper on exchangeable multi-state runs was not available in the sources inspected.

## References
S. Eryilmaz, “Run Statistics Defined on the Multicolor URN Model,” *Journal of Applied Probability* 45 (2008), 1007–1023. DOI: 10.1239/jap/1231340230.

S. Eryilmaz, “Distribution of runs in a sequence of exchangeable multi-state trials,” *Statistics & Probability Letters* 78 (2008), 1505–1513. DOI: 10.1016/j.spl.2008.01.002.
