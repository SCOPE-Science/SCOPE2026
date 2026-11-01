# A four-vacancy improving cycle on the cubic Petersen graph for diversity-seeking jump games

## Finding

The two-type diversity-seeking jump game on a connected cubic graph need not have the finite-improvement property. Specifically, the Petersen graph admits a **closed 60-move sequence of strict unilateral improving jumps** with six distinct strategic agents (three red and three blue) and four vacant vertices. No stubborn agents or weighted utilities are needed. Hence the proposed regular-degree-three potential property fails already with four vacancies. The construction answers the cubic-regular case identified as open in the relevant source's Section 5, without asserting that four vacancies or ten vertices are minimal.

## Assumptions and scope

Let \(G=(V,E)\) be the simple undirected Petersen graph, with \(V=\{0,1,\ldots,9\}\). Its 15 edges, with each unordered edge written once, are

```text
(0,1) (0,4) (0,5) (1,2) (1,6)
(2,3) (2,7) (3,4) (3,8) (4,9)
(5,7) (5,8) (6,8) (6,9) (7,9)
```

Each vertex has degree three. Distinct agents \(r_1,r_2,r_3\) have red type, and \(b_1,b_2,b_3\) have blue type. Only these six agents are present, all strategic, with no stubborn agents. The initial placement is \(r_1\) at 1, \(b_1\) at 2, \(r_2\) at 3, \(b_2\) at 4, \(r_3\) at 5, \(b_3\) at 6; vertices 0, 7, 8 and 9 are vacant.

An agent's utility at its occupied vertex equals the number of its **occupied** neighbors of the opposite type divided by the number of its **occupied** neighbors; the utility is zero when it has no occupied neighbors. One move selects any agent and sends it to any vacant vertex, subject only to its own strict utility increase. The old location becomes vacant. This is the fractional diversity-seeking (not distinct-neighbor-type-count) utility model. No best-response requirement is imposed.

## Proof

Use this ordered block of ten jumps, denoting by \(u\to v\) the relocation from source vertex \(u\) to vacant target vertex \(v\):

| Step | Jump | Moving type in first block | Utility before | Utility after |
|---|---|---|---|---|
| 1 | \(5\to0\) | red | \(0\) | \(1/2\) |
| 2 | \(1\to7\) | red | \(2/3\) | \(1\) |
| 3 | \(6\to1\) | blue | \(0\) | \(1/2\) |
| 4 | \(2\to8\) | blue | \(2/3\) | \(1\) |
| 5 | \(7\to2\) | red | \(0\) | \(1/2\) |
| 6 | \(3\to9\) | red | \(2/3\) | \(1\) |
| 7 | \(8\to3\) | blue | \(0\) | \(1/2\) |
| 8 | \(4\to5\) | blue | \(2/3\) | \(1\) |
| 9 | \(9\to4\) | red | \(0\) | \(1/2\) |
| 10 | \(0\to6\) | red | \(2/3\) | \(1\) |

Every source vertex is occupied immediately before its indicated jump, and every destination is vacant. The entries in the last two columns follow by counting the occupied neighboring vertices from the edge list, *after vacating the source* for the arriving utility. They are exact fractions. In particular every jump is strictly improving.

After the block, vertices 1 through 6 are occupied alternately **blue, red, blue, red, blue, red**, with precisely vertices 0, 7, 8, 9 vacant. Thus the configuration of agent types is the original configuration with red and blue interchanged. The rule and the block are invariant under global interchange of the two types, so executing the block again is another ten strict improving moves and restores the original type placement.

Distinct-agent identity is also respected: after two blocks, the original red labels at vertices 1, 3, 5 move respectively to vertices 3, 5, 1, and the blue labels originally at 2, 4, 6 move respectively to 4, 6, 2. This is a permutation of order three in each color class. Hence repeating the ten-jump block six times (60 strict improvements) restores the original location of **every labeled agent** and all four vacancies. This yields a genuine improving-response cycle for finite, distinct agents and proves the claim.

## Verification

Execute `python verify_cycle.py` with Python 3 (standard library only). It builds the stated graph, checks all degrees are three, initializes the **labeled** state, and replays all 60 moves. It computes each pre- and post-jump utility as an exact `Fraction`, checks the alternating inequalities \(0<1/2\) and \(2/3<1\), checks source occupancy and target vacancy at every step, and asserts exact labeled-state equality at the end. The observed output is:

```text
PASS: Petersen degree 3, 4 vacancies, 6 labeled agents,
      60 exact strictly improving jumps, labeled state restored.
```

The proof is a finite, exhaustive certificate **of the asserted 60-move cycle**, not an enumeration or classification of all possible configurations or all cubic graphs.

## Relationship to prior work

Narayanan, Sabbagh and Voudouris introduce the fractional diversity-seeking game in the May 2023 preprint and its 2025 open-access journal version. Their Theorem 5.1 establishes convergence for regular graphs with **one** vacancy. Their Theorem 5.2 constructs an improving-response cycle on a **degree-four** regular graph with **four** vacancies. Their Section 5 explicitly leaves degree-three regular graphs open. Neither prior theorem yields the degree-three, four-vacancy cycle proved here; the present graph and exact relocation sequence are different.

Narayanan, Opatrny, Tummala and Voudouris (2025 preprint, subsequent journal article) consider **variety-seeking** utilities counting the number of *different neighbor types*, rather than the fraction of unlike occupied neighbors. That model has a two-type potential theorem, whereas the present two-type fractional game cycles. Consequently their cubic example or potential statement is not the same claim nor an implication of it.

## Limitations

This is an existence counterexample. It does not show that four vacancies, ten vertices, or 60 labeled jumps are minimum, does not settle degree-four graphs with two or three vacancies, and does not imply that a pure equilibrium fails to exist. Literature overlap was examined in directly relevant full texts and semantic research-index searches, but unindexed specialized priority remains possible. The numerical verifier checks an explicitly specified finite certificate, not an infinite classification.

## References

1. L. Narayanan, Y. Sabbagh and A. A. Voudouris, *Diversity-seeking Jump Games in Networks*, arXiv:2305.17757, first publicly posted 2023-05-28. https://arxiv.org/abs/2305.17757
2. L. Narayanan, Y. Sabbagh and A. A. Voudouris, *Diversity-seeking jump games in networks*, *Autonomous Agents and Multi-Agent Systems* **39**, article 32 (2025), Sections 2 and 5, Theorems 5.1 and 5.2. https://doi.org/10.1007/s10458-025-09714-8
3. L. Narayanan, J. Opatrny, S. Tummala and A. A. Voudouris, *Variety-Seeking Jump Games on Graphs*, arXiv:2505.10005 (2025); distinct utility function. https://arxiv.org/abs/2505.10005
