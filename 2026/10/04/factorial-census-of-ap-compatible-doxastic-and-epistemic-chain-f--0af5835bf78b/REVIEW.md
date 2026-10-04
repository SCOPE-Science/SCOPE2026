# Review

## Correctness

PASS. Doxasticity bounds the incoming column at target \(j\) by \(\{0,\ldots,j\}\), while \(\mathbf{AP}\)-compatibility forces that column to be downward closed. On a chain, this is exactly an initial segment or the empty set, producing \(j+2\) independent choices and therefore \((n+1)!\) relations.

For basicity, any single edge \(vRt\) witnesses the basic condition at every state \(s\) by choosing the common upper bound \(\max\{s,v\}\); hence among doxastic chain frames, founded is exactly nonemptiness. For epistemicity, \(\mathbf{AP}\)-compatibility turns visionaryness into seriality. Doxasticity then forces the top state to access itself, and that one top loop, together with downward closure of its incoming column, makes every state access the top. Thus the epistemic condition is exactly \(c_{n-1}=n-1\), leaving \(n!\) choices.

An exhaustive standard-library checker agrees with the formulas for all binary relations on chains of sizes \(1\) through \(4\).

## Originality

PASS. The primary source defines basic, visionary, futuristic, doxastic, founded, epistemic, and \(\mathbf{AP}\)-compatible frames and develops their modal correspondence and completeness theory. Its full text contains no finite-chain, linear-order, factorial, or exact-count classification of the relations.

Candidate-specific semantic searches in the published finding database returned no result about \(\mathbf{AP}\)-compatible doxastic chain frames. General web searches likewise found the primary Balbiani article but no equivalent chain parametrization or census.

## Value

PASS. Finite chains are the canonical linearly ordered intuitionistic frames. The result gives a complete normal form for every \(\mathbf{AP}\)-compatible doxastic relation on them, not merely an asymptotic or a sample enumeration. It simultaneously gives exact counts for the founded and epistemic subclasses and shows that epistemicity is a single top-column constraint, with exact density \(1/(n+1)\). This provides a compact finite test family for the new two-modality semantics.

## Closest literature and limitations

The closest source is Balbiani's 2025 paper introducing the two-modality semantics and the frame classes being counted. The paper proves that visionary and futuristic coincide on doxastic frames and defines \(\mathbf{AP}\)-compatibility by \(\le\circ R\subseteq R\), but it does not perform the finite-chain classification.

The formulas are specific to chains. On arbitrary preorders, incoming columns are downsets rather than initial segments, and their interactions with doxasticity need not factor into the same factorial product.

Same-model review: passed. Independent audit: not yet performed.
