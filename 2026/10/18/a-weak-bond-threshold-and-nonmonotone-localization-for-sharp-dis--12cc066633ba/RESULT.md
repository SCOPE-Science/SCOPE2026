# A weak-bond threshold and nonmonotone localization for sharp discrete Sobolev embedding

## Finding
Let \(\tau>0\). For a complex sequence \(u\in\ell^2(\mathbb Z)\), set
\[
E_\tau(u)=\sum_{n\in\mathbb Z\setminus\{0\}}|u_{n+1}-u_n|^2+\tau|u_1-u_0|^2,
\quad
C_\tau=\sup_{u\ne0}\frac{\|u\|_\infty^2}{\|u\|_2\sqrt{E_\tau(u)}}.
\]
The exact sharp constant is \(C_\tau=1\) for \(\tau\ge1\), and this value is never attained by a nonzero sequence. For \(0<\tau<1\), put
\[
r_\tau=\frac{2}{2-\tau+\sqrt{\tau(8-7\tau)}},\qquad
C_\tau=\frac{2\sqrt{r_\tau}[1+(\tau-1)r_\tau]}{1+(2\tau-1)r_\tau}>1.
\]
Here the supremum is attained; up to a nonzero complex scalar and reflection \(n\mapsto1-n\), every extremizer has the explicit form
\[
u_n=\begin{cases}
r_\tau^{-n},&n\le0,\\[2pt]
\displaystyle\frac{\tau r_\tau}{1+(\tau-1)r_\tau}\,r_\tau^{n-1},&n\ge1.
\end{cases}
\]
The sharp constant decreases strictly as \(\tau\) increases from zero to one, with
\[
C_\tau=2-2\sqrt{2\tau}+O(\tau)\quad(\tau\downarrow0),
\qquad C_\tau=1+\frac{(1-\tau)^2}{2}+O((1-\tau)^3)\quad(\tau\uparrow1).
\]
Although the embedding constant changes monotonically, the extremizers' geometric decay ratio \(r_\tau\) does not. It decreases then increases, and has the unique minimum
\[
\tau_{\mathrm{loc}}=\frac{4-\sqrt2}{7},\qquad
r_{\tau_{\mathrm{loc}}}=4\sqrt2-5.
\]
Thus a defect of intermediate strength produces the most spatially concentrated sharp extremizers; concentration is lost both near the intact bond and near complete disconnection.

## Assumptions and scope
All norms are unweighted counting-measure norms on the bi-infinite lattice \(\mathbb Z\). The only nonunit edge conductance is the bond \(\{0,1\}\); \(\tau=0\) is excluded. The sequence and energy may be complex, with the same conclusions for real sequences. The inequality is homogeneous and its sharp constant is defined over all nonzero \(\ell^2\) sequences. The ratio above is well-defined because \(E_\tau(u)=0\) forces an \(\ell^2\) sequence to vanish.

## Proof
**1. Reproducing-resolvent reduction.** Let \(L_\tau\) be the nonnegative bounded self-adjoint weighted graph Laplacian with quadratic form \(E_\tau\). For \(\lambda>0\) and \(j\in\mathbb Z\), let
\[
G_{\tau,j}(\lambda)=\langle\delta_j,(L_\tau+\lambda I)^{-1}\delta_j\rangle.
\]
The Cauchy--Schwarz reproducing-kernel inequality, with equality only for multiples of \((L_\tau+\lambda I)^{-1}\delta_j\), gives
\[
|u_j|^2\le G_{\tau,j}(\lambda)[E_\tau(u)+\lambda\|u\|_2^2].
\]
For any nonzero \(u\), minimizing the bracket divided by \(2\sqrt\lambda\) yields \(\|u\|_2\sqrt{E_\tau(u)}\). Interchanging the two suprema therefore gives the **exact identity**
\[
C_\tau=\sup_{j\in\mathbb Z}\sup_{\lambda>0}2\sqrt\lambda\,G_{\tau,j}(\lambda).
\tag{1}
\]

**2. Exact diagonal and location.** Parameterize \(\lambda=(1-r)^2/r\), \(0<r<1\). The unperturbed resolvent has kernel
\[
g_\lambda(i,j)=\frac{r^{|i-j|+1}}{1-r^2}.
\]
Writing \(v=\delta_0-\delta_1\), we have \(L_\tau=L_1+(\tau-1)|v\rangle\langle v|\). A direct rank-one resolvent identity gives, with \(k(j)=\min(|j|,|j-1|)\),
\[
G_{\tau,j}(\lambda)=\frac{r}{1-r^2}-\frac{(\tau-1)r^{2+2k(j)}}{(1+r)[1+(2\tau-1)r]}.
\tag{2}
\]
The denominator is strictly positive since \(\tau>0\) and \(0<r<1\). For \(0<\tau<1\), the diagonal is largest at exactly \(j=0\) and \(j=1\), while for \(\tau>1\) every diagonal is at most the unweighted diagonal. At the bond endpoint, equation (2) reduces to
\[
G_{\tau,0}(\lambda)=\frac{r[1+(\tau-1)r]}{(1-r)[1+(2\tau-1)r]},\quad
2\sqrt\lambda G_{\tau,0}(\lambda)=K_\tau(r):=\frac{2\sqrt r[1+(\tau-1)r]}{1+(2\tau-1)r}.
\tag{3}
\]

**3. Sharp bond threshold.** For \(0<\tau<1\), direct differentiation of equation (3) shows that the sign of \(K_\tau'(r)\) is the sign of
\[
P_\tau(r)=1+(\tau-2)r+(\tau-1)(2\tau-1)r^2.
\tag{4}
\]
Since \(P_\tau(0)=1\) and \(P_\tau(1)=2\tau(\tau-1)<0\), the quadratic has exactly one zero in \((0,1)\): for \(\tau<1/2\), its other zero is greater than one; for \(\tau>1/2\), its other zero is negative; and for \(\tau=1/2\), it is linear. Solving gives precisely \(r_\tau\) above. Thus \(K_\tau\) has its unique global maximum at \(r_\tau\), exceeding its limiting value \(1\) as \(r\uparrow1\). Equation (1) yields the stated sharp constant. Moreover,
\[
\frac{\partial K_\tau(r)}{\partial\tau}
=-\frac{2r^{3/2}(1-r)}{[1+(2\tau-1)r]^2}<0
\]
for every \(0<r<1\), proving strict decrease of \(C_\tau\) on \((0,1)\).

For \(\tau\ge1\), equation (2) bounds every diagonal by the free diagonal, so (1) yields \(C_\tau\le\sup_{0<r<1}2\sqrt r/(1+r)=1\). To establish sharpness, take free geometric profiles \(u_n=r^{|n-j|}\), translate \(j\) arbitrarily far from the defect, then let \(r\uparrow1\). Their ratio tends to \((1+r)/\sqrt{2(1+r^2)}\to1\). Equality is impossible for any nonzero \(u\): the supremum \(\|u\|_\infty\) is attained at some finite coordinate \(j\), and the reproducing bound at \(\lambda=E_\tau(u)/\|u\|_2^2>0\) is strictly below \(\|u\|_2\sqrt{E_\tau(u)}\), because \(2\sqrt\lambda G_{\tau,j}(\lambda)<1\).

**4. Exact extremizers.** For \(0<\tau<1\), equality in (1) requires \(j\in\{0,1\}\), \(r=r_\tau\), and equality in the reproducing Cauchy--Schwarz estimate. Conversely, at this maximizing parameter, differentiating \(2\sqrt\lambda G_{\tau,0}(\lambda)\) gives \(G_{\tau,0}(\lambda)=2\lambda\|(L_\tau+\lambda I)^{-1}\delta_0\|_2^2\). Consequently the Green profile has \(E_\tau(u)=\lambda\|u\|_2^2\), so its multiplicative inequality is also an equality. Solving the two vertex recurrence equations gives the displayed two-sided geometric profile. Reflection across the bond provides the only other family. The strict spatial dominance in (2), combined with \(C_\tau>1\), excludes limiting maximizers away from the bond.

**5. Localization and boundary expansions.** The critical-point equation (4) and its \(\tau\)-derivative give \(1+(4\tau-3)r=0\) at any interior stationary point of \(r_\tau\). Eliminating \(r\) yields \(7\tau^2-8\tau+2=0\). Exactly one root lies in the admissible range with positive \(r\), namely \(\tau_{\mathrm{loc}}=(4-\sqrt2)/7\), where \(r=4\sqrt2-5\). The derivative of \(r_\tau\) is negative near zero and positive near one, so this unique critical point is its strict minimum. Expanding the radical in \(r_\tau\) and then (3) proves the two stated asymptotic formulas.

## Verification
The standalone script `verify.py` checks the rank-one resolvent identity and recurrence equations symbolically; factors the critical-point derivative; verifies the localization stationary values and both edge expansions; compares the formula with direct energy ratios of truncated Green sequences, scalar numerical optimization, and independently inverted finite Jacobi sections. Its finite calculations test the algebra but are not substitutes for Steps 1--5.

## Relationship to prior work
Ilyin, Laptev and Zelik [1] derive the sharp homogeneous-lattice first-difference interpolation inequality and its explicit free Green function. The free equality threshold \(C_1=1\) is their result and is not newly claimed. Ilyin and Zelik [2] establish a Green-function approach to sharp pointwise Sobolev inequalities in continuum settings. The new object here is a lattice with one variable bond conductance: the exact sharp constant, strict attainment transition, complete defect-localized extremizers, weak-defect asymptotics, and nonmonotone localization parameter are not asserted in those inspected works.

## Limitations
The theorem concerns the single-bond, bi-infinite, nearest-neighbor \(\ell^2\) interpolation inequality only. It neither classifies multiple defects nor claims sharp results for higher lattice dimensions or other interpolation exponents. The result is analytically proved here, but equivalent prior formulations under weighted Jacobi or graph-Sobolev terminology have not been conclusively excluded by an independent literature audit.

## References
[1] A. Ilyin, A. Laptev, S. Zelik, *Sharp interpolation inequalities for discrete operators and applications*, arXiv:1407.0675v1, first publicly posted 2014-07-02; Sections 1--2, especially formulas (1.1), (2.17), (2.18), and Theorem 2.1. https://arxiv.org/abs/1407.0675

[2] A. A. Ilyin, S. V. Zelik, *Green's function asymptotics and sharp point-wise interpolation inequalities*, arXiv:1303.0957v1, first publicly posted 2013-03-05; introduction and general Green-function theory. https://arxiv.org/abs/1303.0957
