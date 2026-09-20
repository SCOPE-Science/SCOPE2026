# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The 2026 neutral-letter characterization reduces the promised automaton problem exactly to alphabeticity. Alphabeticity is equivalent to the two generator identities `aa=a` and `ab=ba` holding modulo Myhill right equivalence after every reachable prefix. Necessity is immediate from support preservation; sufficiency follows because adjacent swaps and duplicate deletion reduce every word to a canonical representative determined only by its support.

A counterexample to either identity has an NL witness: guess a reachable state, one of the two local successor pairs, and a common suffix that distinguishes the two states. Reachability needs a path of length below `|Q|`, and distinguishability needs a path of length below `|Q|^2` in the product automaton. Hence non-alphabeticity is in NL and alphabeticity is in coNL=NL.

For hardness, the reduction from complement bounded-outdegree reachability is sound. The fresh `#` letter is an identity on every state. If the target is unreachable, the language is empty. If it is reachable, a first-hit path word `w` is accepted while `ww` is rejected because both active letters leave the accepting target for the sink; `w` and `ww` have identical support. The construction is complete, fixed-alphabet, and logspace computable. The standard normalization to distinct source and target avoids the empty-path case.

Adversarial checks considered unreachable DFA states, the distinction between state equality and right-language equivalence, the positive-word convention in the motivating circuit model, missing outgoing graph edges, one-letter path supports, and whether the second copy of `w` always leaves the target. Only reachable states enter the semantic criterion; right equivalence, not raw equality, is used; all hardness witnesses are nonempty; missing edges go to a sink; and every nonempty second copy begins with 0 or 1, both of which send the target to the sink.

The standalone verifier reports PASS. It exhaustively compares the right-congruence criterion with explicit minimization on 5,898 small deterministic automata and checks 24,738 small instances of the reachability reduction.

## Originality

**PASS, to the best of our knowledge.** Göller--Manuel, arXiv:2609.18484v1 (16 Sep 2026), was inspected at the theorem and proof level. Its neutral-letter characterization states that constant circuit complexity is equivalent to idempotence/commutativity and support-only membership. It proves PSPACE-completeness for NFA input; its hardness construction adds a fresh symbol as a self-loop on every NFA state. The paper does not state a DFA-input complexity result.

Masopust--Thomazo (DLT 2015) was inspected in its primary PDF. Its Section 3 explicitly formulates k-piecewise testability for **minimal** DFAs; Theorem 2 puts 1-piecewise testability in deterministic logarithmic space. Masopust (MFCS 2016 / arXiv:1603.00361) was also inspected in primary PDF form; Theorem 18 again assumes a minimal DFA and records the 1-piecewise testability test in AC0. Thus the closest prior complexity statements rely on minimal presentations and do not cover arbitrary DFAs.

Targeted searches included exact and synonymous queries for 1-piecewise testability on arbitrary/nonminimal DFAs, NL-hardness of 1-piecewise testability, alphabetic-language DFA recognition, commutative-idempotent/semilattice language recognition, and the motivating arXiv identifier. They returned the cited minimal-DFA and general transformation-semigroup literature, but no theorem equivalent to the arbitrary-DFA NL-completeness result. The current SCOPE archive was searched by the motivating arXiv identifier, piecewise-testable terminology, neutral-letter terminology, and constant-circuit DFA phrasing; no overlap was found.

No novelty is assigned to NL=coNL, DFA-state distinguishability, bounded-outdegree reachability, Simon's congruence, the semilattice identities, or the neutral-letter circuit characterization. The originality claim is only the exact arbitrary-DFA recognition complexity under an explicit neutral letter and the fixed-ternary hardness refinement.

### Residual literature risk

No specific inaccessible paper was identified as a high-probability source of prior coverage. The principal residual risk is folklore: the result follows from standard DFA equivalence machinery plus a short reachability reduction once the presentation question is asked. The 2026 motivating paper is very recent, so a near-simultaneous observation or subsequent revision is also possible.

## Value

**PASS.** The theorem fills the deterministic-input gap left between a known AC0 test on minimal DFAs and the new PSPACE-complete NFA result. It shows that nonminimal deterministic presentation is not a benign implementation detail: even for the extremely simple support-only language class and even when the neutral letter is explicitly an identity transition, semantic quotienting raises recognition to NL-complete. The fixed ternary restriction shows that the hardness is not caused by a growing alphabet.

## Limitations

The result applies only when an identity neutral letter is explicitly present. It does not determine the complexity of constant-circuit membership for arbitrary DFA languages without such a letter, nor does it strengthen the NFA lower bound. The hardness construction uses nonminimal presentations in an essential way, and the proof is sufficiently short that folklore risk should remain attached to the originality claim.
