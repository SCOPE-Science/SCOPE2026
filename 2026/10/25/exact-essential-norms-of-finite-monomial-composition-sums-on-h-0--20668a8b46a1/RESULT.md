# Exact essential norms of finite monomial-composition sums on \(H^0_{v_\alpha}\)

## Finding
Let \(\alpha>0\), and define the little weighted growth space
\[
X_\alpha=H^0_{v_\alpha}(\mathbb D),\qquad v_\alpha(z)=(1-|z|)^\alpha,
\]
with norm \(\|f\|_\alpha=\sup_{z\in\mathbb D}(1-|z|)^\alpha|f(z)|\) and the condition that \(v_\alpha|f|\) vanishes at the boundary. For \(N\ge3\), distinct positive integers \(m_1,\ldots,m_N\), and nonzero scalars \(a_1,\ldots,a_N\), set
\[
T=\sum_{j=1}^N a_j C_{\phi_j},\qquad \phi_j(z)=z^{m_j},\qquad C_{\phi_j}f=f\circ\phi_j.
\]
Then the exact essential norm is
\[
\boxed{\displaystyle \|T\|_e=\sum_{j=1}^N |a_j|m_j^{-\alpha}.}
\]
Here \(\|T\|_e=\inf\{\|T-K\|:K:X_\alpha\to X_\alpha\text{ compact}\}\). The claim concerns finite sums with at least three active, distinct monomial symbols; it does not assert a formula for arbitrary symbols or infinite sums.

## Assumptions and scope
The unit disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). The parameter \(\alpha\) is any positive real number. The integers \(m_j\) are pairwise distinct and positive, and every coefficient \(a_j\) is nonzero. The space is the little growth space \(H^0_{v_\alpha}\), not an arbitrary weighted analytic space. Compactness and essential norm are taken for bounded linear operators on this Banach space.

## Proof
**1. The single-symbol essential norm.** For \(z=r\eta\), with \(|\eta|=1\), the evaluation norm on \(H^\infty_{v_\alpha}\) is exactly \((1-r)^{-\alpha}\). The upper bound follows from the defining norm. For the reverse bound, the analytic function \(g_\eta(w)=(1-\bar\eta w)^{-\alpha}\), using the analytic branch on \(\mathbb D\), satisfies \(\|g_\eta\|_{v_\alpha}\le1\) and \(|g_\eta(r\eta)|=(1-r)^{-\alpha}\). Hence the associated weight is \(\widetilde v_\alpha=v_\alpha\).

The exact essential-norm formula for composition operators on \(H^0_v\) therefore gives, for each positive integer \(m\),
\[
\|C_{z^m}\|_e=\limsup_{|z|\to1}\left(\frac{1-|z|}{1-|z|^m}\right)^\alpha
=\lim_{r\uparrow1}\left(\frac1{1+r+\cdots+r^{m-1}}\right)^\alpha=m^{-\alpha}.
\]
Subadditivity of the quotient norm modulo compact operators yields
\[
\|T\|_e\le\sum_{j=1}^N |a_j|\|C_{z^{m_j}}\|_e=\sum_{j=1}^N |a_j|m_j^{-\alpha}.
\]

**2. Separated boundary peaks.** Choose \(\zeta\in\partial\mathbb D\) so that the points \(\eta_j=\zeta^{m_j}\) are pairwise distinct; only finitely many roots of unity are forbidden. Let \(r_n\uparrow1\), put \(s_{j,n}=r_n^{m_j}\), \(\delta_n=1-r_n\), \(\varepsilon_n=\sqrt{\delta_n}\), and \(k_n=\lfloor\delta_n^{-1/2}\rfloor\). Then \(\varepsilon_n\to0\), \(k_n\to\infty\), and \(k_n(1-s_{j,n})\to0\) for every \(j\).

For \(w\in\mathbb D\), define
\[
u_{j,n}(w)=(1-\bar\eta_jw)^{-\alpha}
\left(\frac{(1+s_{j,n})(1-\bar\eta_jw)}{1-s_{j,n}\bar\eta_jw}\right)^{\varepsilon_n}
\left(\frac{1+\bar\eta_jw}{2}\right)^{k_n},
\]
with analytic branches on \(\mathbb D\). The elementary inequality
\[
(1+s)|1-u|\le2|1-su|\qquad(|u|\le1,\ 0<s<1)
\]
and \((1-|w|)/|1-\bar\eta_jw|\le1\) imply \(\|u_{j,n}\|_\alpha\le2^{\varepsilon_n}\to1\). For each fixed \(n\), the factor with exponent \(\varepsilon_n>0\) forces \(v_\alpha|u_{j,n}|\to0\) at \(\eta_j\), while the first factor forces weighted vanishing at every other boundary point. Thus \(u_{j,n}\in X_\alpha\). The last factor makes \(u_{j,n}\to0\) locally uniformly, while
\[
v_\alpha(s_{j,n}\eta_j)|u_{j,n}(s_{j,n}\eta_j)|
=\left(\frac{1+s_{j,n}}2\right)^{k_n}\longrightarrow1.
\]

Because the \(\eta_j\) are distinct, the peaks separate: for any unimodular \(\lambda_j\), the sum \(f_n=\sum_{j=1}^N\lambda_j u_{j,n}\) satisfies \(\|f_n\|_\alpha\to1\). Indeed, on a fixed small neighborhood of \(\eta_j\) every other peak tends uniformly to zero in weighted norm; outside the union of these neighborhoods all peaks tend uniformly to zero. At \(s_{j,n}\eta_j\), the \(j\)-th peak has weighted modulus tending to one and every other peak tends to zero.

The sequence \((f_n)\) is weakly null in \(X_\alpha\). To see this, the isometric embedding \(f\mapsto v_\alpha f\) maps \(X_\alpha\) into \(C_0(\mathbb D)\); the images of \(f_n\) are uniformly bounded and pointwise tend to zero. Dominated convergence against every finite measure shows weak convergence to zero in \(C_0(\mathbb D)\), and Hahn–Banach transfers weak convergence to the closed subspace corresponding to \(X_\alpha\). Consequently, every compact \(K:X_\alpha\to X_\alpha\) satisfies \(\|Kf_n\|_\alpha\to0\).

**3. Lower bound.** Take \(\lambda_j=\overline{a_j}/|a_j|\) and \(z_n=r_n\zeta\). The diagonal term of \(T f_n(z_n)\) corresponding to \(j\) has positive phase, and all off-diagonal terms tend to zero because \(\eta_i\ne\eta_j\). Hence
\[
\begin{aligned}
\lim_{n\to\infty}v_\alpha(z_n)|T f_n(z_n)|
&=\sum_{j=1}^N |a_j|\lim_{n\to\infty}
\left(\frac{1-r_n}{1-r_n^{m_j}}\right)^\alpha
\left(\frac{1+r_n^{m_j}}2\right)^{k_n}\\
&=\sum_{j=1}^N |a_j|m_j^{-\alpha}.
\end{aligned}
\]
For every compact \(K\), weak nullity gives \(\|Kf_n\|_\alpha\to0\), while \(\|f_n\|_\alpha\to1\). Therefore
\[
\|T-K\|\ge\limsup_n\|(T-K)f_n\|_\alpha\ge\sum_{j=1}^N|a_j|m_j^{-\alpha}.
\]
Taking the infimum over compact \(K\) proves the reverse inequality and the formula.

## Verification
The associated weight was computed directly from the evaluation norm. The single-symbol essential norm follows from the published boundary formula and the identity \(1-r^m=(1-r)(1+r+\cdots+r^{m-1})\). The lower bound uses an explicit bounded weakly-null sequence; it does not infer an infinite-dimensional conclusion from finite numerical tests. All hypotheses needed for the peak separation—finitely many distinct boundary points, \(\alpha>0\), and finite \(N\)—are stated. No external computation or unproved classification is used.

## Relationship to prior work
The 2022 survey by Bonet states the exact essential-norm formula for a single weighted composition operator on \(H^0_v\), which supplies the upper bound after subadditivity. Bonet, Domański and Lindström (1999) establish essential-norm estimates for composition operators on weighted analytic-function spaces. Wolf's 2009 paper is explicitly about differences of weighted composition operators, so the two-term case is a close antecedent; the claim here is restricted to \(N\ge3\) and uses a simultaneous boundary-peak construction to obtain exact additivity for a finite family of distinct monomial symbols. The accessible abstract of Wolf's paper does not establish whether its full text contains a broader finite-sum statement; that remains a prior-art risk rather than evidence of noncoverage.

## Limitations
The formula is proved only for finite sums of distinct monomial symbols on \(H^0_{v_\alpha}(\mathbb D)\) with the standard power weight and \(\alpha>0\). It does not cover arbitrary analytic symbols, repeated symbols before coefficients are combined, infinite sums, or other weights. The exact single-operator boundary formula is cited from a survey and its underlying 2012 paper's full text was not available in this run; the survey's stated theorem and the direct associated-weight computation are used. The full text of the close 2009 difference-operator paper was not obtained, so a broader theorem there cannot be excluded absolutely.

## References
1. J. Bonet, “Weighted Banach spaces of analytic functions with sup-norms and operators between them: a survey,” *Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A Math.* 116, 184 (2022), first published 2022-09-26. DOI: 10.1007/s13398-022-01323-4, especially Theorem 53.
2. J. Bonet, P. Domański and M. Lindström, “Essential Norm and Weak Compactness of Composition Operators on Weighted Banach Spaces of Analytic Functions,” *Canad. Math. Bull.* 42(2), 139–148 (1999). DOI: 10.4153/CMB-1999-016-X.
3. E. Wolf, “Differences of weighted composition operators between weighted Bergman spaces and weighted Banach spaces of holomorphic functions,” *Mathematica* 51(74), no. 2 (2009), 181–192. The abstract describes essential-norm formulas for differences; the full text was not obtained in this run.
4. O. Hyvärinen, M. Kemppainen, M. Lindström, A. Rautio and E. Saukko, “The Essential Norm of Weighted Composition Operators on Weighted Banach Spaces of Analytic Functions,” *Integral Equations Oper. Theory* 72(2), 151–157 (2012). DOI: 10.1007/s00020-011-1919-7.
