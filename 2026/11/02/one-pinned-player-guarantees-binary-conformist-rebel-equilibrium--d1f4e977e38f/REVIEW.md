# Scientific review

## Correctness — PASS

The claim fixes exactly two available actions, unit contributions from the two neighbors on a simple undirected ring, arbitrary conformist/rebel patterns and prescribed stubborn actions. The local best-response equivalence in disagreement bits handles ties without assuming strict incentives. The four-state parity argument proves both endpoint parities possible on every chain, including the one-pin case where endpoint actions coincide, so all pinned blocks admit compatible assignments. For the exact single-pin count, the forbidden rise of the transformed difference word gives exactly \(n+1\) candidate patterns; cyclic XOR closure selects exactly the stated parity class and the fixed value removes global spin ambiguity. The supplied C++ program recomputes equilibria directly; it covers exhaustive four-type assignments through eight vertices, exact pin cases through sixteen, and a three-action counterexample. Finite checks do not certify the infinite theorem; the symbolic argument is the basis for acceptance.

## Originality — PASS with priority uncertainty

Cao–Yang's 2014 Theorem 4 handles only two types and no pinned agents; its classification of the previously frustrated alternating rings is explicitly credited, not repackaged. Cao et al. (2019) analyze two-type best-response dynamics on rings. Cao–Sanchez–Zhang (2026) introduce binary three-type games but prove sufficient general criteria that need not hold on alternating pinned rings; their Section 3 does not state this unconditional cycle result or count. Pei–Cao–Zhang (2026) explicitly restrict the ring theorem to at least three actions, and a direct four-vertex ternary obstruction confirms it cannot imply the binary restoration claim. Searches are not a uniqueness proof: unindexed equivalent work and incompletely accessible literature remain residual risks.

## Mathematical value — PASS

The established binary fashion-game obstruction is a nonexistence phenomenon caused by an alternating ring. Fixing one vertex removes the obstruction for every binary type assignment on every cycle, not just near-alternating examples; moreover the formerly obstructed length family gains exactly \(n/2\) pure equilibria. This gives a sharp and quantitatively explicit intervention result for coordination/anti-coordination networks, as well as a meaningful two-versus-three-action boundary. The result does not assume or imply convergence to one of the restored equilibria.

## Closest literature and limitations

The main primary comparisons are Cao and Yang (2014, ring classification), Cao et al. (2019, two-type dynamics), Cao, Sanchez and Zhang (2026, binary three-type sufficient conditions), and Pei, Cao and Zhang (2026, multi-action ring classification). The exact proof is for simple unweighted cycles and binary actions, and no claim is made for arbitrary networks or three-action restoration. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
