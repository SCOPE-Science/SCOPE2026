# Only the identity retains a noncontractible fixed set on the minimal nine-point example
## Finding
Let \(R\) be the nine-point finite \(T_0\)-space drawn in Figure 1 of Cianci and Ottina. Write its points as \(c_1,c_2,c_3,b_1,b_2,b_3,a_1,a_2,a_3\). Among all 12,575 continuous self-maps \(f:R\to R\), the identity is the only map for which the fixed-point subspace \(\operatorname{Fix}(f)\) is noncontractible. Every nonidentity self-map has a nonempty fixed-point subspace that dismantles by beat-point deletions to a singleton.

The numbers of self-maps with \(|\operatorname{Fix}(f)|=k\) for \(k=1,\ldots,9\) are
\[
3493,\ 4877,\ 2909,\ 1013,\ 234,\ 41,\ 5,\ 2,\ 1.
\]
Exactly 210 distinct fixed subsets occur. The same statements hold for the opposite finite space \(R^{\mathrm{op}}\).
## Assumptions and scope
The specialization order is defined by the thirteen cover relations
\[
\begin{aligned}
&c_1<b_1,\ c_2<b_1,\ c_1<b_2,\ c_2<b_2,\ c_3<b_2,\ c_2<b_3,\ c_3<b_3,\\
&b_1<a_1,\ b_2<a_1,\ b_1<a_2,\ b_3<a_2,\ b_2<a_3,\ b_3<a_3.
\end{aligned}
\]
All comparisons used below are their reflexive-transitive closure. For finite \(T_0\)-spaces, continuous maps are exactly order-preserving maps. Contractibility of a realized fixed set is certified by an explicit dismantling sequence; no claim is made about proper subsets that never arise as fixed sets.
## Proof
The proof is finite and exhaustive. An order-preserving self-map is enumerated by assigning images to the nine points and rejecting an assignment as soon as it violates any already determined order relation. Rechecking every completed assignment against the full transitive order gives 12,575 distinct maps.

For each map \(f\), form the induced subposet on \(\operatorname{Fix}(f)=\{x:f(x)=x\}\). For every fixed subset except the full nine-point set, the attached certificate gives a sequence of deletions. At each step the deleted point is an up-beat point whose strict upper set has a least element, or a down-beat point whose strict lower set has a greatest element. Such a deletion is a strong deformation retract, so a sequence ending in one point proves contractibility. The verifier replays every witness relation against the full order.

There are 210 realized fixed subsets. All 209 proper realized fixed subsets have certified beat-point dismantlings. The full set occurs exactly once: if every point is fixed, the map is the identity. Cianci and Ottina establish that \(R\) itself is homotopically trivial but noncontractible. Hence the identity is exactly the exceptional self-map. Reversing the order preserves the set of monotone self-maps and exchanges up-beat with down-beat points, proving the dual statement for \(R^{\mathrm{op}}\).
## Verification
Run `python3 artifacts/verify.py`. It reconstructs the transitive order from the thirteen covers, independently re-enumerates all order-preserving self-maps, checks uniqueness and the complete fixed-set multiplicity table, and replays every beat-point deletion in `artifacts/fixed_sets.json`. It also checks that the full fixed set belongs only to the identity and that \(R\) itself has no beat point.

The verifier output for the packaged files is:

`VERIFY_OK maps=12575 distinct_fixed_sets=210 sizes=3493,4877,2909,1013,234,41,5,2,1 nonidentity_contractible=12574 dual=invariant`
## Relationship to prior work
Cianci and Ottina identify \(R\) and \(R^{\mathrm{op}}\) as the nine-point homotopically trivial noncontractible finite spaces and note that the same poset already appears in Rival's 1976 fixed-point work. Szymik explains that Rival's example belongs to the finite-poset examples with a selection map, hence has the universal fixed point property. These results guarantee fixed points and place the example in fixed-point theory, but they do not state the topology of every individual fixed-point subspace.

The new statement is stronger in a different direction: it determines all realized fixed-set sizes and proves that every nonidentity fixed set is contractible, while the identity alone retains the noncontractible topology of \(R\). Searches of the cited fixed-point literature and the checked research database did not locate this fixed-set census or its contractibility assertion.
## Limitations
The result concerns this extremal nine-point poset and its order dual; it is not asserted for arbitrary finite spaces with the fixed point property or universal fixed point property. The computation proves an exact finite statement, not an infinite-family theorem. Rival's full 1976 article could not be retrieved in this run after open-access and authorized institutional-access attempts; its known use of the same poset remains the main residual literature risk, although later sources describe its result as a fixed-point-property example rather than a fixed-set-topology classification.
## References
1. Nicolás Cianci and Miguel Ottina, “Smallest homotopically trivial non-contractible spaces,” arXiv:1608.05307v1, 18 August 2016.
2. Markus Szymik, “Homotopies and the universal fixed point property,” arXiv:1210.6496.
3. Ivan Rival, “A fixed point theorem for finite partially ordered sets,” Journal of Combinatorial Theory, Series A 21 (1976), 309–318.
4. Kenneth Baclawski and Anders Björner, “Fixed points in partially ordered sets,” Advances in Mathematics 31 (1979), 263–287.
