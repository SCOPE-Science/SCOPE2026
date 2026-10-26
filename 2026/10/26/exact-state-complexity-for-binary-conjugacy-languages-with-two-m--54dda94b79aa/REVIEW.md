# Scientific review

## Correctness — PASS

The domain contains every ordered pair of nonnegative zero gaps and includes periodic and adjacent-marker boundaries. The Myhill–Nerode count is explicitly partitioned by prefix length and residual marker count. The no-one and two-one portions each have exactly one quotient at precisely \(h+1\) depths. For the remaining prefixes, the union of two rectangles enumerates feasible gap coordinates without double counting. Singleton suffixes are injective within their orientation, and the two-valued suffix sets are injective; the only cross-orientation equality is a translation by the gap difference, and its feasible integer ranges both have length \(\min\{h-\ell,\ell+1\}\). Hence the displayed all-parameter formula follows. A separate bottom-up complete-DFA computation and a direct right-language count test the claim on 300 and 45 parameter pairs respectively; those finite checks support but are not substitutes for the proof.

## Originality — PASS with priority caveat

The classical theory gives upper bounds for cyclic shift and for arbitrary prefix-free languages. The fully inspected Gabric–Holub–Shallit article gives the unrestricted maximum over all words and characterizes the maximizing generalized de Bruijn words, but does not enumerate right-quotient identifications for every two-marker binary necklace. The exact formula here is not obtained by substituting a parameter into those maxima; it is a per-instance equality, with a square collision term and a phase boundary at \(h=2\ell+1\). Relevant scholarly searches found no coincident exact family formula. Inaccessibility of some full historical papers means earlier equivalent coverage cannot be excluded, and this is a self-review priority assessment only.

## Value — PASS

Minimizing a language of cyclic rotations is a natural pattern-recognition and finite-automaton storage problem. The two-marker case is the first sparse nontrivial composition beyond a one-marker orbit. Its answer is an exact infinite family, not a numerical sample, and identifies how the relative cyclic gaps determine residual sharing. The saturation of the collision correction is structural and not an immediate consequence of general worst-case bounds.

## Scope and residual risks

No assertion is made for three or more marked symbols, larger alphabets, or nondeterministic state complexity. The full 2007 article and complete 2013 chapter remained inaccessible; historical priority therefore remains qualified. The result has not received independent external mathematical audit.

Self-review: passed. Independent audit: not yet performed.
