# Review of the spider resistance-diameter allocation theorem

## Correctness — PASS

The result specifies a finite spider, every edge price, budget, full-vertex effective-resistance diameter, and both equality cases. On a tree, effective resistance equals series resistance. Two applications of strict convexity plus the equality condition in armwise Cauchy--Schwarz yield the exact unique optimizer and threshold. In the balanced case, all arm resistance totals equal \(C/B\); in the dominant case, the unique largest-cost arm alone has a larger resistance. The displayed conductance vectors saturate the budget and attain the lower bound. Exact rational verification, direct all-vertex path enumeration, and numerical epigraph comparisons support, but do not replace, these arguments.

## Originality — PASS on inspected evidence, with residual risk

Ghosh--Boyd--Saberi (MTNS 2006), Section VII, already explicitly identifies minimum maximum effective resistance as a convex SDP problem. The present theorem does not claim that formulation as new; its content is the explicit all-parameter spider solution, unique individual conductances, and sharp squared-arm-price dominance boundary. The 2012 Roos--Bai--Chaerani paper gives general robust multi-current network formulations rather than this spider classification. Available prior records about two-hub double stars use a different topology and do not imply the one-hub formula. Actual published-finding corpus queries targeting spider resistance-diameter optimization returned works about spider curvature and other invariants, not an equivalent theorem. General convex formulations alone do not state or eliminate the need to derive the exact threshold. Unlocated equivalent specialist work remains a risk.

## Value — PASS

Resistance diameter measures worst-case pairwise electrical delay rather than the average; minimizing it under heterogeneous conductance prices is a natural fairness/robustness design objective. The theorem replaces a generic conic optimization program with explicit allocations for arbitrarily long arms and edgewise prices and exhibits a sharp qualitative transition. Even with identical individual edge prices, the transition depends on whether the square of the longest arm length exceeds the sum of squared other lengths. The exact uniqueness and price-allocation rule are reusable for such branched networks. The result makes no assertion about other topologies or physical implementation constraints.

## Closest literature and limitations

- Ghosh, Boyd, Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006, https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf ; the paper presents total-resistance optimization and a general minimax SDP extension, not the exact spider classification in its inspected sections.
- Roos, Bai, Chaerani, *Robust Resistance Network Topology Design by Conic Optimization* (2012), https://doi.org/10.24200/squjs.vol17iss1pp125-146 ; models multiple currents on general networks without the displayed spider-specific transition in inspected full text.

The theorem requires a spider tree, a linear positive edgewise budget, and positive conductances. A general tree with two or more branching junctions need not obey its two-regime classification. The source date uses the first date printed on the 2006 conference proceedings; an exact earlier online-upload timestamp was not independently established.

Self-review: passed. Independent audit: not yet performed.
