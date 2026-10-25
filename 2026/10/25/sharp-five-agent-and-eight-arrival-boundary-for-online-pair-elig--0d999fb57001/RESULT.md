# Sharp five-agent and eight-arrival boundary for online pair-eligible proportionality up to one item

## Finding
For either unit goods or unit chores arriving online with **exactly two eligible distinct agents per item**, exact eligibility-aware proportionality up to one item at **every prefix** can be maintained forever with at most five agents. With six agents, seven arrivals are always survivable, while an adaptive adversary forces a violation on the eighth arrival, regardless of the allocator's actions.

## Assumptions and scope
Fix a finite labelled set of agents and a sequence of arrivals. Every arriving item has a two-element eligibility set and must immediately and irrevocably be allocated to one of those agents. Every agent values each item for which they are eligible as one unit, and all other items as zero. Write \(e_i(t)\) for the count of items eligible for agent \(i\), \(L_i(t)\) for their allocated item count, and \(P_i(t)=e_i(t)/2\) for their eligibility-aware proportional share. For goods, PROP1 requires \(L_i(t)+1\ge P_i(t)\) whenever an eligible item is missing, while a non-missing agent satisfies PROP1 automatically. For chores, PROP1 requires \(L_i(t)-1\le P_i(t)\) whenever an item is allocated, and is automatic for an unallocated agent. Both are equivalent, for these integral units, to a signed discrepancy \(d_i\le2\): use \(d_i=e_i-2L_i\) for goods and \(d_i=2L_i-e_i\) for chores. In particular a violation \(d_i=3\) is a shortfall/excess of \(3/2\) units and cannot be repaired by one item.

## Proof
For goods choose the eligible agent with larger signed discrepancy; for chores choose the eligible agent with smaller signed discrepancy. Sort discrepancy coordinates in decreasing order after each allocation. If two coordinates in positions \(a<b\) are chosen, the higher coordinate decreases by one, the lower increases by one, and then the vector is sorted again. Ties do not affect this sorted successor. Initially every discrepancy is zero. Therefore both problems have exactly the same abstract greedy transition relation. Every coordinate sum remains zero.

For five agents the following nine vectors form a transition-closed set containing the zero vector (write each tuple in decreasing order):

```
(0,0,0,0,0)
(1,0,0,0,-1)
(1,1,0,-1,-1)
(1,1,0,0,-2)
(1,1,1,-1,-2)
(2,0,0,-1,-1)
(2,0,0,0,-2)
(2,1,-1,-1,-1)
(2,1,0,-1,-2)
```

Checking each of the ten possible coordinate pairs for each vector gives a successor in this nine-vector set; the included standalone checker reconstructs and closes the set independently from zero. Thus induction, not a bounded simulation, proves every prefix safe for *arbitrarily long* sequences. With fewer agents, pad the vector with permanently unused zero-discrepancy agents to five; the same invariant proves the assertion.

For six agents enumerate only the first seven greedy transitions, exploiting invariance under permutation: the numbers of distinct sorted vectors at depths \(t=0,1,\ldots,7\) are \(1,1,3,6,9,10,11,13\), respectively, and every vector has maximum coordinate at most two. These finite levels exhaust the \(15\) possible pair choices at each depth, establishing a seven-arrival online guarantee without making an infinite claim.

For the converse, an adaptive adversary at each of eight steps selects two agents whose current discrepancies are equal. Whichever agent receives the item, one selected discrepancy rises by one and the other falls by one; the sorted successor is therefore independent of that choice. Starting from all zeros, select equal-coordinate levels in order \(0,0,1,0,-1,0,1,2\). The successive sorted vectors are

```
(0,0,0,0,0,0)
(1,0,0,0,0,-1)
(1,1,0,0,-1,-1)
(2,0,0,0,-1,-1)
(2,1,0,-1,-1,-1)
(2,1,0,0,-1,-2)
(2,1,1,-1,-1,-2)
(2,2,0,-1,-1,-2)
(3,1,0,-1,-1,-2)
```

Every announced equal pair exists, and every allocator choice gives exactly the displayed next sorted vector. At step eight a discrepancy is three, violating PROP1. This works for both signed conventions because equality makes the two possible orientations equivalent up to permutation. The five-agent invariant and the six-agent seven-step enumeration make both thresholds sharp.

## Verification
Run `python verify.py` using Python 3 standard library. It checks the complete five-agent invariant closure, every permutation-canonical reachable state at six agents through step seven, and every transition in the forced eight-arrival equality trace. The exact expected stdout is embedded as `verification_output.txt`. No floating-point arithmetic or randomized sampling is used.

## Relationship to prior work
Biburger, Megow and Shahkarami introduce the same eligibility-based share for online fair division and obtain asymptotic guarantees and adversarial bounds (arXiv:2610.08064v1, public 2026-10-06). Their Appendix C, Lemma 11, already discusses the equal-deficit two-eligible-agent process; the present **adversarial mechanism is not claimed as an invention**. The new content is the sharp five-versus-six agent universal prefix theorem and the precise seven-versus-eight arrival frontier in the pairwise unit domain. Sun, Wang and Li (arXiv:2602.18098) study fair orientations and offline proportionality; offline orientation existence cannot imply a prefix-online guarantee. The earlier unrestricted-eligibility four/five-agent bounds allow larger eligibility sets and do not imply the pairwise five-agent invariant.

## Limitations
Only items with exactly two eligible agents and identical unit values are considered. Eligibility-aware share, not an unconditional equal division of all items, is used. The six-agent lower bound requires an adaptive adversary; no oblivious lower bound is asserted. The finite six-agent enumeration certifies only the first seven rounds, while the five-agent infinite guarantee follows from a closed invariant. Literature priority remains subject to specialist comparison with the older chip-firing literature.

## References
1. S. Biburger, N. Megow and S. Shahkarami, *Online Fair Division under Eligibility Constraints*, arXiv:2610.08064v1, first posted 2026-10-06, especially Appendix C, Lemma 11.
2. Sun, Wang and Li, *Fair Orientations: Proportionality and Equitability*, arXiv:2602.18098 (2026).
3. Hopkins, McConville and Propp, *Sorting via Chip-Firing*, Proceedings of FPSAC 2017, DOI: 10.37236/6823.
