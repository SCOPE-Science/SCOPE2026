# Quantitative positivity of every cumulant for three-edge exponential matchings

## Finding
Let \(m,n\geq3\) be arbitrary integers. Give every edge of the complete bipartite graph \(K_{m,n}\) an independent rate-one exponential cost. Let \(C_{3,m,n}\) be the minimum total cost of a set of three pairwise vertex-disjoint edges. Define its cumulants by
\[
\log\mathbb E e^{tC_{3,m,n}}=\sum_{p\geq1}\frac{\kappa_p(C_{3,m,n})}{p!}t^p
\quad\text{near }t=0.
\]
**Theorem.** Every cumulant is strictly positive. In fact, simultaneously for all integers \(m,n\geq3\) and \(p\geq1\),
\[
\boxed{\kappa_p(C_{3,m,n})\geq\frac{(p-1)!}{2}\left(\frac3{mn}\right)^p>0.}
\]
This resolves the three-edge case, for all rectangular dimensions and every cumulant order, of Conjecture 10 in Wästlund's cited work.

## Assumptions and scope
Costs are mutually independent with density \(e^{-x}\) on \(x\geq0\). An admissible matching consists of exactly three edges with no shared endpoint. The integers \(m,n\) are at least three, and \(p\) is any positive integer. No limit in either graph dimension or cumulant order is taken. The moment generating function is analytic at the origin; all comparisons below concern its Taylor coefficients there.

## Proof
**1. The exact rational moment generating function.** Put \(F(t)=\mathbb E e^{tC_{3,m,n}}\). Equations (36)–(38) of Wästlund's preprint give, after normalizing at the origin, the rational identity
\[
 F(t)=\frac{(P_J(t)-t^2)/P_J(0)}{Q(t)/Q(0)},
\]
where
\[
\begin{aligned}
P_J(t)&=(mn-2t)((m-1)n-t)(m(n-1)-t),\\
Q(t)&=(mn-3t)((m-1)n-2t)(m(n-1)-2t)\\
 &\qquad\cdot((m-2)n-t)((m-1)(n-1)-t)(m(n-2)-t).
\end{aligned}
\]
The normalizing constants ensure \(F(0)=1\). The identity is also verified independently at \(m=n=3\) against the explicit distributional transform in equation (10) of the source; its linear coefficient agrees with the standard exact mean at every tested rectangular dimension.

Write \(\widetilde J(t)=(P_J(t)/P_J(0))/(Q(t)/Q(0))\) and \(h(t)=t^2/P_J(t)\). Then
\[
\log F(t)=\log\widetilde J(t)+\log(1-h(t)).
\]
Set \(R=mn/3\) and \(z=t/R\). Direct factorization gives
\[
 h(Rz)=\frac{\delta z^2}{(1-\alpha z)(1-\beta z)(1-\gamma z)},
 \qquad\delta=\frac{1}{9(m-1)(n-1)},\quad
 \alpha=\frac23,\quad\beta=\frac{m}{3(m-1)},\quad
 \gamma=\frac{n}{3(n-1)}.
\]
For \(m,n\geq3\), one has \(0<\delta\leq1/36\), \(\beta,\gamma\leq1/2\). Thus the series of \(h(Rz)\), which has nonnegative coefficients, is coefficientwise bounded by the universal series
\[
 h_*(z)=\frac{z^2}{36(1-2z/3)(1-z/2)^2}
       =\sum_{p\geq2}a_pz^p,
 \qquad a_p=\left(\frac23\right)^p-\frac{p+3}{3\,2^p}.
\]
Here \(h_*(1)=1/3\) and all \(a_p\) are nonnegative.

**2. A bound on the logarithmic defect valid at every order.** For all \(p\geq2\),
\[
 p a_p\leq\frac13.
\]
Indeed, the exact values \(p a_p\) for \(p=2,3,4,5,6,7\) are respectively \(1/18,5/36,67/324,235/972,1909/7776,31829/139968\), each below \(1/3\). For \(p\geq8\),
\[
 p a_p\leq p(2/3)^p\leq8(2/3)^8=2048/6561<1/3,
\]
because \(p(2/3)^p\) decreases for integer \(p\geq3\).

Expand \(H_*(z)=-\log(1-h_*(z))=\sum_{p\geq2}b_pz^p\), and put \(c_p=pb_p\), with \(c_0=c_1=0\). From \(zH_*'(z)=zh_*'(z)+h_*(z)zH_*'(z)\) one obtains the exact recurrence
\[
 c_p=p a_p+\sum_{k=2}^{p-2}a_kc_{p-k}.
\]
Induction, \(\sum_{k\geq2}a_k=h_*(1)=1/3\), and the previous estimate imply
\[
 0\leq c_p\leq\frac13+\frac12\cdot\frac13=\frac12
 \qquad(p\geq2).
\]
Because \(h(Rz)\) and \(h_*(z)\) have nonnegative coefficients and the former is coefficientwise bounded by the latter, the identity \(-\log(1-h)=\sum_{j\geq1}h^j/j\) proves coefficientwise domination of their logarithmic defects. Therefore
\[
 [z^p]\bigl\{-\log(1-h(Rz))\bigr\}\leq\frac{1}{2p}
 \qquad(p\geq2),
\]
while the first-degree coefficient of this defect is zero.

**3. A unit coefficient margin in the comparison function.** The six poles of \(\widetilde J\), before possible cancellations, are
\[
 \frac{mn}{3},\quad\frac{(m-1)n}{2},\quad
 \frac{m(n-1)}2,\quad(m-2)n,\quad
 (m-1)(n-1),\quad m(n-2),
\]
and its three zeros are \(mn/2,(m-1)n,m(n-1)\). Pair respectively the zeros \(mn/2,(m-1)n,m(n-1)\) with the smaller-or-equal poles \((m-1)n/2,(m-2)n,m(n-2)\). Each paired factor makes a nonnegative contribution to every Taylor coefficient of \(\log\widetilde J(Rz)\). The unpaired pole at \(R=mn/3\) alone contributes \(1/p\) to the coefficient of \(z^p\), while the two other unpaired poles contribute nonnegatively. Consequently
\[
 [z^p]\log\widetilde J(Rz)\geq\frac1p
 \qquad(p\geq1).
\]
Combining this with Step 2 gives \([z^p]\log F(Rz)\geq1/(2p)\) for \(p\geq2\). At \(p=1\) the stronger lower bound is \(1\). Since \([z^p]\log F(Rz)=\kappa_p R^p/p!\), it follows for every integer \(p\geq1\) that
\[
\kappa_p\geq\frac{(p-1)!}{2R^p}
  =\frac{(p-1)!}{2}\left(\frac3{mn}\right)^p>0.
\]
This concludes the proof.

## Verification
The accompanying standard-library Python checker runs exact polynomial and rational arithmetic. It checks the numerator identity and the known expectation formula for \(3\leq m,n\leq16\), independently cross-multiplies the \(3\times3\) transform from the source, and evaluates the coefficient inequalities for \(3\leq m,n\leq12\) through order \(25\). It also checks the majorant through order \(300\). The code reports 11,500 passing exact assertions. Infinite-dimensional and all-order conclusions depend on the coefficient-induction argument, not finite checks. Reproduce with `python3 matching_cumulants_verify.py`.

## Relationship to prior work
Wästlund, *Moment generating functions in combinatorial optimization: Bipartite matching* (arXiv:2602.07563v1, 7 February 2026), states in Conjecture 10 that all cumulants of minimum-cost matchings are positive. Its Proposition 15 proves a zero-free disk for the three-edge generating function, but zero-freeness alone does not imply positivity of every Taylor coefficient of the logarithm. Its explicit polynomial comparison supplies the exact input used in Step 1. Alm and Sorkin (2002) previously treated exact distributions for small matching cardinalities, but a full-text priority comparison was unavailable. The present contribution is a dimension-uniform all-order positivity proof and quantitative lower bound, not the rational transform itself.

## Limitations
The theorem assumes independent unit-rate exponential edge costs and exactly three selected edges. It neither extends to four or more edges nor proves Wästlund's general cumulant conjecture. The displayed lower bound is universal but not asserted optimal. Priority is conditional on the inspected and accessible literature; full-text access to Alm and Sorkin (2002) was unavailable. No independent scientific audit has been performed.

## References
1. Johan Wästlund, *Moment generating functions in combinatorial optimization: Bipartite matching*, arXiv:2602.07563v1 (first posted 7 February 2026), §§2.4, 4.2–4.3, equations (10), (36)–(38), Conjecture 10 and Proposition 15. https://arxiv.org/pdf/2602.07563
2. Sven Erick Alm and Gregory B. Sorkin, *Exact Expectations and Distributions for the Random Assignment Problem*, Combinatorics, Probability and Computing **11** (2002), 217–248, doi:10.1017/S0963548302005114.
3. Gilles Mordant, *A central limit theorem for the random assignment problem*, arXiv:2608.05123 (2026); deals with a large-square perfect-matching limit, rather than all finite cumulants of the three-edge exponential model.
