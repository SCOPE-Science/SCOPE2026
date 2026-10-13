# Sylvester modal types and a sharp logarithmic bisimulation-compression law for complete trees

## Finding

**Theorem.** Fix integers \(q\ge2\) and \(a\ge2\). Let \(T_{q,h}\) be the outward-directed complete \(q\)-ary tree of height \(h\), with every vertex independently assigned one of \(a\) observable colors. Regard it as a finite Kripke model with the parent-to-child relation (not its reflexive/transitive closure). Let \(B_{q,a}(h)\) be the maximum, over all colorings, of the number of states in its greatest color-respecting bisimulation quotient. With
\[
N_h=\frac{q^{h+1}-1}{q-1},
\]
there exist constants \(0<c_{q,a}\le C_{q,a}<\infty\) and \(h_0\) depending only on \(q,a\) such that, for all \(h\ge h_0\),
\[
\boxed{c_{q,a}\frac{N_h}{\log N_h}\le B_{q,a}(h)\le C_{q,a}\frac{N_h}{\log N_h}.}
\]
Thus **even the least compressible coloring** of a complete regular tree admits a logarithmic-factor reduction by ordinary modal bisimulation, and this bound is optimal. In particular, the tight rate holds with only one propositional bit (\(a=2\)).

More precisely, the number \(t_k=t_k(q,a)\) of pairwise inequivalent rooted, color-preserving modal-bisimulation types realized on complete \(q\)-ary trees of height \(k\) satisfies the exact recurrence
\[
\boxed{t_0=a,\qquad t_{k+1}=a\sum_{j=1}^{\min(q,t_k)}\binom{t_k}{j}.}
\]
Every coloring satisfies the finite upper bound
\[
\boxed{|T_{q,h}/{\sim}|\le \sum_{k=0}^{h}\min\{q^{h-k},t_k\}.}
\]
For \(q=a=2\), the recurrence specializes to \(t_{k+1}=t_k(t_k+1)\), yielding \(2,6,42,1806,3263442,\ldots\); the numbers \(t_k+1\) are the classical Sylvester sequence after its initial term. This numerical sequence itself is not claimed as new.

## Assumptions and scope

The vertex set is the words over an alphabet of size \(q\) of lengths at most \(h\); the only accessibility edges join each word to its \(q\) one-letter extensions. The propositional valuation supplies one of \(a\) mutually exclusive and exhaustive vertex colors; for \(a=2\), a single atomic proposition suffices. Bisimulation uses color agreement and the standard forth-and-back condition on outgoing edges. The quotient contains one state per equivalence class of the **greatest** bisimulation on all vertices, not just root types, and is not a quotient by rooted-tree isomorphism or by graded bisimulation. Constants in \(\Theta\) depend on fixed \(q,a\); no uniform assertion for growing \(q\) or \(a\) is made.

The boundary assumptions are necessary. If \(a=1\), all vertices with the same remaining height are bisimilar, and the quotient has exactly \(h+1\) states. If \(q=1\), all vertex heights occur only once and its quotient also has exactly \(h+1=N_h\) states, for any \(a\ge1\).

## Proof

**1. Canonical types and cross-height separation.** Assign to each colored vertex the inductive descriptor \((\text{its color},S)\), where \(S\) is the **set**, not the multiset, of descriptors of its immediate children; a leaf has \(S=\varnothing\). Inductively, two vertices of the same remaining height are bisimilar exactly when their descriptors agree: equal descriptors give a color-respecting forth-and-back relation, and the converse follows because every child of either root must be matched by a bisimilar child of the other. Vertices with different remaining heights cannot be bisimilar, because a vertex with remaining height \(k\) satisfies the basic modal formula \(\Diamond^k\top\) but not \(\Diamond^{k+1}\top\). The quotient size is therefore the sum of the numbers of distinct descriptors at each remaining height.

**2. Exact rooted-type census.** A leaf has \(a\) possible types. At an internal root, choose its color (\(a\) options) and the nonempty set \(S\) of child types. Since there are exactly \(q\) children, \(1\le|S|\le\min(q,t_k)\); conversely, every such set is realized by assigning each member to one child and filling the remaining children with arbitrary members of \(S\). This proves the displayed recurrence and the finite level-by-level bound.

**3. Exponential-in-\(q^k\) type growth.** There are \(N_k\) colored vertices, so \(t_k\le a^{N_k}\le \exp(Cq^k)\), where \(C=(q/(q-1))\log a\). Conversely, \(t_{k+1}\ge a t_k\), hence \(t_k\) diverges. Choose \(m\) with \(t_m\ge2q\) and \(\log t_m>D=q\log(2q)/(q-1)\). For \(t_k\ge2q\),
\[
\binom{t_k}{q}\ge \left(\frac{t_k}{2q}\right)^q,
\]
so \(\log t_{k+1}-D\ge q(\log t_k-D)\). Induction gives \(\log t_k\ge c q^k\) for all \(k\ge m\), with \(c=(\log t_m-D)/q^m>0\). Decreasing \(c\) if needed handles the finitely many earlier indices. Thus, for constants \(c,C>0\) depending on fixed \(q,a\),
\[
\exp(cq^k)\le t_k\le\exp(Cq^k)\qquad(k\ge0).
\]

**4. Universal upper bound.** The level whose remaining height is \(k\) has \(q^{h-k}\) vertices, hence contributes at most \(\min(q^{h-k},t_k)\) classes. Choose \(\delta=(\log q)/(4C)\) and \(k_0=\lfloor\log_q(\delta h)\rfloor\), for sufficiently large \(h\). At all levels \(0\le k\le k_0\), the entire sum is at most \((k_0+1)q^{h/4}=o(q^h/h)\). For larger \(k\), the geometric sum satisfies
\[
\sum_{k=k_0+1}^{h}q^{h-k}=O_{q,a}(q^h/h),
\]
because \(q^{k_0}\) is within a fixed factor of \(\delta h\). This proves the upper bound for every coloring.

**5. Matching realizable lower bound.** Choose \(\beta=2\log q/c\) and \(k_1=\lceil\log_q(\beta h)\rceil\). For sufficiently large \(h\), \(0\le k_1\le h\) and
\[
t_{k_1}\ge\exp(cq^{k_1})\ge q^{2h}\ge q^{h-k_1}.
\]
At the level of depth \(h-k_1\), there are \(q^{h-k_1}\) **disjoint** complete subtrees of height \(k_1\). Since at least that many inequivalent rooted types exist, color these subtrees independently with pairwise distinct types; assign arbitrary colors above the level. The corresponding roots remain pairwise non-bisimilar in the whole tree because all their successors lie inside the chosen subtrees. Consequently
\[
B_{q,a}(h)\ge q^{h-k_1}\ge\frac{q^h}{q\beta h}.
\]
Together with Step 4 and \(N_h=\Theta_q(q^h)\), \(\log N_h=\Theta_q(h)\), this proves the theorem.

**6. Binary specialization and boundaries.** At \(q=a=2\), Step 2 yields \(t_{k+1}=2(t_k+\binom{t_k}{2})=t_k(t_k+1)\). For one color, the descriptor depends only on remaining height, and the singleton-child case has one vertex per height, proving both boundary statements.

## Verification

Run `python verify_modal_compression.py` using Python 3.9 or newer, with no third-party packages. The program exhaustively enumerates 43,276 colored complete trees over five small parameter triples, computes recursive rooted descriptors, and **independently** performs iterative greatest-bisimulation partition refinement on each valuation. It checks equality of the resulting partitions, the exact type recurrence, the separation of different heights, and the finite level bound. For \((q,a,h)=(2,2,3)\), all 32,768 valuations produce 1,806 distinct root types and a maximum nine-state quotient. For \((3,2,2)\), all 8,192 valuations produce 82 rooted types and maximum quotient size six. The program also checks the binary Sylvester recurrence through five steps.

These are finite tests only; the asymptotic statement follows from Steps 3–5, not from extrapolating the tests.

## Relationship to prior work

Figueira and Goren-Roig (2023) establish modal-resource bisimulation semantics, tree unravelling and a correspondence between path-predicate modal logic and basic modal logic. They provide the logical framework, not the displayed finite palette-dependent extremal quotient theorem. Ganardi, Hucke, Jeż, Lohrey and Noeth (2014/2017) prove an \(O(N/\log N)\) upper bound for the *ordered-subtree minimal DAG* of balanced labeled binary trees. That earlier result already supplies an upper bound in the binary case, because ordinary modal bisimulation can identify more vertices than ordered-subtree isomorphism. However, a lower bound for the ordered DAG does **not** imply one for the coarser ordinary-bisimulation quotient. Here the matching lower bound holds on the much more constrained family of complete regular trees with fixed finite color alphabet. Known modal type induction, DAG-compression bounds, and the Sylvester sequence are not individually claimed as new.

## Limitations

The exact maximal quotient size at every \(h\) is not asserted; only the exact count of available rooted modal types and the sharp asymptotic extremal order are proved. The constants are non-effective in the statement but constructive from the proof. No result is claimed for varying branching arity or palette size with height, graded modalities (which count child multiplicities), or modal frames with reflexive/transitive closure edges. A different publication could already contain this special-case lower bound under automata or tree-compression terminology; the cited accessible material and targeted searches did not identify it. Independent mathematical review has not been performed.

## References

1. S. Figueira and G. Goren-Roig, *Modal Logic with Relations over Paths: a Theoretical Development through Comonadic Semantics*, arXiv:2307.09679, first submitted 18 July 2023; especially Sections 2.1, 3.1, and 4.3. https://arxiv.org/abs/2307.09679
2. M. Ganardi, D. Hucke, A. Jeż, M. Lohrey, and E. Noeth, *Constructing Small Tree Grammars and Small Circuits for Formulas*, arXiv:1407.4286, 2014; Journal of Computer and System Sciences, DOI 10.1016/j.jcss.2016.12.007, especially Section 5.3, Theorem 10. https://arxiv.org/abs/1407.4286
3. J. Jacobs and T. Wißmann, *Fast Coalgebraic Bisimilarity Minimization*, Proceedings of the ACM on Programming Languages 7 (POPL), Article 52 (2023), DOI 10.1145/3571245. https://doi.org/10.1145/3571245
