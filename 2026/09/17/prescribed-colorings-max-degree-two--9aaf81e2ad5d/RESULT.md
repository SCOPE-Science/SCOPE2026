# Exact prescribed color-class sizes for graphs of maximum degree two

## Statement

Let \(G\) be a finite simple graph on \(n\) vertices with \(\Delta(G)\le 2\). Let
\(o(G)\) denote the number of connected components of \(G\) that are odd cycles,
and let \(\alpha(G)\) be the independence number. Let
\(a_1,\ldots,a_q\) be nonnegative integers with \(\sum_i a_i=n\).

**Theorem.** There is a proper vertex coloring of \(G\) in which color \(i\)
is used exactly \(a_i\) times if and only if

\[
 a_i\le \alpha(G)\quad\text{for every }i,
 \tag{1}
\]

and

\[
 a_i+a_j\le n-o(G)\quad\text{for every distinct }i,j.
 \tag{2}
\]

Equivalently, after deleting zero entries and sorting the requested class sizes as
\(\lambda_1\ge\lambda_2\ge\cdots\), feasibility is characterized by just

\[
 \lambda_1\le \alpha(G),\qquad
 \lambda_1+\lambda_2\le n-o(G),
\]

where the second inequality is vacuous when there is only one positive part.

Thus the stable-partition types, equivalently the monomial support of the chromatic
symmetric function \(X_G\), have an exact two-inequality description for every
graph of maximum degree two. In particular, for any fixed finite number of color
variables, \(X_G\) has saturated Newton polytope: every lattice point of its Newton
polytope is a coloring weight.

## Why the two obstructions are necessary

Each color class is an independent set, giving (1). For (2), fix two colors.
On every odd-cycle component their union omits at least one vertex, because an odd
cycle cannot be properly colored with two colors. On all other components the two
classes can cover at most all vertices. Hence any two classes contain at most
\(n-o(G)\) vertices in total.

The content is that there are no further global obstructions.

## Local lemma for paths and cycles

Let \(Q\) be a path or a cycle of order \(L\), and let
\(x_1,\ldots,x_q\) be nonnegative integers summing to \(L\).
Then \(Q\) has a proper coloring with these exact multiplicities if and only if

\[
 \max_i x_i\le \alpha(Q).
 \tag{3}
\]

Necessity is immediate. For sufficiency, choose a color \(A\) of maximum
multiplicity \(M\), and write \(R=L-M\) for the number of non-\(A\) symbols.

For a path, (3) says \(M\le\lceil L/2\rceil\), equivalently
\(R\ge M-1\). Use \(M\) ordered gaps \(G_1,\ldots,G_M\) and form

\[
 A\,G_1\,A\,G_2\cdots A\,G_{M-1}\,A\,G_M.
\]

For each other color having multiplicity \(b\le M\), assign its \(b\) copies to
\(b\) consecutive gaps in a cyclic walk through \(G_1,\ldots,G_M\), continuing
the walk where the previous color stopped. Because \(b\le M\), no gap receives
two copies of the same non-\(A\) color. Because the total number \(R\) of assigned
copies is at least \(M-1\), the first \(M-1\) gaps encountered in the cyclic walk
are nonempty. Within each gap, list its distinct colors in arbitrary order. Thus
no equal symbols are adjacent, including across gap boundaries.

For a cycle, (3) says \(M\le\lfloor L/2\rfloor\), so \(R\ge M\). Place the
\(M\) copies of \(A\) cyclically and regard the \(M\) intervals between
consecutive copies as gaps. Assign every other color to distinct gaps by the same
cyclic procedure. Since \(R\ge M\), every gap is nonempty, and since each gap
contains any non-\(A\) color at most once, an arbitrary ordering inside each gap
produces a proper cyclic word. This proves the lemma.

## Global proof by a capacitated flow

Write the connected components of \(G\) as \(Q_1,\ldots,Q_t\). Put

\[
 L_j=|V(Q_j)|,\qquad c_j=\alpha(Q_j).
\]

We seek integers \(x_{ij}\) giving the number of vertices of color \(i\) used
inside component \(Q_j\). By the local lemma, it is enough and necessary to have

\[
 \sum_jx_{ij}=a_i,\qquad
 \sum_i x_{ij}=L_j,\qquad
 0\le x_{ij}\le c_j.
 \tag{4}
\]

These are exactly the integral flows of value \(n\) in the network

- source \(\to\) color \(i\), capacity \(a_i\);
- color \(i\to Q_j\), capacity \(c_j\);
- \(Q_j\to\) sink, capacity \(L_j\).

All capacities are integral. By max-flow/min-cut, a full integral flow exists if
and only if, for every set \(S\) of colors,

\[
 \sum_{i\in S}a_i
 \le
 \sum_{j=1}^t \min\{L_j,\,|S|c_j\}.
 \tag{5}
\]

Indeed, in a minimum cut with precisely the colors in \(S\) on the source side,
each component independently contributes the cheaper of cutting all
\(|S|\) incoming edges (cost \(|S|c_j\)) or its edge to the sink (cost \(L_j\)).

Now evaluate (5) by \(|S|\).

* If \(|S|=1\), its right side is \(\sum_j c_j=\alpha(G)\), exactly (1).
* If \(|S|=2\), a path or even cycle contributes its full order \(L_j\), while an
  odd cycle \(C_{2r+1}\) contributes \(2r=L_j-1\). Therefore the right side is
  exactly \(n-o(G)\), giving (2).
* If \(|S|\ge3\), every path or cycle satisfies \(|S|c_j\ge L_j\), including
  \(C_3\) at equality. Hence the right side is \(n\), and (5) is automatic.

Thus (1) and (2) are sufficient. The resulting integral flow gives local
multiplicities satisfying the local lemma on every component, and concatenating
those component colorings gives the required proper coloring of \(G\).

## Consequence for the remainder-sensitive skewed-coloring conjecture at degree two

Kuchukova--Perkins--Povill formulated a prescribed-coloring conjecture for graphs
of bounded maximum degree. Birken subsequently proved the floor-bound version and,
in Conjecture 5 of arXiv:2609.18629, proposed the following remainder-sensitive
strengthening. Write

\[
 n=s(r+1)+m,\qquad m\in\{1,\ldots,r\}.
\]

The proposed universal condition allows at most \(m\) requested classes of size
\(s+1\), with every other class of size at most \(s\).

The theorem above proves this conjecture for \(r=2\). Indeed, if
\(n=3s+m\) with \(m\in\{1,2\}\), then every graph with maximum degree at most two
has

\[
 \alpha(G)\ge \lceil n/3\rceil=s+1
\]

and, because every odd-cycle component has at least three vertices,

\[
 o(G)\le \lfloor n/3\rfloor=s.
\]

For \(m=1\), the sum of the two largest permitted classes is at most
\((s+1)+s=2s+1\), while \(n-o(G)\ge3s+1-s=2s+1\). For \(m=2\), it is at most
\(2(s+1)=2s+2\), while \(n-o(G)\ge3s+2-s=2s+2\). Hence the exact criterion applies.

This corollary is weaker than the full theorem: the theorem determines every
feasible prescribed profile for each individual maximum-degree-two graph, not only
the profiles guaranteed uniformly over the whole class.

## Computational stress test

The proof is general and does not rely on computation. As an adversarial finite
check, `artifacts/check_degree2_prescribed.py` enumerates every disjoint union of
paths and cycles of total order at most 11, every integer partition of its order,
and compares the criterion above with direct backtracking for an exact proper
coloring. It checks 451 component-multiset graph types and 17,073 graph/partition
pairs. The saved output is `artifacts/check_degree2_prescribed.out`.

## Scope and limitations

The result concerns finite simple graphs with maximum degree at most two. It gives
existence and an exact support characterization; it does not count the colorings,
optimize a sampling algorithm, or address the higher-degree remainder-sensitive
conjecture. Originality is asserted only to the best of our knowledge after the
search documented in `REVIEW.md`.

## References

1. A. Kuchukova, W. Perkins, X. Povill, *Sampling Colorings with Fixed Color Class Sizes*, ICALP 2026; arXiv:2603.08259.
2. M. Birken, *A Hajnal-Szemerédi Theorem for Skewed Colorings*, arXiv:2609.18629 (2026).
3. R. P. Stanley, *A symmetric function generalization of the chromatic polynomial of a graph*, Advances in Mathematics 111 (1995), 166--194.
4. J. P. Matherne, A. H. Morales, J. Selover, *The Newton polytope and Lorentzian property of chromatic symmetric functions*, Selecta Mathematica 30, 42 (2024); arXiv:2201.07333.
