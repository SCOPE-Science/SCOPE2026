# Exact EF1–EFX welfare dichotomy for two complementary perfect matchings

## Finding

Let \\(T\\ge 1\\) be any integer. For two agents whose complementary bundles are disjoint pairs covering the same \\(2T\\) goods, there is an exact dichotomy: the optimal utilitarian welfare of any **complete EF1 allocation** equals that of any **complete EFX allocation** and is either \\(T\\) or \\(T-1\\). The higher value is attainable if and only if the alternating-cycle half-lengths of the agents' pair matchings admit a nearly equal subset partition. The unrestricted optimum is always \\(T\\). Both the exact decision and a witnessing allocation are constructible in \\(O(T^2)\\) time. The all-scale classification and construction are the contribution; the four-good lower-bound example was previously published.

Explicitly, if the alternating components have half-lengths \\(\\ell_1,\\ldots,\\ell_r\\), then the shared EF1 and EFX optimum is

\\[
 W^*_{\\mathrm{EF1}}=W^*_{\\mathrm{EFX}}=
 \\begin{cases}
 T,&\\exists J\\subseteq[r],\\ \\left|T-2\\sum_{j\\in J}\\ell_j\\right|\\le1,\\\\
 T-1,&\\text{otherwise.}
 \\end{cases}
\\]

The exact maximum additive efficiency loss imposed by EFX is one unit and the minimum possible welfare ratio is \\(1/2\\), achieved by the alternating four-good example from Proposition 2.1 of Pyne et al. This relative bound is not claimed as a new lower-bound construction.

## Assumptions and scope

There are exactly two agents and a finite set \\(G\\) of \\(2T\\) distinguishable goods. For each agent \\(i\\in\\{1,2\\}\\), \\(M_i\\) is a **perfect matching** of \\(G\\): a partition into unordered disjoint pairs. For all \\(S\\subseteq G\\), define \\(v_i(S)=\\#\\{e\\in M_i:e\\subseteq S\\}\\). This is a special case of binary SPOC with complement size two and free-matroid rank on completed bundles, with neither empty complementarities nor unpaired goods. Valuations need not be additive across individual goods.

A complete allocation is an ordered partition \\((A_1,A_2)\\) of \\(G\\). Its utilitarian welfare is \\(v_1(A_1)+v_2(A_2)\\). It is EF1 if for both distinct agents \\(i,j\\), either there is no envy, or some \\(g\\in A_j\\) makes \\(v_i(A_i)\\ge v_i(A_j\\setminus\\{g\\})\\). It is EFX if the displayed inequality holds **for every** \\(g\\in A_j\\) (this strengthens the usual condition restricted to positive marginal goods). For an empty other bundle, the condition is vacuous.

The edge-colored multigraph formed by the red edges \\(M_1\\) and blue edges \\(M_2\\) is two-regular with alternating cycles, including a doubled two-edge cycle for every edge common to both matchings. A component of \\(2\\ell_j\\) vertices contains \\(\\ell_j\\) edges of each color. The half-lengths are positive integers with \\(\\sum_j\\ell_j=T\\).

## Proof

**1. Unrestricted optimum.** Every completed pair consumed by a recipient needs two goods disjoint from goods in all other recipient-completed pairs, so for every complete allocation the welfare is at most \\(T\\). Giving all goods to agent 1 attains exactly \\(T\\).

**2. Structure of equality.** An allocation attaining \\(T\\) consists entirely of disjoint pairs valued by their recipients and uses every good. Thus it selects a perfect matching from the union of red and blue matchings and assigns each selected red pair to agent 1 and selected blue pair to agent 2 (common pairs may be assigned either way). An alternating cycle has exactly two ways to cover all its vertices by its own red/blue edges: all red or all blue. Consequently the recipient of **every** good in a component must be the same, and assigning that component to agent 1 contributes \\(\\ell_j\\) utility to agent 1; assigning it to agent 2 contributes \\(\\ell_j\\) utility to agent 2.

Suppose total utilities are \\(R\\) and \\(B\\) respectively, where \\(R+B=T\\). An agent's valuation of the other agent's complete-component union equals the *other* agent's utility because the other-colored pairs are also completely contained componentwise. Removing **any single good** from a nonempty such bundle destroys exactly one pair of the evaluating agent. Therefore in a full-welfare allocation, EF1 and EFX are both equivalent to \\(R\\ge B-1\\) and \\(B\\ge R-1\\), equivalently \\(\\lvert R-B\\rvert\\le1\\). Since \\(R=\\sum_{j\\in J}\\ell_j\\), equality in fair welfare holds precisely for the subset-partition criterion. In that case the complete whole-component assignment itself is EFX.

**3. Constructive one-unit loss otherwise.** If there is no nearly equal subset partition, at least one component has \\(L:=\\ell_h\\ge2\\): otherwise all components have length one and can be split almost equally. Select a largest component \\(h\\) of length \\(L\\) and greedily assign every other component as a whole to the currently lower-utility agent (arbitrary tie breaking). Its contributed pair count is at most \\(L\\). Starting with zero difference, each such assignment leaves a difference \\(d\\) with \\(\\lvert d\\rvert\\le L\\); indeed adding or subtracting a positive integer no greater than \\(L\\) toward zero preserves the bound.

On the reserved alternating cycle, cyclically list its \\(2L\\) vertices as \\(0,1,\\ldots,2L-1\\) so that agent 1's red pairs are \\((2a,2a+1)\\) for \\(0\\le a<L\\), and agent 2's blue pairs are \\((2a+1,2a+2\\pmod{2L})\\). Choose nonnegative integers \\(x,y\\) satisfying \\(x+y=L-1\\) and \\(\\lvert d+x-y\\rvert\\le1\\). Such integers always exist because \\(x-y\\) ranges by steps of two from \\(-(L-1)\\) to \\(L-1\\) and \\(\\lvert d\\rvert\\le L\\). Assign the first \\(x\\) red pairs, indexed \\(0,\\ldots,x-1\\), to agent 1, and the blue pairs indexed \\(x,\\ldots,L-2\\) to agent 2. These pairs are mutually disjoint, cover \\(2(L-1)\\) goods, and leave exactly two goods unallocated. Combining with the other components gives \\(R+B=T-1\\) completed recipient pairs and \\(\\lvert R-B\\rvert\\le1\\).

Give both remaining goods to the recipient with *smaller* provisional completed-pair count (ties arbitrary). Relabel the larger-count recipient as \\(H\\) and the smaller as \\(D\\), with \\(R\\ge B\\) and \\(R-B\\le1\\) now denoting their provisional pair counts. The final high-count bundle has \\(2R\\) goods and own value at least \\(R\\). The final low-count bundle has \\(2B+2\\) goods and own value at least \\(B\\). For a *different* agent evaluating the high-count bundle with any one good removed, its value is at most \\(\\lfloor(2R-1)/2\\rfloor=R-1\\le B\\); similarly the value of the low-count bundle with any good removed is at most \\(\\lfloor(2B+1)/2\\rfloor=B\\le R\\). Both EFX inequalities hold for **every** good of the envied bundle. Additional complete pairs formed by the last two goods can only improve own welfare and preserve these inequalities. Hence the allocation is complete and EFX with welfare at least \\(T-1\\). Step 2 rules out welfare \\(T\\) when the criterion fails, so its welfare must equal \\(T-1\\). This also proves the equality of the best EF1 and best EFX welfare, since every EFX allocation is EF1.

**4. Optimal algorithm and sharp boundary.** Decompose the two matchings into alternating cycles in linear time. Standard subset-sum dynamic programming on the half-lengths decides the nearly equal partition and reconstructs its components in \\(O(T^2)\\) time. If it exists, use the all-component EFX assignment. Otherwise choose a largest cycle, perform the greedy component assignment and the partial-cycle construction above; searching \\(x\\) requires at most \\(O(T)\\) steps.

For the four goods \\(G=\\{0,1,2,3\\}\\), choose \\(M_1=\\{\\{0,1\\},\\{2,3\\}\\}\\) and \\(M_2=\\{\\{1,2\\},\\{3,0\\}\\}\\). Their only alternating component has half-length two, so no balanced subset exists and maximum fair welfare is \\(1\\), while unrestricted welfare is \\(2\\). This is the prior-literature lower-bound instance, included solely to demonstrate sharpness, not as an original counterexample.

## Verification

The standalone `check_spoc_cycles.py` enumerates **all ordered pairs** of perfect matchings on \\(2,4,6,8\\) labeled goods (respectively \\(1,9,225,11025\\) cases). For each matching pair it independently enumerates **all complete two-agent allocations**, evaluates both agents' pair-completion valuations, and computes the exact EFX-constrained optimum. It then compares against the alternating-component formula and independently verifies the supplied constructive allocation's complete coverage, welfare and every single-good EFX inequality. Every one of the \\(11260\\) instances passed. The output `spoc_cycles_check_output.txt` preserves domain counts and cycle-profile multiplicities. Run with `python3 check_spoc_cycles.py`; only the Python standard library is used. These finite checks support but do not prove the arbitrary-size theorem, which is proved above.

## Relationship to prior work

Pyne, Viswanathan, Yang and Zick (arXiv:2610.15801) introduce binary preferences over complementary bundles and prove a complete EFX welfare approximation for purely complementary SPOC valuations (Theorem 4.6). Their Proposition 2.1 contains **exactly** the four-good alternating perfect-pair obstruction recorded in Step 4, and their Theorem 4.7 gives a different family with small fair welfare under more general complement lists and unrestricted agent counts. None of those statements provides the all-size alternating-cycle subset-balance **if-and-only-if** optimum or a universal at-most-one-unit loss for **two complete matching complement lists**. This last distinction is essential: the known four-good witness and the generic EFX existence guarantee are not independently new results.

Goldberg, Høgh and Hollender (arXiv:2301.10354) study general two-agent EFX computation and its complexity frontier, rather than this perfect-matching exact welfare classification. Mackenzie and Suzuki (arXiv:2607.17811) concern fairness-efficiency compatibility under submodular goods, whereas these item-level pair-completion valuations are generally complementary and not submodular. Publicly discoverable closely ranked mathematical-result abstracts on matchings and allocation were also checked at the statement/implication level; those had other objectives or valuation domains.

## Limitations

The theorem requires two agents, **both** complete lists to be perfect matchings of the *same* even-sized goods universe, and the value of each completed complementary pair to be exactly one without additional cross-pair rank constraints. It does not assert this one-unit loss for incomplete complement lists, arbitrary hyperedges, more agents, or general SPOC matroid rank functions. The welfare conclusion concerns utilitarian sum, not Nash welfare or Pareto optimality. The four-good obstruction is previously known. Search-based originality assessment is subject to unindexed equivalent theorems; independent scientific audit and publication-priority adjudication have not occurred.

## References

1. Soumyajit Pyne, Vignesh Viswanathan, Wenhao Yang, Yair Zick. *Fair Allocation with Dichotomous Preferences over Item Complements*. arXiv:2610.15801, first publicly submitted 2026-10-11. https://arxiv.org/abs/2610.15801 ; https://arxiv.org/html/2610.15801v2 (read Definitions in Section 2, Proposition 2.1, Theorems 4.6–4.7, and appendix).
2. Paul W. Goldberg, Alexandros Høgh, and Alexandros Hollender. *The Frontier of Intractability for EFX with Two Agents*. arXiv:2301.10354. https://arxiv.org/abs/2301.10354 (read introduction and relevant EFX existence/complexity sections).
3. Mackenzie and Suzuki. *When One Good Is Not Enough: On the Compatibility of Fairness and Efficiency under Submodular Valuations*. arXiv:2607.17811. https://arxiv.org/abs/2607.17811 (read introduction and scope/results sections).
