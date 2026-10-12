# Sharp epoch-length stability reversal in two-component SVRG

## Finding

For two distinct positive scalar curvatures, the largest mean-square stable constant stepsize of **last-iterate stochastic variance-reduced gradient** (SVRG, Option I) changes order when an epoch is lengthened from two to three inner updates. Writing the normalized curvature heterogeneity as \(z\in(0,1)\), the two- and three-step stability boundaries \(\tau_2(z)\) and \(\tau_3(z)\) satisfy
\[
\tau_3(z)>\tau_2(z)\quad(0<z<z_c),\qquad
\tau_3(z)=\tau_2(z)\quad(z=z_c),\qquad
\tau_3(z)<\tau_2(z)\quad(z_c<z<1),
\]
where the **unique** \(z_c\in(0,1)\) solves
\[
128z_c^3-41z_c^2+6z_c-1=0,
\qquad z_c=0.256342606727\ldots.
\]
Thus an additional stochastic inner update can either enlarge or shrink the exact admissible constant-stepsize interval, depending on component-curvature heterogeneity.

## Assumptions and scope

Let \(a_1,a_2>0\), \(a_1\ne a_2\), and minimize the strongly convex finite sum
\[
f(x)=\tfrac12\bigl(f_1(x)+f_2(x)\bigr),\qquad
f_i(x)=\frac{a_i}{2}x^2.
\]
Define \(\mu=(a_1+a_2)/2>0\), \(z=((a_1-a_2)/(a_1+a_2))^2\in(0,1)\), and normalized stepsize \(t=\eta\mu\), where \(\eta>0\). At the start of each epoch set the snapshot \(s=x_0\). For \(j=1,\ldots,m\) use *independent uniform* draws \(i_j\in\{1,2\}\) and
\[
x_j=x_{j-1}-\eta\bigl(a_{i_j}(x_{j-1}-s)+\mu s\bigr),
\]
then take the **last iterate** \(s_{\mathrm{next}}=x_m\) as the next epoch's snapshot; epoch random draws are independent. Only \(m\in\{2,3\}\) is claimed. Mean-square convergence means \(\mathbb E[s_k^2]\to0\) as the number \(k\) of completed epochs tends to infinity, for every deterministic initial snapshot \(s_0\in\mathbb R\). It also entails convergence at every intermediate inner index for either fixed epoch length.

For \(t\ge0\), set
\[
F_2(t,z)=(1-t)^4+zt^4,
\]
\[
F_3(t,z)=(1-t)^6+zt^4\bigl((1-t)^2+(2-t)^2\bigr)+z^2t^6.
\]
Each equation \(F_m(t,z)=1\) has exactly one root \(\tau_m(z)>0\), besides the root at zero, and
\[
F_m(t,z)<1\ \Longleftrightarrow\ 0<t<\tau_m(z).
\]
In particular, \(\tau_2(z)\in(1,2)\). Hence mean-square convergence for **every** deterministic start holds exactly at \(0<\eta\mu<\tau_m(z)\); equality is not a convergent endpoint for any nonzero start, and beyond it the second moments increase geometrically. The unique crossing has the common normalized stepsize \(t_c=1.396608252736\ldots\), the unique root in \((1,2)\) of
\[
2t_c^3-8t_c^2+13t_c-8=0.
\]
No statement is made for averaged-snapshot SVRG, more components, nonquadratic losses, or higher epoch lengths.

## Proof

Put \(q=(a_1-a_2)/(a_1+a_2)\), so \(q^2=z\). Each selected component has normalized curvature \(1+\xi_j\), where \(\xi_j\in\{-q,q\}\) are independent uniform signs (their sign labeling is immaterial). For a nonzero snapshot \(s\), normalize the iterate as \(y_j=x_j/s\). The update becomes
\[
y_j=(1-t-t\xi_j)y_{j-1}+t\xi_j,\qquad y_0=1.
\]
The first update is exactly \(y_1=1-t\), independent of \(\xi_1\). The next coefficients expand to
\[
y_2=(1-t)^2+t^2\xi_2,
\]
\[
y_3=(1-t)^3+t^2(1-t)\xi_2+t^2(2-t)\xi_3-t^3\xi_2\xi_3.
\]
The four functions \(1,\xi_2,\xi_3,\xi_2\xi_3\) are orthogonal in expectation. Taking second moments gives the claimed \(F_2\) and \(F_3\). Because every epoch resamples independently, conditioning on \(s_k\) yields
\[
\mathbb E[s_{k+1}^2\mid s_k]=F_m(t,z)s_k^2,
\qquad
\mathbb E[s_k^2]=F_m(t,z)^k s_0^2.
\]
This is an exact equivalence, including at equality. Every inner iterate is a linear random multiple of its epoch snapshot with a finite fixed second moment, so convergence of snapshots also gives convergence at inner indices.

For \(m=2\), \(F_2(0,z)=1\), \(F_2(t,z)<1\) for \(0<t\le1\) (using \(z<1\)), and \(\partial_tF_2=4(t-1)^3+4zt^3>0\) for \(t\ge1\). Since \(F_2(2,z)=1+16z>1\), there is exactly one positive cutoff \(\tau_2\in(1,2)\), with the stated inequality on either side.

For \(m=3\), on \(0\le t\le1\), the exact degree-six Bernstein expansion is
\[
F_3(t,z)=\sum_{j=0}^6\binom6j b_j t^j(1-t)^{6-j},
\qquad
(b_0,\ldots,b_6)=\bigl(1,0,0,0,z/3,2z/3,z(1+z)\bigr).
\]
Subtracting the constant polynomial one and setting \(u=t/(1-t)>0\), the nonzero coefficients of \((1+u)^6(F_3-1)\) are strictly negative through degree five; the degree-six coefficient is \(z(1+z)-1\). If it is nonpositive, \(F_3<1\) throughout \(0<t<1\). If it is positive, Descartes' rule of signs and the signs at the two interval endpoints prove exactly one crossing in \((0,1)\). On \(t\ge1\), write \(t=1+y\), \(y\ge0\); direct differentiation gives
\[
\partial_tF_3(1+y,z)
=2z(1+3z)+30z^2y+60z^2y^2
+20z(1+3z)y^3+30z(1+z)y^4+6(1+z)^2y^5>0.
\]
Moreover \(F_3(t,z)\to\infty\) as \(t\to\infty\). These facts prove the unique positive cutoff and strict below/above characterization for every \(z\in(0,1)\), including the case \(F_3(1,z)=1\).

At the two-step cutoff \(t=\tau_2(z)\), solve \(F_2(t,z)=1\) for heterogeneity:
\[
z=-1+\frac4t-\frac6{t^2}+\frac4{t^3}
=\frac{(2-t)(t^2-2t+2)}{t^3}.
\]
This function is strictly decreasing on \((1,2)\), because its derivative equals
\[
-\frac{4(t^2-3t+3)}{t^4}<0.
\]
Substituting into the three-step factor gives the **exact comparison identity**
\[
F_3(\tau_2,z)-1=(\tau_2-2)C(\tau_2),\qquad
C(t)=2t^3-8t^2+13t-8.
\]
The derivative \(C'(t)=6t^2-16t+13\) is strictly positive for every real \(t\), since its discriminant is negative and its leading coefficient positive. Also \(C(1)=-1\), \(C(2)=2\); hence one root \(t_c\in(1,2)\). Eliminating \(t_c\) from \(C(t_c)=0\) and the displayed heterogeneity equation gives
\[
128z_c^3-41z_c^2+6z_c-1=0.
\]
That cubic is strictly increasing since \(384z^2-82z+6>0\) for all real \(z\), and it changes sign between zero and one. Thus its root \(z_c\) is unique and equals the heterogeneity at \(t_c\). Since \(\tau_2(z)\) strictly decreases with \(z\), and \(\tau_2-2<0\), the sign of \(F_3(\tau_2,z)-1\) is negative for \(z<z_c\) and positive for \(z>z_c\). Using the uniqueness of the three-step cutoff gives exactly the announced reversal.

Two exact witnesses certify that the two regimes are substantive, not just a comparison of limiting formulas. For \(z=1/16\), \(t=9/5\),
\[
F_2-1=\frac{657}{10000}>0,
\qquad F_3-1=-\frac{635391}{4000000}<0.
\]
For \(z=9/16\), \(t=11/10\),
\[
F_2-1=-\frac{5643}{32000}<0,
\qquad F_3-1=\frac{483021}{2048000}>0.
\]
Both heterogeneity values correspond to strictly positive distinct component curvatures, e.g. \((a_1,a_2)=(5,3)\) and \((7,1)\), respectively, with \(\mu=4\) in both cases.

## Verification

The standalone Python 3 program `verify_svrg.py` requires only the standard library. Run `python verify_svrg.py` from the directory containing this file. It independently enumerates every sampled sign branch over two and three inner steps using exact rational arithmetic for 160 tested parameter pairs, checks both moment polynomials and the Bernstein identity, proves the displayed rational witness identities by exact integer fractions, and brackets both crossing roots by exact sign comparisons. The execution returned `VERIFY_OK`. Exhaustive symbolic arguments and inequalities above, **not** these finitely many tests, establish the universal theorem.

## Relationship to prior work

Johnson and Zhang (2013) introduce the exact SVRG update and state Option I (last iterate) versus Option II (randomly selected iterate). The algorithm and generic variance-reduction convergence guarantees are prior mathematics. Xiao and Zhang (2014) analyze a proximal/averaged-snapshot variant. Sebbouh and coauthors (2019) analyze a Free-SVRG averaged scheme, and Kahale (2020) studies a quadratic SVRG variant whose snapshots are averaged. The distinctive claim here is only the **necessary-and-sufficient mean-square cutoffs for the two shortest nontrivial last-snapshot epochs, together with their unique curvature-heterogeneity ordering reversal**. The general update equation and the fact that averaging choices influence convergence are not presented as discoveries.

## Limitations

The classification concerns exact arithmetic, independent uniform component sampling, scalar positive quadratic curvatures, one fixed stepsize, last-iterate snapshots, and epochs of precisely two or three steps. The endpoint \(t=\tau_m\) is excluded from convergence for nonzero starts. The thresholds do not imply a practical recommendation independent of epoch cost, gradient-evaluation budget, numerical roundoff, or nonquadratic behavior. Earlier specialized SVRG or incremental-gradient analyses under different notation might contain an equivalent short-epoch calculation; such equivalence is the main remaining originality risk. Self-review is not independent validation.

## References

1. R. Johnson and T. Zhang, *Accelerating Stochastic Gradient Descent Using Predictive Variance Reduction*, NeurIPS 26 (2013), original procedure and Options I/II, <https://proceedings.neurips.cc/paper/2013/file/ac1dd209cbcc5e5d1c6e28598e8cbbe8-Paper.pdf>.
2. L. Xiao and T. Zhang, *A Proximal Stochastic Gradient Method with Progressive Variance Reduction*, arXiv:1403.4699v1 (2014), <https://arxiv.org/pdf/1403.4699v1>; journal version, SIAM J. Optim., DOI:10.1137/140961791.
3. O. Sebbouh et al., *Towards Closing the Gap Between the Theory and Practice of SVRG*, arXiv:1908.02725 (2019), <https://arxiv.org/pdf/1908.02725>.
4. N. Kahale, *Improved SVRG for Quadratic Functions*, arXiv:2006.01017 (2020), <https://arxiv.org/pdf/2006.01017>.
