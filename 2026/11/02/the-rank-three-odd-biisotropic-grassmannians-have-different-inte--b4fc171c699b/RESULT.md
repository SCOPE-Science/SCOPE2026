# The rank-three odd biisotropic Grassmannians have different integral cohomology rings from their additive Grassmannian twins

## Finding
For every integer \(n\ge3\), let \(V\) be a complex vector space of dimension \(2n+1\), let \(\sigma_1,\sigma_2\in\wedge^2V^\vee\) span a general pencil, and let \(X_n\subset\operatorname{Gr}(3,V)\) be the common zero locus of their restrictions to the tautological three-planes. Let \(G_n=\operatorname{Gr}(3,2n-1)\). Both varieties have complex dimension \(d=6n-12\).

Their integral singular cohomology groups are isomorphic as graded abelian groups, by Fonarev--Kuznetsov's theorem, yet **their graded integral cohomology rings are never isomorphic**. Indeed, for the primitive Plücker classes \(H_X\) and \(H_G\),
\[
\deg X_n=\int_{X_n}H_X^d=
\frac{32(6n-12)!(n-1)(2n-3)(2n-1)(64n^3-288n^2+404n-165)}{(2n)!(2n-1)!(2n-2)!}
\]
and
\[
\deg G_n=\int_{G_n}H_G^d=
\frac{2(6n-12)!}{(2n-2)!(2n-3)!(2n-4)!}.
\]
Their ratio satisfies
\[
\frac{\deg X_n}{\deg G_n}=
1+\frac{3(n-2)(6n-11)(7n-5)}{n(n-1)(2n-1)}>1.
\]
For \(n=3\), the two degrees are \(61\) and \(5\), respectively; for \(n=4\), they are \(10329\) and \(462\).

## Assumptions and scope
All varieties and cohomology groups are over \(\mathbb C\); cohomology uses singular cohomology with integral coefficients and its cup product. The pencil of alternating forms is general. Here \(n\ge3\) and \(d=6n-12\). A graded-ring isomorphism is required to preserve integral coefficients, degrees, units, and products; preservation of the Plücker polarization is **not** assumed. The smoothness and the graded additive comparison are the theorems of Fonarev and Kuznetsov, rather than new claims.

## Proof
**1. Geometry and the ambient Chow class.** Let \(S\) be the rank-three tautological subbundle on \(\operatorname{Gr}(3,2n+1)\). The two alternating forms determine a regular section of \(E=(\wedge^2S^\vee)^{\oplus2}\), of rank six. The cited smoothness and dimension theorem gives that the zero scheme \(X_n\) has expected codimension six. Therefore its fundamental class is \(c_6(E)\). With formal Chern roots \(x,y,z\) of \(S^\vee\),
\[
[X_n]=(x+y)^2(x+z)^2(y+z)^2,
\qquad H_X=x+y+z.
\]

**2. Exact projective degree.** The standard three-row Grassmannian coefficient-integration formula gives
\[
\int_{X_n}H_X^{6n-12}
=[x^{2n}y^{2n-1}z^{2n-2}]
(x+y+z)^{6n-12}(x-y)(x-z)(y-z)
(x+y)^2(x+z)^2(y+z)^2.
\]
Write \(B=(x-y)(x-z)(y-z)(x+y)^2(x+z)^2(y+z)^2=\sum b_{abc}x^ay^bz^c\), so \(a+b+c=9\). Expanding the multinomial factor and clearing the factorial denominator reduces the integral to
\[
\frac{(6n-12)!}{(2n)!(2n-1)!(2n-2)!}
\sum_{a,b,c}b_{abc}(2n)_{\underline a}(2n-1)_{\underline b}(2n-2)_{\underline c}.
\]
Here falling factorials \((t)_{\underline a}\) mean \(t(t-1)\cdots(t-a+1)\) for \(a\ge1\), and \(1\) for \(a=0\). Direct polynomial multiplication in the integer ring \(\mathbb Z[n]\) (replayed in `verify_degree.py`) gives the **exact symbolic identity**
\[
\sum_{a,b,c}b_{abc}(2n)_{\underline a}(2n-1)_{\underline b}(2n-2)_{\underline c}
=32(n-1)(2n-3)(2n-1)(64n^3-288n^2+404n-165).
\]
This is a polynomial identity, not an inference from a finite table. Substitution yields the announced formula for \(\deg X_n\).

**3. Degree of the comparison Grassmannian.** The classical three-row rectangular hook-length formula, applied to \(G_n=\operatorname{Gr}(3,2n-1)\), gives
\[
\deg G_n=\frac{2(6n-12)!}{(2n-2)!(2n-3)!(2n-4)!}.
\]
Dividing the two positive degrees and simplifying yields
\[
\frac{\deg X_n}{\deg G_n}
=\frac{2(64n^3-288n^2+404n-165)}{n(n-1)(2n-1)}
=1+\frac{3(n-2)(6n-11)(7n-5)}{n(n-1)(2n-1)}.
\]
For all integers \(n\ge3\), the final correction is strictly positive.

**4. Primitive polarizations and the ring obstruction.** Fonarev--Kuznetsov's cellular comparison shows \(H^2(X_n,\mathbb Z)\cong H^2(G_n,\mathbb Z)\cong\mathbb Z\); both varieties are connected compact smooth complex manifolds, hence \(H^{2d}(-,\mathbb Z)\cong\mathbb Z\) with the complex orientation. The Plücker class on \(G_n\) is primitive because Grassmannians contain Plücker lines. It is also primitive on \(X_n\): in the standard normal form of the pencil, with basis indices \(-n,\ldots,n\), the four-dimensional coordinate subspace spanned by \(e_{-3},e_{-1},e_1,e_3\) is isotropic for both forms, since every pairwise index sum is different from \(-1\) and \(1\). Fix the two-plane \(A=\langle e_{-3},e_{-1}\rangle\) within this four-space \(W\). The set of three-planes \(A\subset U\subset W\) is a projective line entirely contained in \(X_n\), on which \(\mathcal O_{\operatorname{Gr}}(1)\) has degree one. Thus \(H_X\) is primitive in \(H^2(X_n,\mathbb Z)\).

Any isomorphism of graded integral cohomology rings would send the unique primitive degree-two generator \(H_X\) to \(\pm H_G\), and a top-degree generator to a top-degree generator up to sign. Since \(d=6n-12\) is even, the positive integer magnitudes of the top powers would have to be equal. The degree formulas give a strict inequality. Such a graded-ring isomorphism cannot exist. \(\square\)

## Verification
The standalone standard-library program `verify_degree.py` constructs the full 30-monomial polynomial \(B\) from its nine linear factors, checks the symbolic coefficient identity **as an identity of integral polynomials**, and checks the degree and ratio formulas for \(3\le n\le9\). It separately computes the same degree via exact rational torus-fixed-point localization for \(3\le n\le6\) on \(\operatorname{Gr}(3,2n+1)\), with distinct integer torus weights \(0,1,\ldots,2n\). The exact localization expression is
\[
\sum_{|I|=3}
\frac{(\sum_{i\in I}i)^{6n-12}\prod_{\{i,j\}\subset I}(i+j)^2}
{\prod_{i\in I,\,j\notin I}(j-i)}.
\]
Running `python3 verify_degree.py` from a directory containing the standalone file returned `VERIFY_OK`. The computational checks support the exact coefficient manipulation; the mathematical conclusions for **all** \(n\ge3\) rely on the symbolic identity, general geometric facts and primitive-line argument, not on finite enumeration.

## Relationship to prior work
Fonarev and Kuznetsov (arXiv:2610.03309v1, Theorem 1.1) establish equality of **graded abelian groups**, and explicitly distinguish the still-open task of understanding cohomology ring structure (Remark 1.2). Their article does not state the rank-three Plücker-degree ratio or the ring nonisomorphism. The present theorem answers a sharp **negative comparison question** but does not present the full ring.

Benedetti (arXiv:1809.10902v1) treats principally rank-two biisotropic Grassmannians for pencils in **even-dimensional** vector spaces, with a specialized cohomology-ring computation. Fatighenti and Mongardi (arXiv:1904.05679v1, Section 3.8) examine \(\operatorname{BIGr}(3,8)\) for an **even-dimensional** vector space. Those results provide relevant methodological analogues but do not establish the claimed odd-dimensional rank-three infinite-series comparison. The standard general Grassmannian coefficient formula is used as a proof tool, not claimed as new.

## Limitations
No complete presentation of \(H^*(X_n,\mathbb Z)\) is asserted, nor an obstruction for other ranks \(k\). The pencil must be general and the ground field is \(\mathbb C\). The comparison concerns abstract integral graded cohomology rings, not just polarized rings. Historical priority remains provisional: Kuznetsov's cited manuscript on \(\operatorname{BIGr}(3,7)\) is listed as **in preparation** in the motivating paper and was unavailable for comparison, and further unpublished or differently named equivalent computations are possible. Independent mathematical audit has not been performed.

## References
1. A. Fonarev and A. Kuznetsov, *Betti Numbers of Odd Biisotropic Symplectic Grassmannians*, arXiv:2610.03309v1 (public 2026-10-02), especially Theorem 1.1, Remark 1.2 and equation (2.1). https://arxiv.org/html/2610.03309v1
2. V. Benedetti, *Bisymplectic Grassmannians of planes*, arXiv:1809.10902v1 (2018), especially Introduction, Sections 2 and 3. https://arxiv.org/html/1809.10902v1
3. E. Fatighenti and G. Mongardi, *Fano varieties of K3 type and IHS manifolds*, arXiv:1904.05679v1 (2019), Section 3.8. https://arxiv.org/html/1904.05679v1
4. A. Kuznetsov, *The odd biisotropic symplectic Grassmannian \(\operatorname{S_2Gr}(3,7)\)*, cited as in preparation (2026) in reference [Kuz26] of item 1; unavailable for full-text comparison.
