# Disjoint sequences are metric-functionally null in every AM-space

## Finding
Let \(X\) be a real AM-space, and let \(X^\diamond\) denote its metric functionals for the norm metric with basepoint \(0\). Then every pairwise disjoint sequence \((x_n)\subset X\) is d-weakly null:
\[
 x_n\longrightarrow 0\quad\text{in }\sigma(X,X^\diamond),
\]
with no hypothesis on \((\|x_n\|)\).

Therefore, if \(X\) is infinite-dimensional, then every prescribed positive sequence \((a_n)\) occurs as the norm profile of a positive pairwise disjoint d-weakly null sequence: there are \(u_n\ge 0\) with
\[
 u_n\perp u_m\quad(n\ne m),\qquad \|u_n\|=a_n,
\]
and \(u_n\to0\) d-weakly. In particular, choosing \(a_n\to\infty\) gives an unbounded convergent sequence for the metric-functional weak topology.

As a consequence,
\[
 \sigma(X,X^\diamond)=\sigma(X,X^*)
 \quad\Longleftrightarrow\quad
 X\text{ is finite-dimensional}
\]
for real AM-spaces.

## Assumptions and scope
An AM-space is a real Banach lattice whose norm satisfies
\[
 \|x\vee y\|=\max\{\|x\|,\|y\|\}\qquad(x,y\ge0).
\]
Two vectors are disjoint when \(|x|\wedge|y|=0\). For \(w\in X\), the internal metric functional is
\[
 h_w(x)=\|x-w\|-\|w\|.
\]
The space \(X^\diamond\) is the pointwise closure of the internal metric functionals. A sequence is d-weakly null exactly when
\[
 \liminf_{n\to\infty} h(x_n)\ge h(0)=0
\]
for every \(h\in X^\diamond\). The recent topology construction of Gutiérrez and Nevanlinna identifies this convergence with convergence in \(\sigma(X,X^\diamond)\).

The result is about AM-spaces as Banach lattices, including closed AM-sublattices that need not have a strong unit and need not themselves be presented as a full \(C(K)\)-space.

## Proof
By Kakutani's representation theorem, every AM-space \(X\) is lattice isometric to a closed vector sublattice \(Y\) of \(C(K)\) for some compact Hausdorff space \(K\). We identify \(X\) with \(Y\). The norm on \(Y\) is the supremum norm inherited from \(C(K)\).

Let \((x_n)\subset Y\) be pairwise disjoint. Fix \(w\in Y\). Since \(w\) is continuous on compact \(K\), there is \(s\in K\) with
\[
 |w(s)|=\|w\|_\infty.
\]
Pointwise disjointness implies that at most one member of \((x_n)\) is nonzero at \(s\). Hence, for all but at most one \(n\),
\[
 \|x_n-w\|_\infty\ge |x_n(s)-w(s)|=|w(s)|=\|w\|_\infty,
\]
so
\[
 h_w(x_n)=\|x_n-w\|_\infty-\|w\|_\infty\ge0.
\]
Thus every internal metric functional is negative on at most one term of a disjoint sequence.

Now take any \(h\in X^\diamond\). Choose a net \((w_i)\subset X\) such that \(h_{w_i}\to h\) pointwise. If \(h(x_n)<0\) and \(h(x_m)<0\) for two distinct indices \(n\ne m\), pointwise convergence at the two fixed points \(x_n,x_m\) would make some sufficiently late \(h_{w_i}\) negative at both points. This contradicts the preceding paragraph. Therefore \(h(x_n)<0\) for at most one \(n\), and so
\[
 \liminf_{n\to\infty}h(x_n)\ge0=h(0).
\]
This proves d-weak nullity of every disjoint sequence.

Every infinite-dimensional Banach lattice contains an infinite sequence of nonzero pairwise disjoint positive vectors. Choose such a sequence \((v_n)\) in an infinite-dimensional AM-space and set
\[
 u_n=a_n\frac{v_n}{\|v_n\|}.
\]
Then \((u_n)\) remains positive and pairwise disjoint, has \(\|u_n\|=a_n\), and is d-weakly null by the first part.

It remains to compare the metric-functional and classical weak topologies. Each internal metric functional on a normed space is convex and \(1\)-Lipschitz. Pointwise limits preserve convexity and the \(1\)-Lipschitz bound, so every metric functional is norm-continuous and convex, hence weakly lower semicontinuous. Therefore every basic metric-functional open set is weakly open, and
\[
 \sigma(X,X^\diamond)\subseteq\sigma(X,X^*).
\]
If \(X\) is infinite-dimensional, choose \(a_n\to\infty\). The resulting d-weakly null sequence is norm-unbounded, whereas every weakly convergent sequence in a Banach space is norm-bounded. Hence the inclusion is strict.

If \(X\) is finite-dimensional, its lattice atoms give a lattice isometry onto \(\ell_\infty^m\) for some finite \(m\). For the standard coordinate vector \(e_j\),
\[
 h_{t e_j}(x)=\|x-t e_j\|_\infty-t\longrightarrow -x_j,
\qquad
 h_{-t e_j}(x)\longrightarrow x_j
\]
pointwise as \(t\to\infty\). Thus every coordinate functional and its negative belong to \(X^\diamond\). Their metric-functional basic neighborhoods generate the ordinary finite-dimensional topology. Since the metric-functional topology is already no finer than the norm topology, it equals the norm topology, which equals the weak topology in finite dimension.

## Verification
The crucial argument uses only three exact ingredients: Kakutani's lattice-isometric embedding of an AM-space as a closed sublattice of \(C(K)\); norm attainment for each represented \(w\in C(K)\); and the definition of metric functionals as the pointwise closure of internal functions. No passage from ambient \(C(K)\) metric functionals to subspace metric functionals is assumed. This distinction is important: d-weak convergence is known to be invariant under surjective isometries, but arbitrary isometric embeddings do not by themselves transfer all metric functionals.

The existence of an infinite disjoint positive sequence in every infinite-dimensional Banach lattice is a standard lattice fact; one published formulation is Lemma 2.6 of Oikhberg (2016). Scaling preserves disjointness and gives the arbitrary norm profile exactly.

The topology comparison was checked directly from convex weak lower semicontinuity, and the finite-dimensional endpoint was checked explicitly through the coordinate limits of internal metric functionals on \(\ell_\infty^m\).

## Relationship to prior work
Gutiérrez and Nevanlinna introduced d-weak convergence and proved that on bounded sequences in normed spaces it agrees with ordinary weak convergence. Their September 2026 preprint constructs a specific unbounded d-weakly null sequence in \(C[0,1]\) using functions with disjoint supports, and proves that d-weak convergence is exactly convergence in the associated metric-functional topology.

The closest located result extends that compact-function-space mechanism to every infinite \(C(K)\), with arbitrary positive norm profiles. The present statement is not an application of that theorem to a full \(C(K)\)-space: a general AM-space is only represented as a closed sublattice of \(C(K)\), and metric functionals of a subspace need not be restrictions of ambient metric functionals. The proof above instead runs the internal-functional argument directly inside the represented sublattice, which yields the all-disjoint-sequences theorem and the finite/infinite AM-space topology dichotomy.

## Limitations
The theorem is specific to AM-spaces. The proof relies on a supremum-norm representation in which each center \(w\) attains its norm at a point and disjointness is pointwise. It does not assert the same behavior in arbitrary Banach lattices. The result is structurally close to the recent \(C(K)\) disjoint-support construction, so an equivalent abstract-AM formulation could exist under different terminology despite the implication-level searches reported in the review.

## References
1. A. W. Gutiérrez and O. Nevanlinna, *A Weak Topology on Metric Spaces*, arXiv:2609.19368v1, 16 September 2026.
2. A. W. Gutiérrez and O. Nevanlinna, *Metric functionals and weak convergence*, Z. Anal. Anwend., published online 3 June 2026, DOI 10.4171/ZAA/1828; arXiv:2506.04154.
3. S. Kakutani, *Concrete representation of abstract (M)-spaces (A characterization of the space of continuous functions)*, Ann. of Math. 42 (1941), 994--1024.
4. T. Oikhberg, *A note on latticeability and algebrability*, J. Math. Anal. Appl. 434 (2016), 523--537, DOI 10.1016/j.jmaa.2015.09.025.
