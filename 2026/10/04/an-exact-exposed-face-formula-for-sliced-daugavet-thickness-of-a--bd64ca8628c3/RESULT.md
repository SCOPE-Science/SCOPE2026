# An exact exposed-face formula for sliced Daugavet thickness of absolute sums
## Finding
Let \(X\) and \(Y\) be nonzero real Banach spaces with the Daugavet property, and let \(N\) be an absolute normalized norm on \(\mathbb R^2\). Put
\[
S_N^+=S_{(\mathbb R^2,N)}\cap[0,\infty)^2,\qquad
S_{N^*}^+=S_{(\mathbb R^2,N^*)}\cap[0,\infty)^2.
\]
For \(h=(\alpha,\beta)\in S_{N^*}^+\), define its positive support face
\[
F_N(h)=\{(a,b)\in B_{(\mathbb R^2,N)}\cap[0,\infty)^2:\alpha a+\beta b=1\}.
\]
Then the sliced Daugavet index of thickness of the absolute sum \(Z=X\oplus_NY\) is exactly
\[
\mathcal T^s(Z)=
\inf_{\substack{p=(c,d)\in S_N^+\\ h\in S_{N^*}^+}}
\ \max_{q=(a,b)\in F_N(h)}N(c+a,d+b).
\]
Thus, once both factors have the Daugavet property, the sliced thickness index depends only on the two-dimensional absolute norm and is obtained by a compact exposed-face optimization.

## Assumptions and scope
All Banach spaces are real and nonzero. The norm \(N\) is absolute and normalized, so it is coordinatewise monotone on the positive quadrant and its dual norm \(N^*\) is again absolute and normalized. The sliced Daugavet index is
\[
\mathcal T^s(E)=\inf\{r>0:\text{there are }e\in S_E\text{ and a slice }S\subset B_E\text{ with }S\subset B(e,r)\}.
\]
For \(h\in S_{N^*}^+\), compactness of \(B_N\) guarantees that \(F_N(h)\) is nonempty and compact. No smoothness, strict convexity, finite polyhedrality, or symmetry beyond absoluteness is assumed.

## Proof
Write \(Z=X\oplus_NY\).

For the upper bound, fix \(p=(c,d)\in S_N^+\) and \(h=(\alpha,\beta)\in S_{N^*}^+\). Choose \(x\in S_X\), \(y\in S_Y\), \(f\in S_{X^*}\), and \(g\in S_{Y^*}\), and put
\[
z_0=(cx,dy),\qquad z^*=(\alpha f,\beta g).
\]
Then \(z_0\in S_Z\) and \(z^*\in S_{Z^*}\). For \(\delta>0\), let
\[
S_\delta=\{(u,v)\in B_Z:\alpha f(u)+\beta g(v)>1-\delta\}.
\]
If \((u,v)\in S_\delta\) and \(r=(\|u\|,\|v\|)\), then \(r\in B_N\cap[0,\infty)^2\) and
\[
\alpha r_1+\beta r_2>1-\delta.
\]
Moreover,
\[
\|z_0-(u,v)\|_N
\le N(c+\|u\|,d+\|v\|)=N(p+r).
\]
By compactness,
\[
\lim_{\delta\downarrow0}
\sup_{\substack{r\in B_N\cap[0,\infty)^2\\h\cdot r>1-\delta}}
N(p+r)
=
\max_{q\in F_N(h)}N(p+q).
\]
Indeed, any sequence of almost-maximizers for \(\delta\downarrow0\) has a convergent subsequence whose limit lies in \(F_N(h)\). Hence, for every \(\varepsilon>0\), some slice \(S_\delta\) is contained in the ball centered at \(z_0\) of radius
\[
\max_{q\in F_N(h)}N(p+q)+\varepsilon.
\]
Taking the infimum in \(p\) and \(h\) gives the required upper bound.

For the lower bound, take an arbitrary center \(z_0=(x_0,y_0)\in S_Z\) and an arbitrary slice
\[
S=\{(u,v)\in B_Z:f(u)+g(v)>1-\delta\},
\]
where \((f,g)\in S_{Z^*}\). Set
\[
c=\|x_0\|,\quad d=\|y_0\|,\quad
\alpha=\|f\|,\quad\beta=\|g\|.
\]
Then \(p=(c,d)\in S_N^+\) and \(h=(\alpha,\beta)\in S_{N^*}^+\). Choose \(q=(a,b)\in F_N(h)\) attaining
\[
\rho=\max_{q'\in F_N(h)}N(p+q').
\]
Fix \(0<\eta<\delta\).

If \(\alpha>0\) and \(c>0\), apply the Daugavet slice characterization in \(X\) to \(x_0/c\) and the slice determined by \(f/\alpha\). We obtain \(u\in B_X\) such that
\[
(f/\alpha)(u)>1-\eta,\qquad
\|x_0/c-u\|>2-\eta.
\]
A norming functional for \(x_0/c-u\) then gives
\[
\|x_0-au\|\ge(1-\eta)(c+a).
\]
If \(\alpha>0\) and \(c=0\), choose \(u\) in the same slice; then \(\|u\|>1-\eta\), so the same displayed lower bound holds. If \(\alpha=0\), there is no slice restriction in the \(X\)-coordinate: choose \(u=-x_0/c\) when \(c>0\), and any \(u\in S_X\) when \(c=0\). In either case,
\[
\|x_0-au\|\ge(1-\eta)(c+a).
\]
Construct \(v\in B_Y\) analogously so that
\[
\|y_0-bv\|\ge(1-\eta)(d+b)
\]
and, whenever \(\beta>0\), \((g/\beta)(v)>1-\eta\).

Coordinatewise monotonicity of \(N\) gives
\[
\|(au,bv)\|_N\le N(a,b)=1,
\]
while
\[
f(au)+g(bv)>(1-\eta)(\alpha a+\beta b)=1-\eta>1-\delta.
\]
Thus \((au,bv)\in S\), and
\[
\|z_0-(au,bv)\|_N
\ge(1-\eta)N(c+a,d+b)
=(1-\eta)\rho.
\]
Letting \(\eta\downarrow0\), every slice and every unit-sphere center contain points at distance at least \(\rho\), and \(\rho\) is at least the displayed scalar infimum. This proves the lower bound and hence equality.

## Verification
The proof uses only the standard duality
\[
(X\oplus_NY)^*=X^*\oplus_{N^*}Y^*,
\]
coordinatewise monotonicity of absolute norms, compactness of the two-dimensional unit ball, and the usual slice characterization of the Daugavet property.

As consistency checks, the formula agrees with the known exact values for \(\ell_p\)-sums. For \(1<p<\infty\), the published value is
\[
\mathcal T^s(X\oplus_pY)=2^{1/p}
\]
for Daugavet factors. At the endpoints, the published stability of the Daugavet property under \(\ell_1\)- and \(\ell_\infty\)-sums gives value \(2\), which the face formula also yields.

No numerical experiment is needed for the proof.

## Relationship to prior work
Haller, Langemets, Lima, Nadel, and Rueda Zoca introduced and studied \(\mathcal T^s\) for absolute sums. Their 2020 preprint, later published in the Journal of Functional Analysis, gives a general lower estimate from a comparison \(N\ge\gamma\|\cdot\|_1\), a general upper estimate under an exposed-axis hypothesis and \(N\le\Gamma\|\cdot\|_\infty\), and exact values for \(\ell_p\)-sums. The full text inspected does not state an exact formula for arbitrary absolute normalized \(N\). The formula above replaces those one-sided scalar relaxations, for Daugavet factors, by a single exact optimization over positive exposed support faces.

A 2026 preprint by Haller and Ostrak studies the ordinary Daugavet index of thickness and a special two-parameter absolute norm in a counterexample for \(\ell_1\)-sums. Its accessible abstract concerns the ordinary index and a special norm, not the general exposed-face formula above. Full-text comparison with that preprint was not available in the present source access, so it remains a residual literature risk.

## Limitations
The formula is proved only for the sliced index \(\mathcal T^s\) and assumes that both summands have the Daugavet property. It does not assert an analogous equality for the ordinary index \(\mathcal T\) or for \(\mathcal T^{cc}\), and it does not address sums with non-Daugavet factors. The 2026 related preprint could not be inspected in full, so a hidden equivalent formulation there cannot be completely excluded.

## References
1. R. Haller, J. Langemets, V. Lima, R. Nadel, A. Rueda Zoca, “On Daugavet indices of thickness,” arXiv:2005.02045, first submitted 5 May 2020; Journal of Functional Analysis 280 (2021), 108846, DOI:10.1016/j.jfa.2020.108846.
2. R. Haller, A. Ostrak, “A counterexample for the Daugavet index of thickness in \(\ell_1\)-sums,” arXiv:2607.02227, first submitted 2 July 2026.
