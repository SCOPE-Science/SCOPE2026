# Sharp Simes size under pairwise independence for three uniform p-values

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let \(P_1,P_2,P_3\) be pairwise independent random variables, each exactly uniform on \([0,1]\). For \(0\le \alpha\le 1\), let
\[
S_\alpha=\left\{\min_{1\le k\le 3}\frac{3P_{(k)}}{k}\le \alpha\right\}
\]
be the rejection event of the three-hypothesis Simes global-null test. Then the exact worst-case size over all such pairwise-independent triples is
\[
\sup \Pr(S_\alpha)=
\begin{cases}
\displaystyle \alpha+\frac{4\alpha^2}{9},&0\le \alpha\le \frac35,\\[6pt]
\displaystyle \frac{4\alpha}{3}-\frac{\alpha^2}{9},&\frac35\le \alpha\le \frac34,\\[6pt]
\displaystyle 2\alpha-\alpha^2,&\frac34\le \alpha\le 1.
\end{cases}
\]
Every bound is attained by an explicit continuous pairwise-independent uniform construction.

Consequently, pairwise independence alone does not make the Simes test level \(\alpha\): the worst-case size is strictly larger than \(\alpha\) for every \(0<\alpha<1\). Under the global null, the three-hypothesis Benjamini-Hochberg procedure rejects at least one hypothesis exactly on \(S_\alpha\), and its false discovery rate therefore has the same sharp worst-case envelope.

For example, at \(\alpha=0.05\) the exact worst-case size/FDR is
\[
0.05+\frac{4(0.05)^2}{9}=0.051111\ldots.
\]

## Proof of the upper bound

Put \(r=\alpha/3\), and partition \([0,1]\) into
\[
A=(0,r],\qquad B=(r,2r],\qquad C=(2r,3r],\qquad D=(3r,1].
\]
Endpoints are immaterial. Each coordinate label has probabilities
\[
p_A=p_B=p_C=r,\qquad p_D=1-3r.
\]
Because the \(P_i\) are pairwise independent, their category labels are also pairwise independent.

Let \(N_A,N_B,N_C,N_D\) be the category counts among the three coordinates. The Simes test rejects exactly when
\[
N_A\ge 1,\qquad\text{or}\qquad N_A+N_B\ge 2,\qquad\text{or}\qquad N_D=0.
\]
For a count vector \(n=(n_A,n_B,n_C,n_D)\), define
\[
\phi_{jj}(n)=\frac{n_j(n_j-1)}{6},\qquad
\phi_{jk}(n)=\frac{n_jn_k}{6}\quad(j<k).
\]
Pairwise independence gives
\[
\mathbb E\,\phi_{jk}(N)=p_jp_k\qquad (j\le k).
\]

Order the ten pairs as
\[
AA,AB,AC,AD,BB,BC,BD,CC,CD,DD.
\]
For each of the following coefficient vectors \(z^{(m)}\), direct inspection of the 20 nonnegative integer count vectors summing to three gives the pointwise inequality
\[
\mathbf 1_{S_\alpha}(n)\le \sum_{j\le k}z^{(m)}_{jk}\phi_{jk}(n):
\]
\[
\begin{array}{c|rrrrrrrrrr}
&AA&AB&AC&AD&BB&BC&BD&CC&CD&DD\\ \hline
z^{(1)}&1&3&3&3&3&0&0&3&0&0\\
z^{(2)}&1&2&3&3&2&1&1&2&0&0\\
z^{(3)}&1&2&2&4&1&2&2&1&0&0
\end{array}
\]
(the exact finite check is reproduced in `artifacts/check_certificates.py`). Taking expectations gives, respectively,
\[
\Pr(S_\alpha)\le 13r^2+3r(1-3r)=3r+4r^2,
\]
\[
\Pr(S_\alpha)\le 11r^2+4r(1-3r)=4r-r^2,
\]
and
\[
\Pr(S_\alpha)\le 9r^2+6r(1-3r)=6r-9r^2.
\]
Their lower envelope changes at \(r=1/5\) and \(r=1/4\), i.e. at \(\alpha=3/5\) and \(\alpha=3/4\). Converting back to \(\alpha=3r\) yields the stated piecewise upper bound.

## Sharpness constructions

It remains to attain each branch. First choose an exchangeable category triple in \(\{A,B,C,D\}^3\) by choosing a category-count multiset with the probability shown below and then uniformly permuting its three labels among the coordinates. Unlisted multisets have probability zero.

### Region I: \(0\le r\le 1/5\)

\[
\begin{array}{c|c}
\text{multiset}&\text{probability}\\ \hline
DDD&1-9r+23r^2\\
CDD&3r(1-4r)\\
BDD&3r(1-5r)\\
BCC&3r^2\\
BBD&3r^2\\
ADD&3r(1-5r)\\
ACD&6r^2\\
ABD&6r^2\\
AAA&r^2
\end{array}
\]
Its Simes rejection probability is \(3r+4r^2\).

### Region II: \(1/5\le r\le 1/4\)

\[
\begin{array}{c|c}
\text{multiset}&\text{probability}\\ \hline
DDD&1-7r+13r^2\\
CDD&3r(1-4r)\\
BCC&3r^2\\
BBD&3r^2\\
ACD&6r^2\\
ABD&6r(1-4r)\\
AAB&3r(5r-1)\\
AAA&r(1-4r)
\end{array}
\]
Its Simes rejection probability is \(4r-r^2\).

### Region III: \(1/4\le r\le 1/3\)

\[
\begin{array}{c|c}
\text{multiset}&\text{probability}\\ \hline
DDD&(1-3r)^2\\
BCC&3r^2\\
BBD&3r(1-3r)\\
ACD&6r(1-3r)\\
ABB&3r(4r-1)\\
AAC&3r(4r-1)\\
AAB&3r(1-3r)
\end{array}
\]
Its Simes rejection probability is \(6r-9r^2\).

All displayed masses are nonnegative on their stated ranges and sum to one. Moreover, in every region their count moments satisfy
\[
\mathbb E\,\phi_{jk}(N)=p_jp_k\qquad(j\le k),
\]
so the category labels are pairwise independent with marginal probabilities \((r,r,r,1-3r)\). These identities are checked exactly, as polynomial identities in \(r\), in the verification artifact.

Finally, conditional on the three category labels, draw each \(P_i\) independently and uniformly inside its assigned interval. Each \(P_i\) is then uniform on \([0,1]\), and every pair \((P_i,P_j)\) is independent because the two labels are independent and the within-bin draws are conditionally independent. The category-level Simes event is unchanged, completing sharpness.

## Relation to prior literature

Simes (1986) introduced the ordered-p-value test and proved exact level \(\alpha\) under mutual independence. Hommel (1983) studied overall tests under arbitrary dependence and obtained sharp error-probability bounds, while Samuel-Cahn (1996) explicitly discussed anticonservativeness of the Simes procedure under dependence. The present statement addresses a different intermediate regime: all one-dimensional marginals are exactly uniform and every pair of p-values is independent, but the triple need not be mutually independent.

Ramachandra and Natarajan (2023) developed tight probability bounds for pairwise-independent Bernoulli variables, including a closed-form union bound and additional bounds for threshold events. Their linear-programming viewpoint is closely related to the finite certificate used above, but their paper does not state the Simes multiple-testing problem or the three-p-value piecewise envelope given here.

## Limitations

The theorem is for exactly three continuously uniform null p-values. It does not characterize the sharp envelope for four or more p-values, super-uniform but non-uniform null p-values, partial null configurations, or other limited-independence orders. The literature search did not locate an earlier statement of this exact pairwise-independent Simes envelope, but equivalent formulations may exist in older Bonferroni inequalities, probability-bounds, copula, or multiple-testing literature under different terminology. The full text of Hommel (1983) was not accessible through the inspected source; its abstract and later descriptions were checked, leaving a residual coverage risk concerning older arbitrary-dependence formulations.

## Reproducibility

`artifacts/check_certificates.py` uses only the Python standard library and exact rational arithmetic. It checks all 20 occupancy types for each upper-bound certificate and verifies normalization, all ten pair-category laws, and the rejection polynomial for each sharpness construction. `artifacts/verification_output.txt` records the successful output.

## References

- Simes, R. J. (1986). *An improved Bonferroni procedure for multiple tests of significance*. Biometrika 73(3), 751-754. https://doi.org/10.1093/biomet/73.3.751
- Hommel, G. (1983). *Tests of the Overall Hypothesis for Arbitrary Dependence Structures*. Biometrical Journal 25(5), 423-430. https://doi.org/10.1002/bimj.19830250502
- Samuel-Cahn, E. (1996). *Is the Simes Improved Bonferroni Procedure Conservative?* Biometrika 83(4), 928-933. https://www.jstor.org/stable/2337297
- Benjamini, Y. and Hochberg, Y. (1995). *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*. Journal of the Royal Statistical Society, Series B 57(1), 289-300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x
- Ramachandra, A. K. and Natarajan, K. (2023). *Tight Probability Bounds with Pairwise Independence*. SIAM Journal on Discrete Mathematics 37(2), 516-555. https://doi.org/10.1137/21M1408294
