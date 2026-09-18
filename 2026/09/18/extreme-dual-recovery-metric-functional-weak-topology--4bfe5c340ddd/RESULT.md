# Extreme-dual recovery of the classical weak topology from metric functionals

## Result

Let \((X,d)\) be a metric space with a chosen base point \(o\). Write \(X^\diamond\) for the pointwise closure of the internal metric functionals
\[
h_w(x)=d(x,w)-d(o,w),\qquad w\in X,
\]
and let \(\tau_\diamond=\sigma(X,X^\diamond)\) be the topology introduced by Gutiérrez and Nevanlinna, with basic neighborhoods
\[
B(x,F,c)=\bigcap_{h\in F}\{y\in X:h(y)>h(x)-c\},
\]
where \(F\subset X^\diamond\) is finite and \(c>0\).

### Theorem A: a sharp separation property

For every metric space \((X,d)\), the topology \(\tau_\diamond\) is \(T_1\).

This is sharp in the usual separation hierarchy: Gutiérrez and Nevanlinna exhibit a metric on \(\mathbb R\), namely \(d(x,y)=\sqrt{|x-y|}\), for which \(\tau_\diamond\) is not Hausdorff.

### Theorem B: comparison with the classical weak topology

Let \(X\) be a real normed linear space, let \(\tau_w=\sigma(X,X^*)\) denote its classical weak topology, and let
\[
E=\operatorname{Ext}(B_{X^*})
\]
be the extreme points of the closed dual unit ball. Then:

1. \(\tau_\diamond\subseteq \tau_w\).
2. Every \(e\in E\) is \(\tau_\diamond\)-continuous.
3. Consequently, if
   \[
   \operatorname{span}E=X^*,
   \]
   then
   \[
   \boxed{\tau_\diamond=\tau_w.}
   \]

In particular, equality holds for every finite-dimensional real normed space and for every real normed space whose dual is strictly convex. Thus the metric-functional topology agrees with the classical weak topology, at the level of arbitrary nets, on every real Hilbert space and on every real \(\ell^p\), \(1<p<\infty\).

The inclusion can be strict. The unbounded sequence in \(C[0,1]\) constructed in *A Weak Topology on Metric Spaces* converges to zero in \(\tau_\diamond\). It cannot converge weakly, since every weakly convergent sequence in a Banach space is norm bounded. Hence
\[
\tau_\diamond\subsetneq \tau_w
\quad\text{for }C[0,1].
\]

## Proof

### Proof of Theorem A

Fix distinct points \(x,y\in X\). The internal metric functional based at \(y\) is
\[
h_y(z)=d(z,y)-d(o,y).
\]
It satisfies
\[
h_y(x)-h_y(y)=d(x,y)>0.
\]
Choose \(0<c<d(x,y)\). Then \(x\in B(x,\{h_y\},c)\), while \(y\notin B(x,\{h_y\},c)\). Interchanging \(x\) and \(y\) gives the reverse separation. Therefore every singleton is closed and \(\tau_\diamond\) is \(T_1\).

### Step 1: \(\tau_\diamond\subseteq\tau_w\) on normed spaces

Every metric functional on a normed linear space is convex: this is Proposition 2.8 of Gutiérrez--Nevanlinna, applied to the usual linear convexity. Every metric functional is also 1-Lipschitz, hence norm-continuous.

Let \(h\in X^\diamond\) and \(a\in\mathbb R\). Its sublevel set
\[
C_a=\{x\in X:h(x)\le a\}
\]
is norm-closed and convex. By the Hahn--Banach separation theorem, every norm-closed convex subset of a normed space is weakly closed. Hence \(C_a\) is \(\tau_w\)-closed, so \(h\) is weakly lower semicontinuous. Therefore each set
\[
\{y:h(y)>h(x)-c\}
\]
is weakly open. Finite intersections of such sets are weakly open, so every \(\tau_\diamond\)-basic neighborhood is weakly open. Thus \(\tau_\diamond\subseteq\tau_w\).

### Step 2: extreme dual functionals are \(\tau_\diamond\)-continuous

Walsh's Corollary 3.5 identifies every extreme point of the dual unit ball with a singleton Busemann point of the normed space. In the metric-functional terminology, this gives
\[
E\subseteq X^\diamond.
\]
Because the dual ball is centrally symmetric, \(e\in E\) implies \(-e\in E\). The defining property of \(\tau_\diamond\) makes every metric functional lower semicontinuous. Hence both \(e\) and \(-e\) are \(\tau_\diamond\)-lower-semicontinuous. Equivalently, both sets \(\{e>a\}\) and \(\{e<a\}\) are \(\tau_\diamond\)-open for every \(a\in\mathbb R\). Thus every \(e\in E\) is \(\tau_\diamond\)-continuous.

If \(X^*=\operatorname{span}E\), every continuous linear functional on \(X\) is a finite linear combination of \(\tau_\diamond\)-continuous functions, hence is itself \(\tau_\diamond\)-continuous. Since \(\tau_w\) is the coarsest topology making all members of \(X^*\) continuous, this gives \(\tau_w\subseteq\tau_\diamond\). Together with Step 1,
\[
\tau_\diamond=\tau_w.
\]

### Step 3: two useful classes satisfying the extreme-span condition

If \(X^*\) is strictly convex, every point of the dual unit sphere is extreme, so \(E=S_{X^*}\) and its linear span is all of \(X^*\).

If \(X\) is finite-dimensional, then \(X^*\) is finite-dimensional and the Krein--Milman theorem gives
\[
B_{X^*}=\overline{\operatorname{conv}}E.
\]
The linear span of \(E\) is a finite-dimensional, hence closed, subspace of \(X^*\). Since it contains \(\operatorname{conv}E\), it contains \(B_{X^*}\), and therefore equals \(X^*\). Thus \(\tau_\diamond=\tau_w\), which in finite dimension is also the norm topology.

## Context and relation to prior work

Gutiérrez and Nevanlinna introduced \(d\)-weak convergence in 2025 and proved that bounded sequences in normed linear spaces are \(d\)-weakly convergent exactly when they are classically weakly convergent. Their proof uses Walsh's result that extreme points of the dual unit ball are metric functionals. They also observed that, when the dual is strictly convex, a \(d\)-weakly convergent sequence must be weakly convergent and therefore bounded.

Their 16 September 2026 preprint *A Weak Topology on Metric Spaces* upgrades \(d\)-weak convergence to the topology \(\tau_\diamond\), proves that its convergent nets are exactly the \(d\)-weakly convergent nets, that it is coarser than the metric topology, and that it is Hausdorff on normed linear spaces. It also supplies an unbounded \(\tau_\diamond\)-convergent sequence in \(C[0,1]\), correcting an earlier claim.

The result above identifies the position of this new topology relative to the classical weak topology and supplies a simple algebraic criterion for exact recovery. The strict-convex-dual sequence statement from the earlier paper is thereby upgraded to equality of topologies and equivalence for arbitrary nets. The finite-dimensional conclusion requires no smoothness or strict-convexity hypothesis on the norm. The general \(T_1\) statement also locates the new topology sharply between no separation assumption and Hausdorffness.

For comparison, Kell's co-convex topology is another metric-geometric weak topology and agrees with the usual weak topology on Banach spaces. The present result concerns the distinct metric-functional topology defined by Gutiérrez and Nevanlinna.

## Limitations

The condition \(\operatorname{span}\operatorname{Ext}(B_{X^*})=X^*\) is sufficient, not claimed necessary, for \(\tau_\diamond=\tau_w\). The result does not characterize the continuous linear dual of \((X,\tau_\diamond)\) in general, nor does it decide equality for spaces such as \(C(K)\) beyond cases covered by the criterion. The \(C[0,1]\) example shows that equality fails in general.

The topology paper used as the immediate motivation is very recent, so unindexed or unpublished parallel work remains a residual originality risk.

## References

1. A. W. Gutiérrez and O. Nevanlinna, *A Weak Topology on Metric Spaces*, arXiv:2609.19368 (submitted 16 September 2026). https://arxiv.org/abs/2609.19368
2. A. W. Gutiérrez and O. Nevanlinna, *Metric functionals and weak convergence*, Zeitschrift für Analysis und ihre Anwendungen, published online 3 June 2026, DOI 10.4171/ZAA/1828; arXiv:2506.04154. https://doi.org/10.4171/ZAA/1828
3. C. Walsh, *Hilbert and Thompson geometries isometric to infinite-dimensional Banach spaces*, Annales de l'Institut Fourier 68 (2018), 1831--1877, DOI 10.5802/aif.3198. https://doi.org/10.5802/aif.3198
4. M. Kell, *Uniformly Convex Metric Spaces*, Analysis and Geometry in Metric Spaces 2 (2014), 359--380, DOI 10.2478/agms-2014-0015. https://doi.org/10.2478/agms-2014-0015
