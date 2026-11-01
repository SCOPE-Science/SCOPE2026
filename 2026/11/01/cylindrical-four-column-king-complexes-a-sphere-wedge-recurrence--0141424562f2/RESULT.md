# Cylindrical four-column king complexes: a sphere-wedge recurrence and sharp Smith equality

## Finding
For every integer \(n\ge1\), let \(P_n\) be the path on \(n\) vertices and let \(C_4\) be the four-cycle. Write \(X_n=\operatorname{Ind}(P_n\boxtimes C_4)\), where \(\boxtimes\) is the strong graph product and \(\operatorname{Ind}\) is the independence complex. Then
\[
X_n\simeq\Sigma X_{n-2}\vee\Sigma^2X_{n-3}\vee\Sigma^2X_{n-3}\qquad(n\ge6).
\]
The exact initial homotopy types are
\[
\begin{aligned}
X_1&\simeq S^0,\\
X_2&\simeq S^0\vee2S^1,\\
X_3&\simeq3S^1,\\
X_4&\simeq S^1\vee4S^2,\\
X_5&\simeq5S^2\vee4S^3.
\end{aligned}
\]
Here \(aS^j\) abbreviates a wedge of \(a\) copies of the \(j\)-sphere. In particular, every \(X_n\) is a wedge of spheres and has torsion-free reduced integral homology.

Let \(p_n(z)=\sum_{j\ge0}\operatorname{rank}\widetilde H_j(X_n;\mathbb Z)z^{j+1}\), with the formal augmented convention \(p_0(z)=1\). Then
\[
p_1=z,\qquad p_2=z+2z^2,\qquad
p_n=zp_{n-2}+2z^2p_{n-3}\quad(n\ge3),
\]
and the bivariate generating function is
\[
\boxed{\displaystyle\sum_{n\ge0}p_n(z)t^n=\frac{1+zt+2z^2t^2}{1-zt^2-2z^2t^3}.}
\]

The antipodal rotation \(\tau:(i,j)\mapsto(i,j+2\pmod4)\) is a simplicial involution. Its geometric fixed-point space is canonically PL homeomorphic to \(\operatorname{Ind}(P_n\boxtimes P_2)\). Moreover, for all \(n\ge1\),
\[
\boxed{\displaystyle
\sum_j\dim_{\mathbb F_2}\widetilde H_j(|X_n|^\tau;\mathbb F_2)
=\sum_j\dim_{\mathbb F_2}\widetilde H_j(X_n;\mathbb F_2).}
\]
Thus the total mod-two Smith inequality for this involution is **an equality for every length**, although the two spaces generally have different degree distributions of homology.

## Assumptions and scope
The vertices of \(P_n\boxtimes C_4\) are pairs \((i,j)\) with \(0\le i<n\) and \(j\in\mathbb Z/4\mathbb Z\). Distinct pairs \((i,j)\) and \((i',j')\) are adjacent precisely when \(|i-i'|\le1\) and \(j'-j\pmod4\in\{0,1,3\}\). No loop edges are present. All homotopy equivalences are ordinary nonequivariant homotopy equivalences; the fixed-point statement concerns the specified involution on the actual geometric realization. Suspensions are reduced in the displayed positive-dimensional recurrence. The formal \(n=0\) polynomial does not assert a geometric identification for an empty graph realization.

## Proof
**1. Homotopy-preserving moves.** For a finite graph \(H\) and distinct vertices \(u,v\), if \(N_H(u)\subseteq N_H(v)\) (open neighborhoods), then \(\operatorname{Ind}(H)\simeq\operatorname{Ind}(H-v)\). If \(N_H[u]\subseteq N_H[v]\) (closed neighborhoods), then
\[
\operatorname{Ind}(H)\simeq\operatorname{Ind}(H-v)\vee\Sigma\operatorname{Ind}(H-N_H[v]).
\]
In the second case, the link inclusion into \(\operatorname{Ind}(H-v)\) is nullhomotopic because the vertex \(u\) cones off that link. An isolated graph vertex makes the independence complex contractible. These standard graph-folding facts are also Lemma 1 of the cited 2025 work.

**2. A finite-state neighborhood proof valid for every length.** Encode an induced subgraph by one hexadecimal row mask for each row; the mask has bit \(j\) set exactly when column \(j\) is present. Write \(F=15\), and \(F^m\) for \(m\) consecutive complete rows. For a fixed prefix \(w\), let \(\mathcal I(wF^m)\) be the independence complex of the masked graph. In the following table, vertex \(4i+j\) means \((i,j)\); the indicated open/closed move uses that vertex as \(u\) followed by \(v\). A closed move has two children, the first from deleting \(v\), the second from deleting its closed neighborhood. The displayed row words are **induced-graph identities**, not merely equalities of Euler characteristics. All rows hold for \(m\ge2\), except the first row, which requires \(m\ge3\):

```text
prefix         move     u   v     children after normalization
()             closed   0   4     (15,14)F^(m-2); (4,4,4)F^(m-3)
(15,14)        open     0   2     (11,14)F^m
(11,14)        open     0   6     (11,10)F^m
(11,10)        closed   1   0     (10,10)F^m; F^m
(4,4,4)        open     2  10     (4,4,0)F^m
(4,4,0)        closed   2   6     (4,0,0)F^m; F^m
(4,0,0)        cone     -   -     isolated first-row vertex
(10,10)       open     1   8     (10,10,14)F^(m-1)
(10,10,14)    open     1   9     (10,10,12)F^m
(10,10,12)    open     1  10     (10,10,8)F^m
(10,10,8)     open     3  11     (10,10,0)F^m
(10,10,0)     closed   1   5     (10,8,0)F^m; (8,8,0)F^m
(10,8,0)      cone     -   -     isolated first-row vertex
(8,8,0)      closed   3   7     (8,0,0)F^m; F^m
(8,0,0)      cone     -   -     isolated first-row vertex
```

Each inclusion is checked by comparing neighborhoods restricted to at most the first four rows. Every relevant \(u,v\) lies in the first three rows; the graph has edges only within a row or between consecutive rows. Hence rows beyond the fourth cannot change any neighborhood inclusion. In every deletion, all row masks beyond those displayed remain complete and in order. These local facts establish each table row for **all** allowable \(m\), not only for the finite sample values in the checker.

**3. Collapse of the finite-state system.** Define
\[
\begin{aligned}
R_m&=\mathcal I(F^m),& A_m&=\mathcal I((15,14)F^m),\\
B_m&=\mathcal I((4,4,4)F^m),& C_m&=\mathcal I((10,10)F^m).
\end{aligned}
\]
Following the table yields, whenever the displayed terms are in their allowed positive ranges,
\[
\begin{aligned}
R_n&\simeq A_{n-2}\vee\Sigma B_{n-3},\\
A_m&\simeq C_m\vee\Sigma R_m,\\
B_m&\simeq\Sigma R_m,\\
C_m&\simeq\Sigma^2R_{m-1}.
\end{aligned}
\]
Substitution gives the main recurrence for every \(n\ge6\). The five initial sphere wedges are obtained using the same two graph-folding moves, terminating only at isolated-vertex cones and the formal augmented empty graph; the included standalone checker constructs and verifies complete reduction trees for these five graphs. The recurrence and bases prove the wedge classification by induction.

**4. Poincaré series.** A suspension shifts the degree of reduced homology by one, hence \(p_n=zp_{n-2}+2z^2p_{n-3}\) for \(n\ge6\). Direct substitution of the five base cases shows that the same polynomial recurrence with formal \(p_0=1\) holds for \(n=3,4,5\). Summing the recurrence gives the displayed rational generating function.

**5. The fixed space and sharp Smith equality.** Every orbit of the half-turn on graph vertices is an opposite column pair in a single row, either \(\{(i,0),(i,2)\}\) or \(\{(i,1),(i,3)\}\). Each pair is independent. A union of such orbits is an independent face exactly when the selected orbit-vertices form an independent set in \(P_n\boxtimes P_2\): two different orbit types conflict within a row, and all orbit types conflict in neighboring rows. A point of a fixed geometric simplex has equal barycentric weights on the two vertices of each orbit; this identifies the fixed realization PL-homeomorphically with the quotient-orbit independence complex.

Let \(b_n\) be the total reduced Betti number of \(X_n\), and \(c_n\) that of the fixed space, both over \(\mathbb F_2\). The wedge recurrence gives \(b_n=b_{n-2}+2b_{n-3}\), with initial \((b_1,b_2,b_3)=(1,3,3)\). Proposition 23 and Proposition 26 of the cited 2025 paper give the same **numerical** recurrence and initial totals for \(\operatorname{Ind}(P_n\boxtimes P_2)\); the suspension degrees in that earlier recurrence need not match ours. Hence \(b_n=c_n\) for all \(n\). Since both complexes are nonempty, their *unreduced* total Betti numbers differ from these reduced totals by exactly one, so equality also holds in the usual Smith inequality.

## Verification
Run `python3 check_cylindrical_king.py` using Python 3.8 or later. It verifies every neighborhood inclusion and every normalized child in the fifteen-row table for \(104\) template instances; by the locality argument in the proof these checks exhaust all types of locally varying adjacency. It independently computes the exact five base-case wedge reductions and verifies exact graph-folding decompositions through \(n=11\). Separate simplicial boundary matrices over \(\mathbb F_2\) reproduce the Poincaré coefficients of both the cylinder and its fixed locus through \(n=9\), and the total Smith-rank equality is checked through \(n=13\). The arbitrary-length proof is the symbolic local-neighborhood argument plus induction, not an extrapolation from these finite calculations.

## Relationship to prior work
A. Carnero Bravo, *On independence complexes of graph products*, first appeared on arXiv on 9 May 2025, arXiv:2505.06457v1. Its Lemma 1 supplies the standard folding rules; Section 5, particularly Propositions 23, 25, and 26, classifies rectangular \(P_n\boxtimes P_m\) for \(m=2,3,4\) and supplies the fixed-space Betti recurrence. Those earlier results do **not** assert the cylindrical \(P_n\boxtimes C_4\) wedge recurrence or the sharp half-turn Smith equality; the Cartesian/categorical cycle products considered elsewhere there are different graphs. The contribution here is the periodic-width-four strong-product classification and the equality obtained by comparing its genuinely different homotopy polynomial with that of the fixed rectangular king complex. These comparisons identify no equivalent statement in the inspected literature or indexed records; they do not prove absolute novelty beyond the searched material.

## Limitations
The width is exactly four with periodic column identification and open longitudinal path ends. General \(C_m\) widths, both-directions periodic king graphs, and other finite group actions are not covered. The homotopy equivalences are nonequivariant and do not determine an integral equivariant chain-level decomposition. Independent audit has not been performed; implicit coverage in unindexed or unread prior work remains a residual originality risk.

## References
1. Andrés Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457v1, posted 9 May 2025, https://arxiv.org/html/2505.06457v1 (especially Lemma 1 and Propositions 23, 25, 26).
2. The classical mod-two Smith inequality for finite group actions on finite CW complexes; only the inequality's conventional terminology is used here, while the equality is proved directly by the two Betti recurrences.
