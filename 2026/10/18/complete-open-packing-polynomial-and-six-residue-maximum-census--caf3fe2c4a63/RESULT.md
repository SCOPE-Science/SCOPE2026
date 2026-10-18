# Complete open-packing polynomial and six-residue maximum census of circular ladders

## Finding

For an integer \(n\ge 3\), let \(P_n=C_n\square K_2\) have vertices \(a_i,b_i\) for \(i\in\mathbb Z/n\mathbb Z\), with edges \(a_ia_{i+1}\), \(b_ib_{i+1}\), and \(a_ib_i\). An **open packing** is a subset \(S\) such that distinct vertices in \(S\) have disjoint open neighbourhoods. Define the complete cardinality polynomial
\[
O_n(z)=\sum_{S\text{ an open packing of }P_n}z^{|S|}.
\]
For \(m\ge 3\), put
\[
J_m(z)=\sum_{k=0}^{\lfloor m/3\rfloor}
  \frac{m}{m-2k}\binom{m-2k}{k}z^k.
\]
The fractions represent integers, and the term for \(k=0\) equals \(1\). Then the exact **all-size polynomial** is
\[
\boxed{\quad O_n(z)=\begin{cases}J_{2n}(z),&n\text{ odd},\\ J_n(z)^2,&n\text{ even}.\end{cases}\quad}
\]
In fact, the common-neighbour conflict graph of \(P_n\) is isomorphic to the square of the cycle \(C_{2n}\) if \(n\) is odd, and to the disjoint union of two copies of \(C_n^2\) if \(n\) is even. This isomorphism is explicit.

Consequently the largest open-packing size is
\[
\rho^{\mathrm o}(P_n)=\begin{cases}
\lfloor2n/3\rfloor,&n\text{ odd},\\
2\lfloor n/3\rfloor,&n\text{ even},
\end{cases}
\]
and the number \(M_n\) of maximum open packings is
\[
\boxed{\quad
M_n=\begin{cases}
9,&n\equiv0\pmod 6,\\
\frac{n(2n+1)}{3},&n\equiv1\pmod 6,\\
\left(\frac{n(n+1)}{6}\right)^2,&n\equiv2\pmod 6,\\
3,&n\equiv3\pmod 6,\\
n^2,&n\equiv4\pmod 6,\\
2n,&n\equiv5\pmod 6.
\end{cases}\quad}
\]
All vertex positions and both prism layers are distinguished when counting. No quotient by graph automorphisms is taken.

## Assumptions and scope

Graphs are finite, simple, undirected, and labelled by the indices above; \(C_3\) is a triangle. The cycle power \(C_m^2\) joins distinct vertices at circular distance at most two. The empty set is included in \(O_n(z)\), and the definition uses open, not closed, vertex neighbourhoods. The assertions hold for every integer \(n\ge3\), including the small cases \(n=3\) and \(n=4\). The enumerator concerns **vertex** open packing, not edge open packing.

## Proof

**1. Exact conflict graph.** Give the auxiliary graph \(H_n\) vertex set \(V(P_n)\) and join two *distinct* vertices precisely when their open neighbourhoods in \(P_n\) intersect. Since
\[
N(a_i)=\{a_{i-1},a_{i+1},b_i\},\qquad
N(b_i)=\{b_{i-1},b_{i+1},a_i\},
\]
two vertices of the same \(a\)-layer (respectively \(b\)-layer) are adjacent in \(H_n\) precisely when their indices differ by \(\pm2\) modulo \(n\), and an \(a_i\) and a \(b_j\) are adjacent precisely when \(j-i\equiv\pm1\pmod n\). When \(n=3\), the same-layer condition includes the two other vertices of each triangle; when \(n=4\), \(+2\) and \(-2\) indicate the same opposite vertex. Both edge cases are covered by the statement.

Let \(g=\gcd(2,n)\). For each \(\varepsilon\in\{0,\dots,g-1\}\), list the following \(2n/g\) vertices in cyclic order, with \(j=0,\dots,n/g-1\):
\[
a_{\varepsilon+2j},\ b_{\varepsilon+2j+1}.
\]
Indices are read modulo \(n\). These \(g\) lists are disjoint and cover every vertex once. Consecutive terms in each list are a cross-layer pair whose indices differ by \(\pm1\), while terms two positions apart are a same-layer pair whose indices differ by \(\pm2\). Conversely, the exact adjacency conditions displayed above show that every edge of \(H_n\) joins positions at cyclic distance one or two in one of these lists. Thus
\[
H_n\cong\bigsqcup_{j=1}^{g}C_{2n/g}^{2}.
\]
This includes \(n=3\), giving \(C_6^2\), and \(n=4\), giving two copies of \(C_4^2=K_4\).

**2. Exact bijection and enumeration.** A subset \(S\subseteq V(P_n)\) is an open packing if and only if no two of its vertices are adjacent in \(H_n\). Thus \(O_n(z)\) is the independence polynomial of \(H_n\). Independence polynomials multiply on disjoint unions, reducing the claim to the independence polynomial of \(C_m^2\).

For an independent \(k\)-set in \(C_m^2\), list selected vertices clockwise. Their \(k\) successive positive cyclic gaps are all at least three, and sum to \(m\). For \(k\ge1\), after subtracting three from every gap there remain \(m-3k\) indistinguishable units distributed among \(k\) gaps, in
\[
\binom{m-2k-1}{k-1}
\]
ways. There are \(m\) choices for the designated first marked vertex and each actual \(k\)-set is counted \(k\) times. Hence the exact coefficient is
\[
\frac{m}{k}\binom{m-2k-1}{k-1}
=\frac{m}{m-2k}\binom{m-2k}{k},\qquad
1\le k\le\lfloor m/3\rfloor.
\]
No positive \(k\) is feasible beyond that range. The empty set contributes one. This proves \(J_m\) and the displayed formula for \(O_n\), with no asymptotics or induction hypotheses.

**3. Extremal coefficient.** The highest nonzero degree of \(J_m\) is \(k=\lfloor m/3\rfloor\). Write \(m=3q+r\), \(0\le r\le2\); its leading coefficient is \(3\) for \(r=0\), \(m\) for \(r=1\), and \(m(m+1)/6\) for \(r=2\). The even-prism leading coefficient is the square of that number with \(m=n\), and the odd-prism leading coefficient is that number with \(m=2n\). Simplifying by \(n\bmod6\) gives exactly the maximum sizes and all six multiplicity branches above. In particular the exceptional even residue \(n\equiv2\pmod6\) loses one vertex relative to \(\lfloor2n/3\rfloor\).

## Verification

The standalone `verify.py` constructs the original prism adjacency lists independently from the formula and enumerates all \(1,398,080\) labelled vertex subsets for \(3\le n\le10\); each is checked against the direct open-neighbourhood condition. Their cardinality profiles agree coefficientwise with the stated formula. An independent cyclic-column transfer counts the entire polynomial for every \(3\le n\le40\), and direct graph construction checks the explicit cycle-square edge isomorphism for all those dimensions. The six-residue maximum formulas agree with the closed coefficient formula through \(n=150\). Run `python3 verify.py`; the exact expected standard output is embedded as `verification_output.txt`. These finite checks test the implementation and examples; the all-\(n\) result is established by the bijective proof above.

For example, \(O_3(z)=1+6z+3z^2\), \(O_4(z)=1+8z+16z^2\), and \(O_5(z)=1+10z+25z^2+10z^3\).

## Relationship to prior work

The notions of open packing and the two-step (common-neighbour) graph are established; see Brešar, Samadi and Yero (2023), and Samadi, Soltankhah and Yero (2024). Mojdeh, Peterin, Samadi and Yero (2020), Section 3, develop general lower and upper bounds for open packing in Cartesian products; the inspected results do not give the labelled all-cardinality census of circular ladders. The latter studies injective colourings of direct, lexicographic and corona products, not this entire open-packing polynomial on Cartesian prisms. Brešar, Klavžar and Rall (2023), Theorem 2.2, prove \(\rho^{\mathrm o}(G\square K_2)=2\rho_2(G)\) for bipartite \(G\). For even \(n\), that theorem already determines the **maximum size**, and this numerical fact is not claimed as new. The theorem does not enumerate arbitrary open packings or give the maximum-set multiplicities here. Koster, Volkmann and Wehrmann (2026), Theorem 1, prove a cubic-graph relation \(\gamma_{stR}(G)=|V(G)|-\rho^{\mathrm o}(G)\); applying that existing theorem to the maximum size here yields the corresponding signed total Roman minimum, but that relation itself is not new. The present exact conflict-graph isomorphism and complete, labelled cardinality polynomial supply the structural and enumerative refinement. Independent prior discovery of the same cycle-square isomorphism or polynomial under a different terminology remains a possible priority risk.

## Limitations

The result concerns the ordinary two-layer Cartesian prism only, not arbitrary graph products, Möbius ladders, or edge open packings. It gives labelled counts, not automorphism-orbit counts, and does not independently establish any new general algorithmic complexity bound. Any externally known formula for open packing on a different graph family must be compared by implication, not title alone. No independent mathematical audit has been performed and comprehensive bibliographic priority cannot be guaranteed.

## References

1. A. M. C. A. Koster, L. Volkmann and M. Wehrmann, *Signed Total Roman Domination and Domatic Numbers: Degree Three and Complete Multipartite Graphs*, arXiv:2606.27175, first posted 2026-06-25, https://arxiv.org/abs/2606.27175 .
2. B. Brešar, S. Klavžar and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963, first posted 2023-09-10, https://arxiv.org/html/2309.04963v1 .
3. B. Brešar, B. Samadi and I. G. Yero, *Injective coloring of graphs revisited*, Discrete Mathematics 346 (2023), 113348; arXiv:2106.09823, https://arxiv.org/abs/2106.09823 .
4. B. Samadi, N. Soltankhah and I. G. Yero, *Injective coloring of product graphs*, Bulletin of the Malaysian Mathematical Sciences Society (2024); arXiv:2306.01488, https://arxiv.org/html/2306.01488v1 .
5. D. A. Mojdeh, I. Peterin, B. Samadi and I. G. Yero, *(Open) packing number of some graph products*, Discrete Mathematics & Theoretical Computer Science 22:4 (2020), 1, arXiv:1901.06813, https://arxiv.org/abs/1901.06813 .
