# Majority C-colorings of generalized windmill graphs

## Finding

For integers
\[
n\ge1,\qquad m\ge2,
\]
let
\[
W_{n,m}=K_1\vee nK_m
\]
be the generalized windmill graph. Write \(z\) for the universal center and call the \(n\) copies of \(K_m\) the blades.

Every majority C-coloring of \(W_{n,m}\) has the following exact form:

1. every blade is monochromatic;
2. at least
\[
\left\lceil\frac n2\right\rceil
\]
blades have the same color as \(z\).

Conversely, every coloring satisfying these two conditions is a majority C-coloring.

Therefore
\[
\boxed{
\overline\chi_{\geqslant}(W_{n,m})
=
1+\left\lfloor\frac n2\right\rfloor
}
\]
for every \(m\ge2\), and the complete spectrum of feasible color counts is
\[
\boxed{
\left\{
1,2,\ldots,
1+\left\lfloor\frac n2\right\rfloor
\right\}.
}
\]

The structure also gives an exact enumeration. Let \(A_q(n,m)\) be the number of surjective majority C-colorings onto a fixed labeled palette of \(q\) colors, and put
\[
r=\left\lfloor\frac n2\right\rfloor.
\]
If
\[
\left\{\begin{matrix}t\\j\end{matrix}\right\}
\]
denotes a Stirling number of the second kind, then
\[
\boxed{
A_q(n,m)
=
q!\sum_{t=q-1}^{r}
\binom nt
\left\{\begin{matrix}t\\q-1\end{matrix}\right\}
}
\]
for
\[
1\le q\le r+1,
\]
and
\[
A_q(n,m)=0
\]
for larger \(q\).

In particular, the number of labeled optimal colorings is
\[
\boxed{
A_{r+1}(n,m)
=
(r+1)!\binom nr.
}
\]

The formulas are independent of the blade order \(m\) once \(m\ge2\).

## Assumptions and scope

A majority C-coloring of a finite simple graph is a surjective vertex coloring in which every vertex shares its color with at least half of its open neighbors.

The graph \(W_{n,m}\) consists of one universal center and \(n\) mutually anticomplete \(m\)-cliques. The restriction \(m\ge2\) is essential: when \(m=1\), \(W_{n,1}\) is a star and its majority C-chromatic number is \(1\).

Colors are labeled in the enumeration \(A_q(n,m)\). No quotient by graph automorphisms or color permutations is taken.

## Proof

Fix a majority C-coloring \(\varphi\), and let
\[
\alpha=\varphi(z)
\]
be the center color. Consider one blade \(B\cong K_m\).

Suppose first that \(B\) contains \(a>0\) vertices of color \(\alpha\). Every such vertex has degree \(m\): it sees the center and the other \(m-1\) vertices of its blade. It has exactly \(a\) same-colored neighbors, namely the center together with the other \(a-1\) \(\alpha\)-vertices in \(B\). Hence
\[
a\ge\left\lceil\frac m2\right\rceil.
\]

Now consider a non-center color that appears \(t\) times in \(B\). A vertex of this color has exactly \(t-1\) same-colored neighbors, all inside \(B\), so
\[
t-1\ge\frac m2.
\]
Thus
\[
t\ge
\left\lceil\frac m2\right\rceil+1.
\]

If
\[
0<a<m,
\]
the number of vertices of \(B\) not colored \(\alpha\) is at most
\[
m-\left\lceil\frac m2\right\rceil
=
\left\lfloor\frac m2\right\rfloor,
\]
which is smaller than the minimum size of any non-\(\alpha\) color block. This is impossible. Hence a blade containing the center color is entirely colored \(\alpha\).

If a blade contains no \(\alpha\)-vertex, every color used on it must occur at least
\[
\left\lceil\frac m2\right\rceil+1
>
\frac m2
\]
times. Two such color classes cannot fit in \(m\) vertices. Hence this blade also is monochromatic.

We have proved that every blade is monochromatic.

Let \(b\) be the number of blades colored \(\alpha\). The center has degree \(nm\) and exactly \(bm\) neighbors of its own color. Its majority condition is
\[
bm\ge\frac{nm}{2},
\]
equivalently
\[
b\ge\left\lceil\frac n2\right\rceil.
\]

Conversely, suppose every blade is monochromatic and at least \(\lceil n/2\rceil\) blades have the center color. The center then satisfies the majority condition. A vertex in a center-colored blade has all \(m\) of its neighbors in the blade-plus-center clique colored the same. A vertex in any other blade has \(m-1\) same-colored neighbors inside its blade, and
\[
m-1\ge\frac m2
\]
for \(m\ge2\). Thus every vertex satisfies the majority condition.

This proves the structural characterization.

At most
\[
r=\left\lfloor\frac n2\right\rfloor
\]
blades can avoid the center color. Distinct non-center colors require distinct non-center blades, so at most \(r+1\) colors can occur. Equality is achieved by choosing exactly \(r\) non-center blades, assigning them pairwise distinct colors, and assigning the center color everywhere else. This proves
\[
\overline\chi_{\geqslant}(W_{n,m})=r+1.
\]

The same construction with any number
\[
0\le s\le r
\]
of non-center blades gives \(s+1\) colors, proving the spectrum statement.

For the exact enumeration, fix a labeled \(q\)-color palette. Let \(t\) be the number of blades not colored with the center color. Necessarily
\[
q-1\le t\le r.
\]
Choose the center color in \(q\) ways and choose the \(t\) non-center blades in
\[
\binom nt
\]
ways. The \(t\) selected blades must use all \(q-1\) remaining colors. The number of surjections from those \(t\) labeled blades onto the \(q-1\) labeled non-center colors is
\[
(q-1)!
\left\{\begin{matrix}t\\q-1\end{matrix}\right\}.
\]
Summing over \(t\) gives
\[
A_q(n,m)
=
q!\sum_{t=q-1}^{r}
\binom nt
\left\{\begin{matrix}t\\q-1\end{matrix}\right\}.
\]
For \(q=r+1\), only \(t=r\) contributes, giving
\[
A_{r+1}(n,m)
=
(r+1)!\binom nr.
\]

## Verification

The accompanying script `artifacts/verify.py` constructs the generalized windmill directly from its edges and checks the majority condition vertex by vertex.

For
\[
1\le n\le4,\qquad 2\le m\le3,
\]
it exhaustively enumerates every surjective coloring for every color count in the predicted spectrum. It independently compares the graph-theoretic majority condition with the blade-monochromatic structural criterion and compares the exact number of valid colorings with the Stirling-number formula.

It also checks explicit spectrum constructions for every
\[
1\le n\le30,\qquad 2\le m\le10.
\]

Replay output:

`ALL CHECKS PASSED; parameter_cases=16; surjective_assignments_checked=1597912; construction_cases=2295; exhaustive_n=1..4,m=2..3`

The computation is corroborative only. The arbitrary-\(n,m\) theorem follows from the analytic blade argument above.

## Relationship to prior work

Bujtás, Dettlaff, Furmańczyk, and Laskowska introduced majority C-coloring in 2026. Their Definition 1 uses exactly the open-neighborhood half-majority condition used here and defines the maximum number of colors.

The same paper explicitly treats the Dutch windmill
\[
D_{3,n},
\]
also known as the friendship graph, and states
\[
\overline\chi_{\geqslant}(D_{3,n})
=
\left\lfloor\frac n2\right\rfloor+1.
\]
That is precisely the scalar \(m=2\) special case of the generalized windmill formula above and is prior work.

The new content is the all-\(m\) structural theorem for
\[
K_1\vee nK_m,\qquad m\ge2,
\]
together with the complete color-count spectrum and the exact number of surjective colorings for every palette size. The inspected paper does not state a generalized-windmill theorem or an enumeration of friendship colorings.

A later 2026 paper develops majority C-coloring for Cartesian products, including exact Hamming-graph and grid results. It concerns a different graph operation and does not imply the join-of-cliques classification here.

## Limitations

The theorem uses the complete-clique structure inside every blade. It does not automatically extend to arbitrary graphs of the form
\[
K_1\vee nH.
\]

The scalar friendship value is not new and is explicitly credited as prior work. The originality claim concerns the generalized blade size, the exact coloring structure, the full spectrum, and the labeled enumeration.

The literature search included both “windmill” and “friendship” terminology, but differently named clique bouquets could still create residual indexing risk.

## References

1. C. Bujtás, M. Dettlaff, H. Furmańczyk, and A. Laskowska, “Majority C-coloring of graphs,” arXiv:2604.20752v1, first public April 22, 2026. AMS Subject Classification \(05C15,05C85\).
2. C. Bujtás, M. Dettlaff, H. Furmańczyk, A. Laskowska, and Z. Tuza, “Majority C-coloring in Cartesian products,” arXiv:2608.27669v1, first public August 27, 2026.
