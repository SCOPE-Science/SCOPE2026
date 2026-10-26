# Assessment of the sharp approval-committee separation

## Correctness
PASS. The coalition \(S=\{1,2,3\}\) has exactly \(4/3\) payment expression at each voter, while ordinary EJR+ tests the one- and two-voter supporter coalitions and succeeds strictly. The proof independently checks strict core and Pareto efficiency. The two-voter lower bound uses nonwastefulness to make selected-candidate costs sum exactly; the three-voter \(k\le3\) bound is the nine-case strict integer inequality in RESULT.md. Uniform voter replication preserves all relevant inequalities. Exact-rational checker tests both axioms and explicit deviations; numerical tests do not replace the parameter-free arguments.

## Originality
PASS subject to searchable-priority limitations. Brill--Peters (2023) defines ordinary EJR+, and Skowron (2026) Definition 4 gives the stronger up-to-one payment inequality and Example 4 separates it from ordinary EJR+ and the strict core at 1000 voters, 30 candidates, 20 seats. Their inspected sections do not contain the present three-voter/four-seat/five-candidate sharp boundary or the Pareto-efficient witness. The published large witness already establishes nonimplication, which is explicitly excluded from the new claim. Targeted title/definition/example/size searches did not find a smaller covered version. Equivalence embedded in unpublished data, or a stronger result making the size bound immediate, remains a genuine priority risk.

## Value
PASS. A surprisingly small and Pareto-efficient, nonwasteful, core-stable separation sharpens a new payment-based fairness distinction and identifies the structural conditions that suppress it for small committees. The boundary highlights that allowing challenger non-supporters in the payment coalition has genuine effects even with only three voters; it is not a cosmetic reformulation or a routine parameter increment. The strict-versus-weak inequality and nonwastefulness assumptions are essential to the exact boundary.

## Limitations
No uniqueness classification is claimed. The minimum electorate size is claimed under nonwastefulness, while the three-voter minimum seat count is unconditional. The paper's larger separation was already known. Independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
