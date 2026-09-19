# A sharp Hausdorff phase transition for metric-functional weak topologies on CAT(0) comb trees

## Statement

Let \(L=(L_n)_{n\ge 1}\) be a sequence of positive real numbers. Define the **comb tree**
\(T_L\) by taking a geodesic ray \(\gamma=[0,\infty)\), rooted at \(o=\gamma(0)\), and
attaching at \(\gamma(n)\) a terminal segment of length \(L_n\), with endpoint \(x_n\).
With the path metric, \(T_L\) is a proper, complete, locally finite \(\mathbb R\)-tree,
hence a geodesic CAT(0) space.

For a metric space \((X,d)\) with basepoint \(o\), write
\[
h_w(z)=d(z,w)-d(o,w)
\]
and let \(X^\diamond\) be the pointwise closure of the internal metric functionals
\(\{h_w:w\in X\}\). Following Gutiérrez--Nevanlinna, a net \(z_i\) converges
\(d\)-weakly to \(z\) if
\[
\liminf_i h(z_i)\ge h(z)\qquad\text{for every }h\in X^\diamond,
\]
and \(\sigma(X,X^\diamond)\) denotes the topology whose convergent nets are exactly
the \(d\)-weakly convergent nets.

For \(z\in T_L\), let \(p(z)\) be the distance from \(o\) to the attachment point of
the component containing \(z\): on the spine \(p(\gamma(s))=s\), while on the \(n\)-th
tooth \(p(z)=n\). Put \(r(z)=d(z,\gamma)\). Then
\[
b(z):=r(z)-p(z)
\]
is the Busemann function of the unique infinite end of the comb.

### Theorem

1. The full metric-functional compactification is
   \[
   \boxed{T_L^\diamond=\{h_w:w\in T_L\}\cup\{b\}.}
   \]

2. The endpoint sequence has the exact \(d\)-weak limit set
   \[
   \boxed{
   \Lambda_d(x_n)
   =
   \left\{z\in T_L:
   b(z)\le \liminf_{n\to\infty}(L_n-n)
   \right\},
   }
   \]
   with the conventions that a right-hand threshold of \(-\infty\) gives the empty
   set and \(+\infty\) gives all of \(T_L\).

3. There is a sharp global topological dichotomy:
   \[
   \boxed{
   \sigma(T_L,T_L^\diamond)=\text{the metric topology}
   \quad\Longleftrightarrow\quad
   L_n-n\longrightarrow-\infty.
   }
   \]
   If \(L_n-n\not\to-\infty\), then
   \(\sigma(T_L,T_L^\diamond)\) is non-Hausdorff.

4. At the critical comb \(L_n=n\),
   \[
   \boxed{x_n\to z\ \text{in }\sigma(T_L,T_L^\diamond)
   \quad\text{for every }z\in T_L.}
   \]
   Consequently the weak topology is hyperconnected: every two nonempty weak-open
   sets meet. It is nevertheless \(T_1\).

Thus properness, local finiteness, geodesicity, and CAT(0) curvature do not by
themselves force the metric-functional weak topology to be Hausdorff. On this natural
one-ended family, the exact threshold is the horospherical excess \(L_n-n\).

## Proof

### 1. Geometry and the unique boundary metric functional

A closed ball about \(o\) of radius \(R\) meets only the finitely many teeth attached
at integers \(n\le R\), and its intersection with each such tooth is a compact segment.
Hence the ball is compact. Any closed ball centered elsewhere is a closed subset of a
sufficiently large ball about \(o\), so \(T_L\) is proper. Being a metric tree, it is an
\(\mathbb R\)-tree and therefore CAT(0).

For a fixed \(z\in T_L\), if \(w\in T_L\) satisfies \(p(w)>p(z)\), then \(z\) and \(w\)
lie on different teeth (or one lies on the spine), and the tree distance gives
\[
d(z,w)=r(z)+r(w)+p(w)-p(z).
\]
Since \(d(o,w)=p(w)+r(w)\),
\[
h_w(z)=r(z)-p(z)=b(z).
\]
In particular, if \(w=\gamma(t)\) and \(t\to\infty\), then \(h_w(z)\to b(z)\) for every
fixed \(z\), so \(b\in T_L^\diamond\).

Conversely, let a net of internals \(h_{w_i}\) converge pointwise to some
\(h\in T_L^\diamond\). If \(p(w_i)\to\infty\), then the preceding identity is eventually
exact for each fixed \(z\), and \(h=b\). If \(p(w_i)\not\to\infty\), there is a subnet
with \(p(w_i)\le R\) for some finite \(R\). The set
\[
\{w\in T_L:p(w)\le R\}
\]
is a finite union of compact segments, hence compact. A further subnet converges
metrically to some \(w\), and continuity of \(u\mapsto h_u(z)\) for each fixed \(z\)
gives \(h=h_w\). This proves
\[
T_L^\diamond=T_L^\vee\cup\{b\}.
\]

### 2. Exact limit set of the tooth endpoints

Fix \(w\in T_L\) and write \(q=p(w)\). For every integer \(n>q\),
\[
d(x_n,w)=L_n+(n-q)+r(w),
\]
hence
\[
h_w(x_n)=n+L_n-2q\longrightarrow+\infty.
\]
On the other hand,
\[
b(x_n)=L_n-n.
\]
Since the metric functionals are exactly the internals and \(b\), the definition of
\(d\)-weak convergence immediately yields
\[
x_n\overset{d}{\rightharpoonup}z
\quad\Longleftrightarrow\quad
\liminf_n(L_n-n)\ge b(z).
\]
This is the asserted formula for \(\Lambda_d(x_n)\).

### 3. A compact-range lemma for nets

We use a net version of the compactness mechanism behind the bounded-sequence result
of Gutiérrez--Nevanlinna.

**Lemma.** In any metric space, if \(z_i\) converges \(d\)-weakly to \(z\) and the
range of the net has compact metric closure, then \(z_i\to z\) metrically.

Indeed, otherwise some subnet stays outside a fixed ball \(B(z,\varepsilon)\).
Compactness gives a further subnet converging metrically to a point \(y\) with
\(d(y,z)\ge\varepsilon\). Every subnet of a \(d\)-weakly convergent net has the same
\(d\)-weak limit \(z\). Testing against the internal functional
\[
h_y(u)=d(u,y)-d(o,y)
\]
gives
\[
-d(o,y)=\lim h_y(z_i)\ge h_y(z)=d(z,y)-d(o,y),
\]
which forces \(d(z,y)=0\), a contradiction.

Therefore, on every bounded subset of a proper metric space, the restriction of
\(\sigma(X,X^\diamond)\) agrees with the metric topology.

### 4. The Hausdorff phase transition

Assume first that
\[
L_n-n\to-\infty.
\]
For every real \(c\), the Busemann superlevel set
\[
\{z\in T_L:b(z)>c\}
\]
is bounded. On the spine, \(b(\gamma(s))=-s\); on the \(n\)-th tooth,
\(b(z)\le L_n-n\). Hence only finitely many far teeth can meet a fixed superlevel set.

If a net converges weakly to \(z\), then it is eventually in the weak-open neighborhood
\[
\{u:b(u)>b(z)-1\},
\]
which is bounded. The compact-range lemma therefore makes the tail converge
metrically to \(z\). Metric convergence always implies \(d\)-weak convergence because
all metric functionals are \(1\)-Lipschitz. Thus the two topologies have exactly the
same convergent nets, and hence are equal.

Now suppose that \(L_n-n\not\to-\infty\). Then there are a real number \(c\) and an
increasing sequence \(n_j\) such that
\[
L_{n_j}-n_j\ge c.
\]
For every fixed internal \(h_w\),
\[
h_w(x_{n_j})\to+\infty,
\]
while
\[
\liminf_j b(x_{n_j})\ge c.
\]
Hence \(x_{n_j}\) converges \(d\)-weakly to every point \(z\) satisfying \(b(z)\le c\).
There are at least two such points on the spine, because \(b(\gamma(t))=-t\).
A single net (indeed, a sequence) therefore has two distinct limits, so the topology
is not Hausdorff.

For \(L_n=n\), every point of the comb satisfies \(b(z)\le0\), while \(b(x_n)=0\).
Thus \(x_n\) converges weakly to every point. If \(U,V\) are nonempty weak-open sets,
choose \(u\in U\) and \(v\in V\); the same sequence is eventually in both \(U\) and
\(V\), so \(U\cap V\ne\varnothing\). Hence the topology is hyperconnected.

Finally, \(\sigma(X,X^\diamond)\) is \(T_1\) for every metric space: for \(x\ne y\),
the basic neighborhood
\[
B\!\left(x,\{h_y\},\frac{d(x,y)}2\right)
\]
contains \(x\) and excludes \(y\). Thus the critical comb gives a \(T_1\),
hyperconnected, non-Hausdorff weak topology.

## Context and significance

Gutiérrez and Nevanlinna introduced \(d\)-weak convergence through metric functionals
and, in September 2026, constructed the topology \(\sigma(X,X^\diamond)\) whose net
convergence is exactly \(d\)-weak convergence. Their paper proves that this topology is
coarser than the metric topology and gives a non-Hausdorff example on the snowflaked
real line. Their earlier work also proves that bounded \(d\)-weakly convergent sequences
in proper metric spaces converge strongly.

The theorem above isolates what happens in a substantially more rigid geometric class.
The combs are proper, locally finite, one-ended, geodesic, and CAT(0), yet the
metric-functional weak topology can still be maximally non-Hausdorff in the sense that
one sequence converges to every point. Moreover, the family has an exact threshold:
moving the tooth endpoints only sublinearly below the horosphere is not the relevant
criterion; the topology becomes metric precisely when the Busemann heights
\(L_n-n\) tend uniformly to \(-\infty\).

This does not contradict the established CAT(0) weak topology based on
\(\Delta\)-convergence. That theory uses a different notion of weak convergence,
classically formulated for bounded sequences.

## Limitations

- The exact Hausdorff criterion is proved for the explicit one-ended comb family, not
  for arbitrary proper CAT(0) spaces or arbitrary \(\mathbb R\)-trees.
- No classification is given for multi-ended trees.
- The result concerns the metric-functional topology of Gutiérrez--Nevanlinna, not the
  co-convex topology or the standard CAT(0) weak/\(\Delta\) topology.
- The motivating topology paper is very recent, so an unindexed parallel observation or
  a later revision remains a residual originality risk.

## References

1. A. W. Gutiérrez and O. Nevanlinna, *A Weak Topology on Metric Spaces*,
   arXiv:2609.19368v1 (16 September 2026).
   https://arxiv.org/abs/2609.19368
2. A. W. Gutiérrez and O. Nevanlinna, *Metric functionals and weak convergence*,
   Zeitschrift für Analysis und ihre Anwendungen, published online 3 June 2026.
   https://doi.org/10.4171/ZAA/1828
3. A. Lytchak and A. Petrunin, *Weak topology on CAT(0) spaces*,
   Israel Journal of Mathematics 255 (2023), 763--781.
   https://doi.org/10.1007/s11856-022-2420-5
4. A. Daniilidis, M. I. Garrido, J. A. Jaramillo, and S. Tapia-García,
   *Horofunction extension and metric compactifications*,
   Transactions of the American Mathematical Society, Series B 12 (2025), 1130--1155.
   https://doi.org/10.1090/btran/234
