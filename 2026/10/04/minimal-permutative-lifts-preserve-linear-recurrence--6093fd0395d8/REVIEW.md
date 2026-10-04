# Review of Minimal permutative lifts preserve linear recurrence

## Correctness
PASS. Kang and Jäger's conjugacy reduces the lift to a finite permutation skew product. For a length-\(n\) lifted word, its base word and initial fiber state determine the entire lifted word. Linear recurrence bounds the lengths and multiplicities of return words uniformly. Inducing on \([w]\times F\) produces a minimal finite permutation extension of the derived shift, and the finite-derived-system argument used by Bruin yields a uniform bound on fiber-state return in return-word time. Multiplying this bound by the base return-length bound gives a global linear recurrence constant.

The periodic base case is finite. Higher-block recoding needed to make the cocycle one-block preserves linear recurrence. No computational evidence is needed for the proof.

## Originality
PASS. The closest primary source, Kang and Jäger, explicitly gives the skew-product representation and states linear recurrence for minimal lifts over primitive substitution bases, with the general primitive-substitution proof deferred to work in preparation. The present statement assumes only that the base itself is linearly recurrent. Bruin's theorem is about homeomorphic speedups and its finite permutation-extension lemma occurs inside that specialized construction; the inspected text does not state the general permanence theorem for arbitrary minimal finite permutation extensions or permutative lifts.

Searches for equivalent formulations involving finite group extensions, finite-to-one extensions, skew products, and permutative lifts did not find a stronger published statement implying the claim. This negative search evidence is supplementary rather than a proof of novelty. The unavailable work in preparation remains a residual overlap risk.

## Value
PASS. Linear recurrence is a strong quantitative form of uniform recurrence that implies unique ergodicity and strong complexity/return-word control. Permutative lifts are a natural finite-extension construction in the recent source, and extending the recurrence conclusion from primitive substitution bases to every linearly recurrent base isolates the actual dynamical hypothesis needed by the finite-state argument. The result gives a reusable permanence principle rather than a parameter-specific computation.

## Closest literature and limitations
The closest inspected mechanisms are Kang and Jäger's finite skew-product model and Bruin's return-word finite-group argument. The result requires minimality of the extension and does not provide an optimized recurrence constant. A cited work in preparation could eventually overlap, but it was not publicly inspectable.

Same-model review: passed. Independent audit: not yet performed.
