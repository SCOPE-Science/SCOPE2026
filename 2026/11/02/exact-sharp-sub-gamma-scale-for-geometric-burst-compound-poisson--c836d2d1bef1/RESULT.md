# Exact sharp sub-gamma scale for geometric-burst compound Poisson laws

## Finding
For any \(q\in(0,1)\) and \(\lambda>0\), take independent \(N\sim\operatorname{Pois}(\lambda)\) and \(J_1,J_2,\ldots\) with \(\Pr(J=k)=(1-q)q^{k-1}\) for integers \(k\ge1\). Define \(X=\sum_{j=1}^{N}J_j-\lambda/(1-q)\) and its variance \(V=\lambda(1+q)/(1-q)^2\). Then the **smallest** right-sided sub-gamma scale with variance proxy fixed at \(V\) is
\[
c_*(q)=\frac{1+4q+q^2}{3(1-q^2)},\qquad
\log\mathbb E e^{tX}\le\frac{Vt^2}{2(1-c_*(q)t)}\quad(0\le t<1/c_*(q)).
\]
The canonical second-order equilibrium variable \(R\) of \(J\) satisfies the stronger statement \(R\le_{\mathrm{cx}} E\), where \(E\) is exponential with mean \(c_*(q)\). This convex-order bound holds despite the failure of the usual NBUE mean-residual-life property for \(R\).

## Assumptions and scope
The intensity is finite and positive; the geometric parameter is strictly between zero and one. The compound Poisson sum is centered using its exact mean, and the Gaussian variance proxy is fixed at the exact variance rather than enlarged. Convex order \(R\le_{\mathrm{cx}} E\) means \(\mathbb E\varphi(R)\le\mathbb E\varphi(E)\) for every convex function whose expectations exist; because means coincide, it is equivalent to the stop-loss inequalities \(\mathbb E(R-x)_+\le\mathbb E(E-x)_+\) at all \(x\ge0\).

## Proof
**1. Canonical remainder.** For a centered compound Poisson sum, the canonical factorization [1, Theorem 2.1 and Section 6] is
\[
\log\mathbb E e^{tX}=\frac{Vt^2}{2}\mathbb E e^{tR},\quad
f_R(x)=\frac{2\mathbb E(J-x)_+}{\mathbb EJ^2},\quad x\ge0.
\]
Here \(\mathbb EJ^2=(1+q)/(1-q)^2\). Write \(x=m+u\), with integer \(m\ge0\) and \(0\le u<1\). A direct geometric sum yields
\[
f_R(m+u)=\frac{2(1-q)}{1+q}\,q^m[1-(1-q)u].
\]
Consequently \(R=M+U\) for independent \(\Pr(M=m)=(1-q)q^m\) and \(U\in(0,1)\) with density \(2[1-(1-q)u]/(1+q)\). In particular
\[
c:=\mathbb ER=\frac{\mathbb EJ^3}{3\mathbb EJ^2}
=\frac{1+4q+q^2}{3(1-q^2)}.
\]
**2. Stop-loss inequality within one unit cell.** Put \(S(u)=\Pr(R>u)\) and \(F(u)=\mathbb E(R-u)_+\). For \(0\le u\le1\), direct integration gives
\[
S(u)=1-\frac{2(1-q)}{1+q}u+\frac{(1-q)^2}{1+q}u^2,
\]
\[
F(u)=c-u+\frac{1-q}{1+q}u^2-\frac{(1-q)^2}{3(1+q)}u^3.
\]
Thus
\[
cS(u)-F(u)=\frac{(1-q)^2u(u-1)((1+q)u-1)}{3(1+q)^2}.
\]
The expression is positive on \(0<u<1/(1+q)\) and negative on \(1/(1+q)<u<1\). For \(0\le u\le1\), let \(H(u)=\log(F(u)/c)+u/c\), well-defined since \(q>0\). Then \(H'(u)=[F(u)-cS(u)]/[cF(u)]\): it first decreases and then increases, so its maximum on the unit cell occurs at an endpoint. We have \(H(0)=0\) and \(H(1)=\log q+1/c\).

To check \(H(1)<0\), set \(z=(1-q)/(1+q)\in(0,1)\). Elementary algebra gives \(1/c=2z/(1-z^2/3)\), while
\[
-\log q=2\operatorname{artanh}z
=2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1}
>\frac{2z}{1-z^2/3},
\]
since \(3^j\ge2j+1\) for every nonnegative integer \(j\), with strict inequality for \(j\ge2\). Therefore \(F(u)\le c e^{-u/c}\) for the whole unit cell.

**3. Extension to every threshold.** Geometric memorylessness implies \(F(m+u)=q^mF(u)\), including \(u=1\) by continuity. Since \(q<e^{-1/c}\),
\[
F(m+u)=q^mF(u)\le q^m c e^{-u/c}\le c e^{-(m+u)/c},\quad m\ge0.
\]
The right side is the stop-loss transform of an exponential variable of mean \(c\). As the two means equal \(c\), this proves convex order, including all convex tests by the standard stop-loss characterization. Also \(cS(u)<F(u)\) for \(u\in(1/(1+q),1)\), so \(\mathbb E(R-u\mid R>u)=F(u)/S(u)>c\); hence \(R\) fails NBUE despite the convex-order comparison.

**4. Sub-gamma optimality.** Convex order with the exponential law gives \(\mathbb E e^{tR}\le(1-ct)^{-1}\) for \(0\le t<1/c\), hence the announced MGF bound by the exact canonical factorization. Its smallest possible \(c\) is at least \(\kappa_3(X)/(3V)\), by comparing cubic Taylor coefficients as \(t\downarrow0\) with the variance proxy fixed. The Poisson cumulant formula gives \(\kappa_3(X)=\lambda\mathbb EJ^3\), hence \(\kappa_3(X)/(3V)=\mathbb EJ^3/(3\mathbb EJ^2)=c\). Both directions match; no unproved minimization remains. In particular the usual sub-gamma Chernoff consequence is \(\Pr(X\ge\sqrt{2Vs}+cs)\le e^{-s}\) for every \(s\ge0\).

## Verification
The companion standard Python/SymPy checker independently reconstructs the distribution and moments, verifies the exact polynomial stop-loss factorization, the continuity condition \(F(1)=qc\), and performs numerical threshold checks at several geometric parameters. Such finite calculations corroborate the displayed identities; the inequalities for all parameters and all thresholds follow from the analytical argument above.

## Relationship to prior work
Chen [1] establishes the canonical remainder factorization, general optimal-scale variational formula and M-class criterion, and treats gamma and bounded two-point jump laws. The general framework is prior work; the exact geometric-jump convex-order certificate, its NBUE failure and the resulting closed sharp scale are the findings here. The classical treatment of residual lifetimes of compound geometric distributions by Willmot [2] is relevant but concerns geometric summation of other risks rather than a Poisson sum of geometric jumps. The general M-class and exponential stop-loss methods themselves are not claimed as new.

## Limitations
This is an exact theorem only for positive integer geometric jumps and finite Poisson intensity. The variance proxy is fixed, and the scale is one-sided (right-tail). The result does not optimize a freely varying variance proxy and does not assert an optimal Chernoff bound among all possible concentration inequalities. Prior actuarial reliability results could contain overlapping techniques or hidden specializations; independent historical-priority review has not been performed.

## References
[1] Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first public posting 2026-09-02), https://arxiv.org/html/2610.00032v1 , esp. Theorems 2.1 and 4.1 and Section 6.

[2] G. E. Willmot, *On higher-order properties of compound geometric distributions*, Journal of Applied Probability **39** (2002), 324–340, DOI 10.1239/jap/1025131429; bibliographic record and abstract consulted. The complete article was not inspected.
