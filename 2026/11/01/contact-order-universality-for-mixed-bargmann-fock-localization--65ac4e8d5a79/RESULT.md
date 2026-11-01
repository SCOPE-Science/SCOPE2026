# Contact-order universality for mixed Bargmann–Fock localization traces

## Finding
Let two compact strictly convex planar bodies meet only at the origin on opposite sides of a common supporting line. Suppose their normal boundary deficits at the contact point have the same real order \(p>1\), with positive coefficients \(a\) and \(b\). Expanding both bodies by \(R\), and then separating them by any fixed nonnegative normal gap \(g\), produces the universal mixed Toeplitz trace law
\[
\lim_{R\to\infty}R^{-(1-1/p)}\operatorname{Tr}(T_{A_R}T_{B_R})
=\frac{2p}{(p+1)\pi^{3/2}(a+b)^{1/p}}
\int_0^\infty v^{1+1/p}e^{-(g+v)^2}\,dv.
\]
The limit is strictly positive and convergence is locally uniform in \(g\geq0\). It therefore holds when a sequence of nonnegative gaps converges to a finite gap.

At exact tangency the constant simplifies to
\[
\frac{p\,\Gamma(1+1/(2p))}{(p+1)\pi^{3/2}(a+b)^{1/p}}.
\]
For the infinite complex Ginibre determinantal process, the covariance of the particle counts in the two disjoint windows is the negative of this mixed trace. In particular, the magnitude of this covariance grows with the nonintegral contact exponent \(1-1/p\).

## Assumptions and scope
Identify \(\mathbb R^2\) with \(\mathbb C\), writing points as \((x,y)\). Let \(K,L\subset\mathbb R^2\) be compact strictly convex bodies with nonempty interiors and \(C^1\) boundaries near the origin, with
\[
K\subset\{x\leq0\},\qquad L\subset\{x\geq0\},
\qquad K\cap\{x=0\}=L\cap\{x=0\}=\{(0,0)\}.
\]
For each vertical coordinate in the corresponding projection, define the right support section
\(f_K(y)=\sup\{x:(x,y)\in K\}\) and the left support section
\(f_L(y)=\inf\{x:(x,y)\in L\}\). Assume the two-sided asymptotics, as \(y\to0\),
\[
f_K(y)=-a|y|^p+o(|y|^p),\qquad
f_L(y)=b|y|^p+o(|y|^p),
\]
for fixed real \(p>1\) and fixed \(a,b>0\). No global curvature lower bound is assumed. For \(R>0\) and \(g\geq0\), define
\(A_R=RK\) and \(B_R=RL+(g,0)\), using ordinary Euclidean dilation and translation.

Take the analytic Bargmann–Fock space \(\mathcal F^2\) with measure
\(d\mu(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\), reproducing kernel
\(K(z,w)=e^{z\overline w}\), and orthogonal projection \(P\). For bounded measurable sets \(E\), use
\(T_E=P M_{\mathbf1_E}|_{\mathcal F^2}\). All mixed products in this statement are trace-class. The normalization is fixed by \(\operatorname{Tr}T_E=|E|/\pi\).

## Proof
**1. Exact Gaussian trace identity.** The reproducing-kernel integral and the trace-class property of compactly supported positive symbols give
\[
\operatorname{Tr}(T_E T_F)
=\frac1{\pi^2}\int_E\!\int_F e^{-|z-w|^2}\,dA(w)\,dA(z).
\]
Indeed, the factor \(e^{z\overline w+w\overline z-|z|^2-|w|^2}\) is precisely \(e^{-|z-w|^2}\). The identity holds without assuming the Toeplitz operators commute.

**2. Normal and tangential coordinates.** Write the two variables as \(z=(x_1,y_1)\), \(w=(x_2,y_2)\). For each allowed vertical slice use the inward distances
\[
s=R f_K(y_1/R)-x_1\geq0,\qquad
 t=x_2-g-Rf_L(y_2/R)\geq0.
\]
Their admissible upper bounds are the corresponding horizontal slice widths; the widths, at fixed rescaled tangential position, tend to infinity with \(R\). Set
\[
y_1=R^{1-1/p}u,\qquad y_2=y_1+h.
\]
The Jacobian from \((x_1,y_1,x_2,y_2)\) to \((s,u,t,h)\) is \(R^{1-1/p}\). The horizontal separation is
\[
x_2-x_1=g+R\bigl[f_L(y_2/R)-f_K(y_1/R)\bigr]+s+t.
\]
For every fixed \(u,h,s,t\), the assumptions imply
\[
R\bigl[f_L(y_2/R)-f_K(y_1/R)\bigr]
\longrightarrow (a+b)|u|^p.
\]
The slice-width restrictions eventually disappear for every fixed finite \(s,t\).

**3. Integrable domination and the exact limit.** Compactness, strict convexity and the unique contact with the supporting line imply that there is \(c>0\) such that
\[-f_K(y)\geq c|y|^p\]
throughout its vertical projection. Near zero this follows from the assumed positive coefficient; away from zero it follows from the uniqueness of the support point and compactness. Consequently, whenever the transformed integrand is nonzero, its Gaussian factor is bounded by
\[
\exp\bigl(-h^2-[c|u|^p+s+t]^2\bigr),
\]
independently of \(R\) and of \(g\geq0\). This is integrable over
\((u,h,s,t)\in\mathbb R^2\times[0,\infty)^2\): integrating over \((s,t)\) gives a single nonnegative variable with weight equal to that variable, while the remaining exponential decays superpolynomially in \(|u|\). Dominated convergence yields
\[
\lim_{R\to\infty} R^{-(1-1/p)}\operatorname{Tr}(T_{A_R}T_{B_R})
=\frac1{\pi^{3/2}}\int_{\mathbb R}\!\int_0^\infty
v\,e^{-[g+(a+b)|u|^p+v]^2}\,dv\,du.
\]
The integration in \(h\) contributes \(\sqrt\pi\). The domination also applies to the supremum of the pointwise difference over \(g\) in a fixed compact interval, proving locally uniform convergence.

**4. One-dimensional evaluation.** Set \(A=a+b\) and \(q=A|u|^p+v\). At fixed \(q\geq0\), the allowed tangential interval is
\(|u|\leq(q/A)^{1/p}\). Its elementary integral is
\[
\int_{-(q/A)^{1/p}}^{(q/A)^{1/p}}(q-A|u|^p)\,du
=\frac{2p}{p+1}A^{-1/p}q^{1+1/p}.
\]
Substitution proves the asserted coefficient and positivity. At \(g=0\), the substitution \(t=q^2\) gives the stated gamma value. The local uniform result extends the limit to any sequence of gaps tending to a finite nonnegative value.

**5. Count covariance.** The regions have disjoint interiors for every \(g\geq0\). The Ginibre two-point determinant therefore gives
\(\operatorname{Cov}(N(A_R),N(B_R))=-\operatorname{Tr}(T_{A_R}T_{B_R})\). Thus the exact same contact law holds for the negative counting covariance.

## Verification
A standalone standard-library checker, `contact_checker.py`, evaluates the exact finite-size Gaussian integral for the contact-order family
\[
K_p=\{(x,y):|x+1|^2+|y|^p\leq1\},\quad
L_p=\{(x,y):|x-1|^2+|y|^p\leq1\}.
\]
These strictly convex bodies have \(a=b=1/2\). The checker uses analytic integration over inward normal distances and two-dimensional composite Simpson quadrature in the rescaled tangential variables. It passes 55 checks over contact orders \(p=2,4,6\), gaps \(g=0,0.6\), and scales \(R=20,80,320\); the largest-scale normalized values are within one percent of the predicted limits. The checker also tests the exact gamma-integral constant for the zero-gap case. Computations test finite examples only; the proof for all real \(p>1\), all admissible bodies and the infinite limit is the dominated-convergence argument above.

For the equal-radius disk contact \(p=2\) and \(g=0\), the constant is
\(2\Gamma(5/4)/(3\pi^{3/2})\approx0.108518808227677\).
The profile is strictly decreasing in \(g\), with the large-gap asymptotic (after the \(R\to\infty\) limit)
\[
\frac{2p\,\Gamma(2+1/p)}{(p+1)\pi^{3/2}(a+b)^{1/p}}
\frac{e^{-g^2}}{(2g)^{2+1/p}},\qquad g\to\infty.
\]
The two limits must not be interchanged without further estimates.

## Relationship to prior work
The analytic Fock Toeplitz framework and its invariant-symbol algebras are developed in González-Flores, Dupont-García, López-Martínez and Hérnandez-Zamora (2023). That work concerns algebraic decompositions under circle actions; the present contact indicators are not invariant and the invariant-algebra statements do not determine their mixed cross trace. Abreu, Pereira, Romero and Torquato (2016/2017) establish perimeter-order hyperuniform variance bounds for Weyl–Heisenberg ensembles, including the Ginibre case, and Matsui, Katori and Shirai (2020/2021) evaluate single-ball variances. Neither inspected analysis supplies the lower-order mixed trace caused by an isolated tangency of two independently dilated windows. The classical proximity/Derjaguin principle suggests curvature-controlled short-range interactions, but no inspected source supplies the stated all-orders normal-contact formula with its precise Gaussian profile. The claim is a specific normalized theorem, not a claim of novelty for the Gaussian kernel identity or for Laplace's method.

## Limitations
The two bodies must be compact and strictly convex, have unique opposing support points, and share a positive contact-order coefficient on both sides. The result concerns one-dimensional complex Gaussian Fock space and nonnegative normal gaps converging to a finite limit; it does not address arbitrary intersections, multiple contact points, tangential shifts growing with \(R\), large-gap uniformity, or higher complex dimension. The numerical checker does not certify the infinite theorem. Historical priority has not been independently audited; a more general heat-content or proximity theorem may imply this law under equivalent geometric assumptions.

## References
- C. González-Flores, L. A. Dupont-García, R. R. López-Martínez, and F. G. Hérnandez-Zamora, *Toeplitz Operators on Fock Space over \(\mathbb C^n\) with Invariant Symbols under the Action of the Unit Circle*, Axioms 12 (2023), 1080, DOI: `10.3390/axioms12121080`; public 2023-11-25. Primary MSC 30H20 as listed by the journal.
- L. D. Abreu, J. M. Pereira, J. L. Romero, and S. Torquato, *The Weyl–Heisenberg ensemble: hyperuniformity and higher Landau levels*, arXiv:`1612.00359`, first public 2016-12-01; J. Stat. Mech. (2017), 043103.
- T. Matsui, M. Katori, and T. Shirai, *Local number variances and hyperuniformity of the Heisenberg family of determinantal point processes*, arXiv:`2012.10585`, first public 2020-12-19.
