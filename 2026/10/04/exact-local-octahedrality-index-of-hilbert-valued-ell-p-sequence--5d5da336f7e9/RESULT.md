# Exact local-octahedrality index of Hilbert-valued \(\ell_p\) sequence spaces
## Finding
Let \(H\) be a real Hilbert space with \(\dim H\ge 2\), let \(\Gamma\) be an infinite set, and let \(1\le p<\infty\). Put
\[
Z=\ell_p(\Gamma;H)=\left(\bigoplus_{\gamma\in\Gamma}H\right)_p.
\]
For a Banach space \(X\), use the local-octahedrality index
\[
s(X)=\sup\left\{c\in[0,2]:\forall x\in S_X\;\forall\varepsilon>0\;\exists y\in S_X,\ \min\{\|x+y\|,\|x-y\|\}\ge c-\varepsilon}\right\}.
\]
Then
\[
s(Z)=2^{1/\min\{p,2\}}=
\begin{cases}
2^{1/p},&1\le p\le2,\\
\sqrt2,&2\le p<\infty.
\end{cases}
\]
Thus the exact quantitative local-octahedrality threshold has a sharp transition at \(p=2\). In particular, for \(p>2\) a Hilbert fibre of dimension at least two raises the value to \(\sqrt2\), whereas the scalar atomic \(\ell_p\) value can be only \(2^{1/p}\).

## Assumptions and scope
The scalar field is real. The index set \(\Gamma\) is infinite, the fibre \(H\) is Hilbert with \(\dim H\ge2\), and \(1\le p<\infty\). No assertion is made here for finite \(\Gamma\) when \(p<2\), for one-dimensional fibres, or for \(p=\infty\).

Every element of \(\ell_p(\Gamma;H)\) has the usual summable coordinate-norm family. In particular, for every \(x\in S_Z\) and every \(\eta>0\), all but finitely many coordinates satisfy \(\|x_\gamma\|<\eta\).

## Proof
Fix \(x=(x_\gamma)\in S_Z\).

First suppose \(p\ge2\). For each coordinate with \(x_\gamma\ne0\), choose \(u_\gamma\in H\) orthogonal to \(x_\gamma\) and satisfying \(\|u_\gamma\|=\|x_\gamma\|\); set \(u_\gamma=0\) when \(x_\gamma=0\). The hypothesis \(\dim H\ge2\) makes these choices possible. Then \(u=(u_\gamma)\in S_Z\), and the Pythagorean identity gives, coordinate by coordinate,
\[
\|x_\gamma\pm u_\gamma\|^2=2\|x_\gamma\|^2.
\]
Hence
\[
\|x\pm u\|_p^p=2^{p/2}\sum_{\gamma\in\Gamma}\|x_\gamma\|^p=2^{p/2},
\]
so both norms equal \(\sqrt2\). Therefore \(s(Z)\ge\sqrt2\) for \(p\ge2\).

Now suppose \(1\le p\le2\). Given \(\eta>0\), choose \(\gamma_0\in\Gamma\) with \(a:=\|x_{\gamma_0}\|<\eta\). Choose a unit vector \(v\in H\) orthogonal to \(x_{\gamma_0}\) and let \(y\in S_Z\) be supported only at \(\gamma_0\), with \(y_{\gamma_0}=v\). Again by the Pythagorean identity,
\[
\|x\pm y\|_p^p=1-a^p+(1+a^2)^{p/2}.
\]
As \(a\to0\), the right-hand side tends to \(2\). Since \(\eta\) can be arbitrarily small, for every \(\varepsilon>0\) one can choose \(y\) so that both norms are at least \(2^{1/p}-\varepsilon\). Thus \(s(Z)\ge2^{1/p}\) for \(1\le p\le2\).

For the matching upper bound, fix a coordinate \(\gamma_0\) and a unit vector \(h\in H\), and let \(e\in S_Z\) be supported at \(\gamma_0\) with \(e_{\gamma_0}=h\). Take arbitrary \(y\in S_Z\), set \(a=\|y_{\gamma_0}\|\in[0,1]\), and put
\[
T=\sum_{\gamma\ne\gamma_0}\|y_\gamma\|^p=1-a^p.
\]
The parallelogram law in \(H\) gives
\[
\|h+y_{\gamma_0}\|^2+\|h-y_{\gamma_0}\|^2=2(1+a^2),
\]
so
\[
\min\{\|h+y_{\gamma_0}\|,\|h-y_{\gamma_0}\|\}\le\sqrt{1+a^2}.
\]
Consequently
\[
\min\{\|e+y\|_p,\|e-y\|_p\}^p
\le 1-a^p+(1+a^2)^{p/2}.
\]
Write \(g_p(a)=(1+a^2)^{p/2}-a^p\). For \(a>0\),
\[
g_p'(a)=pa\left((1+a^2)^{(p-2)/2}-a^{p-2}\right).
\]
If \(1\le p<2\), then \(g_p\) is decreasing and its maximum on \([0,1]\) is \(g_p(0)=1\). If \(p=2\), it is identically \(1\). If \(p>2\), it is increasing and its maximum is \(g_p(1)=2^{p/2}-1\). Therefore every \(y\in S_Z\) satisfies
\[
\min\{\|e+y\|_p,\|e-y\|_p\}
\le
\begin{cases}
2^{1/p},&1\le p\le2,\\
\sqrt2,&p\ge2.
\end{cases}
\]
This yields the required upper bounds and completes the proof.

## Verification
The argument is entirely analytic. The two critical checks are the coordinatewise Pythagorean construction for the lower bound and the monotonicity of
\[
a\longmapsto(1+a^2)^{p/2}-a^p
\]
for the upper bound. The derivative changes sign exactly at \(p=2\) in the stated way. No finite experiment or numerical approximation is used as evidence for the theorem.

The infinite-cardinality hypothesis is used only in the \(p<2\) lower bound, where it guarantees a coordinate of arbitrarily small norm for each fixed \(x\in S_Z\). The proof does not claim a finite-index analogue in that range.

## Relationship to prior work
Hardtke's work on vector-valued function spaces gives qualitative stability mechanisms for octahedrality and local octahedrality in absolute and Köthe–Bochner sums. The same author later introduced the quantitative index \(s(X)\) and recorded basic values and qualitative direct-sum statements. The inspected statements do not give the displayed exact formula for Hilbert-valued \(\ell_p\) sequence spaces.

The new formula is not a reformulation of the qualitative fact that a space is locally octahedral exactly when \(s(X)=2\): all values here are strictly below \(2\) for finite \(p>1\), and the theorem resolves the exact sub-octahedral scale. For \(p>2\), the value \(\sqrt2\) also separates the Hilbert-valued space from the scalar atomic \(\ell_p\) benchmark \(2^{1/p}\), so the conclusion is genuinely fibre-sensitive rather than a scalar reduction.

## Limitations
The theorem is restricted to real Hilbert fibres of dimension at least two and to infinite index sets. It does not classify finite-index Hilbert-valued sums for \(p<2\), arbitrary uniformly convex fibres, or the \(p=\infty\) endpoint. Literature searches and full-text inspections found no covering statement, but absence from searched sources is not a proof of global novelty; geometric-constant literature using different terminology remains a residual literature risk.

## References
1. J.-D. Hardtke, “On Certain Geometric Properties in Banach Spaces of Vector-Valued Functions,” Journal of Mathematical Physics, Analysis, Geometry 16 (2020), 119–137. DOI: 10.15407/mag16.02.119. Preprint: arXiv:1702.05050.
2. J.-D. Hardtke, “Summands in locally almost square and locally octahedral spaces,” Acta et Commentationes Universitatis Tartuensis de Mathematica 22 (2018), 149–162. DOI: 10.12697/ACUTM.2018.22.13. Preprint: arXiv:1705.06610.
