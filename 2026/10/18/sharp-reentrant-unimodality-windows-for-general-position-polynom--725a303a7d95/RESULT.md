# Sharp reentrant unimodality windows for general-position polynomials of diagonal-deleted multipartite graphs

## Finding

Let \(T^*(r,a)\) have vertex set \([a]\times[r]\), with \((i,j)\) adjacent to \((i',j')\) precisely when \(i\ne i'\) and \(j\ne j'\). This is the complete \(a\)-partite graph with \(r\) vertices per part after deleting all equal-label cross-part edges. A general-position set has no three vertices on any shortest path. Let \(\Psi_{r,a}(z)=\sum_{k\ge0}c_k z^k\) count all such sets by size.

**Theorem.** For all positive integers \(r\),
\[
\Psi_{r,3}\text{ is unimodal}\iff (1\le r\le10)\ \text{or}\ (r\ge18),
\]
\[
\Psi_{r,4}\text{ is unimodal}\iff (1\le r\le11)\ \text{or}\ (r\ge40).
\]
Thus nonunimodality occurs precisely at \(11\le r\le17\) for \(a=3\) and \(12\le r\le39\) for \(a=4\). These are two sharp finite, reentrant parameter windows.

More generally, for \(a,r\ge3\), the complete correct coefficient formula is
\[
\begin{aligned}
&c_0=1,\quad c_1=ar,\quad c_2=\binom{ar}{2},\\
&c_k=a\binom r k+r\binom a k+k!\binom a k\binom r k
 +\mathbf1_{k=3}\,4\binom a2\binom r2
 +\mathbf1_{k=4}\binom a2\binom r2\qquad(k\ge3).
\end{aligned}
\]
Here \(\binom nk=0\) outside \(0\le k\le n\). For \(r=1\), \(\Psi_{1,a}(z)=(1+z)^a\). For \(r=2\) and \(a\in\{3,4\}\), \(\Psi_{2,a}(z)=1+2az+\binom{2a}{2}z^2+2\sum_{k=3}^{a}\binom ak z^k\).

## Assumptions and scope

Graphs are finite, simple, undirected, with both coordinates and all vertices distinguished. Unimodal means that the full coefficient sequence, from degree zero through its degree, first weakly increases and then weakly decreases, permitting ties. All theorems for \(a=3,4\) include \(r=1,2\). The general coefficient identity assumes \(a,r\ge3\). No classification for \(a\ge5\) is claimed.

## Proof

**1. A direct structural classification.** For \(a,r\ge3\), every two distinct nonadjacent vertices of \(T^*(r,a)\) have a common neighbor: choose a first coordinate different from both first coordinates and a second coordinate different from both second coordinates. Hence the graph has diameter two. In any diameter-two graph, a vertex subset is in general position exactly when its induced graph is a disjoint union of cliques: a forbidden geodesic with three selected vertices is precisely an induced path on three vertices among them.

Consider a general-position set \(S\) of size at least three. If \(S\) contains two cells \((i,p),(i,q)\) in the same row, with \(p\ne q\), every other selected cell outside row \(i\) must be in column \(p\) or \(q\); otherwise it is adjacent to both of these mutually nonadjacent cells, giving a forbidden induced three-vertex path. There is at most one selected cell outside row \(i\) in each of columns \(p,q\), because two in the same outside column would be mutually nonadjacent and share \((i,q)\) or \((i,p)\) as a neighbor. If both outside cells exist, they must have the same row, since cells in distinct rows and distinct columns would be adjacent, and one of the original two cells would complete a forbidden induced path. Thus either the entire set is in one row, or \(S\) consists of three corners of a \(2\)-by-\(2\) rectangle, or \(S\) is all four corners. The same argument with any third selected cell in the original row rules out outside vertices whenever three cells share one row.

If no row is repeated, and some column occurs twice, then any selected cell outside that column would be adjacent to both of the mutually nonadjacent cells, again violating general position. Thus \(S\) lies in one column. In the remaining case all row and column coordinates in \(S\) are pairwise distinct, so \(S\) induces a clique. Conversely each of these five forms (one row; one column; coordinate-distinct transversal; three corners; four corners) induces a disjoint union of cliques, so is in general position. For \(k\ge3\), these forms are disjoint, with counts, respectively, \(a\binom rk\), \(r\binom ak\), \(k!\binom ak\binom rk\), \(4\binom a2\binom r2\) when \(k=3\), and \(\binom a2\binom r2\) when \(k=4\). This proves the coefficient identity.

**2. Small-row endpoints.** At \(r=1\), all edges have been deleted, hence every subset is in general position, giving \((1+z)^a\). At \(r=2\), the graph is a crown graph on two classes of \(a\) vertices. For \(a=3\) this is \(C_6\), with polynomial \(1+6z+15z^2+2z^3\). For \(a=4\), shortest-path inspection gives \(1+8z+28z^2+8z^3+2z^4\). Both are unimodal. For a direct reproducible check independent of the subsequent coefficient argument, the accompanying verifier enumerates all vertex subsets using all-pairs shortest paths.

**3. Three parts.** For \(a=3\), \(r\ge3\), the only coefficients requiring comparison with the binomial tail are
\[
\begin{aligned}
 c_3&=\tfrac r2(3r^2+3r-4),\\
 c_4&=\tfrac{r(r-1)}8(r^2-5r+18),\\
 c_k&=3\binom rk\quad(k\ge5).
\end{aligned}
\]
For \(r\ge3\) one has \(1\le c_1\le c_2\le c_3\). The decisive exact differences are
\[
 c_3-c_4=-\tfrac r8(r^3-18r^2+11r-2),
\quad c_5-c_4=\tfrac{r(r-1)}{40}(r^3-14r^2+51r-114).
\]
The first difference is positive for \(3\le r\le17\) and negative for \(r\ge18\): the cubic equals \(r^2(r-18)+11r-2\), which is negative for \(2\le r\le10\) by bounding \(r-18\le-8\), negative for \(11\le r\le17\) by bounding \(r-18\le-1\), and positive for \(r\ge18\). The second difference is nonpositive for \(3\le r\le10\) and positive for \(r\ge11\): the cubic \(Q_3=r^3-14r^2+51r-114\) is negative for \(2\le r\le6\) since \(Q_3\le-8r^2+51r-114<0\), and it increases strictly on \([7,\infty)\) because \(Q_3'(r)=3r^2-28r+51>0\) there, with \(Q_3(10)=-4\) and \(Q_3(11)=84\). Finally \(3\binom rk\) is unimodal in \(k\), and weakly decreases from \(k=5\) if \(r\le10\). Hence the coefficient sequence is unimodal for \(3\le r\le10\), decreases at degree \(3\) then increases at degree \(5\) for \(11\le r\le17\), and is unimodal for \(r\ge18\).

**4. Four parts.** For \(a=4\), \(r\ge3\),
\[
\begin{aligned}
 c_3&=\tfrac{2r}{3}(7r^2-3r+2),\\
 c_4&=\tfrac r6(7r^3-42r^2+95r-54),\\
 c_k&=4\binom rk\quad(k\ge5).
\end{aligned}
\]
Again \(1\le c_1\le c_2\le c_3\) for all \(r\ge3\). Here
\[
 c_3-c_4=-\tfrac r6(7r^3-70r^2+107r-62),
\quad c_5-c_4=\tfrac r{30}(r^4-45r^3+245r^2-525r+294).
\]
The cubic in the first difference is negative at \(r=3,4,5,6,7,8\) and positive at \(r=9\). Its derivative \(21r^2-140r+107\) is positive for \(r\ge6\), proving the signs persist; the six small values are direct substitutions. Thus \(c_3>c_4\) for \(3\le r\le8\), but \(c_3<c_4\) for \(r\ge9\).

Write \(Q_4(r)=r^4-45r^3+245r^2-525r+294\). Its values at \(3,4,5,6\) are negative. For every integer \(7\le r\le38\), \(r^2-45r+245<0\) (the convex quadratic is negative at both ends of that interval), so \(Q_4(r)=r^2(r^2-45r+245)-525r+294<0\). Also \(Q_4(39)=-3450\) and \(Q_4(40)=51294\). For \(r\ge40\), \(Q_4'(r)=r^2(4r-135)+490r-525>0\), proving \(Q_4>0\) thereafter. It follows that \(c_4>c_5\) for \(3\le r\le39\), and \(c_4<c_5\) for \(r\ge40\).

For \(3\le r\le8\), coefficients peak at \(c_3\); for \(9\le r\le11\), they peak at \(c_4\), since the binomial tail declines from index \(5\). For \(12\le r\le39\), \(c_4>c_5<c_6\) since \(\binom r6>\binom r5\) when \(r\ge12\), so unimodality fails. For \(r\ge40\), the sequence increases through \(c_5\), after which its binomial tail is unimodal. This completes the claimed classification.

## Verification

The included standard-library `verify.py` constructs \(T^*(r,a)\) from its edge definition and uses Floyd–Warshall distances to identify every forbidden geodesic triple. It exhaustively enumerates \(107352\) vertex subsets over nine graph instances (\(a=3\), \(1\le r\le5\); \(a=4\), \(1\le r\le4\)), reproducing every coefficient of the structural formula independently. A separate exact-integer sweep checks the classification for \(1\le r\le1000\) in each of the two values of \(a\), or \(2000\) formula cases in all. These finite checks validate arithmetic but do not prove the infinite-range claims, which follow from the sign inequalities above.

## Relationship to prior work

Tuite, Thomas and Chandran introduced the diagonal-deleted Turán graph construction (preprint first public 12 June 2021). Iršič, Klavžar, Rus and Tuite (preprint first public 11 January 2024) introduced general-position polynomials, considered the same graph family, and explicitly asked in Problem 5.2 for its unimodality classification; they identified the sufficient bound \(r\ge19\) when \(a=3\). Their Section 4 gives an expression for all coefficients, but that expression is not the one proved here for the literal graph definition: for example, it predicts coefficient \(20\) at degree three of \(T^*(2,3)\), whereas that graph is \(C_6\) and has only two general-position triples. The present independent induced-cluster classification supplies the correct polynomial for \(a,r\ge3\) and resolves both \(a=3\) and \(a=4\) parameter slices with sharp windows. This is not a claim to settle Problem 5.2 for every \(a\).

## Limitations

The all-parameter coefficient identity is proved for \(a,r\ge3\). Only the two slices \(a=3,4\) receive a complete unimodality classification, with their \(r=1,2\) cases handled separately. No exhaustive claim of bibliographic priority is made, and independent scientific review has not been performed. Direct subset enumeration is finite and is not relied on for the all-integer theorem.

## References

1. J. Tuite, E. J. Thomas and U. Chandran S. V., *On some extremal position problems for graphs*, arXiv:2106.06827 (first public 2021-06-12), https://arxiv.org/abs/2106.06827 .
2. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first public 2024-01-11); *Results in Mathematics* 79 (2024), Article 110, https://doi.org/10.1007/s00025-024-02133-3 .
