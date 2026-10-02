# Sharp \(C(K)\) dichotomy for metric-functional weak convergence

## Setting

Let \(K\) be compact Hausdorff and let \(C(K)\) be the real Banach space with the supremum norm. For \(w,f\in C(K)\), write
\[
h_w(f)=\|f-w\|_\infty-\|w\|_\infty,
\]
and let \(C(K)^\diamond\) be the pointwise closure of the internal metric functionals \(h_w\). A sequence \(f_n\) converges metric-functionally weakly (d-weakly) to \(0\) when
\[
\liminf_{n\to\infty}h(f_n)\ge h(0)=0
\]
for every \(h\in C(K)^\diamond\).

The general comparison between the metric-functional topology and the classical weak topology, including finite-dimensional equality under the extreme-dual span criterion, is prior work and is used here only as background.

## Theorem

For compact Hausdorff \(K\), the following are equivalent:

1. \(K\) is infinite.
2. There exists a norm-unbounded sequence in \(C(K)\) converging d-weakly to \(0\).
3. For every prescribed sequence \(a_n>0\), there are nonnegative functions \(f_n\in C(K)\) with pairwise disjoint supports such that
   \[
   \|f_n\|_\infty=a_n
   \]
   and \(f_n\to0\) d-weakly.

Consequently,
\[
\sigma(C(K),C(K)^\diamond)=\sigma(C(K),C(K)^*)
\quad\Longleftrightarrow\quad
K\text{ is finite}.
\]

Thus the unbounded d-weak phenomenon is not special to \(C[0,1]\): every infinite compact Hausdorff \(K\) supports every positive prescribed norm profile.

## Proof

Assume \(K\) is infinite. We first construct countably many pairwise disjoint nonempty open sets \(U_n\). If \(K\) has infinitely many isolated points, take distinct open singletons. Otherwise choose a non-isolated point \(x\). Every neighborhood of \(x\) is infinite. Starting with an open neighborhood \(V_1\) of \(x\), choose \(y_n\in V_n\setminus\{x\}\). Regularity of compact Hausdorff spaces gives disjoint nonempty open sets \(U_n,V_{n+1}\subset V_n\) with \(y_n\in U_n\) and \(x\in V_{n+1}\). The resulting \(U_n\) are pairwise disjoint.

By normality, for each \(n\) choose \(g_n\in C(K,[0,1])\) with
\[
\|g_n\|_\infty=1,\qquad \operatorname{supp}g_n\subset U_n.
\]
Set \(f_n=a_ng_n\).

Fix an internal metric functional \(h_w\). Compactness gives \(s\in K\) with \(|w(s)|=\|w\|_\infty\). Because the supports of the \(f_n\) are pairwise disjoint, \(s\) belongs to at most one support. Hence, for all but at most one \(n\),
\[
f_n(s)=0
\]
and therefore
\[
\|f_n-w\|_\infty\ge |w(s)|=\|w\|_\infty,
\qquad
h_w(f_n)\ge0.
\]

Now take \(h\in C(K)^\diamond\). If \(h(f_n)<0\) and \(h(f_m)<0\) for two distinct indices, then a net of internal metric functionals converging pointwise to \(h\) would eventually be negative at both \(f_n\) and \(f_m\), contradicting the preceding paragraph. Thus \(h(f_n)<0\) for at most one \(n\), so
\[
\liminf_{n\to\infty}h(f_n)\ge0=h(0).
\]
Hence \(f_n\to0\) d-weakly. Since the positive numbers \(a_n\) were arbitrary, (3) follows, and choosing \(a_n\to\infty\) gives (2).

If \(K\) is finite, then \(C(K)\) is finite-dimensional. The already-established finite-dimensional equality of the metric-functional, weak and norm topologies implies that every d-weakly convergent sequence is norm-convergent and therefore bounded. This excludes (2) and (3).

Finally, weakly convergent sequences in a Banach space are norm bounded. Therefore the unbounded d-weakly null sequence for infinite \(K\) proves strict inequality of the two topologies, whereas finite \(K\) gives equality by finite-dimensionality.

## Relation to prior work

Gutiérrez and Nevanlinna introduced d-weak convergence and proved agreement with ordinary weak convergence for bounded sequences in normed spaces. Their 2026 preprint *A Weak Topology on Metric Spaces* constructs an unbounded d-weakly null sequence in \(C[0,1]\).

An earlier result already established the general topology inclusion, continuity of extreme dual functionals, the extreme-span equality criterion, finite-dimensional equality, and the strictly-convex-dual case. Those statements are not part of the originality claim here.

The claim here is the exact \(C(K)\) dichotomy for all compact Hausdorff \(K\), together with realization of every prescribed positive norm profile by disjoint nonnegative bumps.

## Limitations

The result is qualitative and concerns real \(C(K)\). It does not classify equality of the metric-functional and classical weak topologies for arbitrary infinite-dimensional Banach spaces. The proof is close in spirit to the recent \(C[0,1]\) disjoint-support counterexample, so parallel or subsequent rediscovery remains a concrete originality risk.

## References

1. A. W. Gutiérrez and O. Nevanlinna, *A Weak Topology on Metric Spaces*, arXiv:2609.19368 (2026).
2. A. W. Gutiérrez and O. Nevanlinna, *Metric functionals and weak convergence*, Z. Anal. Anwend. (2026), DOI 10.4171/ZAA/1828.
3. C. Walsh, *Hilbert and Thompson geometries isometric to infinite-dimensional Banach spaces*, Ann. Inst. Fourier 68 (2018), 1831–1877.
