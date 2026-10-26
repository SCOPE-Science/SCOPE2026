# Outer-independent two-rainbow weight enumerator of triangular graphs

## Finding

Let \(n\ge5\) be an integer, let \(T_n=L(K_n)=J(n,2)\), and assign to each vertex one of the four labels \(\varnothing,\{1\},\{2\},\{1,2\}\). A labeling is **outer-independent two-rainbow dominating** when its empty-labeled vertices form an independent set and each empty-labeled vertex has both colors in the union of its neighbors' labels. Its weight is the sum of label cardinalities. Write \(P_n(z)=\sum_f z^{w(f)}\), summing over all such labelings with distinct named colors \(1\) and \(2\).

Put \(N=\binom n2\), \(m_t=n!/(2^t t!(n-2t)!)\), \(L_t=N-t\), and \(U_k=2k(n-k-1)\). Then the complete weight polynomial is
\[
\boxed{P_n(z)=\sum_{t=0}^{\lfloor n/2\rfloor}m_t z^{L_t}\left[(z+2)^{L_t}+2\sum_{k=1}^{t}(-1)^k\binom tk(z+2)^{L_t-U_k}\right].}
\]
Every exponent \(L_t-U_k\) is nonnegative. For \(n\ge5\), the minimum weight and the exact number of minimum-weight labelings are
\[
\boxed{\gamma_{oir2}(T_n)=N-\lfloor n/2\rfloor,\qquad
[z^{N-\lfloor n/2\rfloor}]P_n(z)=m_h\left(2^{N-h}+2\sum_{k=1}^h(-1)^k\binom hk2^{N-h-U_k}\right),\quad h=\lfloor n/2\rfloor.}
\]
The minimum counts are \(3630\) for \(n=5\) and \(60060\) for \(n=6\). More generally, conditional on an arbitrary fixed maximum matching as the empty set, at least the fraction \(1-2h\,2^{-2(n-2)}\) of all singleton-color assignments to the remaining edges are valid; thus the conditional fraction tends to \(1\) exponentially quickly. The new assertion is the all-weight enumerator, not merely the lower bound from vertex cover.

## Assumptions and scope

All graphs are finite, labeled, simple and undirected. A vertex of \(T_n\) is an unordered pair \(\{i,j\}\subseteq[n]\), equivalently an edge of \(K_n\). Two such vertices are adjacent precisely when their pairs intersect. The polynomial distinguishes the colors, so interchanging \(1\) and \(2\) normally counts a different labeling. Empty labels have weight \(0\); singleton labels weight \(1\); double labels weight \(2\). The primary statement covers every integer \(n\ge5\), with no asymptotic or genericity assumptions.

## Proof

**Matching reduction.** The vertices carrying \(\varnothing\) correspond to pairwise nonincident edges of \(K_n\), hence to a unique matching \(M\) of size \(t\), where \(0\le t\le\lfloor n/2\rfloor\). There are \(m_t\) possible matchings. Exactly \(L_t=N-t\) edges remain, each requiring one of the three nonempty labels. Their unrestricted weight factor is \((2z+z^2)^{L_t}=z^{L_t}(z+2)^{L_t}\).

**Bad events and common neighborhoods.** For a missing matching edge \(e=uv\), its neighbors in \(T_n\) are all other edges of \(K_n\) incident with \(u\) or \(v\). Every one is outside \(M\). There are \(2(n-2)\) of them. Let \(B_{e,c}\) be the event that color \(c\in\{1,2\}\) is absent from their labels. Since those labels are nonempty, \(B_{e,1}\) forces all these labels to equal \(\{2\}\), and \(B_{e,2}\) forces them to equal \(\{1\}\).

Choose \(k\) distinct edges of \(M\). Their combined neighborhoods in \(T_n\) contain precisely
\[
U_k=k\cdot2(n-2)-4\binom k2=2k(n-k-1)
\]
selected edges: the four edges joining each pair of disjoint matched pairs were double-counted. For a fixed one-color absence event at every one of these \(k\) matched edges, those \(U_k\) selected edges are forced to the opposite singleton label, while the other \(L_t-U_k\) selected edges remain arbitrary. The weight factor is \(z^{U_k}(2z+z^2)^{L_t-U_k}=z^{L_t}(z+2)^{L_t-U_k}\).

Any intersection requiring absence of both colors is impossible. For two different matching edges, each of their four connecting edges is a common selected neighbor; it cannot be simultaneously forced to \(\{1\}\) and \(\{2\}\). For the same edge, the nonempty neighbors cannot simultaneously avoid both colors. Consequently, inclusion-exclusion over the \(2t\) bad events has only two homogeneous-color subfamilies. Each subset of \(k\ge1\) matched edges contributes twice the sign \((-1)^k\) with the factor above. This gives the displayed fixed-matching polynomial and, after multiplication by \(m_t\) and summation over \(t\), the claimed formula.

**Minimum and multiplicity.** At most \(h=\lfloor n/2\rfloor\) vertices may carry \(\varnothing\), and each other vertex contributes weight at least \(1\); hence \(w(f)\ge N-h\). To realize equality take any maximum matching, split each matched pair across two parts \(A,B\) (put the sole unmatched vertex, if any, in \(A\)), and label selected same-part edges \(\{1\}\), selected cross-part edges \(\{2\}\). Since \(n\ge5\), both parts contain at least two vertices. Every matched edge has selected neighbors of both types. Hence equality is attained. Equality forces exactly \(h\) empties, all other labels singleton. Taking the coefficient of \(z^{N-h}\) in the already established enumerator yields the exact minimum-count formula.

**Density of optimum colorings.** For a fixed maximum matching, independently color each selected edge with \(\{1\}\) or \(\{2\}\) uniformly. For each of the \(h\) empty edges, the probability that one specified color is missing equals \(2^{-2(n-2)}\). The union bound over both colors and all empty edges gives failure probability at most \(2h\,2^{-2(n-2)}\). This proves the quantitative density statement.

## Verification

The standalone script `verify_oi2rd_triangular.py` implements the original four-label neighborhood definition separately from the symbolic formula. It enumerates all \(4^{\binom n2}\) assignments for \(n=3,4,5\), comparing each full coefficient profile, and independently enumerates all singleton-color assignments for maximum matchings through \(n=6\). The resulting full profiles for \(n=3,4,5\) and minimum counts \(6,42,3630,60060\) agree with the formula. The cases \(n=3,4\) are checks of algebraic boundary behavior; the asserted new family begins at \(n=5\). The recorded output is in `verification_output.txt`. These finite checks do not prove the theorem for unrestricted \(n\); the inclusion-exclusion proof above does.

## Relationship to prior work

Outer-independent rainbow domination and its vertex-cover bounds were established in the 2019–2022 literature. Mansouri and Mojdeh (2020) give general bounds and selected graph-family minimum values; Cabrera-Martínez (2022) sharpens inequalities and studies graph joins, lexicographic and corona products; Samadi and Soltankhah (2022 preprint; 2023 publication) study claw-free equality structures and several graph products. Those numerical and structural bounds do not enumerate all labelings on \(T_n\). The triangular graph is a line graph, so its empty sets correspond to matchings; the new enumeration additionally handles the coupled two-color constraints at each matching edge. A publicly indexed enumerator for ordinary two-rainbow functions on complete multipartite graphs concerns a different invariant and graph family: \(T_n\) is not complete multipartite when \(n\ge5\) (nonadjacency fails transitivity). Previously known vertex-cover inequalities explain the minimum lower bound but do not imply the complete polynomial or minimum multiplicity formula. The bibliographic priority claim remains provisional pending independent literature review.

## Limitations

This theorem enumerates outer-independent two-rainbow functions on triangular graphs \(T_n\) only. It does not enumerate unrestricted rainbow domination, outer-independent total rainbow domination, arbitrary line graphs, or Johnson graphs \(J(n,k)\) for \(k\ge3\). It does not assert that the vertex-cover bound or the minimum value is itself previously unknown. Full coverage of obscure and unindexed literature has not been demonstrated. The mathematical checks and review are not independent validation.

## References

1. A. Cabrera-Martínez, *A Note on Outer-Independent 2-Rainbow Domination in Graphs*, Mathematics **10** (2022), article 2287, doi:10.3390/math10132287. Public 30 June 2022; primary MSC 05C69.
2. B. Samadi and N. Soltankhah, *Further results on outer independent 2-rainbow dominating functions of graphs*, arXiv:2208.02340 (initial posting 3 August 2022); RAIRO Operations Research **57** (2023), doi:10.1051/ro/2023097.
3. Z. Mansouri and D. A. Mojdeh, *Outer independent rainbow dominating functions in graphs*, Opuscula Mathematica **40** (2020), 599–615, doi:10.7494/OpMath.2020.40.5.599.
4. Q. Kang, V. Samodivkin, Z. Shao, S. M. Sheikholeslami, and M. Soroudi, *Outer-independent \(k\)-rainbow domination*, Journal of Taibah University for Science **13** (2019), 883–891, doi:10.1080/16583655.2019.1655255.
