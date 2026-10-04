# Sharp small-level Simes size for four pairwise-independent p-values
## Finding
Let \(P_1,P_2,P_3,P_4\) be exactly uniform p-values on \([0,1]\), and assume every pair is independent. Write \(P_{(1)}\leq\cdots\leq P_{(4)}\). For the Simes global-null test
\[
E_\alpha=\left\{\min_{1\leq k\leq4}\frac{4P_{(k)}}{k}\leq\alpha}\right\},
\]
the exact worst-case size is
\[
\sup \Pr(E_\alpha)=\alpha+\frac{13}{16}\alpha^2,\qquad 0\leq\alpha\leq\frac25,
\]
where the supremum ranges over all joint laws with exactly uniform marginals and pairwise independence. At \(\alpha=0.05\), this is \(333/6400=0.05203125\).

## Assumptions and scope
The result uses exact marginal uniformity and pairwise independence only; no joint independence, positive dependence, Gaussianity, or exchangeability is assumed in the upper bound. Exchangeability is used only to exhibit an extremizer. The claimed sharp formula is restricted to \(0\leq\alpha\leq2/5\); no formula is asserted above that range.

Partition \([0,1]\) into the five cells
\[
I_1=(0,\alpha/4],\ I_2=(\alpha/4,\alpha/2],\ I_3=(\alpha/2,3\alpha/4],\ I_4=(3\alpha/4,\alpha],\ I_5=(\alpha,1],
\]
with endpoint conventions immaterial. Let \(N_j\) count p-values in \(I_j\). Then rejection is exactly
\[
N_1\geq1\quad\text{or}\quad N_1+N_2\geq2\quad\text{or}\quad N_1+N_2+N_3\geq3\quad\text{or}\quad N_1+N_2+N_3+N_4=4.
\]

## Proof
Pairwise independence fixes all first and second factorial moments of the five counts. For \(j\leq4\), the cell probability is \(p_j=\alpha/4\), while \(p_5=1-\alpha\). Hence
\[
\mathbb E N_j=4p_j,\qquad
\mathbb E[N_j(N_j-1)]=12p_j^2,\qquad
\mathbb E[N_jN_k]=12p_jp_k\quad(j\ne k).
\]

Define the quadratic certificate
\[
\begin{aligned}
B(N)={}&\frac1{12}N_1(N_1-1)+\frac12N_2(N_2-1)+\frac16N_3(N_3-1)+\frac16N_4(N_4-1)\\
&+\frac13(N_1N_2+N_1N_3+N_1N_4+N_1N_5+N_2N_3)+\frac16N_3N_4.
\end{aligned}
\]
For every weak composition \(N_1+\cdots+N_5=4\), \(\mathbf 1_{E_\alpha}\leq B(N)\). This can be checked without optimization. If \(N_1\geq1\), the \(N_1\)-terms already give at least one: for \(N_1=1\), \(N_1(N_2+N_3+N_4+N_5)/3=1\); for \(N_1=2,3,4\), the diagonal plus cross terms give at least \(3/2,3/2,1\), respectively. If \(N_1=0\) and \(N_2\geq2\), the \(N_2\) diagonal term is at least one. If \(N_1=0\), \(N_2\leq1\), and \(N_2+N_3\geq3\), then either \(N_2=0,N_3\geq3\), or \(N_2=1,N_3\geq2\); the displayed \(N_3\) and \(N_2N_3\) terms give at least one. In the remaining rejection case, \(N_5=0\), \(N_2\leq1\), and \(N_2+N_3\leq2\). The possibilities \((N_2,N_3,N_4)\) are \((0,0,4),(0,1,3),(0,2,2),(1,0,3),(1,1,2)\), on which \(B\) equals \(2,3/2,4/3,1,1\), respectively.

Taking expectations and inserting the pairwise moments gives
\[
\Pr(E_\alpha)\leq\mathbb E B(N)=\alpha+\frac{13}{16}\alpha^2.
\]

To attain equality, choose the count vector \((N_1,\ldots,N_5)\) from the following distribution. Entries not listed have probability zero.

| count vector | probability |
| --- | --- |
| \((0,0,0,0,4)\) | \(1-4\alpha+71\alpha^2/16\) |
| \((0,0,0,1,3)\) | \(\alpha-3\alpha^2/2\) |
| \((0,0,1,0,3)\) | \(\alpha-27\alpha^2/16\) |
| \((0,0,3,0,1)\) | \(\alpha^2/16\) |
| \((0,1,0,0,3)\) | \(\alpha-33\alpha^2/16\) |
| \((0,1,1,2,0)\) | \(3\alpha^2/8\) |
| \((0,1,2,0,1)\) | \(3\alpha^2/16\) |
| \((0,2,0,0,2)\) | \(3\alpha^2/8\) |
| \((1,0,0,0,3)\) | \(\alpha-5\alpha^2/2\) |
| \((1,0,0,1,2)\) | \(3\alpha^2/4\) |
| \((1,0,1,0,2)\) | \(3\alpha^2/4\) |
| \((1,1,0,0,2)\) | \(3\alpha^2/4\) |
| \((4,0,0,0,0)\) | \(\alpha^2/16\) |

All weights are nonnegative for \(0\leq\alpha\leq2/5\), and they sum to one. Conditional on the count vector, assign the multiset of cell labels uniformly to the four coordinates. The displayed weights give exactly \(\Pr(C_i=j)=p_j\) and \(\Pr(C_i=j,C_\ell=k)=p_jp_k\) for every distinct \(i,\ell\), including the same-cell factorial cases. Finally, conditional on the labels, draw each \(P_i\) independently and uniformly within its assigned cell. Each \(P_i\) is then exactly uniform on \([0,1]\), and every pair \((P_i,P_\ell)\) is independent.

Every count vector in the support is an equality point of the certificate: \(B(N)=\mathbf 1_{E_\alpha}\). Therefore the rejection probability of this construction equals \(\alpha+13\alpha^2/16\), proving sharpness. The case \(\alpha=0\) is trivial by continuity.

## Verification
The standalone `verify.py` uses exact rational arithmetic. It enumerates all \(70\) five-part weak compositions of four and checks the pointwise certificate; verifies symbolic first and pairwise count moments of the extremizer; proves every listed probability is nonnegative on \([0,2/5]\) by exact quadratic minimization; checks equality of the certificate on every support state; and confirms the objective polynomial and the exact \(\alpha=1/20\) value. Running it prints `VERIFY_OK`.

## Relationship to prior work
Simes-type procedures are exact under independence and are studied under positive, arbitrary, and more recently negative dependence. Chen, Liu, Tan, and Wang analyze Simes as a p-merging rule under arbitrary and structured dependence; Chi, Ramdas, and Wang study Simes and BH under several notions of negative dependence. Neither inspected treatment gives the exact pairwise-independence four-p-value extremum above.

Ramachandra and Natarajan develop linear-programming and moment methods for sharp or improved probability bounds under pairwise independence, principally for Bernoulli sum-tail and union events. Their framework motivates the use of first and pairwise moments, but the Simes rejection region here is a nested multi-threshold event rather than a single sum-tail event.

A closely related published published-finding corpus record gives the exact pairwise-independent Simes size for three uniform p-values. That three-variable formula does not imply the four-variable formula because both the count polytope and the nested Simes thresholds change. Searches for the four-variable formula, its \(13/16\) coefficient, and equivalent global-null BH/Simes wording returned the three-variable record as the closest direct match, not an implication of this claim.

## Limitations
The exact expression is proved only through \(\alpha=2/5\). The explicit extremizer ceases to be a probability distribution beyond that point because the weight \(\alpha-5\alpha^2/2\) becomes negative; this does not establish the sharp formula for larger \(\alpha\). The literature comparison cannot exclude an older result phrased purely as a finite moment or Bonferroni extremal problem rather than as Simes testing. No claim is made about power, false discovery rate under alternatives, more than four hypotheses, or weaker-than-pairwise assumptions.

## References
1. A. Ramachandra and K. Natarajan, *Tight Probability Bounds with Pairwise Independence*, arXiv:2006.00516, first posted 2020-05-31; later SIAM Journal on Discrete Mathematics.
2. Y. Chen, P. Liu, K. S. Tan, and R. Wang, *Trade-off between validity and efficiency of merging p-values under arbitrary dependence*, arXiv:2007.12366, first posted 2020-07-24.
3. Z. Chi, A. Ramdas, and R. Wang, *Multiple testing under negative dependence*, arXiv:2212.09706, first posted 2022-12-19.
4. R. J. Simes, *An improved Bonferroni procedure for multiple tests of significance*, Biometrika 73 (1986), 751–754.
