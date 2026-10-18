# A sharp ten-vertex character-spectrum collision for tree graphical groups

## Finding

For a finite tree \(T\) on \(n\) vertices and an odd prime power \(q\), let \(G_T(\mathbb F_q)\) be its class-two graphical group and let \(\operatorname{ch}_T(i;q)\) be the number of its irreducible complex characters of degree \(q^i\). The graph-to-character-spectrum map does **not** reconstruct trees, even if the complete degree distribution is supplied for **every** odd prime power.

**Theorem (sharp collision).** Among isomorphism classes of trees on at most nine vertices, no two different trees have the same character-degree multiplicities for every odd prime power \(q\). Among the 106 isomorphism classes of ten-vertex trees there is exactly **one unordered pair** with equal distributions for all such \(q\). One realization uses the following numbered vertex sets and edge lists:

\[
\begin{aligned}
E(T_A)=\{&(0,1),(0,6),(0,9),(1,2),(1,5),\\
 &(2,3),(3,4),(6,7),(7,8)\},\\
E(T_B)=\{&(0,1),(0,7),(1,2),(1,5),(2,3),\\
 &(2,4),(5,6),(7,8),(8,9)\}.
\end{aligned}
\]

The diameters are respectively \(7\) and \(6\), so these trees are nonisomorphic. For odd \(q\), their associated graphical Lie algebras are nonisomorphic, although their graphical groups have indistinguishable **complete irreducible-character degree distributions**. In this family the first collision occurs in Lie dimension \(n+|E(T)|=19\). Nonisomorphism of the groups as abstract groups is asserted at least for odd **prime fields** via the class-two Lazard correspondence; the assertion for general extension fields is not required.

Put \(u=q-1\). For the pair, write \(W_i(u)=\sum_{S\subseteq E(T)}u^{|S|}\mathbf1_{\nu(S)=i}\), with \(\nu(S)\) the matching number of the spanning support forest. The common polynomials are

\[
\begin{aligned}
W_0(u)&=1,\\
W_1(u)&=u(2u^2+10u+9),\\
W_2(u)&=u^2(u+1)(7u^2+28u+26),\\
W_3(u)&=2u^3(u+1)^2(u+2)(3u+7),\\
W_4(u)&=u^4(u+1)^3(u+3)^2.
\end{aligned}
\]

For \(0\le i\le4\), each graph has

\[
\operatorname{ch}_T(i;q)=q^{10-2i}W_i(q-1),
\]

and there are no characters of higher \(q\)-power degree. This conversion from \(W_i\) to characters is a **previously known** theorem; only the sharp minimum, unique tree pair, and consequent nonreconstruction assertion are claimed here.

## Assumptions and scope

Trees are finite, unlabelled for the isomorphism-class census, simple, connected and undirected. Graphical groups are the standard two-step nilpotent groups attached to graphs by assigning one central commutator coordinate to each edge. For the character conversion assume \(q\) odd, so the class-two Kirillov-orbit formula applies. A tree with \(n\) vertices has \(n-1\) edges and its graphical Lie algebra has dimension \(2n-1\). The matching number \(\nu(S)\) is the **maximum size** of a matching in the subgraph with edge set \(S\), not the number of matchings. The irreducible character degrees here are powers of \(q\) and their multiplicities count ordinary complex characters.

Equal universal spectra means equality for all odd prime powers, not just equality at a sampled field order. The sharpness assertion is restricted to connected trees and the specified graphical-group construction, not all finite \(p\)-groups or all graphical groups.

## Proof

**1. Character-theoretic reduction (known).** Let \(B_T(\boldsymbol y)\) denote the alternating \(n\times n\) weighted adjacency matrix with edge coordinates \(y_e\in\mathbb F_q\). For any forest support \(S=\{e:y_e\ne0\}\), a leaf-pivot congruence splits off a nonsingular \(2\times2\) alternating block, and a maximum matching can be chosen through the same leaf edge. Induction gives \(\operatorname{rank}B_T(\boldsymbol y)=2\nu(S)\), independent of the nonzero edge weights and characteristic. Exactly \((q-1)^{|S|}\) weight assignments have support \(S\). By the established Kirillov-orbit character-rank formula, the multiplicity of character degree \(q^i\) is

\[
q^{n-2i}\sum_{S:\nu(S)=i}(q-1)^{|S|}.
\]

This is precisely the already published all-tree matching-support character formula, not an originality claim of the present finding.

**2. A complete finite isomorphism-class census.** The accompanying standalone Python 3 verifier exhaustively constructs every unlabeled tree on \(n=1,\ldots,10\) vertices. Starting from the one-vertex tree, it attaches a leaf at every existing vertex in every already constructed \((n-1)\)-vertex representative, then keeps one representative per canonical tree code. Canonical codes are built by iteratively deleting leaves to obtain the one or two centers, recursively sorting rooted parenthesized subtree codes, and (when there are two centers) joining the two rooted halves in sorted order. The well-known center-rooted tree encoding is a complete tree-isomorphism invariant. Every \(n\)-vertex tree has a leaf, so reversing the leaf addition proves that no tree is omitted. Deduplication is therefore exact rather than probabilistic.

The resulting isomorphism-class counts for successive orders are \(1,1,1,2,3,6,11,23,47,106\).

For each representative with \(m=n-1\) edges, the verifier enumerates all \(2^m\) edge-support masks. It calculates the support's maximum matching size by exhaustive include/exclude recursion: given a selected edge, an optimal matching either excludes it or includes it and excludes all incident edges. Memorization accelerates the recursion without pruning any admissible alternative. It increments the exact integer coefficient

\[
c_{k,i}=|\{S\subseteq E(T):|S|=k,\nu(S)=i\}|.
\]

A map keyed by the full finite vector \((c_{k,i})\) groups potentially equivalent character spectra. The census detects **zero** repeated keys for \(n\le9\), and exactly **one** repeated key (two distinct tree codes) for \(n=10\); that repeated key is exactly the code pair displayed in the theorem. This establishes uniqueness and minimality without a nonexhaustive sample.

**3. Exact finite coefficient certificate.** For both displayed trees the complete nonzero values \((k,i,c_{k,i})\), arranged by edge count, are

\[
\begin{gathered}
(0,0,1);\ (1,1,9);\ (2,1,10),(2,2,26);\\
(3,1,2),(3,2,54),(3,3,28);\\
(4,2,35),(4,3,82),(4,4,9);\\
(5,2,7),(5,3,86),(5,4,33);\\
(6,3,38),(6,4,46);\ (7,3,6),(7,4,30);\\
(8,4,9);\ (9,4,1).
\end{gathered}
\]

For each fixed \(k\), the listed frequencies sum to \(\binom{9}{k}\). Summing \(c_{k,i}u^k\) over \(k\) yields the displayed \(W_i\), and hence the identical character-degree multiplicities for **all** odd \(q\), not merely tested values. Conversely, if two ten-vertex trees have identical character-degree distributions for all odd \(q\), the corresponding polynomials \(W_i(q-1)\) agree at infinitely many prime powers. Polynomial identity over the integers implies equality of all \(c_{k,i}\), so the finite key-based census is exactly the desired universal-spectrum classification.

**4. Nonreconstruction and dimension threshold.** The exact breadth-first-search diameters are \(7\) and \(6\), implying distinct tree-isomorphism types. Mainkar's graph rigidity for the associated two-step nilpotent Lie algebras over characteristic different from two gives their nonisomorphism. A graphical Lie algebra of a tree has dimension \(2n-1\), and the exhaustive absence of smaller tree collisions proves the threshold \(19\) within this construction. The group statement for odd prime fields follows from the class-two Lie correspondence for \(p>2\). This does not require any claim about character-table equality or full group-isomorphism classification at composite \(q\).

## Verification

Run the embedded independent program with Python 3:

```sh
python3 artifacts/verify_tree_collision.py
```

The program recomputes every unlabeled tree through ten vertices, the complete \(2^{n-1}\)-support matching profile of each tree, the unique collision, the edge lists and diameters, and the displayed frequency certificate. As a separate algebraic check, it constructs alternating adjacency matrices over \(\mathbb F_3\) and \(\mathbb F_5\) for **every** one of the 512 supports of each of the displayed trees, computes rank by modular Gaussian elimination, and independently recomputes matching number by a vertex-mask recursion. It additionally checks for \(q=3,5,7\) that

\[
\sum_{i=0}^{4}\operatorname{ch}_T(i;q)q^{2i}=q^{19},
\]

the character-degree-squared identity. The program ends with `VERIFY_OK`. The graph census is mathematically exhaustive over the finite stated range; the all-odd-field extension is a polynomial identity consequence of the previously known rank formula, not extrapolation from the finite-field tests.

## Relationship to prior work

Rossmann formulated the character enumeration question for graphical groups and investigated conjugacy class statistics. O'Brien and Voll derived the general commutator-rank-to-character count through orbit methods. A previously published all-tree result, *Tree graphical groups have matching-support character polynomials*, explicitly supplies the entire weighted-support formula and rooted recursion used in step 1. These known formulas are not independently new and are not presented as such. The additional result here is a **sharp inverse obstruction**: the first universally character-degree-indistinguishable nonisomorphic tree pair, a complete finite-range uniqueness certificate, and the threshold dimension. Mainkar's graph-rigidity theorem distinguishes the associated Lie algebras despite equal character-degree statistics.

An earlier census of generalized-cospectral trees is about adjacency and complement characteristic polynomials, not this support-matching polynomial. Neither its first-collision bound nor its example implies the present sharp ten-vertex statement. Targeted semantic mathematical-record searches using exact matching-support aliases, tree graphical character degrees, minimal collisions, and tree diameters did not find an equivalent exact threshold; absence from search results alone is not proof of priority.

## Limitations

The conclusion concerns full **character-degree multiplicity lists**, not the full ordinary character tables, representation rings, conjugacy-class size distributions, or group cohomology. Nonisomorphism of the associated Lie algebras is claimed over odd characteristic; abstract group nonisomorphism is asserted at least for odd prime fields, not unconditionally for all extension fields. The minimality is **within graphical groups constructed from connected trees**, and is not a minimum among all finite groups or nilpotent Lie algebras. Graphical group character multiplicities in even characteristic are not treated. The finite ten-vertex census depends on executing the included deterministic program, whose full source and outputs are reproducible. A specialized earlier table of the same matching-support invariant might supply equivalent information, so originality remains subject to further literature discovery and independent mathematical audit.

## References

1. E. A. O'Brien and C. Voll, “Enumerating classes and characters of \(p\)-groups,” arXiv:1203.3050v1 (public 14 March 2012), later *Transactions of the American Mathematical Society* **367** (2015), 7775–7796, DOI: 10.1090/tran/6276.
2. M. Mainkar, “Graphs and two-step nilpotent Lie algebras,” arXiv:1310.3414v1 (public 12 October 2013).
3. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” arXiv:2107.05564v1 (public 12 July 2021), *Bulletin of the London Mathematical Society* **54** (2022), 1923–1943, DOI: 10.1112/blms.12665.
4. “Tree graphical groups have matching-support character polynomials,” publicly accessible mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-tree-graphical-groups-have-matching-support-character-polynomial--fb80c871ed65 .
5. A standard tree-isomorphism algorithm based on the Aho–Hopcroft–Ullman center-rooted encoding; its full implementation is included in `artifacts/verify_tree_collision.py`.
