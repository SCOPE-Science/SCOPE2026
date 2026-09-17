# Screewidth of outerplanar graphs is \(O(\sqrt n)\)

## Statement

Let \(\operatorname{scw}(G)\) denote the screewidth of a connected graph \(G\), as defined through tree-cut decompositions by Cenek et al.

**Theorem.** Every connected simple outerplanar graph \(G\) on \(n\ge 1\) vertices satisfies
\[
\boxed{\operatorname{scw}(G)\le 40\sqrt n.}
\]

Consequently, if
\[
S_{\mathrm{out}}(n)=\max\{\operatorname{scw}(G):G\text{ is connected, simple, outerplanar, }|V(G)|=n\},
\]
then
\[
S_{\mathrm{out}}(n)=\Theta(\sqrt n).
\]
Indeed, the fan graph \(F_{n-1}\) has scramble number at least
\(\lfloor\sqrt{n-1}\rfloor+1\), and scramble number is at most screewidth.

This answers Question 5.1 in Rivera Laboy, *The scramble number of outerplanar graphs* (arXiv:2609.03755v2), which asks whether outerplanar graphs have screewidth \(O(\sqrt n)\).

## Definitions used

A tree-cut decomposition \((T,\mathcal X)\) partitions \(V(G)\) into disjoint bags \(X_t\), one for each node \(t\in V(T)\). The adhesion of a link is the set of graph edges whose endpoints lie on opposite sides of that link. The adhesion of a non-leaf node is the set of graph edges whose endpoints lie in bags belonging to distinct components of the tree after deleting that node. The width is the maximum of the link adhesions and the quantities
\[
|X_t|+|\operatorname{adh}(t)|.
\]
The screewidth is the minimum width over all tree-cut decompositions.

We use two established facts.

1. Screewidth is monotone under taking subgraphs.
2. Rivera Laboy's Lemma 3.10 states that if \(M\) is a maximal outerplanar graph on \(n\ge4\) vertices and \(xy\) is an interior edge with
\[
\deg(x)>\sqrt{2n},\qquad \deg(x)\ge\deg(y),
\]
then there is a set \(H\supseteq\{x,y\}\) such that every component \(C\) of \(M-H\) satisfies
\[
|\delta_M(C)|\le (2+\sqrt2)\sqrt n+4,
\tag{1}
\]
and
\[
|H|\le 2\left\lfloor\frac{\Delta(M)}{\sqrt{2n}}\right\rfloor.
\tag{2}
\]

## A balanced-edge lemma

We first record a standard consequence of the weak dual of a maximal outerplanar graph.

**Lemma.** If \(M\) is maximal outerplanar on \(n\ge6\) vertices, then \(M\) has an interior edge \(xy\) such that every component of \(M-\{x,y\}\) has at most \(3n/4\) vertices.

**Proof.**
The weak dual \(T\) of \(M\) is a tree on
\[
N=n-2
\]
vertices, one for each bounded triangular face, and has maximum degree at most \(3\).

Choose a centroid \(z\) of \(T\), so every component of \(T-z\) has at most \(N/2\) vertices. Let \(Q\) be a largest component of \(T-z\), of size \(s\). Since \(\deg_T(z)\le3\),
\[
s\ge\frac{N-1}{3}.
\]
Let \(e\) be the edge from \(z\) into \(Q\). Deleting \(e\) splits \(T\) into parts of sizes \(s\) and \(N-s\). We have
\[
s\le\frac N2\le\frac{3N}{4},
\]
and, because \(N\ge4\),
\[
N-s\le N-\frac{N-1}{3}
=\frac{2N+1}{3}
\le\frac{3N}{4}.
\]
The dual edge \(e\) corresponds to an interior edge \(xy\) of \(M\). Each side of \(xy\) is a triangulated polygon; after deleting \(x\) and \(y\), the number of remaining vertices on that side equals the number of bounded faces on the corresponding side of \(e\). Hence every component of \(M-\{x,y\}\) has at most \(3N/4<3n/4\) vertices. \(\square\)

## A separator with small edge boundary

Put
\[
B(n)=(2+\sqrt2)\sqrt n+4.
\tag{3}
\]
Choose \(xy\) as in the balanced-edge lemma.

If every component \(C\) of \(M-\{x,y\}\) has
\[
|\delta_M(C)|\le B(n),
\]
take \(H=\{x,y\}\).

Otherwise, for some component \(C\),
\[
|\delta_M(C)|>B(n)>2\sqrt{2n}.
\]
All edges in \(\delta_M(C)\) are incident with \(x\) or \(y\). Therefore
\[
\deg(x)+\deg(y)>2\sqrt{2n},
\]
so the endpoint of larger degree has degree greater than \(\sqrt{2n}\). Rivera Laboy's Lemma 3.10 applies to the interior edge \(xy\). It gives a set \(H\supseteq\{x,y\}\) for which (1) holds for every component of \(M-H\).

In either case we have a set \(H\) such that

- every component \(C\) of \(M-H\) has at most \(3n/4\) vertices, because \(x,y\in H\);
- every such component satisfies \(|\delta_M(C)|\le B(n)\);
- and
\[
|H|\le \max\left\{2,\,
2\left\lfloor\frac{\Delta(M)}{\sqrt{2n}}\right\rfloor\right\}
<\sqrt{2n}
\tag{4}
\]
whenever the second alternative is used (the displayed coarse bound is more than enough below).

## Recursive tree-cut construction

We prove the theorem by induction on \(n\). For \(n\le5\), the one-bag decomposition gives
\[
\operatorname{scw}(G)\le n\le40\sqrt n.
\]

Now let \(n\ge6\). Add edges to \(G\), without adding vertices, until obtaining a maximal outerplanar graph \(M\). By subgraph monotonicity,
\[
\operatorname{scw}(G)\le\operatorname{scw}(M),
\]
so it suffices to decompose \(M\).

Choose \(H\) as above, and let
\[
C_1,\ldots,C_r
\]
be the components of \(M-H\), with \(n_i=|C_i|\le3n/4\).

For each \(i\), by induction choose a tree-cut decomposition
\[
(T_i,\mathcal X_i)
\]
of \(M[C_i]\) of width at most \(40\sqrt{n_i}\), and choose an arbitrary node \(r_i\in V(T_i)\).

Construct a new tree \(T\) by adding one node \(r\), setting
\[
X_r=H,
\]
and joining \(r\) to each \(r_i\). Retain all bags of all \(T_i\). These bags partition \(V(M)\).

We bound the width.

### New links

For the new link \(rr_i\), the adhesion is exactly \(\delta_M(C_i)\), so by (3)
\[
|\operatorname{adh}(rr_i)|\le B(n).
\tag{5}
\]

### Old links inside \(T_i\)

For any old link of \(T_i\), its adhesion in the full graph \(M\) consists of its old adhesion in \(M[C_i]\), together with at most all edges of \(\delta_M(C_i)\). Hence
\[
|\operatorname{adh}_M(\ell)|
\le 40\sqrt{n_i}+B(n).
\tag{6}
\]

### Nodes inside \(T_i\)

The same estimate holds for bag width. Passing from \(M[C_i]\) to \(M\) can add to a node adhesion only edges of \(\delta_M(C_i)\), so for every node \(t\in T_i\),
\[
|X_t|+|\operatorname{adh}_M(t)|
\le40\sqrt{n_i}+B(n).
\tag{7}
\]
This also covers the attachment node \(r_i\), including the case that it was a leaf before the new link was added.

### Central node

Deleting \(r\) from \(T\) separates the trees \(T_i\). There are no graph edges between distinct components \(C_i,C_j\), so the node adhesion at \(r\) is empty. Thus its bag width is simply
\[
|H|<\sqrt{2n}.
\tag{8}
\]

Combining (5)--(8), and using \(n_i\le3n/4\),
\[
\begin{aligned}
w(T,\mathcal X)
&\le
40\sqrt{\frac{3n}{4}}+(2+\sqrt2)\sqrt n+4\\
&=
(20\sqrt3+2+\sqrt2)\sqrt n+4.
\end{aligned}
\]
For \(n\ge6\),
\[
(20\sqrt3+2+\sqrt2)\sqrt n+4\le40\sqrt n,
\]
since
\[
40-(20\sqrt3+2+\sqrt2)
=38-20\sqrt3-\sqrt2
>1.94
>\frac4{\sqrt6}.
\]
Therefore
\[
\operatorname{scw}(M)\le40\sqrt n,
\]
completing the induction and the upper bound.

## Lower order of growth

For the fan \(F_m\), Rivera Laboy's Lemma 3.1 gives
\[
\operatorname{sn}(F_m)\ge\lfloor\sqrt m\rfloor+1.
\]
Cenek et al. prove
\[
\operatorname{sn}(G)\le\operatorname{scw}(G).
\]
Taking \(m=n-1\),
\[
S_{\mathrm{out}}(n)
\ge \operatorname{scw}(F_{n-1})
\ge \lfloor\sqrt{n-1}\rfloor+1.
\]
Together with the theorem,
\[
S_{\mathrm{out}}(n)=\Theta(\sqrt n).
\]

## Context and comparison with prior work

Rivera Laboy proved in arXiv:2609.03755v2 that every simple outerplanar graph has scramble number at most
\[
(2+\sqrt2)\sqrt n+4.
\]
The same paper observes that screewidth gives the desired order for fan and wheel graphs but was not used to prove the general outerplanar result, and explicitly poses:

> Is the screewidth of outerplanar graphs bounded by \(O(\sqrt n)\)?

The theorem above gives an affirmative answer. Its main additional step is to turn the paper's bounded-edge-boundary separator lemma into a recursive tree-cut decomposition. The balance condition is supplied by a separating interior edge obtained from the weak dual. At each recursive attachment, the external boundary of a component can increase every pre-existing link or node adhesion by at most the total boundary size of that component; geometric decay of component order absorbs these additive \(O(\sqrt n)\) terms.

The constant \(40\) is not intended to be sharp.

## Limitations

The result concerns screewidth, not divisorial gonality; it does not answer Question 5.2 of Rivera Laboy concerning whether gonality of outerplanar graphs is \(O(\sqrt n)\).

The numerical constant \(40\) is a coarse consequence of the \(3/4\)-balanced separating edge and the boundary constant in Lemma 3.10. Substantially smaller constants may be possible.

The proof uses Rivera Laboy's Lemma 3.10 from arXiv:2609.03755v2 as an input. The relevant theorem statement and proof were inspected. Originality is asserted only to the best of our knowledge. The source posing Question 5.1 was last revised on 15 September 2026, and targeted searches for outerplanar screewidth bounds and equivalent formulations found no later or independent resolution. Because the question is very recent, unindexed or unpublished parallel work remains a residual risk.

No independent validation is asserted.

## References

1. Doel Rivera Laboy, *The scramble number of outerplanar graphs*, arXiv:2609.03755v2 (2026), especially Lemma 3.1, Lemma 3.10, Theorem 3.15, and Question 5.1. https://arxiv.org/abs/2609.03755
2. Lisa Cenek, Lizzie Ferguson, Eyobel Gebre, Cassandra Marcussen, Jason Meintjes, Ralph Morrison, Liz Ostermeyer, Shefali Ramakrishna, and Ben Weber, *Scramble number and tree-cut decompositions*, arXiv:2209.01459 (2022), especially the definition of screewidth, Proposition 3.8, and the inequality \(\operatorname{sn}(G)\le\operatorname{scw}(G)\). https://arxiv.org/abs/2209.01459
