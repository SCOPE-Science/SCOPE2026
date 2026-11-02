# Sharp Hilbert-snowflake exponents after one intrapart edge addition to a biclique

## Finding

For integers \(m\ge3\), \(n\ge2\), start with the unit-edge complete bipartite graph \(K_{m,n}\), and add a single edge joining two vertices in its part of size \(m\). Let \(G_{m,n}^{+}\) be the resulting graph and \(d\) its shortest-path distance. Its exact supremal negative-type exponent is
\[
\wp(G_{m,n}^{+})=\log_2 q_{m,n},
\]
where \(q_{m,n}\) is the unique root in \((1,2)\) of
\[
P_{m,n}(q)= (4mn-2m-6n+2)q^2+(-6mn+m+9n-2)q+2mn-4n=0.
\]
For every \(0\le p<\wp(G_{m,n}^{+})\) the powered distance has strict \(p\)-negative type; at equality it has nonstrict negative type with a one-dimensional zero-mass equality space; for every larger \(p\) negative type fails. Equivalently, \(d^{p/2}\) has an isometric real Hilbert-space realization exactly for \(0\le p\le\wp(G_{m,n}^{+})\). For positive \(p\) below the endpoint the minimum affine Hilbert dimension is \(m+n-1\); at the endpoint it is \(m+n-2\).

The one-edge addition strictly raises the exponent over the complete-bipartite baseline:
\[
\wp(G_{m,n}^{+})>\wp(K_{m,n})
=\log_2\frac{2mn}{2mn-m-n}.
\]
For each fixed \(n\ge2\), the improvement has the sharp asymptotic
\[
\wp(G_{m,n}^{+})-\wp(K_{m,n})
=\frac{2n}{(4n^2-1)\ln 2}\,m^{-2}+O_n(m^{-3}),\qquad m\to\infty.
\]
The family remains outside the unsnowflaked quadratic-embedding class: \(\wp(G_{m,n}^{+})<1\) for all indicated \(m,n\).

## Assumptions and scope

All graphs are finite, simple and undirected. Every edge has length one. Label the modified part \(U=\{a,b,x_1,\dots,x_r\}\), where \(r=m-2\ge1\) and \(ab\) is the added edge, and the other part \(V=\{y_1,\dots,y_n\}\). Cross-part distances and \(d(a,b)\) are one. Every remaining distance between distinct vertices in the same part is two.

For \(p\ge0\), \(p\)-negative type means \(\sum_{v,w}z_vz_wd(v,w)^p\le0\) for all real \(z\) with \(\sum_v z_v=0\), taking diagonal entries to be zero also at \(p=0\). Strict means equality only for \(z=0\). The parameter \(q=2^p\) therefore belongs to \([1,\infty)\).

## Proof

Write \(s=\sum_{v\in U}z_v=-\sum_{v\in V}z_v\), \(u=(z_a+z_b)/2\), and \(v=(z_a-z_b)/2\). Set
\[
h=2q(m-1)-(m-2),\qquad A=4q-2+\frac{4q}{m-2},
\qquad F(q)=2(q-1)-\frac qn-\frac{q(2q-1)}h.
\]
The powered distance matrix is the complete-bipartite powered distance matrix with a correction \(-(q-1)(E_{ab}+E_{ba})\). Using \(\sum_vz_v=0\) and completing squares gives the following **exact identity**, with \(r=m-2\):
\[
\begin{aligned}
\sum_{v,w}z_vz_wd(v,w)^p={}&F(q)s^2-A\left(u-\frac{qs}{h}\right)^2-2v^2\\
&-q\sum_{i=1}^r\left(z_{x_i}-\frac{s-2u}{r}\right)^2
-q\sum_{j=1}^n\left(z_{y_j}+\frac sn\right)^2.
\end{aligned}
\]
All subtracted coefficients are strictly positive for \(q\ge1\). Consequently, negative type holds if and only if \(F(q)\le0\). Indeed, whenever \(F(q)>0\), the explicit zero-sum vector
\[
z_a=z_b=\frac qh,\qquad z_{x_i}=\frac{2q-1}{h},\qquad z_{y_j}=-\frac1n
\]
has \(s=1\), makes all square terms vanish, and has strictly positive quadratic form. When \(F(q)<0\), the quadratic form is strictly negative for nonzero zero-sum vectors. When \(F(q)=0\), every equality vector is a scalar multiple of the displayed vector (including the zero vector), so the nullity on the zero-sum subspace is exactly one.

Since \(nhF(q)=P_{m,n}(q)\) and \(nh>0\), the sign is governed by the displayed quadratic. Its leading coefficient is \(2((2m-3)n-(m-1))>0\), while \(P_{m,n}(1)=-(m+n)<0\). Thus it has exactly one root greater than one. Furthermore,
\[
F(2)=2-\frac2n-\frac6{3m-2}>0
\]
for every \(m\ge3,n\ge2\), proving the location of the root and the strict/nonstrict/failure trichotomy. The Schoenberg distance criterion identifies negative type of \(d^p\) with squared-Euclidean embeddability of \(d^p\), equivalently isometric embeddability of \(d^{p/2}\). The centered squared-distance Gram matrix has rank \(m+n-1\) below the endpoint and \(m+n-2\) at it, giving the asserted minimum affine dimensions.

For the unmodified graph, the analogous optimized coefficient is \(F_0(q)=2(q-1)-q/m-q/n\), with unique zero \(q_0=2mn/(2mn-m-n)\). Their exact difference is
\[
F(q)-F_0(q)=-\frac{2q(q-1)}{mh}<0\qquad(q>1),
\]
so \(q_{m,n}>q_0\), and the edge addition strictly increases the exponent.

For the asymptotic, fix \(n\) and send \(m\) to infinity. Both roots converge to \(q_\infty=2n/(2n-1)\). The identity \(F(q_{m,n})=0\), together with \(F_0(q_0)=0\), gives exactly
\[
\left(2-\frac1m-\frac1n\right)(q_{m,n}-q_0)
=\frac{2q_{m,n}(q_{m,n}-1)}{m\,[m(2q_{m,n}-1)-2(q_{m,n}-1)]}.
\]
Hence
\[
q_{m,n}-q_0=\frac{4n^2}{(2n-1)^2(2n+1)}m^{-2}+O_n(m^{-3}).
\]
Taking the base-two logarithmic ratio yields the asserted sharp coefficient. The \(O_n\) terms arise from ordinary analytic expansions at the positive limiting root.

## Verification

The accompanying `check.py` is standalone Python standard-library code. It constructs shortest-path distances by breadth-first search, compares direct quadratic forms with the completed-square identity using exact rational arithmetic, checks definiteness via exact rational symmetric elimination at sampled powers, constructs explicit positive witnesses outside the range, and tests root bounds and the asymptotic coefficient numerically. Executing `python check.py` prints the assertion counts. These finite checks are supplementary: they do not establish the infinitely quantified theorem, which follows from the analytical proof above.

For the smallest graph in the stated family, \(m=3,n=2\),
\[
q_{3,2}=\frac{17+\sqrt{161}}{16},\quad
\wp(G_{3,2}^{+})=\log_2\left(\frac{17+\sqrt{161}}{16}\right)\approx0.8918360665,
\]
whereas \(\wp(K_{3,2})=\log_2(12/7)\approx0.7776075787\).

## Relationship to prior work

Sánchez (2011, Theorem 3.1) gives the complete-bipartite exponent, which is the exact baseline used above; its all-equal within-part equality loads differ from the present perturbed critical loads. Li and Weston (2009) establish general strict-negative-type interval results. Obata (2022, revised 2023, Theorem 3.12) classifies the unsnowflaked quadratic embedding constant of complete multipartite graphs. For \(m\ge3\), the present modified graph is **not** complete multipartite, since a third vertex of \(U\) is nonadjacent to each of \(a,b\), although \(a,b\) are adjacent. Młotkowski, Skrzypczyk and Wojtylak (2024, Theorems 2.1–2.2) treat **deleted cross-part edges**, rather than an added within-part edge, and their formulas are for the ordinary quadratic embedding constant. Choudhury and Nandi (2025, Theorem 1.1) give a general unsnowflaked quadratic-embedding-constant formula for joins with a regular factor; such an \(p=1\) result does not determine the full sharp negative-type exponent or critical Hilbert snowflake rank. A related complete-multipartite negative-type classification likewise does not cover the nonmultipartite family considered here. An older equivalent formulation using general distance kernels cannot be excluded by this comparison.

## Limitations

Only one added edge within the part of size \(m\ge3\) is treated. No statement is made for multiple edge additions, edge deletions, weighted metrics, arbitrary joins or perturbations to distances three or greater. The smaller boundary \(m=2\) is not part of this claim, because that case remains complete multipartite and is covered by the broader complete-multipartite framework. Exact novelty beyond the inspected literature is not independently certified. Numerical checks are finite and supplementary.

## References

- S. Sánchez, *On the supremal p-negative type of a finite metric space* (2011), arXiv:1108.0451v1, especially Theorem 3.1.
- H. Li and A. Weston, *Strict p-negative type of a metric space* (2009), arXiv:0901.0695v1.
- N. Obata, *Complete Multipartite Graphs of Non-QE Class* (first public June 12, 2022), arXiv:2206.05848v1, Theorem 3.12 (revised version consulted for context).
- W. Młotkowski, M. Skrzypczyk and M. Wojtylak, *On Quadratic Embeddability of Bipartite Graphs and Theta Graphs* (first public September 26, 2024), arXiv:2409.17662v1, Theorems 2.1–2.2.
- P. N. Choudhury and R. Nandi, *Quadratic Embedding Constants of Cartesian Products and Joins of Graphs* (first public August 14, 2025), arXiv:2508.10834v1, Theorem 1.1.
