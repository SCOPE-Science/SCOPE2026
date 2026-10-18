# Sharp simplex-volume phase cascade in Euclidean conical frusta

## Finding

Let \(d\ge2\), \(h,R>0\), \(0\le r\le R\), and let \(K\subset\mathbb R^d\) be the convex hull of two closed Euclidean \((d-1)\)-balls of radii \(R\) and \(r\) in parallel hyperplanes separated by perpendicular distance \(h\). Their centers need not be aligned. Define

\[
C_1=1,\qquad C_k=\frac{k^{k/2}}{(k-1)^{(k-1)/2}}\quad(k\ge2),\qquad t=\frac rR.
\]

The largest possible \(d\)-dimensional volume of a simplex contained in \(K\) is **exactly**

\[
\boxed{\mathcal M_d(K)=\frac{hR^{d-1}}{d!}\max_{1\le j\le d}\bigl(C_{d+1-j}C_j t^{j-1}\bigr).}
\tag{1}
\]

When \(r=0\), the term with \(j=1\) uses \(t^0=1\); all other terms are zero. Every positive term in the maximum is attained by a simplex with \(d+1-j\) vertices on the larger base and \(j\) vertices on the smaller base (all terms are positive when \(r>0\)). Within each base, any group with at least two vertices is a centered regular simplex; the spans of the two groups are mutually orthogonal. A single vertex in either group may lie anywhere in its corresponding closed base ball. Conversely, every **base-supported** maximizing simplex has precisely this structure for some maximizing \(j\), up to the obvious rigid and shear transformations. This is a classification of base-supported maximizers, not a claim that all maximizers must be base-supported.

For \(0<t<1\), the maximizing value of \(j\) changes at exactly \(\lfloor(d-1)/2\rfloor\) distinct thresholds

\[
\boxed{\tau_{d,j}=\frac{C_{d+1-j}C_j}{C_{d-j}C_{j+1}}\quad\left(1\le j\le\left\lfloor\frac{d-1}{2}\right\rfloor\right),}
\tag{2}
\]

which satisfy \(0<\tau_{d,1}<\tau_{d,2}<\cdots<1\). Starting at \(j=1\) for \(t=0\), the optimal count on the smaller base rises successively by one at each threshold. Exactly two adjacent counts tie at each threshold, with no skipped count or triple tie. At \(t=1\), there are additionally two balanced counts tied when \(d\) is even.

In dimension \(3\), (1) becomes \(\mathcal M_3(K)=hR^2\max\{\sqrt3/4,\,2t/3\}\), with its unique transition at \(t=3\sqrt3/8\). In dimension \(4\), the transition is exactly \(t=16/27\).

There is also a high-dimensional freezing law: for each fixed \(0\le t<1\),

\[
\lim_{d\to\infty}\frac{d!\,\mathcal M_d(K)}{hR^{d-1}C_d}
=\max_{j\ge1}C_j t^{j-1}.
\tag{3}
\]

The right side has finitely many relevant competitors for each fixed \(t<1\); the maximizing number of vertices on the smaller base stays bounded as \(d\to\infty\). Its limiting phase thresholds are \(C_j/C_{j+1}\), increasing strictly from \(1/2\) toward \(1\).

## Assumptions and scope

All balls are full closed Euclidean balls in parallel affine hyperplanes; their centers may have arbitrary horizontal displacement. The ambient volume is \(d\)-dimensional Lebesgue measure. A simplex is the convex hull of \(d+1\) affinely independent points of \(K\), without an a priori restriction that its vertices lie on the base circles or spheres. The zero-radius apex case and equal-radius cylindrical case are included. No result is asserted for nonhomothetic or non-Euclidean cross sections.

The primary classification is MSC2020 52A40 (extremal problems for convex bodies). The exact answer concerns unrestricted contained simplices, not simplex approximations with a predetermined orientation or fixed vertex split.

## Proof

**1. Normalize and reduce to the two bases.** Translate, scale horizontally by \(R\), scale vertically by \(h\), and apply a determinant-one horizontal shear to align the base centers. The resulting set is

\[
K_t=\operatorname{conv}\bigl((B_{d-1}\times\{0\})\cup(tB_{d-1}\times\{1\})\bigr),
\]

where \(B_{d-1}\) is the unit Euclidean ball. The transformations multiply volume by \(hR^{d-1}\). For fixed positions of all other vertices, the absolute determinant giving simplex volume is a convex function of the remaining vertex. Every point of \(K_t\) is a convex combination of a point on each base, so replacing that vertex by one of those base points cannot decrease volume. Repeating for the \(d+1\) vertices proves that some maximizer is base-supported and that no unrestricted simplex exceeds the base-supported maximum.

**2. Determine the volume for a fixed split.** Suppose \(k\ge1\) vertices lie on the lower base and \(j\ge1\) on the upper base, with \(k+j=d+1\). Subtract one lower vertex and one upper vertex in the determinant. Expansion along the height coordinate yields

\[
d!\operatorname{vol}_d(S)=\left|\bigwedge_{i=2}^k(a_i-a_1)\wedge\bigwedge_{s=2}^j(b_s-b_1)\right|,
\]

where \(a_i\in B_{d-1}\) and \(b_s\in tB_{d-1}\). The wedge norm is at most the product of the two intrinsic parallelepiped determinants; equality occurs when their difference spans are orthogonal (automatically true if either difference span is trivial).

**3. A sharp ball-simplex determinant bound.** For any \(m\ge2\) points \(u_1,\ldots,u_m\) in a Euclidean ball of radius \(s\), let \(\bar u\) be their mean and let \(\sigma_1,\ldots,\sigma_{m-1}\) be the nonzero singular values of their centered vertex matrix. The determinant of \((u_2-u_1,\ldots,u_m-u_1)\) in its \((m-1)\)-dimensional span is \(\sqrt m\prod_i\sigma_i\), and

\[
\sum_{i=1}^{m-1}\sigma_i^2=\sum_{i=1}^m\|u_i-\bar u\|^2
=\sum_{i=1}^m\|u_i\|^2-m\|\bar u\|^2\le ms^2.
\]

Arithmetic-geometric mean therefore bounds that determinant by

\[
\sqrt m\left(\frac{ms^2}{m-1}\right)^{(m-1)/2}=C_m s^{m-1}.
\]

Equality holds precisely when the points form a regular \((m-1)\)-simplex centered at the ball's origin with circumradius \(s\). For \(m=1\) the empty determinant is \(1\). Combining the two group bounds with the orthogonal-span bound gives \(d!\operatorname{vol}_d(S)\le C_k C_j t^{j-1}\). Place centered regular simplices in orthogonal horizontal coordinate subspaces of dimensions \(k-1\) and \(j-1\) to attain equality simultaneously. This proves (1) and the stated base-supported equality classification.

**4. All transitions, without missed phases.** Put \(q_m=C_{m+1}/C_m\). Let \(f(x)=x\log x\) on \(x>0\), continuously extended by \(f(0)=0\). Then

\[
\log q_m=\tfrac12[f(m+1)-2f(m)+f(m-1)]
=\tfrac12\int_0^1\int_0^1\frac{\mathrm du\,\mathrm dv}{m-1+u+v}.
\]

The integrable endpoint singularity for \(m=1\) is harmless. Thus \(q_m>1\) and the sequence \(q_m\) is strictly decreasing to \(1\). Denote by \(A_j(t)=C_{d+1-j}C_jt^{j-1}\) the coefficient of the \(j\)-vertex upper split. Then

\[
\frac{A_{j+1}(t)}{A_j(t)}=t\frac{q_j}{q_{d-j}}.
\]

For fixed \(t>0\), this ratio decreases strictly with \(j\). Hence \((A_j)\) is strictly log-concave and its maximum occurs at one count or at two adjacent counts. For \(t<1\) the count never exceeds \(\lfloor(d+1)/2\rfloor\). The adjacent tie equation is exactly \(t=q_{d-j}/q_j=\tau_{d,j}\). Since \(q_m\) decreases strictly with \(m\), each \(\tau_{d,j}\) lies in \((0,1)\) and increases strictly with \(j\) over the stated range. No phase can be skipped. At \(t=1\), symmetry \(A_j(1)=A_{d+1-j}(1)\) gives the balanced endpoint tie when \(d\) is even. This proves (2) and every transition claim.

**5. High-dimensional limit.** From the definition, \(C_d\sim\sqrt{ed}\) and, for every fixed \(j\), \(C_{d+1-j}/C_d\to1\). Moreover, \(C_{d+1-j}/C_d\le1\) and \(C_j t^{j-1}\to0\) as \(j\to\infty\) for fixed \(t<1\). Split the maximum into \(j\le J\) and \(j>J\), take \(d\to\infty\) on the finite part, and then \(J\to\infty\). This establishes (3) and boundedness of maximizing upper counts. The limit tie thresholds are \(1/q_j=C_j/C_{j+1}\), strictly increasing toward \(1\).

## Verification

Run `python3 check_frustum.py` using the Python 3 standard library. The script independently constructs regular groups through a Helmert orthonormal basis, evaluates simplex determinants by Gaussian elimination, checks the predicted volumes for all \(486\) layer-split configurations in dimensions \(2\) through \(10\), and tests \(5400\) randomly sampled contained simplices in dimensions \(2\) through \(6\). It also checks strict ordering and two-way ties of computed transition thresholds and a fixed-ratio high-dimensional count. The expected final line begins `PASS: 486 constructed layer configurations`. These finite computations are consistency checks only; Steps 1–5 prove the infinite statements.

## Relationship to prior work

Lassak's 2011 paper proves a general approximation theorem for a maximal contained simplex and, in Lemma 2, classifies maximal simplices inside a symmetric double-cone (one apex and a centered regular base simplex). It does **not** calculate the competition among arbitrarily many upper- and lower-base vertices of an asymmetrically truncated circular cone. Horváth and Lángi's 2014 Theorem 2 identifies orthogonal joins of regular simplices maximizing the volume of polytopes with \(d+2\) vertices on a *single* unit sphere. That supports the geometric motif but does not furnish the radius-weighted, two-parallel-ball simplex optimum or its transition cascade. An independently indexed study, *Universal Santaló and volume-product laws for homothetic frusta* (2026, published-record identifier 3dbfdaf0b359), treats the more general convex hull of homothetic bases, but concerns polar-section integrals, Santaló locations, and volume products, not maximal contained-simplex determinants. McKinney's 1974 work concerns centrally symmetric convex sets; its full text was not accessible for this comparison and its possible relevance to the equal-radius endpoint remains a priority risk. These antecedents are credited, not claimed as new lemmas.

## Limitations

A targeted literature search did not locate the exact frustum formula, but absence from searches does not prove publication novelty. The full text of McKinney (1974) was inaccessible and priority at the cylindrical endpoint therefore remains unresolved. The result does not classify all possible maximizers having vertices on the frustum's ruled side, only those supported on the two bases. The asymptotic statement fixes \(t<1\); it does not characterize the double-scaling regime as \(t\to1\) simultaneously with growing \(d\). No independent mathematical validation has been performed.

## References

1. M. Lassak, *Approximation of convex bodies by inscribed simplices of maximum volume*, Beiträge zur Algebra und Geometrie **52** (2011), 389–394, DOI: 10.1007/s13366-011-0026-x. Original public publication 3 May 2011; freely available original PDF at https://link.springer.com/content/pdf/10.1007/s13366-011-0026-x.pdf.
2. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496, first posted 26 February 2014; see especially Theorem 2, https://arxiv.org/html/1402.6496v3.
3. J. R. McKinney, *On maximal simplices inscribed in a central convex set*, Mathematika **21** (1974), 38–44, DOI: 10.1112/S0025579300005763. Relevant bibliographic record and abstract were accessible; complete text was not.
4. *Universal Santaló and volume-product laws for homothetic frusta*, publicly indexed geometric research result, 11 October 2026, record identifier 3dbfdaf0b359. The full public result was read for comparison of objects, quantifiers and invariant.
