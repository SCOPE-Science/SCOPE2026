# Independent mathematical audit

## correctness

PASS

For \(G_k=(-1)^kG\), the empirical mean gives \(\delta_{2n+1}=-G\) and \(\delta_{2n}=2nG/(2n+1)\), hence \(\delta_k^2\to G^2\). The uniform accumulator therefore has \(v_k/k\to G^2\). The published incremental recurrence telescopes exactly to \(v_k=(k+1)^{-2}\sum_{\tau=0}^k(\tau+1)^2\delta_\tau^2\), so weighted Cesàro convergence gives \(v_k/k\to G^2/3\). The exponential recursion converges to \(G^2\), and its monotone envelope has the same limit. Since \(\gamma_k=O(k^{-1})\) while \(h_k=\Theta(\sqrt{k})\), the practical coordinate update has normalized asymptotic magnitudes \(1/\beta,\sqrt3/\beta,1/\beta\) for uni/inc/exp.

## originality

PASS

The defining A2Grad paper publishes the three moving-average recurrences and motivates the incremental rule as a more aggressive quadratic weighting, but it does not analyze a period-two gradient input or derive the exact scale/gain constants. Targeted searches for A2Grad with alternating/period-two gradients and the \(\sqrt3\) gain found implementations and the original algorithm but no implication-equivalent response law. The result is a new exact response calculation for a canonical highest-frequency discrete signal rather than a parameter renaming of an existing theorem.

## value

PASS

A period-two sign reversal is the canonical highest-frequency discrete forcing for a gradient accumulator. The exact gain separates the three published A2Grad scale rules and quantifies the paper's qualitative claim that the incremental quadratic weighting is more aggressive. This is a motivated exact response invariant of a natural optimizer, not an arbitrary finite slice, and can inform stability/diagnostic comparisons even without a downstream convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
