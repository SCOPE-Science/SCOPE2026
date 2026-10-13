# Exact negative covariance between two-sample runs and Cramér–von Mises discrepancy
## Finding
Let two independent samples of sizes \(m,n\ge 1\) come from the same continuous distribution, and put \(N=m+n\). After pooling and sorting the observations, write \(A_j\) for the number of first-sample labels among the first \(j\) pooled ranks and define the centered label bridge
\[
B_j=N A_j-mj,\qquad 1\le j\le N-1.
\]
Let \(R\) be the number of Wald–Wolfowitz runs in the pooled label word, and let
\[
T=\frac{mn}{N}\int (F_m-G_n)^2\,dH_N,
\qquad H_N=\frac{mF_m+nG_n}{N},
\]
be the classical two-sample Cramér–von Mises discrepancy. Then
\[
T=\frac{1}{mnN^2}\sum_{j=1}^{N-1}B_j^2
\]
and the exact null covariance is
\[
\operatorname{Cov}(R,T)=-\frac{2mn-N}{3N^2}.
\]
Equivalently,
\[
\operatorname{Cov}\!\left(R,\sum_{j=1}^{N-1}B_j^2\right)
=-\frac{mn(2mn-N)}{3}.
\]
The covariance is zero for \(m=n=1\) and is strictly negative for every \(N\ge3\). If \(m/N\to\lambda\in(0,1)\), then
\[
\operatorname{Cov}(R,T)\longrightarrow -\frac{2\lambda(1-\lambda)}{3}.
\]

## Assumptions and scope
Continuity of the common null distribution is used only to make the pooled ranks tie-free. Conditional on the pooled order statistics, the sample-label word is therefore uniform over all binary words with exactly \(m\) first-sample labels and \(n\) second-sample labels. The result is finite-sample and distribution-free under that null. It does not claim a formula under unequal distributions or in the presence of ties.

## Proof
At a pooled rank \(j\),
\[
F_m-G_n=\frac{A_j}{m}-\frac{j-A_j}{n}=rac{B_j}{mn}.
\]
The pooled empirical distribution \(H_N\) has jumps \(1/N\), and the difference vanishes after rank \(N\). Hence
\[
T=\frac{mn}{N}\frac1N\sum_{j=1}^{N-1}\frac{B_j^2}{m^2n^2}
=\frac{1}{mnN^2}\sum_{j=1}^{N-1}B_j^2.
\]
Write
\[
S=\sum_{j=1}^{N-1}B_j^2,
\qquad
R=1+\sum_{i=1}^{N-1}I_i,
\]
where \(I_i\) indicates a label change across pooled ranks \(i\) and \(i+1\). For every edge,
\[
\mathbb P(I_i=1)=\frac{2mn}{N(N-1)}=:p.
\]
Unconditionally \(A_j\) is hypergeometric with parameters \((N,m,j)\), so
\[
\mathbb E[B_j^2]=\frac{mn\,j(N-j)}{N-1}
\]
and therefore
\[
\mathbb E S=\frac{mnN(N+1)}6.
\]

For \(N\ge4\), condition on \(I_i=1\). The two distinguished positions contain one label of each type, with the two orientations equally likely, while the remaining \(N-2\) positions form a uniform word with \(m-1\) and \(n-1\) labels. Thus, for \(j<i\),
\[
\mathbb E[B_j\mid I_i=1]=\frac{j(m-n)}{N-2},
\qquad
\operatorname{Var}(B_j\mid I_i=1)=
\frac{N^2j(N-2-j)(m-1)(n-1)}{(N-2)^2(N-3)}.
\]
For \(j=i\),
\[
\mathbb E[B_i\mid I_i=1]=\frac{(2i-N)(m-n)}{2(N-2)},
\]
\[
\operatorname{Var}(B_i\mid I_i=1)=
\frac{N^2(i-1)(N-i-1)(m-1)(n-1)}{(N-2)^2(N-3)}+\frac{N^2}{4}.
\]
For \(j>i\),
\[
\mathbb E[B_j\mid I_i=1]=-rac{(N-j)(m-n)}{N-2},
\qquad
\operatorname{Var}(B_j\mid I_i=1)=
\frac{N^2(j-2)(N-j)(m-1)(n-1)}{(N-2)^2(N-3)}.
\]
Adding variance plus squared mean, first over \(j\) and then over the distinguished edge \(i\), gives the polynomial identity
\[
\sum_{i=1}^{N-1}\mathbb E[S\mid I_i=1]
=\frac{N(N-1)}6\bigl((N-1)mn+N\bigr).
\]
Consequently,
\[
\begin{aligned}
\operatorname{Cov}(R,S)
&=\sum_{i=1}^{N-1}\operatorname{Cov}(I_i,S)\\
&=p\left(\sum_{i=1}^{N-1}\mathbb E[S\mid I_i=1]-(N-1)\mathbb ES\right)\\
&=-\frac{mn(2mn-N)}3.
\end{aligned}
\]
Dividing by \(mnN^2\) proves the displayed covariance for \(T\). The cases \(N=2\) and \(N=3\), where the displayed conditional-variance denominators are not used, follow by direct enumeration of the finitely many label words and agree with the same formula.

For \(N\ge3\), the smallest possible product \(mn\) at fixed \(m+n=N\) is \(N-1\). Hence \(2mn-N\ge N-2>0\), proving strict negativity. The proportional-sample limit follows immediately from the exact formula.

## Verification
The standalone checker `verify.py` uses only exact rational arithmetic. It enumerates all \(8{,}166\) binary label words arising from every positive pair \((m,n)\) with \(2\le m+n\le12\), checking the bridge identity, the mean of \(S\), and both covariance formulas. It also checks \(777\) conditional aggregate identities for every positive \((m,n)\) with \(4\le m+n\le40\). The recorded replay output is in `verification_output.txt` and reports that all exact checks passed.

The finite enumerations corroborate but do not replace the all-size proof above. No claim is made for alternatives, tied pooled observations without an explicit tie rule, or statistics using a different Cramér–von Mises normalization.

## Relationship to prior work
Biswas, Mukhopadhyay and Ghosh study the two-sample run statistic and record its exact null distribution, mean and variance; in one dimension their construction coincides with the ordinary Wald–Wolfowitz run statistic. Zhou, Zheng and Zhang treat the classical two-sample Cramér–von Mises statistic as a benchmark omnibus discrepancy in the same two-sample equality problem. Marsh gives an independently indexed two-sample nonparametric-testing source classified primarily under MSC 62G10.

The present statement concerns a mixed finite-sample moment linking the local adjacency statistic \(R\) to the global quadratic empirical-bridge energy \(T\). Targeted searches for the statistic names, the bridge formulation, the displayed covariance, and equivalent mixed-moment language did not locate this identity or a stronger statement implying it. Prior exact formulas involving the run statistic and the Mann–Whitney statistic, or the Mann–Whitney statistic and Cramér–von Mises discrepancy, do not determine this covariance: pairwise covariances through a third statistic do not imply the missing pairwise covariance without an additional projection or conditional-expectation identity.

## Limitations
The originality assessment is necessarily relative to the literature and databases inspected. Older runs, rank-test, or empirical-process literature could encode the same mixed moment under a different normalization or notation. The theorem itself is exact under the stated null; the remaining risk is bibliographic, not a gap in the proof.

## References
1. P. Marsh, “A two-sample nonparametric likelihood ratio test,” *Journal of Nonparametric Statistics* 22 (2010), 1053–1065. DOI: 10.1080/10485250903486078. Published online 2010-01-26; primary AMS classification 62G10.
2. M. Biswas, M. Mukhopadhyay and A. K. Ghosh, “A distribution-free two-sample run test applicable to high-dimensional data,” *Biometrika* 101 (2014), 913–926. DOI: 10.1093/biomet/asu045. Published online 2014-10-23.
3. W.-X. Zhou, C. Zheng and Z. Zhang, “Two-Sample Smooth Tests for the Equality of Distributions,” arXiv:1509.03459, first submitted 2015-09-11; later published in *Bernoulli* 23 (2017), 951–989.
