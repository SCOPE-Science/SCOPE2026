# Exact geodesic dispersion and unique area-constrained optimum of flat Möbius bands

## Finding
For every pair of real numbers \(L,w>0\), let \(M_{L,w}\) be the compact flat Möbius band obtained from the Euclidean rectangle \([0,L]\times[-w,w]\) by the identification \((0,y)\sim(L,-y)\). Use its intrinsic length metric \(d\) and normalized area measure. For independent uniform points \(P,Q\in M_{L,w}\), put \(A=4w^2/L^2\). Then
\[
\mathbb E[d(P,Q)^2]=L^2\Phi(A),\qquad
\Phi(A)=
\begin{cases}
\dfrac1{12}+\dfrac A6-\dfrac{A^2}{36},&0<A\le1,\\[4pt]
\dfrac{3A^2+24A-6\log A-11}{72A},&A>1.
\end{cases}
\]
The function \(\Phi\) is three times, but not four times, continuously differentiable at \(A=1\): the right-hand formula minus the polynomial continuation of the left-hand formula equals \((A-1)^4/48+O((A-1)^5)\) as \(A\downarrow1\).

At prescribed area \(\mathcal A=2wL>0\), the normalized squared geodesic dispersion has a unique global minimizer, with
\[
\frac{\mathbb E[d(P,Q)^2]}{\mathcal A}
=\frac{\Phi(A)}{\sqrt A},
\qquad
A=A_*\in(4,5),
\qquad
3A_*^2-24A_*+18\log A_*+21=0.
\]
The numerical values are \(A_*=4.376853931208964\ldots\), \(w/L=\sqrt{A_*}/2=1.046046596859930\ldots\), and minimum normalized dispersion \(0.216380293842592\ldots\). The root described above is the sole root of this equation in \((3,\infty)\); \(A=1\) is also a stationary point of the normalized function but not a minimizer.

## Assumptions and scope
The band is an **abstract compact flat length-metric surface with boundary**. The rectangle's short-edge identification reverses the transverse coordinate; there is no requirement of a smooth isometric embedding into Euclidean three-space. Here \(L\) is the centerline period and \(2w\) is the full width. Distances are shortest intrinsic path lengths, not ambient Euclidean distances. Each of \(P,Q\) is independently distributed according to the area measure divided by \(2wL\). The statements hold for all \(L,w>0\), including the transition \(w=L/2\).

## Proof
**1. The exact geodesic minimum.** The universal covering strip is \(\mathbb R\times[-w,w]\), with deck isometry \(g(x,y)=(x+L,-y)\). Since this strip is Euclidean and convex, the shortest path from one lift of \(P=(x,y)\) to any image \(g^k(Q)\) is the straight segment between their lifts. Its projection is a valid path. Conversely, every path between \(P\) and \(Q\) lifts to a path between such endpoints and cannot be shorter than the Euclidean segment. Therefore
\[
 d(P,Q)^2=\min_{k\in\mathbb Z}\{(x-x'-kL)^2+(y-(-1)^k y')^2\}.
\]
For \(x,x'\in[0,L]\), among even \(k\) the nearest longitudinal displacement is \(U=|x-x'|\), and among odd \(k\) it is \(L-U\). Thus, exactly,
\[
 d(P,Q)^2=\min\{U^2+(y-y')^2,\ (L-U)^2+(y+y')^2\}.
\]

**2. Reduction to one product integral.** The independent rectangle coordinates make \(U\) independent of \(y,y'\); its density is \(2(L-u)/L^2\) on \([0,L]\), while \(y,y'\) are independent uniform random variables on \([-w,w]\). Write \(T=4yy'/L^2\). The squared-distance minimum becomes
\[
 U^2+(y-y')^2-(2LU-L^2-4yy')_+.
\]
Its baseline expectation is \(L^2(1+A)/6\). Conditional on \(T=t\), integrate the positive part against the triangular density: the normalized improvement is exactly
\[
 G(t)=\frac1{L^2}\mathbb E_U[(2LU-L^2-4yy')_+\mid T=t]
 =\begin{cases}
 -\frac13-t,&t<-1,\\[2pt]
 \frac{(1-t)^3}{12},&-1\le t\le1,\\[2pt]
 0,&t>1.
 \end{cases}
\]
Indeed the positivity threshold is \(u_0=L(1+t)/2\). For \(-1\le t\le1\), direct integration yields \(\frac{2}{3L}(L-u_0)^3\); the other two cases correspond to a wholly positive or wholly zero integrand.

The product \(Z=(y/w)(y'/w)\) has density \(-\frac12\log|z|\) on \((-1,1)\), obtained by integrating the two independent uniform densities along the hyperbolas \(uv=z\). Since \(T=AZ\), symmetry yields
\[
 \frac{\mathbb E[(2LU-L^2-4yy')_+]}{L^2}
 =-\frac12\int_0^1\log z\,H(Az)\,dz,
 \quad H(q)=\begin{cases}\frac16+\frac{q^2}2,&0\le q\le1,\\[2pt]q-\frac13,&q>1.\end{cases}
\]
For \(A\le1\), the integral is \(1/12+A^2/36\). For \(A>1\), splitting at \(z=1/A\) gives \((9A^2-12A+6\log A+11)/(72A)\). Subtraction from the baseline proves the two formulas for \(\Phi\), with all endpoint cases included.

**3. Regularity at the phase boundary.** Elementary Taylor expansion of the two displayed elementary expressions at \(A=1\) gives
\[
 \Phi_{>}(A)-\left(\frac1{12}+\frac A6-\frac{A^2}{36}\right)
 =\frac{(A-1)^4}{48}+O((A-1)^5),\qquad A\downarrow1.
\]
Consequently the first three derivatives match there, while the fourth right derivative exceeds the fourth left derivative by \(4!/48=1/2\). This is precisely \(C^3\) but not \(C^4\) regularity.

**4. Fixed-area global optimization.** Because \(2wL=L^2\sqrt A\), minimizing at fixed area is exactly minimizing \(F(A)=\Phi(A)/\sqrt A\) for \(A>0\). Differentiation of the proven closed form gives
\[
 F'(A)=\begin{cases}
 -\dfrac{(A-1)^2}{24A^{3/2}},&0<A<1,\\[5pt]
 \dfrac{h(A)}{144A^{5/2}},&A>1,
 \end{cases}
 \qquad h(A)=3A^2-24A+18\log A+21.
\]
Now \(h(1)=0\), \(h'(A)=6(A-1)(A-3)/A\), and \(h(3)=-24+18\log3<0\). Hence \(h\) decreases strictly on \((1,3)\), increases strictly on \((3,\infty)\), and tends to \(+\infty\); it has exactly one zero \(A_*>3\). The signs of \(F'\) show strict decrease on \((0,A_*)\), apart from its isolated stationary point at \(A=1\), and strict increase on \((A_*,\infty)\). Finally, \(F(A)\to\infty\) at both endpoints \(A\downarrow0\) and \(A\to\infty\). Thus the minimizer is globally unique. The numerical interval \(4<A_*<5\) follows from \(h(4)<0<h(5)\), and the quoted values follow by bisection.

As a comparison, the **untwisted** flat cylinder obtained by identifying \((0,y)\sim(L,y)\) has \(\mathbb E[d_{\mathrm{cyl}}^2]=L^2/12+2w^2/3\), strictly above the Möbius value for every \(L,w>0\). Its fixed-area optimal normalized value is \(\sqrt2/6\), whereas the Möbius optimum is smaller.

## Verification
Run the included standalone file `verify.py` with Python 3 (standard library only). It checks the explicit minimum against eleven deck images for 100,000 independent random configurations, independently integrates the product-density formula by deterministic quadrature over ten aspect ratios, performs six seeded Monte Carlo tests totaling 1,020,000 independent point pairs, and tests the numerical root and nearby fixed-area values. `verification_log.txt` contains the recorded output. Every program assertion passed. Neither numerical integration nor random sampling is used as proof of the all-parameter statements: these follow from the preceding covering-space reduction, exact integral, and derivative-sign argument.

## Relationship to prior work
Tanaka and Hiscock, arXiv:gr-qc/9504021 (first public arXiv posting 1995-04-14), §III.B Eq. (18)–(19), explicitly give the glide-reflection image-distance formulas on a nonorientable flat spacetime. That is a genuine antecedent for the metric quotient, but the work evaluates quantum-field observables on an unbounded Möbius factor, not random-pair intrinsic squared distances on a compact band with boundary, and does not give the area-constrained optimum or the \(C^3\)/non-\(C^4\) threshold. Gálvez and Mira, arXiv:math/0301075 (2003-01-09), study flat immersions and give a distinct example of a flat Möbius strip in §2. Schwartz, arXiv:2308.12641 (initial posting 2023-08-24), studies the *different* problem of minimizing the length-to-width ratio under a smooth, injective, isometric Euclidean-three-space realization.

Related computations of two-point squared geodesic distance on **closed** rectangular Klein bottles, and full geodesic-distance laws on **orientable** finite cylinders, do not determine this compact nonorientable-with-boundary formula or its unique fixed-area optimum. These comparisons are statements of mathematical non-implication, not assertions of exhaustive historical priority.

## Limitations
The result concerns the intrinsic abstract flat quotient; it is **not** an optimum among smoothly embedded physical paper Möbius strips. At the displayed minimizer \(L/(2w)\approx0.478\), which is below the sharp necessary \(\sqrt3\) for a smooth embedded strip proved by Schwartz. The theorem is only about squared intrinsic pair-distance expectation and its fixed-area optimizer; it does not determine the full distance distribution, other moments, or extrinsic geometry. General geodesic image methods predate this calculation, so independent historical-priority checking remains important. No independent mathematical audit is claimed.

## References
1. T. Tanaka and W. A. Hiscock, *Massive scalar field in multiply connected flat spacetimes*, arXiv:gr-qc/9504021, first posted 1995-04-14, §III.B, Eq. (18)–(19). https://arxiv.org/abs/gr-qc/9504021
2. J. A. Gálvez and P. Mira, *Isometric immersions of R² into R⁴ and perturbation of Hopf tori*, arXiv:math/0301075, first posted 2003-01-09, §2. https://arxiv.org/abs/math/0301075
3. R. E. Schwartz, *The Optimal Paper Moebius Band*, arXiv:2308.12641, first posted 2023-08-24; Annals of Mathematics 201 (2025), 291–305. https://arxiv.org/abs/2308.12641
