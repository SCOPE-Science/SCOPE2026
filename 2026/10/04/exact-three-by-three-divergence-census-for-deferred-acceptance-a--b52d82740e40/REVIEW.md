# Same-model scientific review

## Correctness
**PASS.** The final claim is finite and exhaustive. The complete \(3\times3\) domain has \((3!)^6=46{,}656\) profiles, all of which are generated. Two separately coded DA implementations agree profile by profile, and two separately coded TTC implementations agree profile by profile. DA Pareto efficiency is not inferred from TTC; it is checked against all six perfect matchings independently. The symmetry counts are obtained by canonical orbit reduction and independently reconstructed by Burnside's lemma. The actual embedded verifier returns `VERIFY_OK`.

Risk: the proof of the numerical census is computational rather than a closed symbolic count. Multiple exact cross-checks reduce ordinary implementation risk, but independent external validation has not been performed.

## Originality
**PASS.** Abdulkadiroğlu--Sönmez provide the mechanisms, the efficiency/stability tradeoff, and a three-student Pareto-improvement example. Kesten proves broader priority-structure comparison results and explicitly gives the qualitative possibility that an inefficient DA outcome is not Pareto-dominated by TTC. Those results do not state the exact first-size incidence \(4{,}320/46{,}656\), the \(1{,}080\) TTC-dominance count, the exact \(216\)-profile inefficient-but-incomparable stratum, or the \(120\)-class quotient. Searches by aliases, exact counts, reduced probabilities, and the Example-4 implication found no equivalent statement.

Risk: failed search is not proof of novelty. An unindexed thesis, course note, software table, or supplementary computation may contain the same finite census.

## Value
**PASS.** The two mechanisms are canonical competing school-choice rules, and the cited literature frames their stability-versus-efficiency tradeoff as a central design question. Three-by-three is the first nontrivial size because the mechanisms coincide at every smaller strict unit-capacity profile. Exact frequencies distinguish three materially different outcomes—agreement, TTC Pareto improvement, and incomparability—and quantify the specific literature-known phenomenon in which TTC fails to repair an inefficient DA outcome. The quotient removes arbitrary labels and shows that the exceptional stratum consists of six intrinsic types.

Same-model review: passed. Independent audit: not yet performed.
