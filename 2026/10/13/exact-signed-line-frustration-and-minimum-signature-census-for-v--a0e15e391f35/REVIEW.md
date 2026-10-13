# Self-review

## Correctness — PASS

The signed-line sign convention is derived from the actual oriented incidence entries. The cost of a base orientation is the sum of the products of in- and out-degrees, exactly the existing orientation identity. An odd cycle forces at least one mixed vertex; because the odd cycles are vertex-disjoint, the local contributions supply an additive lower bound. A block-tree orientation construction attains it with exactly one mixed minimum-degree vertex on each odd cycle. Equality requires precisely these configurations. Rooting the block tree shows a twofold global orientation choice and an independent binary choice at each designated mixed vertex incident to a noncycle edge. For a connected graph with edges the signed-line graph is connected, so global reversal is the precise two-to-one kernel of orientation-to-signature, yielding the stated number. An isolated-vertex case is handled separately. Exact finite computational tests compare independent orientation and switching enumerations; they corroborate but do not replace the proof.

## Originality — PASS

The nearest paper, Bal's *The Antisymmetric Line Graph*, arXiv:2603.03087, defines exactly this signed line graph and proves the general orientation formula, the defect bound, and some special families; its full Sections 3, 8 and 9 were inspected. Those already-published results are not claimed as new. The present claim is an explicit cactus-wide weighted odd-cycle minimum **and** a complete count of optimal switching signatures. The older full text by Belardo, Stanić and Zaslavsky (arXiv:1908.02001) studies signed-line constructions and related frustration inequalities but does not give these two formulas. Searches for equivalent directed two-path, optimal-orientation, odd-unicyclic and signed-line formulations, plus comparison of the specific mathematical implications of the closest indexed research findings, did not identify a covering result. Residual risk: terminology and unindexed equivalent results, including different signed-line conventions. A negative search is not a guarantee of novelty.

## Value — PASS

This theorem exactly resolves a natural frustration invariant on an infinite graph class extending both trees and odd unicyclic graphs to arbitrarily many disjoint odd cycle blocks, with unbounded vertex degrees. Its degree-sensitive answer is not determined by odd-cycle count alone: an odd cycle with \(h\) leaves at each cycle vertex has base-graph edge bipartization number one but signed-line frustration \(h+1\). The optimal-signature product also describes degeneracies of the global optimum and distinguishes the degree-two and higher-degree cases, a genuinely additional structural invariant rather than a routine restatement of the extremal value.

## Closest literature and limitations

H. S. Bal, *The Antisymmetric Line Graph*, arXiv:2603.03087 (2026), Lemma 2 and Sections 8–9. F. Belardo, Z. Stanić, T. Zaslavsky, *Total graph of a signed graph*, arXiv:1908.02001, Sections 2–3. The proof does not extend automatically to cycles sharing vertices. Exhaustive tests terminate at the specified finite orders and do not certify all graphs. Some literature may not be indexed, and independent external audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
