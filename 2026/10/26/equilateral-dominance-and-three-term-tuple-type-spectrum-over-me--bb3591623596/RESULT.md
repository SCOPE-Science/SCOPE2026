# Equilateral dominance and three-term tuple-type spectrum over metric stars

## Finding
Let \(\mathcal U_3\) be the countable universal homogeneous metric space with distances \(\{0,1,2,3\}\). Fix the individually named \((n+1)\)-point metric star \(A_n=\{h,v_1,\ldots,v_n\}\), where \(d(h,v_j)=1\) and \(d(v_i,v_j)=2\) for distinct leaves. For integers \(k\ge1\) and \(n\ge0\), let \(T_k(n)\) count complete types of ordered, pairwise distinct \(k\)-tuples outside \(A_n\), over all named points of \(A_n\).

For every fixed \(k\), \(T_k(n)\) has an explicit finite **positive integer exponential spectrum**:
\[
 T_k(n)=\sum_{m\in\mathcal M_k} b(m)^n,
\]
where \(\mathcal M_k\) consists of all labelled \(\{1,2,3\}\)-valued metrics on \(\{h,x_1,\ldots,x_k\}\), and \(b(m)\) is the number of admissible distance vectors from one additional star leaf, defined precisely below.

For \(k\ge3\), the **three largest distinct spectral bases and their exact multiplicities** are
\[
\begin{array}{c|c}
\text{base}&\text{multiplicity}\\\hline
3^k&1\\
8\cdot3^{k-2}&\binom{k}{2}\\
22\cdot3^{k-3}&3\binom{k}{3}.
\end{array}
\]
Consequently,
\[
\begin{aligned}
T_k(n)={}&(3^k)^n+\binom{k}{2}(8\cdot3^{k-2})^n\\
&+3\binom{k}{3}(22\cdot3^{k-3})^n
+O_k\!\left((22\cdot3^{k-3}-1)^n\right).
\end{aligned}
\]
The constants in \(O_k\) depend only on \(k\), and the statement includes \(n=0\). In particular, a uniformly sampled type has an all-distance-two metric on its tuple together with the hub with probability
\[
1-\binom{k}{2}(8/9)^n+O_k((22/27)^n)\qquad(k\ge3).
\]
For \(k=2\), the complete exact spectrum is
\[
T_2(n)=9\cdot4^n+6\cdot5^n+6\cdot6^n+7^n+8^n+9^n.
\]
For \(k=1\), \(T_1(n)=3^n+2\cdot2^n\). These formulas count injective tuples disjoint from named parameters; equality/algebraic types are excluded.

## Assumptions and scope
Distances between distinct points in \(\mathcal U_3\) belong to \(\{1,2,3\}\). Such a countable Fraïssé limit exists because the finite metric spaces with this distance set have amalgamation. Complete tuple types over a finite named base correspond bijectively to labelled finite metric extensions: universality realizes every permitted extension, and ultrahomogeneity identifies realizations with identical distance matrices. There are no extra non-distance relations.

Given \(m\in\mathcal M_k\), write \(p_i=m(h,x_i)\), \(\delta_{ij}=m(x_i,x_j)\), and define
\[
 b(m)=\left|\left\{(s_1,\ldots,s_k)\in\{1,2,3\}^k:
 \begin{array}{l}
 |s_i-p_i|\le1\le s_i+p_i\ \text{for every }i,\\
 |s_i-s_j|\le\delta_{ij}\le s_i+s_j\ \text{for }i<j
 \end{array}\right\}\right|.
\]
Thus \(b(m)\) is an exact finite integer (at least one, because \(s_i=p_i\) is always admissible).

## Proof
**Leaf factorization.** Fix the distances among the new \(k\) points and from them to the hub, obtaining \(m\). A leaf \(v_t\), at distance one from the hub, can have the distance vector \(s\) precisely when the displayed inequalities hold: these are exactly all triangles involving that leaf, the hub, and the new tuple. Different leaves contribute independently. Indeed, for any two leaves and any new point, their mutual distance is two, while their two distances to that point lie in \(\{1,2,3\}\). The triangle inequalities hold automatically because the difference is at most two and the sum is at least two. All other triangles are already among the core or were checked. Consequently exactly \(b(m)^n\) metric extensions have the fixed core \(m\). Summing over cores establishes the full spectrum.

**Three largest bases.** The hub distances \(p_i=2\) impose no restriction on \(s_i\); either alternative hub distance admits only two of the three possible values. Thus if any hub distance differs from two, \(b(m)\le2\cdot3^{k-1}\). With all \(p_i=2\), a tuple edge of length two imposes no restriction on the two associated leaf entries. An edge of length one forbids the two ordered pairs \((1,3),(3,1)\); an edge of length three forbids just \((1,1)\).

The unrestricted core, with all hub and tuple distances equal to two, uniquely has \(b(m)=3^k\). Every other core has \(b(m)\le8\cdot3^{k-2}\), because the worst nontrivial individual edge is a length-three edge. Equality requires exactly one such edge and all other edges (including hub edges) of length two: any other imposed edge restriction removes an additional assignment. There are \(\binom{k}{2}\) such metrics, proving the second line of the spectral table.

For the remaining cores, a non-two hub distance gives at most \(18\cdot3^{k-3}\) vectors, and the presence of any length-one tuple edge gives at most \(21\cdot3^{k-3}\). If all hub distances are two and there are at least two length-three tuple edges, two such edges sharing an endpoint forbid two overlapping pairwise \((1,1)\) events among three ternary coordinates. Inclusion-exclusion leaves \(3^3-(3+3-1)=22\) options, hence at most \(22\cdot3^{k-3}\). If instead two length-three edges are disjoint, there are at most \(8^2\cdot3^{k-4}\), strictly less than \(22\cdot3^{k-3}\). Therefore the third base is \(22\cdot3^{k-3}\), attained exactly by two length-three edges sharing a vertex and all other distances two. Every further non-two edge strictly forbids an assignment not already excluded. The corresponding cores are metrics, since a length-three edge and two length-two edges form a valid triangle. Their number is \(k\binom{k-1}{2}=3\binom{k}{3}\).

Because all spectral bases are integers and the core set is finite for fixed \(k\), the remaining bases are at most \(22\cdot3^{k-3}-1\), proving the error bound. Dividing by \((3^k)^n\) proves equilateral dominance. The probability estimate follows by reciprocal expansion; the quadratic correction to the second term is exponentially smaller than \((22/27)^n\).

**Small arities.** For \(k=1\), hub distances one and three each allow two leaf distances, and hub distance two allows three. For \(k=2\), separate cores according to tuple distance one, two, or three. Their leaf-base multiplicities are, respectively, \((4:2,5:4,7:1)\), \((4:4,6:4,9:1)\), and \((4:3,5:2,6:2,8:1)\). Adding these gives the displayed complete formula.

## Verification
The included `verify_star_metric.py` uses complete finite metric triangle tests independently of the spectral formula for its direct brute-force counts. It checks all cores through arity four, compares the largest bases and their multiplicities to the theorem, and brute-force enumerates all extensions for arities one through three with zero, one, and two leaves, and for arity four with zero leaves. It also checks the pair formula for five leaf counts. Its recorded output ends with `ALL_TESTS_PASS`. These are finite corroborations, not an exhaustive computation for every arity or leaf count; the proof above establishes the infinite claims.

## Relationship to prior work
The existence, universality, and Katětov one-point extension criterion for finite-distance Urysohn metric spaces are classical; see Sauer's 2010 and 2011 accounts. The separate result on Widom–Rowlinson partition functions for nonalgebraic **one-types** of the generic three-distance metric space provides a related counting viewpoint, but does not state the ordered arbitrary-arity star spectrum, its three dominant bases, or their exact multiplicities. The present claim is limited to a fixed named metric star and injective tuples; it is not a general formula for arbitrary named finite metric parameters.

## Limitations
Novelty is assessed against accessible, searched literature and database results, not certified exhaustively. The exact full list of smaller spectral coefficients for arbitrary arity is supplied algorithmically by the finite \(\mathcal M_k\)-sum, rather than as a uniform closed expression. The theorem does not address parameter metrics other than this star or the corresponding limit with other allowed distance sets. No external independent validation is claimed.

## References
1. Norbert Sauer, *Vertex partitions of metric spaces with finite distance sets*, arXiv:1010.4212 (first public arXiv version 20 October 2010), especially Section 2 on Katětov functions and homogeneous finite-distance metrics, https://arxiv.org/abs/1010.4212.
2. Norbert Sauer, *Distance sets of universal and Urysohn metric spaces*, arXiv:1107.4794 (first public arXiv version 24 July 2011), especially Sections 1–2 on distance sets and extension criteria, https://arxiv.org/abs/1107.4794.
3. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, published-finding corpus record `2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989` (comparison source; its accessible summary describes only one-types).
