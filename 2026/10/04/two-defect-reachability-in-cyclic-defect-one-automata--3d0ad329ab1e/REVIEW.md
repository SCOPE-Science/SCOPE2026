# Same-model review

## Correctness
PASS. The proof reduces any exactly-two-\(b\) word acting on the full state set to \(ba^kba^j\). The second \(b\) lowers the rank precisely when the intermediate missing state is outside the two-element kernel class of the duplicated image. On those states, \(b\) is a bijection onto \(Q\setminus\{e,d\}\), so the oriented separation of the final two holes can be any nonzero residue except \(\rho=d-e\). Both orientations fail exactly for an antipodal pair with \(n\) even and \(\rho=n/2\). The constructive choices of \(k\) and \(j\) give length at most \(2n\).

The packaged verifier independently checks this classification, the explicit witness, and the exceptional count. It exhausts all rank-\((n-1)\) transformations for \(3\le n\le7\) and performs deterministic checks for \(8\le n\le13\). Finite computation is supplementary; the proof carries the infinite statement.

## Originality
PASS to the best of the inspected literature. Don's 2016 Proposition 15 gives \(n(n-k)\) for circular defect-one automata when the excluded-to-duplicated displacement is coprime to \(n\); this is credited as prior coverage. Casas--Volkov and Zhu give stronger all-subset conclusions for standardized completely reachable automata under additional orbit hypotheses. Hoffmann treats arbitrary rank-\((n-1)\) maps combined with primitive groups, which gives the single-cycle case when \(n\) is prime. Ferens--Szykuła give a general codimension-two upper bound of \(5n/2\) for completely reachable automata.

The surviving contribution is the exact two-occurrence classification for an arbitrary rank-\((n-1)\) map next to a cycle, including non-coprime displacement and without complete reachability, together with the sole antipodal parity obstruction. Targeted published-finding corpus searches returned the Černý special case and unrelated nearby records, not an implication-equivalent statement.

## Value
PASS. Codimension two is a structurally important and currently sharp-testing layer for reaching thresholds: recent binary completely reachable counterexamples already appear there. The result supplies a closed local criterion, an explicit reaching word, a uniform sharp \(2n\) bound in the nonexceptional class, and a precise boundary showing when two defect-one steps cannot suffice.

## Closest literature and limitations
The closest classical source is Don's circular defect-one proposition; the closest recent sources are Casas--Volkov and Zhu on standardized binary completely reachable automata. The main residual literature risk is an older equivalent formulation in circular-automata or transformation-semigroup terminology. Scientifically, the main limitation is that the antipodal exceptional targets are only ruled out for words with exactly two occurrences of the rank-\((n-1)\) letter; their reachability with more occurrences is left open here.

Same-model review: passed. Independent audit: not yet performed.
