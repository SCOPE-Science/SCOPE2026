# Sharp equal-sensitivity two-kernel approximation of a quadratic Bergman monomial

## Finding

In the classical normalized analytic Bergman space \(A^2(\mathbb D)\), let \(K_a(z)=(1-\overline a z)^{-2}\), and let \(f(z)=z^2\). Among all **distinct** pairs \(a,b\in\mathbb D\) with \(|a|=|b|\), the unique maximum of
\[
\mathcal P(a,b)=\|\operatorname{Proj}_{\operatorname{span}\{K_a,K_b\}}f\|_{A^2}^2
\]
(up to common rotation, complex conjugation of the relative angle, and interchange of the points) occurs at
\[
|a|^2=|b|^2=t_*,\qquad \cos(\arg(b/a))=c_*,
\]
where \(t_*\) is the unique root in \((39078/100000,39079/100000)\) of
\[
5t^4-9t^3+9t^2-5t+1=0,
\]
and
\[
c_*={15t_*^3-17t_*^2+14t_*-4\over2}.
\]
The maximizing squared projection is \(\mathcal P_*=F(t_*,c_*)\), where the explicit rational function \(F\) is given below. Numerically,
\[
\begin{aligned}
t_*&=0.39078072031918159\ldots,\\
|a|=|b|&=0.62512456384242460\ldots,\\
c_*&=-0.11499664218141442\ldots,\\
|\arg(b/a)|&=1.68604794621828735\ldots,\\
\mathcal P_*&=0.15741816657239726\ldots .
\end{aligned}
\]
Thus the equal-sensitivity optimal pair is **neither coincident nor antipodal nor orthogonal**. It captures the fraction \(3\mathcal P_*=0.47225449971719\ldots\) of the target's squared Bergman norm.

## Assumptions and scope

The inner product is \(\langle f,g\rangle=\pi^{-1}\int_{\mathbb D}f(z)\overline{g(z)}\,dA(z)\), linear in the first variable. Consequently \(\|z^2\|^2=1/3\) and \(\|K_a\|=(1-|a|^2)^{-1}\). Requiring equal radii is therefore the natural **equal evaluation-norm** (equal-sensitivity) condition, rather than a fixed arbitrary radial slice. The radius is optimized jointly with the angular separation. No assertion about the unconstrained two-point dictionary is made.

By rotation, write \(a=\sqrt t\), \(b=\sqrt t\,e^{i\theta}\), \(0<t<1\), and \(c=\cos\theta\). For distinct points, \(-1\le c<1\); the value \(c=1\) is used solely as a collision-limit boundary value, not as the projection onto a one-dimensional repeated kernel.

## Proof

**1. Exact two-kernel projection.** Let \(G=(K_{a_j}(a_i))_{i,j=1}^2\) and \(v=(a^2,b^2)^{\mathsf T}\). Reproduction and orthogonal projection give \(\mathcal P=v^*G^{-1}v\). Write \(q=1-2tc+t^2\) and \(P=\cos(2\theta)-2t\cos(3\theta)+t^2\cos(4\theta)\). Evaluation of the two-by-two inverse yields
\[
F(t,c)=\frac{2t^2(1-t)^2\{q^2-(1-t)^2P\}}{q^2-(1-t)^4}.
\]
Cancelling the factor common to numerator and denominator gives the everywhere regular form for \(0<t<1\), \(-1\le c\le1\):
\[
F(t,c)=\frac{t(1-t)^2Q(t,c)}{1-t+t^2-tc},
\]
where
\[
\begin{aligned}
Q(t,c)={}&(4t^4-8t^3+4t^2)c^3\\
&+(4t^4-12t^3+12t^2-4t)c^2\\
&+(-4t^3+7t^2-6t+1)c\\
&+t^3+t^2-t+1.
\end{aligned}
\]
The denominator equals \((1-t)^2+t(1-c)>0\). The expression extends continuously to the closed rectangle \([0,1]\times[-1,1]\), with zero at \(t=0\) and \(t=1\). At the only potentially ambiguous corner \((1,1)\), note \(Q(t,1)=(1-t)^2(8t^2-7t+2)\) and \(Q(t,c)-Q(t,1)=O(1-c)\) uniformly, giving \(F=O((1-t)^2)\).

**2. The boundary cannot maximize.** The angular boundary values are
\[
F(t,1)=t(1-t)^2(8t^2-7t+2),\quad
F(t,-1)=\frac{t^2(1-t^2)^2}{1+t^2}.
\]
The derivative of the first is \(2(t-1)(2t-1)(10t^2-8t+1)\), giving its absolute maximum
\[
\max_{0\le t\le1}F(t,1)=\frac{1179+144\sqrt6}{12500}<\frac18.
\]
For the second, put \(y=t^2\); differentiation yields its absolute maximum \((71-17\sqrt{17})/8<1/8\). However the exact interior test \(F(2/5,-1/8)=1967/12500>1/8\). Hence a global maximizer is genuinely interior.

**3. Exact stationary-point elimination.** Write \(F=A/B\) in reduced polynomial form and set \(U=(A_cB-AB_c)/[t(t-1)^4]\), \(V=(A_tB-AB_t)/(t-1)\). Both are polynomials with integer coefficients. An exact polynomial resultant gives
\[
\begin{aligned}
\operatorname{Res}_c(U,V)={}&-4096t^{15}(2t^2-1)(4t^2-4t-1)\\
&\quad\cdot(2t^3-2t^2+2t-1)^4\\
&\quad\cdot(5t^4-9t^3+9t^2-5t+1).
\end{aligned}
\]
All of these equalities are verified by exact rational polynomial arithmetic in `checker.py`. The factors have the following common-root restrictions, also obtainable from exact lexicographic polynomial reduction:

* On the quartic factor, \(c=(15t^3-17t^2+14t-4)/2\).
* On the cubic factor, \((c-(2t^2-t+1))^2=0\). Its only root in \((0,1)\) has \(t>1/2\), hence \(c>1\).
* On \(2t^2-1=0\), necessarily \(c=3t/2>1\) for its positive root.
* The factor \(4t^2-4t-1\) has no root in \((0,1)\).

Sturm's exact root count gives precisely two quartic roots in \((0,1)\). Their rational isolating brackets are \((39078/100000,39079/100000)\) and \((67924/100000,67926/100000)\). The displayed cubic expression for \(c\) is strictly increasing in \(t\) (its derivative is a positive quadratic). On the first bracket it lies strictly between \(-1\) and \(1\), while on the second it exceeds \(1\). Exact reduction also proves that the first quartic pair simultaneously zeros \(U\) and \(V\). It is therefore the **only** interior stationary point. Compactness of the parameter rectangle and Step 2 force it to be the unique global maximizer.

**4. Optimal approximation.** For either angular orientation of the maximizing pair, the orthogonal projection coefficients are exactly \(G^{-1}v\). The squared residual is \(1/3-F(t_*,c_*)=0.17591516676093607\ldots\). Rotations and permutation are the only maximizing-point symmetries described by the theorem.

## Verification

`checker.py` uses exact polynomial, Groebner-basis and Sturm-root computations over the rationals to check the Gram identity, reduced rational formula, derivative factors, resultant, algebraic common-root restrictions, root counts, isolating intervals, and strict boundary comparisons. It also prints supplementary decimal approximations. To reproduce: install dependencies from `requirements.txt` and run `python checker.py`. The checker was executed successfully from the packaged files. The global statement relies on the analytic compactness and boundary argument plus these exact algebraic certificates, not on numerical optimization.

## Relationship to prior work

Qu, Qian, Li and Zhu introduced an existence theorem for best finite reproducing-kernel approximations in weighted Bergman spaces (available online November 10, 2021). Qian's January 18, 2022 preprint develops existence for broader analytic RKHSs, including repeated kernels, and explicitly defers global computation of optimal parameters to separate work. This finding addresses a different, **quantitative** question: it solves the natural equal-evaluation-norm two-atom optimization for the first quadratic Bergman monomial, including the unique non-cardinal angle and an algebraic exact constant. General existence and the known two-by-two Gram formula alone do not specify the optimizer; the stationary elimination and global comparison are essential.

## Limitations

The equal-sensitivity constraint \(|a|=|b|\) is essential to this theorem. Unrestricted two-kernel optimality, other target monomials, other Bergman weights, and multi-kernel designs are not proved. The result treats distinct parameters; the coincident-parameter value in the proof is a confluent limit only. An equivalent calculation may exist outside the literature examined; independent priority review and independent mathematical validation have not been performed.

## References

1. W. Qu, T. Qian, H. Li, K. Zhu, *Best kernel approximation in Bergman spaces*, Applied Mathematics and Computation **416** (2022), 126749, DOI 10.1016/j.amc.2021.126749. Available online November 10, 2021.
2. T. Qian, *n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2201.07228 (first posted January 18, 2022), especially Theorem 2.1 and Remark 5.2.
