# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The reduction is an exact specialization of the published multigraph characterization: when k1=n1-2, deleting a pair of vertices leaves the relevant k1-vertex induced subgraph, so the condition is equivalent to a lower bound on the number of edges incident with every vertex pair. The odd-q lower bound follows from the minimum-degree vertex inequality and the handshake lemma; the construction uses an almost-regular simple graph of minimum degree (q+1)/2. The q=1,2,4 formulas have separate matching lower bounds and explicit sharp constructions. The final LRC dichotomy uses the established fact that D(n,k,r) is always either d* or d*-1.

The proof was stress-tested against small exact integer optimizations during review, and the public verification artifact independently checks the stated constructions and parameter identities over a finite range. Those computations support, but are not used in place of, the symbolic proof.

## Originality

PASS, to the best of our knowledge. The highly relevant primary source by Khabbazian and Médard was inspected in full. It proves the general multigraph equivalence, gives an exact theorem for n1-k1=1, and remarks that similar methods can extend to n1-k1<=3. It does not provide the codimension-two odd-gap formula or the q=2,4 thresholds stated here. Searches for the exact parameter condition, synonymous LMD/LRC formulations, the n1-k1=2 specialization, and follow-up work through the present did not locate a published result giving these formulas.

The main residual originality risk is terminology: the auxiliary pair-incidence extremal number is elementary and may have appeared under a graph covering or degree-sum name not retrieved by the searches. That would not by itself imply prior publication of the LRC criterion, but a broader theorem could potentially subsume it. No concrete source implying the displayed codimension-two LRC result was found.

## Value

PASS. The result advances the exact largest-minimum-distance classification from codimension one to a broad codimension-two regime, gives a closed form for every feasible odd gap q>=3, settles two additional even gaps, and supplies infinite explicit LRC parameter families outside the exact cases listed in the current primary source. The threshold is sharp on both sides: below it D=d*-1, at or above it D=d*.

## Scientific limitations

The arbitrary-odd formula is restricted to q<=2n1-3; larger odd gaps and general even gaps q>=6 remain open here. The result is for the unrestricted-field linear LMD problem and does not optimize finite alphabet size. Same-model review is not independent validation.
