# The circle-valued mapping space of each minimal nine-point homotopically trivial finite space retracts to constants
## Finding
Let \(R\) be the nine-point finite \(T_0\)-space in Cianci--Ottina, Figure 1, and let \(R^{\mathrm{op}}\) be its opposite. Cianci and Ottina prove that, up to homeomorphism, these are the two nine-point homotopically trivial noncontractible finite spaces. Let \(C=S^0\circledast S^0\) denote the four-point minimal finite circle, with two minimal points below two maximal points.

For each \(X\in\{R,R^{\mathrm{op}}\}\), the compact-open mapping space \(\operatorname{Map}(X,C)\) has exactly \(172\) points, and the subspace of the four constant maps is a strong deformation retract. For \(R\), there is an explicit sequence of \(168\) beat-point deletions, consisting of \(68\) up-beat and \(100\) down-beat deletions, which leaves exactly the four constants. Their inherited pointwise order is precisely \(C\). Therefore
\[
\operatorname{Map}(X,C)\simeq C,
\qquad
[X,C]=\{*\}.
\]
Thus every individual map \(X\to C\) is null-homotopic, while the full finite mapping space is nevertheless noncontractible.

## Assumptions and scope
The specialization order is used for every finite \(T_0\)-space. The source \(R\) has points \(c_1,c_2,c_3,b_1,b_2,b_3,a_1,a_2,a_3\), with covers
\[
\begin{aligned}
&c_1<b_1,\ c_2<b_1,\\
&c_1<b_2,\ c_2<b_2,\ c_3<b_2,\\
&c_2<b_3,\ c_3<b_3,\\
&b_1<a_1,\ b_1<a_2,\\
&b_2<a_1,\ b_2<a_3,\\
&b_3<a_2,\ b_3<a_3.
\end{aligned}
\]
The target \(C\) has minima \(u_0,u_1\) and maxima \(v_0,v_1\), with \(u_i<v_j\) for all \(i,j\in\{0,1\}\). Continuity between finite \(T_0\)-spaces is equivalent to order preservation. The compact-open specialization order on the finite function space is the pointwise order.

The claim concerns the full finite mapping space, not merely its set of homotopy classes. No claim is made about mapping spaces into arbitrary targets.

## Proof
Every order-preserving map \(R\to C\) was exhaustively enumerated in two independent ways. Direct filtering of all \(4^9\) functions gives \(172\) maps. A second recursive enumeration prunes a partial assignment whenever it violates an already determined order relation; it returns the identical lexicographically ordered list of \(172\) maps.

On this \(172\)-element pointwise ordered set, the certificate in `beat_sequence.json` deletes \(168\) points. At each step the verifier recomputes the current active poset. For an up-beat deletion it checks that the recorded witness is the least element of the strict upper set; for a down-beat deletion it checks that the witness is the greatest element of the strict lower set. Hence every deletion is a Stong beat-point deletion and therefore a strong deformation retraction. The terminal set consists exactly of the four constant maps
\[
\operatorname{const}_{u_0},\quad
\operatorname{const}_{u_1},\quad
\operatorname{const}_{v_0},\quad
\operatorname{const}_{v_1}.
\]
The verifier checks all six relevant comparabilities and confirms that their inherited order is exactly the four-point circle order. The composite of the beat-point retractions is therefore a strong deformation retraction of \(\operatorname{Map}(R,C)\) onto its constant-map copy of \(C\).

For \(R^{\mathrm{op}}\), let \(\theta:C\to C\) be the order-reversing involution interchanging \(u_0\leftrightarrow v_0\) and \(u_1\leftrightarrow v_1\). If \(f:R^{\mathrm{op}}\to C\) is order-preserving, then \(\theta\circ f:R\to C\) is order-preserving, and this bijection reverses the pointwise order. Thus \(\operatorname{Map}(R^{\mathrm{op}},C)\cong \operatorname{Map}(R,C)^{\mathrm{op}}\). The same beat-point reduction dualizes, with up- and down-beat counts interchanged, and leaves the same constant-map core.

Finally, a finite-space homotopy class is a connected component of the mapping space; equivalently, two maps are homotopic exactly when joined by a fence of pointwise-comparable maps. Since the core \(C\) is connected, \([X,C]\) is a singleton for both sources.

## Verification
Run `python3 verify.py` in the directory containing `verify.py` and `beat_sequence.json`. The expected terminal line is:

`VERIFY_OK maps=172 deletions=168 up=68 down=100 core=4 constants dual_maps=172`

The verifier reconstructs the source and target orders from cover data, recomputes transitive closure, enumerates all maps twice, replays every beat-point witness against the current active mapping poset, checks the terminal induced order, and independently enumerates maps from the opposite source. Because the domain and target are finite and every one of the \(4^9\) set maps is covered by the first enumeration, the count is exhaustive rather than experimental sampling.

## Relationship to prior work
Cianci and Ottina classify the smallest homotopically trivial noncontractible finite spaces and identify exactly the two nine-point homeomorphism types \(R\) and \(R^{\mathrm{op}}\). Their paper supplies the source poset and the extremal motivation, but it does not state the \(172\)-map circle-valued function-space calculation or a constant-map core.

May proves the general finite-space function-space facts used here: the compact-open specialization order is pointwise order, and homotopies of maps between finite spaces are detected by fences of pointwise-comparable maps. These general statements do not determine the core of this particular \(172\)-point mapping space.

Barmak discusses the same nine-point poset in connection with fixed-point and collapsibility phenomena and records its earlier appearance in work of Rival. The inspected discussion does not give the circle-valued mapping-space enumeration or beat-point core. Rival's original paper was not available in full text during this comparison, so possible unnoticed overlap there remains a residual literature risk; the available bibliographic and secondary descriptions concern its fixed-point theorem rather than this mapping-space invariant.

## Limitations
The theorem is an exact statement about two specific nine-point sources and the four-point circle target. The strong deformation retraction is certified by a finite deletion sequence rather than by a closed-form family valid for broader targets. The source date recorded in the metadata is the first public arXiv date of the Cianci--Ottina source used here; the underlying nine-point poset appeared earlier in Rival's work, as explicitly noted above.

The literature search found no statement implying the exact \(172\)-point enumeration or the constant-map strong deformation retract, but absence from searched sources is not a proof of historical novelty. The inaccessible original Rival paper is the main residual originality risk.

## References
1. N. Cianci and M. Ottina, *Smallest homotopically trivial non-contractible spaces*, arXiv:1608.05307v1, submitted 2016-08-18; primary MSC 55P15.
2. J. P. May, *Finite Spaces and Larger Contexts*, Corollary 3.2.11 and Proposition 3.2.12 (function-space order and finite homotopy criterion).
3. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, Example 4.3.3 and the discussion of Rival's nine-point example.
4. I. Rival, *A Fixed Point Theorem for Finite Partially Ordered Sets*, Journal of Combinatorial Theory, Series A 21 (1976), 309--318.
