# Scientific review: concave-envelope isotonic stability

## Correctness — PASS

The theorem covers every integer \(n\ge2\), all strictly positive fitting masses and edge-variation weights, and every real input pair. Weighted PAV has finitely many linear block-average pieces; the edge-step decomposition gives their exact variation seminorms. For a step crossing a block, the only nonzero output gradients occur at its two external boundaries, yielding a mass-coordinate chord. Their maximum is the least concave majorant of edge weights. Strictly decreasing block data with sufficiently separated exterior singleton levels realize each chord locally, so the bound is sharp and attained; strictly increasing data attain the unit case. The adjoining-slope condition is precisely discrete concavity. The provided exact-rational checker independently tests block partition norms, input pairs, attaining witnesses, and the linear-time hull algorithm. Computations are not used to infer the all-dimensional result.

## Originality — PASS with explicit residual risk

Yeganova–Wilbur (2009) supplies weighted PAV and fitted block means. Guyader–Jégou–A. Németh–S. Németh (2012) studies order-cone geometry and iterative bounded-variation fitting. Yang–Barber (2017) gives a **general qualitative** nonexpansivity criterion for unweighted isotonic projection under arbitrary seminorms; its neighbor-averaging theorem can subsume the **unweighted qualitative contraction subcase**, which is not claimed separately as new. The assessed result instead computes the exact constant when contraction fails, for arbitrary quadratic observation masses and independently chosen variation weights, with a mass-coordinate concave-majorant formula, attainment and a linear-time algorithm. Searches of mathematical publications and published research records returned related projection stability results in coordinatewise norms but no statement implying this quantitative weighted-variation formula. A historically implicit formula remains possible, particularly in older sensitivity analyses of PAV.

## Mathematical value — PASS

The observation masses arise naturally as precision/reliability weights, whereas the edge weights specify the desired regularity of perturbations. Their interaction previously left the sharp path-variation sensitivity undetermined in the inspected literature. The theorem turns this operator stability question into the classical geometry of a concave envelope; it identifies all contractive weight configurations, gives an exact and efficiently computable amplification ratio for noncontractive configurations, and produces actual worst-case perturbations. Three-vertex examples have arbitrarily large amplification when one edge penalty becomes small, showing the precision of the weight criterion matters rather than simply providing a routine small-parameter correction.

## Closest sources and limitations

Closest primary sources: Yeganova and Wilbur, doi:10.1007/s10957-008-9477-0, weighted PAV §2; Guyader and collaborators, arXiv:1211.3930, order-cone geometry §§1–2; Yang and Barber, arXiv:1706.01852, contraction theorem in §2 and proof in §6. No independent external audit has been performed. The mathematical theorem is confined to finite weighted least-squares chains with positive parameters; any generalizations to partial orders or alternate losses are outside its scope. The literature search cannot exclude unindexed equivalent calculations.

Self-review: passed. Independent audit: not yet performed.
