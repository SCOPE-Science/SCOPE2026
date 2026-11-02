# A dispersal-only extinction threshold in a two-patch Beverton–Holt population

## Finding
Consider a source patch and a sink patch with separate Beverton–Holt recruitment functions and a constant total survival fraction after dispersal. Negative density-dependent *emigration* from the source can produce stable extinction and a stable positive equilibrium simultaneously, despite the absence of an intrinsic Allee effect in either local recruitment law.

More precisely, for the class defined below, let \(M_0\) be its linearization at extinction. If \(\rho(M_0)<1\), \(\alpha>1/3\), and
\[
\frac{2cr}{3\sqrt{3\alpha}}>1,
\]
then extinction is locally asymptotically stable, while at least two strictly positive fixed points exist. In particular, the condition \(\rho(M_0)<1\) does *not* imply extinction from every positive initial state, even with strictly increasing and concave Beverton–Holt recruitment in both patches and a fixed, density-independent total fraction \(c\) surviving dispersal.

There is also a fully rational example with **exactly two strictly positive fixed points**. One is a hyperbolic saddle and the other is locally asymptotically stable; extinction is locally asymptotically stable too. These three hyperbolic equilibria persist for all sufficiently small perturbations of the model's five parameters, so coexistence of the two stable outcomes is not confined to a single parameter tuple.

## Assumptions and scope
For any \(x,y\geq0\), parameters \(0<c,q,\alpha<1\), \(r>1\), and \(0<s<1\), consider the discrete-time system \((x_{t+1},y_{t+1})=F(x_t,y_t)\), where
\[
F(x,y)=\begin{pmatrix}
c(1-p(x))\,r\,x/(1+x)+cq\,s\,y/(1+y)\\
cp(x)\,r\,x/(1+x)+c(1-q)\,s\,y/(1+y)
\end{pmatrix},\qquad p(x)=\frac{\alpha}{(1+x)^2}.
\]
The underlying recruitment maps are \(f_1(x)=rx/(1+x)\) and \(f_2(y)=sy/(1+y)\), which are strictly increasing and strictly concave for positive arguments; the first is a local source and the second a local sink. The dispersal-survival matrix is
\[
D(x)=c\begin{pmatrix}1-p(x)&q\\p(x)&1-q\end{pmatrix}.
\]
All four entries of \(D(x)\) are positive and each column sums to the same constant \(c<1\) for every density. Thus the mechanism depends on the source's density-dependent *allocation* of dispersers, not changing aggregate mortality.

Write \(a=cr(1-\alpha)\), \(b=cqs\), \(d=cr\alpha\), \(e=c(1-q)s\). The extinction Jacobian is \(M_0=\bigl(\begin{smallmatrix}a&b\\d&e\end{smallmatrix}\bigr)\), a strictly positive matrix with \(0<e<1\).

## Proof
### A general sufficient condition for two positive fixed points
Set
\[
H(x)=\frac{crx}{1+x}\left(1-\frac{\alpha}{(1+x)^2}\right),\quad
K(x)=\frac{cr\alpha x}{(1+x)^3},\quad B=cqs,\quad E=c(1-q)s.
\]
The fixed point equations are \(x=H(x)+B\,y/(1+y)\) and \(y=K(x)+E\,y/(1+y)\). For each \(x\geq0\), the strictly increasing function \(y\mapsto y-Ey/(1+y)\) maps \([0,\infty)\) bijectively onto itself, since its derivative is \(1-E/(1+y)^2>0\). It therefore gives a unique continuous solution \(y=y(x)\) of the sink equation; \(y(0)=0\) and \(y(x)>0\) for \(x>0\). Moreover, \(K(x)\) is bounded and \(y(x)-E y(x)/(1+y(x))\geq y(x)-E\), so \(y(x)\) is uniformly bounded.

Define \(G(x)=H(x)+B\,y(x)/(1+y(x))-x\). We have \(G(0)=0\). Differentiating the sink equation at zero gives \(y'(0)=d/(1-e)\), hence
\[
G'(0)=a+\frac{bd}{1-e}-1<0.
\]
The inequality follows from \(\rho(M_0)<1\): since \(M_0\) is positive and \(e<1\), the inequality \((1-a)(1-e)>bd\) is equivalent to \(\rho(M_0)<1\). For \(\alpha>1/3\), the positive number \(x_*=\sqrt{3\alpha}-1\) is the maximizer of
\[
\frac{H(x)}x=cr\left(\frac1{1+x}-\frac{\alpha}{(1+x)^3}\right),
\]
and its maximum equals \(2cr/(3\sqrt{3\alpha})\). Thus the displayed hypothesis implies \(G(x_*)>H(x_*)-x_*>0\). On the other hand, \(H\) and \(y\) are bounded, so \(G(x)\to-\infty\) as \(x\to\infty\). By the intermediate-value theorem, \(G\) vanishes at least once in \((0,x_*)\) and once in \((x_*,\infty)\). Both yield strictly positive equilibria. Since \(\rho(M_0)<1\), the extinction equilibrium is locally asymptotically stable by linearization.

### An exact rational bistability witness
Choose
\[
(c,r,s,q,\alpha)=\left(\frac45,6,\frac14,\frac15,\frac9{10}\right).
\]
Now \(H(x)=12x(10x^2+20x+1)/[25(1+x)^3]\), \(K(x)=108x/[25(1+x)^3]\), \(B=1/25\), and \(E=4/25\). The extinction matrix is
\[
M_0=\frac1{25}\begin{pmatrix}12&1\\108&4\end{pmatrix},\qquad
\sigma(M_0)=\left\{\frac{8\pm2\sqrt{31}}{25}\right\}\subset(-1,1).
\]
For \(x>0\) write \(v=y/(1+y)\), which must belong to \((0,1)\). The source equation forces
\[
v=V(x)=\frac{xR(x)}{(1+x)^3},\qquad R(x)=25x^3-45x^2-165x+13.
\]
The sink equation becomes \(V(x)-(1-V(x))[K(x)+(4/25)V(x)]=0\). After multiplication by its strictly positive denominator, this is precisely
\[
\frac{xP(x)}{5(1+x)^6}=0,\qquad
P(x)=500x^7-1695x^6-4854x^5+11995x^4+17364x^3-9165x^2-178x+33.
\]
Descartes' rule gives at most four positive roots of \(P\), counted with multiplicity. Direct exact rational substitution gives opposite signs at the endpoints of each of the four intervals
\[
\left(\frac{53}{1000},\frac{54}{1000}\right),\quad
\left(\frac{43}{100},\frac{44}{100}\right),\quad
\left(\frac{16}{5},\frac{13}{4}\right),\quad
\left(\frac{18}{5},\frac{361}{100}\right).
\]
These intervals therefore contain all four positive roots, one simple root each. Since \(R'(x)=15(x+1)(5x-11)\), \(R\) is decreasing below \(11/5\) and increasing above it. In the first interval, \(0<R(x)<13\) and \(0<V(x)<(54/1000)13<1\). In the fourth, \(0<R(x)<8\) and \(0<V(x)<(361/100)8/(23/5)^3<1\). In the second and third intervals \(R(x)<0\), so \(V(x)<0\) and these algebraic roots are biologically inadmissible. Thus **exactly two strictly positive equilibria exist**. Each is recovered uniquely from its admissible root by \(y=V(x)/(1-V(x))\).

The Jacobian at a positive equilibrium is
\[
J(x,y)=\begin{pmatrix}H'(x)&(1/25)(1+y)^{-2}\\K'(x)&(4/25)(1+y)^{-2}\end{pmatrix},
\]
where
\[
H'(x)=\frac{12/25+(456/25)x+(24/5)x^2}{(1+x)^4},\qquad
K'(x)=\frac{108(1-2x)}{25(1+x)^4}.
\]
Throughout the first root interval, \(H'(x)>1\), \(K'(x)>0\), and the other two Jacobian entries are positive. Thus its Perron eigenvalue exceeds one. The other eigenvalue lies in \((-1,1)\): it is at most the lower diagonal entry \(<4/25\) and is bounded below by \(-\sqrt{J_{12}J_{21}}>-1\) since \(J_{12}J_{21}<(1/25)(108/25)<1\). This equilibrium is a hyperbolic saddle. Throughout the fourth interval, \(H'(x)+(1/25)<1\) and \(|K'(x)|+4/25<1\); consequently \(\lVert J\rVert_\infty<1\), and that equilibrium is locally asymptotically stable. The extinction equilibrium is also locally asymptotically stable, as the displayed eigenvalues show.

The three fixed points are hyperbolic, and all coefficients depend smoothly on the five parameters. The implicit-function theorem therefore continues these equilibria and their stability types to a neighborhood of the displayed parameter tuple, preserving the strict model restrictions. In particular, there is an open family of examples with stable extinction and stable positive coexistence.

## Verification
The companion `verify.py` runs with the Python 3 standard library and uses exact rational arithmetic. It reconstructs the polynomial elimination identity, checks all four disjoint root brackets, verifies the \(0<V<1\) feasibility tests and the Jacobian inequalities, and verifies the extinction matrix entries. The proof of existence of roots uses the intermediate-value theorem and Descartes' rule; numerical root approximations are neither assumed nor needed.

## Relationship to prior work
McGrane-Corrigan, Mason and de Andrade Moral (2024) study the broad density-dependent dispersal and survival-cost setting, prove a positive equilibrium under a supercritical extinction Jacobian, and show numerically that the extinction-stability dichotomy can fail through periodic dynamics even below threshold. Their results do not entail this explicit **subcritical pair of positive fixed points**, nor classify their two stability types for concave recruitment with constant column survival. Their Theorem 5.1 addresses \(\rho(M_0)>1\), the opposite spectral regime. Their full-text Example 3 uses Ricker and Hassell-1 local dynamics and a periodic orbit, not an exact two-equilibrium classification.

Constant-dispersal Beverton–Holt results, including the dichotomy summarized in that paper's Section 3, require fixed migration proportions and hence do not imply this density-responsive construction. Previously reported multiple-attractor models involving a *local* strong Allee effect likewise have different recruitment assumptions. The general qualitative mechanism of density-dependent dispersal changing stability is established in older work; neither that principle nor the classical spectral linearization test is claimed as new.

## Limitations
The general inequality is a sufficient condition for at least two positive fixed points, not a necessary condition or complete global bifurcation classification. The exact assertion of precisely two positive equilibria and their stability is for the displayed rational parameter choice and nearby parameter values, not all parameter values. No global basin-separator theorem, global attractor classification, or environmental stochasticity claim is made. The full text of certain older specialist dispersal papers was not accessible; specialized prior-art equivalence remains a possibility. The work has not undergone independent external audit.

## References
1. B. McGrane-Corrigan, O. Mason, R. de Andrade Moral, *A density-dependent metapopulation model: Extinction, persistence and source-sink dynamics*, arXiv:2405.04505v1, first posted May 7, 2024. https://arxiv.org/abs/2405.04505
2. J. A. L. Silva, M. L. de Castro, D. A. R. Justo, *Stability in a metapopulation model with density-dependent dispersal*, Bulletin of Mathematical Biology 63 (2001), 485–505. https://doi.org/10.1006/bulm.2000.0221
3. D. Knipl, G. Röst, *Spatially heterogeneous populations with mixed negative and positive local density dependence*, Theoretical Population Biology 106 (2016), 6–15. https://discovery.ucl.ac.uk/id/eprint/1474382/
4. I. B. S. de Godoy, B. McGrane-Corrigan, O. Mason, R. de Andrade Moral, W. A. C. Godoy, *Plant-host shift, spatial persistence, and the viability of an invasive insect population*, Ecological Modelling 475 (2023), 110172. https://doi.org/10.1016/j.ecolmodel.2022.110172
