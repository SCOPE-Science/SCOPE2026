# Scientific assessment: finite Heyting-chain powers

## Correctness: PASS

The implication operation in a chain yields either its second input or the top element, so intermediate truth values cannot arise at a coordinate absent from the generators there. Positive/zero signatures determine zero sets of all terms under conjunction, disjunction, and implication. Conversely, negation and double negation give Boolean tests isolating each signature; the per-coordinate intermediate-level coverage then constructs each supported singleton value, proving sufficiency. Inclusion–exclusion counts valid decorations of distinct binary words, and the rank cutoff follows from the minimum number of positive positions. For fixed chain size, the pair-collision graph gives the Poisson birthday law: disjoint edges supply factorial moments, while connected components on three or more indices vanish by strict moment inequalities; variance handles the high-collision regime. Missing local levels have vanishing probability when collision expectation is bounded. The self-contained finite closure verifier checks 11,189 complete generator tuples and 36 independent census cases, with 693 rank boundaries.

## Originality: PASS, with residual historical uncertainty

Martins–Moraschini (2023, arXiv:2306.15997), Section 3 and its Coloring Theorem, provides the closest relevant Heyting-generation background. The inspected theorem does not classify ordered generating tuples of a specified finite Heyting-chain power, count them by positive-word weight, or give a random birthday law. Czédli (2024, DOI:10.15826/umj.2024.1.004), especially Theorem 1, computes generator numbers for the *distributive-lattice reduct* and uses unrelated posets; it neither has Heyting implication nor this weighted tuple and random law. Carai (2024, arXiv:2406.05480) studies free Gödel algebras and coproducts, not these direct-power generators. Targeted published-finding corpus comparisons surfaced results on free-algebra automorphisms, random distributive-lattice orbits, and general occupancy, none proving the present exact classification. Standard inclusion–exclusion and birthday limits are tools, not claimed as individually new. A specialized older antecedent may exist, and no independent audit has been performed.

## Mathematical value: PASS

Finite powers of Heyting chains are standard building blocks in many-valued algebraic logic, and finding the minimum generating size for direct powers is a natural invariant. The result is more than a restatement of a rank: it characterizes **every** successful ordered tuple, supplies a uniform exact census, and distinguishes worst-case construction from typical random generation. The comparison with lattice-reduct generation documents how a logical connective changes generation. This provides a reusable description of finite generating configurations and a probability threshold, both logically motivated rather than arbitrary finite subcases.

## Limits

The theorem concerns bounded Heyting powers, not monadic Gödel powers or the lattice reduct. The asymptotic statement holds for fixed chain size, and the finite checks do not establish the infinite probability limit. Historical coverage beyond the inspected sources remains uncertain.

Self-review: passed. Independent audit: not yet performed.
