# Self-review

**Correctness — PASS.** The upper bound for all sizes counts exactly one third of reversal-equivalent orders on the positive side of every ternary question. The lower bounds through eight labels have complete node-labeled trees with 9,386 distinct leaf witnesses in aggregate. A second implementation checks every leaf and every query split, while a trace-refinement enumeration determines the VC dimensions through six labels. The finite claims do not rely on sampling or extrapolation.

**Originality — PASS under the accessible comparisons.** The closest primary source, Courcelle's 2020 preprint, establishes the ternary relation and reversal quotient but not the shattering dimensions. Manurangsi–Rubinstein 2017 discusses generic dimension computation, and Peters–Procaccia 2021 studies pairwise ranking elicitation rather than ternary midpoint mistake trees. The accessible earlier pairwise-permutation dimension result uses a different query domain and does not entail the claimed values. Full search strings, source inspections, implication comparisons, and remaining priority risks are in `AUDIT.json`. Searches do not establish exhaustive historical priority.

**Mathematical value — PASS.** The finite classification proves sharpness of a universal information-theoretic upper bound up to eight labels, discovers the first failure of the naive cardinality bound at six, and the first adaptive-versus-static gap at four. This is a natural complete sequence of exact online dimensions, with a 13-level certificate already containing 8,192 leaves. Larger label counts and the VC dimensions from seven labels onward remain open in this package.

The largest lower bounds rely on explicit executable certificates; no independent audit has been performed. The literature comparison is limited to the inspected material and available research records.

Self-review: passed. Independent audit: not yet performed.
