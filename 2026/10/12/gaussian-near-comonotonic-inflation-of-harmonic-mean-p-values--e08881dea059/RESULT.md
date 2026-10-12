# Gaussian near-comonotonic inflation of harmonic-mean p-values

## Finding
Fix an integer \(n\ge2\), weights \(w_i\ge0\) satisfying \(\sum_{i=1}^{n}w_i=1\), and a significance level \(p\in(0,1)\). Let \(Z,E_1,\ldots,E_n\) be independent standard normal random variables. For a pairwise correlation parameter \(0\le r<1\), set
\[
X_i^{(r)}=\sqrt r\,Z+\sqrt{1-r}\,E_i,\qquad
U_i^{(r)}=\Phi(X_i^{(r)}),\qquad
H_r=\left(\sum_{i=1}^{n}\frac{w_i}{U_i^{(r)}}\right)^{-1},
\]
where \(\Phi\) and \(\phi\) are the standard normal distribution function and density. Thus the \(U_i^{(r)}\) are exact uniform null p-values following an equicorrelated Gaussian copula with **pairwise correlation** \(r\). With \(q=\Phi^{-1}(p)\), the exact one-sided boundary derivative is
\[
\boxed{\lim_{r\uparrow1}
\frac{\Pr(H_r\le p)-p}{1-r}
=\left(1-\sum_{i=1}^{n}w_i^2\right)
\phi(q)\left(q+\frac{\phi(q)}{p}\right).}
\]
If at least two weights are positive, the coefficient is strictly positive for every fixed \(p\in(0,1)\). Consequently, for every such fixed \(p\) and weight vector, there exists \(r_0(p,w,n)<1\) such that \(\Pr(H_r\le p)>p\) for all \(r_0<r<1\). If only one weight is nonzero, \(H_r\) is uniform and the excess is identically zero for every \(r\). For equal weights the coefficient is multiplied by \(1-1/n\).

## Assumptions and scope
The dimension, weights, and level are fixed while \(r\uparrow1\). We assume neither independence of the p-values nor an asymptotic regime with \(p\downarrow0\) or \(n\to\infty\). The definition uses \(\Phi(X_i^{(r)})\); replacing every \(\Phi\) by \(1-\Phi\) gives the same law by normal symmetry. The theorem includes weights equal to zero. The factor loading \(\sqrt r\) is not the pairwise correlation: the latter is precisely \(r\). The limit at \(r=1\) itself is comonotonic and has \(H_1=\Phi(Z)\).

## Proof
Write \(h=\sqrt{1-r}\), \(c=\sqrt{1-h^2}\), and \(f(x)=1/\Phi(x)\). For a fixed vector \(e=(e_i)\), the strictly decreasing function
\[
z\longmapsto\sum_iw_i f(cz+he_i)
\]
varies continuously from infinity to one. Because \(f(q)=1/p>1\), there is a unique threshold \(z_*(e,h)\) satisfying \(\sum_iw_i f(cz_*+he_i)=f(q)\). The event \(H_r\le p\) is equivalent to \(Z\le z_*(E,h)\), whence
\[
\Pr(H_r\le p)=\mathbb E\,\Phi(z_*(E,h)). \tag{1}
\]
Let \(m=\sum_iw_ie_i\), \(d_i=e_i-m\), \(v=\sum_iw_id_i^2\), and \(M=\max_i|e_i|\). Then \(\sum_iw_id_i=0\). With \(y=cz_*+hm\), the threshold equation becomes
\[
\sum_iw_i f(y+hd_i)=f(q). \tag{2}
\]
By monotonicity, \(y\) lies between \(q-h\max_i d_i\) and \(q-h\min_i d_i\); in particular \(|y-q|\le2hM\). When \(hM\) is sufficiently small (depending only on fixed \(p\)), the derivative \(|f'|\) is bounded below and \(f'',f'''\) are bounded in the relevant compact neighborhood of \(q\). Taylor expansion of (2), using \(\sum_iw_id_i=0\), first yields \(|y-q|\le C_p h^2M^2\). Expanding again gives
\[
0=f'(q)(y-q)+\tfrac12 f''(q)h^2v+O_p(h^3M^3),
\quad
 y=q-\frac{f''(q)}{2f'(q)}h^2v+O_p(h^3M^3). \tag{3}
\]
Differentiating \(f=1/\Phi\) explicitly,
\[
\frac{f''(q)}{-f'(q)}=q+\frac{2\phi(q)}{\Phi(q)}=:R(q).
\]
Since \(c^{-1}=1+h^2/2+O(h^4)\), (3) implies
\[
z_*(e,h)=q-hm+\frac{h^2}{2}\bigl(q+R(q)v\bigr)
+O_p\bigl(h^3(1+M)^3\bigr). \tag{4}
\]
Here and below constants can depend on the fixed dimension and weights. To justify expectations rigorously, restrict first to \(M\le h^{-1/2}\). For sufficiently small \(h\), all Taylor steps apply there and the absolute remainder in (4) has expectation \(O(h^3)\), since Gaussian maxima have finite third moments. Off this event,
\[
\Pr\{M>h^{-1/2}\}\le 2n\exp(-1/(2h)),
\]
and \(\Phi\) is bounded by one. The same Gaussian-tail bound controls the truncated moments used below. Thus (1) and (4), and Taylor's formula for \(\Phi\), imply
\[
\Pr(H_r\le p)=p+\phi(q)\mathbb E(z_*-q)
-\frac{q\phi(q)}2\mathbb E(z_*-q)^2+o(h^2). \tag{5}
\]
The exact Gaussian moment identities are
\[
\mathbb E m=0,\quad \mathbb E m^2=\sum_iw_i^2=:s,
\quad \mathbb E v=1-s.
\]
Substituting them into (4) and then (5) gives
\[
\Pr(H_r\le p)-p
=\frac{h^2\phi(q)}2\bigl[q+R(q)(1-s)-qs\bigr]+o(h^2)
=h^2(1-s)\phi(q)\left(q+\frac{\phi(q)}p\right)+o(h^2).
\]
As \(h^2=1-r\), the asserted limit follows. Finally, \(\phi(q)/\Phi(q)>-q\) for \(q<0\): integrate \(\phi(q)=\int_{-\infty}^q(-t)\phi(t)\,dt\), whose integrand exceeds \((-q)\phi(t)\) except at an endpoint. For \(q\ge0\), positivity of \(q+\phi(q)/\Phi(q)\) is immediate. Since \(s<1\) exactly when at least two weights are positive, strict local inflation follows. This completes the proof.

## Verification
The standalone program `VERIFY.py` numerically evaluates the exact bivariate conditional Gaussian integral for four nondegenerate weight/level combinations and three correlations approaching one. Its twelve comparisons corroborate convergence to the analytical coefficient. Run `python VERIFY.py` with Python, NumPy, and SciPy. The numerical integration is **not** used to prove the universal limit or the strict sign; those follow from the expansion and Gaussian tail argument above.

## Relationship to prior work
Chen, Wang, Wang, and Zhu (first posted 2024; [1]) prove harmonic-mean subuniformity for independence, negative upper-orthant dependence, extremal mixture copulas, and some Clayton copulas. Their Section 7, Figure 1, and conclusion instead give numerical evidence and explicitly leave positive Gaussian correlations unresolved. Their Gaussian parameter is a *factor loading*, so its square is pairwise correlation; the present parameter \(r\) is pairwise correlation. The result here supplies an analytic, all-dimension, all-weight, fixed-level local answer at the comonotonic endpoint, not a result for the entire correlation interval.

Chakraborty, Guo, Shedden, and Stoev [2] study calibration as \(p\downarrow0\) for a fixed dependence structure; that is a different and generally non-interchangeable asymptotic limit. Liu [3] analyzes heavy-tail second-order corrections for fixed Gaussian correlations strictly below one and explicitly notes nonuniform behavior at the perfect-correlation boundary; its Gaussian results therefore do not imply the fixed-level derivative as \(r\uparrow1\). Ordinary normal-Taylor and Gaussian tail estimates are classical tools, not claimed as innovations.

## Limitations
This is pointwise in the significance level: the neighborhood \((r_0(p,w,n),1)\) need not be uniform over \(p\in(0,1)\), over all weights, or in dimension. The result proves neither global subuniformity for any entire nontrivial correlation interval nor monotonicity as a function of correlation away from one. It concerns exact Gaussian copulas and reciprocal (harmonic) aggregation, not other dependence models or other power means. Independent bibliographic priority verification has not been performed; an equivalent earlier perturbative statement could exist under different terminology.

## References
[1] Y. Chen, R. Wang, Y. Wang, W. Zhu, *Sub-uniformity of harmonic mean p-values*, arXiv:2405.01368 (first public version 2024-05-02), later *Canadian Journal of Statistics*, doi:10.1002/cjs.70017. https://arxiv.org/html/2405.01368v2

[2] P. Chakraborty, F. R. Guo, K. Shedden, S. Stoev, *On the Universal Calibration of Heavy-tailed Combination Tests*, arXiv:2509.12066v3 (2026 revision). https://arxiv.org/html/2509.12066v3

[3] T. Liu, *Copula Geometry and Second-Order Calibration of Heavily Right Aggregation*, arXiv:2609.29658v1 (2026), Section 7 and Appendices A–B. https://arxiv.org/pdf/2609.29658
