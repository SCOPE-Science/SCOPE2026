# Same-model scientific review

## Correctness assessment
PASS. The claim reduces to finite exhaustive checks on simple labeled graphs. For \(n=7\), the primary verifier enumerates all edge counts through \(9\), finds no saturated graph below \(9\), and finds exactly \(840\) at \(9\). The representative extremal graph has automorphism group order \(6\), so its orbit has size \(840\), proving uniqueness up to isomorphism.

For \(n=8\), the primary verifier enumerates all edge counts through \(10\), finds no saturated graph below \(10\), and finds exactly \(11760\) at \(10\). The two stated representatives are saturated, have distinct degree sequences, and have orbit sizes \(1680\) and \(10080\), which sum to \(11760\). A second implementation uses a different edge-role test for \(K_3\cup 2K_2\) and reproduces the extremal counts.

## Originality assessment
PASS, best-of-knowledge. The closest current primary literature found is arXiv:2608.00459v1, which treats \(K_p\cup K_q\cup K_r\) for sufficiently large \(n\); its specialization \(p=q=2\), \(r=3\) is the same forbidden graph. Targeted web searches for exact small-order saturation of \(K_3\cup 2K_2\), including the equivalent notation \(K_2\cup K_2\cup K_3\), did not locate the \(n=7\) or \(n=8\) values or the stated extremal classifications.

Targeted published-finding corpus semantic searches included the exact claims, the equivalent forbidden-graph notation, generic disconnected-graph saturation language, and small-order extremal classification language. The closest returned published-finding corpus items concerned other saturation problems, especially `2026/9/16/SCOPE011` on fan saturation and `2026/9/17/SCOPE001` on weak rainbow saturation of \(C_4\); neither contains the present claim or an equivalent stronger result.

## Value assessment
PASS. The recent literature establishes the sufficiently-large-order regime for this three-clique union, while these computations resolve and classify the first two admissible orders. The result shows explicitly that the small-order extremal structure is different from the eventual large-order picture and provides certified boundary data that can inform attempts to determine the full finite-\(n\) transition.

## Closest literature
- Hanlai Lin, Zhen He, and Yiduo Xu, arXiv:2608.00459v1, first submitted 2026-08-01, MSC2020 \(05C35\). This is the direct literature lead and covers the same family for sufficiently large order.
- A January 2026 paper on \(K_3\cup 2K_2\)-designs was found in web search, but it concerns edge decompositions rather than graph saturation and does not imply the present saturation values.

## Scientific limitations
The result is restricted to \(n=7,8\), and the proof is computational. The literature search was targeted rather than formally exhaustive, so an inaccessible or unpublished prior computation could still exist. No claim is made about \(n\ge 9\).

Same-model review: passed. Independent audit: not yet performed.
