# Two-dimensional nonnormal shadowing–robustness ratios approach two

## Finding

For every fixed \(0<\varepsilon<1\) and \(K>0\), put
\[
A_{\varepsilon,K}=\begin{pmatrix}1-\varepsilon&K\\0&-1-\varepsilon\end{pmatrix}
\]
on the Euclidean complex plane. Let \(\operatorname{Shad}(A)\) be the optimal uniform two-sided shadowability constant and let \(r_{\mathrm{hyp}}(A)\) be the operator-norm distance to an operator whose spectrum meets the unit circle, as defined below. Then
\[
\boxed{\lim_{K\to\infty}r_{\mathrm{hyp}}(A_{\varepsilon,K})\operatorname{Shad}(A_{\varepsilon,K})=2-\varepsilon.}
\]
In particular, the explicit invertible hyperbolic, nonnormal matrix
\[
A_{1/4,8}=\begin{pmatrix}3/4&8\\0&-5/4\end{pmatrix}
\]
satisfies
\[
r_{\mathrm{hyp}}(A_{1/4,8})\operatorname{Shad}(A_{1/4,8})\geq\frac{56}{39}>\sqrt2.
\]
Thus the sharp \(\sqrt2\) upper estimate valid for normal hyperbolic operators does not extend to all hyperbolic operators, already in complex dimension two. Ratios in this family approach \(2\) by first taking \(K\to\infty\) and then \(\varepsilon\downarrow0\). No general upper bound of \(2\) is asserted.

## Assumptions and scope

All norms on \(\mathbb C^2\) are Euclidean operator/vector norms. Write \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). For an invertible hyperbolic matrix \(A\), define
\[
(\mathcal L_Ax)_n=x_{n+1}-Ax_n,\qquad
\operatorname{Shad}(A)=\|\mathcal L_A^{-1}\|_{\ell^\infty(\mathbb Z,\mathbb C^2)\to\ell^\infty(\mathbb Z,\mathbb C^2)},
\]
and
\[
r_{\mathrm{hyp}}(A)=\inf\{\|E\|_2:\sigma(A+E)\cap\mathbb T\neq\varnothing\}
=\left(\max_{|z|=1}\|(zI-A)^{-1}\|_2\right)^{-1}.
\]
The inverse exists and is bounded for every hyperbolic invertible matrix. For the stated family, \(1-\varepsilon\in(0,1)\) and \(-1-\varepsilon<-1\) are distinct eigenvalues, so all these definitions apply. Its off-diagonal entry is nonzero, hence the displayed matrix is not normal.

## Proof

**1. Spectral splitting.** Set \(a=1-\varepsilon\), \(b=-1-\varepsilon\). The stable and unstable spectral projections are, respectively,
\[
P_s=\frac{A-bI}{a-b}=\begin{pmatrix}1&K/2\\0&0\end{pmatrix},\qquad
P_u=I-P_s=\begin{pmatrix}0&-K/2\\0&1\end{pmatrix}.
\]
They are idempotent, their product vanishes, and \(AP_s=aP_s\), \(AP_u=bP_u\). For any bounded forcing \(e=(e_n)_{n\in\mathbb Z}\), the unique bounded solution to \(x_{n+1}-Ax_n=e_n\) is
\[
x_n=\sum_{j=0}^\infty a^jP_se_{n-1-j}-\sum_{j=0}^\infty b^{-j-1}P_ue_{n+j}.
\tag{1}
\]
Both sums converge uniformly for \(\|e\|_\infty\leq1\); uniqueness follows since a nonzero stable eigenvector explodes under negative iterates and a nonzero unstable eigenvector explodes under positive iterates.

**2. Two-sided shadowability bounds.** If \(\|e\|_\infty\leq1\), then each complex coordinate of every \(e_n\) has absolute value at most \(1\). Formula (1), \(\sum_{j\ge0}a^j=1/\varepsilon\), and \(\sum_{j\ge0}|b|^{-j-1}=1/\varepsilon\) imply
\[
|(x_n)_1|\leq\frac{K+1}{\varepsilon},\qquad
|(x_n)_2|\leq\frac1\varepsilon.
\]
Consequently \(\|x_n\|_2\leq |(x_n)_1|+|(x_n)_2|\leq(K+2)/\varepsilon\), proving the upper bound. For the lower bound choose, at the displayed coordinate \(n=0\), the unit forcing
\[
e_{-1-j}=(0,1),\qquad e_j=(-1)^{j+1}(0,1),\qquad j\geq0.
\]
Substitution in (1) yields \(x_0=(K/\varepsilon,-1/\varepsilon)\). Hence
\[
\frac K\varepsilon\leq\frac{\sqrt{K^2+1}}\varepsilon
\leq\operatorname{Shad}(A_{\varepsilon,K})\leq\frac{K+2}\varepsilon,
\qquad
\lim_{K\to\infty}\frac{\operatorname{Shad}(A_{\varepsilon,K})}{K}=\frac1\varepsilon.
\tag{2}
\]

**3. Exact minimum of the resolvent's off-diagonal denominator.** For \(|z|=1\),
\[
(zI-A)^{-1}=\begin{pmatrix}
(z-a)^{-1}&K((z-a)(z-b))^{-1}\\
0&(z-b)^{-1}
\end{pmatrix}.
\]
Let \(m_\varepsilon=\min_{|z|=1}|z-a|\,|z-b|\). Writing \(c=\operatorname{Re}z\in[-1,1]\), its squared objective is
\[
(1+a^2-2ac)\big(1+(1+\varepsilon)^2+2(1+\varepsilon)c\big).
\]
The coefficient of \(c^2\) is \(-4(1-\varepsilon)(1+\varepsilon)<0\), so this concave quadratic attains its minimum at an endpoint. At \(z=1\) the product of distances is \(\varepsilon(2+\varepsilon)\); at \(z=-1\) it is \(\varepsilon(2-\varepsilon)\). Therefore
\[
\boxed{m_\varepsilon=\varepsilon(2-\varepsilon).}
\tag{3}
\]
Every diagonal part of the resolvent has norm at most \(1/\varepsilon\), while its single upper-right entry has maximal absolute value \(K/m_\varepsilon\). The triangle and reverse triangle inequalities for the operator norm give
\[
\frac K{m_\varepsilon}-\frac1\varepsilon\leq
\max_{|z|=1}\|(zI-A)^{-1}\|_2\leq
\frac K{m_\varepsilon}+\frac1\varepsilon.
\tag{4}
\]
By the resolvent formula for the hyperbolicity margin,
\[
\lim_{K\to\infty}K\,r_{\mathrm{hyp}}(A_{\varepsilon,K})=m_\varepsilon.
\tag{5}
\]
Combining (2), (3), and (5) proves the boxed limit.

**4. A fully explicit finite counterexample.** The right inequality in (4) and the first inequality in (2) imply for every \(K>0\)
\[
r_{\mathrm{hyp}}(A_{\varepsilon,K})\operatorname{Shad}(A_{\varepsilon,K})
\geq\frac{K/\varepsilon}{K/[\varepsilon(2-\varepsilon)]+1/\varepsilon}
=\frac{(2-\varepsilon)K}{K+2-\varepsilon}.
\tag{6}
\]
At \(\varepsilon=1/4\), \(K=8\), the right side equals \(56/39\). Since \(56^2=3136>3042=2\cdot39^2\), it exceeds \(\sqrt2\). The strict normal-class upper bound is therefore inapplicable to this nonnormal family.

## Verification

The projector identities and concavity coefficient were expanded directly; the exact rational calculation \(56/39\) and strict comparison with \(\sqrt2\) can be reproduced by running `python3 verify_bounds.py` using only the standard library. The computational check corroborates finite algebra. The assertions about all \(K\), the bounded bi-infinite inverse, and the limiting products follow from the displayed analytic arguments and are not inferred from finite tests.

## Relationship to prior work

Z. Yuan (2026), *Sharp Shadowability Bounds for Normal Hyperbolic Linear Operators* (doi:10.20944/preprints202609.1610.v1), proves the optimal \(\sqrt2\) upper bound assuming normality and explicitly raises quantitative nonnormal upper bounds as a subsequent question; its general Green-resolvent preliminaries apply here, but its normal-class theorem does not. Morales and Nguyen (2023), *Quantifying the Shadowing Property* (doi:10.1007/s10884-023-10317-8), introduce general shadowability constants and give hyperbolic operator estimates; the available publisher preview does not establish the specific nonnormal ratio, and its full text was not available for complete comparison. Yuan, Xu, and Brzdęk (2025), *On the best Ulam constant and solutions of the higher order linear difference equation with constant coefficients* (doi:10.1007/s00208-025-03280-w), compute best constants in a different scalar, principally one-sided spectral regime; that result does not determine the ratio in (6). Standard formulas for the Green inverse and the complex stability radius are used as background rather than claimed as novel.

## Limitations

This statement gives a concrete failure of the normal-class \(\sqrt2\) bound, a family limit \(2-\varepsilon\), and finite witnesses; it does **not** prove that \(2\) bounds the ratio for arbitrary nonnormal hyperbolic matrices or operators. It does not determine the exact finite-\(K\) shadowability constant. The older Morales–Nguyen article could not be read beyond a publisher-provided preview, leaving a residual originality risk for an equivalent result phrased in Lipschitz-shadowing terminology. The normal-class comparison is in the Euclidean Hilbert norm, not an arbitrary equivalent coordinate norm.

## References

1. Z. Yuan, *Sharp Shadowability Bounds for Normal Hyperbolic Linear Operators*, Preprints.org, first posted September 18, 2026, doi:10.20944/preprints202609.1610.v1, https://www.preprints.org/manuscript/202609.1610.
2. C. A. Morales and T. Nguyen, *Quantifying the Shadowing Property*, Journal of Dynamics and Differential Equations, first published October 20, 2023, doi:10.1007/s10884-023-10317-8.
3. T. Yuan, B. Xu and J. Brzdęk, *On the best Ulam constant and solutions of the higher order linear difference equation with constant coefficients*, Mathematische Annalen (2025), doi:10.1007/s00208-025-03280-w.
