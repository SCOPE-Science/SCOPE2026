# The first minimal-domination cycle gap: complete five-query traces and a vertex-transitive amplification

## Finding

Let \(C_n\) denote the simple cycle with vertex set \(\{0,\ldots,n-1\}\), for \(n\ge3\), and let \(\mathcal D_n\) be the family of **inclusion-minimal dominating vertex sets**. Each concept is its vertex-membership vector; a query at vertex \(v\) returns one exactly when \(v\) belongs to the unknown minimal dominating set. Both VC dimension and Littlestone dimension use this same binary query domain.

The first cycle for which the two dimensions differ is \(C_{11}\):
\[
|\mathcal D_{11}|=44,\qquad
\operatorname{VCdim}(\mathcal D_{11})=4,\qquad
\operatorname{Ldim}(\mathcal D_{11})=5.
\]
For every \(3\le n\le10\), the dimensions agree; the exact values for increasing \(n\) are \(1,2,2,2,3,3,4,4\). A complete enumeration of all \(\binom{11}{5}=462\) five-coordinate query supports shows that their maximum number of distinct traces is \(29\), attained by exactly \(11\) supports. The full spectrum, displayed as `(number of traces : number of supports)`, is

| Traces | Supports | Traces | Supports | Traces | Supports |
|---:|---:|---:|---:|---:|---:|
| 11 | 11 | 14 | 22 | 15 | 44 |
| 16 | 11 | 18 | 11 | 19 | 88 |
| 20 | 33 | 21 | 77 | 22 | 44 |
| 23 | 11 | 24 | 66 | 25 | 33 |
| 29 | 11 | | | | |

The cycle \(C_{11}\) also exhibits a distinction between **two** natural classes on exactly the same query domain: its \(22\) inclusion-maximal independent sets have VC and Littlestone dimensions both equal to \(4\), while enlarging the class to all \(44\) minimal dominating sets preserves the VC dimension but raises the Littlestone dimension by one.

For every integer \(m\ge1\), let \(G_m\) be the disjoint union of \(m\) copies of \(C_{11}\). This is a vertex-transitive, two-regular graph and its minimal-dominating-set membership class satisfies
\[
\operatorname{VCdim}(\mathcal D(G_m))=4m,
\qquad
\operatorname{Ldim}(\mathcal D(G_m))=5m.
\]
In particular, the adaptive-minus-static gap is unbounded in this natural graph class.

## Assumptions and scope

All graphs are finite, simple and undirected. A set \(D\subseteq V(G)\) dominates \(G\) if every vertex lies in \(D\) or has a neighbor in \(D\). It is *inclusion-minimal* if deleting any one element destroys domination. This is not the same as being a minimum-cardinality dominating set, and is not the same as being an inclusion-maximal independent set. Every maximal independent set is minimal dominating, but the reverse can fail.

A query support \(S\subseteq V(G)\) is VC-shattered when each of its \(2^{|S|}\) membership patterns is realized by some concept. A complete binary decision tree of depth \(d\), with internal nodes labeled by query vertices and with every root-to-leaf membership pattern realizable, witnesses Littlestone dimension at least \(d\). The exact finite claims here concern \(3\le n\le11\); no general formula for all longer connected cycles is asserted.

## Proof

**1. Exhaustive concept enumeration is complete.** For each cycle size \(n\), enumerate every one of the \(2^n\) vertex subsets. Let \(N[v]=\{v-1,v,v+1\}\), indices interpreted modulo \(n\). A chosen subset \(D\) is dominating precisely when \(\bigcup_{v\in D}N[v]=V\). It is inclusion-minimal precisely when each \(v\in D\) has a *private vertex* \(w\in N[v]\) satisfying \(N[w]\cap D=\{v\}\): such a vertex ceases to be dominated on deleting \(v\), and conversely minimality forces such a witness. The supplied `verify_cycle11.py` implements this criterion, while `independent_check.py` independently tests domination and minimality by explicitly removing each selected vertex. Both methods yield exactly \(44\) concepts for \(C_{11}\), as well as the displayed finite small-cycle counts.

**2. Static dimension.** The support \(S=\{0,2,4,6\}\) is shattered: `cycle11_certificate.json` lists one of the \(44\) full vertex masks for each of its \(16\) membership patterns, and the checker verifies every projection. For the upper bound, the checker examines **each** of the \(462\) five-element supports and each of the \(44\) concepts, constructs the set of induced five-bit traces, and counts its size. The complete trace histogram above is obtained, with maximum \(29<32\); thus no five-element support is shattered. Any shattered set of more than five coordinates would contain a shattered five-coordinate subset. Therefore the VC dimension is exactly four. The checker likewise enumerates supports for \(3\le n\le10\) to determine their exact VC dimensions.

**3. Adaptive dimension.** The certificate supplies a complete depth-five decision tree containing exactly \(31\) labeled internal nodes and \(32\) terminal witnesses. Each terminal witness is one of the enumerated minimal dominating sets and satisfies every membership/nonmembership requirement along its path. Terminal witnesses are pairwise distinct. The checker replays every path. Hence the Littlestone dimension is at least five. Conversely every shattered depth-\(d\) complete binary tree needs \(2^d\) distinct hypotheses, so \(|\mathcal D_{11}|=44<64\) excludes depth six. Thus the dimension is five. For \(3\le n\le10\), the enumerated VC dimension equals \(\lfloor\log_2|\mathcal D_n|\rfloor\); since VC dimension never exceeds Littlestone dimension, and the latter never exceeds that hypothesis-count bound, the two dimensions agree there. An independent complete version-space recurrence verifies the same finite adaptive values.

**4. The maximal-independent-set contrast.** The same enumeration filters the \(44\) minimal dominating sets to the \(22\) concepts with no adjacent selected vertices. Their VC dimension is four by exhaustive support check, and their Littlestone dimension lies between four and \(\lfloor\log_2 22\rfloor=4\). Thus adding the non-independent minimal dominating sets has no effect on the static dimension but raises the adaptive one.

**5. Products and graph symmetry.** Every minimal dominating set of a disjoint union is the union of exactly one minimal dominating set from each component. Its binary concept class is therefore the Cartesian product of the component classes on disjoint query domains. VC dimension is additive: a support in the union is shattered if and only if its projection is shattered in each component. Littlestone dimension is additive too. For the lower bound, attach a complete shattered decision tree for the second factor below each leaf of a complete shattered tree for the first; iterate. For the upper bound, the optimal realizable mistake-bound characterization of Littlestone dimension gives independent predictors on each component, and the combined predictor makes at most the sum of their respective mistake bounds. This characterization follows directly by induction on the version-space splitting recurrence: predict the label whose remaining version space has greatest Littlestone dimension, so every mistaken prediction lowers that dimension. Applying additivity to the depth-five and VC-four cycle base gives the two displayed product formulas. The automorphism group of a disjoint union of isomorphic cycles permutes components and rotates each component, so \(G_m\) is vertex-transitive.

## Verification

The self-contained files `cycle11_certificate.json`, `verify_cycle11.py` and `independent_check.py` are included alongside this document. Run both Python programs from their containing directory using a standard Python 3.10-or-newer interpreter. Neither program downloads data nor depends on nonstandard packages. The first verifies every cycle through eleven vertices, the full five-query histogram, the four-query static witness, the complete depth-five adaptive certificate, and the maximal-independent-set comparison. The second enumerates minimal dominating sets by a different test, calculates exact Littlestone dimensions from the full version-space recurrence, independently recomputes all five-query trace counts, and replays the witness tree. Successful execution prints `ALL_CYCLE11_MINIMAL_DOMINATION_CHECKS_PASS` and `ALL_INDEPENDENT_CYCLE11_CHECKS_PASS`, respectively.

The finite statements are based on *exhaustive*, not sampled, computations. The extension to arbitrary disjoint-union multiplicity is proved by the product argument and does not rely on extrapolating finite experiments.

## Relationship to prior work

Bhaskar's 2017 *Thicket Density* develops the finite tree-shattering viewpoint and connects it to Shelah's model-theoretic ranks [1]. Malliaris and Moran's 2021 *Agnostic Online Learning and Excellent Sets* develops related adaptive-learning and stability theory [2]. These give the general meaning of Littlestone dimension but do not state the cycle/minimal-domination values here. Couturier, Heggernes, van 't Hof and Kratsch [3] study the enumeration of minimal dominating sets and explicitly characterize inclusion-minimality using private neighbors; their classification and algorithms concern other graph classes and do not calculate the present VC/Littlestone invariants. Manurangsi [4] studies general hardness of approximating learning dimensions, not these exact small-cycle values.

Prior exact calculations for vertex-membership classes of minimal dominating sets on paths and of maximal independent sets on cycles provide nearby comparisons but do not imply the present minimal-domination cycle conclusion: changing a path to a cycle changes domination and minimality globally, while requiring independence removes half the concepts for the eleven-cycle. The present result additionally gives the complete five-query trace distribution and a two-regular vertex-transitive product family. No claim of absolute historical priority is made.

## Limitations

The first-gap assertion is restricted to simple connected cycles of orders three through eleven. The general Littlestone dimension or VC dimension of minimal dominating sets on arbitrary longer connected cycles remains open here; the displayed product identities apply to disjoint unions of eleven-cycles only. Exhaustive computational checking establishes finite facts, not formulas for untested cycle orders. The work has not undergone an independent mathematical audit. Related results may exist under the names `domination hypergraph`, `thicket dimension`, `Shelah 2-rank`, or `minimal transversal family`; these naming variations remain a historical-priority risk.

## References

[1] Siddharth Bhaskar, *Thicket Density*, 2017, arXiv:1702.03956, https://arxiv.org/abs/1702.03956 (first public version 2017-02-13).

[2] Maryanthe Malliaris and Shay Moran, *Agnostic Online Learning and Excellent Sets*, 2021, arXiv:2108.05569, https://arxiv.org/abs/2108.05569 (first public version 2021-08-12).

[3] Jean-François Couturier, Pinar Heggernes, Pim van 't Hof and Dieter Kratsch, *Minimal Dominating Sets in Graph Classes: Combinatorial Bounds and Enumeration*, Theoretical Computer Science 487 (2013), 82–94; freely readable preprint https://pimvanthof.github.io/mds_journal.pdf.

[4] Pasin Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, ITCS 2023, https://doi.org/10.4230/LIPIcs.ITCS.2023.85.
