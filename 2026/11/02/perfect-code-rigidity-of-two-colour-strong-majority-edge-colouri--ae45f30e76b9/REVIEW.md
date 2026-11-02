# Self-review

## Correctness: PASS

For a cubic edge \(uv\), exactly four other edges are adjacent. With two named colours, the strong-majority condition forces a two-versus-two split. If \(a_v\) denotes incident red degree, a red edge implies \(a_u+a_v=4\) and a blue edge implies \(a_u+a_v=2\). The allowed endpoint pairs disconnect the profiles into \(\{1,3\}\) and \(\{0,2\}\); connectedness forces one family, and its monochromatic-degree-three centres form exactly one efficient dominating set. Conversely the red-on-code-star construction makes a two-versus-two split around both kinds of edges. These arguments yield an exact two-to-one correspondence, not merely a necessary condition. Counting closed neighbourhoods establishes divisibility by four. The order-power-of-two classification accurately applies Knor–Potočnik's published Theorem 1.2 and the explicit three-colouring of even-cycle Möbius ladders. Their Lemma 2.2 and its forced propagation justify exactly four efficient codes on each feasible Möbius ladder. Direct finite checks of the untransformed definitions are independently replayable using `verify.py`. Scientific risk: the known 2012 classification is imported as a cited theorem rather than reproved.

## Originality: PASS, historically qualified

The full relevant treatment of the strong-majority edge invariant in arXiv:2605.23828 does not give the cubic two-colour perfect-code correspondence. The treatment in arXiv:2608.04122 concerns few-colour bounds, primarily at minimum degree five or higher, and does not cover the result. The 2012 paper proves efficient-domination statements, but predates the 2026 edge-colouring notion and does not derive the new edge-colour translation. A previously accessible exact result for circular prisms is a strict family-specific consequence and is **not** represented as newly established. Related published mathematical records treating strong-majority colourings of complete graphs and generalized bipartite degree thresholds do not imply the universal cubic correspondence. Searches of aliases, exact graph families, and source sections found no covering statement. Risk: historical priority cannot be conclusively ruled out from non-indexed manuscripts or alternate terminology.

## Mathematical value: PASS

The result gives a necessary-and-sufficient structural criterion and an exact solution-count bijection for the *entire* connected cubic family, translating a local edge-neighbour colouring condition into classical exact closed-neighbourhood packing. It immediately determines a new edge-colouring index for every connected cubic vertex-transitive graph of power-of-two order using a nontrivial classification theorem, and it yields the full Möbius-ladder phase transition together with an exact optimum-colouring count. This is not a routine variant of a small enumeration, nor a re-claim of the known efficient-domination classifications. The use of the prior prism special case is explicitly limited to an overlap comparison.

## Scope and residual risks

No conclusions are made about noncubic graphs, arbitrary non-perfect-code cubic graphs with index three versus four, or counting three-colour assignments. Independent assessment is not performed; broader literature priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
