# Scientific review

## Correctness

**PASS.** The exact shattering criterion follows from transitive closure and the impossibility of labeling a transitive edge false while an alternate positive directed path remains. Mantel's theorem and discrete convexity establish the exact static maximum and explicit bipartite witnesses attain it. A mistake-count argument bounds the adaptive dimension by the maximum possible number of positive ordered-pair relations. Complete and independently checked online-shattering trees of depths three and six attain this bound locally; blockwise concatenation attains it for every bounded-component size at most four. An independent Boolean-adjacency enumeration checks \(19\) and \(219\) labeled posets and the embedded certificates. The arbitrary-size assertions are derived symbolically.

## Originality

**PASS with residual priority uncertainty.** Targeted source, alias, parameter, and implication searches of research records, accessible previous findings, and primary publications did not identify the full bounded-component classification. The closest general papers concern VC/Littlestone theory (Malliaris–Moran 2021; Chase–Freitag–Reyzin 2023). Duan–Ouyang–Wang (first posted 2024-12-09) analyzes compatibility between whole orders, not binary membership of ordered vertex pairs; its numerically similar VC expression does not imply this shattering criterion or the exact online formulas. The sharp finite certificates and the finite-component amplification were compared against accessible earlier findings about order-ideal and basis-membership classes. Published or archived material not located in these searches remains a genuine risk.

## Value

**PASS.** The finding replaces a generic dimension computation with a complete structural characterization of shattered order queries, an all-parameter exact static law, and a sharp characterization of the smallest component size permitting an unbounded static–adaptive discrepancy. The full gap is determined for all orders of the ground set under component bounds three and four. This is relevant to online relation learning with structural locality: even targets that split into at most three-point comparability components can have arbitrarily larger online shattering rank than VC dimension. The result is not a claim about unrestricted large components or arbitrary logical languages.

## Limits

Exact online dimension is established only for component caps through four. Priority cannot be certified from finite source searches alone. Computational certificates have been replayed; independent external validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
