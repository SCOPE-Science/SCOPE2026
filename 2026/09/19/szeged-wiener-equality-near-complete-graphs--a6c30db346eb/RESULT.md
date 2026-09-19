# Equality in the Szeged–Wiener bound for graphs with an \(n-2\) clique

## Statement

For a connected graph \(G\), write
\[
W(G)=\sum_{\{u,v\}\subseteq V(G)}d(u,v),\qquad
Sz(G)=\sum_{uv\in E(G)}n_{uv}(u)n_{uv}(v),
\]
where \(n_{uv}(u)\) is the number of vertices strictly closer to \(u\) than to \(v\), and put \(\eta(G)=Sz(G)-W(G)\).

Let \(G\) be a 2-connected graph of order \(n\ge 10\) containing a clique \(Q\cong K_{n-2}\). Write \(V(G)\setminus Q=\{x,y\}\), and partition \(Q\) into
\[
A=N_Q(x)\setminus N_Q(y),\quad
B=N_Q(y)\setminus N_Q(x),\quad
C=N_Q(x)\cap N_Q(y),\quad
D=Q\setminus(N_Q(x)\cup N_Q(y)),
\]
with sizes \(a,b,c,d\), so \(a+b+c+d=n-2\).

Then the Szeged–Wiener gap is given exactly by the following formulas.

If \(xy\in E(G)\),
\[
\boxed{\eta(G)=8ab+2ac+3ad+2bc+3bd+4cd-4d.}
\tag{1}
\]
If \(xy\notin E(G)\) and \(c>0\),
\[
\boxed{\eta(G)=5ab+2ac+2ad-2a+2bc+2bd-2b+4cd+2c-4d-2.}
\tag{2}
\]
If \(xy\notin E(G)\) and \(c=0\),
\[
\boxed{\eta(G)=5ab+2ad-a+2bd-b-4d-3.}
\tag{3}
\]

Consequently, among all 2-connected graphs of order \(n\ge10\) containing an \((n-2)\)-clique,
\[
\boxed{\eta(G)=2n}
\]
holds if and only if, up to interchanging \(x\) and \(y\), one of the following occurs:

1. \(xy\in E(G)\), \(N_Q(x)=\{u\}\), and \(N_Q(y)=\{v\}\) for distinct \(u,v\in Q\). This is the equality family displayed by Zhang and Li and exists for every \(n\ge10\).
2. \(n=10\), \(xy\in E(G)\), \(N_Q(x)=\{u\}\), and \(N_Q(y)=\{u,v\}\) for distinct \(u,v\in Q\).

Thus the Zhang–Li family is the only infinite equality family inside the natural near-complete class \(\omega(G)\ge n-2\), with one additional isomorphism type at order \(10\).

## Context

Bonamy, Knor, Lužar, Pinlou, and Škrekovski proved that every 2-connected noncomplete graph satisfies \(\eta(G)\ge2n-6\), characterized equality there, and conjectured the stronger bound \(\eta(G)\ge2n\) outside three exceptional near-complete graphs for \(n\ge10\). Zhang and Li proved that conjecture in 2026. They then posed the problem of characterizing all equality graphs with \(\eta(G)=2n\). Their Lemma 8 gives the first family above and explicitly notes that its sufficient condition is not necessary.

The theorem here solves that equality problem completely under the structural hypothesis that the graph contains a clique on all but two vertices. It also gives the exact gap for every 2-connected graph in that class, not just the equality cases.

## Proof of the exact formulas

For the first two cases the graph has diameter two. For any edge \(uv\),
\[
n_{uv}(u)=1+|N(u)\setminus N[v]|.
\]
For an edge entirely inside \(Q\), the two outside vertices distinguish its endpoints only through their membership types \(A,B,C,D\). The Szeged contribution of a \(Q\)-edge is therefore

\[
\begin{array}{c|cccc}
 &A&B&C&D\\ \hline
A&1&4&2&2\\
B&4&1&2&2\\
C&2&2&1&3\\
D&2&2&3&1
\end{array}
\]

where diagonal entries apply to two vertices in the same class. Hence the total contribution from edges inside \(Q\) is
\[
S_Q=\sum_{X\in\{A,B,C,D\}}\binom{|X|}{2}
+4ab+2ac+2ad+2bc+2bd+3cd.
\tag{4}
\]

Suppose first that \(xy\in E(G)\). The remaining edge contributions are
\[
(a+1)(b+1),\quad 2a(1+b+d),\quad c(1+b+d),\quad
2b(1+a+d),\quad c(1+a+d),
\]
coming respectively from \(xy\), the \(xA\)-edges, the \(xC\)-edges, the \(yB\)-edges, and the \(yC\)-edges. Also
\[
W(G)=\binom n2+a+b+2d.
\]
Combining this with (4) and simplifying gives (1).

Now suppose \(xy\notin E(G)\) and \(c>0\). The remaining edge contributions are
\[
a(1+b+d),\quad c(b+d+2),\quad b(1+a+d),\quad c(a+d+2),
\]
and
\[
W(G)=\binom n2+1+a+b+2d.
\]
Together with (4), this yields (2).

Finally let \(xy\notin E(G)\) and \(c=0\). Two-connectivity forces \(a,b\ge2\), and now \(d(x,y)=3\). The \(Q\)-edge table is the restriction of (4) to \(A,B,D\). For an \(xA\)-edge the vertex \(y\) lies on the \(A\)-endpoint side, so each such edge contributes \(b+d+2\); symmetrically each \(yB\)-edge contributes \(a+d+2\). Moreover
\[
W(G)=\binom n2+a+b+2d+2.
\]
Simplification gives (3).

## Proof of the equality classification

The two-connectivity conditions in this parametrization are elementary. If \(xy\in E(G)\), then
\[
a+c\ge1,\qquad b+c\ge1,\qquad a+b+c\ge2.
\tag{5}
\]
If \(xy\notin E(G)\), then
\[
a+c\ge2,\qquad b+c\ge2.
\tag{6}
\]
These conditions are also sufficient because deleting any single vertex leaves the surviving part of \(Q\) connected and leaves both outside vertices attached to it, possibly through the edge \(xy\).

### Adjacent outside vertices

Put \(s=a+b\). From (1), the equality \(\eta(G)=2n\) is equivalent to
\[
d(3s+4c-6)=2s+2c+4-8ab-2cs.
\tag{7}
\]

If \(c=0\), (5) gives \(a,b\ge1\). When \(s=2\), necessarily \(a=b=1\), and both sides of (7) vanish; the order condition gives \(d\ge6\). When \(s\ge3\), using \(ab\ge s-1\) makes the right-hand side at most \(12-6s<0\), impossible.

Assume \(c\ge1\). If \(a,b\ge1\), then \(s\ge2\) and \(ab\ge s-1\), so the right-hand side of (7) is at most
\[
12-6s+2c(1-s)<0.
\]
Hence one of \(a,b\) must vanish, or both do. If exactly one vanishes, say \(b=0\), then for \(s=1\), (7) becomes
\[
d(4c-3)=6,
\]
whose only solution is \(c=1,d=6\). For \(s=2\), the only zero-numerator possibility has order below \(10\); for \(s\ge3\), the right-hand side is at most \(6\) while the coefficient of \(d\) is at least \(7\), and the case \(d=0\) again has order below \(10\). If \(a=b=0\), then \(c\ge2\) and (7) becomes
\[
d(4c-6)=2c+4;
\]
the only integral solutions have order \(8\). Thus the adjacent case gives exactly the two families in the statement.

### Nonadjacent outside vertices

If \(c=0\), (6) gives \(a,b\ge2\), hence \(s\ge4\). Equation (3) and \(\eta(G)=2n\) give
\[
d(2s-6)=3s+7-5ab.
\tag{8}
\]
Since \(ab\ge2(s-2)\), the right side is at most \(27-7s<0\), impossible.

If \(c\ge1\), equations (2) and \(\eta(G)=2n\) give
\[
d(2s+4c-6)=6+4s-5ab-2cs.
\tag{9}
\]
When \(c=1\), (6) forces \(a,b\ge1\); direct use of \(ab\ge s-1\) leaves only \(s=2,3\), and (9) gives respectively nonintegral values \(d=5/2,1/2\). Let \(c\ge2\). The cases \(s=0,1\) yield only orders below \(10\). For \(s\ge2\) and \(ab>0\), the right side of (9) is at most \(1\), whereas the coefficient of \(d\) is at least \(6\); if \(d=0\), the equation becomes
\[
5ab+2s(c-2)=6,
\]
which has no solution with \(ab>0\). If \(ab=0\), then either \(d>0\) forces the sole small solution \((s,c,d)=(2,2,1)\) of order \(7\), or \(d=0\) forces \(s(c-2)=3\), again giving order below \(10\). Thus there are no nonadjacent equality graphs of order at least \(10\).

This completes the classification.

## Verification

The accompanying verifier constructs the graphs directly from \((a,b,c,d)\), computes all-pairs shortest-path distances, and then evaluates \(W\) and \(Sz\) from their definitions. It checks the three closed formulas on 1,160 connected parameter profiles in a finite parameter box. It also checks every 2-connected profile through order \(18\), totaling 8,175 profiles, and finds exactly the equality profiles stated above.

The finite computation is supporting evidence; the theorem is established by the symbolic argument above.

## Originality and limitations

The 2026 Zhang–Li paper was inspected through its equality section. It explicitly poses the full equality classification as Problem 7, exhibits the first family above, and states that its sufficient condition is not necessary, but does not classify graphs with an \((n-2)\)-clique or give formulas (1)–(3). The 2017 Bonamy–Knor–Lužar–Pinlou–Škrekovski paper was inspected in an author-hosted full text; it proves the earlier \(2n-6\) theorem, characterizes those equality cases, and formulates the stronger \(2n\) conjecture, but does not give the present classification.

Searches using Szeged–Wiener gap, equality \(2n\), clique of order \(n-2\), near-complete graphs, clique deletion, and equivalent Szeged-index terminology found no earlier statement of the formulas or classification. Originality is therefore asserted only to the best of our knowledge. No specific inaccessible paper was identified as especially likely to contain this classification; residual risk remains from older chemical-graph literature using different family terminology and from very recent unindexed work.

The result is a partial solution of Zhang and Li's Problem 7: it covers exactly the graphs with clique number at least \(n-2\), not arbitrary 2-connected equality graphs.

## References

1. Lily Zhang and Evan Li, *Improved Bounds on the Szeged–Wiener Gap and the BKLPS Conjecture*, arXiv:2609.20025, 2026. https://arxiv.org/abs/2609.20025
2. Marthe Bonamy, Martin Knor, Borut Lužar, Alexandre Pinlou, and Riste Škrekovski, *On the difference between the Szeged and the Wiener index*, Applied Mathematics and Computation 312 (2017), 202–213. https://doi.org/10.1016/j.amc.2017.05.047
