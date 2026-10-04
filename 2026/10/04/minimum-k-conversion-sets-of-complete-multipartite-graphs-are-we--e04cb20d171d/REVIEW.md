# Review

## Correctness
PASS. The proof identifies the exact state variable \(U\), the number of newly activated vertices outside a not-yet-activated part. For an incomplete nondeficient part \(i\), the threshold condition is exactly \(k-s_i+U\ge k\), equivalently \(U\ge s_i\). This makes the sorted parking inequalities both necessary and sufficient. The packaged exhaustive verifier agrees with the literal dynamics through order \(8\).

## Originality
PASS. The closest exact primary source, Adams–Brass–Stokes–Troxell (arXiv:1102.5361), gives the already-known complete-multipartite minimum cardinality and a construction of one minimum set. The checked theorem section does not classify every minimum set or count them. Searches under the aliases irreversible conversion, target set selection, perfect target set, contagious set, and dynamic monopoly found no broader statement implying the weighted profile theorem. The main residual risk is older weakly indexed terminology.

## Value
PASS. Minimum cardinality alone does not say which optimal seed placements work. The theorem exposes the precise obstruction as a weighted parking condition, yields an exact count of optimum placements, and gives an efficient profile test. The explicit \(K_{1,100,100}\), \(k=50\) stalled optimum-cardinality profile shows this is not a formal restatement of the known minimum value.

## Closest literature and limitations
The scalar minimum \(\max\{|X|,k\}\) for \(N>k\) is prior work and is not claimed as new. The result is restricted to uniform thresholds on complete multipartite graphs and to minimum seed sets. The full Dreyer–Roberts publisher text was not directly available here; its complete-multipartite minimum-value coverage is corroborated by the inspected later primary paper.

Same-model review: passed. Independent audit: not yet performed.
