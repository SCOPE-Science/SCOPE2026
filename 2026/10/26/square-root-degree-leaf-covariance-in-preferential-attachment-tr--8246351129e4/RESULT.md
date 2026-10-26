# Square-root degree–leaf covariance in preferential-attachment trees

## Finding
For every integer \(n\ge2\), let \(D_n\) denote the degree of the initially distinguished vertex of a standard preferential-attachment tree and let \(L_n\) denote its total number of degree-one vertices. Set
\[q_n=\frac{1}{4^{n-2}}\binom{2n-4}{n-2},\qquad C_n=\operatorname{Cov}(D_n,L_n).\]
Then \(C_2=C_3=0\), and for all \(n\ge2\),
\[\boxed{C_{n+1}-C_n=\frac{(n-3)q_n}{3(n-1)}+\frac{(2n-3)q_n^2}{3(n-1)^2}.}\]
Consequently \(C_n>0\) for all \(n\ge4\), and its exact finite value is the sum of the displayed increments for indices \(2,\ldots,n-1\). The scaling and relative influence satisfy
\[\boxed{\lim_{n\to\infty}\frac{C_n}{\sqrt n}=\frac{2}{3\sqrt\pi},\qquad\lim_{n\to\infty}\frac{C_n}{\mathbb E D_n}=\frac13.}\]
The sharp Pearson-correlation asymptotic is
\[\boxed{\operatorname{Corr}(D_n,L_n)\sim\frac{2}{\sqrt{\pi(2-4/\pi)}}\,n^{-1/2}.}\]
Thus the covariance diverges at the same order as the expected founding-node degree, although the linear correlation tends to zero.

## Assumptions and scope
Start at time \(2\) from a single undirected edge joining labeled vertices \(1\) and \(2\). At each integer step \(n\ge2\), introduce vertex \(n+1\) and connect it by one edge to an existing vertex chosen with conditional probability proportional to its current ordinary (undirected) degree. The total degree of a tree of order \(n\) is \(2(n-1)\). The marked vertex is specifically the original vertex \(1\); its degree is \(D_n\), and \(L_n\) counts *all* degree-one vertices, including the marked vertex when applicable. All expectations and covariances are unconditional over the attachment process. The identities concern every integer \(n\ge2\). The correlation formula concerns \(n\ge4\), when both variances are positive.

## Proof
Write \(a_n=1/[2(n-1)]\) and let \(I_n\) indicate that vertex \(n+1\) attaches to the marked vertex. Let \(J_n\) indicate that it attaches to any degree-one vertex. With \(\mathcal F_n\) the existing tree history, define \(Q_n=\mathbf1\{D_n=1\}\). Then
\[D_{n+1}=D_n+I_n,\quad L_{n+1}=L_n+1-J_n,\]
\[\mathbb E[I_n\mid\mathcal F_n]=a_nD_n,\quad\mathbb E[J_n\mid\mathcal F_n]=a_nL_n,\quad \mathbb E[I_nJ_n\mid\mathcal F_n]=a_nQ_n.\]
The last equation accounts for the only possible overlap between attachment to the marked vertex and attachment to a leaf. Since \(Q_{n+1}=Q_n(1-I_n)\), its mean \(q_n=\mathbb E Q_n\) obeys \(q_2=1\) and
\[q_{n+1}=(1-a_n)q_n.\]
Iteration yields the central-binomial expression in the statement. Let \(d_n=\mathbb E D_n\) and \(\ell_n=\mathbb E L_n\). Taking conditional means gives
\[d_{n+1}=(1+a_n)d_n,\quad \ell_{n+1}=(1-a_n)\ell_n+1,\quad(d_2,\ell_2)=(1,2).\]
Direct substitution/induction using the recurrence for \(q_n\) gives the exact marginal identities
\[d_n=(2n-3)q_n,\qquad\ell_n=\frac{2(n-1)}3+\frac43q_n.\]
The leaf mean above is independently known in the literature and is used here only as an input to the new mixed covariance.

Expanding the product of the two updated statistics and taking conditional expectation gives
\[\begin{aligned}
\mathbb E[D_{n+1}L_{n+1}\mid\mathcal F_n]
&=D_nL_n+D_n-D_n(a_nL_n)+a_nD_n(L_n+1)-a_nQ_n\\
&=D_nL_n+(1+a_n)D_n-a_nQ_n.
\end{aligned}\]
Subtract \(d_{n+1}\ell_{n+1}\), with \(d_{n+1}=(1+a_n)d_n\) and \(\ell_{n+1}=(1-a_n)\ell_n+1\), to obtain the *exact* covariance recursion
\[C_{n+1}=C_n+a_n^2d_n\ell_n-a_nq_n.\]
Substituting the displayed marginal identities yields the boxed increment. At \(n=2\) its two terms cancel, so \(C_3=C_2=0\). For every \(n\ge3\), the first term is nonnegative, the second strictly positive, proving strict positivity for all \(n\ge4\) without requiring a numerical computation.

By Stirling's formula, \(q_n\sim1/\sqrt{\pi n}\). The increment therefore equals
\[C_{n+1}-C_n=\frac{1+o(1)}{3\sqrt{\pi n}};\]
the second term is \(O(n^{-2})\). Comparing the sum with the integral of \(t^{-1/2}\) establishes \(C_n\sim(2/(3\sqrt\pi))\sqrt n\), while \(d_n=(2n-3)q_n\sim(2/\sqrt\pi)\sqrt n\), proving the ratio \(1/3\).

For completeness, the variances needed for Pearson correlation follow by direct conditioning. Because \(I_n\) is conditionally Bernoulli with mean \(a_nD_n\),
\[\mathbb E[D_{n+1}^2]=(1+2a_n)\mathbb E[D_n^2]+a_nd_n.\]
Induction from \(n=2\) gives \(\mathbb E[D_n^2]=2(n-1)-d_n\), and hence
\[\operatorname{Var}(D_n)=\left(2-\frac4\pi\right)n+o(n).\]
The conditional variance of the leaf update is \(a_nL_n(1-a_nL_n)\). The law of total variance therefore yields, with \(v_n=\operatorname{Var}(L_n)\),
\[v_{n+1}=(1-2a_n)v_n+a_n\ell_n(1-a_n\ell_n).\]
Since \(a_n\ell_n\to1/3\), multiply the recurrence by \(n-1\), telescope, and compare with \(\sum_{j\le n}j\) to obtain \(v_n\sim n/9\). Combining the two variance estimates with the covariance asymptotic proves the stated Pearson-correlation formula.

## Verification
The standalone `verify.py` checks all degree-proportional attachment histories from order \(2\) through order \(9\) with exact rational probabilities. At each order it compares the enumerated means, marked-leaf probability, second moments, and covariance with the formulas above. It also checks the exact finite sum through order \(249\), plus numerical scaling diagnostics at orders \(1000\), \(10000\), and \(100000\). Run from the folder containing this document using `python verify.py`. The exact enumerations are finite consistency tests; the full-order assertions are proved by the conditional-expectation identities.

## Relationship to prior work
Janson's 2017 account of linear preferential-attachment trees gives the general split-tree representation, not a root-degree versus total-leaf covariance. Contat and collaborators' 2023 study of the oldest vertices uses their degree martingales for root inference, without the total-leaf mixed statistic. The 2002 work of Krapivsky and Redner analyzes global degree-count fluctuations, including counts of degree-one vertices, but not covariance against the degree of an age-marked founding vertex. Hartle and Krapivsky (2026) derive the exact marginal leaf mean, variance, and certain *global-count* covariances; those marginal/global results are not claimed here. The positive covariance derived here also differs from the bounded root-degree/leaf-count covariance for uniform recursive trees, and from marked-degree/leaf relationships in plane-increasing trees governed by a different attachment rule. No claim of exhaustive historical priority is made.

## Limitations
The formulas apply to the precisely specified single-edge-seeded, degree-proportional preferential-attachment tree, not to multi-edge preferential attachment, arbitrary affine attachment kernels, or arbitrary marked birth times. The correlation asymptotic does not assert independence or a joint central limit theorem. The exact degree-count marginals in the proof have classical antecedents; the claimed contribution is their marked-versus-global mixed covariance, its exact sign, and its sharp growth and correlation constants. Historical-priority uncertainties remain concerning broad moment-recursion treatments of preferential attachment and equivalent specializations of other initial-condition models. No independent audit has been performed.

## References
1. S. Janson, *Random recursive trees and preferential attachment trees are random split trees*, arXiv:1706.05487v1 (public 2017-06-17); Combinatorics, Probability and Computing 28 (2019), 81–99, DOI:10.1017/S0963548318000226.
2. A. Contat, N. Curien, P. Lacroix, E. Lasalle, and V. Rivoirard, *Eve, Adam and the Preferential Attachment Tree*, arXiv:2303.04752 (first posted 2023; inspected v2).
3. P. L. Krapivsky and S. Redner, *Finiteness and Fluctuations in Growing Networks*, arXiv:cond-mat/0207107v2, J. Phys. A 35 (2002), 9517–9534.
4. H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021v1 (2026), specifically Sec. IV.1 on leaf-count moments and Sec. IV.2 on other global-count covariances.
