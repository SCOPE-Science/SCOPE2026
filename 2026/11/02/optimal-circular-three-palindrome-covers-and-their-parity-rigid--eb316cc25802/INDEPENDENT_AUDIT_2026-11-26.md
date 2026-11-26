# Independent mathematical audit

## correctness

PASS

Every aaa requires two loop steps. For any distinct unordered pair, the two opposite-center palindromes require two separate consecutive equal-label adjacencies; its label is not the entire circle, so at least three occurrences are necessary. The resulting undirected closed-walk degrees have odd baseline at every vertex for even q. Extra loops cannot change parity, so at least q/2 extra nonloop edges are required. At equality each vertex must meet exactly one such edge, and there is no loop excess. For odd q there is no parity excess and equality forces every lower bound individually. For either parity a looped complete graph (augmented by any perfect matching for even q) is connected Eulerian; the first traversal of each pair expands to three alternations without changing endpoints, and a loop expands to two loop steps. This gives every required window, exact multiplicities and attainment of every stated profile, including q=2. The iff is explicitly among covers. `python3 /workspace/review-evidence/reproduce.py 4` independently verifies minima 8, 15 and 28 by finite state BFS starting at a completed compulsory 000 and checking both cyclic wrap windows; this does not prove the general formula.

## originality

PASS

The exact all-q length formula and matching Euler construction are duplicated in the dated 2026-11-22 catalogue record 18d0cf3a4b8f, and its proof yields the same parity equality profile. This is equivalent mathematical coverage, not merely a similar title and not present-day novelty relative to that record. It is dated later than the frozen finding's 2026-11-02 record; it does not supply evidence that the frozen claim was already known on its record date. The inspected earlier results give general formulations or different covering objectives, not this exact solution or its rigidity. This is a qualified assessment at the frozen record date, not a historical claim about who first found the theorem.

## value

PASS

The target language is the full, natural length-three palindrome family. The theorem gives the exact sampling budget for cyclic coverage and a rigid adjacency-count classification, including a parity correction that is necessary and sufficient. Knowing only that an Euler tour exists or knowing the minima for a few alphabet sizes does not recover those facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
