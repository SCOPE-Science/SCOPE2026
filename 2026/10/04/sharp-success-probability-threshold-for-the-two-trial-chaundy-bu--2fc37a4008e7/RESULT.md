# Sharp success-probability threshold for the two-trial Chaundy–Bullard step
## Finding
Let \(k\ge1\) and \(m\ge0\) be integers. For \(0\le p\le1\), define
\[
\Delta_{k,m}(p)=\Pr\{\operatorname{Bin}(2k+m,p)\ge k\}-\Pr\{\operatorname{Bin}(2k+m+2,p)\ge k+1\}.
\]
Set
\[
p^*_{k,m}=\frac{k+m+1}{2k+m+1}.
\]
Then \(\Delta_{k,m}(0)=\Delta_{k,m}(p^*_{k,m})=\Delta_{k,m}(1)=0\), while
\[
\Delta_{k,m}(p)>0\quad\text{for }0<p<p^*_{k,m},
\qquad
\Delta_{k,m}(p)<0\quad\text{for }p^*_{k,m}<p<1.
\]
Thus \(p^*_{k,m}\) is the exact interior success-probability threshold for the two-trial step. In particular, the sufficient range \(p\le1/2\) obtained by specializing Theorem 3.3 of Fokkink--Papavassiliou--Pelekis to block size two is strictly nonsharp, by the exact amount
\[
p^*_{k,m}-\frac12=\frac{m+1}{2(2k+m+1)}.
\]

## Assumptions and scope
All binomial variables have the displayed integer number of trials and common success probability \(p\). The claim compares one threshold step when two additional Bernoulli trials are appended. It is an exact finite-sample statement for every \(k\ge1\), \(m\ge0\), and \(p\in[0,1]\). It does not assert an analogous closed threshold for block sizes larger than two.

## Proof
Let \(S\sim\operatorname{Bin}(2k+m,p)\) and independently let \(Y\sim\operatorname{Bin}(2,p)\). Then \(S+Y\sim\operatorname{Bin}(2k+m+2,p)\). Conditioning on the only values of \(S\) that can change the event when \(Y\) is added gives
\[
\Pr\{S+Y\ge k+1\}
=\Pr\{S\ge k+1\}+\Pr\{S=k\}\Pr\{Y\ge1\}+\Pr\{S=k-1\}\Pr\{Y=2\}.
\]
Therefore
\[
\Delta_{k,m}(p)
=\Pr\{S=k\}(1-p)^2-\Pr\{S=k-1\}p^2.
\]
For \(0<p<1\), the neighboring binomial masses satisfy
\[
\frac{\Pr\{S=k-1\}}{\Pr\{S=k\}}
=\frac{k}{k+m+1}\frac{1-p}{p}.
\]
Substitution yields the exact factorization
\[
\Delta_{k,m}(p)
=\Pr\{S=k\}(1-p)
\left((1-p)-\frac{k}{k+m+1}p\right).
\]
The first two factors are positive in the open unit interval. The last factor vanishes exactly when
\[
(k+m+1)(1-p)=kp,
\]
which is equivalent to \(p=p^*_{k,m}\), and it changes sign from positive to negative there. Directly at \(p=0\), both tail probabilities are zero; directly at \(p=1\), both are one. This proves the complete sign classification. Finally,
\[
p^*_{k,m}-\frac12
=\frac{2(k+m+1)-(2k+m+1)}{2(2k+m+1)}
=\frac{m+1}{2(2k+m+1)}.
\]

## Verification
The accompanying standard-library script `verify.py` evaluates both binomial tails with exact rational arithmetic, checks the displayed factorization for \(1\le k\le8\) and \(0\le m\le5\), checks equality at the exact threshold, checks strict signs on both sides, and verifies the closed form for the excess above \(1/2\). It returns `VERIFY_OK`. These finite checks are stress tests; the proof above supplies the all-parameter theorem.

## Relationship to prior work
Fokkink, Papavassiliou and Pelekis study exactly these successive binomial-tail comparisons. Their Theorem 3.3 proves, for general block size \(n\), the sufficient range \(0\le p\le1/n\). With \(n=2\), that gives \(p\le1/2\). Their proof analyzes the derivative of a tail-gap function but does not state the exact two-trial threshold above \(1/2\). Their Corollary 3.2 identifies the \(m=0\), \(p=1/n\) case with the Chaundy--Bullard inequality.

Older work of Anderson--Samuels and Jogdeo--Samuels concerns related monotonicity, Poisson comparisons, and binomial medians. The accessible descriptions and the later source do not state the present all-\(k,m\) if-and-only-if two-trial threshold. The original Anderson--Samuels article and the Chaundy--Bullard paper could not be fully inspected through the available public-text route during this verification, so an unlocated equivalent older formulation remains a residual literature risk.

## Limitations
The theorem is specific to adding two Bernoulli trials. It does not classify the sharp success-probability region for arbitrary block size \(n\ge3\). The originality assessment is literature-bounded rather than a proof of historical uniqueness; the inaccessible older full texts noted above remain a residual risk.

## References
1. R. Fokkink, S. Papavassiliou, C. Pelekis, “Some inequalities on Binomial and Poisson probabilities,” arXiv:2011.11795v1, first public 2020-11-23, especially Corollary 3.2 and Theorem 3.3.
2. T. W. Anderson, S. M. Samuels, “Some inequalities among binomial and Poisson probabilities,” Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, Vol. I, 1967, pp. 1--12.
3. K. Jogdeo, S. M. Samuels, “Monotone Convergence of Binomial Probabilities and a Generalization of Ramanujan's Equation,” Annals of Mathematical Statistics 39 (1968), 1191--1195, doi:10.1214/aoms/1177698243.
