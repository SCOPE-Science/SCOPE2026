# Sharp commutator law for Gaussian thin-rectangle curvature

## Finding

Let \(\Sigma\) be a real positive-definite \(2\times2\) covariance matrix, \(S=\Sigma^{-1}\), and \(A\) a real symmetric \(2\times2\) matrix. For each unit vector \(u\), take a perpendicular unit vector \(v\) and the centered orthogonal rectangle
\[
K_{\varepsilon,u}=\{zu+wv:|z|\le\varepsilon^{-1},\ |w|\le\varepsilon\}.
\]
Let \(\gamma_\Sigma\) be the centered Gaussian probability measure with covariance \(\Sigma\), and define
\[
H_\varepsilon(u)=\left.\frac{d^2}{dt^2}\log\gamma_\Sigma(e^{tA}K_{\varepsilon,u})\right|_{t=0}.
\]
Then \(H_\varepsilon\) converges uniformly over all unoriented axes \(u\) to \(H_0\), with \(H_\varepsilon(u)=H_0(u)+O_{A,\Sigma}(\varepsilon^2)\), and the exact sharp limiting maximum is
\[
\boxed{\max_{u\in\mathbb S^1}H_0(u)=\frac{\|AS-SA\|_F^2}{16\det S}.}
\]
In particular, the sharp thin-rectangle curvature is strictly positive precisely when \(A\) and \(\Sigma\) fail to commute.

There is an exact orientation profile. In an orthonormal eigenbasis of \(A\), write \(A=\operatorname{diag}(a,b)\) and
\[
S=\begin{pmatrix}p&c\\c&q\end{pmatrix},\quad p,q>0,\quad pq>c^2,
\qquad r=\frac{c}{\sqrt{pq}}.
\]
For \(u=(u_1,u_2)\), let \(\phi\) denote the argument of \((\sqrt p\,u_1,\sqrt q\,u_2)\) and set \(w=\sin(2\phi)\). Then
\[
H_0(u)=-\frac{(a-b)^2}{2}\frac{w(w+r)}{(1+rw)^2}.
\]
When \(AS\ne SA\), precisely two unoriented axes attain the maximum, characterized by
\[
\boxed{\sin(2\phi)=-\frac{r}{2-r^2}.}
\]
The unstable directions, meaning \(H_0(u)>0\), are exactly those with \(w\) strictly between \(0\) and \(-r\). Their total angular length in the transformed projective angle \(\phi\in[0,\pi)\) is \(\arcsin|r|\). These are lengths in the transformed angle, not in Euclidean direction angle.

## Assumptions and scope

The theorem holds for every real symmetric \(A\) and every positive-definite real \(\Sigma\), in dimension two only. The matrix norm is the Frobenius norm, \(\|B\|_F^2=\operatorname{tr}(B^TB)\). The Gaussian measure is normalized to total mass one; derivatives concern the logarithm of the Gaussian mass of the **transformed set** \(e^{tA}K_{\varepsilon,u}\). The long half-side is exactly \(\varepsilon^{-1}\), the short half-side exactly \(\varepsilon\). For commuting \(A,S\), the maximum is zero; no uniqueness assertion is made in that case.

## Proof

**1. Gaussian second variation and line limit.** By the change of variables \(x=e^{tA}y\),
\[
\gamma_\Sigma(e^{tA}K)=C_\Sigma e^{t\operatorname{tr}A}
\int_K\exp\left[-\tfrac12\langle e^{tA}Se^{tA}y,y\rangle\right]dy.
\]
Differentiating twice at \(t=0\) shows, for the probability measure \(\mu_{K,\Sigma}\) obtained by restricting and renormalizing \(\gamma_\Sigma\) to \(K\),
\[
(\log\gamma_\Sigma(e^{tA}K))''\big|_0=
\operatorname{Var}_{\mu_{K,\Sigma}}(\langle ASy,y\rangle)
-\mathbb E_{\mu_{K,\Sigma}}\langle(A^2S+ASA)y,y\rangle.
\]
Set \(\alpha=\langle Su,u\rangle\), \(\beta=\langle ASu,u\rangle\), and \(\zeta=\langle(A^2S+ASA)u,u\rangle\). Under the normalized Gaussian restriction to \(K_{\varepsilon,u}\), all polynomial moments of degrees at most four converge to those of \(Zu\), where \(Z\sim N(0,\alpha^{-1})\). Therefore
\[
H_0(u)=\frac{2\beta^2-\alpha\zeta}{\alpha^2}.
\]
This convergence is uniform with error \(O_{A,\Sigma}(\varepsilon^2)\): in coordinates \((z,w)\) on the rectangle, extend the \(z\)-integral to \(\mathbb R\) with a uniformly Gaussian-small tail, Taylor-expand the polynomial-times-Gaussian integrand in \(w\), and integrate symmetrically over \([-\varepsilon,\varepsilon]\). The odd first-order term vanishes, and the second derivative has a common integrable Gaussian majorant (uniform in \(u\in\mathbb S^1\)); the normalizing integral divided by \(2\varepsilon\) stays uniformly bounded away from zero. Hence all moment ratios, and therefore \(H_\varepsilon\), have the asserted uniform \(O(\varepsilon^2)\) error.

**2. Algebraic factorization.** Orthogonal diagonalization of \(A\) does not change the maximum or the claimed commutator quotient. Writing \(u=(x,y)\) in that basis gives
\[
\begin{aligned}
\alpha&=px^2+2cxy+qy^2,\\
\beta&=apx^2+(a+b)cxy+bqy^2,\\
\zeta&=2a^2px^2+(a+b)^2cxy+2b^2qy^2.
\end{aligned}
\]
Direct expansion yields the exact polynomial identity
\[
\alpha\zeta-2\beta^2=(a-b)^2xy\,[c(px^2+qy^2)+2pqxy].
\]
Set \(T=px^2+qy^2>0\), \(r=c/\sqrt{pq}\) and \(w=2\sqrt{pq}\,xy/T\in[-1,1]\). Then \(\alpha=T(1+rw)\) and
\[
H_0(u)=-\frac{(a-b)^2}{2}\frac{w(w+r)}{(1+rw)^2}.
\]
Every \(w\in[-1,1]\) is realized by some unoriented axis because \(w=\sin(2\phi)\) for \(\phi=\arg(\sqrt p\,x,\sqrt q\,y)\).

**3. Sharp square identity and equality.** Since \(|r|<1\), the exact identity
\[
4(1-r^2)w(w+r)+r^2(1+rw)^2=((2-r^2)w+r)^2
\]
implies the global sharp upper bound
\[
H_0(u)=\frac{(a-b)^2r^2}{8(1-r^2)}-
\frac{(a-b)^2((2-r^2)w+r)^2}{8(1-r^2)(1+rw)^2}.
\]
Equality holds at \(w=-r/(2-r^2)\). For \(a\ne b\) and \(r\ne0\), this lies strictly between \(-1\) and \(1\), so there are exactly two projective angles giving equality. Moreover \(\|AS-SA\|_F^2=2(a-b)^2c^2\) and \(\det S=pq-c^2\), giving the stated invariant maximum. If \(AS=SA\), the maximum is zero, attained by eigendirections when \(A\) has distinct eigenvalues, and identically if \(A\) is scalar.

**4. Full instability region.** The denominator of the orientation profile is positive. Thus \(H_0(u)>0\) exactly when \(w(w+r)<0\), i.e. \(w\) lies strictly between \(0\) and \(-r\). As \(w=\sin 2\phi\), these comprise two arcs of angular length \(\tfrac12\arcsin|r|\) each in the projective transformed angle \(\phi\in[0,\pi)\), proving the total length.

## Verification

Run `python3 verify.py` from the directory containing the files. The pure-standard-library checker expands the seven-variable polynomial factorization coefficient-by-coefficient, checks the sharp square identity as a formal polynomial, and tests the exact rational instance \(S=\left(\begin{smallmatrix}1&-1/2\\-1/2&1\end{smallmatrix}\right)\), \(A=\operatorname{diag}(1,-1)\), whose sharp maximum is \(1/6\) and optimum transformed angle satisfies \(\sin2\phi=2/7\). Auxiliary finite-width quadrature approaches \(1/6\). Universal statements are proved analytically above; numerical tests alone are not proofs.

## Relationship to prior work

Kalantzopoulos's arXiv:2610.07248v1 derives the Gaussian quadratic-form second variation, proves a qualitative commutativity criterion for arbitrary orthogonal boxes, and gives one two-dimensional angular counterexample. This result uses those formulas and the thin-rectangle mechanism, but supplies an additional exact **basis-invariant optimized magnitude**, a sum-of-squares angular deficit, all equality directions and an exact instability-angle measure for arbitrary planar matrices. The stated published criterion alone provides positivity/nonpositivity, not the numerical optimum and equality portrait. Cordero-Erausquin--Rotem (2020) supplies an earlier qualitative counterexample scheme, not the general planar sharp profile. Putterman's 2026 stability paper concerns near-equality in the positive Gaussian (B)-theorem regime, not this identified negative-curvature orientation problem, although full-text overlap risk remains.

## Limitations

Only planar orthogonal rectangles collapsing to a Gaussian line are optimized. No maximization over all convex bodies is asserted; the theorem does not provide an explicit uniform finite-width positivity threshold or settle any global logarithmic Brunn--Minkowski conjecture. The \(O(\varepsilon^2)\) constant depends on \(A\) and \(\Sigma\). Search-based originality assessment cannot exclude unindexed calculations, and the entire 2026 stability preprint was not inspected.

## References

- P. Kalantzopoulos, *Commutativity in a Poincaré-Type Inequality*, arXiv:2610.07248v1 (first submitted 2026-10-05), https://arxiv.org/html/2610.07248v1. The derivative formula, thin-box reduction and qualitative commutation criterion are the starting points.
- D. Cordero-Erausquin and L. Rotem, *Several results regarding the (B)-conjecture*, Geometric Aspects of Functional Analysis I (2020), pp. 247–262, https://webusers.imj-prg.fr/~dario.cordero/Docs/articles/B-note-gafa.pdf. A precursor to the thin-box counterexample mechanism.
- E. Putterman, *Sharp stability for the (B)-theorem*, arXiv:2608.08472 (2026), https://arxiv.org/abs/2608.08472. Background on positive stability, not a known formula for the negative-curvature directional supremum.
