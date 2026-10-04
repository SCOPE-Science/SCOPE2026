# Axis-strict absolute sums have no positive symmetric strong diameter scale
## Finding
For every absolute normalized norm \(N\) on \(\mathbb R^2\) satisfying \(N(1,t)>1\) and \(N(t,1)>1\) for every \(t>0\), every pair of nonzero real Banach spaces \(X,Y\), and every \(d\in(0,2]\), the absolute sum \(X\oplus_NY\) fails the symmetric strong diameter \(d\) property \(\mathrm{SSD}(d)\mathrm P\). Consequently, for every \(1\le p<\infty\), every \(\ell_p\)-sum with at least two nonzero real Banach summands fails \(\mathrm{SSD}(d)\mathrm P\) for every \(d>0\).

The hypothesis on \(N\) says that the unit sphere leaves each coordinate axis immediately: no point \((1,t)\) or \((t,1)\) with \(t>0\) remains in the unit ball. The conclusion is stronger than failure of the endpoint symmetric strong diameter two property: every positive quantitative level fails.

## Assumptions and scope
All Banach spaces are real and nonzero. An absolute normalized norm \(N\) on \(\mathbb R^2\) satisfies \(N(a,b)=N(|a|,|b|)\) and \(N(1,0)=N(0,1)=1\). The absolute sum \(Z=X\oplus_NY\) has norm \(\|(x,y)\|=N(\|x\|,\|y\|)\).

For \(d\in(0,2]\), \(Z\) has \(\mathrm{SSD}(d)\mathrm P\) when for every finite family of slices \(S_i\) of \(B_Z\) and every \(\varepsilon>0\), there are \(z_i\in S_i\) and \(w\in B_Z\) with \(\|w\|>1-\varepsilon\) such that \(z_i\pm (d/2)w\in S_i\) for every \(i\).

The theorem assumes axis strictness in both directions:
\[
N(1,t)>1\quad\text{and}\quad N(t,1)>1\qquad(t>0).
\]
For the \(\ell_p\)-norm with \(1\le p<\infty\), this holds because \(\|(1,t)\|_p=(1+t^p)^{1/p}>1\) whenever \(t>0\).

## Proof
Fix \(d\in(0,2]\) and put \(s=d/2>0\). For \(0<\delta<1\), define the two axis-clearance functions
\[
\rho_1(\delta)=\sup\{b\in[0,1]:N(1-\delta,b)\le1\},\qquad
\rho_2(\delta)=\sup\{a\in[0,1]:N(a,1-\delta)\le1\}.
\]
They are well-defined because \(0\) belongs to both defining sets, and every coordinate of \(B_N\) has absolute value at most \(1\).

Axis strictness and continuity imply
\[
\rho_1(\delta)\longrightarrow0,\qquad \rho_2(\delta)\longrightarrow0
\quad(\delta\downarrow0).
\]
Indeed, if for example \(\rho_1(\delta_n)\not\to0\) along \(\delta_n\downarrow0\), compactness of \([0,1]\) gives a subsequence and some \(b>0\) with \(N(1,b)\le1\), contradicting \(N(1,b)>1\). The other coordinate is identical.

Choose \(\delta>0\) so small that
\[
N\left(\frac{\rho_2(\delta)}s,\frac{\rho_1(\delta)}s\right)<\frac12.
\]
Take \(x^*\in S_{X^*}\) and \(y^*\in S_{Y^*}\). Since the dual absolute norm is normalized, \((x^*,0)\) and \((0,y^*)\) are norm-one functionals on \(Z\). Hence
\[
S_1=\{(x,y)\in B_Z:x^*(x)>1-\delta\},\qquad
S_2=\{(x,y)\in B_Z:y^*(y)>1-\delta\}
\]
are slices.

Suppose \(Z\) had \(\mathrm{SSD}(d)\mathrm P\). Apply the definition to \(S_1,S_2\) with \(\varepsilon=1/2\). We obtain \(z_1=(x_1,y_1)\in S_1\), \(z_2=(x_2,y_2)\in S_2\), and \(w=(u,v)\in B_Z\) such that
\[
\|w\|>\frac12,\qquad z_i\pm s w\in S_i\quad(i=1,2).
\]
From \(z_1\pm sw\in S_1\),
\[
\|x_1\pm su\|>1-\delta.
\]
Because these perturbed points still lie in \(B_Z\), monotonicity of an absolute norm gives
\[
N(1-\delta,\|y_1\pm sv\|)\le1,
\]
so \(\|y_1\pm sv\|\le\rho_1(\delta)\). The triangle inequality then yields
\[
s\|v\|\le\rho_1(\delta).
\]
The slice \(S_2\) gives in exactly the same way
\[
s\|u\|\le\rho_2(\delta).
\]
Therefore
\[
\|w\|=N(\|u\|,\|v\|)
\le N\left(\frac{\rho_2(\delta)}s,\frac{\rho_1(\delta)}s\right)
<\frac12,
\]
contradicting \(\|w\|>1/2\). Thus \(X\oplus_NY\) fails \(\mathrm{SSD}(d)\mathrm P\) for every positive \(d\).

For an arbitrary \(\ell_p\)-sum with \(1\le p<\infty\) and at least two nonzero summands, choose one nonzero coordinate and group all remaining coordinates into the second summand. This is an isometric decomposition \(X\oplus_pY\) with both factors nonzero, so the preceding argument applies.

## Verification
The proof was reconstructed directly from the slice definition. The two nonstandard points checked explicitly are: (i) axis strictness forces both clearance functions \(\rho_1,\rho_2\) to converge to zero by compactness and continuity; and (ii) coordinate functionals define genuine slices because the dual of an absolute normalized sum has normalized coordinate axes. No finite computation or numerical experiment is used as evidence.

Boundary checks agree with the statement. The argument needs \(d>0\), because division by \(s=d/2\) is essential. It does not apply to \(\ell_\infty\), where \(N(1,t)=1\) for \(0\le t\le1\), and the published endpoint theory shows markedly different behavior there.

## Relationship to prior work
Haller, Langemets, Lima, and Nadel proved in 2018 that for an absolute normalized norm different from \(\ell_\infty\), the corresponding two-summand space cannot have the endpoint \(\mathrm{SSD}2\mathrm P\); for \(\ell_\infty\)-sums they proved the endpoint property holds exactly when one factor has it. Their theorem does not imply failure at smaller quantitative levels.

Oja, Saealle, and Zolk introduced \(\mathrm{SSD}(d)\mathrm P\) in 2020 and proved \(s\)-ASQ implies \(\mathrm{SSD}(2s)\mathrm P\). Their direct-sum results concern \(s\)-ASQ and \(s\)-LASQ. Failure of \(s\)-ASQ cannot be reversed through that one-way implication to obtain failure of \(\mathrm{SSD}(d)\mathrm P\). The theorem above therefore supplies a distinct quantitative obstruction: for all \(\ell_p\)-sums with \(p<\infty\), the entire positive symmetric strong diameter scale disappears.

## Limitations
The axis-strict hypothesis is sufficient, not claimed necessary, for total collapse of the positive \(\mathrm{SSD}(d)\mathrm P\) scale. Absolute norms with nontrivial flat pieces on one or both coordinate edges are not classified here. No assertion is made for the nonsymmetric properties \(\mathrm{SD}(d)\mathrm P\) or \(\mathrm{LD}(d)\mathrm P\), and no assertion is made for a one-summand space. The literature comparison cannot exclude an equivalent statement under unindexed or substantially different terminology.

## References
1. R. Haller, J. Langemets, V. Lima, R. Nadel, *Symmetric strong diameter two property*, arXiv:1804.01705v1, 5 April 2018; especially Theorem 3.1.
2. E. Oja, N. Saealle, I. Zolk, *Quantitative versions of almost squareness and diameter 2 properties*, Acta et Commentationes Universitatis Tartuensis de Mathematica 24 (2020), DOI:10.12697/ACUTM.2020.24.09; especially Definition 1.5, Propositions 1.6, 1.7, 2.5, and 2.6.
