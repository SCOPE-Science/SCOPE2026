# All Schatten-\(p\) distances select one metric ray in the two-level quasi-Hermitian problem
## Finding
For every \(2\times2\) quasi-self-adjoint operator with simple real spectrum and normalized left eigenvectors \(\phi_1,\phi_2\), write \(s=|\langle\phi_1,\phi_2\rangle|\in[0,1)\). For every Schatten index \(1\le p\le\infty\), the minimization of \(\|\Theta-I\|_p\) over all positive metrics \(\Theta=C_1|\phi_1\rangle\langle\phi_1|+C_2|\phi_2\rangle\langle\phi_2|\), \(C_1,C_2>0\), has a unique minimizer \(\Theta_p=c_p(s)(|\phi_1\rangle\langle\phi_1|+|\phi_2\rangle\langle\phi_2|)\). For \(1<p<\infty\), with \(q=p/(p-1)\), \(c_p(s)=((1+s)^{q-1}+(1-s)^{q-1})/((1+s)^q+(1-s)^q)\) and the minimum distance is \(d_p(s)=2s/((1+s)^q+(1-s)^q)^{1/q}\); at the endpoints, \(c_1(s)=1/(1+s)\), \(d_1(s)=2s/(1+s)\), \(c_\infty(s)=1\), and \(d_\infty(s)=s\). Consequently every Schatten criterion selects the same positive metric ray, and at \(p=2\) this ray and normalization recover the 2018 Hilbert–Schmidt minimizer.

This gives a complete two-level answer to the alternative Schatten-class minimizations explicitly suggested in the 2018 metric-selection paper. The norm changes the scalar normalization of the selected metric, but not its positive ray.

## Assumptions and scope
Let \(H\) be a \(2\times2\) quasi-self-adjoint operator with two distinct real eigenvalues. Let \(\phi_1,\phi_2\in\mathbb{C}^2\) be the normalized left eigenvectors used in the standard biorthogonal description, so \(\|\phi_1\|=\|\phi_2\|=1\) and they are linearly independent. Put
\[
s=|\langle\phi_1,\phi_2\rangle|,\qquad 0\le s<1.
\]
For this class, every positive metric has the form
\[
\Theta=C_1|\phi_1\rangle\langle\phi_1|+C_2|\phi_2\rangle\langle\phi_2|,\qquad C_1,C_2>0.
\]
The optimization is over this full positive metric family. The identity \(I\) and Schatten norms are taken in the original Hilbert-space inner product.

## Proof
Set
\[
t=\frac{C_1+C_2}2>0,\qquad u=\frac{C_1-C_2}{C_1+C_2}\in(-1,1).
\]
The trace and determinant of \(\Theta\) are
\[
\operatorname{tr}\Theta=2t,\qquad \det\Theta=t^2(1-u^2)(1-s^2).
\]
Hence the eigenvalues of \(\Theta\) are
\[
\lambda_\pm=t(1\pm r),\qquad r=\sqrt{s^2+(1-s^2)u^2}.
\]
Therefore \(r\ge s\), with equality exactly when \(u=0\), equivalently \(C_1=C_2\).

Because \(\Theta-I\) is Hermitian, its singular values are \(|t(1+r)-1|\) and \(|t(1-r)-1|\). Thus, for fixed \(r\), the problem reduces to minimizing
\[
F_p(t,r)=\left(|t(1+r)-1|^p+|t(1-r)-1|^p\right)^{1/p}
\]
when \(1\le p<\infty\), and the maximum of the two absolute values when \(p=\infty\).

For \(1<p<\infty\), strict convexity gives a unique minimizing \(t\). At that point the two residuals have opposite signs and the derivative equation is
\[
(1+r)\big(t(1+r)-1\big)^{p-1}=(1-r)\big(1-t(1-r)\big)^{p-1}.
\]
Writing \(q=p/(p-1)\), this yields
\[
t_p(r)=\frac{(1+r)^{q-1}+(1-r)^{q-1}}{(1+r)^q+(1-r)^q}.
\]
Substitution gives the one-variable optimum
\[
m_p(r)=\frac{2r}{\big((1+r)^q+(1-r)^q\big)^{1/q}}.
\]
Its logarithmic derivative is
\[
\frac{d}{dr}\log m_p(r)=\frac1r-\frac{(1+r)^{q-1}-(1-r)^{q-1}}{(1+r)^q+(1-r)^q}.
\]
After multiplication by the positive denominator, its numerator is
\[
(1+r)^{q-1}+(1-r)^{q-1}>0.
\]
Thus \(m_p(r)\) is strictly increasing, so the global minimum occurs uniquely at \(r=s\), forcing \(C_1=C_2\). Setting \(r=s\) gives the stated \(c_p(s)\) and \(d_p(s)\).

For \(p=1\), the fixed-\(r\) objective is piecewise linear. Its unique minimum occurs at \(t=1/(1+r)\), with value \(2r/(1+r)\), again strictly increasing in \(r\). For \(p=\infty\), the unique fixed-\(r\) optimum equioscillates the two residuals, giving \(t=1\) and minimum \(r\). Hence both endpoints also force \(r=s\) and \(C_1=C_2\).

At \(p=2\), \(q=2\), so
\[
c_2(s)=\frac1{1+s^2},
\]
which is exactly the coefficient in the published two-dimensional Hilbert–Schmidt minimizer when \(s^2=\gamma\).

## Verification
The accompanying verifier independently evaluates the closed-form coefficient and minimum for representative values of \(s\) and \(p\), compares them against a dense two-parameter search over positive \(C_1,C_2\), checks the \(p=2\) specialization, and checks the strict monotonicity formula numerically. It reports `VERIFY_OK`.

The computational check is supplementary: the proof above is algebraic and covers the entire continuous domain \(0\le s<1\), \(1\le p\le\infty\).

## Relationship to prior work
Krejčiřík, Lotoreichik, and Znojil formulated metric selection by minimizing Hilbert–Schmidt distance and explicitly noted that analogous minimizations can be posed in other Schatten classes, including operator norm. Their two-dimensional example gives the Hilbert–Schmidt optimizer with equal coefficients \(1/(1+s^2)\). The result here solves that stated alternative family for every Schatten index and shows that all of those norms select the same positive metric ray.

Earlier two-level work by Znojil and Geyer parameterized the positive metric ambiguity for a specific \(2\times2\) model and discussed possible restrictions for choosing a metric, but did not give the Schatten-distance family above. Feinberg and Znojil later parameterized all metrics compatible with a generic finite-dimensional pseudo-Hermitian matrix; their result supplies a broad description of the admissible metric space rather than this norm-minimization law.

## Limitations
The ray-invariance theorem is specific to dimension two and to distance from the identity in Schatten norms. It does not assert that the same ray remains optimal in higher dimensions, under weighted/unity-constrained normalizations, or for non-Schatten objectives. The literature comparison found no direct statement of the complete formula above, but an equivalent two-vector matrix-approximation theorem could exist under different terminology.

## References
1. D. Krejčiřík, V. Lotoreichik, M. Znojil, *The minimally anisotropic metric operator in quasi-Hermitian quantum mechanics*, Proc. R. Soc. A 474 (2018), 20180264. arXiv:1804.06766v1; DOI:10.1098/rspa.2018.0264.
2. M. Znojil, H. B. Geyer, *Construction of a unique metric in quasi-Hermitian quantum mechanics: non-existence of the charge operator in a \(2\times2\) matrix model*, Phys. Lett. B 640 (2006), 52–56. arXiv:quant-ph/0607104v1; DOI:10.1016/j.physletb.2006.07.028.
3. J. Feinberg, M. Znojil, *Which Metrics Are Consistent with a Given Pseudo-Hermitian Matrix?*, J. Math. Phys. 63 (2022), 013505. arXiv:2111.04216v2; DOI:10.1063/5.0079385.
