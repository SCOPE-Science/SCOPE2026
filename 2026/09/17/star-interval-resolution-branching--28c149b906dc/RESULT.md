# Branching controls interval-resolution complexity on star posets

## Summary

Let \(P\) be a finite connected poset whose Hasse diagram is an arbitrarily oriented star \(K_{1,r}\) with \(r\ge 1\) leaves, and let
\[
\Lambda_P=\operatorname{End}_P\!\left(\bigoplus_{I\in\operatorname{Int}(P)}\mathbb I_I\right)^{\mathrm{op}}
\]
be its interval endomorphism algebra over a field \(k\). Then
\[
\boxed{\operatorname{gldim}\Lambda_P=\max\{2,r\}}
\]
for every orientation and every coefficient field. Equivalently, using the relative Auslander formula,
\[
\boxed{\operatorname{int\!\!-res\!\!-gldim}_k P=\max\{0,r-2\}}.
\]

Thus the interval-resolution global dimension of a star depends only on its number of leaves, not on the orientation. The cases \(r\le2\) reduce to type \(A\), and \(r=3\) recovers the previously known type-\(D_4\) value. The formula gives new quantitative growth for larger stars.

A second consequence is a local branching lower bound for every finite connected poset \(Q\) with at least two elements. If \(\Delta(Q)\) is the maximum degree of its Hasse diagram, then
\[
\boxed{\operatorname{int\!\!-res\!\!-gldim}_k Q\ge \max\{0,\Delta(Q)-2\}},
\qquad
\boxed{\operatorname{gldim}\Lambda_Q\ge \max\{2,\Delta(Q)\}}.
\]
The bound is sharp on stars.

## Context

Aoki recently proved an exact combinatorial formula for the global dimension of the interval endomorphism algebra of an arbitrary finite connected poset. For intervals \(S,C\subseteq P\), define
\[
\bar\omega(S,C)=|\operatorname{Max}(C\setminus S)|+|\operatorname{Min}(S\setminus C)|.
\]
If \(\mathcal W(S,C)\) is the set of intervals \(T\) in which \(S\) has extremal upper boundary and \(C\) has extremal lower boundary, then \((S,C)\) is called saturated when \(\mathcal W(S,C)\) is a singleton. Aoki's Theorem 6.5 gives
\[
\operatorname{gldim}\Lambda_P=\Omega(P):=
\max_{(S,C)\text{ saturated}}\bar\omega(S,C).
\]
The same paper recalls the relative Auslander formula
\[
\operatorname{int\!\!-res\!\!-gldim}_kP=\operatorname{gldim}\Lambda_P-2
\]
for \(|P|>1\).

Earlier, Aoki--Escolar--Tada proved that interval-resolution global dimension is monotone under passage to full subposets. Their paper also computes the value \(1\) for every orientation of \(D_4\), which is exactly the \(r=3\) star case after subtracting two from the interval-endomorphism global dimension.

## The oriented-star theorem

Let \(P=P_{p,q}\) have center \(c\), lower leaves
\[
L=\{\ell_1,\ldots,\ell_p\},
\]
and upper leaves
\[
U=\{u_1,\ldots,u_q\},
\]
with cover relations \(\ell_i\lessdot c\lessdot u_j\). Here \(p,q\ge0\) and \(p+q=r\ge1\). Every orientation of the undirected star is of this form after labeling incoming and outgoing edges.

### Theorem

For every field \(k\),
\[
\operatorname{gldim}\Lambda_{P_{p,q}}=\max\{2,p+q\}.
\]
Hence
\[
\operatorname{int\!\!-res\!\!-gldim}_k P_{p,q}=\max\{0,p+q-2\}.
\]

### Proof

An interval in \(P_{p,q}\) has one of two forms.

1. It is a singleton leaf.
2. It contains \(c\), in which case it is
   \[
   I_{A,B}=\{c\}\cup A\cup B
   \]
   for arbitrary \(A\subseteq L\) and \(B\subseteq U\).

Indeed, a subset containing \(c\) is connected, and it is convex precisely because whenever it contains both a lower and an upper leaf it already contains the only element between them, namely \(c\). A subset not containing \(c\) cannot contain two leaves and remain an interval: two leaves on the same side are disconnected, while a lower and an upper leaf have \(c\) strictly between them and hence fail convexity.

Assume first that \(r\ge2\). We show that \(\bar\omega(S,C)\le r\) for every pair of intervals, hence in particular for every saturated pair.

If both \(S\) and \(C\) contain \(c\), then \(S\cap C\ne\varnothing\), so
\[
\bar\omega(S,C)
\le |C\setminus S|+|S\setminus C|
=|S\triangle C|
\le r.
\]

If both are singleton leaves, then \(\bar\omega(S,C)\le2\le r\).

It remains to consider one central interval \(X\ni c\) and one singleton leaf \(\{x\}\). If \(x\in X\), the two intervals intersect and the same symmetric-difference bound gives \(\bar\omega\le r\). Suppose \(x\notin X\). The singleton contributes at most one to \(\bar\omega\). If \(X=\{c\}\), then \(\bar\omega\le2\le r\). If \(|X|\ge2\), then \(X\) contains \(c\) and at least one leaf. Therefore not every element of \(X\) is minimal and not every element is maximal: if the chosen leaf is below \(c\), then \(c\) is not minimal and the leaf is not maximal; if it is above \(c\), then \(c\) is not maximal and the leaf is not minimal. Consequently
\[
|\operatorname{Min}(X)|\le |X|-1,
\qquad
|\operatorname{Max}(X)|\le |X|-1.
\]
Since \(x\notin X\), we also have \(|X|\le r\). Thus in either ordering of the pair,
\[
\bar\omega(S,C)\le 1+(|X|-1)=|X|\le r.
\]
This proves \(\Omega(P_{p,q})\le r\) for \(r\ge2\).

For the matching lower bound, set
\[
S=L\cup\{c\},
\qquad
C=\{c\}\cup U.
\]
Both are intervals. In \(P\), \(S\) is a relative downset with extremal upper boundary \(U=\operatorname{Max}(P\setminus S)\), and \(C\) is a relative upset with extremal lower boundary \(L=\operatorname{Min}(P\setminus C)\). Hence \(P\in\mathcal W(S,C)\). Since \(S\cup C=P\), no other interval can belong to \(\mathcal W(S,C)\); therefore \((S,C)\) is saturated. Moreover,
\[
\bar\omega(S,C)=|U|+|L|=q+p=r.
\]
Thus \(\Omega(P_{p,q})=r\) whenever \(r\ge2\).

For \(r=1\), the poset is a two-element chain. Let \(a<b\) be its two elements and take \(S=\{a\}\), \(C=\{b\}\). The only interval containing both is \(P\); the singleton \(S\) has extremal upper boundary in \(P\), and \(C\) has extremal lower boundary in \(P\). Hence \((S,C)\) is saturated and
\[
\bar\omega(S,C)=1+1=2.
\]
Since \(P\) has only two elements, \(\bar\omega\le2\) for every pair, so \(\Omega(P)=2\).

Aoki's global-dimension formula now gives
\[
\operatorname{gldim}\Lambda_{P_{p,q}}=\max\{2,r\}.
\]
Applying the relative Auslander formula for \(|P|>1\) gives
\[
\operatorname{int\!\!-res\!\!-gldim}_kP_{p,q}=\max\{0,r-2\}.
\]
The proof is independent of the coefficient field. \(\square\)

## Corollary: a maximum-degree lower bound

Let \(Q\) be any finite connected poset with \(|Q|>1\), and let \(v\) be a vertex of maximum Hasse degree \(d=\Delta(Q)\). Form the full subposet \(Q_v\) on \(v\) together with all Hasse neighbors of \(v\).

No two lower neighbors of \(v\) are comparable, because each is covered by \(v\); dually, no two upper neighbors are comparable. Every lower neighbor is below every upper neighbor through \(v\). Therefore the Hasse diagram of \(Q_v\) is an oriented star with \(d\) leaves.

By the star theorem,
\[
\operatorname{int\!\!-res\!\!-gldim}_k Q_v=\max\{0,d-2\}.
\]
By Aoki--Escolar--Tada monotonicity for full subposets,
\[
\operatorname{int\!\!-res\!\!-gldim}_k Q_v
\le
\operatorname{int\!\!-res\!\!-gldim}_k Q.
\]
Hence
\[
\operatorname{int\!\!-res\!\!-gldim}_k Q\ge\max\{0,\Delta(Q)-2\}.
\]
Using the relative Auslander formula again gives
\[
\operatorname{gldim}\Lambda_Q\ge\max\{2,\Delta(Q)\}.
\]
Both inequalities are attained by stars.

## Consequence for hereditary incidence algebras

If the undirected Hasse graph of a finite poset is a tree, there is a unique saturated chain between comparable vertices. Its incidence algebra is therefore the path algebra of its acyclic Hasse quiver, hence is hereditary. In particular, every nontrivial star poset has ordinary incidence-algebra global dimension \(1\).

Nevertheless, for stars with \(r\) leaves,
\[
\operatorname{int\!\!-res\!\!-gldim}_kP=\max\{0,r-2\},
\]
which is unbounded as \(r\to\infty\). Thus interval-relative homological complexity can grow without bound inside a family whose ordinary incidence algebras all remain hereditary.

## Computational check

The accompanying script `artifacts/verify_star_interval_gldim.py` independently enumerates all intervals, tests Aoki's extremal-boundary conditions, enumerates saturated pairs, and maximizes \(\bar\omega\) for every split \(r=p+q\) with \(1\le r\le6\). It confirms
\[
\operatorname{gldim}\Lambda_{P_{p,q}}=\max\{2,r\}
\]
for every one of these orientations. This finite check is supporting evidence only; the proof above is general.

## Originality boundary

The formula is an application of Aoki's general saturated-pair theorem, not a replacement for it. Known coverage includes:

- \(r\le2\): the Hasse quiver is type \(A\), for which interval-resolution global dimension is already known to be zero;
- \(r=3\): the Hasse quiver is type \(D_4\), for which Aoki--Escolar--Tada already state interval-resolution global dimension \(1\) for every orientation.

The claimed new contribution is the exact orientation-independent formula for arbitrary stars, especially \(r\ge4\), together with the sharp maximum-Hasse-degree lower bound for arbitrary finite posets and the resulting unboundedness on hereditary star incidence algebras. Exact-formula and synonymous literature searches did not locate these statements; see `REVIEW.md` for the search scope and residual uncertainty.

## References

1. T. Aoki, *Interval endomorphism algebras of posets: Reedy structure, combinatorics, and homological theory*, arXiv:2609.15927v1 (2026). In particular Theorems 6.3 and 6.5, and the relative Auslander formula discussed in the introduction. https://arxiv.org/abs/2609.15927
2. T. Aoki, E. G. Escolar, S. Tada, *Summand-injectivity of interval covers and monotonicity of interval resolution global dimensions*, Journal of Applied and Computational Topology 9, Article 13 (2025), DOI 10.1007/s41468-025-00210-2. In particular Theorem 4.1 and Example 2.6. https://doi.org/10.1007/s41468-025-00210-2
3. H. Asashiba, E. G. Escolar, K. Nakashima, M. Yoshiwaki, *Approximation by interval-decomposables and interval resolutions of persistence modules*, Journal of Pure and Applied Algebra 227 (2023), 107397, DOI 10.1016/j.jpaa.2023.107397. https://arxiv.org/abs/2207.03663
