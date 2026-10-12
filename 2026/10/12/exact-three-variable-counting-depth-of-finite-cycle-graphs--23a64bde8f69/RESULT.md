# Exact three-variable counting depth of finite cycle graphs

Let \(C_n\) be the finite simple undirected cycle on \(n\ge 3\) vertices. Write
\(D^3_{\#}(G)\) for the minimum quantifier depth of a first-order sentence with
counting quantifiers using at most three variables that defines \(G\) up to
isomorphism among finite simple graphs.

## Theorem

For every \(n\ge3\),
\[
D^3_{\#}(C_n)=
\begin{cases}
2,&3\le n\le5,\\[2mm]
1+\left\lceil \log_2\!\left\lfloor n/2\right\rfloor\right\rceil,&n\ge6.
\end{cases}
\]

More precisely, let
\[
H=C_{m_1}\dot\cup\cdots\dot\cup C_{m_t},\qquad t\ge2,
\]
be a nontrivial disjoint union of cycles with
\(\sum_i m_i=n\), and put \(m=\min_i m_i\). Then the least depth of a
three-variable counting sentence distinguishing \(C_n\) from \(H\) is
\[
D^3_{\#}(C_n,H)=1+\lceil\log_2 m\rceil.
\]

The balanced rival
\[
C_{\lfloor n/2\rfloor}\dot\cup C_{\lceil n/2\rceil}
\]
therefore attains the defining-depth maximum for \(n\ge6\).

## Conventions and the WL bridge

Run standard ordered-pair 2-dimensional Weisfeiler--Leman refinement from the
atomic equality/edge/nonedge coloring. For a graph \(G\), let
\(\operatorname{diag}C^{2,r}(G)\) be the multiset of colors of the diagonal
pairs \((v,v)\) after \(r\) refinement rounds.

Pikhurko--Verbitsky, arXiv:1003.4865, Lemma 4.3, records the exact bridge:
\[
\operatorname{diag}C^{2,r}(G)=\operatorname{diag}C^{2,r}(H)
\]
iff Duplicator wins the \((r+1)\)-round three-pebble counting game on
\(G,H\). Together with the counting Ehrenfeucht theorem, the first diagonal
round at which two graphs differ is therefore one less than their exact
three-variable counting quantifier depth.

## Pair-color doubling lemma on unions of cycles

Fix \(r\ge0\) and write \(L=2^r\). If every cycle component of a 2-regular
graph has length \(>2L\), then after \(r\) pair-refinement rounds the pair
color of \((x,y)\) depends only on
\[
\min\{d(x,y),L+1\},
\]
where vertices in different components are assigned distance \(+\infty\).
In particular, the finite distances \(0,1,\ldots,L\) have universal colors
(independent of the component lengths), while all pairs at distance \(>L\)
or in different components share one universal far color.

This is proved by induction. Initially equality, adjacency and nonadjacency
are exactly the truncated distance classes \(0,1,>1\). If the statement is
true at threshold \(L\), the multiset of intermediate pair colors through a
vertex \(z\) detects whether two radius-\(L\) neighborhoods can meet and,
when they do, their least possible distance sum. Hence one refinement
separates all finite distances through \(2L\). When the relevant cycle
components are longer than \(4L\), these neighborhoods do not wrap far
enough around a component to alter the universal local multiplicities.
All distances beyond \(2L\), including disconnected pairs, remain merged.

For the exact threshold below we need this lemma only one round before the
shortest cycle can wrap, where its hypotheses hold strictly.

## Exact separation from a disjoint union of cycles

Let
\[
s=\lceil\log_2 m\rceil.
\]
Because \(m\ge3\), we have \(s\ge2\), and
\[
2^{s-1}<m\le2^s.
\]

At round \(s-2\), set \(L=2^{s-2}\). Every component of \(H\) has length
at least \(m>2L\), so the doubling lemma applies. For any vertex, exactly
two vertices occur at each distance \(1,\ldots,L\), and all remaining
\(n-1-2L\) vertices have the common far color. The same row profile occurs
in \(C_n\). Consequently the diagonal colors after round \(s-1\) are equal:
\[
\operatorname{diag}C^{2,s-1}(C_n)
=
\operatorname{diag}C^{2,s-1}(H).
\]
Thus Duplicator survives \(s\) rounds in the three-pebble counting game.

Now perform one more pair refinement, from round \(s-2\) to round \(s-1\).
The old colors distinguish exactly distances through \(L\), so a pair gets
a non-far new color whenever its finite distance is at most \(2L=2^{s-1}\);
a pair farther away, or in another component, remains in the new far class.

Take \(v\) in a shortest \(m\)-cycle of \(H\). Its component diameter is
\(\lfloor m/2\rfloor\le2^{s-1}\), so every vertex of that component is
non-far from \(v\) at round \(s-1\). Therefore the far-color multiplicity in
the row of \(v\) is exactly
\[
n-m.
\]

In \(C_n\), since \(H\) has at least two components,
\(n\ge2m>2^s\), hence \(2^{s-1}<n/2\). Exactly \(2^s\) other vertices lie
within distance \(2^{s-1}\) of \(v\), so its far-color multiplicity is
\[
n-1-2^s.
\]
These two numbers differ by
\[
(n-m)-(n-1-2^s)=1+2^s-m>0.
\]
Hence the diagonal colors differ after round \(s\):
\[
\operatorname{diag}C^{2,s}(C_n)
\ne
\operatorname{diag}C^{2,s}(H).
\]
By the WL/counting-game bridge,
\[
D^3_{\#}(C_n,H)=s+1=1+\lceil\log_2 m\rceil.
\]

## Maximizing over all rivals

A same-order rival that is not 2-regular is already separated after the
first diagonal refinement, because the diagonal color records the vertex
degree. Thus the only potentially hardest same-order rivals are 2-regular
graphs, namely disjoint unions of cycles.

For a nontrivial cycle decomposition of \(n\), the shortest component has
\[
m\le\lfloor n/2\rfloor.
\]
The exact pairwise formula is increasing in \(m\), and the balanced
decomposition
\[
C_{\lfloor n/2\rfloor}\dot\cup C_{\lceil n/2\rceil}
\]
attains \(m=\lfloor n/2\rfloor\). This gives, for \(n\ge6\),
\[
D^3_{\#}(C_n)
=
1+\left\lceil\log_2\left\lfloor n/2\right\rfloor\right\rceil.
\]

For \(n=3,4,5\), no disconnected 2-regular simple graph exists on \(n\)
vertices. The conjunction “there are exactly \(n\) vertices” and “every
vertex has exactly two neighbors” defines \(C_n\) with depth \(2\).
Depth \(1\) cannot define a nontrivial adjacency pattern among same-order
simple graphs, so the value is exactly \(2\).

## Relation to prior work

The Pikhurko--Verbitsky survey (arXiv:1003.4865) supplies the exact
2-WL/three-variable-counting correspondence used above and surveys logical
depth and width, but the inspected text contains no exact cycle formula of
this form. Kiefer--Schweitzer (arXiv:1605.03480; LMCS 15(2:19), 2019) gives
general upper bounds on the quantifier depth needed when 2-WL distinguishes
two graphs, and Lichter--Ponomarenko--Schweitzer (arXiv:1905.03008) improves
general 2-WL iteration bounds. Neither inspected source states this
cycle-specific exact identification law.

This finding is distinct from the current ledger's earlier cycle result,
which computes the strict stabilization depth of 2-WL on the single graph
\(C_n\) and its counting width. The present theorem is a global
identification statement: it determines the hardest nonisomorphic rival and
the exact three-variable counting quantifier depth needed to define \(C_n\).

## Computational regression check

The accompanying `artifacts/verify.py` implements standard ordered-pair
2-WL jointly on \(C_n\) and every disjoint-cycle rival. It exhaustively
checks all cycle partitions for \(6\le n\le20\) (223 nontrivial partitions)
and balanced extremal witnesses through \(n=40\). It verifies that for
shortest component \(m\), the first full pair-color difference is round
\(\lceil\log_2 m\rceil-1\), the first diagonal difference is round
\(\lceil\log_2 m\rceil\), and the resulting defining-depth formula holds.
Its expected terminal output is:

`VERIFY_OK partitions=223 exhaustive_n=6..20 balanced_n=6..40 formula_small=3..5`

The computation is a regression check; the proof above is uniform.
