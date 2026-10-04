# Same-model review

## Correctness
PASS. The claim is restricted to the step-4 comparison count of Condat's published Fig. 2 pseudocode. The upper bound follows from a monotone integer invariant: every nonterminal cleanup pass removes at least one candidate and the terminal list has \(K\) elements. The \(K=1\) case is proved separately from the reset inequality. For \(K\ge2\), the equality family is explicit; its threshold recurrence forces exactly one deletion per pass until \(K\) candidates remain. Exact-rational replay checks the construction over a broad finite grid without substituting for the analytic proof.

## Originality
PASS with residual risk. Condat's 2014 preprint already states \(O(N^2)\) worst-case complexity and explicitly gives a transformed adversarial sequence for the proposed algorithm, so neither quadratic behavior nor the existence of an adversary is claimed here. The reviewed source does not give the sharp support-conditioned maximum \(T_{N,K}\), and its complexity table reports only the coarse proposed-algorithm bound. Targeted published-finding corpus searches did not return an implication-equivalent finding. A 2026 weighted dynamic-threshold preprint is highly relevant and studies the same add/reset/remove mechanism; its accessible abstract does not state this support-conditioned formula, but the full text was unavailable through the lawful route checked, so equivalence there remains the principal risk.

## Value
PASS. The final support size \(K\) is a natural quantity already tracked by the source algorithm and used in the same paper's complexity table for other methods. The exact law shows a nontrivial structural discontinuity: support one is forced to a singleton cleanup state, whereas support two already attains the full quadratic leading order. This refines a coarse worst-case label into a sharp sparsity-sensitive statement useful for adversarial testing and for understanding when the reset refinement can or cannot eliminate long cleanup phases.

Same-model review: passed. Independent audit: not yet performed.
