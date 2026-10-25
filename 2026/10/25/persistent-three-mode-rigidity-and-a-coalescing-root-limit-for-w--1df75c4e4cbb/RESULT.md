# Persistent three-mode rigidity and a coalescing-root limit for weighted Bergman quadratics

## Finding

For \(\alpha>-1\), let \(d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\,dA(z)/\pi\) on the unit disk and put \(\beta=\alpha+2>1\). Define the sharp, same-measure, fourth-power quadratic norm
\[
K_\beta=\max_{0\ne p\in\mathrm{span}\{1,z,z^2\}}\frac{\int_{\mathbb D}|p|^4\,d\mu_\alpha}{(\int_{\mathbb D}|p|^2\,d\mu_\alpha)^2}.
\]
Every maximizer \(p(z)=a+bz+cz^2\) has \(abc\ne0\), and its phases obey \(2\arg b\equiv\arg a+\arg c\pmod{2\pi}\). Thus **all three monomials are indispensable**, for every finite admissible weight.

As \(\beta\to\infty\), the sharp norm and its best two-monomial counterpart \(K_\beta^{(2)}\), where at most two of \(a,b,c\) may be nonzero, satisfy
\[
K_\beta=6-\frac{24}{\beta}+\frac{132}{\beta^2}+O(\beta^{-3}),\qquad
K_\beta-K_\beta^{(2)}=\frac{12}{\beta^2}+O(\beta^{-3}).
\]
All sequences of maximizers have the following coefficient-scale law. After scaling and a rotation, write their coefficients as positive real numbers, normalized by \(\|p\|_{L^2(\mu_\alpha)}=1\). Then
\[
\beta a\longrightarrow\sqrt2,\qquad b\longrightarrow2,\qquad \frac{\sqrt2}{\beta}c\longrightarrow1.
\]
Equivalently, if the polynomial is made monic and its coefficient phases are removed by rotation, its rescaled root multiset \(\{\beta z_1,\beta z_2\}\) converges to \(\{-\sqrt2,-\sqrt2\}\). This is a **double-root scaling limit**, not a claim that finite-weight roots are repeated.

## Assumptions and scope

The statement concerns all complex analytic polynomials of degree at most two and the *same* probability-normalized measure in both norms. It does not concern variable exponents with separately adjusted Bergman weights, general analytic functions, or higher-degree polynomials. Here \(K_\beta^{(2)}\) is optimized over the union of the three two-coordinate subspaces. The notation \(O(\beta^{-3})\) means a bound by a constant times \(\beta^{-3}\) for sufficiently large real \(\beta\).

## Proof

**Exact reduction.** Radial orthogonality gives
\[
m_k=\int |z|^{2k}\,d\mu_\alpha=\frac{k!}{\beta(\beta+1)\cdots(\beta+k-1)}\quad(k\ge1),\qquad m_0=1.
\]
The numerator equals \(\|p^2\|_{L^2(\mu_\alpha)}^2\); explicitly,
\[
|a|^4+4m_1|ab|^2+m_2|b^2+2ac|^2+4m_3|bc|^2+m_4|c|^4.
\]
For fixed coefficient magnitudes the only phase-dependent term is \(|b^2+2ac|^2\), maximized when the phases align. Set \(x=|a|\), \(y=\sqrt{m_1}|b|\), \(z=\sqrt{m_2}|c|\) and normalize \(x^2+y^2+z^2=1\). The exact objective becomes
\[
\mathcal N_\beta=x^4+4x^2y^2+4x^2z^2+C_\beta y^4+D_\beta xy^2z+E_\beta y^2z^2+F_\beta z^4,
\]
where
\[
C_\beta=\frac{2\beta}{\beta+1},\quad D_\beta=4\sqrt{C_\beta},\quad E_\beta=\frac{12\beta}{\beta+2},\quad F_\beta=\frac{6\beta(\beta+1)}{(\beta+2)(\beta+3)}.
\]
Continuity on the positive octant sphere proves existence of a maximizer.

**Exclusion of every coordinate face.** If \(x=0\) with \(yz>0\), introducing positive \(x\) increases the objective to first order through \(D_\beta xy^2z\); the same reasoning excludes \(z=0\) with \(xy>0\). If \(y=0\) and \(x^2+z^2=1\), insert \(y^2=t>0\) and scale \((x,z)\) by \(\sqrt{1-t}\). The derivative at \(t=0\) is
\[
4x^2+D_\beta xz+E_\beta z^2-2(x^4+4x^2z^2+F_\beta z^4).
\]
After discarding its nonnegative mixed term, the remainder is exactly
\[
2x^4+(E_\beta-4)x^2z^2+(E_\beta-2F_\beta)z^4>0,
\]
since \(E_\beta-4=8(\beta-1)/(\beta+2)>0\) and \(E_\beta-2F_\beta=24\beta/((\beta+2)(\beta+3))>0\). This also treats the pure \(x\) and pure \(z\) endpoints. At the pure \(y\) endpoint, adding a small squared \(x\)-mass increases the objective with derivative \(4-2C_\beta>0\). Therefore no boundary maximizer exists. With all coordinates nonzero, phase alignment is forced.

**Localization near the top mode.** Put \(t=y^2\) and \(z=\sqrt{1-x^2-t}\), so \(0\le x^2+t\le1\). At the formal \(\beta=\infty\) coefficients \((C,D,E,F)=(2,4\sqrt2,12,6)\), direct expansion gives
\[
\mathcal N_\infty-6=-8x^2+3x^4-4t^2+4\sqrt2 xtz
\le-5x^2-4t^2+4\sqrt2 xt\le-\kappa(x^2+t^2),
\]
where \(\kappa=(9-\sqrt{33})/2>0\) is the smallest eigenvalue of \(\begin{psmallmatrix}5&-2\sqrt2\\-2\sqrt2&4\end{psmallmatrix}\). Thus the unique formal limiting maximizer is \((x,t,z)=(0,0,1)\). For finite large \(\beta\), the exact difference from the pure top mode is
\[
\mathcal N_\beta-F_\beta=(4-2F_\beta)x^2+(E_\beta-2F_\beta)t
 +(F_\beta-3)x^4+(2F_\beta-E_\beta)x^2t
 +(C_\beta-E_\beta+F_\beta)t^2+D_\beta xtz.
\]
Its coefficients differ from their limiting counterparts by \(O(\beta^{-1})\), except the positive linear term in \(t\), which is \(24\beta/((\beta+2)(\beta+3))=O(\beta^{-1})\). Consequently, for some fixed positive constants \(c,B\) and every \(\beta\ge B\),
\[
\mathcal N_\beta-F_\beta\le-c(x^2+t^2)+\frac{B}{\beta}t.
\]
The maximum is at least \(F_\beta\) (test \(p=z^2\)); therefore every maximizer satisfies \(x=O(\beta^{-1})\) and \(t=O(\beta^{-1})\).

**Sharp asymptotics.** Write \(x=u/\beta\), \(t=v/\beta\) with bounded nonnegative \(u,v\). The preceding exact expression and Taylor expansions, uniformly on every bounded parameter rectangle, give
\[
\mathcal N_\beta=F_\beta+\beta^{-2}Q(u,v)+O(\beta^{-3}),\qquad
Q(u,v)=-8u^2+4\sqrt2uv-4v^2+24v.
\]
Equivalently, \(Q(u,v)=48-8(u-\sqrt2v/4)^2-3(v-4)^2\). The strictly concave quadratic has its unique maximum \(48\) at \((u,v)=(\sqrt2,4)\). Comparing maximizers with this test point, compactness implies that *all* optimal pairs converge there. Since \(F_\beta=6-24/\beta+84/\beta^2+O(\beta^{-3})\), the claimed sharp expansion follows. Substituting \(y^2\sim4/\beta\) and the moment normalizations gives \(a\sim\sqrt2/\beta\), \(b\sim2\), \(c\sim\beta/\sqrt2\). Dividing by \(c\), and applying convergence of polynomial root multisets, yields the double-root limit.

**Two-monomial comparison.** For all sufficiently large \(\beta\), the best \((x,y)\)-only fourth moment is below \(2\), the best \((x,z)\)-only moment is \(F_\beta>3\), and the best \((y,z)\)-only moment is attained at
\[
y^2=\frac{E_\beta-2F_\beta}{2(E_\beta-C_\beta-F_\beta)}\in(0,1),\qquad
K_\beta^{(2)}=F_\beta+\frac{(E_\beta-2F_\beta)^2}{4(E_\beta-C_\beta-F_\beta)}.
\]
Here \(E_\beta-C_\beta-F_\beta=2\beta(2\beta^2+13\beta+9)/((\beta+1)(\beta+2)(\beta+3))>0\). The exact expression expands as \(K_\beta^{(2)}=F_\beta+36/\beta^2+O(\beta^{-3})\). Subtraction gives the sharp difference \(12/\beta^2+O(\beta^{-3})\).

## Verification

The standalone `CHECKER.py` verifies radial-moment identities, coefficient algebra and the strict face-variation identities for rational sample weights; it also evaluates the large-weight formulas as a numerical consistency check. These finite tests supplement rather than replace the uniform estimates, compactness, and exact inequalities in the proof.

## Relationship to prior work

Kulikov, *Functionals with extrema at reproducing kernels* (arXiv:2203.12349, first posted 2022-03-23), proves contractivity between Bergman norms with **different weight parameters matched to the exponents** and a convex-functional principle. Melentijević, *Hypercontractive inequalities for weighted Bergman spaces* (arXiv:2211.03655, first posted 2022-11-08), studies the dilation operator and sharp hypercontractive radius; his primary classification is 30H20. Wang and Zhang, *Hypercontractive inequalities and Nikol'skiĭ-type inequalities on weighted Bergman spaces* (arXiv:2505.12760, first posted 2025-05-19), prove sharp dimension-uniform degree-based bounds, not the exact same-measure quadratic optimizer. The previously known unweighted quadratic fourth-moment calculation gives the \(\alpha=0\) special case; it neither proves full-weight mode persistence nor supplies the sharp concentration limit and two-monomial gap. No novelty claim is made for radial moment orthogonality, phase alignment alone, or the existence of maximizers.

## Limitations

No exact finite-\(\beta\) closed form for \(K_\beta\) or uniqueness theorem for its positive coefficient magnitudes is asserted. The coefficient/root law is asymptotic and does not say finite-weight roots coincide. The present priority comparison does not exclude obscure equivalent formulations in older literature. This work has not received independent mathematical validation.

## References

1. A. Kulikov, *Functionals with extrema at reproducing kernels*, arXiv:2203.12349, version 1 dated 2022-03-23. https://arxiv.org/abs/2203.12349
2. P. Melentijević, *Hypercontractive inequalities for weighted Bergman spaces*, arXiv:2211.03655, first public arXiv record 2022-11-08. https://arxiv.org/abs/2211.03655
3. Z. Wang and K. Zhang, *Hypercontractive inequalities and Nikol'skiĭ-type inequalities on weighted Bergman spaces*, arXiv:2505.12760, 2025-05-19. https://arxiv.org/abs/2505.12760
