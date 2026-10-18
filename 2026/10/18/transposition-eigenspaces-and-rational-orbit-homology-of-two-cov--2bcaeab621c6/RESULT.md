# Transposition eigenspaces and rational orbit homology of two-cover graph complexes

## Finding

For every integer \(m\ge4\), let \(K_m=\operatorname{Cov}_{m,2}\) be the simplicial complex on the \(\binom m2\) edges of the complete graph on \([m]\): a set of edges is a face if and only if two graph vertices suffice to meet every selected edge. The transposition \(\tau=(1\,2)\) acts on \(K_m\) by relabeling the underlying graph.

The rational degree-three homology representation of \(\langle\tau\rangle\cong C_2\) has eigenspace dimensions

\[
\dim\widetilde H_3(K_m;\mathbb Q)^+=\binom{m-2}{4},\qquad
\dim\widetilde H_3(K_m;\mathbb Q)^-=\binom{m-2}{3}.
\]

Equivalently,

\[
\operatorname{tr}\bigl(\tau_*\mid\widetilde H_3(K_m;\mathbb Q)\bigr)
=\binom{m-2}{4}-\binom{m-2}{3}.
\]

The rational reduced homology of the **topological quotient** \(|K_m|/\langle\tau\rangle\) is concentrated in degrees three and four, where

\[
\dim\widetilde H_3\bigl(|K_m|/\langle\tau\rangle;\mathbb Q\bigr)=\binom{m-2}{4},
\]
\[
\dim\widetilde H_4\bigl(|K_m|/\langle\tau\rangle;\mathbb Q\bigr)
=\binom{m-2}{4}+\binom{m-2}{3}+\binom{m-2}{2}.
\]

Here \(\binom ak=0\) for \(k>a\). A key independently proved identity is the reduced Lefschetz number

\[
\widetilde L(\tau;K_m)=\binom{m-1}{3}.
\]

## Assumptions and scope

Graphs are simple, have vertex set \([m]\), and have no loops. Faces are *sets of graph edges*, including the empty face in the augmented chain complex. A vertex cover is a set of graph vertices meeting every selected edge. All group actions on chains use the orientation signs induced by the permutation of edge-vertices. The eigenspaces \(\pm\) are the eigenspaces of the involution over \(\mathbb Q\), not mod-two eigenspaces. The topological quotient is the quotient of the geometric realization, not an unproved simplicial quotient on orbit vertices.

Anamitro Biswas identifies this complex with the finite-set Čech complex on the two-element subsets of \([m]\), in the symmetric-difference metric at scale \(4\le r<8\) under that paper's diameter-parameter convention [2]. The underlying homology ranks are older: Jonsson's Theorem 7.1 [1] gives, integrally,

\[
\widetilde H_j(K_m;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{\binom{m-1}{4}},&j=3,\\
\mathbb Z^{\binom m4},&j=4,\\
0,&\text{otherwise}.
\end{cases}
\]

A published result [3] identifies \(\widetilde H_4(K_m;\mathbb Q)\) with the permutation module on the four-element subsets of \([m]\). Neither these rank formulas nor the known degree-four representation is claimed as new.

## Proof

**1. Signed fixed-face formula.** Set \(W=[m]\setminus\{1,2\}\), \(n=|W|=m-2\), and let \(E_W\) be the complete-graph edges within \(W\). The transposition's orbits on graph-edge vertices of \(K_m\) are: each fixed edge of \(E_W\); the fixed edge \(x=\{1,2\}\); and, for each \(i\in W\), the two-edge orbit \(y_i=\{\{1,i\},\{2,i\}\}\). An invariant face is a union of these orbits. A face with \(q\) selected edge-orbits contributes \((-1)^{q+1}\) to the reduced simplicial Lefschetz number: if the face comprises \(h\) graph edges, its chain dimension has sign \((-1)^{h-1}\), and its orientation permutation has sign \((-1)^{h-q}\). The formula includes the empty face, contributing \(-1\). Consequently

\[
\widetilde L(\tau;K_m)=-\sum_{\substack{F\text{ a union of edge-orbits}\\F\in K_m}}(-1)^{q(F)}.
\tag{1}
\]

**2. Reduce to an outside graph.** Let \(Z\subseteq E_W\) denote the selected fixed graph edges. If \(Z=\varnothing\), all the \(n+1\) orbits \(x,y_i\) can be selected freely, because \(\{1,2\}\) covers the resulting edges. Their total alternating weight is \((1-1)^{n+1}=0\). If \(Z\ne\varnothing\) has no cover of size two inside \(W\), it contributes nothing. Otherwise set

\[
C(Z)=\{\{u,v\}\subseteq W:\{u,v\}\text{ covers }Z\},\quad
U(Z)=\bigcup C(Z),\quad
I(Z)=\{u\in W:u\text{ alone covers }Z\}.
\]

For a nonempty such \(Z\), the only possible selections of the extra orbits are the empty selection; \(\{x\}\) if \(I(Z)\ne\varnothing\); \(\{y_i\}\) for \(i\in U(Z)\); \(\{x,y_i\}\) for \(i\in I(Z)\); and \(\{y_i,y_j\}\) for \(\{i,j\}\in C(Z)\). There are no allowed selections containing at least three distinct \(y\)-orbits or containing \(x\) with two distinct \(y\)-orbits, since covering those edges would use exactly \(\{1,2\}\), which does not meet \(Z\). Thus the alternating sum over the added orbits is

\[
s(Z)=1-\mathbf1_{I(Z)\ne\varnothing}-|U(Z)|+|I(Z)|+|C(Z)|.
\tag{2}
\]

**3. Classify nonzero weights without bounding the graph size.** The exact classification for every simple nonempty graph \(Z\subseteq E_W\) of covering number at most two is

\[
s(Z)=\begin{cases}
n-1,&Z\text{ is exactly one edge},\\
1,&Z\text{ is exactly two distinct edges},\\
1,&Z\text{ is exactly one triangle},\\
-1,&Z\text{ is exactly one four-cycle},\\
0,&\text{otherwise}.
\end{cases}\tag{3}
\]

To verify it, first suppose \(I(Z)\ne\varnothing\). Then \(Z\) is a star with \(d\ge1\) edges. For \(d=1\), all pairs meeting this edge belong to \(C(Z)\), yielding \(s=n-1\). For \(d=2\), \(C(Z)\) consists of the \(n-1\) pairs through the center and the extra pair of leaves, yielding \(s=1\). For \(d\ge3\), only the \(n-1\) pairs through the center qualify, yielding \(s=0\).

If \(I(Z)=\varnothing\), choose a cover \(\{u,v\}\in C(Z)\), and let \(X\) and \(Y\) be its respective nonempty exclusive neighbor sets: \(X=\{w\ne u,v:\{u,w\}\in Z\}\), \(Y=\{w\ne u,v:\{v,w\}\in Z\}\). Let \(\varepsilon\in\{0,1\}\) indicate whether \(\{u,v\}\in Z\). Every cover in \(C(Z)\), other than \(\{u,v\}\), is exactly one of these: \(\{u,y\}\) when \(Y=\{y\}\); \(\{v,x\}\) when \(X=\{x\}\); or \(X\cup Y\) when \(\varepsilon=0\) and \(|X\cup Y|=2\). The last option cannot occur with \(|X\cup Y|=1\), since that would make \(Z\) a star. These cases are exhaustive because an alternative cover sharing \(u\) must hit every edge from \(v\) to \(Y\), and similarly for \(v\); one sharing neither hub must contain all of \(X\cup Y\) and cannot hit the edge \(\{u,v\}\).

Think of \(C(Z)\) as the edges of an auxiliary graph with vertex set \(U(Z)\). Equation (2) becomes \(s(Z)=1-|U(Z)|+|C(Z)|\). The just-listed possible cover edges give a tree (and hence weight zero) except in three precise configurations. If \(\varepsilon=1\) and \(X=Y\) is a singleton, \(Z\) is a triangle and the cover graph is a triangle (weight \(1\)). If \(\varepsilon=0\) and \(X,Y\) are distinct singletons, \(Z\) is a two-edge matching and the cover graph is a four-cycle (weight \(1\)). If \(\varepsilon=0\) and \(X=Y\) has two elements, \(Z\) is a four-cycle and the cover graph has two disconnected edges (weight \(-1\)). This proves (3), including all graph sizes and all possible isolated vertices.

**4. Evaluate the Lefschetz number.** Write \(e=\binom n2\). There are \(\binom n2\) single-edge outside graphs, \(\binom e2\) two-edge outside graphs, \(\binom n3\) triangles, and \(3\binom n4\) labeled four-cycles. Substituting (3) into (1) gives

\[
\widetilde L(\tau;K_m)
=(n-1)\binom n2-\binom{\binom n2}{2}+\binom n3+3\binom n4
=\binom{n+1}{3}=\binom{m-1}{3}.
\tag{4}
\]

The final equality is an integer binomial identity, valid already for \(n\ge2\).

**5. Homology characters and the quotient.** By [1], rational reduced homology is confined to degrees three and four. By [3], degree-four homology is the four-subset permutation module; a four-subset is fixed by \(\tau\) precisely if it contains both labels \(1,2\) or neither. Therefore

\[
\operatorname{tr}(\tau_*\mid\widetilde H_4(K_m;\mathbb Q))
=\binom n2+\binom n4.
\]

The Lefschetz identity \(\widetilde L=\operatorname{tr}(H_4)-\operatorname{tr}(H_3)\) and (4) yield

\[
\operatorname{tr}(\tau_*\mid\widetilde H_3)=
\binom n2+\binom n4-\binom{n+1}3=\binom n4-\binom n3.
\]

Together with the known degree-three rank \(\binom{m-1}4=\binom n4+\binom n3\), the two eigenspace dimensions in the finding follow by taking half the sum and difference of rank and trace. Likewise, the degree-four positive eigenspace rank is \(\binom n4+\binom n3+\binom n2\). After barycentric subdivision, the action on simplicial cells is without inversions; rational transfer (finite-group averaging) identifies rational homology of the geometric quotient with the invariant homology of \(K_m\). Thus the displayed quotient formulas hold for every \(m\ge4\).

## Verification

Run `python3 verify.py` using Python's standard library. It separately enumerates **all** outside edge graphs with two-covers for \(2\le n\le6\), evaluates (2), and verifies every instance of classification (3). It also separately enumerates **all** transposition-invariant simplices for \(4\le m\le7\) and computes the signed augmented Lefschetz sum directly from edge orbits. It checks the resulting characters and binomial identities for \(4\le m\le100\). The output is included in `verify_output.txt` and ends in `VERIFY_OK`. These tests corroborate the proof but do not replace the unbounded classification argument or the cited homology theorems.

## Relationship to prior work

Jonsson's Theorem 7.1 [1] already gives the complete **nonequivariant integral homology ranks and concentration** for \(K_m\). Biswas [2] independently discusses exactly the same family as two-subset Čech complexes and proposes a stronger **nonequivariant homotopy** wedge conjecture, which is not used here as a theorem. The published four-subset sphere result [3] already gives the entire **degree-four rational** symmetric-group character. The present result concerns the previously unreported **degree-three transposition character** and the rational homology of the corresponding involution quotient; neither is implied by the prior ranks and degree-four character without the new fixed-face Lefschetz calculation (1)--(4).

## Limitations

The result determines the action of the single conjugacy class of transpositions in degree three, not the full \(S_m\)-representation and not an equivariant homotopy type. The quotient conclusion concerns rational homology, not integral torsion or its fundamental group. No conjectural infinite-family wedge homotopy type is used. The original older paper's full PDF was not accessible in this inspection, but its exact Theorem 7.1 statement and homology formulas were available in the indexed author's text; complete-text comparison for unindexed earlier equivariant results remains a residual literature risk.

## References

[1] Jakob Jonsson, *Simplicial Complexes of Graphs and Hypergraphs with a Bounded Covering Number*, SIAM Journal on Discrete Mathematics 19 (2005), 633–650, Theorem 7.1, DOI: 10.1137/S0895480104443680.

[2] Anamitro Biswas, *Čech complexes for finite sets*, arXiv:2609.32786v1, initially submitted 2026-09-26, especially Sections 1 and 5, https://arxiv.org/html/2609.32786v1.

[3] *Four-subset sphere cycles give the rational top-homology permutation character of covering complexes*, publicly indexed mathematical result, identifier d06d65e27c16, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-four-subset-sphere-cycles-give-the-rational-top-homology-permuta--d06d65e27c16.
