# Exact parametric almost-squareness phase diagram for \(\ell_p(\Gamma)\)
## Finding
Let \(\Gamma\) be an infinite set, let \(2\le p<\infty\), and let \(r,s\in(0,1]\). Recall that a real Banach space \(X\) is \((r,s)\)-\(\mathrm{SQ}_{<\aleph_0}\) when for every finite set \(A\subset S_X\) there is \(y\in S_X\) such that \(\|rx\pm sy\|\le1\) for every \(x\in A\).

Then \(\ell_p(\Gamma)\) is \((r,s)\)-\(\mathrm{SQ}_{<\aleph_0}\) exactly in the following cases:

\[
\begin{array}{c|c}
\text{case} & \text{exact condition}\\ \hline
p=2 & r^2+s^2\le1,\\
p>2\text{ and }\Gamma\text{ uncountable} & r^p+s^p\le1,\\
p>2\text{ and }\Gamma\text{ countably infinite} & r^p+s^p<1.
\end{array}
\]

Thus for \(p>2\) the boundary \(r^p+s^p=1\) detects a genuine separability change: it is attained on uncountable \(\ell_p(\Gamma)\) and fails on ordinary separable \(\ell_p\). At \(p=2\), orthogonality removes that boundary defect.

## Assumptions and scope
All spaces and scalars are real. The index set \(\Gamma\) is infinite, \(2\le p<\infty\), and \(r,s\in(0,1]\). The statement concerns the finite-set parametric property \(\mathrm{SQ}_{<\aleph_0}\), not the transfinite version with larger test sets. No assertion is made for \(1\le p<2\), for complex scalars, or for finite-dimensional \(\ell_p\).

The proof uses only the scalar Clarkson inequality, countability of supports in \(\ell_p(\Gamma)\), vanishing of coordinates in separable \(\ell_p\), and Hilbert-space orthogonality at \(p=2\).

## Proof
First record a scalar inequality with its equality case. For \(p\ge2\), put \(q=p/2\ge1\). For real \(a,b\), convexity of \(t\mapsto t^q\) and the identity \(|a+b|^2+|a-b|^2=2(a^2+b^2)\) give
\[
|a+b|^p+|a-b|^p
\ge 2(a^2+b^2)^q
\ge 2(|a|^p+|b|^p).
\]
The second inequality is \((u+v)^q\ge u^q+v^q\) for \(u,v\ge0\). If \(p>2\), then \(q>1\), and equality throughout holds exactly when \(ab=0\). If \(p=2\), equality always holds.

For necessity, suppose \(\ell_p(\Gamma)\) is \((r,s)\)-\(\mathrm{SQ}_{<\aleph_0}\). Apply the property to any one-point set \(\{x\}\subset S_{\ell_p(\Gamma)}\), obtaining \(y\in S_{\ell_p(\Gamma)}\) with both \(\|rx+sy\|_p\le1\) and \(\|rx-sy\|_p\le1\). Summing the scalar inequality over \(\Gamma\) yields
\[
2\ge \|rx+sy\|_p^p+\|rx-sy\|_p^p
\ge2(r^p+s^p),
\]
so \(r^p+s^p\le1\). In particular, for \(p=2\) this is \(r^2+s^2\le1\).

Assume now \(p=2\) and \(r^2+s^2\le1\). Given finite \(A\subset S_{\ell_2(\Gamma)}\), the span of \(A\) is finite-dimensional. Since \(\Gamma\) is infinite, choose \(y\in S_{\ell_2(\Gamma)}\) orthogonal to that span. Then for every \(x\in A\),
\[
\|rx\pm sy\|_2^2=r^2+s^2\le1.
\]
This proves the Hilbert case.

Next assume \(p>2\), \(\Gamma\) is uncountable, and \(r^p+s^p\le1\). Every element of \(\ell_p(\Gamma)\) has countable support. Hence a finite set \(A\subset S_{\ell_p(\Gamma)}\) has a countable union of supports, so there is \(\gamma\in\Gamma\) outside all of them. Taking \(y=e_\gamma\), for every \(x\in A\) we have disjoint supports and therefore
\[
\|rx\pm sy\|_p^p=r^p+s^p\le1.
\]
Thus the entire closed \(p\)-ball in the parameter plane is attained in the uncountable case.

Now let \(p>2\), let \(\Gamma\) be countably infinite, and assume the strict inequality \(r^p+s^p<1\). After identifying \(\Gamma\) with \(\mathbb N\), fix finite \(A\subset S_{\ell_p}\). For each sign define
\[
F_\pm(a)=r^p(1-|a|^p)+|ra\pm s|^p.
\]
Both functions are continuous and satisfy \(F_\pm(0)=r^p+s^p<1\). Hence there is \(\delta>0\) such that \(|a|<\delta\) implies \(F_\pm(a)\le1\) for both signs. Every \(x\in\ell_p\) has \(x_n\to0\), so by finiteness of \(A\) one can choose \(n\) with \(|x_n|<\delta\) for every \(x\in A\). With \(y=e_n\),
\[
\|rx\pm sy\|_p^p
=r^p(1-|x_n|^p)+|rx_n\pm s|^p
=F_\pm(x_n)\le1
\]
for every \(x\in A\). This proves sufficiency in the strict interior.

It remains to exclude the boundary in countable \(\ell_p\) when \(p>2\). Assume \(r^p+s^p=1\), and choose a unit vector \(x\in\ell_p\) whose every coordinate is nonzero; for instance, normalize the sequence \((2^{-n})_{n\ge1}\). If a unit vector \(y\) satisfied \(\|rx\pm sy\|_p\le1\), then the summed scalar Clarkson inequality would have lower bound \(2(r^p+s^p)=2\) while the two norm bounds give upper bound \(2\). Hence equality must hold in the scalar inequality at every coordinate. Because \(p>2\), equality forces \((rx_n)(sy_n)=0\) for every \(n\). Since \(r,s>0\) and every \(x_n\ne0\), this gives \(y_n=0\) for every \(n\), contradicting \(\|y\|_p=1\). Thus the boundary fails in the countably infinite case, completing the classification.

## Verification
The proof is self-contained apart from standard definitions. The scalar Clarkson inequality and its strict equality condition are derived directly above from convexity and superadditivity, so the boundary argument does not rely on an unstated equality theorem.

A standalone script, `verify.py`, numerically checks the scalar inequality and strictness on a deterministic grid for representative real exponents, checks the disjoint-support identity, and checks the one-coordinate construction formula. Its successful output is `VERIFY_OK`. These finite checks are sanity tests only; the infinite-dimensional statement is proved analytically.

## Relationship to prior work
Oja, Saealle, and Zolk introduced the one-parameter quantitative \(s\)-ASQ notion in 2020. Avilés, Ciaci, Langemets, Lissitsin, and Rueda Zoca introduced the two-parameter \((r,s)\)-\(\mathrm{SQ}_{<\kappa}\) property in 2022. Their Definition 6.1 is the definition used here, and their Remark 6.2 identifies the earlier \(s\)-ASQ notion with an approximate two-parameter form.

The 2022 paper also proves, for an infinite cardinal \(\kappa\) and integer \(n\), the specific point that \(\ell_n(\kappa)\) is \((2^{-1/n},2^{-1/n})\)-\(\mathrm{SQ}_{<\kappa}\) in the uncountable-support argument, and it notes that the countable case only gives an approximate witness in that proof. The present result classifies the full parameter region for every real \(p\ge2\) at the ordinary finite-set level, and identifies the exact open-versus-closed boundary distinction between countable and uncountable index sets when \(p>2\).

Bibliographic and exact web searches for the full \(\ell_p(\Gamma)\) parameter region, the countable/uncountable boundary, and quantitative almost squareness located the 2022 transfinite paper but no source stating this classification or a stronger theorem that implies it.

## Limitations
The result does not classify \((r,s)\)-\(\mathrm{SQ}_{<\aleph_0}\) for \(1\le p<2\), complex \(\ell_p\), finite-dimensional \(\ell_p\), or transfinite test families of cardinality beyond the finite level. The literature comparison is strongest against the inspected 2020 and 2022 primary texts and database searches; differently named equivalent formulations elsewhere remain a residual bibliographic risk.

## References
1. E. Oja, N. Saealle, and I. Zolk, “Quantitative versions of almost squareness and diameter 2 properties,” Acta et Commentationes Universitatis Tartuensis de Mathematica 24 (2020), 131–145. DOI: 10.12697/ACUTM.2020.24.09.
2. A. Avilés, S. Ciaci, J. Langemets, A. Lissitsin, and A. Rueda Zoca, “Transfinite almost square Banach spaces,” arXiv:2204.13449v1, 28 April 2022.
