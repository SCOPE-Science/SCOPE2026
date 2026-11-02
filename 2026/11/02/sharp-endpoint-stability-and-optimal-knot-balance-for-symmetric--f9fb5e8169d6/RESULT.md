# Sharp endpoint stability and optimal knot balance for symmetric five-node linear splines

## Finding
For each real \(0<\varepsilon<1\), take the ordered knots \((-1,-\varepsilon,0,\varepsilon,1)\) and let \(P_\varepsilon\) be the real \(L^2[-1,1]\)-orthogonal projection onto continuous functions affine between consecutive knots. Write
\[
C(\varepsilon)=\frac{7+3\varepsilon}{3(1+\varepsilon)},\qquad
E(\varepsilon)=\frac{300+403\varepsilon+27\varepsilon^2-23\varepsilon^3-3\varepsilon^4}{3(1+\varepsilon)(5+\varepsilon)(12-3\varepsilon-\varepsilon^2)}.
\]
Then the **exact attained operator norm** is
\[
\boxed{\|P_\varepsilon\|_{L^\infty\to L^\infty}=\max\{C(\varepsilon),E(\varepsilon)\}.}
\]
Put \(\varepsilon_*=(\sqrt{161}-11)/4\). The center knot is the unique maximizing knot for \(0<\varepsilon<\varepsilon_*\); both endpoints are the only maximizing knots for \(\varepsilon_*<\varepsilon<1\); and the center and both endpoints maximize at the transition. Every shoulder knot has strictly smaller row norm. The norm has a **unique minimum** over all symmetric five-knot patterns at
\[
\boxed{\varepsilon_*=\frac{\sqrt{161}-11}{4},\qquad \min_{0<\varepsilon<1}\|P_\varepsilon\|=\frac43+\frac{\sqrt{161}}{21}.}
\]
The clustering limits are \(\lim_{\varepsilon\downarrow0}\|P_\varepsilon\|=7/3\) and \(\lim_{\varepsilon\uparrow1}\|P_\varepsilon\|=22/9\). In particular, the center row exceeds two exactly for \(0<\varepsilon<1/3\), giving a sharp clustered-knot amplification mechanism within the five-node family.

## Assumptions and scope
All functions, inner products and splines are real. The underlying space has ordinary Lebesgue measure on \([-1,1]\); an overall positive normalization does not affect the orthogonal projector. There are exactly five distinct, symmetric knots, \(0<\varepsilon<1\), and the spline degree is one, with continuity imposed at the interior knots. Input is essentially bounded measurable and output is represented by its continuous spline; the operator norm is taken in the essential supremum norm. Statements about optimality are **only within this one-parameter symmetric five-node family**, not among arbitrary partitions or projection operators.

## Proof
Let \(t_0=-1,t_1=-\varepsilon,t_2=0,t_3=\varepsilon,t_4=1\), and let \(\phi_i\) be the standard nodal hat splines, so \(\phi_i(t_j)=\delta_{ij}\). For \(h=(1-\varepsilon,\varepsilon,\varepsilon,1-\varepsilon)\), direct integration gives the symmetric positive-definite Gram matrix \(G\) with
\[
G_{ii}=\frac{h_{i-1}+h_i}{3},\quad G_{i,i+1}=\frac{h_i}{6},
\]
with omitted endpoint gaps set to zero and every other entry zero. The reproducing kernel is \(K_\varepsilon(t,s)=\phi(t)^{\mathsf T}G^{-1}\phi(s)\). Thus
\[
\|P_\varepsilon\|=\sup_{t\in[-1,1]}\int_{-1}^1|K_\varepsilon(t,s)|\,ds.
\]
For fixed \(s\), the kernel is affine in \(t\) on each knot interval. The integral of its absolute value is consequently convex on each such interval, so its supremum occurs at a knot. Reflection reduces the five possible knot rows to the endpoint, shoulder and center classes.

Explicit inversion yields the following three rows of \(G^{-1}\), in nodal order; the other two are their reversals:
\[
\begin{aligned}
R_0={}&\left(\frac{\varepsilon^2-\varepsilon-24}{2(\varepsilon-1)(\varepsilon+3)},-\frac{\varepsilon+6}{\varepsilon+3},\frac12,-\frac{\varepsilon}{\varepsilon+3},\frac{\varepsilon}{2(\varepsilon+3)}\right),\\
R_1={}&\left(-\frac{\varepsilon+6}{\varepsilon+3},\frac{2(\varepsilon+6)}{\varepsilon+3},-1,\frac{2\varepsilon}{\varepsilon+3},-\frac{\varepsilon}{\varepsilon+3}\right),\\
R_2={}&\left(\frac12,-1,\frac{\varepsilon+3}{2\varepsilon},-1,\frac12\right).
\end{aligned}
\]
Each row alternates strictly in sign for the entire admissible parameter interval. An affine function joining opposite-sign endpoint values of magnitudes \(a,b>0\) on an interval of length \(h\) has absolute integral \(h(a^2+b^2)/(2(a+b))\). Applying this elementary identity over the four intervals gives the exact nodal kernel integrals
\[
\begin{aligned}
E(\varepsilon)&=\int_{-1}^1|K_\varepsilon(-1,s)|\,ds,\\
S(\varepsilon)&=\int_{-1}^1|K_\varepsilon(-\varepsilon,s)|\,ds
=\frac{5\varepsilon^2+38\varepsilon+25}{3(\varepsilon+1)(\varepsilon+5)},\\
C(\varepsilon)&=\int_{-1}^1|K_\varepsilon(0,s)|\,ds.
\end{aligned}
\]
The shoulder is never maximal, since
\[
E(\varepsilon)-S(\varepsilon)=\frac{2\varepsilon(\varepsilon^3+15\varepsilon^2+53\varepsilon+11)}{3(\varepsilon+1)(\varepsilon+5)(12-3\varepsilon-\varepsilon^2)}>0.
\]
Moreover,
\[
E(\varepsilon)-C(\varepsilon)=\frac{4(\varepsilon+6)(2\varepsilon^2+11\varepsilon-5)}{3(\varepsilon+1)(\varepsilon+5)(12-3\varepsilon-\varepsilon^2)}.
\]
All denominators here are positive for \(0<\varepsilon<1\). The polynomial \(2\varepsilon^2+11\varepsilon-5\) changes sign exactly once in this interval, at \(\varepsilon_*=(\sqrt{161}-11)/4\); this proves the claimed maximizing knot classes and the two branches.

The center branch satisfies \(C'(\varepsilon)=-4/[3(1+\varepsilon)^2]<0\). Direct differentiation gives
\[
E'(\varepsilon)=\frac{4Q(\varepsilon)}{3(1+\varepsilon)^2(5+\varepsilon)^2(12-3\varepsilon-\varepsilon^2)^2}>0,
\]
where \(Q(\varepsilon)=\varepsilon^6+30\varepsilon^5+298\varepsilon^4+1278\varepsilon^3+2483\varepsilon^2+2460\varepsilon+1770\) has positive coefficients. The maximum of one strictly decreasing branch and one strictly increasing branch therefore has its unique global minimum at their crossing. Substitution simplifies the minimum to \(4/3+\sqrt{161}/21\). Taking the one-sided limits in the two branches gives \(7/3\) and \(22/9\). Finally \(C(\varepsilon)>2\) is exactly equivalent to \(\varepsilon<1/3\).

At any maximizing knot \(t_*\), the measurable input \(f(s)=\operatorname{sgn}K_\varepsilon(t_*,s)\) has essential norm one, and \((P_\varepsilon f)(t_*)=\int|K_\varepsilon(t_*,s)|\,ds\). This proves actual norm attainment (zero values of the kernel may be assigned either sign).

## Verification
The standalone `check.py` reconstructs the Gram matrix and its inverse symbolically, checks the three exact nodal absolute-integral identities, all branch-difference and derivative identities, the minimizer, and both clustering limits. Independently, it constructs hat functions and applies adaptive quadrature to the absolute kernel on all four subintervals at thirteen rational parameter values, including 533 nodal and interior evaluation comparisons. These finite tests corroborate, but do not replace, the all-parameter algebraic proof above. Execute with Python 3, SymPy, NumPy and SciPy installed using `python check.py`.

## Relationship to prior work
The general one-dimensional linear-spline \(L^\infty\) orthoprojector bound of three, known from Ciesielski and sharp in Oskolkov's work, is not claimed as new; the present result is a **specific exact five-node stability profile and a sharp minimax knot balance**. Kayumov's 2004 survey and study of second-order \(L\)-splines gives this history and studies distinct exponential/trigonometric spline spaces. Oswald's 2006 example establishes unbounded norms for two- and higher-dimensional simplicial spline spaces and recalls the one-dimensional bound; it does not give the five-node symmetric profile. A known two-periodic spline projection calculation concerns a different infinite periodic knot configuration and does not determine the finite clustered arrangement here. Searches for the displayed radical, the two limiting constants and symmetric-five-knot formulas found no decisive equivalent; absence of a search hit does not prove priority.

## Limitations
The result does not determine the exact norms for nonsymmetric five-node knot arrangements, different spline degrees, discrete sampling measures, or higher spatial dimensions. The extrema as \(\varepsilon\to0\) and \(\varepsilon\to1\) are **limits of distinct-knot projectors** and are not norms of a projector obtained by simply merging repeated knots. Historical specialist studies, including Oskolkov's 1979 work, may contain unindexed equivalent finite-knot formulas; that priority risk is unresolved. No independent scientific audit has been conducted.

## References
1. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first public posting 2004-08-30. https://arxiv.org/abs/math/0408418
2. P. Oswald, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces*, arXiv:math/0611573, first public posting 2006-11-19. https://arxiv.org/abs/math/0611573
3. Z. Ciesielski, *Properties of the orthonormal Franklin system*, 1963, cited in the two papers above.
4. K. I. Oskolkov, *The upper bound of the norms of orthogonal projections onto subspaces of polygonals*, 1979, cited in Kayumov's review; specialist full text not inspected.
