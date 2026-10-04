# Review: Exact ternary length-five single-deletion covering number

## Correctness
**PASS.** The claim is stated for the exact finite domain \(\Sigma_3^5\to\Sigma_3^4\). The upper bound is witnessed by 21 explicit codewords generated from seven representatives under cyclic symbol translation. The lower bound is an exact fractional-cover dual certificate: ten symmetry-orbit weights total \(468/23>20\), and exhaustive integer checking over all 243 possible length-five centers proves every deletion ball has weight at most one. Thus every cover has at least 21 codewords. The verifier reconstructs both halves without floating point arithmetic.

## Originality
**PASS.** The foundational paper arXiv:1911.09944 defines this exact invariant and supplies general bounds, but the inspected full text does not state the finite value \(\mathsf K_{\mathsf D}^{3}(5,1)=21\). Exact-value, alias, supersequence-cover, and deletion-cover searches found no matching indexed research record or accessible primary source giving this value. The 2023 fixed-length Levenshtein paper studies a different metric, and the 2025 subsequence-cover paper uses a different per-word covering notion. A 2026 paper is highly relevant, but only its abstract and preview were inspectable; this is retained as an explicit residual risk rather than treated as negative evidence from the whole paper.

## Value
**PASS.** The minimum deletion-covering cardinality is the central invariant of the foundational literature. This is a natural small nonbinary instance at a length where the general bounds remain far from exact, and the nonuniform dual weights expose the deletion-ball irregularity that motivates the weighted-covering method. The result provides an exact benchmark for constructions and bounds without claiming a broader theorem.

## Closest literature and limitations
The closest inspected source is Lenz–Rashtchian–Siegel–Yaakobi, arXiv:1911.09944, which defines \(\mathsf K_{\mathsf D}^{q}(n,R)\), develops weighted covering lower bounds, and gives general single-deletion bounds. Xie–Sun–Ge, arXiv:2606.15379, develops newer nonbinary bounds and constructions, but the accessible abstract/preview does not state this exact small parameter. The claim is limited to \(q=3,n=5,R=1\), and possible overlap in inaccessible portions of the 2026 paper remains a residual literature risk.

Same-model review: passed. Independent audit: not yet performed.
