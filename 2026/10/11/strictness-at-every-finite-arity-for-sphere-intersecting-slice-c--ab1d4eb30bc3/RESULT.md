# Strictness at every finite arity for sphere-intersecting slice combinations
## Finding
For every integer \(m\ge 2\), put \(n=m+1\) and define the absolute normalized norm
\[
N_m(r_1,\ldots,r_n)=\max_{1\le q\le n}\sum_{j\ne q}|r_j|
\]
on \(\mathbb R^n\). Let
\[
Z_m=\left(\bigoplus_{i=1}^{n}c_0\right)_{N_m}.
\]
Then \(Z_m\) has property \(\mathrm{P3}^{(m)}\), meaning that every convex combination of at most \(m\) slices of \(B_{Z_m}\) meets \(S_{Z_m}\), but \(Z_m\) fails \(\mathrm{P3}^{(m+1)}\). Consequently the finite-arity sphere-intersection properties form a strict hierarchy at every level.

More quantitatively, for every \(0<\alpha<m^{-2}\), there are \(m+1\) coordinate slices whose equal-weight average is contained in
\[
\frac{m(1+m\alpha)}{m+1}B_{Z_m},
\]
and the displayed radius is strictly smaller than \(1\).

## Assumptions and scope
All Banach spaces are real. A slice of \(B_X\) is
\[
S(B_X,f,\alpha)=\{x\in B_X:f(x)>1-\alpha\},
\qquad f\in S_{X^*},\ \alpha>0.
\]
Property \(\mathrm{P3}^{(k)}\) means that every convex combination of at most \(k\) slices of \(B_X\) intersects \(S_X\).

The proof uses the known fact that \(c_0\) has \(\mathrm{P1}\), hence every finite convex combination of slices of \(B_{c_0}\) intersects \(S_{c_0}\). No claim is made here about the corresponding finite-arity hierarchy for \(\mathrm{P2}\), nor about optimality among all possible witnesses for failure of \(\mathrm{P3}^{(m+1)}\).

## Proof
Write
\[
B_m^+=\{r\in[0,\infty)^n:N_m(r)\le1\}.
\]
The nonzero vertices of \(B_m^+\) are
\[
e_1,\ldots,e_n,\qquad
v=\left(\frac1m,\ldots,\frac1m\right).
\]
Indeed, if a vertex has a zero \(q\)-th coordinate, then the constraint indexed by \(q\) becomes
\[
\sum_{j=1}^{n}r_j\le1,
\]
so that supporting face is a simplex and its only nonzero vertices are the standard basis vectors. If all coordinates are positive, the nonnegativity constraints are inactive. A vertex must then have all \(n\) inequalities
\[
\sum_{j\ne q}r_j\le1
\]
active; their normal vectors form the invertible matrix with zero diagonal and ones off the diagonal. Hence all coordinates are equal, and solving the active equations gives \(r_i=1/(n-1)=1/m\).

For \(1\le q\le n\), define the positive facet
\[
F_q=\left\{r\in B_m^+:\sum_{j\ne q}r_j=1\right\}.
\]
The vertex \(v\) belongs to every \(F_q\), while \(e_i\in F_q\) exactly when \(i\ne q\). Therefore any collection of at most \(m=n-1\) nonzero vertices of \(B_m^+\) lies in a common facet \(F_q\): choose \(q\) different from every index \(i\) for which one of the chosen vertices equals \(e_i\).

Now take \(k\le m\) slices
\[
S^\ell=S(B_{Z_m},f^\ell,\alpha_\ell),
\qquad 1\le\ell\le k,
\]
and positive weights \(\lambda_\ell\) with \(\sum_{\ell=1}^k\lambda_\ell=1\). Write \(f^\ell=(f^\ell_i)_{i=1}^n\). Standard duality for a finite absolute sum gives
\[
1=\|f^\ell\|
=\max_{r\in B_m^+}\sum_{i=1}^n r_i\|f_i^\ell\|.
\]
Choose a nonzero maximizing vertex \(a^\ell\in\{e_1,\ldots,e_n,v\}\). For every \(i\) with \(f_i^\ell\ne0\), choose the coordinate slice
\[
T_{\ell,i}
=
S\left(B_{c_0},\frac{f_i^\ell}{\|f_i^\ell\|},\frac{\alpha_\ell}{2}\right);
\]
when \(f_i^\ell=0\), choose any fixed nonempty slice of \(B_{c_0}\). If \(x_{\ell,i}\in T_{\ell,i}\) for all \(i\), then
\[
y^\ell=(a_i^\ell x_{\ell,i})_{i=1}^n
\]
belongs to \(B_{Z_m}\) and satisfies
\[
f^\ell(y^\ell)
>
\left(1-\frac{\alpha_\ell}{2}\right)
\sum_{i=1}^n a_i^\ell\|f_i^\ell\|
=
1-\frac{\alpha_\ell}{2}
>
1-\alpha_\ell.
\]
Thus \(y^\ell\in S^\ell\).

The vertices \(a^1,\ldots,a^k\) lie in a common \(F_q\). Set
\[
c_i=\sum_{\ell=1}^k\lambda_\ell a_i^\ell.
\]
Then \(c=(c_i)\in F_q\), so \(N_m(c)=1\). For each \(i\) with \(c_i>0\), put
\[
\mu_{\ell,i}=\frac{\lambda_\ell a_i^\ell}{c_i}.
\]
These are nonnegative and sum to \(1\). Since \(c_0\) has \(\mathrm{P3}\), choose
\[
w_i\in
\left(\sum_{\ell=1}^k\mu_{\ell,i}T_{\ell,i}\right)\cap S_{c_0},
\]
and write \(w_i=\sum_\ell\mu_{\ell,i}x_{\ell,i}\) with \(x_{\ell,i}\in T_{\ell,i}\). Coordinates with \(c_i=0\) may be filled arbitrarily, because then every \(a_i^\ell=0\). With the resulting choices,
\[
z=\sum_{\ell=1}^k\lambda_\ell y^\ell
=(c_iw_i)_{i=1}^n.
\]
Hence \(\|z_i\|=c_i\) for every \(i\), and therefore
\[
\|z\|=N_m(c)=1.
\]
Thus every convex combination of at most \(m\) slices meets the sphere, proving \(\mathrm{P3}^{(m)}\).

It remains to show failure at arity \(m+1\). For each \(1\le i\le n\), let \(g_i\in S_{c_0^*}\), regarded as a norm-one functional supported on the \(i\)-th summand of \(Z_m\). Fix \(0<\alpha<m^{-2}\) and let
\[
S_i=S(B_{Z_m},g_i,\alpha).
\]
If \(x\in S_i\), then \(\|x_i\|>1-\alpha\). For \(j\ne i\), choose \(q\) distinct from both \(i\) and \(j\), which is possible because \(n=m+1\ge3\). Since \(\|x\|\le1\),
\[
\sum_{\ell\ne q}\|x_\ell\|\le1,
\]
and the left side contains both \(\|x_i\|\) and \(\|x_j\|\). Consequently
\[
\|x_j\|<\alpha.
\]

Take
\[
z=\frac1n\sum_{i=1}^{n}x^{(i)},
\qquad x^{(i)}\in S_i.
\]
For each coordinate \(j\),
\[
\|z_j\|
\le
\frac{1+(n-1)\alpha}{n}
=
\frac{1+m\alpha}{m+1}.
\]
Therefore
\[
\|z\|
\le
\frac{m(1+m\alpha)}{m+1}
<1,
\]
where the last inequality is exactly \(\alpha<m^{-2}\). Thus the equal-weight convex combination
\[
\frac1{m+1}\sum_{i=1}^{m+1}S_i
\]
does not meet \(S_{Z_m}\), and \(\mathrm{P3}^{(m+1)}\) fails.

## Verification
The argument is symbolic for arbitrary \(m\ge2\). The finite-dimensional vertex calculation is exhaustive: a positive vertex either lies on a coordinate face, where the feasible set is a simplex, or has full support, where all \(n\) independent facet inequalities must be active. The common-facet step uses only the pigeonhole fact that at most \(n-1\) standard basis vertices cannot occupy all \(n\) indices.

The slice-lifting step keeps the same maximizing vertex for each functional and uses only normalized coordinate slices of \(c_0\). The final sphere point is obtained because every nonzero coordinate of the convex average has a norm-one \(c_0\) factor, so its vector of coordinate norms is exactly the common-facet point \(c\). The failure argument is uniform in \(m\) and gives the explicit strict radius bound above. No finite enumeration is used as evidence for the infinite family.

## Relationship to prior work
Haller's 2026 preprint introduces the notation \(\mathrm{P3}^{(m)}\) for the restriction to at most \(m\) slices and constructs an infinite-dimensional real space with \(\mathrm{P3}^{(2)}\) but not \(\mathrm{P3}\). Its example is
\[
\left(\bigoplus_{i=1}^{3}c_0\right)_N,
\qquad
N(r,s,t)=\max\{|r|+|s|,\ |r|+|t|,\ |s|+|t|\},
\]
which is precisely the case \(m=2\) of the family above. The focal paper does not state strictness between every consecutive finite arity.

Abrahamsen and Lima proved that \(c_0\), more generally \(C(K)\) for scattered compact \(K\), has \(\mathrm{P1}\); this supplies the coordinate-space input used in the lifting argument. López-Pérez, Martín, and Rueda Zoca characterized the unrestricted sphere-intersection property by attainment of diameter two in every convex combination of slices. That characterization does not determine the finite-arity hierarchy.

## Limitations
The construction is tailored to the sphere-intersection property. It does not establish strictness of the analogous \(\mathrm{P2}^{(m)}\) hierarchy, classify all spaces separating two consecutive arities, or prove that the quantitative radius \(m(1+m\alpha)/(m+1)\) is optimal. The focal preprint is recent, so an equivalent generalization under different finite-arity or diameter-two terminology remains a residual originality risk.

## References
1. R. Haller, *Weak stability and binary convex combinations of slices*, arXiv:2608.11827v1, first submitted 2026-08-12.
2. T. A. Abrahamsen and V. Lima, *Relatively weakly open convex combinations of slices*, arXiv:1701.06169v1; Proc. Amer. Math. Soc. 146 (2018), 4421--4427.
3. G. López-Pérez, M. Martín, and A. Rueda Zoca, *Strong diameter two property and convex combinations of slices reaching the unit sphere*, arXiv:1703.04749; Mediterr. J. Math. 16 (2019), 122.
