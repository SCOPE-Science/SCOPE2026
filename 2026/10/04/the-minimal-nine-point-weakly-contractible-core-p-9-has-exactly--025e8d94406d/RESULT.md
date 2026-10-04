# The minimal nine-point weakly contractible core has exactly two maximal contractible opens
## Finding
Let \(P(9)\) be the nine-point finite \(T_0\)-space with minima \(c_0,c_1,c_2\), middle points \(p,q,y\), maxima \(g,h,k\), and cover relations
\[
c_0<p,y,\qquad c_1<p,q,y,\qquad c_2<q,y,
\]
\[
p<g,h,\qquad q<g,k,\qquad y<h,k.
\]
Among the nonempty open subsets of \(P(9)\), exactly eleven are contractible. Exactly two of those eleven are maximal under inclusion:
\[
U_g=\{c_0,c_1,c_2,p,q,g\}
\]
and
\[
V=P(9)\setminus\{g\}=\{c_0,c_1,c_2,p,q,y,h,k\}.
\]
Every contractible open subset is contained in \(U_g\) or in \(V\), and \(U_g\cup V=P(9)\). Consequently \(\{U_g,V\}\) is the unique unordered two-member cover of \(P(9)\) by contractible open subspaces. In the reduced convention of Fernández-Ternero--Macías-Virgós--Vilches, \(\operatorname{gcat}(P(9))=1\); equivalently, in the unreduced convention the value is \(2\).

## Assumptions and scope
The specialization order is chosen so that the minimal open neighbourhood of \(x\) is \(U_x=\{z:z\le x\}\); hence open subsets are lower sets. Contractible means contractible as a finite topological space, not merely weakly contractible. The statement concerns the displayed labelled representative \(P(9)\); no claim is made here about its order dual or about all nine-point spaces.

The cited classification establishes that the displayed type is weakly contractible but noncontractible. The noncontractibility needed for the category lower bound is also checked directly here: the displayed poset has more than one point and no beat point.

## Proof
For a finite \(T_0\)-space, a point is an up beat point when its strict upper set has a minimum and a down beat point when its strict lower set has a maximum. Deleting a beat point is a strong deformation retract, and a finite \(T_0\)-space is contractible exactly when successive beat-point deletions reduce it to a singleton.

There are only \(2^9=512\) subsets of \(P(9)\). Testing the lower-set condition against the transitive closure of the thirteen displayed cover relations leaves exactly twenty-seven open subsets, including the empty set. For every nonempty open subset, the verifier recursively tries every available beat-point deletion and records a successful reduction exactly when one reaches a singleton. This yields exactly the following eleven contractible opens:
\[
\{c_0\},\ \{c_1\},\ \{c_2\},\ \{c_0,c_1,p\},\ \{c_1,c_2,q\},
\]
\[
\{c_0,c_1,c_2,p,q\},\ \{c_0,c_1,c_2,y\},\ U_g,
\]
\[
\{c_0,c_1,c_2,p,y,h\},\ \{c_0,c_1,c_2,q,y,k\},\ V.
\]
Inclusion comparison among these eleven sets has exactly two maximal elements, namely \(U_g\) and \(V\). Their union is all of \(P(9)\). Every other contractible open is therefore contained in at least one of these two.

Any cover by two contractible open subsets can be enlarged, without losing contractibility, only when the enlarged sets remain among the eleven sets listed above. More directly, exhaustive comparison of all unordered pairs from the eleven contractible opens finds exactly one pair whose union is \(P(9)\), namely \(\{U_g,V\}\). Thus this cover is unique.

Finally, \(P(9)\) itself has no beat point: each minimal point has at least two minimal elements in its strict upper set, each maximal point has at least two maximal elements in its strict lower set, and each middle point has at least two relevant neighbours on both sides. Hence \(P(9)\) is not contractible. A one-member contractible-open cover is therefore impossible, while the displayed two-member cover exists. This proves the stated geometric-category value in either normalization.

## Verification
The standalone file `verify.py` reconstructs the transitive order from the thirteen cover relations, enumerates all \(512\) subsets, checks the lower-set condition, recursively validates beat-point reductions, determines inclusion-maximal contractible opens, and tests all unordered pairs of contractible opens for covering. Its expected terminal line is:

`VERIFY_OK opens=27 contractible_nonempty=11 maximal=2 covering_pairs=1 maximal=c0,c1,c2,p,q,g;c0,c1,c2,p,q,y,h,k full_has_no_beat=true`

The computation is exhaustive over a finite set. It is not being used as evidence for an infinite statement.

## Relationship to prior work
Fernández-Ternero, Macías-Virgós, and Vilches introduced the reduced finite-space geometric category used here and related it to strong homotopy methods. Cianci and Ottina classified the minimum weakly contractible noncontractible finite spaces, giving the nine-point type from which \(P(9)\) is taken. Cárdenas, Flores, Quintero, and Villar-Liñán later developed algorithms for geometric category and related covering invariants, but their full text does not treat the Cianci--Ottina nine-point space. Mosquera-Lois and Tanaka give a self-contained description of \(P(9)\), prove that \(g\) is an essential weak point, and use \(P(9)\) as a base for ordinary, stable, and weak LS-category constructions; their paper does not compute geometric category or classify contractible open covers of \(P(9)\).

The new point here is the complete contractible-open census at \(P(9)\): there are eleven such opens, precisely two are inclusion-maximal, and those two give the unique two-set geometric cover. The existence of the cover follows easily from known facts about \(g\); its uniqueness and maximal-open classification do not.

## Limitations
The result is a finite, object-specific classification. It does not classify geometric covers of the order-dual space, ten-point weakly contractible examples, or arbitrary weakly contractible finite spaces. A literature search cannot prove absolute novelty; the originality assessment rests on statement-level comparison with the most directly relevant full texts located and on explicit residual-risk disclosure in `AUDIT.json`.

## References
1. D. Fernández-Ternero, E. Macías-Virgós, J. A. Vilches, *Lusternik--Schnirelmann category of simplicial complexes and finite spaces*, arXiv:1501.07540v1, first public 2015-01-29; Topology Appl. 194 (2015), 37--50.
2. N. Cianci, M. Ottina, *Smallest homotopically trivial non-contractible spaces*, arXiv:1608.05307v1, first public 2016-08-18; later published as *Smallest weakly contractible non-contractible topological spaces*, Proc. Edinburgh Math. Soc. 63 (2020), 263--274.
3. M. Cárdenas, R. Flores, A. Quintero, M. T. Villar-Liñán, *Covering-based numbers related to the LS-category of finite spaces*, arXiv:2209.14739v1, first public 2022-09-29; Rev. Unión Mat. Argentina 68 (2025), 205--229.
4. D. Mosquera-Lois, K. Tanaka, *Weak, stable, and ordinary Lusternik--Schnirelmann category of finite spaces*, arXiv:2609.39615v1, first public 2026-09-30.
