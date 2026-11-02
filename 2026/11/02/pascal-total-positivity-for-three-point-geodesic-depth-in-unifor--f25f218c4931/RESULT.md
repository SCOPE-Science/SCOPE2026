# Pascal total positivity for three-point geodesic depth in uniform Cayley trees

## Finding

Let \(n\ge3\) and let \(T\) be a uniformly random tree on \([n]\). Fix three distinct labeled vertices \(u,v,w\). Write \(D=d_T(u,v)\) for the length of the \(u\)-to-\(v\) path, and \(H=d_T(w,P_T(u,v))\) for the minimum graph distance of \(w\) to that path. For integers \(1\le d\le n-1\), define \(k=n-d-1\), and use \((k)_{\underline h}=k(k-1)\cdots(k-h+1)\) when \(0\le h\le k\), and zero when \(h>k\).

**Theorem (Pascal survival kernel and likelihood-ratio order).** For every \(1\le d\le n-1\),
\[
\Pr(H\ge0\mid D=d)=1,\qquad
\Pr(H\ge h\mid D=d)=\frac{(n-d-1)_{\underline h}}{(n-2)n^{h-1}}\quad(h\ge1).
\]
Hence the matrix of conditional survival probabilities, with rows indexed in increasing order by \(k=n-d-1\in\{0,\ldots,n-2\}\) and columns by \(h\in\{0,\ldots,n-2\}\), is exactly the Pascal matrix \(\bigl[\binom{k}{h}\bigr]\) multiplied by positive column scalars
\[
c_0=1,\qquad c_h=\frac{h!}{(n-2)n^{h-1}}\quad(h\ge1).
\]
**Every minor is nonnegative**, and for increasing index sets \(k_1<\cdots<k_r\), \(h_1<\cdots<h_r\), its determinant is strictly positive if and only if \(k_i\ge h_i\) for all \(i\). In addition, for every \(1\le d<n-1\),
\[
H\mid(D=d+1)\quad<_{\mathrm{lr}}\quad H\mid(D=d),
\]
where the direction signifies decreasing likelihood-ratio order, with the laws distinct. Thus for every pair of strictly increasing real functions \(f,g\) on the finite relevant supports, \(\operatorname{Cov}(f(D),g(H))<0\).

A finer geometric statement holds: conditional on a prescribed ordered path from \(u\) to \(v\), on \(w\) not belonging to that path, and on \(H=h\ge1\), the closest vertex of that path to \(w\) is uniform among all \(d+1\) path vertices. Its location is independent of \(H\) under this conditioning.

## Assumptions and scope

All trees are unrooted, simple, and uniformly sampled among the \(n^{n-2}\) Cayley trees, with no vertex or edge weights. Graph distances count edges. All three labels are fixed and distinct, and \(D\) has support exactly \(1,\ldots,n-1\). The falling factorial is zero for infeasible indices; binomial coefficients satisfy \(\binom{k}{h}=0\) for \(h>k\). The notation \(<_{\mathrm{lr}}\) denotes ordinary likelihood-ratio order with unequal distributions; the pointwise ratio of the smaller to the larger probability mass function is nonincreasing, including support zeros. At \(d=n-1\) the pendant depth is deterministically zero. The theorem does not treat nonuniform trees or an arbitrary graph.

## Proof

**1. Conditional path and forest.** Fix \(D=d\) and an ordered path \(u=x_0,x_1,\ldots,x_d=v\). There are \((n-2)_{\underline{d-1}}\) possible ordered interior label sequences. Deleting the path edges leaves a rooted forest whose prescribed roots are exactly these \(d+1\) path vertices: all remaining vertices independently attach within one of the rooted components, and conditioning on the path makes the forest uniform among such rooted forests. Conversely each such forest and path uniquely determines the original tree. By the classical rooted-forest count there are \(q n^{n-q-1}\) such forests on \(n\) labels with a prescribed root set of size \(q\). This gives the positive conditional event probability for every feasible \(d\), and shows
\[
\Pr(w\notin P_T(u,v)\mid D=d)=\frac{n-d-1}{n-2}.
\]

**2. Exact depth in a uniformly rooted forest.** Fix \(q\in\{1,\ldots,n-1\}\) prescribed roots, a specified nonroot \(w\), and let \(L\) be its distance to its root. There are \(q n^{n-q-1}\) rooted forests. For \(\ell\ge1\), a prescribed chain from \(w\) to a root with \(\ell\) edges has \(q(n-q-1)_{\underline{\ell-1}}\) choices (choice of endpoint root and distinct intermediate nonroots). After forcing these \(\ell\) parent arrows, the other \(m=n-q-\ell\) nonroots must eventually attach to the \(q+\ell\) absorbing vertices. The number of completions is
\[
(q+\ell)n^{m-1}\quad(m\ge1),\qquad 1\quad(m=0).
\]
Both values are covered by the expression \((q+\ell)n^{m-1}\) since \(q+\ell=n\) when \(m=0\). To verify this count without independence assumptions, the directed matrix-tree theorem gives the \(m\times m\) reduced Laplacian \(n I_m-\mathbf1\mathbf1^{\mathsf T}\). Its eigenvalues are \(n\) with multiplicity \(m-1\) and \(n-m=q+\ell\) once; the empty determinant is one. Hence
\[
\Pr(L=\ell)=\frac{(q+\ell)(n-q-1)_{\underline{\ell-1}}}{n^\ell}
\quad(1\le\ell\le n-q).
\]
This telescopes to
\[
\Pr(L\ge\ell)=\frac{(n-q-1)_{\underline{\ell-1}}}{n^{\ell-1}}.
\]
The uniform choice of the root endpoint in the above counting also proves that the root reached by \(w\), conditional on \(L=\ell\), is uniform among all prescribed roots.

**3. Geodesic survival and Pascal structure.** Apply step 2 with \(q=d+1\), and multiply by the off-path probability from step 1. For \(h\ge1\),
\[
\Pr(H\ge h\mid D=d)=\frac{n-d-1}{n-2}\frac{(n-d-2)_{\underline{h-1}}}{n^{h-1}}
=\frac{(n-d-1)_{\underline h}}{(n-2)n^{h-1}}.
\]
The column-scaled Pascal representation follows from \((k)_{\underline h}=h!\binom{k}{h}\). The Pascal matrix is totally nonnegative by the planar path interpretation: \(\binom{k}{h}\) counts northeast/horizontal directed lattice paths from \((-k,0)\) to \((0,h)\). The Lindström–Gessel–Viennot determinant expansion identifies each ordered minor with a nonnegative count of nonintersecting path families. Such a family exists exactly when the ordered source/sink indices satisfy \(k_i\ge h_i\) for every \(i\). Multiplication of columns by positive scalars preserves minor signs and strict support.

**4. The stronger likelihood-ratio comparison.** Subtract consecutive tails. For \(h\ge1\),
\[
p_d(h):=\Pr(H=h\mid D=d)=\frac{(n-d-1)_{\underline h}(d+h+1)}{(n-2)n^h},
\qquad p_d(0)=\frac{d-1}{n-2}.
\]
For common positive support at \(h\ge1\),
\[
\frac{p_{d+1}(h)}{p_d(h)}
=\frac{n-d-h-1}{n-d-1}\cdot\frac{d+h+2}{d+h+1},
\]
a product of two nonincreasing nonnegative functions of \(h\), strictly decreasing wherever both masses are positive. At \(h=0\), the ratio is \(d/(d-1)\) when \(d\ge2\), which exceeds the ratio at \(h=1\) because \(d/(d-1)>(d+3)/(d+2)\); for \(d=1\) the smaller law has positive mass at zero while the larger law does not. The upper endpoint of the shorter-geodesic distribution can only add a zero to the numerator. This verifies the likelihood-ratio ordering across the complete support, including all boundary cases. Stochastic ordering follows. Since the conditional tail at \(h=1\) decreases strictly with \(d\), and all \(D=d\) have positive probability, the standard independent-copy covariance identity gives \(\operatorname{Cov}(f(D),g(H))<0\) for strictly increasing \(f,g\).

## Verification

The included standalone \(\texttt{check.py}\) uses only the Python standard library. It independently enumerates all \(n^{n-2}\) labeled trees through \(n=7\) via Prüfer codes, reconstructs paths, and compares conditional depth tails with exact rational formulas; it also tests the conditional uniform geodesic projection. It checks normalizations, the Pascal column-scaling identities and likelihood-ratio inequalities for every \(3\le n\le50\), and all Pascal minors (including strict-support criteria) for \(3\le n\le8\). Running \(\texttt{python3 check.py}\) produced **91,703 exact assertions passed**. These finite tests support but do not replace the proof for all \(n\).

## Relationship to prior work

The uniform rooted-forest count \(q n^{n-q-1}\) is classical and appears as formula (6) in Pitman's *Coalescent Random Forests* (technical report 457, publicly listed September 1996). Aldous and Pitman's *A Family of Random Trees with Random Edge Lengths* (technical report 526, 1998) includes a general marked-subtree probability identity in Lemma 5, which can recover the underlying three-vertex enumerations; those foundational enumeration identities are **not** claimed as new. The totally nonnegative Pascal matrix itself is classical. The assessed structural assertion is that **the conditional three-point geodesic survival family is exactly a Pascal kernel of all orders, with explicit nonzero-minor support and the stronger strict likelihood-ratio decrease in the geodesic length**. Inspected sources did not explicitly state this conditional ordering package. Published-record searches for geodesic projection, pendant depth, reverse likelihood-ratio ordering and Pascal survival kernels did not show a covering statement; this is not proof of absolute historical novelty.

## Limitations

The result applies only to uniformly weighted Cayley trees and to three distinct fixed labels. The finite-\(n\) probability formula is derivable from earlier general marked-subtree enumerations, so there is a genuine priority risk that the stronger positivity and ordering inequalities may be implicit or previously recorded elsewhere. No new general tree-generation process, nonuniform extension, or independent expert validation is claimed. This work does not attempt a classification of multi-vertex geodesic projections.

## References

1. J. Pitman, *Coalescent Random Forests*, University of California, Berkeley technical report 457 (public record September 1, 1996); later published in *Annales de l'Institut Henri Poincaré* 34 (1998), 339–383. https://statistics.berkeley.edu/sites/default/files/tech-reports/457.pdf
2. D. Aldous and J. Pitman, *A Family of Random Trees with Random Edge Lengths*, Berkeley technical report 526 (public record June 1, 1998); *Random Structures & Algorithms* 15 (1999), 176–195, especially Lemma 5 and Section 3. https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/526.pdf
