# Complete singleton two-rainbow domination spectra of paths and cycles

## Finding
For each finite graph \(G\), a *singleton two-rainbow dominating function* is a map \(f:V(G)\to\{0,1,2\}\) such that every zero-labelled vertex has at least one neighbour labelled \(1\) and at least one labelled \(2\). Its weight is \(w(f)=|\{v:f(v)\ne0\}|\). Let \(P_n(z)\) and \(C_n(z)\) be the polynomials summing \(z^{w(f)}\) over these functions on the labelled path of order \(n\) and labelled cycle of order \(n\), respectively.

**Theorem (joint open and cyclic spectra).** For every integer \(n\ge1\),
\[
P_n(z)=\sum_{k=0}^{\lfloor(n-1)/2\rfloor}\binom{n-k-1}{k}2^{n-2k}z^{n-k}.
\]
For every integer \(n\ge3\),
\[
C_n(z)=\sum_{0\le k<n/2}\frac{n}{n-k}\binom{n-k}{k}2^{n-2k}z^{n-k}
+4\mathbf1_{4\mid n}z^{n/2}.
\]
The first generating function is \(\sum_{n\ge1}P_n(z)t^n=2zt/(1-2zt-zt^2)\). The second is
\[
\sum_{n\ge3}C_n(z)t^n=
\frac{2zt(1+t)}{1-2zt-zt^2}
-\frac{2zt^2}{1+zt^2}-2zt-4z^2t^2.
\]
In particular, the exact number of minimum-weight functions on a cycle is \(2n\) for odd \(n\), \(4\) for \(4\mid n\), and \(n^2\) for \(n\equiv2\pmod4\). On a path the number is \(2\) for odd \(n\) and \(2n\) for even \(n\). Thus the cyclic boundary creates a sharp quadratic-versus-constant change in the minimum multiplicity.

## Assumptions and scope
All vertices have fixed distinct positions along the path or cycle; the labels \(1\) and \(2\) are distinct. There is no restriction on the neighbours of a positively labelled vertex. Paths have \(n\ge1\) vertices, cycles have \(n\ge3\) vertices and no multiple edges or loops. Unlike unrestricted two-rainbow domination, each positive vertex receives exactly one colour. The polynomial weights count positively labelled vertices, not the sum of their numeric labels. The cycles are unrooted as graphs but their vertex positions are fixed for enumeration: no division by rotations, reflections or colour exchange is made.

## Proof
Write \(Z=\{v:f(v)=0\}\), and let \(k=|Z|\). Every zero has two distinct neighbours of different positive colours. Thus zeros are pairwise nonadjacent, and, on a path, no endpoint belongs to \(Z\). Conversely, fix a zero set satisfying those necessary restrictions. Draw an auxiliary *inequality edge* between the two coloured neighbours of each zero. A colouring of the remaining \(n-k\) vertices is feasible exactly when the endpoints of every inequality edge have different colours.

For a path this auxiliary graph is a forest: its edges follow the line through the isolated omitted positions and cannot close a cycle. A forest with \(n-k\) vertices and \(k\) distinct inequality edges has \(n-2k\) components, hence exactly \(2^{n-2k}\) proper two-colourings. The eligible zero positions are the \(n-2\) interior vertices, so there are \(\binom{n-k-1}{k}\) ways to choose \(k\) pairwise nonadjacent zeros. Their feasible count gives the stated path sum, including \(n=1\) and \(n=2\).

For a cycle, if \(k<n/2\), at least one pair of consecutive vertices is positively labelled. In that case the auxiliary inequality graph again cannot close a cycle: closing it would force every positive vertex to be separated from both adjacent positive vertices by zeros all the way around the original cycle. It is therefore a forest with \(k\) edges, and has \(2^{n-2k}\) proper two-colourings. For \(0\le k<n/2\), the number of labelled independent \(k\)-sets of the cycle is \(\frac{n}{n-k}\binom{n-k}{k}\), as follows either by recording the positive gaps around the selected zeros or by a standard anchored-gap count.

The only missing case is \(k=n/2\), possible when \(n\) is even. The zeros alternate with positive vertices and there are exactly two possible zero sets. The inequality edges then form a cycle on \(n/2\) positively labelled vertices (possibly with two parallel constraints when \(n=4\)). This cycle admits precisely two colourings when \(n/2\) is even, and no colouring when \(n/2\) is odd. Accordingly the extremal contribution is \(4z^{n/2}\) when \(4\mid n\), and zero otherwise. This proves the cyclic polynomial in every permitted order.

For the rational expressions, define \(A_n(z)=(2z)^n I(C_n,(4z)^{-1})\), where \(I(C_n,x)\) counts independent vertex sets of the cycle. Its transfer matrix can be taken as
\[
T(z)=\begin{pmatrix}2z&z\\1&0\end{pmatrix}.
\]
For \(n\ge3\), \(A_n(z)=\operatorname{tr}(T(z)^n)\). The full-alternation case changes its naive coefficient by \(2(-1)^{n/2}z^{n/2}\) for even \(n\), so
\[
C_n(z)=\operatorname{tr}(T(z)^n)+(i\sqrt z)^n+(-i\sqrt z)^n
\qquad(n\ge3).
\]
The characteristic polynomial of \(T(z)\) is \(u^2-2zu-z\). Summing its two eigenvalue power series, and adding the conjugate pair \(\pm i\sqrt z\), gives the asserted cyclic rational generating function after removing the formal terms in degrees one and two. The path polynomial has initial terms \(P_1(z)=2z\), \(P_2(z)=4z^2\), and recurrence \(P_n(z)=2zP_{n-1}(z)+zP_{n-2}(z)\) for \(n\ge3\), giving its rational generating function.

The maximum allowable zeros and coefficients of their terms now prove the minimum claims: if \(n=2m+1\) is odd, the maximum is \(k=m\) with cyclic multiplicity \(2n\); if \(4\mid n\), it is \(k=n/2\) with multiplicity \(4\); if \(n\equiv2\pmod4\), the alternating support is impossible and \(k=n/2-1\), whose coefficient simplifies to \(n^2\). For paths, the maximum is \(\lfloor(n-1)/2\rfloor\), and the coefficient equals \(2\) in odd order and \(2n\) in even order.

## Verification
The included `verify.py` independently enumerates every assignment from \(\{0,1,2\}^n\) for paths of orders \(1\) through \(11\) and cycles of orders \(3\) through \(11\), testing the neighbourhood condition directly rather than using independent-set or forest identities. It checks every weight coefficient, examining 531426 assignments in total. It also verifies the complete coefficient formulas against the independent polynomial recurrences for orders \(3\) through \(100\). Successful execution prints `VERIFY_OK direct_assignments=531426 paths=1..11 cycles=3..11 recurrence_lengths=3..100`. The finite checks support but do not substitute for the proof for all orders.

## Relationship to prior work
Singleton two-rainbow domination is also called dual-server domination. Lange (2026, Proposition 12) gives the minimum *value* on cycles, including the distinction \(4\mid n\); this minimum is recovered here and is explicitly prior work. Žerovnik (2025) gives bounds for singleton two-rainbow domination on Cartesian products of paths and cycles. Bonomo and collaborators (2018) compare domination parameters involving two, and Bouchou and Blidia (2016) study criticality of a different, unrestricted two-rainbow invariant on paths and cycles. These established results motivate but do not state the joint *complete cardinality-polynomial* formulas or the corresponding number of minimum singleton functions established above. In particular the restriction to singleton colours must not be conflated with the set-valued standard two-rainbow model. The occurrence of independent-set polynomials in the proof is an exact reduction, not a claim that independent-set polynomials are new.

## Limitations
Only ordinary singleton two-rainbow domination with distinguishable positive colours is treated. No formula is claimed for arbitrary degree-two graph components beyond applying multiplication over disjoint components, for higher colour counts, or for unrestricted set-valued rainbow domination. The enumeration does not count colourings modulo automorphisms. Historical priority beyond the inspected sources may be affected by an earlier generic transfer-matrix or cyclic-word enumerator; independent mathematical and historical assessment is still needed.

## References
1. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow k-Domination in Regular Graphs*, arXiv:2610.06906v1 (first public version October 1, 2026), especially Proposition 12. https://arxiv.org/html/2610.06906v1
2. J. Žerovnik, *On 2-domination and 2-rainbow domination of cylindrical graphs*, Computational and Applied Mathematics (2025), DOI:10.1007/s40314-025-03201-2. https://link.springer.com/article/10.1007/s40314-025-03201-2
3. F. Bonomo, B. Brešar, L. N. Grippo, M. Milanič, M. D. Safe, *Domination parameters with number 2: interrelations and algorithmic consequences*, Discrete Applied Mathematics 235 (2018), 23–50, DOI:10.1016/j.dam.2017.08.017. https://arxiv.org/abs/1511.00410
4. A. Bouchou, M. Blidia, *Criticality indices of 2-rainbow domination of paths and cycles*, Opuscula Mathematica 36 (2016), 563–574, DOI:10.7494/OpMath.2016.36.5.563. https://www.opuscula.agh.edu.pl/om-vol36iss5art1
