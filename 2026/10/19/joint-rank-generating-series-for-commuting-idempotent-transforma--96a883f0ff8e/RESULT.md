# Joint-rank generating series for commuting idempotent transformations

## Finding
For every integer \(n\geq0\), let \(T_n\) be the full transformation monoid on a labeled \(n\)-element set. Define
\[
F_n(u,v,z)=\sum_{\substack{e,f\in T_n\\e^2=e,\ f^2=f,\ ef=fe}}u^{|\operatorname{im}(e)|}v^{|\operatorname{im}(f)|}z^{|\operatorname{im}(ef)|}.
\]
In formal power series with coefficients in \(\mathbb Q[u,v,z]\),
\[
\boxed{\sum_{n\geq0}F_n(u,v,z)\frac{x^n}{n!}=\exp\!\left(xuvz\sum_{a,b\geq0}\frac{(xu)^a(xv)^b}{a!b!}\exp\bigl(x(a+1)(b+1)\bigr)\right).}
\]
In particular, writing \(t_n=F_n(1,1,1)\), the values for \(n=0,\ldots,11\) are
\[
1,1,7,58,601,7616,113989,1963060,38178193,826879312,19727279461,513864449396.
\]
For positive \(n\), a rank triple \((r,s,h)\) occurs exactly when \(1\le h\le\min(r,s)\) and \(r+s-h\le n\). The coefficients are explicit positive integers as given below.

## Assumptions and scope
Maps are total functions on a labeled finite set; multiplication denotes composition. Both maps are idempotent and commute. For \(n=0\), use the unique empty function, so \(F_0=1\) and the triple \((0,0,0)\) occurs once. The parameters \(u,v,z\) mark the image sizes of the first map, second map and product, respectively. All identities are formal: for any fixed power of \(x\), only finitely many terms contribute.

## Proof
For an idempotent transformation, the image is its pointwise fixed-point set. When idempotents \(e,f\) commute, \(p=ef=fe\) is idempotent, its image is the common fixed-point set of \(e\) and \(f\), and therefore
\[
H=\operatorname{im}(p)=\operatorname{im}(e)\cap\operatorname{im}(f).
\]
Set \(U=\operatorname{im}(e)\setminus H\), \(V=\operatorname{im}(f)\setminus H\), and \(W=[n]\setminus(H\sqcup U\sqcup V)\). These sets are disjoint and exhaust the ground set. Every \(h\in H\) is fixed by both maps. Every \(a\in U\) is fixed by \(e\) and is sent by \(f\) to some \(h\in H\); similarly every \(b\in V\) is fixed by \(f\) and is sent by \(e\) to some \(h\in H\). These targets divide \(U\) and \(V\) into fibers \(U_h,V_h\), indexed by \(h\in H\).

If \(w\in W\), then \(e(w)\in H\sqcup U\) and \(f(w)\in H\sqcup V\). The two values \(ef(w)\) and \(fe(w)\) agree if and only if their associated roots in \(H\) agree. Consequently, for one and only one \(h\in H\),
\[
e(w)\in\{h\}\sqcup U_h,\qquad f(w)\in\{h\}\sqcup V_h.
\]
Conversely, every choice of these disjoint sets, assignments of the vertices in \(U\) and \(V\) to roots, and two images for every \(w\in W\) as displayed, defines commuting idempotents. This proves a bijective normal form: each root \(h\) carries \(a=|U_h|\) first-map-only image points, \(b=|V_h|\) second-map-only image points, and any number \(c\) of remaining vertices. Each of those \(c\) vertices has exactly \((a+1)(b+1)\) choices for its two images. Each root contributes one to all three ranks; the \(a\) points contribute to the first rank and the \(b\) points to the second.

For a single labeled rooted component, choosing its distinguished root, two disjoint auxiliary labeled subsets and an arbitrary residual subset thus has exponential generating function
\[
K(x;u,v,z)=xuvz\sum_{a,b\ge0}\frac{(xu)^a(xv)^b}{a!b!}\sum_{c\ge0}\frac{\bigl(x(a+1)(b+1)\bigr)^c}{c!}.
\]
The components corresponding to different roots form an unordered labeled set, so the labeled exponential formula gives \(\exp K\), proving the boxed series.

For an explicit finite coefficient, put \(a=r-h\), \(b=s-h\), and \(c=n-r-s+h\). When these are nonnegative and \(h\ge1\), let \([a]=\{1,\ldots,a\}\), with the usual empty-set convention. Then
\[
\boxed{[u^rv^sz^h]F_n(u,v,z)=\frac{n!}{h!a!b!c!}\sum_{\alpha:[a]\to[h]}\ \sum_{\beta:[b]\to[h]}\left(\sum_{j=1}^h\bigl(1+|\alpha^{-1}(j)|\bigr)\bigl(1+|\beta^{-1}(j)|\bigr)\right)^c.}
\]
Indeed, choose the four labeled sets \(H,U,V,W\) first, assign the points of \(U,V\) to the \(h\) roots, and then assign the ordered pair of images for each point of \(W\). The same counting proves all coefficients are strictly positive precisely on the stated support, while outside it they vanish.

For total counts, let \(b_k\) count connected rooted components of size \(k\). The normalization above yields
\[
b_k=k\sum_{a+b+c=k-1}\frac{(k-1)!}{a!b!c!}(a+1)^c(b+1)^c\quad(k\ge1).
\]
Removing the component containing a distinguished ground-set element proves
\[
t_0=1,\qquad t_n=\sum_{k=1}^n\binom{n-1}{k-1}b_k t_{n-k}\quad(n\ge1),
\]
which is an integer recurrence independent of formal-series manipulation.

## Verification
The accompanying standalone Python 3 file `verify.py` checks the theorem in three independent ways. Direct enumeration of all idempotent total maps and their commuting pairs is compared to the finite multinomial coefficient formula for all rank triples for \(1\le n\le5\). An additional direct check at \(n=6\) covers \(1057\) idempotent maps and all their ordered pairs. Finally the rooted-component recurrence reproduces \(t_n\) through \(n=11\). The checker prints `CHECKER_OK` upon completion. These are finite corroborations; the proof of the all-\(n\) statement is the bijection above.

## Relationship to prior work
André, Araújo and Konieczny (2011) study the semigroup generated by idempotents inside regular centralizers of idempotent transformations. Mir and Alali (2024) determine zero-divisor bands and automorphism groups in restricted-range transformation centralizer semigroups. Both concern structural properties of centralizers, but neither derives an all-degree simultaneous rank enumeration of ordered commuting idempotents in the unrestricted full transformation monoid. The classical labeled exponential formula is used here as an enumerative tool, not claimed as new. The specific finite normal form, trivariate series, and coefficient enumeration are the claims made here.

## Limitations
This result counts labeled ordered pairs of idempotents, not conjugacy classes or pairs of arbitrary (non-idempotent) maps. Searches of indexed mathematical literature and related research records did not locate a previous equivalent trivariate rank formula, but non-indexed semigroup enumerations or semilattice-action species may contain an equivalent description; originality must remain subject to independent literature review. Direct computation alone establishes only the checked finite sizes. No asymptotic estimate is claimed.

## References
- J. M. André, J. Araújo and J. Konieczny, *Regular centralizers of idempotent transformations*, Semigroup Forum 82 (2011), 307–318, DOI: 10.1007/s00233-010-9274-6. Author-shared full text: https://www.researchgate.net/publication/225682461_Regular_centralizers_of_idempotent_transformations
- D. J. Mir and A. S. Alali, *On Centralizers of Idempotents with Restricted Range*, Symmetry 16 (2024), article 769, publicly available June 19, 2024, DOI: 10.3390/sym16060769, https://www.mdpi.com/2073-8994/16/6/769
- The standard labeled combinatorial exponential formula, used in its elementary finite-set form.
