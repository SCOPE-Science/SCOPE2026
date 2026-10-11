# Logarithmic suppression conditionality in a semi-greedy non-quasi-greedy Markushevich basis
## Finding
Fix \(\theta>0\), and let \(X_\theta\) be the quasi-Banach sequence space constructed by Berná with quasi-norm
\[
\|x\|_\theta=\|x\|_1+\theta H(x).
\]
For a finite set \(A\subset\mathbb N\), let \(P_A\) be the canonical coordinate projection, and for every integer \(m\ge1\) define the suppression conditionality constant
\[
k_m(\theta)=\sup\left\{\frac{\|P_Ax\|_\theta}{\|x\|_\theta}:x\in X_\theta\setminus\{0\},\ A\subset\mathbb N\text{ finite},\ |A|\le m\right\}.
\]
Then, for every integer \(m\ge1\),
\[
\max\left\{1,\frac{1+\theta\log m}{2}\right\}
\le k_m(\theta)
\le 1+\theta\left(\log m+\frac1e\right).
\]
Consequently, for every fixed \(\theta>0\),
\[
k_m(\theta)\asymp_\theta \log(m+1).
\]
Thus Berná's semi-greedy but non-quasi-greedy Markushevich basis has logarithmic suppression conditionality, rather than faster polynomial or unrestricted growth.

## Assumptions and scope
Berná defines, for \(t>0\) and a scalar \(z\),
\[
h_t(z)=z\log\max\{|z|,t\},
\]
and for \(x=(x_n)\in\ell_1\),
\[
S(x)=\sum_n x_n,\qquad
F_t(x)=\sum_n h_t(x_n)-h_t(S(x)),\qquad
H(x)=\sup_{t>0}|F_t(x)|.
\]
The space \(X_\theta\) is the \(\|\cdot\|_\theta\)-closure of \(c_{00}\). All logarithms are natural. The proof below works over both the real and complex scalar fields. The claim concerns the original quasi-norm \(\|\cdot\|_\theta\), not an arbitrary equivalent \(p\)-norm.

## Proof
For the lower bound, Berná proves that whenever \(A,B\subset\mathbb N\) are disjoint and \(|A|=|B|=m\),
\[
\|\mathbf 1_A\|_\theta=m(1+\theta\log m),\qquad
\|\mathbf 1_A-\mathbf 1_B\|_\theta=2m.
\]
With \(x=\mathbf 1_A-\mathbf 1_B\), one has \(P_Ax=\mathbf 1_A\), hence
\[
k_m(\theta)\ge \frac{1+\theta\log m}{2}.
\]
Also \(k_m(\theta)\ge1\), since any nonzero coordinate vector is fixed by a one-coordinate projection.

For the upper bound, fix a finite \(A\) with \(1\le |A|=k\le m\), put \(y=P_Ax\), and write \(L=\|y\|_1\). If \(L=0\) there is nothing to prove. By the homogeneity of \(H\), it suffices to estimate \(H(y)\) after normalizing \(L=1\). Write \(r_j=|y_j|\) on the support of \(y\), so \(\sum_j r_j=1\), and put \(u=|S(y)|\le1\).

For \(t\ge1\), every logarithmic factor equals \(\log t\), so the linear terms cancel and \(F_t(y)=0\). Suppose \(0<t<1\). Since every \(r_j\le1\),
\[
\left|\sum_j y_j\log\max\{r_j,t\}\right|
\le \sum_j r_j\bigl(-\log\max\{r_j,t\}\bigr)
\le \sum_j r_j\log\frac1{r_j}
\le \log k.
\]
The last inequality is the entropy bound for a probability vector supported on at most \(k\) points, with the convention \(0\log 0=0\). For the correction term, if \(u\ge t\), then
\[
u|\log u|\le \frac1e,
\]
while if \(u<t\), then
\[
u|\log t|\le t|\log t|\le \frac1e.
\]
Therefore \(|F_t(y)|\le \log k+1/e\) for every \(t>0\), and by homogeneity
\[
H(y)\le \|y\|_1\left(\log k+\frac1e\right).
\]
Consequently,
\[
\|P_Ax\|_\theta
\le \left[1+\theta\left(\log m+\frac1e\right)\right]\|P_Ax\|_1
\le \left[1+\theta\left(\log m+\frac1e\right)\right]\|x\|_\theta.
\]
Taking the supremum over \(x\ne0\) and over \(|A|\le m\) proves the upper bound. The two inequalities imply the stated logarithmic order.

## Verification
The lower estimate uses the exact identities in equations (5.1) and (5.2) of arXiv:2610.05052v1. The upper estimate is independent of finite experimentation: it uses only the defining formula for \(F_t\), the homogeneity of \(H\), the elementary entropy inequality \(\sum_j r_j\log(1/r_j)\le\log k\), and the scalar bound \(s|\log s|\le1/e\) on \((0,1]\). The argument covers every finite coordinate set and every vector in \(X_\theta\).

## Relationship to prior work
Berná proves that the canonical Markushevich basis is semi-greedy but not quasi-greedy, and proves the lower estimate \(\|P_A\|\ge(1+\theta\log m)/2\) for the initial coordinate sets of every ordering. The paper does not formulate suppression conditionality constants and does not give an upper bound over all coordinate sets; a full-text search of the source finds no occurrence of “conditionality” or \(k_m\). The new entropy estimate supplies that missing global upper bound and therefore identifies the exact logarithmic growth order.

Classical work on quasi-greedy bases in Banach spaces gives \(k_m=O(\log m)\), with logarithmic-order examples. Those theorems do not imply the present statement because Berná's basis is explicitly not quasi-greedy and its ambient space is nonlocally convex. The result therefore shows that logarithmic suppression conditionality by itself does not distinguish this new semi-greedy counterexample from the classical quasi-greedy scale.

## Limitations
The bounds leave a factor-of-two gap in the leading logarithmic coefficient: the result determines the growth order, not the exact asymptotic constant. It concerns Berná's original family of quasi-norms \(\|\cdot\|_\theta\); no claim is made that the same explicit constants survive the equivalent \(p\)-renormings from the source. No converse characterization of semi-greediness or quasi-greediness is asserted.

## References
1. P. M. Berná, *A semi-greedy Markushevich basis which is not quasi-greedy*, arXiv:2610.05052v1, 2026.
2. F. Albiac, J. L. Ansorena, and P. Wojtaszczyk, *Conditional quasi-greedy bases in non-superreflexive Banach spaces*, arXiv:1702.06326, 2017.
3. G. Garrigós and P. Wojtaszczyk, *Conditional quasi-greedy bases in Hilbert and Banach spaces*, arXiv:1301.4844, 2013.
4. F. Albiac, J. L. Ansorena, M. Berasategui, and P. M. Berná, *When Greedy Approximation Breaks: Counterexamples in Quasi-Banach Spaces*, arXiv:2510.13693, 2025.
