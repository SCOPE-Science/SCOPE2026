# Review of Exact length-six non-overlapping codes at alphabet sizes seven through nine

## Correctness
PASS. The exact SQN recurrence is a complete characterization of the maximum-cardinality problem. Reversal reduces to \(x_1\le y_1\). For fixed levels through three, the objective is affine in \(x_5\), so \(x_5\) can be taken at an endpoint; after substituting that choice, the objective is affine in \(x_4\), so only its two endpoints need inspection. Exhaustive integer enumeration then proves the three optima and unique reduced profiles. Proposition 11 and uniqueness of partition systems for \(q\ge3\) give the counts \(14\), \(16\), and \(6552\).

The standalone verifier uses only integer arithmetic and ends in `VERIFY_OK`. The public companion solver from Stanovnik–Moškon–Mraz independently returns the same values and profiles for all three instances.

Risk: this is a finite exact classification; it does not imply a general formula for larger \(q\).

## Originality
PASS with residual bibliographic risk. The 2024 full text explicitly reports nonbinary exact SQN solutions only for \(3\le q\le6\) and gives Table 1 only for \(2\le q\le6\). Searches for the length-six values, the \(q=9\) value, cross-bifix-free aliases, and Blackburn comparisons found length-five exact published-finding corpus records as the closest matches, not this statement. The classical 2012–2013 sources provide constructions and bounds rather than these exact instances.

Risk: the generic solver is public, so an unpublished or unindexed run may already contain these numbers; failed searches are not a proof of novelty.

## Value
PASS. These are the first three alphabet sizes immediately beyond the published exact nonbinary table at length six. The pair \(q=7,8\) preserves the simple \(AB^5\) extremal form, while \(q=9\) is a concrete structural transition to a two-level partition and improves the best \(k=5\) Blackburn construction by \(258\). The exact maximum-code counts expose how sharply the extremal family expands at that transition.

Risk: the result is narrow and does not by itself settle Blackburn's broader conjecture or the behavior for \(q\ge10\).

## Closest literature and limitations
Chee–Kiah–Purkayastha–Wang (2012) and Blackburn (2013) provide the historical constructions and bounds. Stanovnik–Moškon–Mraz (2024) provide the exact SQN framework and report solved nonbinary instances only through \(q=6\). The present result solves the next three length-six alphabet sizes and classifies/counts all maxima there. Literature search cannot exclude obscure unindexed computations.

Same-model review: passed. Independent audit: not yet performed.
