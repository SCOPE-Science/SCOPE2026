# Exact Minkowski asymmetry and unique centers of semi-balanced cactus root polytopes

## Finding
Let \(G=(V,E)\) be a connected finite simple cactus graph with at least two edges: each edge belongs to at most one undirected simple cycle. Orient each edge once so that every cycle has equally many edges directed in its two cyclic directions (a *semi-balanced orientation*). Put
\[
Q_G=\operatorname{conv}\{r_e=e_{\mathrm{head}(e)}-e_{\mathrm{tail}(e)}:e\in E\}\subset\mathbb R^V.
\]
Let \(B\) be the bridge-edge set and \(\mathcal C\) the set of undirected cycles of \(G\). Define
\[
H=|B|+\sum_{C\in\mathcal C}\frac{|E(C)|}{2}.
\]
Then \(H\) is an integer at least \(2\), the intrinsic Minkowski asymmetry and its **unique** minimizing center are
\[
\boxed{s(Q_G)=H-1,\qquad
c_G=\frac1H\left(\sum_{e\in B}r_e+\frac12\sum_{e\in E\setminus B}r_e\right).}
\]
Thus the unique center assigns twice as much convex-combination weight to any bridge edge as to any cycle edge, independently of cycle sizes or the chosen semi-balanced orientation. In particular, the asymmetry is independent of the cyclic arrangement of directions, and depends only on the number of bridges and the half-lengths of the cycles.

There is a constructive, integer-coefficient sharpness certificate: for **every** \(e\in E\), there are exactly \(H-1\) **distinct** edges \(f\ne e\) such that
\[
\boxed{Hc_G-r_e=\sum_{f\in S_e}r_f,\qquad |S_e|=H-1.}
\]
Consequently the reflected point \((Hc_G-r_e)/(H-1)\) is the uniform average of \(H-1\) distinct root-polytope vertices.

## Assumptions and scope
All convex bodies and centers are taken in the affine hull of the root polytope. For a positive-dimensional polytope \(P\), define its Minkowski asymmetry by
\[
s(P)=\min_{c\in\operatorname{relint}P}\inf\{s\ge1:-(P-c)\subseteq s(P-c)\}.
\]
A tree with at least two edges is included; its root polytope is a positive-dimensional simplex. The graph may have multiple cycles, arbitrarily arranged bridges, and cut vertices. Since every cycle is semi-balanced, all cycles are even. The statement does not address odd-cycle graphs, non-semi-balanced orientations, multiple edges, loops, or one-edge (zero-dimensional) polytopes. The Euclidean metric is irrelevant because Minkowski asymmetry is affine invariant.

## Proof
**1. Affine circuit decomposition.** Let \(n=|V|\), \(m=|E|\), and \(q=|\mathcal C|\). Because \(G\) is connected and its cycles are edge-disjoint, \(m=n-1+q\). The oriented incidence matrix with columns \(r_e\) has rank \(n-1\). A semi-balanced orientation admits a vertex potential \(\ell\) with \(\ell(\mathrm{head}(e))-\ell(\mathrm{tail}(e))=1\); hence all \(r_e\) belong to the common affine hyperplane \(\ell\cdot x=1\). Thus the space of affine dependencies among the \(m\) root vectors has dimension \(m-(n-1)=q\).

For each cycle \(C\) of length \(2k_C\), fix a cyclic traversal and split its edges into two classes \(C^+\) and \(C^-\) according to agreement with that traversal. Semi-balancedness gives \(|C^+|=|C^-|=k_C\), and telescoping gives the affine relation
\[
\sum_{e\in C^+}r_e=\sum_{e\in C^-}r_e.
\]
The \(q\) relations are independent because the cycles are edge-disjoint, and exhaust all affine dependencies by the dimension count. Consequently \(Q_G\) is the affine **join** of one factor \(Q_C=\operatorname{conv}\{r_e:e\in C\}\) per cycle and one singleton factor \(\{r_e\}\) per bridge. Here 'join' means that the affine dependencies of the vertex configuration are precisely the dependencies internal to each factor.

**2. A balanced cycle factor.** Fix a cycle of length \(2k\), with \(k\ge2\). Each of its two \(k\)-vertex classes \(C^+\) and \(C^-\) spans an affine \((k-1)\)-simplex: the only affine relation among all \(2k\) root vectors is the one displayed above, so each proper subset is affinely independent. Both simplices contain in their relative interiors the common barycenter
\[
b_C=\frac1k\sum_{e\in C^+}r_e=\frac1k\sum_{e\in C^-}r_e
=\frac1{2k}\sum_{e\in C}r_e.
\]
Their affine direction spaces intersect trivially, as another intersection would produce an additional affine dependence. Hence \(Q_C\), translated by \(-b_C\), is a free sum of two simplices in complementary linear spaces.

A \((k-1)\)-simplex has Minkowski asymmetry \(k-1\), uniquely minimized at its barycenter: if a proposed center has barycentric coordinates \(a_1,\ldots,a_k\), reflecting the \(i\)-th vertex forces \((s+1)a_i\ge1\) for every \(i\); summation forces \(s\ge k-1\), with equality only when all \(a_i=1/k\). Projecting the free sum onto either simplex direction space proves that \(Q_C\) has asymmetry at least \(k-1\) and forces any sharp center to project to the simplex barycenter. Conversely, the negative of each cycle vertex relative to \(b_C\) lies in \((k-1)(Q_C-b_C)\), by averaging the other \(k-1\) vertices in its own class. Thus \(s(Q_C)=k-1\), with unique center \(b_C\).

**3. The join rule and its uniqueness.** Consider an affine join of \(r\) compact convex factors \(P_i\), each having a unique Minkowski center \(b_i\). Set \(\sigma_i=s(P_i)\) for positive-dimensional factors and \(\sigma_i=0\) for singleton factors. Write any interior center of the join uniquely as \(c=\sum_i\theta_i c_i\) with \(\theta_i>0\), \(\sum_i\theta_i=1\), and \(c_i\in\operatorname{relint}P_i\). For a vertex \(x\in P_i\), its reflection \(((s+1)c-x)/s\) can belong to the join only if
\[
(s+1)\theta_i-1\ge\sigma_i.
\]
Indeed the unnormalized \(i\)-th factor component is \((s+1)\theta_i c_i-x\); it must be a nonnegative multiple of a point of \(P_i\), and for non-singleton \(P_i\) the required multiple is at least its optimal reflection factor. For singleton factors mere nonnegativity gives the same inequality with \(\sigma_i=0\). Summing yields
\[
s+1\ge\sum_i(\sigma_i+1).
\]
Equality is achieved by \(\theta_i=(\sigma_i+1)/\sum_j(\sigma_j+1)\) and \(c_i=b_i\); the reflected vertices then lie in the join. Equality also forces every factor center and every \(\theta_i\), proving uniqueness. Therefore the join has asymmetry \(\sum_i(\sigma_i+1)-1\).

For the cactus factors, \(\sigma_C=k_C-1\), while \(\sigma_e=0\) for bridge singletons. Substitution gives \(s(Q_G)=H-1\) and \(c_G=H^{-1}(\sum_{e\in B}r_e+\sum_C k_C b_C)\), which is exactly the displayed center formula.

**4. Explicit reflection certificate.** For each cycle, fix one of its equal-size edge classes, \(C^+\) or \(C^-\). If the reflected edge \(e\) belongs to a cycle, choose the class **containing** \(e\) in that cycle, remove \(e\), and choose either class in every other cycle. Include all bridge edges except \(e\) if \(e\) is itself a bridge. The selected edges form a set \(S_e\) of cardinality \(H-1\). The equal-sum cycle identities give \(\sum_{f\in S_e}r_f=Hc_G-r_e\). This verifies sharp reflected containment constructively. The join lower bound and uniqueness already proved establish that the factor \(H-1\) cannot be improved.

## Verification
Run `python verify.py` with Python 3 and no external dependencies. The verifier constructs 270 deterministic oriented cactus examples (including pure trees, mixed even cycles, bridges, and differently oriented balanced cycles), checks the exact affine ranks, each cycle's equal-sum affine dependence, the positive center coefficients, and all 3,685 exact reflection identities using rational arithmetic. Its output is `VERIFY_OK cases= 270 reflection_identities= 3685`.

The finite checks test implementations and boundary examples; they do **not** prove the theorem for all cacti. The all-size proof is the affine-dependency, simplex, and join argument above. The tested construction interleaves cycle and bridge additions and hence includes bridges between different cycles.

## Relationship to prior work
Kálmán and Tóthmérész (arXiv:2105.00960, Sections 2–3 and 11) define semi-balanced root polytopes, characterize their affine cycle dependencies, and study Jaeger dissections, interior polynomials and gluing product formulas. Those algebraic cycle facts are used here. Their statements do not provide the present Minkowski asymmetry, unique center, or uniform-reflection certificate for cactus configurations.

Numata, Takahashi and Tamaki (arXiv:2203.14521, Sections 1 and 5) classify faces of directed edge polytopes and discuss cycles and trees, rather than Minkowski reflection factors. Kálmán and Tóthmérész (arXiv:2203.17127) calculate graph-polytope Ehrhart data via spanning-tree activity, not affine asymmetry. A published published-finding corpus result on oriented cycle root polytopes gives exact Ehrhart polynomials and the balanced cycle dependence; it concerns only individual cycles and does not assert this Minkowski classification for cacti. These results are compatible as structural background, not the same invariant or a known stronger asymmetry theorem.

## Limitations
This is a complete classification **only** for connected semi-balanced cactus graphs with at least two edges. A general semi-balanced graph may have overlapping cycles whose affine relations do not decompose into independent blocks, so the join argument does not extend unchanged. One-edge root polytopes are excluded because the asymmetry convention for zero-dimensional bodies varies. Literature searches and inspected primary material did not identify the exact result, but no search can establish universal priority; an equivalent theorem under signed graph edge-polytopes or free-sum convexity terminology remains a residual risk. Independent external validation has not been performed.

## References
1. Tamás Kálmán and Lilla Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960 (first public version 2021-05-03), *Mathematika* 68 (2022), 1176–1220, DOI 10.1112/mtk.12163.
2. Yasuhide Numata, Yusuke Takahashi, and Dai Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521 (first public version 2022-03-28).
3. Tamás Kálmán and Lilla Tóthmérész, *\(h^*\)-vectors of graph polytopes using activities of dissecting spanning trees*, arXiv:2203.17127 (first public version 2022-03-31), *Algebraic Combinatorics* 6 (2023), 1637–1651, DOI 10.5802/alco.318.
4. *Exact Ehrhart polynomials of oriented cycle root polytopes*, publicly available published-finding corpus research record, identifier 2026/10/4/SCOPE-exact-ehrhart-polynomials-of-oriented-cycle-root-polytopes--e32575b66377.
