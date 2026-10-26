# Scientific review

## Correctness — PASS

The theorem concerns complete final EFX with two agents, three known-horizon goods, fixed oblivious input, and fully revealed singleton values. The one-versus-two completion lemma is obtained directly from the strong any-good definition of EFX and nonnegativity. A strict tie refinement reduces the guarantee to two exhaustive cases at the second arrival: agreement gives four equiprobable prefixes of which at least two permit an EFX singleton/pair completion; disagreement gives two equiprobable prefixes of which at least one permits it. Two additive inputs indistinguishable on the first arrival force incompatible recipients for the first good in every EFX allocation, yielding the matching upper bound. The exact verifier checks 4096 weak additive profile pairs, 36 strict ranking pairs, 729 nonadditive monotone maximum-value function pairs, and both upper witnesses. Computational enumeration is supplementary, not the infinite proof.

## Originality — PASS

The closest directly comparable published theorem is Cohen, Teh and Wooldridge, arXiv:2609.28333, Theorem 5.4: their two-agent/three-good specialization yields a \(1/3\) constructive lower bound and a \(1/2\) universal upper bound. Their inspected proof does not supply the matching adaptive second-arrival policy. Chen and Long, arXiv:2609.23577, allow an unrestricted/unknown stopping horizon in their small-success EFX impossibility, so it does not cover fixed, known three-good success. Neoh and Teh, arXiv:2504.03951, count offline EFX completions; Melissourgos and Protopapas, arXiv:2508.04779, investigate deterministic guarantees with predictive information. Searches for fixed-horizon online EFX probability, ordinal second-item policies, equivalent minimax games, and exact two-agent three-good constants revealed no covering claim. Historical-priority uncertainty remains, and absence of a database hit is not treated as proof of novelty.

## Mathematical value — PASS

The exact first nontrivial stochastic EFX frontier resolves a motivated quantitative gap between \(1/3\) and \(1/2\) in a very recent general impossibility theorem, using a valuation-independent online policy that only needs observed singleton comparisons. Its extension from additive inputs to all nonnegative monotone set functions follows from a structural one-versus-two completion lemma. It also separates known finite-horizon guarantees from impossibility for unrestricted unknown horizons. The statement is limited to two agents, three goods and an oblivious input; no broader constant is asserted.

## Limitations and residual risks

No independent audit has been performed. Mathematical correctness relies on the online revelation of both agents' singleton values, strong final EFX, independence of the random bits, and a fixed nonadaptive input. A previously published equivalent special-case policy could still exist outside the inspected literature and indexed research records; the closest general theorem does not itself state this exact result. The proof does not address strategic reporting, fairness after prefixes, unknown horizon or more than three goods.

Self-review: passed. Independent audit: not yet performed.
