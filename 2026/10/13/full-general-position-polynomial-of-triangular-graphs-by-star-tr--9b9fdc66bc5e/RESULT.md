# Full general-position polynomial of triangular graphs by star–triangle components

## Finding
Let \(K_n\) be the labeled complete graph on \([n]\), \(T_n=L(K_n)=J(n,2)\) its line graph, and \(\Psi_n(z)=\sum_{S\subseteq V(T_n),\ S\text{ general position}}z^{|S|}\), including the empty set. For every integer \(n\ge0\),
\[
\boxed{\sum_{n\ge0}\Psi_n(z)\frac{u^n}{n!}=\exp\!\left(u e^{uz}-\frac{u^2z}{2}+\frac{u^3z^3}{6}\right).}
\]
An explicit coefficient recurrence is
\[
\Psi_0(z)=1,\qquad
\Psi_n(z)=\sum_{s=1}^{n}\binom{n-1}{s-1}c_s(z)\Psi_{n-s}(z),
\]
where
\[
c_1(z)=1,\quad c_2(z)=z,\quad c_3(z)=3z^2+z^3,\quad c_s(z)=s z^{s-1}\ (s\ge4).
\]
For \(n\ge3\), the highest nonzero degree is \(n\) if \(3\mid n\), and \(n-1\) otherwise, agreeing with the earlier extremal theorem of Ghorbani et al. Moreover, if \(3\mid n\) and \(n>0\),
\[
[z^n]\Psi_n(z)=\frac{n!}{6^{n/3}(n/3)!}.
\]
This counts all maximum sets, not merely their common size.

## Assumptions and scope
All graphs are finite, simple and undirected. A vertex set is *in general position* if no graph geodesic contains three of its vertices. The vertices of \(T_n\) are the two-element subsets of \([n]\), adjacent if they intersect. By convention \(T_0\) and \(T_1\) are empty graphs and \(\Psi_0=\Psi_1=1\); \(T_2\) is one vertex. Both \(u\) and \(z\) are formal indeterminates; the series identity is in \(\mathbb Q[z][[u]]\). The theorem concerns the ordinary vertex general-position polynomial of the triangular graph, not the polynomial of its complement, the Kneser graph \(K(n,2)\).

## Proof
For \(n\ge4\), any two vertices of \(T_n\) are adjacent or have distance two: two disjoint edges of \(K_n\) have a bridging edge meeting both. Thus three selected vertices lie on a geodesic exactly when they induce a three-vertex path in \(T_n\). The same no-induced-path criterion holds trivially in \(T_0,T_1,T_2,T_3\), where every nonempty adjacency component is complete. Consequently a set \(S\subseteq E(K_n)\) is general position in \(T_n\) if and only if every connected component of \(T_n[S]\) is a clique.

Regard \(S\) as the edge set of \(H=([n],S)\). The nonisolated components of \(H\) correspond bijectively to the components of \(T_n[S]\). Such a component contributes a clique precisely when all its edges are pairwise incident. A simple graph whose edges pairwise intersect is a star or a triangle: choose two distinct incident edges \(ab\) and \(ac\); any edge not incident to \(a\) must be \(bc\), and if \(bc\) occurs, no edge incident to a fourth vertex can meet all three edges. Conversely, stars and triangles have pairwise intersecting edges. Hence \(H\) is a disjoint union of isolated vertices, stars, and triangles, and **every** such union supplies a general-position set. This is a genuine bijection, including empty selections, and its underlying unweighted component classification is known in the earlier general-position literature.

Count the labeled allowed components by their number \(s\) of vertices and by their number of selected edges. An isolated vertex contributes \(c_1=1\); a two-vertex edge contributes \(c_2=z\); a three-vertex component is one of three two-edge stars or one triangle, so \(c_3=3z^2+z^3\); and for \(s\ge4\) a star is uniquely specified by one of its \(s\) centers and contains \(s-1\) edges, giving \(c_s=sz^{s-1}\). The exponential formula for labeled sets of components now gives
\[
\sum_{n\ge0}\Psi_n(z)\frac{u^n}{n!}
=\exp\left(\sum_{s\ge1}c_s(z)\frac{u^s}{s!}\right).
\]
Evaluating the exponent yields
\[
\sum_{s\ge1}c_s(z)\frac{u^s}{s!}
=u+\frac{u^2z}{2}+\frac{u^3(3z^2+z^3)}{6}
+\sum_{s\ge4}\frac{s u^s z^{s-1}}{s!}
=u e^{uz}-\frac{u^2z}{2}+\frac{u^3z^3}{6}.
\]
The exponential series identity follows. Classifying a configuration according to the unique component containing label \(1\) gives the displayed recurrence: choose its \(s-1\) other vertices, its weighted structure counted by \(c_s(z)\), and any admissible graph on the remaining \(n-s\) vertices.

Finally, every triangle component contributes as many edges as vertices, while every star or isolated vertex contributes exactly one fewer edge than vertices. Therefore the number of selected edges equals \(n\) minus the number of nontriangle components. If \(3\mid n\), the degree \(n\) is attained exactly when all vertices partition into triangles; the number of these partitions is \(n!/(6^{n/3}(n/3)!)\). If \(3\nmid n\), at least one nontriangle component is required, so the degree is at most \(n-1\), and the single star spanning all \(n\) vertices attains it for \(n\ge2\) (for \(n=1\), the empty edge set has degree zero). This also verifies the boundary cases.

## Verification
The standalone Python 3 file `verify_triangular_gp.py` constructs the recurrence over exact integers, independently builds each finite line graph and all graph shortest-path distances, and performs exhaustive branch-and-prune enumeration of all general-position subsets for \(0\le n\le7\). Pruning is valid because adding vertices cannot undo a geodesic triple. It compares **every coefficient** with the recurrence; it also checks the highest degree and divisible-by-three maximum-set multiplicity for \(3\le n\le20\). Running `python3 verify_triangular_gp.py` produces `VERIFY_OK`; the accompanying `verification_output.txt` records one execution. The numerical checks are finite confirmations; the preceding argument proves the identities for all \(n\).

## Relationship to prior work
Ghorbani, Maimani, Momeni, Rahimi Mahid, Klavžar and Rus, *The general position problem on Kneser graphs and on some graph operations* (arXiv:1903.04286, Section 4.2, Theorem 4.4), determine the largest possible cardinality of a general-position set in \(L(K_n)\) and use the disjoint-clique support decomposition. Di Stefano, Klavžar, Krishnakumar, Tuite and Yero, *Lower General Position Sets in Graphs* (arXiv:2306.09965, Section 5, Theorem 5.2), determine the **smallest maximal** size and explicitly discuss disjoint stars and triangles for maximal sets. Those structural and extremal observations are not claimed to be new. Iršič, Klavžar, Rus and Tuite, *General Position Polynomials* (arXiv:2401.05696, Section 4, Theorem 4.2), enumerate all sizes for **Kneser** graphs \(K(n,2)\), the complements of the present triangular graphs, not for \(L(K_n)\). The asserted contribution here is the full polynomial for \(L(K_n)\), its bivariate exponential generating function, exact coefficient recurrence and maximum-set count.

## Limitations
The result concerns triangular graphs only. Its underlying star–triangle characterization and maximum cardinality were previously understood; this is an enumerative refinement, not a new general-position characterization. It does not establish a new unimodality or root-location theorem. An equivalent count written in general labeled-component-enumeration terminology could exist outside the indexed sources examined. The scripted enumeration stops at \(n=7\), while the proof covers every nonnegative integer \(n\). Independent mathematical review has not been performed.

## References
1. M. Ghorbani, H. R. Maimani, M. Momeni, F. Rahimi Mahid, S. Klavžar and G. Rus, *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286 (first posted 2019-03-11), Section 4.2. https://arxiv.org/abs/1903.04286
2. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite and I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (first posted 2023-06-16), Section 5. https://arxiv.org/abs/2306.09965
3. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first posted 2024-01-11), Section 4. https://arxiv.org/abs/2401.05696
