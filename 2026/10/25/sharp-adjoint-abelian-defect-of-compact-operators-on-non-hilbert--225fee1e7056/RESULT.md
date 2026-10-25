# Sharp adjoint-abelian defect of compact operators on non-Hilbert sequence spaces

## Finding
For every \(2<p<\infty\), on the real or complex classical sequence space \(\ell_p=\ell_p(\mathbb N)\), the nonlinear adjoint-abelian equation \(T'J_p=J_pT\) has a **uniformly sharp quantitative obstruction** on the compact-operator ideal. Write \(p'=p/(p-1)\), and equip the smooth space \(\ell_p\) with its normalized duality map
\[
J_p(x)_j=\|x\|_p^{2-p}|x_j|^{p-2}\overline{x_j}\quad (x\ne0),\qquad J_p(0)=0.
\]
Here \(J_p(x)\) denotes a continuous linear functional on \(\ell_p\), identified with a coefficient vector in \(\ell_{p'}\), and \(T'\) denotes the Banach transpose. Define the nonlinear intertwining defect
\[
\delta_p(T)=\sup_{\|x\|_p=1}\big\|J_p(Tx)-T'J_p(x)\big\|_{p'}.
\]
For every compact linear operator \(T:\ell_p\to\ell_p\),
\[
\boxed{\delta_p(T)\ge c_p\|T\|,\qquad
c_p=\frac{p-2}{p-1}(p-1)^{-1/(p-2)}.}
\]
The constant is **the best possible over all nonzero compact operators**: if \(P_1(x)=x_1e_1\), then \(\|P_1\|=1\) and \(\delta_p(P_1)=c_p\). All nonzero real scalar multiples of \(P_1\) attain equality. In particular \(c_4=2/(3\sqrt3)\), \(c_p\sim(p-2)/e\) as \(p\downarrow2\), and \(c_p\to1\) as \(p\to\infty\).

## Assumptions and scope
The scalar field is either \(\mathbb R\) or \(\mathbb C\). The space is infinite-dimensional \(\ell_p(\mathbb N)\), not finite-dimensional \(\ell_p^d\), and \(2<p<\infty\). Compactness is essential for the bound as stated: for example, the identity operator has zero defect. The normalized duality map is the unique map satisfying \(\|J_p(x)\|_{p'}=\|x\|_p\) and \(J_p(x)(x)=\|x\|_p^2\). The quantity \(\delta_p\) is homogeneous under real scalings of \(T\); for complex scalars the conjugate-homogeneity of the duality map requires retaining the stated complex-linear transpose convention.

## Proof
**Continuity, compactness, and a remote coordinate.** The normalized duality map is norm-to-norm continuous on \(\ell_p\) for \(1<p<\infty\), and satisfies \(J_p(ax)=aJ_p(x)\) for every nonnegative real \(a\). Given \(\varepsilon>0\), choose a finitely supported unit vector \(u\) with \(\|Tu\|_p>\|T\|-\varepsilon\), possible by density. Let \(e_n\) be a canonical unit vector with \(n\) beyond the support of \(u\). Both \(e_n\in\ell_p\) and its coordinate functional \(e_n'\in\ell_{p'}\) converge weakly to zero as \(n\to\infty\). As \(T\) and \(T'\) are compact (the latter by the compact-adjoint theorem),
\[
\|Te_n\|_p\to0,\qquad\|T'e_n'\|_{p'}\to0.
\]

**Exact two-coordinate normalization and lower bound.** Fix \(0<a<1\), put \(b=(1-a^p)^{1/p}\), and let \(u_n=au+be_n\). The supports of \(u\) and \(e_n\) are disjoint, hence \(\|u_n\|_p=1\). The coordinate formula gives the *exact* identity
\[
J_p(u_n)=a^{p-1}J_p(u)+b^{p-1}e_n'.
\]
Consequently \(Tu_n\to aTu\) and, by continuity, \(J_p(Tu_n)\to aJ_p(Tu)\), while \(T'J_p(u_n)\to a^{p-1}T'J_p(u)\). Therefore, by the definition of the defect and the reverse triangle inequality,
\[
\begin{aligned}
\delta_p(T)&\ge\big\|aJ_p(Tu)-a^{p-1}T'J_p(u)\big\|_{p'}\\
&\ge a\|Tu\|_p-a^{p-1}\|T'\|\\
&>a(\|T\|-\varepsilon)-a^{p-1}\|T\|.
\end{aligned}
\]
Let \(\varepsilon\downarrow0\), and maximize over \(a\in[0,1]\). Because \(p>2\), the unique interior maximizing value is \(a_*=(p-1)^{-1/(p-2)}\); at that point
\[
\max_{0\le a\le1}(a-a^{p-1})
=\frac{p-2}{p-1}(p-1)^{-1/(p-2)}=c_p.
\]
This proves the asserted inequality, including \(T=0\) trivially.

**Exact sharpness.** For \(P_1x=x_1e_1\) and any unit \(x\), both \(J_p(P_1x)\) and \(P_1'J_p(x)\) are supported in the first dual coordinate, with respective coefficients \(\overline{x_1}\) and \(|x_1|^{p-2}\overline{x_1}\). Thus
\[
\|J_p(P_1x)-P_1'J_p(x)\|_{p'}=t-t^{p-1},\qquad t=|x_1|\in[0,1].
\]
Every such \(t\) occurs for a unit vector with at most two nonzero coordinates. Its maximum is precisely \(c_p\), completing sharpness. If \(T=rP_1\) for nonzero real \(r\), both terms in the defect scale by \(r\), with the same conclusion.

**Endpoint behavior.** Taking logarithms in the explicit formula gives \(c_p/(p-2)\to e^{-1}\) as \(p\downarrow2\). Both factors tend to one as \(p\to\infty\). At \(p=4\) direct substitution gives \(2/(3\sqrt3)\).

## Verification
The proof uses only norm continuity of the explicit duality map, density of finitely supported vectors, weak nullity of canonical coordinate vectors and their duals, compactness of the Banach adjoint, and a one-variable maximization. The supplementary standalone `CHECKER.py` tests the duality-map normalization, the disjoint-support scaling law, the limiting inequality on finite-rank blocks with unused coordinates, and the sharp coordinate witness at several exponents. No finite-dimensional test is used in place of the compactness argument.

## Relationship to prior work
Stampfli (1969) introduced the adjoint-abelian relation \(T'J=JT\) on Banach spaces. Fleming and Jamison (1977, Section 5, Theorem 5.5) classified exact adjoint-abelian operators on classical \(L_p\) geometries as scalar multiples of involutive isometries; this already rules out nonzero compact exact solutions on infinite \(\ell_p\). **No novelty is claimed for that qualitative consequence.** Shameem's 2026 work studies spectral representations of compact operators satisfying exact duality self-adjointness; our theorem instead determines the best possible *positive norm-distance coefficient of the nonlinear equation* for the entire compact ideal on non-Hilbert \(\ell_p\), with rank-one sharpness. Existing qualitative spectral-projection results for exact solutions do not imply this coefficient. Published work on convex defect norms for band projections concerns a different functional, not the present adjoint-abelian equation.

## Limitations
The inequality is proved only for \(2<p<\infty\) and compact operators on infinite-dimensional classical sequence spaces. The theorem does not assert the same exact coefficient for \(1<p<2\), general \(L_p\)-spaces, all weakly compact operators, or noncompact operators; \(T=I\) disproves an unqualified extension. The historical classification of exact solutions precedes this result; an older equivalent quantitative bound not found in the inspected literature remains a priority risk. No independent validation is claimed.

## References
- M. Shameem, *Spectral theorem for compact self-adjoint operators on smooth Banach spaces*, arXiv:2608.06873, first publicly posted 2026-08-07; version 2 publicly posted 2026-10-15, especially the definition \(T'J=JT\) and spectral representation section. https://arxiv.org/html/2608.06873v2
- J. G. Stampfli, *Adjoint Abelian operators on Banach space*, Canadian Journal of Mathematics 21 (1969), 505–512, definition and Sections I–III. https://doi.org/10.4153/CJM-1969-058-4
- R. J. Fleming and J. E. Jamison, *Classes of operators on vector valued integration spaces*, Journal of the Australian Mathematical Society Series A 24 (1977), 129–138, Section 5, Theorem 5.5. https://doi.org/10.1017/S1446788700020152
- R. J. Fleming and J. E. Jamison, *Hermitian operators and isometries on sums of Banach spaces*, Proceedings of the Edinburgh Mathematical Society 32 (1989), 169–191, Proposition 4.2. https://doi.org/10.1017/S0013091500028583
