# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The construction replaces only the family of erased one-step transitions from the initial state to the Jirásková--Masopust suffix-start states. A deterministic h-ary routing tree makes exactly the same original target states reachable by erased-only words. Its fresh internal states have no visible transitions, and original target states receive no erased outgoing transitions. Hence projection yields exactly the same visible language as the direct-fan-out witness.

The routing-state formula is exact in the stated routing-only model. With J fresh routing states, each of the J routing states and L targets requires an incoming erased edge, while the root and routing states provide at most h(J+1) erased outgoing edges. Thus J+L <= h(J+1). The partially filled h-ary tree attains the resulting lower bound.

The input automaton is finite because both the routing tree and the visible chain are acyclic. Minimality follows from distinct accepted continuation lengths for chain states, the visible-versus-erased first-symbol distinction between chain and routing states, and descendant-leaf continuations separating distinct routing states.

The asymptotic exponent follows by substituting m=floor(N/(t+1)) and J=(N-m)/(h-1)+O(1), then expressing m in terms of the total minimal input-state count n_N=N+J.

The finite verification artifact checks representative values k=3,4,5; h=2,3,4; N=6,...,12. It confirms minimal input size, exact equality of the reachable visible-subset transition system with the direct-fan-out construction after inert routing states are removed, and the cited geometric lower bound in all 63 cases.

## Originality — PASS

The 2012 Jirásková--Masopust paper explicitly states that its finite-language construction requires a domain alphabet of linear size in the number of states and leaves open whether this can be limited by a constant. The present result does not claim to close that exact problem; it gives a quantitative partial answer by obtaining a state-independent domain alphabet while retaining an arbitrarily large fraction of the witness's exponential lower-bound rate.

Searches were made for fixed/bounded/constant alphabet formulations of finite-language projection state complexity, hidden or unobservable alphabet reduction, synonymous projection formulations, later work citing the 2012 paper, and stronger finite-language determinization results. The inspected later projection papers of Hoffmann concern permutation and commutative automata. Geffert--Pališínová--Szabari study binary prefix coding of regular languages, which changes the representation by a code rather than replacing erased fan-out while preserving the same projected language. Recent block-language work reviews finite-language determinization bounds but does not state this construction.

No inspected source states the fixed-hidden-alphabet routing lemma, the exact routing overhead, or the near-preservation corollary. Originality is therefore assessed to the best of our knowledge, not as an exhaustive literature guarantee.

A residual risk is Kai Salomaa's 2011 personal communication, cited as reference [31] in the 2012 paper, on NFA-to-DFA conversion for finite languages over a k-letter alphabet. It was not available as a public paper and could contain unpublished refinements relevant to the background determinization bound.

## Value — PASS

The result directly addresses a published structural limitation of a standard finite-language projection witness. It supplies a reusable alphabet-compression mechanism, an exact optimal routing cost in a natural model, and an explicit tradeoff between hidden alphabet size and preserved exponential state-complexity rate. For power-of-two projected alphabets, the retained exponent can be made arbitrarily close to the known optimal finite-NFA determinization exponent while keeping the domain alphabet fixed with respect to the state count.

## Scientific limitations

The exact constant-domain-alphabet attainability question remains open. The theorem establishes a family indexed by N rather than every possible total input-state count. The optimality claim for J is only for deterministic routing-only replacements in which the root and fresh routing states are the sources of the new erased transitions and the original targets remain erased-transition sinks.
